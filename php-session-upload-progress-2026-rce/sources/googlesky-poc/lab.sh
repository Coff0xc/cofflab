#!/usr/bin/env bash
# CVE-2026-115560 lab manager.
#   ./lab.sh up        build + start vuln (:8094) and mitigated (:8095) containers
#   ./lab.sh teardown  stop, remove containers + volumes + lab image
#   ./lab.sh logs      tail apache/php logs
set -euo pipefail
cd "$(dirname "$0")/lab"

case "${1:-}" in
  up)
    docker compose up -d --build --wait
    echo "[+] vuln-php       -> http://127.0.0.1:8094  (php_serialize + upload_progress ON)"
    echo "[+] mitigated-php  -> http://127.0.0.1:8097  (upload_progress.enabled=0)"
    ;;
  teardown|down)
    docker compose down -v --remove-orphans
    docker rmi cve-2026-115560-lab:latest 2>/dev/null || true
    echo "[+] lab torn down (containers, volumes, image removed)"
    ;;
  logs)
    docker compose logs -f
    ;;
  *)
    echo "usage: $0 up|teardown|logs" >&2
    exit 64
    ;;
esac
