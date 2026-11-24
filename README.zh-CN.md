[English](README.md) | **中文** | [日本語](README.ja.md)

# cofflab

![scope](https://img.shields.io/badge/scope-public%20PoC%20only-blue) ![repro](https://img.shields.io/badge/repro-isolated%20sandbox-green)

Coff0xc 维护的公开 PoC 策展库，覆盖 CVE 与非 CVE 漏洞。每条记录登记产品、评分、日期、公开材料实际证明的内容，以及隔离沙箱中的复现状态。

只收已经公开的材料，入库只读、不执行；复现只在[隔离环境](REPRO.md)进行。仅供授权安全研究与防御。

**复现：**
- ✅ 完整——隔离沙箱内端到端复现
- ◐ 部分——部分复现或在 mock 上验证
- — 无目标——无可用 vulnerable 目标
- 待复现——尚未复现

---

## 目录

### Web / CMS (179)

| 编号 | 产品 | 评分 | 受影响版本 | 修复版本 | 判定 | CVE 状态 | 复现 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [CVE-2026-91618](CVE-2026-91618) | Oracle Application Development Framework (ADF) | 3.1 9.1 (Oracle) | Oracle Application Development Framework (ADF) 12.2.1.4.0 | November 2026 Critical Patch Update | Oracle ADF 安全框架未授权访问；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-40128](CVE-2026-40128) | SAP NetWeaver Application Server Java | 3.1 9.0 (SAP) | SAP NetWeaver Application Server Java (Web Container) | SAP Note 3727078 | SAP NetWeaver AS Java 登录处理未授权路径遍历；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-61532](CVE-2026-61532) | Chamilo LMS | 3.1 9.0 (GHSA) | Chamilo LMS <1.11.40 and <2.0.3 | 1.11.40 / 2.0.3 | Chamilo LMS 课程备份导入路径遍历致代码执行；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-123488](CVE-2026-123488) | Craft CMS 元素搜索 | 3.1 9.8 (GHSA)；4.0 9.3 (GitHub) | 4.0.0–4.18.8 and 5.0.0–5.11.1 (MySQL/MariaDB, emulated PDO prepares) | 4.18.9 / 5.11.2 | 未认证 SQLi 写库 / 提权 | 已确认 | ◐ 部分 |
| [CVE-2026-129448](CVE-2026-129448) | Apache Roller XML-RPC | 3.1 9.8 (public claim, unverified) | Roller 4.0.0–6.1.4 (CVE-2026-82384 lists 6.1.5 only; same bug) | 6.1.6 | 框架需自备 gadget；本地 mock | 未核实 | ◐ 部分 |
| [CVE-2026-90817](CVE-2026-90817) | Vanderbilt REDCap | 3.1 9.8 (public claim, unverified) | REDCap 13.3.0+ before 16.0.49 LTS / 17.3.10 LTS / 17.4.4 | 16.0.49 LTS / 17.3.10 LTS / 17.4.4 | 发现者脚本 / 占位框架 / 批量检测 | 未核实 | ◐ 部分 |
| [CVE-2026-123751](CVE-2026-123751) | WP Duplicate | 3.1 9.8 (CISA-ADP) | WP Duplicate through 1.1.11 | unknown | 未执行的利用脚本；未在真实 WordPress 上证实 RCE | 已确认 | ◐ 部分 |
| [CVE-2026-126473](CVE-2026-126473) | OpenEMR | 4.0 9.3 (VulnCheck)；3.1 9.1 (VulnCheck) | OpenEMR < 8.4.0 (8.3.0 tested) | 8.4.0 | 实验室 Docker 中对官方 8.3.0 镜像未认证创建 FHIR Patient；8.4.0 拒绝冒号形式注册 | 已确认 | — 无目标 |
| [CVE-2026-111559](CVE-2026-111559) | Batflat CMS | 4.0 9.3 (CERT.pl) | Batflat CMS 1.2.0–1.3.7 | none (project unmaintained) | /contact 表单 SSTI 未认证 RCE；仅 curl PoC，无修复（项目已无人维护） | 已确认 | 待复现 |
| [CVE-2026-126173](CVE-2026-126173) | AutomatorWP Pro Webhooks | 3.1 9.8 (Wordfence) | AutomatorWP Pro Webhooks <= 1.4.4 | 1.4.5 | 实验室中未认证任意密码重置/管理员接管；1.4.5 修复 | 已确认 | 待复现 |
| [CVE-2026-48356](CVE-2026-48356) | Adobe Commerce / Magento | 3.1 9.3 (Adobe) | Adobe Commerce / Magento Open Source 2.4.4-2.4.9 | 2.4.9-p2 | 低权限 REST token 文件上传至 webshell RCE（实验室）；Sansec SA-2026-0027 | 已确认 | 待复现 |
| [CVE-2026-119977](CVE-2026-119977) | WordPress 核心 | 3.1 8.1 (Wordfence) | WordPress Core 4.7.0-7.1.3 | 7.1.4 | 升级窗口 TOCTOU 植入攻击者 wp-config.php；配置接管至 RCE（实验室）；已列入 KEV | 已确认 | ◐ 部分 |
| [CVE-2026-110447](CVE-2026-110447) | Collabora Online 内置 CODE Server | 3.1 9.8 (NVD)；4.0 9.2 (MITRE) | Collabora Online Built-in CODE Server (richdocumentscode) before 26.4.303 | 26.4.303 | 经 proxy.php 未认证命令注入；1-day PoC；已列入 KEV、在野利用已确认 | 已确认 | — 无目标 |
| [CVE-2026-48907](CVE-2026-48907) | Joomla! JCE | 3.1 9.8 (NVD)；4.0 10.0 (Joomla) | Joomla! JCE extension < 2.9.99.5 | 2.9.99.5 | 未认证创建 JCE 配置文件上传 PHP 并 RCE；已列入 KEV | 已确认 | 待复现 |
| [CVE-2026-125423](CVE-2026-125423) | Gitea 自动初始化 | 3.1 8.8 (NVD)；3.1 8.5 (GHSA) | Gitea before 28.4.0 (auto_init=true, Default README template) | 28.4.0 | 实验室 RCE：auto-init 竞态 + 符号链接覆盖 hook；需建仓权限 | 已确认 | 待复现 |
| [CVE-2026-63219](CVE-2026-63219) | GeoNetwork | 3.1 8.6 (GHSA) | GeoNetwork before 4.4.12 / 4.2.17 | 4.4.12 / 4.2.17 | 未授权上传 XSLT 格式化器；脚本自称反弹 shell，本仓未执行 | 已确认 | 待复现 |
| [CVE-2026-58400](CVE-2026-58400) | GeoNetwork | 3.1 9.1 (GHSA) | GeoNetwork before 4.4.12 / 4.2.17 | 4.4.12 / 4.2.17 | Saxon 允许 XSLT 调用 Java 执行；与 63219 同链，未执行 | 已确认 | 待复现 |
| [CVE-2026-128046](CVE-2026-128046) | OpenMage LTS | 4.0 9.2 (VulnCheck)；3.1 8.1 (VulnCheck) | OpenMage magento-lts 20.17.0 before 20.18.2 and 21.0.0-beta1 before 21.0.0-beta3 | 20.18.2 / 21.0.0-beta3 | 未授权访客上传 .phar、请求可预测路径后在实验室执行；需服务器把 .phar 映射到 PHP 并对外提供 media/custom_options/ | 已确认 | 待复现 |
| [CVE-2026-69157](CVE-2026-69157) | atomic-server | 3.1 9.8 (GHSA) | atomic-server 0.29.0-0.40.1 (GHSA; NVD says to 0.40.2) |  | 未授权 /setup 邀请获 Drive 全部写权限；脚本自称，未核实 | 已确认 | 待复现 |
| [CVE-2026-130648](CVE-2026-130648) | WWBN AVideo | 3.1 8.7 (GHSA)；4.0 9.3 (NVD) | WWBN AVideo from 6.5 (GHSA; no fixed version listed) |  | javascript: videoLink 存储型 XSS；脚本自称，未核实 | 已确认 | 待复现 |
| [CVE-2026-69158](CVE-2026-69158) | atomic-server | 3.1 8.6 (GHSA) | atomic-server <= 0.40.1 |  | 未授权 /bookmark 全响应 SSRF；脚本自称，未核实 | 已确认 | 待复现 |
| [CVE-2026-69156](CVE-2026-69156) | atomic-server | 3.1 8.1 (GHSA) | atomic-server 0.30.0-0.40.1 |  | internalId 任意文件读取；PoC 的未授权说法与 GHSA 冲突 | 已确认 | 待复现 |
| [CVE-2026-100397](CVE-2026-100397) | Rucio | 3.1 9.8 (GHSA) | Rucio server < 36.4.1 (per PoC; GHSA lists branch fixes 35.9.1 / 38.6.1 / 40.4.2 / 41.1.1) | 36.4.1 (per PoC); GHSA branches 35.9.1 / 38.6.1 / 40.4.2 / 41.1.1 | SSH 质询令牌可冒充任意账户；未授权管理员冒充，未核实 | 已确认 | 待复现 |
| [CVE-2026-126967](CVE-2026-126967) | SmarterMail | 3.0 8.8 (GHSA) | SmarterMail all builds < 9735 | Build 9735 | 认证后文件存储遍历写 ASPX webshell 得 SYSTEM；脚本自称，未核实 | 已确认 | 待复现 |
| [CVE-2026-71481](CVE-2026-71481) | altcha | 3.1 7.5 (GHSA) | altcha-org/altcha (Composer) >= 2.0.0, < 2.0.3 (GHSA; PoC claims altcha-lib <= 0.5.x) | 2.0.3 (GHSA); v0.6.0 (per PoC) | 缺失或空 HMAC 签名被接受；单请求绕过 CAPTCHA，未核实 | 已确认 | 待复现 |
| [CVE-2026-1492](CVE-2026-1492) | User Registration & Membership 插件 | 3.1 9.8 (Wordfence) | User Registration & Membership ≤ 5.1.2 | 5.1.3 | 未认证通过会员注册 role 参数创建管理员账号；5.1.3 修复 | 已确认 | 待复现 |
| [CVE-2026-129493](CVE-2026-129493) | Bolo 博客 | 4.0 8.7 (VulnCheck) | Bolo (bolo-solo) 1.7–2.6.4 | none (unfixed upstream) | 未认证经公开 GET /articles 泄露文章查看密码 | 已确认 | 待复现 |
| [CVE-2026-129494](CVE-2026-129494) | CloudPaste | 4.0 8.7 (VulnCheck) | CloudPaste 1.1.0–1.9.1 | none (unfixed upstream) | 未认证经 POST /api/proxy/link 泄露 WebDAV 存储凭证 | 已确认 | 待复现 |
| [CVE-2026-129492](CVE-2026-129492) | Bolo 博客 | 4.0 5.3 (VulnCheck) | Bolo (bolo-solo) 1.7–2.6.4 | none (unfixed upstream) | 未认证存储型 XSS（commentOriginalCommentName），可盗会话 | 已确认 | 待复现 |
| [CVE-2026-129491](CVE-2026-129491) | forum-java | 4.0 5.1 (VulnCheck) | forum-java 20f7e68–63152c4 | none (unfixed upstream) | 已认证存储型 XSS（评论回复框），可盗会话 | 已确认 | 待复现 |
| [CVE-2026-130354](CVE-2026-130354) | phpMyFAQ | 4.0 6.9 (VulnCheck) | phpMyFAQ 4.1.0–4.1.11 | 4.1.12 | 未认证经 WebAuthn 注册直接创建已激活账号，绕过人工审核与域名白名单 | 已确认 | 待复现 |
| [CVE-2026-130347](CVE-2026-130347) | phpMyFAQ | 4.0 6.3 (VulnCheck) | phpMyFAQ before 4.1.12 (4.2.0-alpha before 4.2.0-RC.2) | 4.1.12 / 4.2.0-RC.2 | 密码重置绕过外部身份（OIDC/LDAP/SSO）账号认证，跳过 IdP MFA | 已确认 | 待复现 |
| [CVE-2026-110960](CVE-2026-110960) | Auth Armor 插件 | 3.1 9.8 (GHSA) | Auth Armor ≤ 1.0.3 | unknown | 未认证经泄露的 API 凭证与注册重置接管账号；修复版本未标明 | 已确认 | 待复现 |
| [CVE-2026-126269](CVE-2026-126269) | NocoDB | 4.0 9.3 (VulnCheck) | NocoDB < 2026.09.0 | 2026.09.0 | 附件 MIME 白名单子串匹配放行 text/html，同源渲染存储型 XSS；2026.09.0 修复 | 已确认 | 待复现 |
| [CVE-2026-126274](CVE-2026-126274) | NocoDB | 4.0 9.3 (VulnCheck) | NocoDB < 2026.08.1 | 2026.08.1 | 表/列标题经 innerHTML 渲染进删除对话框，存储型 XSS；2026.08.1 修复 | 已确认 | 待复现 |
| [CVE-2026-126273](CVE-2026-126273) | NocoDB | 4.0 9.2 (VulnCheck) | NocoDB < 2026.09.0 | 2026.09.0 | 首个未认证注册经未完成管理员引导认领超级管理员；2026.09.0 修复 | 已确认 | 待复现 |
| [CVE-2026-126937](CVE-2026-126937) | Zipline | 4.0 9.2 (VulnCheck); 3.1 8.1 (GHSA) | Zipline ≤ 4.6.4 | 4.6.5 | 初始配置 TOCTOU 竞态可建多个 SUPERADMIN；实验有据，未核实 | 已确认 | 待复现 |
| [CVE-2026-124020](CVE-2026-124020) | Control Web Panel | 4.0 9.2 (VulnCheck); 3.1 8.1 (GHSA) | CWP < 1.30.6 (CWP and CWPpro) | 1.30.6 | Host 头密码重置投毒窃取恢复码；账户接管，RCE 自称，未核实 | 已确认 | 待复现 |
| [CVE-2026-119258](CVE-2026-119258) | Swipe WordPress plugin | 3.1 8.1 (GHSA) | Swipe WordPress plugin <= 1.4 | no vendor patch at disclosure | 未授权 AJAX 处理器为任意活跃会话发会话 cookie；管理员接管，未核实 | 已确认 | 待复现 |
| [CVE-2026-100105](CVE-2026-100105) | Grafana | 3.1 7.7 (GHSA) | Grafana 12.4.0–12.4.13, 13.0.0–13.0.11, 13.1.0–13.1.8, 13.2.0–13.2.4 | 12.4.14 / 13.0.12 / 13.1.9 / 13.2.5 | 联系点授权绕过（schema 降级）；告警载荷被改道，实验有据 | 已确认 | 待复现 |
| [CVE-2026-129357](CVE-2026-129357) | Magma NMS | 4.0 2.1 (VulnDB); 3.1 6.3 (VulnDB) | Magma <= 1.9.0 | no upstream fix (synthetic remediation in lab) | host 组织只读成员一次 POST 制造 SUPERUSER；实验有据 | 已确认 | 待复现 |
| [CVE-2026-131850](CVE-2026-131850) | ILIAS | 4.0 8.6 (VulnCheck) | ILIAS 11.0 - 11.5.x | 11.6 | 管理员 ORDER BY 注入（注册码表）；布尔探针与盲注提取，未核实 | 已确认 | 待复现 |
| [CVE-2026-13447](CVE-2026-13447) | MStore API | 3.1 9.8 (Wordfence) | MStore API <= 4.20.0 (lab 4.18.4) | 4.21.1 | 未认证 JWT 伪造接管管理员；签名从不校验，实验室 4.18.4 已验证 | 已确认 | 待复现 |
| [CVE-2026-13355](CVE-2026-13355) | Meta Box AIO | 3.1 9.8 (Wordfence) | Meta Box AIO <= 3.11.0; MB Frontend Submission <= 4.5.6; MB User Profile <= 3.11.0 | 3.12.0 | 未认证经前端提交链创建管理员账号；须公开 mbfs 表单，未核实 | 已确认 | 待复现 |
| [CVE-2026-1357](CVE-2026-1357) | WPvivid 备份迁移 | 3.1 9.8 (Wordfence) | WPvivid Backup & Migration <= 0.9.123 | 0.9.124 | 未认证经 RSA 失效开放与路径穿越上传任意 PHP；须已生成的 API 令牌，Docker 实验室 RCE | 已确认 | 待复现 |
| [CVE-2026-133117](CVE-2026-133117) | Product Feed for WooCommerce | 4.0 8.8 (VulnCheck); 3.1 8.2 (VulnCheck) | WebToffee Product Feed before 2.4.4 | 2.4.4 | 硬编码 cron salt 致未授权触发管理操作，未核实 | 已确认 | 待复现 |
| [CVE-2026-133092](CVE-2026-133092) | TeamCity | 3.1 8.8 (JetBrains) | JetBrains TeamCity before 2026.2.2, 2026.1.6 | 2026.2.2 / 2026.1.6 | Git 子模块 URL 致远程代码执行（检测型 PoC，未核实） | 已确认 | 待复现 |
| [CVE-2026-133086](CVE-2026-133086) | TeamCity | 3.1 8.8 (JetBrains) | JetBrains TeamCity before 2026.2.2, 2026.1.6 | 2026.2.2 / 2026.1.6 | Kotlin DSL 沙箱 URL 流处理器致远程代码执行（检测型 PoC，未核实） | 已确认 | 待复现 |
| [CVE-2026-133087](CVE-2026-133087) | TeamCity | 3.1 8.8 (JetBrains) | JetBrains TeamCity before 2026.2.2, 2026.1.6 | 2026.2.2 / 2026.1.6 | Kotlin DSL 沙箱时区回调致远程代码执行（检测型 PoC，未核实） | 已确认 | 待复现 |
| [CVE-2026-133172](CVE-2026-133172) | cozy-stack | 4.0 8.7 (VulnCheck); 3.1 8.8 (VulnCheck) | cozy-stack before 1.6.69 | 1.6.69 | 共享盘移动越权致跨租户文件读取，未核实 | 已确认 | 待复现 |
| [CVE-2026-133234](CVE-2026-133234) | stoatchat | 4.0 8.7 (VulnCheck); 3.1 7.5 (VulnCheck) | stoatchat before 0.16.5 | 0.16.5 | JXL 解码无界致内存耗尽拒绝服务，未核实 | 已确认 | 待复现 |
| [CVE-2026-133235](CVE-2026-133235) | Tandoor Recipes | 4.0 8.3 (VulnCheck); 3.1 7.7 (VulnCheck) | Tandoor Recipes before 2.7.4 | 2.7.4 | Nextcloud WebDAV 客户端 SSRF 可达内网，未核实 | 已确认 | 待复现 |
| [CVE-2026-133173](CVE-2026-133173) | WatchAlert | 4.0 7.1 (VulnCheck); 3.1 6.5 (VulnCheck) | WatchAlert 2.0.0 through 3.9.20 | 3.9.21 | 跨租户 IDOR 泄露监控凭据，未核实 | 已确认 | 待复现 |
| [CVE-2026-133113](CVE-2026-133113) | Gogs | 4.0 7.1 (VulnCheck); 3.1 6.5 (VulnCheck) | Gogs through 0.14.4 | 0.14.5 | PR 合并 API 绕过受保护分支，未核实 | 已确认 | 待复现 |
| [CVE-2026-133114](CVE-2026-133114) | WooCommerce Side Cart | 4.0 5.3 (VulnCheck); 3.1 4.3 (VulnCheck) | Caddy WooCommerce Side Cart 3.0.0 before 3.2.1 | 3.2.1 | saved-items 端点缺失授权泄露非公开商品数据，未核实 | 已确认 | 待复现 |
| [CVE-2026-133080](CVE-2026-133080) | TeamCity | 3.1 8.8 (JetBrains) | JetBrains TeamCity before 2026.2.2, 2026.1.6 | 2026.2.2 / 2026.1.6 | 经 Maven 仓库设置远程代码执行；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-133015](CVE-2026-133015) | TeamCity | 3.1 8.8 (JetBrains) | JetBrains TeamCity before 2026.2.1, 2026.1.5 | 2026.2.1 / 2026.1.5 | 经 Kotlin DSL 启动类路径库远程代码执行；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-133016](CVE-2026-133016) | TeamCity | 3.1 8.8 (JetBrains) | JetBrains TeamCity before 2026.2.1, 2026.1.5 | 2026.2.1 / 2026.1.5 | 经 Kotlin DSL 脚本定义远程代码执行；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-133018](CVE-2026-133018) | TeamCity | 3.1 8.8 (JetBrains) | JetBrains TeamCity before 2026.2.1, 2026.1.5 | 2026.2.1 / 2026.1.5 | 经 Kotlin DSL UI 补丁回调远程代码执行；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-133019](CVE-2026-133019) | TeamCity | 3.1 8.8 (JetBrains) | JetBrains TeamCity before 2026.2.1, 2026.1.5 | 2026.2.1 / 2026.1.5 | 经 Kotlin DSL 上下文参数回调远程代码执行；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-133027](CVE-2026-133027) | TeamCity | 3.1 8.8 (JetBrains) | JetBrains TeamCity before 2026.2.1, 2026.1.5 | 2026.2.1 / 2026.1.5 | 经令牌认证用户名处理提权；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-133089](CVE-2026-133089) | TeamCity | 3.1 8.1 (JetBrains) | JetBrains TeamCity before 2026.2.2, 2026.1.6 | 2026.2.2 / 2026.1.6 | TFS 助手进程未认证命令服务；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-22309](CVE-2026-22309) | JTL-Shop | 3.1 9.3 (JTL); 4.0 8.6 (JTL) | JTL-Shop 5.6.0-5.8.3 | 5.8.4 / 5.7.6 / 5.6.6 (2026-11-12) | 经访客跟踪爬虫 User-Agent 存储型 XSS；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-91115](CVE-2026-91115) | silverstripe-framework | 3.1 8.8 (GHSA) | Silverstripe Framework 6.0.0-6.2.12 | 6.2.13 | Silverstripe i18nTextCollectorTask 不安全类实例化；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-133095](CVE-2026-133095) | TeamCity | 3.1 8.1 (JetBrains) | JetBrains TeamCity before 2026.2.2, 2026.1.6 | 2026.2.2 / 2026.1.6 | TeamCity Hub 集成设置 CSRF；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-133017](CVE-2026-133017) | TeamCity | 3.1 8.0 (JetBrains) | JetBrains TeamCity before 2026.2.1, 2026.1.5 | 2026.2.1 / 2026.1.5 | 经 TeamCity Git VCS 根设置远程代码执行；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-72898](CVE-2026-72898) | Metabase | 3.1 10.0 (GHSA); 4.0 10.0 (GHSA) | Metabase 58.0-<58.24, 59.0-<59.21, 60.0-<60.17, 61.0-<61.11, 62.0-<62.9, 63.0-<63.5 | 58.24 / 59.21 / 60.17 / 61.11 / 62.9 / 63.5 | 未授权 SQL 注入致管理员接管；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-21962](CVE-2026-21962) | Oracle HTTP Server | 3.1 10.0 (Oracle) | Oracle HTTP Server 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0 | Oracle Critical Patch Update January 2026 | Oracle HTTP Server / WebLogic 代理插件身份验证绕过；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-105899](CVE-2026-105899) | ColdFusion | 3.1 10.0 (Adobe) | Adobe ColdFusion 2025 before Update 14, 2023 before Update 26 | 2025 Update 14 / 2023 Update 26 (APSB26-144) | ColdFusion 任意文件上传远程代码执行；检测型 PoC，未核实 | 已确认 | ◐ 部分 |
| [CVE-2026-133083](CVE-2026-133083) | TeamCity | 3.1 8.0 (JetBrains) | JetBrains TeamCity before 2026.2.2, 2026.1.6 | 2026.2.2 / 2026.1.6 | TeamCity Server Health 报告存储型 XSS；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-133091](CVE-2026-133091) | TeamCity | 3.1 8.0 (JetBrains) | JetBrains TeamCity before 2026.2.2, 2026.1.6 | 2026.2.2 / 2026.1.6 | TeamCity 用户页面存储型 XSS；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-22310](CVE-2026-22310) | JTL-Shop | 3.1 8.0 (JTL); 4.0 7.6 (JTL) | JTL-Shop 5.5.0-5.8.3 | 5.8.4 / 5.7.6 / 5.6.6 / 5.5.5 (2026-11-11) | JTL-Shop 404 重定向存储型 XSS；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-106622](CVE-2026-106622) | ColdFusion | 3.1 10.0 (Adobe) | Adobe ColdFusion 2025 before Update 14, 2023 before Update 26 | 2025 Update 14 / 2023 Update 26 (APSB26-144) | ColdFusion 服务端请求伪造；检测型 PoC，未核实 | 已确认 | ◐ 部分 |
| [CVE-2026-106624](CVE-2026-106624) | ColdFusion | 3.1 10.0 (Adobe) | Adobe ColdFusion 2025 before Update 14, 2023 before Update 26 | 2025 Update 14 / 2023 Update 26 (APSB26-144) | ColdFusion 代码注入远程代码执行；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-22308](CVE-2026-22308) | JTL-Shop | 3.1 9.3 (ENISA); 4.0 8.6 (ENISA) | JTL-Shop 5.0.0-5.8.3 | 5.8.4 / 5.7.6 / 5.6.6 / 5.5.5 (JTL advisory 2026-11-12) | JTL-Shop OPC 预览模式反射 XSS；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-130158](CVE-2026-130158) | RepoManager | 3.1 9.0 (GitHub) | RepoManager <5.13.3 | 5.13.3 | RepoManager 存储型 XSS；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-130236](CVE-2026-130236) | Auth0 Authorization Extension | 3.1 8.5 (Okta) | Auth0 Authorization Extension <2.13 | 2.13 | Auth0 授权扩展认证绕过与规则注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-129048](CVE-2026-129048) | WP Photo Album Plus | 3.1 9.9 (Patchstack) | WP Photo Album Plus <=9.3.06.003 | 9.3.07.001 | WP Photo Album Plus 远程代码包含；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-14492](CVE-2026-14492) | WP Duplicate – WordPress Migration Plugin | 3.1 9.8 (Wordfence) | WP Duplicate <=1.1.11 | No known patch | WP Duplicate 未授权任意文件上传致 RCE；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-130754](CVE-2026-130754) | LaraDashboard | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | LaraDashboard <=1.5.4 | No fix released (latest 1.5.4) | LaraDashboard OAuth 登录未验邮箱致任意账号接管；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2023-54422](CVE-2023-54422) | iDocView | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | iDocView <13.10.1_20231115 | 13.10.1_20231115 | iDocView /html/2word 未授权文件上传致 RCE；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2023-54419](CVE-2023-54419) | nginxWebUI | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | nginxWebUI 3.0.0-3.5.7 | 3.5.8 | nginxWebUI 认证绕过致 runCmd 命令执行；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2022-51027](CVE-2022-51027) | MeterSphere | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | MeterSphere 1.13.0-1.14.6 / 1.15.0-1.16.3 | 1.14.7 / 1.16.4 | MeterSphere 预认证插件接口代码注入致 RCE；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2021-48025](CVE-2021-48025) | OpenSNS | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | OpenSNS 3.2.1 | No known patch | OpenSNS shareBox 未授权代码注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2021-48023](CVE-2021-48023) | Weaver E-cology | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | Weaver E-cology 9.0 | No known patch | 泛微 E-cology uploadOperation.jsp 未授权任意文件上传；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2018-25443](CVE-2018-25443) | Baidu UEditor | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | Baidu UEditor 1.4.0-1.4.3.3 | No known patch | 百度 UEditor catchimage 未授权文件上传；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-114516](CVE-2026-114516) | Etherpad | 3.1 9.8 (GHSA) | Etherpad 1.8.14-3.3.2 | 3.3.3 | Etherpad 预认证路径遍历致任意文件读取；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-77369](CVE-2026-77369) | Daptin | 3.1 9.6 (GHSA) | Daptin 0.11.4-0.12.29 | 0.12.30 | Daptin YJS 协同端点越权读写受限行内容；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-71499](CVE-2026-71499) | cf-manager | 3.1 10 (GHSA) | cf-manager <1.1.2 | 1.1.2 | cf-manager SSRF 致任意 Worker 代码执行；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-77367](CVE-2026-77367) | Daptin | 3.1 9.4 (GHSA) | Daptin <0.12.30 | 0.12.30 | Daptin sort 参数未授权 SQL 注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-123058](CVE-2026-123058) | JTL-Shop | 4.0 9.2 (ENISA); 3.1 9 (ENISA) | JTL-Shop 5.5.0-5.5.4 / 5.6.0-5.6.5 / 5.7.0-5.7.5 / 5.8.0-5.8.3 | 5.5.5 / 5.6.6 / 5.7.6 / 5.8.4 | JTL-Shop 未锁定 Web 安装器致未授权接管；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-110009](CVE-2026-110009) | Unzer Payments | 3.1 9.8 (Wordfence) | Unzer Payments <=2.2.1 | 无已知补丁（Wordfence 2026-11-18：Patched? No） | Unzer Payments 未授权认证绕过致账户接管；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-110811](CVE-2026-110811) | Trust Payments Gateway for WooCommerce (JavaScript Library) | 3.1 9.8 (Wordfence) | Trust Payments Gateway for WooCommerce (JavaScript Library) <=1.3.8 | 无已知补丁（Wordfence 2026-11-18：Patched? No） | Trust Payments Gateway 未授权认证绕过致管理员接管；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-124990](CVE-2026-124990) | Masteriyo LMS – LMS Course Builder, Quizzes & Certificates | 3.1 9.8 (Wordfence) | Masteriyo LMS <=3.5.1 | 3.5.2 | Masteriyo LMS PHP 对象注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-130735](CVE-2026-130735) | Grav | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | Grav 2.0.0 to <2.2.18 | 2.2.18 | Grav Twig 注入致代码执行；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-55506](CVE-2026-55506) | Wavelog | 3.1 9.6 (GHSA) | Wavelog <2.5 | 2.5 | Wavelog QSL 图片文件名路径遍历致任意文件删除；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-130156](CVE-2026-130156) | Bazarr | 3.1 9.4 (GHSA) | Bazarr <1.6.3-beta.11 | 1.6.3-beta.11 | Bazarr 字幕操作路径遍历致任意文件读写；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-55508](CVE-2026-55508) | Wavelog | 3.1 9.4 (GHSA) | Wavelog <2.5 | 2.5 | Wavelog OQRS 未授权 SQL 注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-130160](CVE-2026-130160) | RepoManager | 3.1 8.8 (GHSA) | RepoManager <5.13.3 | 5.13.3 | RepoManager 已认证 OS 命令注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-132906](CVE-2026-132906) | TeamCity | 3.1 8.8 (JetBrains) | TeamCity <2026.2 / <2026.1.4 / <2025.11.8 | 2026.2 / 2026.1.4 / 2025.11.8 | TeamCity Kotlin DSL 沙箱逃逸致 RCE；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-132909](CVE-2026-132909) | TeamCity | 3.1 8.8 (JetBrains) | TeamCity <2026.2 / <2026.1.4 / <2025.11.8 | 2026.2 / 2026.1.4 / 2025.11.8 | TeamCity Mercurial 仓库内容致 RCE；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-132917](CVE-2026-132917) | TeamCity | 3.1 8.8 (JetBrains) | TeamCity <2026.2 / <2026.1.4 / <2025.11.8 | 2026.2 / 2026.1.4 / 2025.11.8 | TeamCity Kotlin DSL 文件写入绕过致 RCE；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-133476](CVE-2026-133476) | Dolibarr | 3.1 8.8 (MITRE) | Dolibarr <24.0.3 | 24.0.3 | Dolibarr SQL 过滤绕过致账户接管；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-125061](CVE-2026-125061) | JTL PayPal Checkout plugin | 4.0 8.5 (JTL); 3.1 8.7 (JTL) | JTL PayPal Checkout plugin 1.2.0–2.3.1 | 2.3.2 / 2.2.2 | JTL PayPal Checkout 插件存储型 XSS；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-122676](CVE-2026-122676) | PublishPress Authors | 3.1 8.5 (Patchstack) | PublishPress Authors <=4.18.0 | 4.20.0 | PublishPress Authors 盲注 SQL 注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-132913](CVE-2026-132913) | TeamCity | 3.1 8.4 (JetBrains) | TeamCity <2026.2 / <2026.1.4 / <2025.11.8 | 2026.2 / 2026.1.4 / 2025.11.8 | TeamCity P4 代码评审存储型 XSS；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-103035](CVE-2026-103035) | TeamPass | 3.1 8.3 (GHSA) | TeamPass <3.2.1.2 | 3.2.1.2 | TeamPass 文件夹越权致凭据子树被盗；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-125060](CVE-2026-125060) | JTL-Shop | 4.0 8.8 (JTL); 3.1 8.2 (JTL) | JTL-Shop 5.2.0–5.8.3 | 5.8.4 / 5.7.6 / 5.6.6 / 5.5.5 | JTL-Shop 结账配送地址 IDOR；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-59988](CVE-2026-59988) | django-docutils | 3.1 8.2 (GHSA) | django-docutils <0.30.0 | 0.30.0 | django-docutils 未受信 RST 渲染致文件读/SSRF/存储型 XSS；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-103026](CVE-2026-103026) | Paymenter | 3.1 8.1 (GHSA) | Paymenter <1.5.7 | 1.5.7 | Paymenter Livewire 确认动作越权改服务器状态；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-132892](CVE-2026-132892) | TeamCity | 3.1 8.1 (JetBrains) | TeamCity <2026.2 | 2026.2 | TeamCity 授权流程提权；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-132907](CVE-2026-132907) | TeamCity | 3.1 8.1 (JetBrains) | TeamCity <2026.2 / <2026.1.4 / <2025.11.8 | 2026.2 / 2026.1.4 / 2025.11.8 | TeamCity 项目查看者重定向父项目 GitHub App 凭据；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-129056](CVE-2026-129056) | Authorizer | 3.1 9.8 (Patchstack) | Authorizer <3.17.2 | 3.17.2 | Authorizer 权限分配不当致提权；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-89095](CVE-2026-89095) | Shortcodes and extra features for Phlox theme | 3.1 8.1 (Wordfence) | Shortcodes and extra features for Phlox theme <=2.17.22 | 2.17.24 | Phlox 主题附加功能插件本地文件包含；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-120556](CVE-2026-120556) | Toocheke Companion | 3.1 8.1 (Wordfence) | Toocheke Companion <=2.38 | 2.39 | Toocheke Companion 缺失授权致任意文章/附件删除；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-131795](CVE-2026-131795) | Aora | 3.1 8.1 (Patchstack) | Aora <=1.3.5 | 1.3.24 | Aora 主题 PHP 本地文件包含；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-132903](CVE-2026-132903) | TeamCity | 3.1 8.1 (JetBrains) | TeamCity <2026.2 / <2026.1.4 / <2025.11.8 | 2026.2 / 2026.1.4 / 2025.11.8 | TeamCity 云代理实例启停越权；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-109555](CVE-2026-109555) | WP STAGING / WP STAGING Pro | 3.1 8.0 (Wordfence) | WP STAGING <=4.17.0 / WP STAGING Pro <=6.17.0 | 4.18.0 / 6.18.0 | WP STAGING PHP 对象注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-132914](CVE-2026-132914) | TeamCity | 3.1 8.0 (JetBrains) | TeamCity <2026.2 / <2026.1.4 / <2025.11.8 | 2026.2 / 2026.1.4 / 2025.11.8 | TeamCity Issue Log 标签页存储型 XSS；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-133500](CVE-2026-133500) | Gladys Assistant | 4.0 8.5 (VulDB); 3.1 9.1 (VulDB) | Gladys Assistant <=4.71.0 | 4.72.0 | Gladys Assistant 备份恢复接口操作系统命令注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-133501](CVE-2026-133501) | Gladys Assistant | 4.0 8.5 (VulDB); 3.1 9.0 (VulDB) | Gladys Assistant <=4.71.0 | 4.72.0 | Gladys Assistant 备份恢复接口路径遍历；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-128915](CVE-2026-128915) | InstaWP Connect | 3.1 8.5 (Patchstack) | InstaWP Connect <=0.1.4.4 | 0.1.4.5 | InstaWP Connect 盲注 SQL 注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-130010](CVE-2026-130010) | Chatterbug Forms | 3.1 8.1 (Wordfence) | Chatterbug Forms <=1.1 | 1.2 | Chatterbug Forms 未授权任意文件删除；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-120681](CVE-2026-120681) | Mang Board | 3.1 9.1 (Wordfence) | Mang Board <=2.4.7 | 2.4.8 | Mang Board 未授权删除任意看板帖子；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-125085](CVE-2026-125085) | Nexter Extension | 3.1 8.8 (Wordfence) | Nexter Extension <=4.9.0 | 4.9.1 | Nexter Extension 权限提升至管理员；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-118522](CVE-2026-118522) | Video & Photo Gallery for Ultimate Member | 3.1 8.1 (Wordfence) | Video & Photo Gallery for Ultimate Member <=1.1.4 | 1.1.5 | Video & Photo Gallery for Ultimate Member 任意文件删除；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-126716](CVE-2026-126716) | Mega Forms | 3.1 8.1 (Wordfence) | Mega Forms <=1.7.9 | 1.8.0 | Mega Forms 未授权任意文件删除；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-129073](CVE-2026-129073) | miniorange-otp-verification | 3.1 9.8 (Patchstack) | miniorange-otp-verification <=5.6.1 | 5.6.2 | miniOrange OTP 验证插件旁路身份验证；检测型 PoC、未核实 | 已确认 | 待复现 |
| [CVE-2026-15826](CVE-2026-15826) | User Profile Builder | 3.1 9.8 (Wordfence) | User Profile Builder <=3.16.4 | 3.16.5 | User Profile Builder 类型混淆未授权身份验证绕过；检测型 PoC、未核实；Wordfence 报告有拦截攻击 | 已确认 | 待复现 |
| [CVE-2026-129039](CVE-2026-129039) | Newsletters | 3.1 9.8 (Patchstack) | Newsletters <= 4.18.2 | 4.18.3 | Newsletters 反序列化对象注入；检测型 PoC、未核实 | 已确认 | 待复现 |
| [CVE-2026-129043](CVE-2026-129043) | Newsletters | 3.1 9.3 (Patchstack) | Newsletters <= 4.18.2 | 4.18.3 | Newsletters SQL 注入；检测型 PoC、未核实 | 已确认 | 待复现 |
| [CVE-2026-14914](CVE-2026-14914) | Tegsoft Contact Center | 3.1 10.0 (USOM) | Tegsoft Contact Center before latest-202611161510 | latest-202611161510 | Tegsoft Contact Center 任意文件上传致 Web Shell；检测型 PoC、未核实 | 已确认 | 待复现 |
| [CVE-2026-80188](CVE-2026-80188) | BuddyBoss Addons | 3.1 9.8 (Wordfence) | BuddyBoss Addons <= 1.2.1 | 1.2.2 | BuddyBoss Addons 未验证社交登录身份令牌导致未授权账户接管；检测型 PoC、未核实 | 已确认 | 待复现 |
| [CVE-2025-42884](CVE-2025-42884) | SAP NetWeaver Enterprise Portal | 3.1 6.5 (SAP) | SAP NetWeaver Enterprise Portal EP-BASIS 7.50 / EP-RUNTIME 7.50 | Per SAP Note 3660969 | SAP NetWeaver Enterprise Portal JNDI 注入；CISA KEV 2026-11-20 收录，暂无公开 PoC | 已确认 | 待复现 |
| [CVE-2026-128049](CVE-2026-128049) | OpenMage Magento LTS | 4.0 9.4 (VulnCheck); 3.1 9.0 (VulnCheck) | OpenMage Magento LTS before 20.18.2; 21.0.0-beta1 before 21.0.0-beta3 | 20.18.2 / 21.0.0-beta3 | OAuth 确认接口 GET 请求缺 form-key 校验致 CSRF；仅检测型 PoC、未核实 | 已确认 | 待复现 |
| [CVE-2026-126380](CVE-2026-126380) | Vvveb CMS | 4.0 9.4 (VulnCheck); 3.1 9.1 (VulnCheck) | Vvveb before 1.0.9.0 | 1.0.9.0 | 已认证管理员上传 .phar 绕过媒体黑名单、可传 polyglot webshell；仅检测型 PoC、未核实 | 已确认 | 待复现 |
| [CVE-2026-94565](CVE-2026-94565) | NukeViet CMS | 3.1 9.3 (GHSA) | NukeViet CMS 3.x through 4.6.01 (Contact module) | 4.6.01 | 未认证访客经 Contact 模块提交含斜杠前缀事件处理属性的消息致存储型 XSS；仅检测型 PoC、未核实 | 已确认 | 待复现 |
| [CVE-2026-94567](CVE-2026-94567) | NukeViet CMS | 3.1 9.3 (GHSA) | NukeViet CMS before 4.5.12 and 4.6.02 (SVG upload) | 4.5.12 / 4.6.02 | SVG 上传中以内部 DTD 实体隐藏 script 元素致存储型 XSS；仅检测型 PoC、未核实 | 已确认 | 待复现 |
| [CVE-2026-94598](CVE-2026-94598) | NukeViet CMS | 3.1 8.2 (GHSA) | NukeViet CMS 4.5.08 through 4.5.12 and 4.6.02 (iframe srcdoc) | 4.5.12 / 4.6.02 | iframe srcdoc 值中伪造清洗标记致存储型 XSS；仅检测型 PoC、未核实 | 已确认 | 待复现 |
| [CVE-2026-54064](CVE-2026-54064) | NukeViet CMS | 3.1 8.7 (GHSA) | NukeViet CMS before 4.5.09 (news posting) | 4.5.09 | 有新闻发布权限的用户以换页符前缀事件处理属性绕过 filterAttr() 致存储型 XSS；仅检测型 PoC、未核实 | 已确认 | 待复现 |
| [CVE-2026-54065](CVE-2026-54065) | NukeViet CMS | 3.1 8.7 (GHSA) | NukeViet CMS before 4.5.09 (comment admin edit) | 4.5.09 | 已认证管理员经评论 attach 值路径穿越致应用文件被删；仅检测型 PoC、未核实 | 已确认 | 待复现 |
| [CVE-2026-77326](CVE-2026-77326) | MapServer | 3.1 8.6 (GHSA) | MapServer 8.2.0 through 8.6.5 (WMS GetLegendGraphic) | 8.6.5 | 未认证攻击者经 WMS GetLegendGraphic 触发堆缓冲区溢出致进程崩溃；仅崩溃型 PoC，未证明 RCE | 已确认 | 待复现 |
| [CVE-2026-94564](CVE-2026-94564) | NukeViet CMS | 3.1 8.2 (GHSA) | NukeViet CMS before 4.6.01 (Contact module) | 4.6.01 | 未认证访客经 URL 属性中带前导零的数字 HTML 实体致存储型 XSS；仅检测型 PoC、未核实 | 已确认 | 待复现 |
| [CVE-2026-133874](CVE-2026-133874) | Iceburg CRM | 4.0 8.6 (VulnCheck); 3.1 8.1 (VulnCheck) | Iceburg CRM through 5.0.0 | No known patch | 已认证用户经 saveRecord() 向未授权模块写数据、可提权至管理员；仅检测型 PoC、未核实 | 已确认 | 待复现 |
| [CVE-2026-120539](CVE-2026-120539) | Restrictions for BuddyPress | 3.1 9.8 (NVD) | <= 1.5.4 (requires BuddyPress and Paid Memberships Pro both active) | 1.5.5 | 未授权代码注入：请求 URI 经 {${...}} 插值进入 eval()；检测型 PoC 触发注入并回显 marker | 已确认 | 待复现 |
| [CVE-2026-3300](CVE-2026-3300) | Everest Forms Pro | 3.1 9.8 (NVD) | <= 1.9.12 (requires Calculation Addon / Complex Calculation enabled) |  | 未授权 PHP 代码注入（Calculation Addon）；PoC 触发注入并回显 PWNED；自 2026-04-13 在野利用 | 已确认 | 待复现 |
| [CVE-2026-131754](CVE-2026-131754) | APCu Manager | 3.1 9.8 (NVD) | APCu Manager through 4.6.1 |  | CWE-502; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-131782](CVE-2026-131782) | Simple Shopping Cart | 3.1 9.8 (NVD) | Simple Shopping Cart through 5.3.3 |  | CWE-502; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-129175](CVE-2026-129175) | Unstable Slope Management Program | 3.1 9.8 (CISA); 4.0 9.3 (CISA) | Unstable Slope Management Program (version not specified in NVD/GHSA) | Fixed on or around 2026-10-19 (per NVD) | CWE-306; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-132165](CVE-2026-132165) | Drupal core | unknown | Drupal core <10.6.22, 11.0.0-11.3.21, 11.4.0-11.4.12 | 10.6.22 / 11.3.22 / 11.4.13 | 权限提升 | 已确认 | 待复现 |
| [CVE-2026-125294](CVE-2026-125294) | Nexter Blocks Pro | 3.1 9.8 (Wordfence) | Nexter Blocks Pro up to and including 5.0.10 |  | CWE-269; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-134433](CVE-2026-134433) | Frappe ERPNext | 4.0 8.4 (VulnCheck); 3.1 8.5 (VulnCheck) | ERPNext before 15.124.2 and 16.x before 16.53.0 | 15.124.2 / 16.53.0 | CWE-862; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-134448](CVE-2026-134448) | Dockhand | 4.0 8.6 (VulnCheck); 3.1 8.1 (VulnCheck) | Dockhand 1.0.7 before 1.0.57 | 1.0.57 | CWE-22; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-134451](CVE-2026-134451) | Dockhand | 4.0 8.6 (VulnCheck); 3.1 8.1 (VulnCheck) | Dockhand before 1.0.57 | 1.0.57 | CWE-269; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-134452](CVE-2026-134452) | Dockhand | 4.0 8.7 (VulnCheck); 3.1 8.8 (VulnCheck) | Dockhand before 1.0.57 | 1.0.57 | CWE-426; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-134258](CVE-2026-134258) | Admidio | 4.0 9.3 (VulnCheck); 3.1 8.7 (VulnCheck) | Admidio 5.0.0 before 5.0.18 | 5.0.18 | CWE-22; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-134262](CVE-2026-134262) | Admidio | 4.0 9.2 (VulnCheck); 3.1 8.1 (VulnCheck) | Admidio 5.0.0 before 5.0.18 | 5.0.18 | CWE-79; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-134250](CVE-2026-134250) | Grav Form plugin | 4.0 8.8 (VulnCheck); 3.1 8.0 (VulnCheck) | Grav Form plugin 1.1.0 before 9.1.40 | 9.1.40 | CWE-79; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-134253](CVE-2026-134253) | Grav API plugin | 4.0 8.7 (VulnCheck); 3.1 8.8 (VulnCheck) | Grav API plugin 1.0.0 before 1.1.4 | 1.1.4 | CWE-94; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-134282](CVE-2026-134282) | Vikunja | 4.0 8.6 (VulnCheck); 3.1 8.1 (VulnCheck) | Vikunja 0.14.0 before 2.8.0 | 2.8.0 | CWE-915; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-134316](CVE-2026-134316) | @better-auth/electron | 4.0 8.6 (VulnCheck); 3.1 8.1 (VulnCheck) | 1.5.0-beta.12 before 1.7.16 and 1.8.0-beta.0 before 1.8.0-beta.5 | 1.7.16 / 1.8.0-beta.5 | CWE-201; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-134322](CVE-2026-134322) | better-auth | 4.0 8.6 (VulnCheck); 3.1 8.1 (VulnCheck) | 0.4.12-beta.7 before 1.7.16 and 1.8.0-beta.0 before 1.8.0-beta.5 | 1.7.16 / 1.8.0-beta.5 | CWE-287; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-134654](CVE-2026-134654) | Mailflare | 4.0 8.6 (VulnCheck); 3.1 8.1 (VulnCheck) | Mailflare before 48957fb | 48957fb | CWE-640; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-129024](CVE-2026-129024) | Everest Forms | 3.1 8.6 (Patchstack) | Everest Forms through 3.6.4 |  | CWE-22; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-131701](CVE-2026-131701) | WP Media Folder | 3.1 8.5 (Patchstack) | WP Media Folder through 6.2.8 |  | CWE-89; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-131705](CVE-2026-131705) | ProfileGrid | 3.1 8.5 (Patchstack) | ProfileGrid through 6.0.0.6 |  | CWE-89; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-131707](CVE-2026-131707) | ProfileGrid | 3.1 8.8 (Patchstack) | ProfileGrid through 6.0.0.6 |  | CWE-502; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-131750](CVE-2026-131750) | Everest Forms | 3.1 8.6 (Patchstack) | Everest Forms through 3.6.4 |  | CWE-22; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-134804](CVE-2026-134804) | Portainer | 3.1 8.8 (VulnCheck); 4.0 8.7 (VulnCheck) | Portainer 2.39.0 before 2.39.9, 2.40.0 before 2.45.4, 3.0.0 before 3.1.0 | 2.39.9 / 2.45.4 / 3.1.0 | CWE-639; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-134836](CVE-2026-134836) | Dashy | 3.1 8.1 (VulnCheck); 4.0 8.6 (VulnCheck) | Dashy 4.0.0 before 4.9.12 | 4.9.12 | CWE-346; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-135157](CVE-2026-135157) | Future AGI | 4.0 8.6 (VulnCheck); 3.1 8.1 (VulnCheck) | Future AGI before 1.51.0 | 1.51.0 | CWE-287; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-135161](CVE-2026-135161) | Interstellar | 4.0 9.2 (VulnCheck); 3.1 8.6 (VulnCheck) | Interstellar before 6.3.0 | 6.3.0 | CWE-918; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-135164](CVE-2026-135164) | Formance Ledger | 4.0 8.7 (VulnCheck); 3.1 8.8 (VulnCheck) | Formance Ledger 2.2.0-beta.3 before 2.4.18 | 2.4.18 | CWE-89; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-135208](CVE-2026-135208) | Kerberos Agent | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | Kerberos Agent before 3.14.4 | 3.14.4 | CWE-1394; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-135174](CVE-2026-135174) | Softaculous Virtualizor | 4.0 9.2 (VulnCheck); 3.1 8.1 (VulnCheck) | Softaculous Virtualizor before 3.2.9 | 3.2.9 | CWE-89; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-133469](CVE-2026-133469) | Xen Orchestra | 3.1 9.8 (GHSA) | Xen Orchestra before 6.9.2 / 6.10.1 | 6.9.2 / 6.10.1 | CWE-287; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-135429](CVE-2026-135429) | Tabbycat | 4.0 8.8 (VulnCheck); 3.1 9.1 (VulnCheck) | Tabbycat 2.9.0 through 2.12.1 |  | CWE-863; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-135436](CVE-2026-135436) | KindleEar | 4.0 8.7 (VulnCheck); 3.1 8.8 (VulnCheck) | KindleEar 3.0.0 through 3.5.3 |  | CWE-94; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-95793](CVE-2026-95793) | HPE Morpheus Manager | 3.1 8.8 (HPE) | HPE Morpheus Software 9.1.0-2 and earlier, 9.0.2-3 and earlier, 8.1.2-2 and earlier | 9.1.0-3 / 9.0.2-4 / 8.1.2-3 | PoC 触发漏洞 | 已确认 | 待复现 |

### AI / LLM (22)

| 编号 | 产品 | 评分 | 受影响版本 | 修复版本 | 判定 | CVE 状态 | 复现 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [CVE-2026-85228](CVE-2026-85228) | Amazon Deep Java Library (DJL) | 3.1 9.1 (AMZN); 4.0 8.8 (AMZN) | Amazon Deep Java Library (DJL) 0.13.0–0.36.0 | 0.37.0 | DJL 张量缓冲校验整数溢出；未授权信息泄露/拒绝服务；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-40217](CVE-2026-40217) | BerriAI LiteLLM | 3.1 8.8 PR:L (public README) | LiteLLM before v1.83.11 (image digest pinning required; some rebuilt tags are not vulnerable) | v1.83.11+ (RestrictedPython) | 认证后实验室 RCE，需要 API key | 已确认 | ◐ 部分 |
| [CVE-2026-130796](CVE-2026-130796) | Flowise | 4.0 8.8 (VulnCheck)；3.1 8.2 (VulnCheck) | 3.1.3-3.1.4 |  | 未认证泄露明文 MCP token；附带脚本是离线逻辑模拟 | 已确认 | ✅ 完整 |
| [CVE-2026-102895](CVE-2026-102895) | GPUStack | 3.1 9.8 (GHSA) | < 2.2.0 | 2.2.0 | 实验室验证的未认证管理员接管；在野利用为厂商报告，未经此 PoC 证实 | 已确认 | ◐ 部分 |
| [CVE-2026-59726](CVE-2026-59726) | Ruflo MCP Bridge | 3.1 10.0 (GHSA) | Ruflo < 3.16.3 (default docker-compose MCP bridge) | 3.16.3 | 经 MCP bridge terminal_execute 未认证 RCE；Exploit-DB 已验证 autopwn | 已确认 | 待复现 |
| [CVE-2026-63129](CVE-2026-63129) | mssql-mcp-core | 3.1 8.8 (GHSA) | mssql-mcp-core <= 0.5.0 (also reader <= 0.4.2, writer <= 0.4.2, server <= 0.5.2) | 0.6.0 | MCP 工具调用未参数化致 SQL 注入；xp_cmdshell 自称，未核实 | 已确认 | 待复现 |
| [CVE-2026-73678](CVE-2026-73678) | Minds Platform | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | MindsDB Minds Platform 26.1.0 and earlier | No fixed release published in CVE record (2026-11-20) | 未授权远程代码执行（Agent scratchpad exec()）；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-77312](CVE-2026-77312) | Flyto2 Core | 3.1 10.0 (GitHub) | Flyto2 Core <2.26.8 | 2.26.8 | Flyto2 Core 未设防数据/文件模块任意文件写入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-77315](CVE-2026-77315) | Flyto2 Core | 3.1 8.5 (GitHub) | Flyto2 Core <2.26.8 | 2.26.8 | Flyto2 Core http.paginate 二阶 SSRF；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-63189](CVE-2026-63189) | Dialoqbase | 3.1 9.8 (GHSA) | Dialoqbase <1.11.5 | 1.11.5 | Dialoqbase 未授权路径遍历致任意文件读；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-76807](CVE-2026-76807) | Todoist MCP Server | 3.1 9.3 (GHSA) | Todoist MCP Server <10.3.3 | 10.3.3 | Todoist MCP Server DNS 重绑定致网站读写 Todoist 数据；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-130154](CVE-2026-130154) | Zyrabit Platform | 3.1 9.1 (GHSA) | Zyrabit Platform <2.4.4 | 2.4.4 | Zyrabit import_to_vault 路径遍历致任意文件读写；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-77359](CVE-2026-77359) | Jupyter MCP Server | 4.0 9.3 (GHSA) | Jupyter MCP Server <1.0.3 | 1.0.3 | Jupyter MCP Server DNS 重绑定劫持后端；通告内含可复现 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-131304](CVE-2026-131304) | Splunk AI Assistant | 3.1 8.1 (Splunk) | Splunk AI Assistant <2.0.0 | 2.0.0 | Splunk AI Assistant 租户越权读数据/冒认操作；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-131305](CVE-2026-131305) | Splunk AI Assistant | 3.1 8.1 (Splunk) | Splunk AI Assistant <2.0.0 | 2.0.0 | Splunk AI Assistant 未授权改功能配置；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-93328](CVE-2026-93328) | Google Cloud MCP Toolbox for Databases | 4.0 9.3 (GoogleCloud) | Google Cloud MCP Toolbox for Databases 1.2.0-1.4.0 | past 1.4.0 + allowlists (googleapis/mcp-toolbox#3454) | Google Cloud MCP Toolbox 云存储源路径穿越与缺失授权，未认证外泄宿主文件并覆写任意本地文件；实验室复现 PoC、未核实 | 已确认 | 待复现 |
| [CVE-2026-133968](CVE-2026-133968) | MONAI Label | 3.1 9.8 (MITRE) | MONAI Label through 0.8.5 | 0.8.6 (security release 2026-11-22; fix PR #1915) | 数据存储上传接口路径遍历致任意文件写入、可致 RCE；2026 年 9 月起已在野利用，暂无公开 PoC | 已确认 | 待复现 |
| [CVE-2026-48705](CVE-2026-48705) | MONAI | 3.1 9.3 (GHSA) | MONAI before 1.6.1 (PydicomReader); MONAILabel deployments using it | MONAI 1.6.1 | 含 NaN/inf 的 DICOM 致 MONAILabel 服务器崩溃与推理损坏；崩溃型 PoC、本仓未核实 | 已确认 | 待复现 |
| [CVE-2026-118683](CVE-2026-118683) | MONAI | 4.0 8.6 (VulnCheck) | MONAI 1.2.0 before 1.6.1 | MONAI 1.6.1 | 恶意 bundle 的 logging.conf 在工作流构造时被 fileConfig 求值致代码执行；仅检测型 PoC、未核实 | 已确认 | 待复现 |
| [CVE-2026-54039](CVE-2026-54039) | LibreChat | 3.1 8.1 (GHSA) | LibreChat 0.7.0 through 0.8.6 (local registration + social provider) | 0.8.6 | 未认证攻击者经注册接口伪造 provider 值致账户接管；仅检测型 PoC、未核实 | 已确认 | 待复现 |
| [CVE-2026-135211](CVE-2026-135211) | BISHENG | 4.0 9.2 (VulnCheck); 3.1 8.1 (VulnCheck) | BISHENG before 3.0.0 | 3.0.0 | CWE-306; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-130169](CVE-2026-130169) | AutoGPT Platform | 3.1 10.0 (GHSA) | AutoGPT Platform 0.6.26 through 0.7.4 | 0.8.0 | CWE-287; PoC 触发漏洞 | 已确认 | 待复现 |

### 网络与安全 (168)

| 编号 | 产品 | 评分 | 受影响版本 | 修复版本 | 判定 | CVE 状态 | 复现 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [CVE-2026-130151](CVE-2026-130151) | Okta Privileged Access Gateway | 3.1 8.5 (Okta) | Okta Privileged Access Gateway <1.116.3 (RDP support) | 1.116.3 | Okta 特权访问网关 FreeRDP 智能卡内存问题致命令执行；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-95643](CVE-2026-95643) | ManageEngine DDI Central | 3.1 9.1 (Zohocorp) | Zohocorp ManageEngine DDI Central build <6500 | 6500 | DDI Central Telnet 功能经 IPv6 作用域标识的认证 PowerShell 命令注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-95645](CVE-2026-95645) | ManageEngine DDI Central | 3.1 9.1 (Zohocorp) | Zohocorp ManageEngine DDI Central build <6500 | 6500 | DDI Central Windows 代理 clear_blocked_domains 认证命令注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-104935](CVE-2026-104935) | Ivanti Connect Secure | 3.1 8.6 (Ivanti) | Ivanti Connect Secure 25.1.1.2 and prior; 25.1.2.2 and prior; 22.8R2.5 and prior | 25.1.1.3 / 22.8R2.6 | Ivanti Connect Secure 认证绕过；已确认在野利用（KEV 2026-10-13），无公开 PoC | 已确认 | — 无目标 |
| [CVE-2026-111357](CVE-2026-111357) | Ivanti Connect Secure | 3.1 7.0 (NVD); 3.1 8.8 (Ivanti) | Ivanti Connect Secure 25.1.1.2 and prior; 25.1.2.2 and prior; 22.8R2.5 and prior | 25.1.1.3 / 22.8R2.6 | Ivanti Connect Secure 关键功能缺失认证致本地提权；已确认在野利用（KEV 2026-10-30），无公开 PoC | 已确认 | — 无目标 |
| [CVE-2026-118527](CVE-2026-118527) | Ivanti Connect Secure | 3.1 4.3 (Ivanti) | Ivanti Connect Secure 25.1.1.2 and prior; 25.1.2.2 and prior; 22.8R2.5 and prior | 25.1.1.3 / 22.8R2.6 | Ivanti Connect Secure 可预测文件名致文件上传到已知位置；已确认在野利用（KEV 2026-10-30），无公开 PoC | 已确认 | — 无目标 |
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
| [CVE-2026-83548](CVE-2026-83548) | SonicWall SMA1000 | 3.1 10.0 (NVD) | SMA1000 6210 / 7210 / 8200v: 12.4.3-03453 and older, 12.5.0-02835 and older | 12.4.3-03526 and higher, 12.5.0-02952 and higher (platform-hotfix) | 未授权 SSRF → CouchDB RCE → root 全链工具；厂商确认在野利用，CISA KEV | 已确认 | — 无目标 |
| [CVE-2026-83549](CVE-2026-83549) | SonicWall SMA1000 | 3.1 7.8 (NVD) | SMA1000 6210 / 7210 / 8200v: 12.4.3-03453 and older, 12.5.0-02835 and older | 12.4.3-03526 and higher, 12.5.0-02952 and higher (platform-hotfix) | 认证后 AMC 命令注入 → root；同一工具，CISA KEV | 已确认 | — 无目标 |
| [CVE-2026-123633](CVE-2026-123633) | F5 NGINX HTTP/2 | 4.0 9.2 (F5)；3.1 8.1 (F5) | NGINX Open Source 1.19.7-1.30.6 and 1.31.0-1.31.8 with HTTP/2 proxying | 1.30.7 / 1.31.9 | UAF 触发器 + 自称 ret2libc RCE 的脚本，未核实 | 已确认 | 待复现 |
| [CVE-2026-110486](CVE-2026-110486) | Eclipse Mosquitto | 3.1 9.8 (NVD) | 2.1.0–2.1.2 (builtin WebSocket listener) | 2.1.3 | 实验室触发解析器失同步（空 WebSocket 帧）；RCE 未证明 | 已确认 | 待复现 |
| [CVE-2026-124040](CVE-2026-124040) | CivetWeb HTTP/2 | 4.0 9.2 (VulnCheck)；3.1 8.1 (VulnCheck) | CivetWeb through 1.16, built with USE_HTTP2 and enable_http2 | No fixed release listed (PoC repo ships fix-http2.patch) | HPACK 投毒把方法/路径藏过字面头 ACL；命令执行只在作者的高权限演示回调里 | 已确认 | 待复现 |
| [CVE-2026-116448](CVE-2026-116448) | Dell PowerStore SDNAS | 3.1 9.8 (GHSA) | Dell PowerStore OS <= 3.6.0.0 with SDNAS enabled (per PoC README; GHSA lists no version range) | PowerStore OS 4.0.0.1 (per PoC README) | SDNAS 诊断接口 OS 命令注入；RCE 脚本自称，未核实 | 已确认 | 待复现 |
| [CVE-2026-123634](CVE-2026-123634) | F5 NGINX 解析器 (SSI) | 4.0 9.2 (F5)；3.1 8.1 (F5) | NGINX 0.6.18-1.31.8 (proxy with SSI subrequests) | 1.30.7 / 1.31.9 | 解析器 UAF 崩溃（Docker 实验）；含利用脚本，未核实 | 已确认 | 待复现 |
| [CVE-2026-121810](CVE-2026-121810) | F5 NGINX HTTP/3 (QUIC) | 4.0 9.2 (F5)；3.1 8.1 (F5) | NGINX 1.25.0-1.31.8 (HTTP/3) | 1.30.7 / 1.31.9 | HTTP/3 QUIC UAF 崩溃（Docker 实验）；含利用脚本，未核实 | 已确认 | 待复现 |
| [CVE-2026-113425](CVE-2026-113425) | F5 NGINX 邮件代理 | 4.0 9.2 (F5)；3.1 8.1 (F5) | NGINX 0.5.33-1.31.8 (mail proxy) | 1.30.7 / 1.31.9 | 邮件代理 UAF 崩溃（Docker 实验）；含利用脚本，未核实 | 已确认 | 待复现 |
| [CVE-2026-118899](CVE-2026-118899) | F5 NGINX TLS 1.3 | 4.0 8.7 (F5)；3.1 7.5 (F5) | NGINX 1.13.0-1.31.8 (TLS 1.3, http block) | 1.30.7 / 1.31.9 | TLS 1.3 无限循环 DoS（Docker 实验）；含利用脚本，未核实 | 已确认 | 待复现 |
| [CVE-2026-116442](CVE-2026-116442) | Dell PowerStore NDMP | 3.1 8.1 (GHSA) | Dell PowerStore OS <= 3.6.0.0 with NDMP enabled (per PoC README; GHSA lists no version range) | PowerStore OS 4.0.0.1 (per PoC README) | NDMP 重放认证绕过；PoC 仅展示未授权 NDMP 响应 | 已确认 | 待复现 |
| [CVE-2026-114202](CVE-2026-114202) | ASUS Control Center Express | 4.0 10.0 (NVD) | ASUS Control Center Express all firmware versions prior to patch (PoC tested through v1.7.27) | no fixed version published | 硬编码 JWT 密钥伪造管理员令牌；密钥须自行提取，未核实 | 已确认 | 待复现 |
| [CVE-2026-131852](CVE-2026-131852) | OwnTracks Recorder | 3.1 9.8 (GHSA) | OwnTracks Recorder before 1.0.5 | 1.0.5 | location tid 存储型格式化字符串；指针泄露与持续 DoS（实验），未核实 | 已确认 | 待复现 |
| [CVE-2026-92182](CVE-2026-92182) | pfSense CE | 3.0 8.8 (GHSA) | pfSense CE ≤ 2.8.1 | pfSense CE 2.8.2 | 低权限账户可调管理 XMLRPC 方法；root RCE，未核实 | 已确认 | 待复现 |
| [CVE-2026-123640](CVE-2026-123640) | F5 NGINX ssl_preread | 3.1 5.3 (GHSA) | nginx 1.15.2–1.31.8 (ssl_preread) | 1.30.7 / 1.31.9 | ssl_preread SNI 校验不足；错误路由/越界读（Docker 实验），未核实 | 已确认 | 待复现 |
| [CVE-2026-120993](CVE-2026-120993) | F5 NGINX stream SSL | 3.1 5.3 (GHSA) | nginx 1.31.4–1.31.8 (stream SSL + PROXY v2) | 1.31.9 | PROXY v2 + 动态证书空指针解引用；worker 崩溃（Docker 实验），未核实 | 已确认 | 待复现 |
| [CVE-2026-125283](CVE-2026-125283) | F5 NGINX alias/try_files | 3.1 5.3 (GHSA) | nginx 0.9.6–1.31.8 (alias + try_files) | 1.30.7 / 1.31.9 | alias + try_files 整数下溢；越界读（Docker 实验），未核实 | 已确认 | 待复现 |
| [CVE-2026-120967](CVE-2026-120967) | F5 NGINX stream SNI | 3.1 4.8 (GHSA) | nginx 1.25.5–1.31.8 (stream SNI mTLS) | 1.30.7 / 1.31.9 | stream SNI mTLS 校验时机太晚；绕过到受保护后端（实验），未核实 | 已确认 | 待复现 |
| [CVE-2026-129358](CVE-2026-129358) | Magma NMS | 4.0 1.9 (VulDB) | Magma NMS up to 1.9.0 | none (unfixed upstream) | 组织名未经转义渲染进内联 CONFIG 脚本，存储型 XSS | 已确认 | 待复现 |
| [CVE-2026-129351](CVE-2026-129351) | TRENDnet TEW-657BRM 路由器 | 4.0 10.0 (VulDB) | TEW-657BRM v1.0R firmware 1.00.1 | none (EOL, no vendor fix) | 未认证超长 .htm 路径经 sprintf 越界写 GOT；已停产，无厂商修复 | 已确认 | 待复现 |
| [CVE-2026-129353](CVE-2026-129353) | D-Link DIR-600L 路由器 | 4.0 10.0 (VulDB) | DIR-600L B1 firmware 2.17, 2.17b02 | none (EOL, no vendor fix) | 未认证经 id/password 无界 strcpy 栈溢出；已停产，无厂商修复 | 已确认 | 待复现 |
| [CVE-2026-129354](CVE-2026-129354) | D-Link DIR-600L 路由器 | 4.0 10.0 (VulDB) | DIR-600L B1 firmware 2.17b02 | none (EOL, no vendor fix) | 未认证经 SOAPAction 头溢出 HNAP hnap_main 栈；已停产，无厂商修复 | 已确认 | 待复现 |
| [CVE-2026-110697](CVE-2026-110697) | Quay 容器镜像仓库 | 3.1 9.9 (Red Hat) | Quay < 3.9.28; 3.10 < 3.10.28; 3.12 < 3.12.24; 3.14 < 3.14.10; 3.15 < 3.15.9; 3.16 < 3.16.7; 3.17 < 3.17.7; 3.18 < 3.18.3 | 3.9.28 / 3.10.28 / 3.12.24 / 3.14.10 / 3.15.9 / 3.16.7 / 3.17.7 / 3.18.3 | 机器人列表 SQL LIKE 通配符注入泄露跨租户机器人令牌；各分支修复版已发布 | 已确认 | 待复现 |
| [CVE-2026-126147](CVE-2026-126147) | FortiMail | 3.1 9.8 (Fortinet) | FortiMail 8.0.0–8.0.1, 7.6.0–7.6.6, 7.4.0–7.4.8, 7.2.0–7.2.9 | 8.0.2 / 7.6.7 / 7.4.9; migrate off 7.2 | 管理接口路径穿越可写任意文件并执行命令；8.0.2/7.6.7/7.4.9 修复 | 已确认 | 待复现 |
| [CVE-2026-126148](CVE-2026-126148) | FortiMail | 3.1 9.8 (Fortinet) | FortiMail 8.0.0–8.0.1, 7.6.0–7.6.6 | 8.0.2 / 7.6.7 | HA 入网请求经 hostname/peer-ip 字段命令注入；8.0.2/7.6.7 修复 | 已确认 | 待复现 |
| [CVE-2026-129352](CVE-2026-129352) | TRENDnet TEW-657BRM 路由器 | 4.0 9.4 (VulDB) | TEW-657BRM v1.0R firmware 1.00.1 | none (EOL, no vendor fix) | 已认证经 multipart 首行无界 strncpy 栈溢出；已停产，无厂商修复 | 已确认 | 待复现 |
| [CVE-2026-114550](CVE-2026-114550) | libwebsockets | 3.0 8.1 (GHSA) | libwebsockets v4.2–v4.5.8 (MQTT client role) | 5.0.0 | MQTT PUBACK 越界写改写链表与函数指针；实验有据，未核实 | 已确认 | 待复现 |
| [CVE-2026-129355](CVE-2026-129355) | dufs | 4.0 6.9 (VulnDB); 3.1 6.5 (VulnDB) | dufs 0.1.0–0.46.0 | 0.47.0 | WebDAV COPY 无删除权限覆盖已有文件；实验有据 | 已确认 | 待复现 |
| [CVE-2026-129359](CVE-2026-129359) | Magma orc8r | 4.0 5.5 (VulnDB); 3.1 7.3 (VulnDB) | Magma <= 1.9.0 | no upstream fix (synthetic remediation in lab) | 硬编码内部凭证让任意 gRPC 调用方成可信服务；实验有据 | 已确认 | 待复现 |
| [CVE-2026-129360](CVE-2026-129360) | Magma orc8r | 4.0 6.9 (VulnDB); 3.1 7.3 (VulnDB) | Magma <= 1.9.0 | no upstream fix (synthetic remediation in lab) | 操作员身份跟随可伪造的证书序列请求头；实验有据 | 已确认 | 待复现 |
| [CVE-2026-76466](CVE-2026-76466) | Cisco Expressway | 3.1 9.8 (Cisco) | Expressway-C / Expressway-E clustered, X15.5.3 and earlier (X14 and earlier too) | X15.5.20 | 集群 Expressway 硬编码 Erlang cookie 未授权 root RCE；实验室已验证，F6 确认在野利用 | 已确认 | — 无目标 |
| [CVE-2026-13249](CVE-2026-13249) | Honeywell PD45 打印机 | 3.1 9.8 (Honeywell) | Honeywell PD45 firmware >= F10.19.010040 and < F10.22.030745 | F10.22.030745 | 打印机 Web 管理未认证任意文件上传；确切上传地址未公开，须操作者自供 URL，未核实 | 已确认 | 待复现 |
| [CVE-2026-13768](CVE-2026-13768) | Gardyn 智能花园 | 4.0 9.5 (ICS-CERT); 3.1 10.0 (ICS-CERT) | Gardyn Home Kit and Studio devices (exposed iothubowner key) | Cloud-side fix deployed (2026-07); devices auto-update firmware when connected | 泄露的 IoT Hub 所有者密钥可枚举全 fleet 并经 upgrade() 命令注入 RCE；云端已修复，未核实 | 已确认 | 待复现 |
| [CVE-2026-116440](CVE-2026-116440) | PowerStore SDNAS | 3.1 9.8 (Dell) | Dell PowerStore SDNAS versions before 5.1.0.0-2798105 | 5.1.0.0-2798105 (DSA-2026-479) | SDNAS 未认证远程缓冲区溢出；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-132622](CVE-2026-132622) | GearUP Hyperev | 4.0 9.4 (VulDB); 3.1 9.1 (VulDB) | GearUP Hyperev up to 20261020 |  | WLAN 扫描接口命令注入（时延检测），未核实 | 已确认 | 待复现 |
| [CVE-2026-133185](CVE-2026-133185) | goproxy | 4.0 9.1 (VulnCheck); 3.1 7.4 (VulnCheck) | elazarl/goproxy before 1.9.4 | 1.9.4 | math/rand 种子可预测致 TLS 叶证书私钥泄露，未核实 | 已确认 | 待复现 |
| [CVE-2026-116443](CVE-2026-116443) | PowerStore SDNAS | 3.1 9.8 (Dell) | Dell PowerStore SDNAS versions before 5.1.0.0-2798105 | 5.1.0.0-2798105 (DSA-2026-479) | NAS TFTP 服务栈缓冲区溢出；崩溃检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-116446](CVE-2026-116446) | PowerStore SDNAS | 3.1 9.8 (Dell) | Dell PowerStore SDNAS versions before 5.1.0.0-2798105 | 5.1.0.0-2798105 (DSA-2026-479) | NAS NFS 服务越界内存访问；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-116449](CVE-2026-116449) | PowerStore SDNAS | 3.1 9.8 (Dell) | Dell PowerStore SDNAS versions before 5.1.0.0-2798105 | 5.1.0.0-2798105 (DSA-2026-479) | SDNAS 操作系统命令注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-116441](CVE-2026-116441) | PowerStore SDNAS | 3.1 9.6 (Dell) | Dell PowerStore SDNAS versions before 5.1.0.0-2798105 | 5.1.0.0-2798105 (DSA-2026-479) | 存储处理器互联驱动越界写；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-111505](CVE-2026-111505) | OpenManage Enterprise | 3.1 8.8 (Dell) | Dell OpenManage Enterprise versions prior to 4.8.0 | 4.8.0 (DSA-2026-467) | OpenManage Enterprise 操作系统命令注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-111506](CVE-2026-111506) | PowerStore | 3.1 8.8 (Dell) | Dell PowerStoreT OS 5.1.x versions prior to 5.1.0.0-2798105 | 5.1.0.0-2798105 or later (DSA-2026-479) | PowerStore 缺失认证；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-111545](CVE-2026-111545) | PowerStore | 3.1 8.8 (Dell) | Dell PowerStoreT OS 5.1.x versions prior to 5.1.0.0-2798105 | 5.1.0.0-2798105 or later (DSA-2026-479) | PowerStore SQL 注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-133323](CVE-2026-133323) | MiCollab | 3.1 10.0 (Mitel) | MiCollab 10.3 (10.3.0.18) and earlier | Patch for 10.3 (10.3.0.18) (MISA-2026-0012) | MiCollab AWV 盲命令注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-133303](CVE-2026-133303) | MiCollab | 3.1 9.0 (Mitel) | MiCollab 10.3 (10.3.0.18) and earlier | Patch for 10.3 (10.3.0.18) (MISA-2026-0012) | MiCollab AWV XML 注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-133310](CVE-2026-133310) | Wing FTP Server | 4.0 9.2 (VulnCheck); 3.1 8.1 (VulnCheck) | Wing FTP Server before 8.2.8 | 8.2.8 | Wing FTP Server NUL 字节文件掩码绕过；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-116447](CVE-2026-116447) | PowerStore SDNAS | 3.1 8.8 (Dell) | Dell PowerStore SDNAS versions before 5.1.0.0-2798105 | 5.1.0.0-2798105 (DSA-2026-479) | PowerStore SDNAS 本地提权；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-116411](CVE-2026-116411) | PowerStore | 3.1 8.8 (Dell) | Dell PowerStore SDNAS versions before 5.1.0.0-2798105 | 5.1.0.0-2798105 (DSA-2026-479) | PowerStore 服务端请求伪造；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-76460](CVE-2026-76460) | Identity Services Engine | 3.1 10.0 (Cisco) | Cisco ISE 3.1-3.5 and ISE-PIC 3.4-3.5 | 3.1 Patch 12 / 3.2 Patch 11 / 3.3 Patch 12 / 3.4 Patch 7 / 3.5 Patch 4 (2026-09-16) | Cisco ISE API 身份验证绕过；检测型 PoC，未核实 | 已确认 | ◐ 部分 |
| [CVE-2026-84295](CVE-2026-84295) | WS_FTP Server | 3.1 10.0 (Progress) | Progress WS_FTP Server before 2024.0.6 / 2025.0.3 | 2024.0.6 / 2025.0.3 | WS_FTP Server 身份验证缺失；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-77537](CVE-2026-77537) | UniFi Protect | 3.1 10.0 (UI) | UniFi Protect Application before 7.2.105 | 7.2.105 | UniFi Protect 命令注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-95787](CVE-2026-95787) | ArubaOS (AOS-10) | 3.1 10.0 (HPE) | ArubaOS AOS-10 10.8.1.1 and below, 10.7.2.6 and below, 10.4.1.13 and below | 10.8.1.2 / 10.7.2.7 / 10.4.1.14 and above (HPE SBNW05162) | ArubaOS PAPI 协议身份验证绕过；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-111507](CVE-2026-111507) | PowerStore | 3.1 8.1 (Dell) | Dell PowerStore versions before 5.1.0.0-2798105 | 5.1.0.0-2798105 (DSA-2026-479) | Dell PowerStore 授权绕过；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-111547](CVE-2026-111547) | PowerStore | 3.1 8.1 (Dell) | Dell PowerStore versions before 5.1.0.0-2798105 | 5.1.0.0-2798105 (DSA-2026-479) | Dell PowerStore 越界读取；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-116417](CVE-2026-116417) | PowerScale InsightIQ | 3.1 8.1 (Dell) | Dell PowerScale InsightIQ 6.3.0-6.4.0 | 6.4.1 (DSA-2026-480) | Dell PowerScale InsightIQ 弱口令要求；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-15409](CVE-2026-15409) | SMA1000 | 3.1 10.0 (SonicWall) | SonicWall SMA1000 12.4.3-03245/03387/03434, 12.5.0-02283/02624/02800 (platform-hotfix) and earlier | 12.4.3-03453 / 12.5.0-02835 and higher (SNWLID-2026-0008) | SonicWall SMA1000 预认证服务端请求伪造；检测型 PoC，未核实 | 已确认 | ◐ 部分 |
| [CVE-2026-109469](CVE-2026-109469) | Entra Device Registration | 3.1 10.0 (Microsoft) | Microsoft Entra Device Registration (hosted service) | Official fix available (Microsoft service-side remediation, MSRC 2026-11-05) | Entra 设备注册用户可控密钥授权绕过；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-102255](CVE-2026-102255) | SMA1000 | 3.1 10.0 (SonicWall) | SonicWall SMA1000 12.4.3-03526 and older, 12.5.0-02952 and older (platform-hotfix) | 12.4.3-03670 / 12.5.0-03082 and higher (SNWLID-2026-0017) | SonicWall SMA1000 预认证 SSRF（非预期转发代理路径）；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-77550](CVE-2026-77550) | UniFi OS Server | 3.1 10.0 (UI) | UniFi OS Server 5.1.21 and earlier; UniFi OS devices 5.1.26 and earlier; Express 4.0.16 and earlier | UniFi OS Server 5.1.37+; devices 5.1.31+; NAS 5.1.32+; Express 4.0.17+ (Bulletin 067) | UniFi OS Server CRLF 注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-77554](CVE-2026-77554) | UniFi Talk Application | 3.1 10.0 (UI) | UniFi Talk Application 5.2.7 and earlier | 5.3.2 or later (Bulletin 067) | UniFi Talk 应用命令注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-84236](CVE-2026-84236) | Guardium Data Protection | 3.1 9.8 (IBM) | IBM Guardium Data Protection 12.2 | 12.2.4 | IBM Guardium Data Protection 反序列化 RCE；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-87977](CVE-2026-87977) | Guardium Data Protection | 3.1 9.8 (IBM) | IBM Guardium Data Protection 12.2 | 12.2.4 | IBM Guardium Data Protection SQL 注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-76536](CVE-2026-76536) | Splunk Enterprise | 3.1 9.4 (Splunk) | Splunk Enterprise 10.4-10.4.4, 10.2-10.2.8, 10.0-10.0.11, 9.4-9.4.16 | 10.4.5 / 10.2.9 / 10.0.12 / 9.4.17 (SVD-2026-1103) | Splunk Enterprise 集群配置认证绕过；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-76535](CVE-2026-76535) | Splunk Enterprise | 3.1 9.1 (Splunk) | Splunk Enterprise 10.6.0.5, 10.4-10.4.4, 10.2-10.2.8, 10.0-10.0.11, 9.4-9.4.16 | 10.6.1 / 10.4.5 / 10.2.9 / 10.0.12 / 9.4.17 (SVD-2026-1103) | Splunk Enterprise RapidDiag 认证绕过；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-82339](CVE-2026-82339) | Guardium Data Protection | 3.1 9.1 (IBM) | IBM Guardium Data Protection 12.2 | 12.2.4 | IBM Guardium Data Protection SharePoint S-TAP 缺失认证；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-76538](CVE-2026-76538) | Splunk Enterprise | 3.1 8.8 (Splunk) | Splunk Enterprise 10.4-10.4.4, 10.2-10.2.8, 10.0-10.0.11, 9.4-9.4.15 | 10.4.5 / 10.2.9 / 10.0.12 / 9.4.16 (SVD-2026-1103) | Splunk Enterprise 数据模型加速 SPL 注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-76540](CVE-2026-76540) | Splunk Enterprise | 3.1 8.8 (Splunk) | Splunk Enterprise 10.4-10.4.4, 10.2-10.2.8, 10.0-10.0.11, 9.4-9.4.16 | 10.4.5 / 10.2.9 / 10.0.12 / 9.4.17 (SVD-2026-1103) | Splunk Enterprise 指标告警不当授权；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-84273](CVE-2026-84273) | Guardium Data Protection | 3.1 8.1 (IBM) | IBM Guardium Data Protection 12.2 | 12.2.4 | IBM Guardium Data Protection 数据源路径遍历；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-85018](CVE-2026-85018) | Guardium Data Protection | 3.1 8.1 (IBM) | IBM Guardium Data Protection 12.2 | 12.2.4 | IBM Guardium Data Protection Terraform 提供方证书校验缺失；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-82342](CVE-2026-82342) | Guardium Data Protection | 3.1 8.1 (IBM) | IBM Guardium Data Protection 12.2 | 12.2.4 | IBM Guardium Data Protection PROXY 协议头栈溢出；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-76544](CVE-2026-76544) | Splunk Enterprise | 3.1 8.1 (Splunk) | Splunk Enterprise 10.4-10.4.4, 10.2-10.2.8, 10.0-10.0.11, 9.4-9.4.15 | 10.4.5 / 10.2.9 / 10.0.12 / 9.4.16 (SVD-2026-1103) | Splunk Enterprise 指标告警过滤器 SPL 注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-132808](CVE-2026-132808) | UniFi Access Application | 3.1 9.9 (Ubiquiti) | UniFi Access Application <4.3.24 | 4.3.24 | UniFi Access 越权致已纳管设备命令执行；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-132804](CVE-2026-132804) | UniFi Access Application | 3.1 9.9 (Ubiquiti) | UniFi Access Application <4.3.24 | 4.3.24 | UniFi Access SSRF 致 UniFi OS 内提权；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-132803](CVE-2026-132803) | UniFi Access Application | 3.1 9.9 (Ubiquiti) | UniFi Access Application <4.3.24 | 4.3.24 | UniFi Access 认证后 SQL 注入致提权；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-132802](CVE-2026-132802) | UniFi Access Application | 3.1 9.9 (Ubiquiti) | UniFi Access Application <4.3.24 | 4.3.24 | UniFi Access 链接解析不当致 root 代码执行；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-132139](CVE-2026-132139) | DrayTek Vigor2960 | 4.0 9.4 (VulDB); 3.1 9.9 (VulDB) | Vigor2960 1.5.1.0-1.5.1.6 | 1.5.1.7 | DrayTek Vigor2960 setSWMProfile 栈溢出；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-121805](CVE-2026-121805) | F5 BIG-IP | 4.0 9.3 (F5); 3.1 9.8 (F5) | BIG-IP 21.1.0 / 17.5.x / 17.1.x with PEM::subscriber iRule | 21.1.0.4.0.19.3-ENG / 17.5.1.11.0.61.12-ENG / 17.1.3.7.0.21.4-ENG | BIG-IP PEM::subscriber iRule 处理栈溢出；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-120722](CVE-2026-120722) | F5 BIG-IP | 4.0 9.3 (F5); 3.1 9.8 (F5) | BIG-IP 21.1.0 / 17.5.x / 17.1.x with DNS::scrape iRule | 21.1.0.4.0.19.3-ENG / 17.5.1.11.0.61.12-ENG / 17.1.3.7.0.21.4-ENG | BIG-IP DNS::scrape iRule 处理栈溢出；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-120292](CVE-2026-120292) | F5 BIG-IP | 4.0 9.3 (F5); 3.1 9.8 (F5) | BIG-IP 21.1.0 / 17.5.0-17.5.1 / 17.1.0-17.1.3 with MR::message route iRule | 21.1.0.4.0.19.3-ENG / 17.5.1.11.0.61.12-ENG / 17.1.3.7.0.21.4-ENG | BIG-IP MR::message route iRule 处理栈溢出；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-120285](CVE-2026-120285) | F5 BIG-IP | 4.0 9.3 (F5); 3.1 9.8 (F5) | BIG-IP 21.1.0 / 17.5.0-17.5.1 / 17.1.0-17.1.3 with PSC::ip_address iRule | 21.1.0.4.0.19.3-ENG / 17.5.1.11.0.61.12-ENG / 17.1.3.7.0.21.4-ENG | BIG-IP PSC::ip_address iRule 处理栈溢出；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-116953](CVE-2026-116953) | F5 BIG-IP | 4.0 9.3 (F5); 3.1 9.8 (F5) | BIG-IP 21.1.0 / 17.5.0-17.5.1 / 17.1.0-17.1.3 with GENERICMESSAGE::route iRule | 21.1.0.4.0.19.3-ENG / 17.5.1.11.0.61.12-ENG / 17.1.3.7.0.21.4-ENG | BIG-IP GENERICMESSAGE::route iRule 处理栈溢出；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-131287](CVE-2026-131287) | Splunk SOAR | 3.1 9.6 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 | Splunk SOAR 跨仓 playbook 引用致 RCE；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-132142](CVE-2026-132142) | DrayTek Vigor2960 | 4.0 9.4 (VulDB); 3.1 9.1 (VulDB) | Vigor2960 1.5.1.0-1.5.1.6 | 1.5.1.7 | DrayTek Vigor2960 dataflowstatus 栈溢出；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-132143](CVE-2026-132143) | DrayTek Vigor2960 | 4.0 9.4 (VulDB); 3.1 9.9 (VulDB) | Vigor2960 1.5.1.0-1.5.1.6 | 1.5.1.7 | DrayTek Vigor2960 doWebBackup 栈溢出；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-132141](CVE-2026-132141) | DrayTek Vigor2960 | 4.0 9.4 (VulDB); 3.1 9.9 (VulDB) | Vigor2960 1.5.1.0-1.5.1.6 | 1.5.1.7 | DrayTek Vigor2960 jsonstatus 栈溢出；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-131253](CVE-2026-131253) | Splunk SOAR | 3.1 9.9 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 | Splunk SOAR App Wizard 代码注入致 RCE；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-132807](CVE-2026-132807) | UniFi Access Application | 3.1 9 (Ubiquiti) | UniFi Access Application <4.3.24 | 4.3.24 | UniFi Access 证书校验不当致敏感信息泄露与越权；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-123637](CVE-2026-123637) | BIG-IP | 4.0 9.3 (F5); 3.1 9.8 (F5) | BIG-IP APM 21.1.0 / 17.5.0-17.5.1 / 17.1.0-17.1.3 | 工程热修复 BIGIP-21.1.0.4.0.19.3-ENG3 / BIGIP-17.5.1.11.0.61.12-ENG3 / BIGIP-17.1.3.7.0.21.4-ENG3（F5 K000163937） | F5 BIG-IP APM 栈溢出致 TMM 崩溃与 RCE；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-104099](CVE-2026-104099) | Fabio | 3.1 9.1 (GHSA) | Fabio <1.7.3 | 1.7.3 | Fabio 未规范化路径致访问控制绕过；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-131202](CVE-2026-131202) | Splunk Enterprise Security | 3.1 9.1 (Splunk) | Splunk Enterprise Security <8.7.0 | 8.7.0 | Splunk Enterprise Security REST API 路径遍历致 RCE；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-131199](CVE-2026-131199) | Splunk Enterprise Security | 3.1 8.8 (Splunk) | Splunk Enterprise Security <8.7.0 | 8.7.0 | Splunk ES 任意 SPL 命令执行；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-131236](CVE-2026-131236) | Splunk Enterprise Security | 3.1 8.8 (Splunk) | Splunk Enterprise Security <8.7.0 | 8.7.0 | Splunk ES 存储型 SPL 注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-131246](CVE-2026-131246) | Splunk SOAR | 3.1 8.8 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 | Splunk SOAR 审批越权读外部提示；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-131252](CVE-2026-131252) | Splunk SOAR | 3.1 8.8 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 | Splunk SOAR 跨租户资产篡改；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-131261](CVE-2026-131261) | Splunk SOAR | 3.1 8.8 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 | Splunk SOAR 恶意应用安装致任意代码执行；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-131263](CVE-2026-131263) | Splunk SOAR | 3.1 8.8 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 | Splunk SOAR 连接器应用任意文件写入致 RCE；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-131269](CVE-2026-131269) | Splunk SOAR | 3.1 8.8 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 | Splunk SOAR 应用验证致任意代码执行；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-131270](CVE-2026-131270) | Splunk SOAR | 3.1 8.8 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 | Splunk SOAR 仓库路径穿越致任意文件写；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-131271](CVE-2026-131271) | Splunk SOAR | 3.1 8.8 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 | Splunk SOAR 斜杠命令越权读凭据；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-131295](CVE-2026-131295) | Splunk SOAR | 3.1 8.8 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 | Splunk SOAR 越权子 playbook 执行；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-131258](CVE-2026-131258) | Splunk SOAR | 3.1 8.7 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 | Splunk SOAR 笔记存储型 XSS；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-131260](CVE-2026-131260) | Splunk SOAR | 3.1 8.7 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 | Splunk SOAR 容器导入存储型 XSS；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-131203](CVE-2026-131203) | Splunk Enterprise Security | 3.1 8.3 (Splunk) | Splunk Enterprise Security <8.7.0 | 8.7.0 | Splunk ES 风险排除宏篡改致 SPL 执行；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-131209](CVE-2026-131209) | Splunk Enterprise Security | 3.1 8.3 (Splunk) | Splunk Enterprise Security <8.7.0 | 8.7.0 | Splunk ES UEBA 实体风险评分 SPL 注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-131215](CVE-2026-131215) | Splunk Enterprise Security | 3.1 8.3 (Splunk) | Splunk Enterprise Security <8.7.0 | 8.7.0 | Splunk ES UEBA 发现排除规则 SPL 注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-131218](CVE-2026-131218) | Splunk Enterprise Security | 3.1 8.3 (Splunk) | Splunk Enterprise Security <8.7.0 | 8.7.0 | Splunk ES Mission Control 仪表盘 SPL 注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-131293](CVE-2026-131293) | Splunk SOAR | 3.1 8.3 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 | Splunk SOAR playbook 运行数据越权读写；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-104129](CVE-2026-104129) | pREST | 3.1 8.1 (GHSA) | pREST <2.4.0 | 2.4.0 | pREST _groupby 参数 SQL 注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-123891](CVE-2026-123891) | SDDC Manager | 3.1 8.1 (VMware) | SDDC Manager 9.1.x.x / 9.0.x.x / 5.x | 9.1.1.0200 / 9.0.2.0100 / 5.2.5 | SDDC Manager SQL 注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-131200](CVE-2026-131200) | Splunk Enterprise Security | 3.1 8.1 (Splunk) | Splunk Enterprise Security <8.7.0 | 8.7.0 | Splunk ES 威胁情报查询生成 SPL 执行；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-131210](CVE-2026-131210) | Splunk Enterprise Security | 3.1 8.1 (Splunk) | Splunk Enterprise Security <8.7.0 | 8.7.0 | Splunk ES UEBA 发现排除查找 SPL 注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-131282](CVE-2026-131282) | Splunk SOAR | 3.1 8.1 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 | Splunk SOAR 诊断日志包泄露密码重置凭据；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-131297](CVE-2026-131297) | Splunk SOAR | 3.1 8.1 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 | Splunk SOAR 身份提供方绑定缺失致越权认证；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-133493](CVE-2026-133493) | DIR-600L | 4.0 9.3 (VulDB); 3.1 10.0 (VulDB) | D-Link DIR-600L 2.17b02 | No fixed firmware confirmed | D-Link DIR-600L gena.cgi 命令注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-20320](CVE-2026-20320) | Cisco BroadWorks | 3.1 7.5 (Cisco) | BroadWorks earlier than RI.2026.07 | RI.2026.07 | Cisco BroadWorks 未授权 XXE；已确认在野利用（KEV 2026-11-10），暂无公开 PoC | 已确认 | 待复现 |
| [CVE-2026-111793](CVE-2026-111793) | Openwave Webtop Media Transcoder | 3.1 4.3 (MITRE) | Webtop Media Transcoder < 1.1.22.0 | 1.1.22.0 | Openwave Webtop 媒体转码器文件类型限制绕过；已确认在野利用（KEV 2026-11-10），暂无公开 PoC | 已确认 | 待复现 |
| [CVE-2026-126262](CVE-2026-126262) | FortiAnalyzer / FortiManager | 3.1 9.8 (Fortinet) | FortiAnalyzer 8.0.0-8.0.1 / 7.6.0-7.6.7 / 7.4.0-7.4.11 / 7.2.0-7.2.12; FortiManager (FA features) 8.0.0 / 7.6.0-7.6.7 / 7.4.0-7.4.11 / 7.2.0-7.2.12 | FortiAnalyzer 8.0.2 / FortiManager 8.0.1 / 7.6.8 / 7.4.12 / 7.2.13 | FortiAnalyzer/FortiManager OFTP 服务 SQL 注入；仅版本检查工具、未核实 | 已确认 | 待复现 |
| [CVE-2026-126261](CVE-2026-126261) | FortiManager | 3.1 9.8 (Fortinet) | FortiManager 8.0.0 / 7.6.0-7.6.7 / 7.4.0-7.4.5 / 7.2.0-7.2.8 | 8.0.1 / 7.6.8 / 7.4.6 / 7.2.9 | FortiManager FGFM 服务注册密码验证前授权不当；仅版本检查工具、未核实 | 已确认 | 待复现 |
| [CVE-2026-126259](CVE-2026-126259) | FortiOS | 3.1 9.8 (Fortinet) | FortiOS 8.0.0 / 7.6.0-7.6.7 / 7.4.0-7.4.12 / 7.2.0-7.2.13 / 7.0 all | 8.0.1 / 7.6.8 / 7.4.13 / 7.2.14 (7.0 migrate) | FortiOS 高可用集群缺失认证；仅版本检查工具、未核实 | 已确认 | 待复现 |
| [CVE-2026-126254](CVE-2026-126254) | FortiOS / FortiSASE | 3.1 9.6 (Fortinet) | FortiOS 8.0.0-8.0.1 / 7.6.0-7.6.7 / 7.4.0-7.4.12 / 7.2.0-7.2.13; FortiSASE 26.3.1, 26.2/26.1/25.x | 8.0.2 / 7.6.8 / 7.4.13 / 7.2.14; FortiSASE 26.3.2 (26.2 and earlier migrate) | FortiOS/FortiSASE BGP 守护进程数值截断；仅版本检查工具、未核实 | 已确认 | 待复现 |
| [CVE-2026-126253](CVE-2026-126253) | FortiOS / FortiSASE | 3.1 9.3 (Fortinet) | FortiOS 8.0.0-8.0.1 / 7.6.0-7.6.7 / 7.4.0-7.4.12 / 7.2.0-7.2.13 / 7.0.1-7.0.19; FortiSASE 26.3.1, 26.2/26.1/25.x | 8.0.2 / 7.6.8 / 7.4.13 / 7.2.14; FortiSASE 26.3.2 (26.2 and earlier, 7.0 migrate) | FortiOS/FortiSASE OSPF 认证绕过；仅版本检查工具、未核实 | 已确认 | 待复现 |
| [CVE-2026-126229](CVE-2026-126229) | FortiManager / FortiAnalyzer | 3.1 9.1 (Fortinet) | FortiManager / FortiAnalyzer 8.0.0-8.0.1 / 7.6.0-7.6.7 / 7.4.0-7.4.11 / 7.2.0-7.2.12 / 7.0 all | 8.0.2 / 7.6.8 / 7.4.12 / 7.2.13 (7.0 migrate) | FortiManager/FortiAnalyzer dmserver 用户可控键授权绕过；仅版本检查工具、未核实 | 已确认 | 待复现 |
| [CVE-2026-126260](CVE-2026-126260) | FortiAnalyzer / FortiManager | 3.1 9.0 (Fortinet) | FortiAnalyzer / FortiManager 8.0.0 / 7.6.0-7.6.7 / 7.4.0-7.4.11 (7.2 not affected) | 8.0.1 / 7.6.8 / 7.4.12 | FortiAnalyzer/FortiManager OFTP 服务服务端请求伪造；仅版本检查工具、未核实 | 已确认 | 待复现 |
| [CVE-2026-133993](CVE-2026-133993) | D-Link DIR-600L | 4.0 9.3 (NVD); 3.1 10.0 (NVD) | 2.17b02 |  | gena.cgi GENA 处理器经 service 参数栈溢出；仅检测型 PoC | 已确认 | 待复现 |
| [CVE-2026-105016](CVE-2026-105016) | Microsoft QUIC (msquic) | 3.1 9.8 (Microsoft) | Microsoft QUIC (msquic) before the October 13, 2026 fixes; any service built on a vulnerable msquic (HTTP/3 servers, QUIC services) | Microsoft October 13, 2026 updates — Windows 11 builds 10.0.26100.9711 / 10.0.26200.9711 / 10.0.26300.9711 (KB5127648); .NET 8.0.32 / 9.0.21 / 10.0.14 | CWE-122; 本地/Docker 实验室 RCE | 已确认 | 待复现 |
| [CVE-2026-133680](CVE-2026-133680) | D-Link DCS-935L | 3.1 9.9 (VulDB); 4.0 8.6 (VulDB) | D-Link DCS-935L 1.10.01 | Unknown — no fixed firmware version identified in VulDB/NVD as of 2026-11-22 | CWE-78; 本地/Docker 实验室 RCE | 已确认 | 待复现 |
| [CVE-2026-129794](CVE-2026-129794) | SOES (Simple Open EtherCAT Slave) | 3.1 8.8 (RT-Labs) | SOES up to and including 3.2.0 | 3.2.1 | CWE-787; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-129796](CVE-2026-129796) | SOES (Simple Open EtherCAT Slave) | 3.1 8.8 (RT-Labs) | SOES up to and including 3.2.0 | 3.2.1 | CWE-191; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-133985](CVE-2026-133985) | TEW-657BRM | 3.1 8.8 (VulDB); 4.0 7.4 (VulDB) | TEW-657BRM 1.00.1 |  | CWE-119; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-134352](CVE-2026-134352) | Rclone | 4.0 9.2 (VulnCheck); 3.1 8.1 (VulnCheck) | Rclone from 1.51.0 before 1.76.0 | 1.76.0 | CWE-287; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-124010](CVE-2026-124010) | XWEB EVO | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | XWEB EVO before 5.6.2 | 5.6.2 | CWE-78; 本地/Docker 实验室 RCE | 已确认 | 待复现 |
| [CVE-2026-124014](CVE-2026-124014) | XWEB EVO | 4.0 8.8 (VulnCheck); 3.1 9.1 (VulnCheck) | XWEB EVO 4.3.0 through 5.8.8 |  | CWE-306; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-102764](CVE-2026-102764) | BeyondTrust Remote Support | 4.0 9.3 (NVD) | BeyondTrust Remote Support <= 26.2.3 (self-hosted); Privileged Remote Access shares the affected code | BT26-05-RS patch (supported builds 24.3.1-26.2.3); BeyondTrust-hosted SaaS auto-patched 2026-10-08/09 | CWE-290; 本地/Docker 实验室 RCE; 公开 RCE | 已确认 | 待复现 |
| [CVE-2026-103782](CVE-2026-103782) | Dell Enterprise Sonic Distribution | 3.1 9.9 (Dell) | Dell Enterprise Sonic Distribution prior to 4.6.1 | 4.6.1 | CWE-88; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-135171](CVE-2026-135171) | Wing FTP Server | 4.0 9.2 (VulnCheck); 3.1 8.1 (VulnCheck) | Wing FTP Server before 8.2.8 | 8.2.8 | CWE-341; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-115873](CVE-2026-115873) | Cribl Stream | 4.0 8.7 (Cribl); 3.1 9.9 (Cribl) | Cribl Stream 4.20.4 and earlier | 4.21.0 | CWE-94; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-115899](CVE-2026-115899) | Cribl Stream | 4.0 9.3 (Cribl); 3.1 9.8 (Cribl) | Cribl Stream 4.20.4 and earlier | 4.21.0 | CWE-94; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-115901](CVE-2026-115901) | Cribl Stream | 4.0 8.5 (Cribl); 3.1 9.0 (Cribl) | Cribl Stream 4.20.4 and earlier | 4.21.0 | CWE-79; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-134882](CVE-2026-134882) | TOTOLINK A7100RU | 4.0 10.0 (VulDB); 3.1 10.0 (VulDB) | TOTOLINK A7100RU 7.4cu.2313_B20191024 |  | CWE-77; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-101218](CVE-2026-101218) | Dell Enterprise Sonic Distribution | 3.1 8.2 (Dell) | Dell Enterprise Sonic Distribution before 4.6.1 | 4.6.1 | CWE-78; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-103783](CVE-2026-103783) | Dell Enterprise Sonic Distribution | 3.1 8.2 (Dell) | Dell Enterprise Sonic Distribution before 4.6.1 | 4.6.1 | CWE-78; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-103788](CVE-2026-103788) | Dell Enterprise Sonic Distribution | 3.1 9.6 (Dell) | Dell Enterprise Sonic Distribution before 4.6.1 | 4.6.1 | CWE-78; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-134624](CVE-2026-134624) | N-able MailAssure (SpamExperts) | 4.0 9.3 (N-able) | N-able MailAssure (SpamExperts) before 20261121.1943 | 20261121.1943 | CWE-918; 仅版本检测 | 已确认 | 待复现 |
| [CVE-2026-110631](CVE-2026-110631) | Komodo Periphery | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | Komodo through 2.3.3 (default install: no core_public_keys / passkeys configured) |  | CWE-1188; 本地/Docker 实验室 RCE | 已确认 | 待复现 |

### 运行环境 / 框架 / 浏览器 (88)

| 编号 | 产品 | 评分 | 受影响版本 | 修复版本 | 判定 | CVE 状态 | 复现 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [CVE-2026-57898](CVE-2026-57898) | Eclipse BaSyx Java Server SDK | 3.1 9.0 (Eclipse) | Eclipse BaSyx Java Server SDK 2.0.0-milestone-05–2.0.0-milestone-12 (MongoDB backend) | 2.0.0-milestone-13 | Eclipse BaSyx AAS 缩略图接口未授权任意文件写入（MongoDB 后端）；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-114938](CVE-2026-114938) | OpenJDK Base64（Java4Shell） | 4.0 9.2 (Calif)；3.1 8.1 (Oracle)；3.1 9.8 (Red Hat) | OpenJDK 17.0.6 and later on x86-64 with AVX-512 VBMI (17/21/25/27 lines; Oracle also lists Java 8 Performance Pack 8u511b33-perf) | vendor November 2026 CPU / OpenJDK 17.0.21.1, 21.0.13.1 and equivalent distributor builds | 触发 / 崩溃 / 泄露 / 实验；没有公开通用 RCE | 已确认 | ◐ 部分 |
| [CVE-2026-90436](CVE-2026-90436) | Apache Axis 1.x | 3.1 9.8 (CISA-ADP) | Apache Axis 1.x through 1.4 | 无修复版本（EOL；修复仅存于上游 commit 41f3b4e8） | 未认证类实例化的实验室复现；默认 classpath 上未证实 RCE | 已确认 | ◐ 部分 |
| [CVE-2024-27834](CVE-2024-27834) | WebKit (Apple) | 3.1 5.5 (NVD) | Safari < 17.5；iOS/iPadOS < 16.7.8 及 17.x < 17.5；macOS < 14.5；tvOS < 17.5；watchOS < 10.5；WebKitGTK / WPE WebKit < 2.44.2 | Safari 17.5；iOS 16.7.8 / iOS 17.5；iPadOS 16.7.8 / iPadOS 17.5；macOS Sonoma 14.5；tvOS 17.5；watchOS 10.5 | 仅分析；无可运行 PoC | 已确认 | — 无目标 |
| [CVE-2026-126187](CVE-2026-126187) | React Server Components / Next.js | 4.0 9.5 (GHSA) | react-server-dom-* 19.0.0–19.3.0; Next.js 16.0.0–16.4.0 (App Router + Cache Components) | react-server-dom-* 19.0.9 / 19.1.10 / 19.2.9 / 19.3.1; Next.js 16.4.1 | 实验室 Docker 应用中的 RCE；触发需要罕见条件 | 已确认 | ◐ 部分 |
| [CVE-2026-125350](CVE-2026-125350) | Google Chrome | 3.1 8.8 (NVD) | Chrome < 157.0.8103.50 | 157.0.8103.50 / .51 (Windows, macOS), 157.0.8103.50 (Linux, Android), Extended Stable 156.0.8078.96 | 通过回归测试文件触发渲染器崩溃；无 RCE payload | 已确认 | ✅ 完整 |
| [CVE-2026-111497](CVE-2026-111497) | Node.js Brotli | 4.0 9.2 (Google)；3.1 9.8 (NVD) | Node.js < 22.23.4, < 24.22.1, < 26.12.1; Bun < 1.4.4; Brotli 1.0.3-1.2.0 | Node.js 22.23.4 / 24.22.1 / 26.12.1; Bun 1.4.4; Brotli 1.2.1 | 经畸形 Brotli 流验证的远程 DoS；RCE 仅为分析 | 已确认 | ◐ 部分 |
| [CVE-2026-129349](CVE-2026-129349) | Apache Shiro DefaultLdapRealm | 4.0 9.1 (Apache) | Apache Shiro through 3.0.0 with DefaultLdapRealm/JndiLdapRealm and authenticationCachingEnabled=true (not the default) | 3.0.1 | 一次有效登录后认证绕过；启用缓存（非默认）时任意密码通过 | 已确认 | ◐ 部分 |
| [CVE-2026-86829](CVE-2026-86829) | Apache Airflow 核心 | 3.1 8.8 (Apache) | apache-airflow-core < 3.4.0 | 3.4.0 (apache/airflow PR #72718) | DAG 作者经 XCom 反序列化在调度器 RCE；3.3.2 实验室验证，3.4.0 干净 | 已确认 | ◐ 部分 |
| [CVE-2026-115560](CVE-2026-115560) | PHP session 上传进度 | 4.0 9.2 (PHP) | PHP with session.serialize_handler=php_binary or php_serialize in server config, application switching to php at runtime via ini_set() before session_start(), and session.upload_progress.enabled=1 (PHP default). Validated on php:8.4.27-apache. | 8.5.13 / 8.4.28 / 8.3.37 / 8.2.36 (2026-11-19) | 实验室中经 session 处理器错配未认证 RCE（php:8.4.27-apache）；已于 8.5.13/8.4.28/8.3.37/8.2.36 修复，缓解是关闭上传进度 | 已确认 | ◐ 部分 |
| [CVE-2026-75604](CVE-2026-75604) | Windows 上的 Next.js | 3.1 9.0 (GHSA) | Next.js 13.4.0–15.5.23 and 16.0.0–16.3.2 on Windows, Pages Router + App Router without Cache Components | 15.5.24 / 16.3.3 | 经 Server Actions 加密密钥泄露未认证 RCE；需 Windows 主机与 Pages/App Router，实验室在 next@16.2.11 验证 | 已确认 | — 无目标 |
| [CVE-2026-115893](CVE-2026-115893) | Wasmtime | 3.1 9.9 (GHSA) | Wasmtime < 36.0.19, 37.0.0-42.x, 43.0.0-48.0.6, 49.0.0-49.0.3 (aarch64 Cranelift) | 36.0.19, 48.0.7, 49.0.4 | aarch64 JIT 沙箱逃逸至宿主代码执行（实验室）；49.0.3 上 5/5 成功，49.0.4 拒绝 | 已确认 | 待复现 |
| [CVE-2026-109618](CVE-2026-109618) | PHP | 3.1 9.8 (NVD)；4.0 9.2 (PHP) | PHP 5.4.0-8.5.11 | 8.2.35, 8.3.36, 8.4.27, 8.5.12 | 预认证 RCE 链 A/B/C 公开（D/E 付费）；实验室在 PHP 5.4–8.5.11 验证；已列入 KEV | 已确认 | ◐ 部分 |
| [CVE-2026-109619](CVE-2026-109619) | PHP | 3.1 8.1 (NVD)；4.0 9.2 (PHP) | PHP 5.4.0-8.5.11 | 8.2.35, 8.3.36, 8.4.27, 8.5.12 | FPM worker 跨请求残留状态 UAF/信息泄露 RCE（实验室）；已列入 KEV | 已确认 | — 无目标 |
| [CVE-2026-126910](CVE-2026-126910) | Chrome V8 Maglev | 3.1 8.8 (NVD) | Chrome before 157.0.8103.78 | 157.0.8103.78 | 实验室证实类型混淆 stale load；未转 RCE，需开发者标志 | 已确认 | 待复现 |
| [CVE-2026-128134](CVE-2026-128134) | NLTK dot2img | 3.1 7.8 (GHSA) | NLTK before 3.10.4 | 3.10.4 | 本地 PATH 劫持演示；README 的 7.3/3.9.2 与 GHSA 7.8/3.10.4 冲突 | 已确认 | 待复现 |
| [CVE-2026-130001](CVE-2026-130001) | mustache (Ruby) | 3.1 9.8 (GHSA) | mustache gem <= 1.1.2 | 1.1.3 | 模板无限制方法调用致 RCE；脚本自称，未核实 | 已确认 | 待复现 |
| [CVE-2026-47884](CVE-2026-47884) | Spring Framework XsltView | 3.1 9.8 (GHSA) | Spring Framework 5.2.x–5.3.49, 6.0.x–6.0.30, 6.1.x–6.1.28, 6.2.x–6.2.19, 7.0.0–7.0.8 (XsltView + catch-all /** mapping + implicit view name) | 5.3.50 / 6.0.31 / 6.1.29 / 6.2.20 / 7.0.9 | 攻击者视图名经 XsltView 解析；SSRF 与 XSLT Java 扩展 RCE，未核实 | 已确认 | 待复现 |
| [CVE-2026-131842](CVE-2026-131842) | Poppler pdfdetach | 4.0 5.7 (VulnCheck) | Poppler pdfdetach 24.03.0–26.11.0 | none (upstream work item 1826 open) | pdfdetach 路径穿越，内嵌文件可写到输出目录之外 | 已确认 | 待复现 |
| [CVE-2026-131873](CVE-2026-131873) | Gargoyle | 4.0 6.9 (VulnCheck) | Gargoyle 2023.1–2026.1.1 | Spatterlight 1.5.5 import (commit 45385f1) | Plus 解释器 ReadAction() 栈溢出，构造 .plus 文件可使解释器崩溃 | 已确认 | 待复现 |
| [CVE-2026-121265](CVE-2026-121265) | SQL::Abstract | 3.1 9.8 (GHSA) | SQL::Abstract < 2.000003 | 2.000003 | 数组列值当字面 SQL 拼进 insert/update/generate，未认证注入；2.000003 修复 | 已确认 | 待复现 |
| [CVE-2026-107360](CVE-2026-107360) | rubygem-safemode | 3.1 9.6 (Red Hat) | rubygem-safemode through 2.0.3; Red Hat Satellite 6.16–6.18 | upstream PR #75 (unmerged); rubygem-safemode 1.5.0-3.el8sat / 1.5.0-3.el9sat | 复合赋值绕过 safemode Jail 白名单，执行任意无参方法；上游修复 PR 未合并 | 已确认 | 待复现 |
| [CVE-2026-128027](CVE-2026-128027) | FrankenPHP | 4.0 9.3 (VulnCheck) | FrankenPHP images built before 2026-02-04 (< 1.1.11) | 1.1.11 | 陈旧基础层镜像带的 libcrypto 可预认证栈溢出；1.1.11 修复 | 已确认 | 待复现 |
| [CVE-2026-128014](CVE-2026-128014) | FrankenPHP | 4.0 9.2 (VulnCheck); 3.1 8.1 (GHSA) | FrankenPHP 1.13.1 (Brotli 1.2.0); all builds shipping Brotli < 1.2.1 | 1.13.2 (Brotli 1.2.1) | 内置 Brotli 1.2.0 解码死循环；未授权 worker DoS，实验有据 | 已确认 | 待复现 |
| [CVE-2026-123753](CVE-2026-123753) | Apache Axis2/Java | 3.1 9.1 (GHSA) | Apache Axis2/Java < 2.0.2 (PoC tested 2.0.1) | 2.0.2 | WS-Addressing ReplyTo/FaultTo SSRF，完整 SOAP 响应外泄；实验有据 | 已确认 | 待复现 |
| [CVE-2026-132825](CVE-2026-132825) | Ruby | 3.1 7.4 (MITRE) | Ruby < 3.3.14; 3.4.0-< 3.4.13; 4.0.0-< 4.0.10 | 3.3.14 / 3.4.13 / 4.0.10 | 单字节编码大小写转换堆越界写 1 字节；ASAN 崩溃与 glibc 堆元数据损坏，实验有据 | 已确认 | 待复现 |
| [CVE-2026-133168](CVE-2026-133168) | DCMTK | 4.0 8.5 (VulnCheck); 3.1 7.8 (VulnCheck) | DCMTK 3.7.1 | 3.7.2 (patch pending; fix commit c22836c, no release tagged) | JPEG 编码器平面转换堆越界写，未核实 | 已确认 | 待复现 |
| [CVE-2026-133243](CVE-2026-133243) | node-soap | 4.0 8.8 (VulnCheck); 3.1 8.2 (VulnCheck) | node-soap before 1.14.1 | 1.14.1 | WSDL.xmlToObject 原型污染；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-71164](CVE-2026-71164) | Helidon | 3.1 9.8 (Oracle) | Helidon 3.0.0-3.2.17 (Imperative Web Server) | 3.2.18 (Oracle CSPU Aug 2026) | Helidon 命令式 Web 服务器远程代码执行；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-133307](CVE-2026-133307) | ClassiCube | 4.0 8.7 (VulnCheck); 3.1 8.8 (VulnCheck) | ClassiCube before 1.4.0 | 1.4.0 | ClassiCube Png_Decode 堆越界写；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-116499](CVE-2026-116499) | Qiskit SDK | 3.1 8.4 (IBM) | Qiskit SDK v1.4.2-v2.6.2 | 2.6.2 (IBM patched release) | Qiskit SDK QPY 加载反序列化远程代码执行；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-133254](CVE-2026-133254) | IntelliJ IDEA | 3.1 8.3 (JetBrains) | IntelliJ IDEA before 2026.3, 2026.2.4 | 2026.3 / 2026.2.4 | 经 IntelliJ IDEA 代码来源插件代码执行；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-130886](CVE-2026-130886) | @fastify/reply-from | 3.1 8.2 (GHSA) | @fastify/reply-from 12.8.1-12.8.3 | 12.8.4 | @fastify/reply-from 代理路径遍历；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-92937](CVE-2026-92937) | vm2 | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | vm2 3.11.6 | 3.11.7 | vm2 沙箱逃逸远程代码执行；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-0881](CVE-2026-0881) | Firefox | 3.1 10.0 (Mozilla) | Firefox <147, Thunderbird <147 | Firefox 147 / Thunderbird 147 (MFSA2026-01) | Firefox 消息系统沙箱逃逸；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-92940](CVE-2026-92940) | vm2 | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | vm2 3.11.3-3.11.6 | 3.11.7 | vm2 globalAgent 泄露宿主 HTTPS 凭证；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-92941](CVE-2026-92941) | vm2 | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | vm2 3.11.3-<3.11.7 | 3.11.7 | vm2 TLS 信任库篡改；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-92946](CVE-2026-92946) | vm2 | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | vm2 before 3.11.7 | 3.11.7 | vm2 require.external 远程代码执行；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-92947](CVE-2026-92947) | vm2 | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | vm2 before 3.11.7 | 3.11.7 | vm2 Buffer 池内存泄露；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-92955](CVE-2026-92955) | vm2 | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | vm2 before 3.11.8 | 3.11.8 | vm2 NodeVM 沙箱逃逸；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-92956](CVE-2026-92956) | vm2 | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | vm2 3.10.1-3.11.6 | 3.11.7 | vm2 WebAssembly 沙箱逃逸；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-92960](CVE-2026-92960) | vm2 | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | vm2 before 3.11.6 | 3.11.6 | vm2 os/dns 进程级状态泄露；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-92953](CVE-2026-92953) | vm2 | 3.1 10.0 (VulnCheck); 4.0 9.3 (VulnCheck) | vm2 3.11.0-3.11.7 | 3.11.8 | vm2 TypedArray 原型污染；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-92948](CVE-2026-92948) | vm2 | 3.1 9.9 (VulnCheck); 4.0 9.4 (VulnCheck) | vm2 3.9.6-3.11.6 | 3.11.7 | vm2 node:test 沙箱逃逸；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-92951](CVE-2026-92951) | vm2 | 3.1 9.9 (VulnCheck); 4.0 9.4 (VulnCheck) | vm2 before 3.11.7 | 3.11.7 | vm2 模块白名单绕过；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-92957](CVE-2026-92957) | vm2 | 3.1 9.9 (VulnCheck); 4.0 9.4 (VulnCheck) | vm2 through 3.11.6 | 3.11.7 | vm2 NodeVM 内置拒绝列表绕过；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-92944](CVE-2026-92944) | vm2 | 3.1 9.8 (VulnCheck); 4.0 9.3 (VulnCheck) | vm2 3.10.2-3.11.6 | 3.11.7 | vm2 Promise 沙箱逃逸；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-128138](CVE-2026-128138) | NLTK | 3.1 9.8 (GitHub) | NLTK 3.10.3-<3.10.4 | 3.10.4 | NLTK JVM 沙箱绕过；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-92950](CVE-2026-92950) | vm2 | 3.1 8.6 (VulnCheck); 4.0 9.3 (VulnCheck) | vm2 before 3.11.7 | 3.11.7 | vm2 CLI 沙箱逃逸；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-92954](CVE-2026-92954) | vm2 | 3.1 8.6 (VulnCheck); 4.0 9.2 (VulnCheck) | vm2 3.10.0-3.11.7 | 3.11.8 | vm2 宿主 Promise 拒绝服务；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-92958](CVE-2026-92958) | vm2 | 3.1 8.5 (VulnCheck); 4.0 8.4 (VulnCheck) | vm2 through 3.11.6 | 3.11.7 | vm2 fs/promises 拒绝列表绕过；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-92943](CVE-2026-92943) | AWS IoT Device SDK for Python | 3.1 8.1 (AMZN); 4.0 9.2 (AMZN) | AWS IoT Device SDK for Python 1.5.3-1.6.0 | 1.6.1 | AWS IoT Device SDK 证书主机名校验缺失；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-130235](CVE-2026-130235) | Okta .NET SDK Abstractions | 3.1 8.7 (Okta) | Okta .NET SDK Abstractions 1.0.0-beta-4.0.7 | 4.0.8 | Okta .NET SDK 请求 URL 校验缺失（SSWS 令牌外泄）；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-130179](CVE-2026-130179) | Okta .NET SDK Abstractions | 3.1 8.5 (Okta) | Okta .NET SDK Abstractions 3.0.0-4.0.7 | 4.0.8 | Okta .NET SDK 凭据覆盖；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-61798](CVE-2026-61798) | netty-incubator-codec-ohttp | 3.1 8.1 (GitHub) | netty-incubator-codec-ohttp <0.0.23.Final | 0.0.23.Final | netty-incubator-codec-ohttp HPKE 私钥泄露；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-130234](CVE-2026-130234) | Okta Swift Management SDK | 3.1 8.0 (Okta) | Okta Swift Management SDK <0.1.1 | 0.1.1 | Okta Swift SDK 路径参数编码缺失；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-130756](CVE-2026-130756) | pnpm exe | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | pnpm exe <10.34.8, 11.x <11.28.8 | 10.34.8 / 11.28.8 | pnpm exe 信任已泄露 eMudhra 中间 CA；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2019-25782](CVE-2019-25782) | ThinkPHP | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | ThinkPHP 5.0.0-5.0.23 | 5.0.24 | ThinkPHP 5.0 _method 构造器代码注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2012-20007](CVE-2012-20007) | ThinkPHP | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | ThinkPHP 2.0-2.2 / 3.0 Lite | No known patch | ThinkPHP Dispatcher PATH_INFO eval 注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-83020](CVE-2026-83020) | Oracle Platform Security for Java | 3.1 10 (Oracle) | Oracle Platform Security for Java 12.2.1.4.0 / 14.1.2.0.0 | September 2026 Critical Security Patch Update | Oracle Platform Security for Java 未授权接管；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-82994](CVE-2026-82994) | Oracle Platform Security for Java | 3.1 9.8 (Oracle) | Oracle Platform Security for Java 12.2.1.4.0 / 14.1.2.0.0 | September 2026 Critical Security Patch Update | Oracle Platform Security for Java 未授权接管（LDAP）；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-82995](CVE-2026-82995) | Oracle Platform Security for Java | 3.1 9.8 (Oracle) | Oracle Platform Security for Java 12.2.1.4.0 / 14.1.2.0.0 | September 2026 Critical Security Patch Update | Oracle Platform Security for Java 未授权接管（SOAP）；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-91570](CVE-2026-91570) | Oracle WebLogic Server | 3.1 9.8 (Oracle) | Oracle WebLogic Server 12.2.1.4.0 / 14.1.1.0.0 / 14.1.2.0.0 / 15.1.1.0.0 | November 2026 Critical Patch Update | Oracle WebLogic Server 未授权接管（TopLink，HTTP）；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-91583](CVE-2026-91583) | Oracle WebLogic Server | 3.1 9.8 (Oracle) | Oracle WebLogic Server 12.2.1.4.0 / 14.1.1.0.0 / 14.1.2.0.0 / 15.1.1.0.0 | November 2026 Critical Patch Update | Oracle WebLogic Server 未授权接管（TopLink，HTTP）；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-91585](CVE-2026-91585) | Oracle WebLogic Server | 3.1 9.8 (Oracle) | Oracle WebLogic Server 12.2.1.4.0 / 14.1.1.0.0 / 14.1.2.0.0 / 15.1.1.0.0 | November 2026 Critical Patch Update | Oracle WebLogic Server 未授权接管（TopLink，TCP）；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-103119](CVE-2026-103119) | Apache Tomcat | 3.1 9.1 (NVD) | Apache Tomcat 11.0.0-M25 to 11.0.26 | 11.0.27 | Apache Tomcat AJP 响应串扰致数据泄露；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-133528](CVE-2026-133528) | BeamNG.drive | 4.0 9.3 (VulnCheck); 3.1 8.6 (VulnCheck) | BeamNG.drive <0.40.6 | 0.40.6 | BeamNG.drive LuaJIT 沙箱逃逸致 RCE；真实 exploit（drbloop2000）+ 检测型 PoC（fankh），未核实 | 已确认 | 待复现 |
| [CVE-2026-127064](CVE-2026-127064) | @fastify/reply-from | 3.1 8.2 (OpenJSF) | @fastify/reply-from <12.8.4 | 12.8.4 | @fastify/reply-from 分号路径参数绕过致路径穿越；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-117659](CVE-2026-117659) | InfoScan | 4.0 8.5 (CISA); 3.1 8.1 (CISA) | Dorsett Controls InfoScan <=1.45.0 | 1.46 | InfoScan Electron 客户端 TLS 证书校验缺失；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-129496](CVE-2026-129496) | PHP | 4.0 9.2 (PHP Group) | PHP 8.2 <8.2.36 / 8.3 <8.3.37 / 8.4 <8.4.28 / 8.5 <8.5.13 | 8.2.36 / 8.3.37 / 8.4.28 / 8.5.13 | PHP 时区缓存释放后使用致远程代码执行；lab 型 PoC，未在本仓核实 | 已确认 | 待复现 |
| [CVE-2026-129474](CVE-2026-129474) | PHP | 4.0 9.2 (PHP Group) | PHP 8.5.0–<8.5.13 | 8.5.13 | PHP 垃圾回收器魔术方法回溯释放后重用；触发型 PoC，RCE 未证实、未核实 | 已确认 | 待复现 |
| [CVE-2026-126714](CVE-2026-126714) | PHP | 4.0 9.2 (PHP Group) | PHP 8.2 <8.2.36 / 8.3 <8.3.37 / 8.4 <8.4.28 / 8.5 <8.5.13 | 8.2.36 / 8.3.37 / 8.4.28 / 8.5.13 | PHP 会话文件部分覆盖导致反序列化 RCE；Docker 实验室内含参考利用，仅实验室 RCE、未核实 | 已确认 | 待复现 |
| [CVE-2026-129289](CVE-2026-129289) | PHP | 4.0 9.2 (PHP Group) | PHP 8.2 <=8.2.35 / 8.3 <=8.3.36 / 8.4 <=8.4.27 / 8.5 <=8.5.12 | 8.2.36 / 8.3.37 / 8.4.28 / 8.5.13 | PHP-FPM 请求走私；需复用后端连接；触发型 PoC，RCE 未证实、未核实 | 已确认 | 待复现 |
| [CVE-2026-133212](CVE-2026-133212) | @fastify/reply-from | 3.1 9.0 (OpenJSF) | @fastify/reply-from before 12.9.1 | 12.9.1 | 无请求体时仍转发 Content-Length 致 HTTP 请求走私；仅检测型 PoC、未核实 | 已确认 | 待复现 |
| [CVE-2026-77355](CVE-2026-77355) | isomorphic-git | 3.1 8.8 (GHSA) | isomorphic-git before 1.38.7 (Windows NTFS) | 1.38.7 | 恶意仓库经 Windows NTFS 保留路径别名污染 .git 元数据；仅检测型 PoC、未核实 | 已确认 | 待复现 |
| [CVE-2026-86017](CVE-2026-86017) | isomorphic-git | 3.1 8.0 (GHSA) | isomorphic-git before 1.38.8 (cherry-pick symlink) | 1.38.8 | cherry-pick 跟随符号链接将攻击者 blob 写到工作树外；仅检测型 PoC、未核实 | 已确认 | 待复现 |
| [CVE-2026-104711](CVE-2026-104711) | Apache Struts | 3.1 9.8 (NVD); 3.1 8.1 (Apache) | 2.0.0-2.3.37, 2.5.0-2.5.33, 6.0.0-6.11.0, 7.0.0-7.3.0 | 6.12.0 (6.x), 7.4.0 (7.x) | legacy RestfulActionMapper 的 OGNL 注入；PoC 在 Docker lab 中演示 eval 与 exec，输出经 X_Matched_Action 回显；exec 需 lab guard 放宽 | 已确认 | 待复现 |
| [CVE-2026-133325](CVE-2026-133325) | Apache Tomcat | 3.1 9.8 (NVD) | 11.0.28-11.0.29, 10.1.62, 9.0.124 |  | Apache Tomcat 密钥交换无实体认证；PoC 仅做版本指纹检测，不实施密钥交换攻击（需 MITM 位置）；PoC 自称范围与通告不符，未核实 | 已确认 | 待复现 |
| [CVE-2026-95517](CVE-2026-95517) | Apache Tomcat | 3.1 9.1 (NVD) | 11.0.0-M1-11.0.27, 10.1.0-M1-10.1.61, 9.0.13-9.0.123 | 11.0.29, 10.1.62, 9.0.124 | Apache Tomcat EncryptInterceptor 无完整性校验；PoC 仅做 token 位翻转篡改探测 | 已确认 | 待复现 |
| [CVE-2026-124626](CVE-2026-124626) | @fastify/express | 3.1 9.1 (NVD) | 4.0.5-4.0.9 | 4.0.10 | CWE-287; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-129504](CVE-2026-129504) | @fastify/express | 3.1 9.1 (NVD) | 4.0.0-4.0.9 | 4.0.10 | CWE-436; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-133120](CVE-2026-133120) | @fastify/express | 3.1 9.1 (NVD) | < 4.0.10 | 4.0.10 | CWE-174; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-133250](CVE-2026-133250) | @fastify/middie | 3.1 9.1 (NVD) | <= 9.3.7 | 9.3.8 | CWE-288; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-133867](CVE-2026-133867) | @fastify/express | 3.1 9.1 (NVD) | 4.0.7-4.0.9 | 4.0.10 | CWE-287; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-134814](CVE-2026-134814) | binary-parser | 4.0 9.2 (VulnCheck); 3.1 8.1 (GHSA) | binary-parser before 2.3.1 | 2.3.1 | CWE-94; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-134815](CVE-2026-134815) | simple-git | 4.0 9.2 (VulnCheck); 3.1 8.1 (VulnCheck) | simple-git before 4.1.0 | 4.1.0 | CWE-88; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-125396](CVE-2026-125396) | Ghostscript | 4.0 8.5 (VulnCheck); 3.1 7.8 (VulnCheck) | Ghostscript before 10.08.0 | 10.08.0 | CWE-648; PoC 在实验室复现 | 已确认 | 待复现 |
| [CVE-2026-129975](CVE-2026-129975) | gpgme | 3.1 8.1 (Red Hat) | gpgme |  | CWE-415; PoC 触发漏洞 | 已确认 | 待复现 |

### 数据库 (18)

| 编号 | 产品 | 评分 | 受影响版本 | 修复版本 | 判定 | CVE 状态 | 复现 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [CVE-2026-118383](CVE-2026-118383) | MongoDB Server 复制 | unknown | 8.0.x before 8.0.37 (8.0.34 tested); 8.2.12 still reproduced at collection time | 8.0.37 (SERVER-138175, SERVER-138119) | 实验室 UAF 崩溃，未证实代码执行 | 已确认 | — 无目标 |
| [CVE-2026-116366](CVE-2026-116366) | ClickHouse Server | 4.0 9.5 (ClickHouse) | ClickHouse 26.3 < 26.3.62.3-lts, 26.8 < 26.8.36.3-lts, 26.9 < 26.9.27.3-stable, 26.10 < 26.10.3.7-stable | 26.3.62.3-lts / 26.8.36.3-lts / 26.9.27.3-stable / 26.10.3.7-stable (2026-10-30) | 自称未认证 RCE；实验室仅验证 differential 检测 + 武器化 DoS | 已确认 | ◐ 部分 |
| [CVE-2026-13078](CVE-2026-13078) | MongoDB Server | 3.1 7.7 (MongoDB)；4.0 6.3 (MongoDB) | MongoDB Server 7.0 before 7.0.39, 8.0 before 8.0.28, 8.2 before 8.2.12, 8.3 before 8.3.7 | 7.0.39, 8.0.28, 8.2.12, 8.3.7 | 低权限认证用户经 MozJS 模块加载器本地文件泄露；非 RCE | 已确认 | 待复现 |
| [CVE-2026-73504](CVE-2026-73504) | cassandra-jdbc-wrapper | 3.1 5.5 (GHSA) | cassandra-jdbc-wrapper < 4.16.4; >= 5.0.0, < 5.0.2 | 4.16.4 / 5.0.2 | 认证令牌明文写入 DEBUG 日志；4.16.4/5.0.2 修复，实验有据 | 已确认 | 待复现 |
| [CVE-2026-116244](CVE-2026-116244) | pgAdmin 4 | 3.1 9.6 (NVD)；4.0 7.1 (PostgreSQL) | pgAdmin 4 ≤ 9.18 | 9.19 (2026-10-29) | 服务模式 libpq 用 pgAdmin 服务账号 Kerberos 凭证连攻击者数据库；9.19 修复 | 已确认 | 待复现 |
| [CVE-2026-126837](CVE-2026-126837) | MongoDB Node.js driver | 4.0 9.1 (MongoDB); 3.1 7.4 (MongoDB) | MongoDB Node.js driver 3.3.3 to < 7.8.0 | 7.8.0 | SRV 父域校验绕过致数据库流量劫持；凭证泄露，实验有据 | 已确认 | 待复现 |
| [CVE-2026-119179](CVE-2026-119179) | MongoDB Node.js driver | 4.0 8.3 (MongoDB); 3.1 7.0 (MongoDB) | mongodb >= 6.11.0 < 6.22.0 and >= 7.0.0 < 7.8.0 | 6.22.0 / 7.8.0 | CSOT 超时后带未读回复的连接回池；跨请求数据泄露，未核实 | 已确认 | 待复现 |
| [CVE-2026-115290](CVE-2026-115290) | Elasticsearch | 3.1 7.5 (GHSA) | Elasticsearch 8.10.0–8.19.23, 9.0.0–9.4.8, 9.5.0–9.5.5 (remote_cluster_server enabled) | 8.19.24 / 9.4.9 / 9.5.6 | 远程集群接口鉴权前反序列化致未授权递归 DoS；实验有据 | 已确认 | 待复现 |
| [CVE-2026-126755](CVE-2026-126755) | ArangoDB | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | ArangoDB <3.12.11 | 3.12.11 | ArangoDB 认证绕过；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-116331](CVE-2026-116331) | PostgreSQL | 3.1 8.8 (PostgreSQL) | PostgreSQL < 18.7, 17.12, 16.16, 15.20, 14.25 | 18.7 / 17.12 / 16.16 / 15.20 / 14.25 | PostgreSQL min/max 聚合类型混淆，对象创建者可执行任意代码；检测型 PoC、未核实 | 已确认 | 待复现 |
| [CVE-2026-6460](CVE-2026-6460) | PostgreSQL | 3.1 8.8 (PostgreSQL) | PostgreSQL < 18.7, 17.12, 16.16, 15.20, 14.25 | 18.7 / 17.12 / 16.16 / 15.20 / 14.25 | PostgreSQL 类型混淆，对象创建者可经 ALTER ... SET DATA TYPE 执行任意代码；检测型 PoC、未核实 | 已确认 | 待复现 |
| [CVE-2026-134292](CVE-2026-134292) | SurrealDB | 4.0 9.3 (NVD); 3.1 9.8 (NVD) | < 4.0.0 | 4.0.0 | CWE-862; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-134337](CVE-2026-134337) | ArcadeDB | 4.0 8.7 (VulnCheck); 3.1 8.8 (VulnCheck) | ArcadeDB native-image server builds 26.8.1 before 26.11.1 | 26.11.1 | CWE-693; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-134293](CVE-2026-134293) | SurrealDB | 4.0 8.8 (VulnCheck); 3.1 8.2 (VulnCheck) | SurrealDB 3.1.0 before 4.0.0 | 4.0.0 | CWE-89; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-134295](CVE-2026-134295) | SurrealDB | 4.0 8.7 (VulnCheck); 3.1 8.8 (VulnCheck) | SurrealDB 3.0.0 before 4.0.0 | 4.0.0 | CWE-22; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-134300](CVE-2026-134300) | SurrealDB | 4.0 7.2 (VulnCheck); 3.1 8.1 (VulnCheck) | SurrealDB 2.2.0 before 4.0.0 | 4.0.0 | CWE-863; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-134309](CVE-2026-134309) | SurrealDB | 4.0 8.7 (VulnCheck); 3.1 8.8 (VulnCheck) | SurrealDB 1.0.0 before 4.0.0 | 4.0.0 | CWE-863; PoC 触发漏洞 | 已确认 | 待复现 |
| [CVE-2026-134803](CVE-2026-134803) | DBHub | 3.1 8.1 (VulnCheck); 4.0 7.2 (VulnCheck) | DBHub before 1.7.0 | 1.7.0 | CWE-436; PoC 触发漏洞 | 已确认 | 待复现 |

### 操作系统 / 系统 / DevOps (53)

| 编号 | 产品 | 评分 | 受影响版本 | 修复版本 | 判定 | CVE 状态 | 复现 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [CVE-2026-65094](CVE-2026-65094) | NVIDIA VIRTIO-Net for BlueField | 3.1 9.0 (NVIDIA) | NVIDIA VIRTIO-Net GA <25.10.6; LTS25 <25.10.2; LTS24 <24.10.50; LTS23 1.7.21 and older (BlueField-3) | 25.10.6 (GA) / 25.10.2 (LTS25) / 24.10.50 (LTS24) / 23.10.23 (LTS23) | NVIDIA VIRTIO-Net for BlueField 任意写致代码执行；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-74127](CVE-2026-74127) | AMD Platform Security Processor (PSP) boot ROM | 4.0 9.4 (AMD) | AMD Zen 1 / Zen+ processors (PSP boot ROM) | No fix planned (AMD: boot ROM immutable) | Zen 1/Zen+ PSP boot ROM 签名校验绕过；Google 已在真实硬件验证 PoC，AMD 不修复 | 已确认 | — 无目标 |
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
| [CVE-2026-112611](CVE-2026-112611) | Apple CoreGraphics PDF | 3.1 6.1 (NVD) | iOS before 27.2 / 26.7.2, iPadOS before 27.2 / 26.7.2, macOS before 15.8.2 / 26.7.2 | iOS 27.2 / 26.7.2, macOS Sequoia 15.8.2 / Tahoe 26.7.2 | 设备上验证 PDF 指定地址写原语；尚未实现代码执行 | 已确认 | 待复现 |
| [CVE-2026-99288](CVE-2026-99288) | Linux 内核 TCP | 3.1 5.9 (NVD) | Linux kernel with vulnerable TCP ehash lookup (before upstream commit 4e2b3ef19e0e) | Upstream commit 4e2b3ef19e0e (inet: reject unhashed sockets during established lookups) | 按通告机制重写的竞态触发器；触发内核 panic 需精确抢占 | 已确认 | 待复现 |
| [CVE-2026-129987](CVE-2026-129987) | Dokploy | 3.1 9.9 (GHSA) | Dokploy < 0.31.1 (v0.29.0-v0.31.0 per upstream version archaeology) | 0.31.1 | 认证后 RCE：改库密码命令注入；完整链路自称，未核实 | 已确认 | 待复现 |
| [CVE-2026-43499](CVE-2026-43499) | Linux 内核 rtmutex | 3.1 7.8 (Linux kernel) | Linux kernel rtmutex path (PoC targets 4.14.186+ on realme RMX3031/MT6893) |  | realme RMX3031 内核提权 stage1；root 自称，未核实 | 已确认 | 待复现 |
| [CVE-2026-112477](CVE-2026-112477) | Apple iOS IOSurface | 3.1 7.0 (NVD) | iOS 26.x (tested on iOS 26.4, arm64e) | iOS 26.7.2 / iPadOS 26.7.2 | IOSurface UAF 陈旧条目读取原语；研究型 PoC，未展示提权 | 已确认 | 待复现 |
| [CVE-2026-130587](CVE-2026-130587) | OpenFunction | 3.1 9.9 (GHSA) | OpenFunction through 1.2.0 | no vendor fix (upstream issue #532 OPEN) | 租户 PodSpec 原样进 operator 工作负载；节点逃逸，厂商未修复 | 已确认 | 待复现 |
| [CVE-2026-126978](CVE-2026-126978) | Philips Hue Bridge | 3.0 8.8 (GHSA) | Philips Hue Bridge gen 2 and gen 3 (all firmware prior to patch) | no fixed version published | HAP 配对 TLV8 堆溢出；邻接网络、未授权，未核实 | 已确认 | 待复现 |
| [CVE-2026-126979](CVE-2026-126979) | Philips Hue Bridge | 3.0 8.8 (GHSA) | Philips Hue Bridge gen 2 and gen 3 (all firmware prior to patch) | no fixed version published | ChaCha20 长度下溢跳过 HAP 认证；邻接网络，未核实 | 已确认 | 待复现 |
| [CVE-2026-130335](CVE-2026-130335) | Info-ZIP Zip | 3.1 2.9 (MITRE) | Info-ZIP Zip 3.0, 3.1 beta–3.1c | Debian zip/3.0-16 (quote_arg fix) | 受害者执行 zip -T 时构造的压缩包名可注入命令；需本地前置条件 | 已确认 | 待复现 |
| [CVE-2026-121529](CVE-2026-121529) | FortiClient | 3.1 9.6 (GHSA); 3.1 9.1 (Fortinet) | FortiClient Windows / Windows PAM 7.4.0–7.4.7, 7.2.0–7.2.14; FortiClient Mac 7.4.0–7.4.7 | 7.4.8 / 7.2.15 | 本地 API 源校验缺失；受害者浏览器驱动致 RCE（模型实验），未核实 | 已确认 | 待复现 |
| [CVE-2026-99273](CVE-2026-99273) | Linux 内核 (ksmbd) | unknown | Linux < 7.3.2 with CONFIG_SMB_SERVER | mainline a025c4991a7d8; stable 6.12.117 / 6.18.61 / 7.3.2 | ksmbd 响应缓冲外 2 字节堆越界写；KASAN 证据，暂无评分 | 已确认 | 待复现 |
| [CVE-2026-13043](CVE-2026-13043) | WatchGuard 终端安全 | 4.0 9.3 (WatchGuard) | WatchGuard Endpoint Security < 8.00.26.0012 (Windows) | 8.00.26.0012 | 本地管理员伪造驱动握手直达特权 IOCTL；读 MSR 破 KASLR、任意进程内存读取 | 已确认 | 待复现 |
| [CVE-2026-133274](CVE-2026-133274) | THC-Hydra | 4.0 7.1 (VulnCheck); 3.1 6.5 (VulnCheck) | THC-Hydra through 9.7 | commit 6ab9ad8 (post-9.7, no release tagged) | hydra-http-form.c 的 Set-Cookie 解析栈越界写；恶意服务端可致 Hydra 客户端崩溃，未核实 | 已确认 | 待复现 |
| [CVE-2026-133305](CVE-2026-133305) | sqlmap | 4.0 2.3 (VulnCheck); 3.1 4.3 (VulnCheck) | sqlmap before 1.10.11.89 | 1.10.11.89 | 跨站重定向泄露 Cookie 与 Authorization 头，未核实 | 已确认 | 待复现 |
| [CVE-2026-133189](CVE-2026-133189) | Cinder | 3.1 9.6 (Red Hat) | OpenStack Cinder with SSH-based storage drivers | Upstream patch proposed, no fixed release published (2026-11-19) | Cinder SSH 存储驱动命令注入；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-130778](CVE-2026-130778) | Incus | 4.0 10.0 (VulnCheck); 3.1 10.0 (VulnCheck) | Incus <7.6.0 | 7.6.0 / 6.0.9 LTS | Incus mTLS 证书链认证绕过；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-130786](CVE-2026-130786) | Incus | 4.0 9.4 (VulnCheck); 3.1 9.9 (VulnCheck) | Incus <7.6.0 | 7.6.0 / 6.0.9 LTS | Incus OCI 配置注入致宿主机 root 命令执行；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-132891](CVE-2026-132891) | JetBrains TeamCity | 3.1 9.8 (JetBrains) | TeamCity 2026.1 <2026.1.4, 2025.11 <2025.11.8 | 2026.2 / 2026.1.4 / 2025.11.8 | TeamCity 外部拉取请求致 RCE；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-123890](CVE-2026-123890) | VMware vCenter | 3.1 9.8 (VMware) | vCenter 9.1.x / 9.0.x / 8.0 / 5.x | 9.1.1.0200 / 9.0.2.0200 / 8.0 U3m / 5.2.5 | VMware vCenter 目录服务认证绕过；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-132234](CVE-2026-132234) | TeamCity | 3.1 9.9 (JetBrains) | TeamCity 2026.1 <2026.1.3 / <2025.11.7 | 2026.1.3 / 2025.11.7 | TeamCity Mercurial VCS root 参数注入致 RCE；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-132233](CVE-2026-132233) | TeamCity | 3.1 9.9 (JetBrains) | TeamCity 2026.1 <2026.1.3 / <2025.11.7 | 2026.1.3 / 2025.11.7 | TeamCity 构建属性注入致 RCE；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-132232](CVE-2026-132232) | TeamCity | 3.1 9.9 (JetBrains) | TeamCity 2026.1 <2026.1.3 / <2025.11.7 | 2026.1.3 / 2025.11.7 | TeamCity Perforce 设置参数注入致 RCE；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-132231](CVE-2026-132231) | TeamCity | 3.1 9.9 (JetBrains) | TeamCity 2026.1 <2026.1.3 / <2025.11.7 | 2026.1.3 / 2025.11.7 | TeamCity Perforce 设置字符映射致 RCE；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-130784](CVE-2026-130784) | Incus | 4.0 9.4 (VulnCheck); 3.1 9.9 (VulnCheck) | Incus <7.6.0 | 7.6.0 | Incus 默认项目资源继承越权致宿主 root 代码执行；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-130780](CVE-2026-130780) | Incus | 4.0 9.4 (VulnCheck); 3.1 9.9 (VulnCheck) | Incus <7.6.0 | 7.6.0 | Incus 迁移路径遍历致宿主任意路径写；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-129991](CVE-2026-129991) | Dokploy | 3.1 9.9 (GHSA) | Dokploy <0.31.1 | 0.31.1 | Dokploy 备份前缀命令注入致宿主 RCE；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-129316](CVE-2026-129316) | Dokploy | 3.1 9.9 (GHSA) | Dokploy 0.29.13 to <0.31.0 | 0.31.0 | Dokploy WebSocket 处理器缺授权致成员越权到宿主 root；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-129986](CVE-2026-129986) | Dokploy | 3.1 9.9 (GHSA) | Dokploy <0.31.1 | 0.31.1 | Dokploy mount.deleteFileMount 命令注入致宿主 RCE；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-129989](CVE-2026-129989) | Dokploy | 3.1 9.9 (GHSA) | Dokploy <0.31.1 | 0.31.1 | Dokploy Nixpacks publishDirectory 命令注入致宿主 RCE；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-130759](CVE-2026-130759) | Fleet | 4.0 9.4 (VulnCheck); 3.1 9.9 (VulnCheck) | Fleet 4.71.0 to <4.88.2 | 4.88.2 | Fleet SAML SSO 认证绕过；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-130771](CVE-2026-130771) | Incus | 4.0 8.5 (VulnCheck); 3.1 9.9 (VulnCheck) | Incus <7.6.0 | 7.6.0 | Incus 备份/镜像元数据致宿主文件读写；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-130773](CVE-2026-130773) | Incus | 4.0 9.4 (VulnCheck); 3.1 9.9 (VulnCheck) | Incus <7.6.0 | 7.6.0 | Incus 默认项目资源创建越权；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-126752](CVE-2026-126752) | Dagu | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | Dagu 1.23.0 to <2.0.0 | 2.0.0 | Dagu 未授权 RCE；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-73969](CVE-2026-73969) | AnsibleForms | 3.1 9.8 (GHSA) | AnsibleForms <6.2.1 | 6.2.1 | AnsibleForms 硬编码 JWT 密钥致认证绕过；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-130779](CVE-2026-130779) | Incus | 4.0 8.5 (VulnCheck); 3.1 9.6 (VulnCheck) | Incus <7.6.0 | 7.6.0 | Incus 自定义卷备份快照名路径遍历致宿主目录删除；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-130783](CVE-2026-130783) | Incus | 4.0 9.3 (VulnCheck); 3.1 9.6 (VulnCheck) | Incus <7.6.0 | 7.6.0 | Incus 操作事件泄露令牌且缺授权致完全接管；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-126088](CVE-2026-126088) | OpenPLC Runtime | 4.0 9.2 (CISA); 3.1 8.1 (CISA) | OpenPLC Runtime <=4.2.4 | 4.3.0 | OpenPLC Runtime 竞态致未授权建管理员账号；检测型 PoC，未核实 | 已确认 | 待复现 |
| [CVE-2026-111760](CVE-2026-111760) | Git | 3.1 8.0 (GHSA) | Git 2.50.2、2.51.3、2.52.1、2.53.1、2.54.1、2.55.1、2.56.1 之前版本 | 2.50.2、2.51.3、2.52.1、2.53.1、2.54.1、2.55.1、2.56.1 | CWE-59 | 已确认 | 待复现 |
| [CVE-2026-97631](CVE-2026-97631) | EDK II | 4.0 9.5 (TianoCore); 3.1 8.8 (Red Hat) | TianoCore EDK II NetworkPkg UefiPxeBcDxe（edk2-stable202608 及更早） | 上游主线 PR #13200/#13302（2026-10-15 合并）；Red Hat RHSA-2026:96240 | CWE-787 | 已确认 | 待复现 |
| [CVE-2026-120382](CVE-2026-120382) | Synology DiskStation Manager | 3.1 9.8 (Synology) | DSM before 7.1.1-42962-10 / 7.2.1-69057-14 / 7.2.2-72806-11 / 7.3.2-86009-6 / 7.4.1-90080-2 | 7.4.1-90080-2 / 7.3.2-86009-6 | CWE-88; PoC 触发漏洞 | 已确认 | 待复现 |


点进 CVE 目录看完整判定和引用。
