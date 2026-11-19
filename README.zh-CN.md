[English](README.md) | **中文** | [日本語](README.ja.md)

# Coff0xc CVE 策展

Coff0xc 维护的 CVE 漏洞与公开 PoC 策展库。每条记录登记产品、评分、日期，以及公开材料实际证明的内容。

只收已经公开的材料，入库只读、不执行。仅供授权安全研究与防御。

## 目录

| CVE | 产品 | 评分 | 判定 |
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
| [CVE-2026-119958](CVE-2026-119958) | Windows LDAP | 3.1 9.8 (Microsoft) | 越界写 + 崩溃的实验室复现；未在真实 Windows LDAP 上证实 RCE |
| [CVE-2026-123039](CVE-2026-123039) | Check Point Gaia OS | 3.1 7.8 (Check Point) | 经全局可写 socket 提权到 root 的实验室复现；未在真实 Gaia 上验证 |
| [CVE-2026-123158](CVE-2026-123158) | OpenSSH sshd | 3.1 8.1 (MITRE) | 绕过密码认证登录的实验室复现；无真实环境证据 |
| [CVE-2026-123218](CVE-2026-123218) | IBM Aspera Faspex 5 | 3.1 9.8 (IBM) | 仅版本检测；未证实绕过 |
| [CVE-2026-123751](CVE-2026-123751) | WP Duplicate | 3.1 9.8 (CISA-ADP) | 未执行的利用脚本；未在真实 WordPress 上证实 RCE |
| [CVE-2026-124194](CVE-2026-124194) | Microsoft Outlook | 3.1 6.5 (Microsoft) | 仅触发 .msg 文件；未在真实 Outlook 上证实 NTLM 泄露 |
| [CVE-2026-90436](CVE-2026-90436) | Apache Axis 1.x | 3.1 9.8 (CISA-ADP) | 未认证类实例化的实验室复现；默认 classpath 上未证实 RCE |
| [CVE-2024-27834](CVE-2024-27834) | WebKit (Apple) | 3.1 5.5 (NVD) | 仅分析；无可运行 PoC |
| [CVE-2026-111560](CVE-2026-111560) | Barracuda ESG / ADC / WAF / WSG | 4.0 8.6 (Mandiant)；3.1 7.2 (NVD) | 实验室 root 命令执行（需管理员权限）；未认证 root 需与 CVE-2026-116606 联动 |
| [CVE-2026-115731](CVE-2026-115731) | Puppet / OpenVox Server | 4.0 9.4 (Perforce)；3.1 9.9 (NVD) | 厂商通告确认的服务器命令执行（需有效的 CA 签发客户端证书） |
| [CVE-2026-116606](CVE-2026-116606) | Barracuda ESG | 4.0 9.3 (Mandiant)；3.1 9.8 (NVD) | 未认证配置恢复触发；root 需与 CVE-2026-111560 联动 |
| [CVE-2026-19868](CVE-2026-19868) | SonicWall SonicOS | 3.1 7.5 (CISA-ADP)；3.1 7.1 (SonicWall) | 仅版本检测 |
| [CVE-2026-129271](CVE-2026-129271) | N-able N-central Patch Management | 4.0 8.5 (N-able) | 认证后本地提权到 root（需 ProductAdmin 凭证 + 回调） |
| [CVE-2026-129280](CVE-2026-129280) | N-able N-central | 4.0 9.3 (N-able) | 未认证配置写入（单次操作演示，可逆） |
| [CVE-2026-102895](CVE-2026-102895) | GPUStack | 3.1 9.8 (GHSA) | 实验室验证的未认证管理员接管；在野利用为厂商报告，未经此 PoC 证实 |
| [CVE-2026-114713](CVE-2026-114713) | UnrealIRCd | 3.1 8.6 (GHSA) | 服务器间命令注入的实验室 PoC；非操作系统级 RCE |
| [CVE-2026-116779](CVE-2026-116779) | FreeSWITCH | 3.1 9.8 (GHSA) | 实验室验证的 SIP MESSAGE 命令执行；无真实部署证据 |
| [CVE-2026-119618](CVE-2026-119618) | Apache httpd mod_http2 | 3.1 8.1 (NVD)；3.1 9.8 (Red Hat) | ASan/TSan 下堆损坏 + 崩溃；未证实 RCE |
| [CVE-2026-126187](CVE-2026-126187) | React Server Components / Next.js | 4.0 9.5 (GHSA) | 实验室 Docker 应用中的 RCE；触发需要罕见条件 |
| [CVE-2026-125350](CVE-2026-125350) | Google Chrome | 3.1 8.8 (NVD) | 通过回归测试文件触发渲染器崩溃；无 RCE payload |

点进 CVE 目录看完整判定和引用。
