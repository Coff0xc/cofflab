# Coff0xc CVE 策展

A curated collection of CVE vulnerabilities and public proof-of-concept material, maintained by Coff0xc. Each entry records the product, scores, dates, and what the public material actually demonstrates.

只收已经公开的材料，入库只读、不执行。仅供授权安全研究与防御。

## 目录

| CVE | 产品 | 评分 | Assessment |
| --- | --- | --- | --- |
| [CVE-2024-10441](CVE-2024-10441) | Synology DSM/BSM synoplugind | 3.1 9.8（公开 README，未复核厂商公告） | 补丁对比 + 本地验证，没有现成远程 exploit |
| [CVE-2026-40217](CVE-2026-40217) | BerriAI LiteLLM | 3.1 8.8 PR:L（公开 README） | 认证后实验室 RCE，需要 API key |
| [CVE-2026-114938](CVE-2026-114938) | OpenJDK Base64（Java4Shell） | 4.0 9.2 (Calif)；3.1 8.1 (Oracle)；3.1 9.8 (Red Hat) | 触发 / 崩溃 / 泄露 / 实验；没有公开通用 RCE |
| [CVE-2026-118383](CVE-2026-118383) | MongoDB Server 复制 | unknown | 实验室 UAF 崩溃，未证实代码执行 |
| [CVE-2026-123007](CVE-2026-123007) | F5 NGINX HTTP/2 | 4.0 9.2 (F5)；3.1 8.1 (F5) | 触发 + 仅新鲜 Docker 的 RCE 演示 |
| [CVE-2026-123488](CVE-2026-123488) | Craft CMS 元素搜索 | 3.1 9.8 (GHSA)；4.0 9.3 (GitHub) | 未认证 SQLi 写库 / 提权 |
| [CVE-2026-129448](CVE-2026-129448) | Apache Roller XML-RPC | 3.1 9.8（公开声称，未核验） | 框架需自备 gadget；本地 mock |
| [CVE-2026-90817](CVE-2026-90817) | Vanderbilt REDCap | 3.1 9.8（公开声称，未核验） | 发现者脚本 / 占位框架 / 批量检测 |
| [CVE-2026-129287](CVE-2026-129287) | N-able N-central | 4.0 8.3 (N-able) | 认证后带外 XXE 读文件；闭源设备，本地不可复现 |
| [CVE-2026-130796](CVE-2026-130796) | Flowise | 4.0 8.8 (VulnCheck)；3.1 8.2 (VulnCheck) | 未认证泄露明文 MCP token；附带脚本是离线逻辑模拟 |
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

点进 CVE 目录看完整判定和引用。
