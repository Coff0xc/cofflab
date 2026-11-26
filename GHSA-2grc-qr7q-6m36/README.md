# GHSA-2grc-qr7q-6m36 — Gogs git diff 參數注入任意檔案寫入

| 項 | 值 |
| --- | --- |
| 產品 | Gogs |
| CWE | CWE-88 |
| 影響版本 | Gogs <= 0.14.3 |
| 修復版本 | 0.14.4 |
| CVSS | 3.1 9.6 (GHSA) |
| 公開成色 | GHSA 通告含可直接照做的 PoC 步驟；CVE 編號未獲 NVD 證實 |

公開材料實際證明了什麼：GHSA 通告載明 `DiffBinary()` 把使用者控制的分支名直接拼進 `git diff --full-index --binary <base> <head>`，未加 `--end-of-options`；攻擊者推送名為 `--output=/path/to/target` 的分支並建立 PR，git 即把 diff 內容寫入攻擊者指定路徑。需具寫入權限的已認證帳號。本倉未運行 PoC。

## 來源

| 目錄 | 上游 | 許可證 | 成色 |
| --- | --- | --- | --- |
| [sources/ghsa-advisory](sources/ghsa-advisory) | [api.github.com — GHSA-2grc-qr7q-6m36](https://api.github.com/repos/gogs/gogs/security-advisories/GHSA-2grc-qr7q-6m36) | unknown | trigger |

字段以 [meta.yaml](meta.yaml) 為準。
