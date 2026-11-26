# verify-entry — 验证一条入库

> 用途：验证一条 cofflab 条目（新入库或已入库复核），从编号核对到目录同步，
> 每步都有 pass/fail，交出去之前先拿出证据。
> 权威：`~/workspace/cve-poc-tools/docs/ingest-spec.md` 是唯一权威；
> 本 skill 与 ingest-spec 冲突时，以 ingest-spec 为准。
> 本 skill 不复制 ingest-spec 的规则全文，只给流程与证据清单。

## Launch（前置条件）

- 本地 clone 在 `~/workspace/cve-poc-clone`，已 `git pull --ff-only` 同步；
  要验证的条目 ID 已知（形如 `CVE-2026-137043`）。
- 已读 ingest-spec 与本 skill。没读完不开始。

## Doctor（自检——任一不通先修环境，不开始验证）

- `python3 -c 'import yaml'` 能跑（PyYAML 6.x）。
- `gh api repos/Coff0xc/cofflab/commits/main -q '.sha'` 能读回远端 HEAD。
- `python3 ~/workspace/cve-poc-tools/tools/gen_catalog.py --dry-run --repo ~/workspace/cve-poc-clone`
  能跑（只读，输出条目数与两份 README 行数）。

## Drive（验证流程——按顺序，每步都有 pass/fail）

1. **编号核对**：NVD / GHSA / 厂商三处对年份与编号，不以 GitHub 仓库名为准。
   任一处查不到编号，不建目录、不入库，记下来写清原因。
2. **PoC 真实性（只读）**：clone 下来看过、不是空骨架/占位/纯镜像、
   不是已入库的重复。**绝不执行** PoC、exploit、`run.sh`、容器、扫描器。
   克隆被执行风险检查拦截时，改走通告源（厂商通告 / GHSA / NVD 记录 /
   研究员文章），PoC 代码不收，在 `meta.yaml notes` 里记清“PoC 存在、已只读核实、
   代码未收”。
3. **评分与日期**：优先级 厂商公告 > NVD/GHSA > 研究员博客 > PoC README。
   CVSS 必须 version + score + source 齐全，缺一不写、索引写 unknown；
   日期拆开写（patched / advisory_published / cve_published / poc_verified）；
   冲突写进 `notes`，两边都留，不选一个“看起来对”的。
4. **依赖链**：源目录里有 `requirements*.txt` / `package.json` / `go.mod` /
   `Cargo.toml` / `Gemfile` / `composer.json` / `pyproject.toml` / `setup.py` /
   `setup.cfg` 的，跑 `python tools/check_deps.py --source sources/<作者>-<简称>`；
   BLOCK（不在 registry 上、或 OSV 有 MAL-* 记录）与 UNVERIFIED 一律不入库；
   结果原样贴进 `SOURCE.yaml review.notes`。**没跑 check_deps 就不许写“无外联”。**
5. **布局**：跑 `python tools/check_layout.py`（检查时临时拷进仓库 `tools/`、
   跑完立即 `rm -rf tools`、提交前 `git status` 确认干净）；退出码非 0 不准 commit。
6. **目录同步**：新条目先在 `gen_catalog.py` 的 `CATEGORY_OF` 里加一行再跑
   （133335 的教训：缺这一行整库目录生成失败）；跑 `gen_catalog.py` 同步
   两份根 README（英文 + 繁體中文），绝不手改表；两份表行数与顺序一致。

## Evidence（每条入库要留的证据）

- NVD 记录链接与快照文件的 sha256（SOURCE.yaml 里 `content_sha256`）。
- PoC 仓库的 40 位 commit（SOURCE.yaml 里 `commit`；非 git 源填 `n/a`）。
- KEV 状态（在列 / 不在列，进列日期与整改期限）。
- 验证时读到的原文行（NVD 描述、厂商通告句、PoC README 自称的影响面）。
- `check_layout.py`、`check_deps.py`、`gen_catalog.py --dry-run` 的输出行
  （退出码 + 关键行，原样贴，不改写）。

## Cleanup（收尾）

- 删 staging、删 /tmp 临时克隆；工作区 `git status` 干净。
- 一次 commit 只做一件事（新增一个源，或修正一条元数据）；commit 说明写 CVE ID 和源 id。
- push 用凭证助手 + HTTP/1.1（`git -c credential.helper='!/usr/bin/gh auth git-credential'
  -c http.version=HTTP/1.1 push`）；普通 `git push` 会失败（hatch-git 包装不读
  `~/.gitconfig`）；push 失败停下来记 stderr，不重试；禁 force-push。

## 禁令（反向清单——只写“要做什么”不够，必须写明“绝对不能干什么”）

- 严禁执行任何 PoC、exploit、`run.sh`、容器、扫描器。
- 严禁改上游 PoC 逻辑、补利用链、修 exploit 让它“更能打”。
- 严禁编 CVSS、日期、影响面；没有出处就写 `unknown`。
- 严禁把上游 README 放到 CVE 根目录；严禁把 `CLAUDE.md`、`AGENTS.md`、
  `.cursor/`、`.grok/`、`.agents/` 收进来。
- 严禁把单源文件直接摊在 `CVE-*/` 根下。
- 严禁手改目录表；严禁只拷工作区、不记 SHA；严禁 force-push。
- 严禁在没跑 `check_deps` 的情况下写“无外联”“无依赖问题”。

## 维护

- 本 skill 只改流程与证据清单，不改 ingest-spec 的规则。
- ingest-spec 变了，本 skill 跟着变；变完按 Drive 对一条真实条目重跑一次证明，
  证明失败就不用新版。
- 结论只出三种：clean（流程与证据都对）/ changed（只改本 skill 自己的目录，
  改完重跑证明）/ blocked（缺前置条件或权威冲突，停下来等人定夺）。
  维护 skill 时绝不改产品代码（不改任何条目数据）。
