# php-session-upload-progress-2026-rce — PHP Session Upload Progress Serialize-Handler Mismatch RCE

| Item | Value |
| --- | --- |
| Product | PHP (ext/session upload progress) |
| CWE | CWE-502 |
| Affected | PHP with session.serialize_handler=php_binary or php_serialize in server config, application switching to php at runtime via ini_set() before session_start(), and session.upload_progress.enabled=1 (PHP default). Validated on php:8.4.27-apache. |
| Fixed | No patch as of 2026-10-24; official mitigation is session.upload_progress.enabled=0 |
| CVSS | unknown |
| Assessment | Unauthenticated RCE via session handler mismatch in lab (php:8.4.27-apache); unpatched, mitigation is disabling upload progress |

What the public material actually demonstrates: session upload progress runs pre-RINIT, before application code; when the server handler is `php_binary`/`php_serialize` but the application switches to `php` at runtime, the upload-progress data is unserialized with the wrong handler, giving unauthenticated object-injection remote code execution. The lab validates it end-to-end on `php:8.4.27-apache` — a build fully patched for PHP2Shell (CVE-2026-109618 / CVE-2026-109619) is still vulnerable.

No CVE record exists for this issue: the upstream repository calls it CVE-2026-115560, but neither NVD nor CVE.org has a record for that ID as of 2026-11-19. It is ingested as a no-CVE entry with the php.net informational advisory of 2026-10-23 as authority.

## Sources

| Directory | Upstream | License | Assessment |
| --- | --- | --- | --- |
| [sources/googlesky-poc](sources/googlesky-poc) | https://github.com/googlesky/CVE-2026-115560 | MIT | rce-local |

Fields are authoritative in [meta.yaml](meta.yaml).
