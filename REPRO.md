# Reproduction methodology

Every entry in this catalog is reproduced, or attempted, in an isolated
environment. Nothing is executed on a host, and no PoC is run against a
live system. There are two reproduction paths, chosen by what the target
needs.

## Path 1: unshare sandbox (default)

A wrapper runs one command inside fresh Linux namespaces and destroys
the staging afterwards.

- Namespaces: user, mount, pid, net, ipc, uts. The sandbox runs as root
  inside its own user namespace.
- Mounts: `/home` and `/root` are hidden, `/proc` is hidden,
  `/etc/shadow`, `/etc/gshadow` and `/etc/ssh` are hidden. `/tmp` is a
  fresh tmpfs. The PoC source is bind-mounted read-only; the PoC runs
  from a writable copy in the sandbox `/tmp`. The repository is never
  visible inside.
- Network: the network namespace has no interfaces. Loopback stays down
  unless explicitly enabled for a local target.
- Capabilities: all dropped before the PoC runs, so it cannot umount
  the hiding binds, remount, chroot, ptrace, or touch the network stack.
- Staging lives under `/var/tmp` and is removed on exit. Results are
  copied to a persistent output directory by the wrapper after exit.

This path is used when the PoC needs no real vulnerable target, or when
the target can be mocked locally.

## Path 2: crun containers (real targets)

`docker run` does not work on the reproduction host, so Docker is only
used to pull and export images; containers are run directly with crun.

- Docker 29.1.3, storage driver `vfs`, `iptables: false`,
  `bridge: none`. The daemons are started manually from a shell, not
  via systemd.
- An image is exported to a rootfs, a spec is generated, and the spec
  is adjusted: `ociVersion` set to `1.0.0`, the `network` namespace
  removed (the container shares the host network namespace), and the
  terminal disabled.
- The target and the PoC run in the same container, driven by an init
  script. `crun exec` into a running container does not work here, so
  no process is added after start.
- The target binds to the host `127.0.0.1:<port>`; the PoC reaches it
  on localhost inside the same container.
- One target container at a time. Exported rootfs directories are
  removed after each run, and images are pruned regularly.

This path is used when a real vulnerable target can be built from a
public image (for example a vulnerable application, database, or
service).

## Safety audit

Every PoC source is read before it is run. Sources are classified as
safe, suspicious, or malicious/destructive. Suspicious sources are
ones whose own functionality is dual-use (for example a scanner that
takes a CIDR range, or a script that changes a default password);
they are not backdoors, credential theft, or callbacks. No source
classified malicious or destructive has been found. A source is only
run after this read-through, and only inside one of the two paths
above.

## Status meanings

- **Full** — reproduced end-to-end in an isolated sandbox.
- **Partial** — partially reproduced, or verified on a mock.
- **No target** — no vulnerable target is available to reproduce
  against.
- **Pending** — not yet reproduced.

`review.executed` in each entry's `meta.yaml` records whether the
PoC itself was executed. A custom probe or validator does not count;
only execution of the curated PoC material does.

## Environment

- Ubuntu 24.04, Docker 29.1.3, crun 1.14.1.
- Reproduction is for authorized security research and defense only.
