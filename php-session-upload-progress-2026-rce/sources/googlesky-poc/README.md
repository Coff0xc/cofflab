# CVE-2026-115560 — PHP session upload progress serialize-handler mismatch → RCE

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Research status: validated RCE](https://img.shields.io/badge/research-validated%20RCE-success.svg)](#validated-results-2026-10-23-php8427-apache)

Proof-of-concept for the **unpatched** PHP vulnerability disclosed in the
[php.net informational advisory of 2026-10-23](https://www.php.net/archive/2026.php#2026-10-23-1),
two days after the PHP2Shell emergency release (CVE-2026-109618 / -109619).

* **Type:** unauthenticated remote code execution via session unserialize object injection
* **Status (2026-10-24):** no patch yet — handled in the regular release cycle;
  official mitigation is `session.upload_progress.enabled=0`
* **Validated against:** `php:8.4.27-apache` (mod_php) — i.e. a build **fully
  patched for PHP2Shell** is still vulnerable to this issue

## Advisory preconditions

All three must hold (php.net, 2026-10-23):

1. `session.serialize_handler` = `php_binary` or `php_serialize` in the **server config**
2. the application switches the handler to `php` **at runtime** via
   `ini_set()` **before** `session_start()`
3. `session.upload_progress.enabled = 1` (**PHP default**)

## Root cause — verified against php-src `PHP-8.4`

Session upload progress (ext/session, the rfc1867 callback) runs **pre-RINIT**,
before any application code:

| step | source | what happens |
|---|---|---|
| write | `php_session_rfc1867_callback` → `MULTIPART_EVENT_FILE_START` → `php_rinit_session(0)` | `PS(serializer)` is resolved from the **server ini** (`php_serialize`) |
| write | `php_session_rfc1867_update()` → `php_session_flush(1)` | session file is written **immediately**, in `php_serialize` format, containing `upload_progress_<value>` as a **raw, unsanitized array key** — the value of the attacker's `PHP_SESSION_UPLOAD_PROGRESS` field. `|` is legal in a key because `php_serialize` keys are length-prefixed |
| read | application: `ini_set('session.serialize_handler','php')` → `OnUpdateSerializer` | re-points `PS(serializer)` — allowed while the session is not active |
| read | `session_start()` → `PS_SERIALIZER_DECODE_FUNC(php)` | the `php` handler decodes `key\|serialized` pairs and splits at the **first `|`** — which sits inside the attacker key — so `php_var_unserialize()` runs on attacker bytes: **arbitrary object instantiation** |
| pop | `PHP_VAR_UNSERIALIZE_DESTROY(var_hash)` | runs on the SUCCESS *and* FAILURE paths, so the gadget's `__destruct` fires **even though the overall decode returns FAILURE** (trailing session junk after the payload) |

Resulting session file (captured mid-upload from the lab, `docker exec`):

```
a:1:{s:56:"upload_progress_|O:9:"LabGadget":1:{s:3:"cmd";s:2:"id";}";a:5:{s:10:"start_time";i:1792774742;…}}
                            ^
                            the "php" handler splits here; everything after it is unserialize()d
```

### The cleanup race (why the PoC is concurrent)

With the default `session.upload_progress.cleanup=1`, `MULTIPART_EVENT_END`
deletes the progress key when the upload finishes — and **every** parse exit
path reaches `fileupload_done:` in `main/rfc1867.c`, so a client abort does not
help. The payload therefore lives in the session file **only while the upload
is in flight**. Two facts make the race deterministic in practice:

* the files save handler holds `flock(LOCK_EX)` only around each brief
  initialize→flush cycle (`php_session_flush(1)` calls `s_close`), so
  concurrent readers are not blocked for the duration of the upload;
* the producer trickles a multi-MB body (`post_max_size` caps the size, not the
  duration), keeping the window open for minutes if desired.

In the lab: a 2–4 MiB upload at 16 KiB/0.1–0.15 s gives a 13–38 s window; the
consumer wins after ~3 s every run.

### Session id adoption quirk (bonus)

The rfc1867 `MULTIPART_EVENT_FORMDATA` handler accepts `PHPSESSID` from the
**POST body** without consulting `session.use_only_cookies`, so the producer
needs no cookie. (The consumer request goes through normal `session_start()`,
which does require the cookie under the default `use_only_cookies=1`.)

## Lab

```
lab/
├── Dockerfile               php:8.4.27-apache + writable /var/www/html/p (proof drop dir)
├── docker-compose.yml
├── conf/99-vuln.ini         php_serialize + upload_progress ON (PHP defaults restated)
├── conf/99-mitigated.ini    same + session.upload_progress.enabled=0 (official mitigation)
└── src/
    ├── index.php            vulnerable app: ini_set switch to "php" + session_start() + LabGadget
    ├── noswitch.php         control endpoint: no switch → same handler read/write → harmless
    └── info.php             JSON dump of the relevant global ini values
```

`LabGadget` (a class whose `__destruct` runs `shell_exec($this->cmd)`) stands in
for any real gadget class reachable at `unserialize()` time; against a real
application the gadget comes from its dependency tree (Monolog/Guzzle/…).

## Run

```console
$ ./lab.sh up          # vuln :8094, mitigated :8097 (builds image, waits for health)
$ python3 poc.py check   --target http://127.0.0.1:8094
$ python3 poc.py exploit --target http://127.0.0.1:8094 --cmd "id"
$ ./lab.sh teardown    # containers + volumes + image removed
```

### Validated results (2026-10-23, php:8.4.27-apache)

| target | expected | result |
|---|---|---|
| `:8094/index.php` (vulnerable) | RCE | ✅ `uid=33(www-data)…` in **3.3 s** (1108 reads) — reproduced, 3.3 s again (1724 reads) |
| `:8097/index.php` (mitigation `upload_progress.enabled=0`) | no RCE | ✅ no result (89459 reads) |
| `:8094/noswitch.php` (no runtime switch) | no RCE | ✅ no result (82912 reads) |

Server-side signature on the vulnerable target while the consumer wins:

```
PHP Warning: session_start(): Failed to decode session object. Session has been destroyed in …/index.php on line 21
```

— the decode fails, but the injected object's `__destruct` has already run.

## Impact notes

* Any SAPI that parses multipart bodies (mod_php, FPM, php-cgi, FrankenPHP)
  exposes the write path; the read path only needs the runtime handler switch.
* The required gadget class is application-supplied — object injection → RCE
  impact scales with the target's dependency tree.
* Real-world exposure is narrow (the runtime `ini_set` switch is unusual),
  which is why PHP is fixing it in the regular cycle — but the feature
  combination is on-by-default on the write side.

## Mitigation (official)

```ini
session.upload_progress.enabled = 0   ; php.ini / FPM pool / server config — NOT ini_set()
```

then restart all PHP workers. Verified effective by the `:8097` control above.

## References

* php.net informational advisory, 2026-10-23 — <https://www.php.net/archive/2026.php#2026-10-23-1>
* PHP2Shell (CVE-2026-109618/-109619) advisories, 2026-10-21 — same feature,
  different bugs; this lab's base image is patched against them
* php-src `PHP-8.4`: `ext/session/session.c` (rfc1867 callback, `php` decode
  func, `OnUpdateSerializer`), `main/rfc1867.c` (`fileupload_done`)
