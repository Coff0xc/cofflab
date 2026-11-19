# 收录机器人：拉取 + 改造规范

你维护的是 **Coff0xc 的 CVE 漏洞仓库**，不是别人 PoC 的镜子。上游代码原样嵌进来，目录、评分、日期、成色必须是本仓库的策展层。

读完本文再动手。对照 [`source-issues.md`](source-issues.md) 看上一批错在哪。收完跑 `python tools/check_layout.py`。

## 0. 硬禁止

- 不执行任何 PoC、exploit、`run.sh`、容器、扫描器。
- 不改上游 PoC 逻辑，不补利用链，不修 exploit 让它「更能打」。
- 不把上游 README 放到 CVE 根目录。
- 不编 CVSS、日期、影响面。没有出处就写 `unknown`。
- 不把 `CLAUDE.md`、`AGENTS.md`、`.cursor/`、`.grok/`、`.agents/` 收进来。
- 不把单源文件直接摊在 `CVE-*/` 根下。

## 1. 目标布局

```text
CVE-<YEAR>-<N>/
  README.md          # 本仓库策展说明（中文）。永远是这个文件，不是上游 README
  meta.yaml          # 机器可读事实。索引从这里生成
  sources/
    <author>-<slug>/
      SOURCE.yaml    # 本源的出处钉死
      ...            # 上游快照（可删无关文件，不改编译逻辑）
```

单源也走 `sources/`。作者与简称小写、连字符，例如 `sfewer-r7`、`fixedbyreboot`、`ikow-poc`。

CVE 根目录 **只允许** `README.md`、`meta.yaml`、`sources/`。

## 2. 拉取

1. 确认 CVE ID 格式 `CVE-YYYY-N+`。年份与编号以 NVD/GHSA/厂商为准，不以 GitHub 仓库名为准。
2. 记录输入：`upstream_url`、默认分支、HEAD SHA、收录日期（UTC `YYYY-MM-DD`）。
3. 用 **指定 commit** 做只读快照（`git clone --depth 1` 之后立刻记下 `rev-parse HEAD`，或 `git fetch` + `git checkout <sha>`）。禁止只拷工作区、不记 SHA。
4. 快照之后立刻核对关键文件还在磁盘上（Windows 会把 `poc.py` 一类文件隔离）。缺文件先记 `SOURCE.yaml.issues`，不准假装上游没有。
5. 只读静态看，不运行：
   - `LICENSE` / `COPYING` 是否存在。
   - README 引用的相对路径是否都在树里。
   - 是否有远程下载再执行、硬编码 webhook、不明二进制。
   - README 自称的 impact 和目录/文件名是否一致。
6. 查厂商/NVD/GHSA 的评分和日期，**不要**用 PoC README 当唯一权威。

非 GitHub 源（Exploit-DB、博客、厂商通告）：`upstream` 写原文 URL，`commit` 填 `n/a`，另写 `content_sha256`（对该文件或打包快照）。

## 3. 改造

对每个源：

1. 建 `CVE-YYYY-N/sources/<author>-<slug>/`。
2. 把上游快照放进去，保持相对结构。
3. **删除**（见第 6 节），不要改剩下的 PoC 代码。
4. 写 `SOURCE.yaml`（字段见第 5 节）。坏链、缺文件、过称、无许可证都写进 `issues`，原文不动。
5. 若该 CVE 目录还不存在：从 `_template/CVE-YYYY-NNNNN/` 复制，写 `meta.yaml` 和策展 `README.md`。
6. 若已存在：只追加 `sources/<新源>/`，更新 `meta.yaml.sources` 和策展 README 的来源表。禁止覆盖已有策展结论，除非新证据推翻它，并在 `meta.yaml.notes` 写明。

上游 README 留在 `sources/<id>/README.md`。CVE 根 `README.md` 用第 4 节模板重写。

## 4. 策展 README（CVE 根）

中文。短。按这个顺序，不写利用步骤：

1. 标题：`# CVE-YYYY-N — 产品 漏洞类型`
2. 事实表：产品、CWE、影响版本、修复版本、CVSS（版本 + 分数 + 出处）、本仓库判定的公开成色
3. 「公开材料实际证明了什么」：一句。禁止把实验室 RCE 写成通用未授权 RCE
4. 来源表：目录、上游、许可证、成色
5. 链接到 `meta.yaml`

根目录总索引的「评分」列格式：`4.0 9.2 (F5)` 或 `3.1 9.8 (GHSA)`。多个分数用分号。未知写 `unknown`。

## 5. 机器字段

### `meta.yaml`

```yaml
id: CVE-YYYY-N
aliases: []                 # 例如 [Java4Shell]
product: ""
vendor: ""
cwe: []                     # 例如 [CWE-89]
affected: ""                # 人类可读范围
fixed: ""
advisory:                   # 可空
  - name: GHSA-...
    url: https://...
    published: YYYY-MM-DD
cvss:                       # 可多条。一条都没有就写 []
  - version: "3.1"          # "3.1" | "4.0"
    score: 9.8              # 数字。没有就不要造这条
    vector: ""              # 没有就 ""
    source: ""              # Oracle / F5 / GHSA / NVD / Red Hat / Calif ...
demonstrated: []            # 只许用下面枚举
public_rce: false           # 仅当公开材料对非实验目标证明了代码执行
notes: ""                   # 日期冲突、评分冲突写这里
collected: YYYY-MM-DD
sources:
  - id: author-slug
    path: sources/author-slug
```

`demonstrated` 只许：

`version-check` | `trigger` | `crash` | `leak` | `lab-repro` | `rce-local` | `sqli-read` | `sqli-write` | `priv-esc` | `dos`

`rce-local` = 作者限定在新鲜本地/Docker 实验室。`public_rce: true` 需要作者未加这类限定，且材料表明对真实部署成功。做不到就 `false`。

### `sources/<id>/SOURCE.yaml`

```yaml
id: author-slug
upstream: https://github.com/org/repo
commit: "<40-char sha or n/a>"
collected: YYYY-MM-DD
license: MIT                # 或 unknown / 其他 SPDX
review:
  executed: false
  static: true
  notes: "只读检查：无远程执行器；README 有坏链见 issues"
issues:                     # 没有就 []
  - "broken_link: README exploit/exploit.py -> http://exploit/exploit.py"
  - "missing_asset: nginx-http2-rce-720p-8x.gif"
  - "license: unknown"
  - "claim-mismatch: README 自称完整 RCE，正文限定新鲜 Docker"
dropped:
  - CLAUDE.md
maturity: crash             # version-check | trigger | crash | leak | lab | rce-local | exploit-unverified
```

## 6. 删除名单

删这些（匹配到就删，记入 `dropped`）：

- `CLAUDE.md`、`AGENTS.md`、`GEMINI.md`、`.cursor/`、`.grok/`、`.agents/`、`.vscode/`
- `.git/`（嵌套仓库）
- `__pycache__/`、`.venv/`、`node_modules/`、`*.pyc`
- 社交媒体 HTML/通告稿导出（标题带 `alert`、LinkedIn、Substack export 且不是 PoC）
- 上游 CI 配置可选删：`.github/workflows/` 不帮助理解漏洞就删

保留：PoC/exp 源码、lab、detection 规则、LICENSE、上游 README、与复现直接相关的 evidence 日志。

## 7. 评分与日期规则

- 一条 CVSS 必须同时有 `version`、`score`、`source`。缺一不可。
- 优先级：厂商公告 > NVD/GHSA > 研究员博客 > PoC README。
- 根 README 索引禁止只写一个光秃数字。
- 日期拆开写：`patched`、`advisory_published`、`cve_published`、`poc_verified`。PoC 徽章上的日期默认当 `poc_verified`。
- 冲突写进 `meta.yaml.notes`，两边都留，不选一个「看起来对」的。

## 8. 收完

1. `python tools/check_layout.py`
2. 更新仓库根 `README.md` 收录表（从各 `meta.yaml` 填，不要手写评分）
3. 一次 commit 只做一件事：新增一个源，或修正一条元数据。commit 说明写 CVE ID 和源 id

## 9. 本仓库身份

根 README 第一句必须表明：这是 Coff0xc 维护的 CVE 漏洞与公开 PoC 策展库。第三方代码版权归原作者，许可证见各 `SOURCE.yaml` 与 `NOTICE`。
