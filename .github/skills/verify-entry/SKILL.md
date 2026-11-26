# verify-entry — 驗證一條入庫

> 用途：驗證一條 cofflab 條目（新入庫或已入庫複核），從編號核對到目錄同步，
> 每步都有 pass/fail，交出去之前先拿出證據。
> 權威：`~/workspace/cve-poc-tools/docs/ingest-spec.md` 是唯一權威；
> 本 skill 與 ingest-spec 衝突時，以 ingest-spec 為準。
> 本 skill 不復制 ingest-spec 的規則全文，只給流程與證據清單。

## Launch（前置條件）

- 本地 clone 在 `~/workspace/cve-poc-clone`，已 `git pull --ff-only` 同步；
  要驗證的條目 ID 已知（形如 `CVE-2026-137043`）。
- 已讀 ingest-spec 與本 skill。沒讀完不開始。

## Doctor（自檢——任一不通先修環境，不開始驗證）

- `python3 -c 'import yaml'` 能跑（PyYAML 6.x）。
- `gh api repos/Coff0xc/cofflab/commits/main -q '.sha'` 能讀回遠端 HEAD。
- `python3 ~/workspace/cve-poc-tools/tools/gen_catalog.py --dry-run --repo ~/workspace/cve-poc-clone`
  能跑（只讀，輸出條目數與兩份 README 行數）。

## Drive（驗證流程——按順序，每步都有 pass/fail）

1. **編號核對**：NVD / GHSA / 廠商三處對年份與編號，不以 GitHub 倉庫名為準。
   任一處查不到編號，不建目錄、不入庫，記下來寫清原因。
2. **PoC 真實性（只讀）**：clone 下來看過、不是空骨架/佔位/純鏡像、
   不是已入庫的重複。**絕不執行** PoC、exploit、`run.sh`、容器、掃描器。
   克隆被執行風險檢查攔截時，改走通告源（廠商通告 / GHSA / NVD 記錄 /
   研究員文章），PoC 代碼不收，在 `meta.yaml notes` 裡記清“PoC 存在、已只讀核實、
   代碼未收”。
3. **評分與日期**：優先級 廠商公告 > NVD/GHSA > 研究員博客 > PoC README。
   CVSS 必須 version + score + source 齊全，缺一不寫、索引寫 unknown；
   日期拆開寫（patched / advisory_published / cve_published / poc_verified）；
   衝突寫進 `notes`，兩邊都留，不選一個“看起來對”的。
4. **依賴鏈**：源目錄裡有 `requirements*.txt` / `package.json` / `go.mod` /
   `Cargo.toml` / `Gemfile` / `composer.json` / `pyproject.toml` / `setup.py` /
   `setup.cfg` 的，跑 `python tools/check_deps.py --source sources/<作者>-<簡稱>`；
   BLOCK（不在 registry 上、或 OSV 有 MAL-* 記錄）與 UNVERIFIED 一律不入庫；
   結果原樣貼進 `SOURCE.yaml review.notes`。**沒跑 check_deps 就不許寫“無外聯”。**
5. **佈局**：跑 `python tools/check_layout.py`（檢查時臨時拷進倉庫 `tools/`、
   跑完立即 `rm -rf tools`、提交前 `git status` 確認乾淨）；退出碼非 0 不準 commit。
6. **目錄同步**：新條目先在 `gen_catalog.py` 的 `CATEGORY_OF` 里加一行再跑
   （133335 的教訓：缺這一行整庫目錄生成失敗）；跑 `gen_catalog.py` 同步
   兩份根 README（英文 + 繁體中文），絕不手改表；兩份錶行數與順序一致。

## Evidence（每條入庫要留的證據）

- NVD 記錄鏈接與快照文件的 sha256（SOURCE.yaml 裡 `content_sha256`）。
- PoC 倉庫的 40 位 commit（SOURCE.yaml 裡 `commit`；非 git 源填 `n/a`）。
- KEV 狀態（在列 / 不在列，進列日期與整改期限）。
- 驗證時讀到的原文行（NVD 描述、廠商通告句、PoC README 自稱的影響面）。
- `check_layout.py`、`check_deps.py`、`gen_catalog.py --dry-run` 的輸出行
  （退出碼 + 關鍵行，原樣貼，不改寫）。

## Cleanup（收尾）

- 刪 staging、刪 /tmp 臨時克隆；工作區 `git status` 乾淨。
- 一次 commit 只做一件事（新增一個源，或修正一條元數據）；commit 說明寫 CVE ID 和源 id。
- push 用憑證助手 + HTTP/1.1（`git -c credential.helper='!/usr/bin/gh auth git-credential'
  -c http.version=HTTP/1.1 push`）；普通 `git push` 會失敗（hatch-git 包裝不讀
  `~/.gitconfig`）；push 失敗停下來記 stderr，不重試；禁 force-push。

## 禁令（反向清單——只寫“要做什麼”不夠，必須寫明“絕對不能幹什麼”）

- 嚴禁執行任何 PoC、exploit、`run.sh`、容器、掃描器。
- 嚴禁改上游 PoC 邏輯、補利用鏈、修 exploit 讓它“更能打”。
- 嚴禁編 CVSS、日期、影響面；沒有出處就寫 `unknown`。
- 嚴禁把上游 README 放到 CVE 根目錄；嚴禁把 `CLAUDE.md`、`AGENTS.md`、
  `.cursor/`、`.grok/`、`.agents/` 收進來。
- 嚴禁把單源文件直接攤在 `CVE-*/` 根下。
- 嚴禁手改目錄表；嚴禁只拷工作區、不記 SHA；嚴禁 force-push。
- 嚴禁在沒跑 `check_deps` 的情況下寫“無外聯”“無依賴問題”。

## 維護

- 本 skill 只改流程與證據清單，不改 ingest-spec 的規則。
- ingest-spec 變了，本 skill 跟著變；變完按 Drive 對一條真實條目重跑一次證明，
  證明失敗就不用新版。
- 結論只出三種：clean（流程與證據都對）/ changed（只改本 skill 自己的目錄，
  改完重跑證明）/ blocked（缺前置條件或權威衝突，停下來等人定奪）。
  維護 skill 時絕不改產品代碼（不改任何條目數據）。
