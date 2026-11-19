# 本批抓取问题

给收录机器人看。分两块：你自己入库时犯的错，和上游仓库自带的缺陷。以后每抓一个源，按同样清单过一遍。

## 1. 机器人入库错误

当前 `main` 的快照把别人的仓库原样摊进了本仓库，看不出这是 Coff0xc 的 CVE 库。

| 问题 | 证据 | 正确做法 |
| --- | --- | --- |
| 单源摊到 CVE 根目录 | `CVE-2026-118383/`、`CVE-2026-123007/`、`CVE-2026-123488/` 的 README 都是上游原文 | 即使只有一个源，也放进 `sources/<作者>-<简称>/`。CVE 根目录只放策展 `README.md` 和 `meta.yaml` |
| 没有钉上游 commit | 整库一次 snapshot，`SOURCE` 记录为零 | 每个源写 `SOURCE.yaml`：url、commit SHA、收录日期、许可证 |
| 评分没有刻度和出处 | 根表一列「评分」：9.2 / 9.5 / 9.2 / 9.8 | 必须带 CVSS 版本和来源。冲突时全列，禁止编一个数 |
| 发明了 9.5 | `CVE-2026-118383` 根表写 9.5；上游 README 没有分数 | 没有出处就写 `unknown`，不准填 |
| 把「完整 RCE」写进索引 | `CVE-2026-123007` 行；上游自己写只打得过新鲜 Docker | 成色看上游自我限定，不看目录名或 `exploit.py` |
| 原样复制坏 README | `CVE-2026-123007/README.md` 链到 `http://exploit/exploit.py`，引用不存在的 gif | 上游文件不改；坏链、缺文件记进 `SOURCE.yaml.issues` |
| 把无关文件收进来 | `douglasmun-lab/CLAUDE.md`；带空格的 HTML 通告稿 | 按删除名单丢掉。不是 PoC、许可证、来源自述就不要 |
| 许可证没登记 | Rapid7 / arkrwn / ashrafzaryouh 无 LICENSE；根目录也无 | `SOURCE.yaml.license` 填 `MIT` 或 `unknown`。未知不能假装有 |
| 日期未核对 | Craft 上游 README 把修复写成 2026-11-06 | 补丁日、通告日、CVE 日、PoC 日分开写。只信 GHSA/厂商，不信 PoC 徽章 |
| 只读检查没有产物 | 规则写了「收录前只读检查」，仓库里没有检查记录 | 每次收录填 `SOURCE.yaml.review` |

## 2. 上游仓库自带的问题

这些问题要记进 `SOURCE.yaml.issues`，不要改上游文件去「修好」。

### CVE-2026-114938（OpenJDK Base64 / Java4Shell）

同一 CVE 五个源，成色差一个数量级。不能当同一个 PoC 收。

| 源 | 它实际是什么 | 问题 |
| --- | --- | --- |
| `ashrafzaryouh/CVE-2026-114938` | 版本检测脚本 | 无 LICENSE。没有利用代码。文件夹名叫 CVE 不等于有 PoC |
| `arkrwn/PoC-CVE-2026-114938-CrashLeak` | 崩溃 / 泄露复现 | 无 LICENSE。不是 RCE |
| `douglasmun/CVE-2026-114938_Java4Shell_lab` | 教学实验，验证溢出和修复 | 带 `CLAUDE.md`（代理指令，会污染以后扫这个仓库的机器人）。`docs/` 里有带空格的 HTML 通告稿，Windows 不友好，也不是 PoC |
| `ikow/java4shell-poc` | 公开材料里最完整的链 | 目录和类名带 Exploit；作者自己写标准容器里没拿到 shell。MIT |
| `r3dvei1/java4shell` | 分析 + 复现套件 | 明确写了没有武器化 RCE。MIT |

公开情报本身也打架：Calif CVSS 4.0 9.2，Oracle CVSS 3.1 8.1，Red Hat CVSS 3.1 9.8。入库时三个都记，索引不要只留 9.2。

### CVE-2026-118383（MongoDB 副本集 UAF）

- 上游 `googlesky/CVE-2026-118383` 质量高：有证据目录、gdb oracle、固定版本对照。MIT。
- 证实的是崩溃 / 内存损坏，不是代码执行。`assisted` 模式还用了测试 failpoint。
- 上游 README 不给 CVSS。禁止用聚合站的「Critical 9」或自己估的 9.5 填进索引当权威分。
- `poc.py` 在 Windows 上会被 Defender 一类引擎隔离。拉取后要核对工作区文件还在，不能把隔离当成「上游没这个文件」。

### CVE-2026-123007（NGINX HTTP/2）

源：`sfewer-r7/CVE-2026-123007`（Rapid7）。

- 无 LICENSE。
- README 把 `exploit/exploit.py` 链成 `http://exploit/exploit.py`（坏链）。
- 引用 `nginx-http2-rce-720p-8x.gif`，仓库里没有这个文件。
- `exploit.py` 只是 300 字节启动器，实现在 `exploit/nginx_rce/`。
- 作者限定：只对本地刚起来的 Docker 演示；并发、旧堆、带宽、代理都会失败。
- 公开评分是 F5 CVSS 4.0 9.2 和 CVSS 3.1 8.1。必须写版本。

### CVE-2026-123488（Craft CMS SQLi）

源：`fixedbyreboot/CVE-2026-123488-POC`。MIT。单文件，结构干净。

- README 写 `Fixed: 4.18.9 / 5.11.2 (2026-11-06)`。厂商 GHSA-qcvp-ggx3-97r6 发布于 2026-10-22；独立综述把修复版本发布放在 2026-09-17；2026-11-06 是 CVE/NVD 日和该 PoC 验证徽章日。三个日期不要并成一个。
- CVSS 3.1 9.8 和 CVSS 4.0 9.3 都有公开值。写清楚用的是哪一个。
- 默认路径会写数据库（堆叠 `UPDATE`）。策展里要标明是写操作，不是探测。

## 3. 以后每条源的固定检查

1. 有没有 LICENSE。
2. README 里的相对链接和图片是否存在。
3. 声称的 impact（RCE / 崩溃 / 检测）和文件实际做的事是否一致。
4. 评分的 CVSS 版本和出处。
5. 补丁日、通告日、CVE 日是否被写成同一个日期。
6. 是否夹带 `CLAUDE.md`、代理规则、社交媒体 HTML、无关二进制。
7. 是否需要执行才能「证明」——本仓库收录前不执行。
