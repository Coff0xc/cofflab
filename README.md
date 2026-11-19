# Coff0xc CVE 策展

Coff0xc 维护的 CVE 漏洞与公开 PoC 策展库。每条记录写的是我的判定：产品、评分、日期、公开材料实际证明了什么。

只收已经公开的材料，入库只读、不执行。仅供授权安全研究与防御。

## 目录

| CVE | 产品 | 评分 | 我的判定 |
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

点进 CVE 目录看完整判定和引用。
