[English](README.md) | **中文** | [日本語](README.ja.md)

# cofflab

![scope](https://img.shields.io/badge/scope-public%20PoC%20only-blue) ![repro](https://img.shields.io/badge/repro-isolated%20sandbox-green)

Coff0xc 维护的公开 PoC 策展库，覆盖 CVE 与非 CVE 漏洞。每条记录登记产品、评分、日期、公开材料实际证明的内容，以及隔离沙箱中的复现状态。

只收已经公开的材料，入库只读、不执行；复现只在隔离环境进行。仅供授权安全研究与防御。

**复现：** ✅ 完整——隔离沙箱内端到端复现 · ◐ 部分——部分复现或在 mock 上验证 · — 无目标——无可用 vulnerable 目标 · 待复现——尚未复现。

---

## 目录

### Web / CMS (11)

| 编号 | 产品 | 评分 | 受影响版本 | 修复版本 | 判定 | CVE 状态 | 复现 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [CVE-2026-123488](CVE-2026-123488) | Craft CMS 元素搜索 | 3.1 9.8 (GHSA)；4.0 9.3 (GitHub) | 4.0.0–4.18.8 and 5.0.0–5.11.1 (MySQL/MariaDB, emulated PDO prepares) | 4.18.9 / 5.11.2 | 未认证 SQLi 写库 / 提权 | 已确认 | ◐ 部分 |
| [CVE-2026-129448](CVE-2026-129448) | Apache Roller XML-RPC | 3.1 9.8 (public claim, unverified) | Roller 4.0.0–6.1.4 (CVE-2026-82384 lists 6.1.5 only; same bug) | 6.1.6 | 框架需自备 gadget；本地 mock | 未核实 | ◐ 部分 |
| [CVE-2026-90817](CVE-2026-90817) | Vanderbilt REDCap | 3.1 9.8 (public claim, unverified) | REDCap 13.3.0+ before 16.0.49 LTS / 17.3.10 LTS / 17.4.4 | 16.0.49 LTS / 17.3.10 LTS / 17.4.4 | 发现者脚本 / 占位框架 / 批量检测 | 未核实 | ◐ 部分 |
| [CVE-2026-123751](CVE-2026-123751) | WP Duplicate | 3.1 9.8 (CISA-ADP) | WP Duplicate through 1.1.11 | unknown | 未执行的利用脚本；未在真实 WordPress 上证实 RCE | 已确认 | ◐ 部分 |
| [CVE-2026-126473](CVE-2026-126473) | OpenEMR | 4.0 9.3 (VulnCheck)；3.1 9.1 (VulnCheck) | OpenEMR < 8.4.0 (8.3.0 tested) | 8.4.0 | 实验室 Docker 中对官方 8.3.0 镜像未认证创建 FHIR Patient；8.4.0 拒绝冒号形式注册 | 已确认 | — 无目标 |
| [CVE-2026-111559](CVE-2026-111559) | Batflat CMS | 4.0 9.3 (CERT.pl) | Batflat CMS 1.2.0–1.3.7 | none (project unmaintained) | /contact 表单 SSTI 未认证 RCE；仅 curl PoC，无修复（项目已无人维护） | 已确认 | 待复现 |
| [CVE-2026-126173](CVE-2026-126173) | AutomatorWP Pro Webhooks | 3.1 9.8 (Wordfence) | AutomatorWP Pro Webhooks <= 1.4.4 | 1.4.5 | 实验室中未认证任意密码重置/管理员接管；1.4.5 修复 | 已确认 | 待复现 |
| [CVE-2026-48356](CVE-2026-48356) | Adobe Commerce / Magento | 3.1 9.3 (Adobe) | Adobe Commerce / Magento Open Source 2.4.4-2.4.9 | 2.4.9-p2 | 低权限 REST token 文件上传至 webshell RCE（实验室）；Sansec SA-2026-0027 | 已确认 | 待复现 |
| [CVE-2026-119977](CVE-2026-119977) | WordPress 核心 | 3.1 8.1 (Wordfence) | WordPress Core 4.7.0-7.1.3 | 7.1.4 | 升级窗口 TOCTOU 植入攻击者 wp-config.php；配置接管至 RCE（实验室）；已列入 KEV | 已确认 | 待复现 |
| [CVE-2026-110447](CVE-2026-110447) | Collabora Online 内置 CODE Server | 3.1 9.8 (NVD)；4.0 9.2 (MITRE) | Collabora Online Built-in CODE Server (richdocumentscode) before 26.4.303 | 26.4.303 | 经 proxy.php 未认证命令注入；1-day PoC；已列入 KEV、在野利用已确认 | 已确认 | 待复现 |
| [CVE-2026-48907](CVE-2026-48907) | Joomla! JCE | 3.1 9.8 (NVD)；4.0 10.0 (Joomla) | Joomla! JCE extension < 2.9.99.5 | 2.9.99.5 | 未认证创建 JCE 配置文件上传 PHP 并 RCE；已列入 KEV | 已确认 | 待复现 |

### AI / LLM (4)

| 编号 | 产品 | 评分 | 受影响版本 | 修复版本 | 判定 | CVE 状态 | 复现 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [CVE-2026-40217](CVE-2026-40217) | BerriAI LiteLLM | 3.1 8.8 PR:L (public README) | LiteLLM before v1.83.11 (image digest pinning required; some rebuilt tags are not vulnerable) | v1.83.11+ (RestrictedPython) | 认证后实验室 RCE，需要 API key | 已确认 | ◐ 部分 |
| [CVE-2026-130796](CVE-2026-130796) | Flowise | 4.0 8.8 (VulnCheck)；3.1 8.2 (VulnCheck) | 3.1.3-3.1.4 |  | 未认证泄露明文 MCP token；附带脚本是离线逻辑模拟 | 已确认 | ✅ 完整 |
| [CVE-2026-102895](CVE-2026-102895) | GPUStack | 3.1 9.8 (GHSA) | < 2.2.0 | 2.2.0 | 实验室验证的未认证管理员接管；在野利用为厂商报告，未经此 PoC 证实 | 已确认 | ◐ 部分 |
| [CVE-2026-59726](CVE-2026-59726) | Ruflo MCP Bridge | 3.1 10.0 (GHSA) | Ruflo < 3.16.3 (default docker-compose MCP bridge) | 3.16.3 | 经 MCP bridge terminal_execute 未认证 RCE；Exploit-DB 已验证 autopwn | 已确认 | 待复现 |

### 网络与安全 (18)

| 编号 | 产品 | 评分 | 受影响版本 | 修复版本 | 判定 | CVE 状态 | 复现 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [CVE-2026-123007](CVE-2026-123007) | F5 NGINX HTTP/2 | 4.0 9.2 (F5)；3.1 8.1 (F5) | NGINX Open Source 1.9.5–1.30.6 and 1.31.0–1.31.8 with HTTP/2 enabled | Open Source 1.30.7 / 1.31.9; NGINX Plus 37.3.0.1 / 37.0.8.1 | 触发 + 仅新鲜 Docker 的 RCE 演示 | 已确认 | — 无目标 |
| [CVE-2026-129287](CVE-2026-129287) | N-able N-central | 4.0 8.3 (N-able) | before 2026.4.1 Hotfix 3 | 2026.4.1 Hotfix 3 (build 2026.4.1.39) | 认证后带外 XXE 读文件；闭源设备，本地不可复现 | 已确认 | ◐ 部分 |
| [CVE-2026-119958](CVE-2026-119958) | Windows LDAP | 3.1 9.8 (Microsoft) | Windows 10 1607–Windows 11 26H2、Windows Server 2016–2025 | 2026 年 11 月安全更新 | 越界写 + 崩溃的实验室复现；未在真实 Windows LDAP 上证实 RCE | 已确认 | ✅ 完整 |
| [CVE-2026-123039](CVE-2026-123039) | Check Point Gaia OS | 3.1 7.8 (Check Point) | Gaia OS R81–R82.20（Quantum 网关、Force 防火墙、安全管理/日志服务器、多域、Maestro） | Jumbo Hotfix：R82.20 Take 14、R82.10 Take 52、R82 Take 132、R81.20 Take 174 | 经全局可写 socket 提权到 root 的实验室复现；未在真实 Gaia 上验证 | 已确认 | ◐ 部分 |
| [CVE-2026-123158](CVE-2026-123158) | OpenSSH sshd | 3.1 8.1 (MITRE) | OpenSSH < 10.6p2（Linux + musl libc 且无 PAM，如 Alpine Linux） | OpenSSH 10.6p2 | 绕过密码认证登录的实验室复现；无真实环境证据 | 已确认 | — 无目标 |
| [CVE-2026-123218](CVE-2026-123218) | IBM Aspera Faspex 5 | 3.1 9.8 (IBM) | Faspex 5.0.0–5.0.19 | 5.0.19 PL1（Fix Pack 1） | 仅版本检测；未证实绕过 | 已确认 | ✅ 完整 |
| [CVE-2026-111560](CVE-2026-111560) | Barracuda ESG / ADC / WAF / WSG | 4.0 8.6 (Mandiant)；3.1 7.2 (NVD) | ESG ≤ 9.4.0.27；ADC ≤ 6.4.0；WAF ≤ 11.0.1；WSG ≤ 16.1.100.100；BMA ≤ 5.5.4.0；WCC ≤ 2.2.1 | ESG 9.4.0.030；其余产品按厂商通告补丁升级 | 实验室 root 命令执行（需管理员权限）；未认证 root 需与 CVE-2026-116606 联动 | 已确认 | ◐ 部分 |
| [CVE-2026-116606](CVE-2026-116606) | Barracuda ESG | 4.0 9.3 (Mandiant)；3.1 9.8 (NVD) | ESG < 9.4.0.030 | 9.4.0.030 | 未认证配置恢复触发；root 需与 CVE-2026-111560 联动 | 已确认 | ◐ 部分 |
| [CVE-2026-19868](CVE-2026-19868) | SonicWall SonicOS | 3.1 7.5 (CISA-ADP)；3.1 7.1 (SonicWall) | Gen7 7.3.3-7015 及更早；Gen8 8.2.2-8015 及更早 | Gen7 7.3.4-7013 及更高；Gen8 8.2.3-8015 及更高 | 仅版本检测 | 已确认 | ✅ 完整 |
| [CVE-2026-129271](CVE-2026-129271) | N-able N-central Patch Management | 4.0 8.5 (N-able) | Patch Management Component < 2.14.4.5829 | 2.14.4.5829（随 N-central 2026.4.1 Hotfix 3，build 2026.4.1.39，2026-11-16） | 认证后本地提权到 root（需 ProductAdmin 凭证 + 回调） | 已确认 | — 无目标 |
| [CVE-2026-129280](CVE-2026-129280) | N-able N-central | 4.0 9.3 (N-able) | N-central < 2026.4.1 HF3 | 2026.4.1 HF3（build 2026.4.1.39，2026-11-16） | 未认证配置写入（单次操作演示，可逆） | 已确认 | ◐ 部分 |
| [CVE-2026-114713](CVE-2026-114713) | UnrealIRCd | 3.1 8.6 (GHSA) | 6.0.0–6.2.7 (5.x EOL also affected) | 6.2.7.1 / hotfix bundle-20261107 | 服务器间命令注入的实验室 PoC；非操作系统级 RCE | 已确认 | ✅ 完整 |
| [CVE-2026-116779](CVE-2026-116779) | FreeSWITCH | 3.1 9.8 (GHSA) | <= 1.11.2 | 1.11.3 (adds enable-chat-api-proto, off by default) | 实验室验证的 SIP MESSAGE 命令执行；无真实部署证据 | 已确认 | ◐ 部分 |
| [CVE-2026-119618](CVE-2026-119618) | Apache httpd mod_http2 | 3.1 8.1 (NVD)；3.1 9.8 (Red Hat) | httpd 2.4.55–2.4.70, mod_h2 2.0.8–2.0.42 | 2.4.71, mod_h2 2.0.43 | ASan/TSan 下堆损坏 + 崩溃；未证实 RCE | 已确认 | — 无目标 |
| [CVE-2026-126170](CVE-2026-126170) | Fortinet FortiManager / FortiAnalyzer | 3.1 9.8 (Fortinet) | FortiAnalyzer 8.0.0-8.0.2, 7.6.0-7.6.7; FortiAnalyzer Cloud 8.0.1-8.0.2, 7.6.0-7.6.7; FortiAnalyzer-BigData 7.6.0-7.6.2; FortiManager 8.0.0-8.0.2, 7.6.0-7.6.7; FortiManager Cloud 8.0.1-8.0.2, 7.6.0-7.6.7; FortiSASE-Sovereign 25, 25.3, 25.4, 26.2 | 8.0.3, 7.6.8, FortiAnalyzer-BigData 7.6.3 | 实验室中经 JRPC JSON 注入未认证 RCE；7.6.7 与 7.6.8 对照 | 已确认 | ✅ 完整 |
| [CVE-2026-124079](CVE-2026-124079) | rConfig Core / Pro | 4.0 9.3 (VulnCheck)；3.1 9.8 (VulnCheck) | rConfig Core >= 8.0.0, < 8.2.19; rConfig Pro < 8.4.1 | rConfig Core 8.2.19 (2026-10-27); rConfig Pro 8.4.1 | 实验室中经 Redis 支撑的 Horizon 队列投毒未认证 RCE | 已确认 | ◐ 部分 |
| [CVE-2026-121653](CVE-2026-121653) | Ivanti Endpoint Manager Core | 3.1 9.8 (Ivanti) | Ivanti EPM 2024 SU7 and prior | EPM 2024 SU8 | 实验室中未认证 SQLi → 经 Core 数据库账号执行操作系统命令 | 已确认 | ◐ 部分 |
| [CVE-2026-111585](CVE-2026-111585) | TeamViewer 客户端 | 3.1 8.8 (TeamViewer) | TeamViewer clients prior to 15.83 (15.82.6 tested) | 15.83 (bulletin TV-2026-1011) | 真实 15.82.6 二进制上的 viewer 堆溢出 + 崩溃；RCE 为宣称，崩溃已证实 | 已确认 | ◐ 部分 |

### 运行环境 / 框架 / 浏览器 (13)

| 编号 | 产品 | 评分 | 受影响版本 | 修复版本 | 判定 | CVE 状态 | 复现 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [CVE-2026-114938](CVE-2026-114938) | OpenJDK Base64（Java4Shell） | 4.0 9.2 (Calif)；3.1 8.1 (Oracle)；3.1 9.8 (Red Hat) | OpenJDK 17.0.6 and later on x86-64 with AVX-512 VBMI (17/21/25/27 lines; Oracle also lists Java 8 Performance Pack 8u511b33-perf) | vendor November 2026 CPU / OpenJDK 17.0.21.1, 21.0.13.1 and equivalent distributor builds | 触发 / 崩溃 / 泄露 / 实验；没有公开通用 RCE | 已确认 | ◐ 部分 |
| [CVE-2026-90436](CVE-2026-90436) | Apache Axis 1.x | 3.1 9.8 (CISA-ADP) | Apache Axis 1.x through 1.4 | 无修复版本（EOL；修复仅存于上游 commit 41f3b4e8） | 未认证类实例化的实验室复现；默认 classpath 上未证实 RCE | 已确认 | ◐ 部分 |
| [CVE-2024-27834](CVE-2024-27834) | WebKit (Apple) | 3.1 5.5 (NVD) | Safari < 17.5；iOS/iPadOS < 16.7.8 及 17.x < 17.5；macOS < 14.5；tvOS < 17.5；watchOS < 10.5；WebKitGTK / WPE WebKit < 2.44.2 | Safari 17.5；iOS 16.7.8 / iOS 17.5；iPadOS 16.7.8 / iPadOS 17.5；macOS Sonoma 14.5；tvOS 17.5；watchOS 10.5 | 仅分析；无可运行 PoC | 已确认 | — 无目标 |
| [CVE-2026-126187](CVE-2026-126187) | React Server Components / Next.js | 4.0 9.5 (GHSA) | react-server-dom-* 19.0.0–19.3.0; Next.js 16.0.0–16.4.0 (App Router + Cache Components) | react-server-dom-* 19.0.9 / 19.1.10 / 19.2.9 / 19.3.1; Next.js 16.4.1 | 实验室 Docker 应用中的 RCE；触发需要罕见条件 | 已确认 | ◐ 部分 |
| [CVE-2026-125350](CVE-2026-125350) | Google Chrome | 3.1 8.8 (NVD) | Chrome < 157.0.8103.50 | 157.0.8103.50 / .51 (Windows, macOS), 157.0.8103.50 (Linux, Android), Extended Stable 156.0.8078.96 | 通过回归测试文件触发渲染器崩溃；无 RCE payload | 已确认 | ✅ 完整 |
| [CVE-2026-111497](CVE-2026-111497) | Node.js Brotli | 4.0 9.2 (Google)；3.1 9.8 (NVD) | Node.js < 22.23.4, < 24.22.1, < 26.12.1; Bun < 1.4.4; Brotli 1.0.3-1.2.0 | Node.js 22.23.4 / 24.22.1 / 26.12.1; Bun 1.4.4; Brotli 1.2.1 | 经畸形 Brotli 流验证的远程 DoS；RCE 仅为分析 | 已确认 | ◐ 部分 |
| [CVE-2026-129349](CVE-2026-129349) | Apache Shiro DefaultLdapRealm | 4.0 9.1 (Apache) | Apache Shiro through 3.0.0 with DefaultLdapRealm/JndiLdapRealm and authenticationCachingEnabled=true (not the default) | 3.0.1 | 一次有效登录后认证绕过；启用缓存（非默认）时任意密码通过 | 已确认 | ◐ 部分 |
| [CVE-2026-86829](CVE-2026-86829) | Apache Airflow 核心 | 3.1 8.8 (Apache) | apache-airflow-core < 3.4.0 | 3.4.0 (apache/airflow PR #72718) | DAG 作者经 XCom 反序列化在调度器 RCE；3.3.2 实验室验证，3.4.0 干净 | 已确认 | ◐ 部分 |
| [php-session-upload-progress-2026-rce](php-session-upload-progress-2026-rce) | PHP session 上传进度 | unknown | PHP with session.serialize_handler=php_binary or php_serialize in server config, application switching to php at runtime via ini_set() before session_start(), and session.upload_progress.enabled=1 (PHP default). Validated on php:8.4.27-apache. | No patch as of 2026-10-24; official mitigation is session.upload_progress.enabled=0 | 实验室中经 session 处理器错配未认证 RCE（php:8.4.27-apache）；未修复，缓解是关闭上传进度 | 已确认 | ◐ 部分 |
| [CVE-2026-75604](CVE-2026-75604) | Windows 上的 Next.js | 3.1 9.0 (GHSA) | Next.js 13.4.0–15.5.23 and 16.0.0–16.3.2 on Windows, Pages Router + App Router without Cache Components | 15.5.24 / 16.3.3 | 经 Server Actions 加密密钥泄露未认证 RCE；需 Windows 主机与 Pages/App Router，实验室在 next@16.2.11 验证 | 已确认 | 待复现 |
| [CVE-2026-115893](CVE-2026-115893) | Wasmtime | 3.1 9.9 (GHSA) | Wasmtime < 36.0.19, 37.0.0-42.x, 43.0.0-48.0.6, 49.0.0-49.0.3 (aarch64 Cranelift) | 36.0.19, 48.0.7, 49.0.4 | aarch64 JIT 沙箱逃逸至宿主代码执行（实验室）；49.0.3 上 5/5 成功，49.0.4 拒绝 | 已确认 | 待复现 |
| [CVE-2026-109618](CVE-2026-109618) | PHP | 3.1 9.8 (NVD)；4.0 9.2 (PHP) | PHP 5.4.0-8.5.11 | 8.2.35, 8.3.36, 8.4.27, 8.5.12 | 预认证 RCE 链 A/B/C 公开（D/E 付费）；实验室在 PHP 5.4–8.5.11 验证；已列入 KEV | 已确认 | 待复现 |
| [CVE-2026-109619](CVE-2026-109619) | PHP | 3.1 8.1 (NVD)；4.0 9.2 (PHP) | PHP 5.4.0-8.5.11 | 8.2.35, 8.3.36, 8.4.27, 8.5.12 | FPM worker 跨请求残留状态 UAF/信息泄露 RCE（实验室）；已列入 KEV | 已确认 | 待复现 |

### 数据库 (3)

| 编号 | 产品 | 评分 | 受影响版本 | 修复版本 | 判定 | CVE 状态 | 复现 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [CVE-2026-118383](CVE-2026-118383) | MongoDB Server 复制 | unknown | 8.0.x before 8.0.37 (8.0.34 tested); 8.2.12 still reproduced at collection time | 8.0.37 (SERVER-138175, SERVER-138119) | 实验室 UAF 崩溃，未证实代码执行 | 已确认 | — 无目标 |
| [CVE-2026-116366](CVE-2026-116366) | ClickHouse Server | 4.0 9.5 (ClickHouse) | ClickHouse 26.3 < 26.3.62.3-lts, 26.8 < 26.8.36.3-lts, 26.9 < 26.9.27.3-stable, 26.10 < 26.10.3.7-stable | 26.3.62.3-lts / 26.8.36.3-lts / 26.9.27.3-stable / 26.10.3.7-stable (2026-10-30) | 自称未认证 RCE；实验室仅验证 differential 检测 + 武器化 DoS | 已确认 | ◐ 部分 |
| [CVE-2026-13078](CVE-2026-13078) | MongoDB Server | 3.1 7.7 (MongoDB)；4.0 6.3 (MongoDB) | MongoDB Server 7.0 before 7.0.39, 8.0 before 8.0.28, 8.2 before 8.2.12, 8.3 before 8.3.7 | 7.0.39, 8.0.28, 8.2.12, 8.3.7 | 低权限认证用户经 MozJS 模块加载器本地文件泄露；非 RCE | 已确认 | 待复现 |

### 操作系统 / 系统 / DevOps (11)

| 编号 | 产品 | 评分 | 受影响版本 | 修复版本 | 判定 | CVE 状态 | 复现 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [CVE-2024-10441](CVE-2024-10441) | Synology DSM/BSM synoplugind | 3.1 9.8 (public README, vendor advisory not verified) | DSM 6.2.4–7.2.2 and BSM/DSMUC branches before the 2024-11 smallfix | DSM 7.2.2-72806-1 / 7.2.1-69057-6 / 7.2-64570-4 / 7.1.1-42962-7 / 6.2.4-25556-8; BeeStation OS 1.1-65374; DSMUC 3.1.4-23079 | 补丁对比 + 本地验证，没有现成远程 exploit | 未核实 | ◐ 部分 |
| [CVE-2026-124194](CVE-2026-124194) | Microsoft Outlook | 3.1 6.5 (Microsoft) | Microsoft 365 Apps 版经典 Outlook、Office LTSC 2021/2024（2026-11-10 前构建） | 2026 年 11 月 10 日 Patch Tuesday Office 更新 | 仅触发 .msg 文件；未在真实 Outlook 上证实 NTLM 泄露 | 已确认 | ◐ 部分 |
| [CVE-2026-115731](CVE-2026-115731) | Puppet / OpenVox Server | 4.0 9.4 (Perforce)；3.1 9.9 (NVD) | Puppet Enterprise 2023.8.0–<2023.8.13、2025.0.0–<2025.12.1、2026.0.0–<2026.0.1；OpenVox Server ≤ 9.1.0 / ≤ 8.17.0；OpenVox Agent ≤ 9.2.0 / ≤ 8.31.1 | Puppet Enterprise 2023.8.13 / 2025.12.1 / 2026.0.1；OpenVox Server 9.2.0 / 8.18.0；OpenVox Agent 9.3.0 / 8.32.0；Puppet Core 9.1.3 / 8.22.2 | 厂商通告确认的服务器命令执行（需有效的 CA 签发客户端证书） | 已确认 | — 无目标 |
| [CVE-2026-98432](CVE-2026-98432) | Linux 内核 TCP | 3.1 9.8 (Linux kernel) | Linux kernel since 4.4 (IPv4 TCP) | 6.6.159 and later stable releases (two kfree_rcu() calls) | KASAN 验证的 inet_csk_route_req UAF 崩溃；未证实代码执行 | 已确认 | — 无目标 |
| [CVE-2026-76954](CVE-2026-76954) | Synology DSM 认证 API | 3.1 9.8 (Synology) | DSM <= 7.2.1-69057-12, 7.2.2-72806, 7.3.2-86009, 7.4.1-90080 | 7.2.1-69057-13, 7.2.2-72806-10, 7.3.2-86009-5, 7.4.1-90080-1 (Synology-SA-26:19) | 认证前堆叠 SQLi 打 syno-pam-key.db；文件读写为厂商通告说法，PoC 未证实 | 已确认 | ◐ 部分 |
| [CVE-2026-124552](CVE-2026-124552) | Webmin Shorewall 模块 | 4.0 4.8 (VulnCheck)；3.1 4.8 (VulnCheck) | Webmin through 2.670 | Post-2.670 (upstream commit 01b988dbf, webmin/webmin#2908) | 实验室中存储 XSS → root 命令执行（需 Shorewall 模块账号 + 管理员查看）；另展示未修复遍历 0day | 已确认 | ◐ 部分 |
| [CVE-2026-104623](CVE-2026-104623) | SUSE Rancher Manager | 3.1 6.3 (SUSE) | Rancher Manager 2.11.0-2.11.18, 2.12.0-2.12.14, 2.13.0-2.13.10, 2.14.0-2.14.6, 2.15.0-2.15.2 (and older) | 2.11.19 / 2.12.15 / 2.13.11 / 2.14.7 / 2.15.3 | 认证用户在管理集群拿到 shell pod；无特权 pod，API 权限受限 | 已确认 | ◐ 部分 |
| [CVE-2026-105437](CVE-2026-105437) | Git 三路合并 | 3.1 7.5 (GitLab) | Git <= 2.56.0 (and the 2.50-2.55 series) | Git 2.56.1, and 2.50.2 / 2.51.3 / 2.52.1 / 2.53.1 / 2.54.1 / 2.55.1 | 合并攻击者控制内容时堆溢出；2.56.0 SIGSEGV，2.56.1 干净 | 已确认 | ✅ 完整 |
| [CVE-2026-53362](CVE-2026-53362) | Linux 内核 IPv6 分片 | 3.1 7.8 (Linux kernel) | Linux kernel 6.12.x (CentOS Stream 10 / RHEL 10, e.g. 6.12.0-242.el10); __ip6_append_data() paged-allocation path | upstream commit 38becddc (fix in stable trees) | 实验室中在 CentOS/RHEL 10（内核 6.12.x）容器逃逸至 root；IPv4 同类 CVE-2026-53366 未覆盖 | 已确认 | 待复现 |
| [CVE-2026-97229](CVE-2026-97229) | GitLab CE/EE | 3.1 10.0 (GitLab) | GitLab CE/EE 19.2 before 19.2.8, 19.3 before 19.3.5, 19.4 before 19.4.2 | 19.2.8, 19.3.5, 19.4.2 | 实验室中未认证 CI lint 正则越界写直达 system()（git 身份，19.4.1 CE）；植入恶意 CI 配置需写权限 | 已确认 | 待复现 |
| [CVE-2026-110264](CVE-2026-110264) | GitLab CE/EE | 3.1 10.0 (GitLab) | GitLab CE/EE 7.0 before 18.11.13, 19.0 before 19.0.10, 19.1 before 19.1.9, 19.2 before 19.2.9, 19.3 before 19.3.6, 19.4 before 19.4.3 | 18.11.13, 19.0.10, 19.1.9, 19.2.9, 19.3.6, 19.4.3, 19.5.1 | 经 .org 渲染触发 Onigmo 整数溢出；仅 oracle/差分证据，未证明完整 shell | 已确认 | 待复现 |


点进 CVE 目录看完整判定和引用。
