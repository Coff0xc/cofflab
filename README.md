**English** | [中文](README.zh-CN.md) | [日本語](README.ja.md)

# Coff0xc CVE Curation

A curated collection of CVE vulnerabilities and public proof-of-concept material, maintained by Coff0xc. Each entry records the product, scores, dates, and what the public material actually demonstrates.

Only publicly available material is collected. Ingestion is read-only and never executes anything; reproduction runs only in an isolated environment. For authorized security research and defense only.

## Catalog

| ID | Product | Score | Assessment |
| --- | --- | --- | --- |
| [CVE-2024-10441](CVE-2024-10441) | Synology DSM/BSM synoplugind | 3.1 9.8 (public README, vendor advisory not verified) | Patch-diff analysis + local verification; no ready-made remote exploit |
| [CVE-2026-40217](CVE-2026-40217) | BerriAI LiteLLM | 3.1 8.8 PR:L (public README) | Authenticated lab RCE; requires an API key |
| [CVE-2026-114938](CVE-2026-114938) | OpenJDK Base64 (Java4Shell) | 4.0 9.2 (Calif)；3.1 8.1 (Oracle)；3.1 9.8 (Red Hat) | Trigger / crash / leak / lab experiment; no public general-purpose RCE |
| [CVE-2026-118383](CVE-2026-118383) | MongoDB Server replication | unknown | Lab UAF crash; code execution not demonstrated |
| [CVE-2026-123007](CVE-2026-123007) | F5 NGINX HTTP/2 | 4.0 9.2 (F5)；3.1 8.1 (F5) | Trigger + RCE demo only against a freshly started Docker instance |
| [CVE-2026-123488](CVE-2026-123488) | Craft CMS element search | 3.1 9.8 (GHSA)；4.0 9.3 (GitHub) | Unauthenticated SQLi with database writes / privilege escalation |
| [CVE-2026-129448](CVE-2026-129448) | Apache Roller XML-RPC | 3.1 9.8 (public claim, unverified) | Framework requires a self-supplied gadget; local mock only |
| [CVE-2026-90817](CVE-2026-90817) | Vanderbilt REDCap | 3.1 9.8 (public claim, unverified) | Discoverer's script / placeholder framework / bulk detection |
| [CVE-2026-129287](CVE-2026-129287) | N-able N-central | 4.0 8.3 (N-able) | Authenticated out-of-band XXE file read; closed-source appliance, not locally reproducible |
| [CVE-2026-130796](CVE-2026-130796) | Flowise | 4.0 8.8 (VulnCheck)；3.1 8.2 (VulnCheck) | Unauthenticated plaintext MCP token leak; bundled script is an offline logic simulation |
| [CVE-2026-119958](CVE-2026-119958) | Windows LDAP | 3.1 9.8 (Microsoft) | Lab repro of OOB write + crash; no RCE on real Windows LDAP |
| [CVE-2026-123039](CVE-2026-123039) | Check Point Gaia OS | 3.1 7.8 (Check Point) | Lab priv-esc to root via world-writable socket; not verified on real Gaia |
| [CVE-2026-123158](CVE-2026-123158) | OpenSSH sshd | 3.1 8.1 (MITRE) | Lab repro of password-auth bypass login; no live evidence |
| [CVE-2026-123218](CVE-2026-123218) | IBM Aspera Faspex 5 | 3.1 9.8 (IBM) | Version check only; no bypass demonstrated |
| [CVE-2026-123751](CVE-2026-123751) | WP Duplicate | 3.1 9.8 (CISA-ADP) | Unexecuted exploit script; no RCE on real WordPress proven |
| [CVE-2026-124194](CVE-2026-124194) | Microsoft Outlook | 3.1 6.5 (Microsoft) | Trigger .msg files only; no NTLM leak on real Outlook proven |
| [CVE-2026-90436](CVE-2026-90436) | Apache Axis 1.x | 3.1 9.8 (CISA-ADP) | Lab repro of unauthenticated class instantiation; no RCE on default classpath |
| [CVE-2024-27834](CVE-2024-27834) | WebKit (Apple) | 3.1 5.5 (NVD) | Analysis only; no runnable PoC |
| [CVE-2026-111560](CVE-2026-111560) | Barracuda ESG / ADC / WAF / WSG | 4.0 8.6 (Mandiant)；3.1 7.2 (NVD) | Lab root command execution (needs admin); unauth root only chained with CVE-2026-116606 |
| [CVE-2026-115731](CVE-2026-115731) | Puppet / OpenVox Server | 4.0 9.4 (Perforce)；3.1 9.9 (NVD) | Advisory-confirmed server command execution (needs valid CA-signed client cert) |
| [CVE-2026-116606](CVE-2026-116606) | Barracuda ESG | 4.0 9.3 (Mandiant)；3.1 9.8 (NVD) | Unauthenticated config-restore trigger; root only chained with CVE-2026-111560 |
| [CVE-2026-19868](CVE-2026-19868) | SonicWall SonicOS | 3.1 7.5 (CISA-ADP)；3.1 7.1 (SonicWall) | Version check only |
| [CVE-2026-129271](CVE-2026-129271) | N-able N-central Patch Management | 4.0 8.5 (N-able) | Authenticated local priv-esc to root (needs ProductAdmin creds + callback) |
| [CVE-2026-129280](CVE-2026-129280) | N-able N-central | 4.0 9.3 (N-able) | Unauthenticated config write (single-operation demo, reversible) |
| [CVE-2026-102895](CVE-2026-102895) | GPUStack | 3.1 9.8 (GHSA) | Lab-verified unauthenticated admin takeover; in-the-wild use is vendor-reported, not proven by this PoC |
| [CVE-2026-114713](CVE-2026-114713) | UnrealIRCd | 3.1 8.6 (GHSA) | Lab PoC of server-to-server command injection; not OS-level RCE |
| [CVE-2026-116779](CVE-2026-116779) | FreeSWITCH | 3.1 9.8 (GHSA) | Lab-verified SIP MESSAGE command execution; no live-deployment proof |
| [CVE-2026-119618](CVE-2026-119618) | Apache httpd mod_http2 | 3.1 8.1 (NVD)；3.1 9.8 (Red Hat) | Heap corruption + crash under ASan/TSan; RCE not proven |
| [CVE-2026-126187](CVE-2026-126187) | React Server Components / Next.js | 4.0 9.5 (GHSA) | RCE in lab Docker app; trigger requires rare conditions |
| [CVE-2026-125350](CVE-2026-125350) | Google Chrome | 3.1 8.8 (NVD) | Renderer crash via regression test file; no RCE payload |
| [CVE-2026-126473](CVE-2026-126473) | OpenEMR | 4.0 9.3 (VulnCheck)；3.1 9.1 (VulnCheck) | Unauthenticated FHIR Patient create in lab Docker against official 8.3.0 image; fixed 8.4.0 rejects colon-form registration |
| [CVE-2026-98432](CVE-2026-98432) | Linux kernel TCP | 3.1 9.8 (Linux kernel) | KASAN-verified UAF crash in inet_csk_route_req; no code execution demonstrated |
| [CVE-2026-111497](CVE-2026-111497) | Node.js Brotli | 4.0 9.2 (Google)；3.1 9.8 (NVD) | Validated remote DoS via crafted Brotli stream; RCE analysis only |
| [CVE-2026-116366](CVE-2026-116366) | ClickHouse Server | 4.0 9.5 (ClickHouse) | Unauthenticated RCE claimed; lab validates differential detection + weaponized DoS only |
| [CVE-2026-126170](CVE-2026-126170) | Fortinet FortiManager / FortiAnalyzer | 3.1 9.8 (Fortinet) | Unauthenticated RCE via JRPC JSON injection in lab; differential 7.6.7 vs 7.6.8 |
| [CVE-2026-76954](CVE-2026-76954) | Synology DSM Auth API | 3.1 9.8 (Synology) | Pre-auth stacked SQLi against syno-pam-key.db; file read/write per vendor advisory, not demonstrated by PoC |
| [CVE-2026-129349](CVE-2026-129349) | Apache Shiro DefaultLdapRealm | 4.0 9.1 (Apache) | Auth bypass after one valid login; any password accepted when caching enabled (non-default) |
| [CVE-2026-124079](CVE-2026-124079) | rConfig Core / Pro | 4.0 9.3 (VulnCheck)；3.1 9.8 (VulnCheck) | Unauthenticated RCE via Redis-backed Horizon queue poisoning in lab |
| [CVE-2026-86829](CVE-2026-86829) | Apache Airflow core | 3.1 8.8 (Apache) | DAG-author RCE in scheduler via XCom deserialization; lab-verified on 3.3.2, clean on 3.4.0 |
| [CVE-2026-121653](CVE-2026-121653) | Ivanti Endpoint Manager Core | 3.1 9.8 (Ivanti) | Unauthenticated SQLi → OS command execution via Core DB account in lab |
| [CVE-2026-124552](CVE-2026-124552) | Webmin Shorewall modules | 4.0 4.8 (VulnCheck)；3.1 4.8 (VulnCheck) | Stored XSS → root command execution in lab (needs Shorewall-module account + admin view); unpatched traversal 0day also shown |
| [CVE-2026-104623](CVE-2026-104623) | SUSE Rancher Manager | 3.1 6.3 (SUSE) | Authenticated user gets shell pod on management cluster; unprivileged pod, scoped API access |
| [CVE-2026-105437](CVE-2026-105437) | Git three-way merge | 3.1 7.5 (GitLab) | Heap overflow on merge of attacker-controlled content; SIGSEGV on 2.56.0, clean on 2.56.1 |
| [CVE-2026-111585](CVE-2026-111585) | TeamViewer clients | 3.1 8.8 (TeamViewer) | Viewer heap overflow + crash on real 15.82.6 binaries; RCE claimed, crash proven |
| [php-session-upload-progress-2026-rce](php-session-upload-progress-2026-rce) | PHP session upload progress | unknown | Unauthenticated RCE via session handler mismatch in lab (php:8.4.27-apache); unpatched, mitigation is disabling upload progress |

See each CVE directory for the full assessment and references.
