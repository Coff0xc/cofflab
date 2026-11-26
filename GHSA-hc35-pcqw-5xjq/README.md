# GHSA-hc35-pcqw-5xjq — Gogs NTFS 繞過經 Git Hook 遠端程式碼執行

| 項 | 值 |
| --- | --- |
| 產品 | Gogs |
| CWE | CWE-22、CWE-41、CWE-94 |
| 影響版本 | Gogs <= 0.14.3 |
| 修復版本 | 未列（通告稱 PR #8408 修復不完整，未列修復版本） |
| CVSS | 3.1 9.9 (GHSA) |
| 公開成色 | GHSA 通告含可直接照做的 PoC 步驟；無 CVE 編號 |

公開材料實際證明了什麼：GHSA 通告載明 `isRepositoryGitPath` 只擋結尾點號與空格，未擋 NTFS Alternate Data Streams，路徑 `.git::$INDEX_ALLOCATION/hooks/pre-commit` 會解析為真實的 `.git/hooks/pre-commit`；已認證且具寫入權限的使用者可經 web editor 寫入 Git hook，Gogs 執行 `git commit` 時不帶 `--no-verify`，hook 即以 Gogs 服務帳號執行，於 Windows 宿主拿 RCE。本倉未運行 PoC。

## 來源

| 目錄 | 上游 | 許可證 | 成色 |
| --- | --- | --- | --- |
| [sources/ghsa-advisory](sources/ghsa-advisory) | [api.github.com — GHSA-hc35-pcqw-5xjq](https://api.github.com/repos/gogs/gogs/security-advisories/GHSA-hc35-pcqw-5xjq) | unknown | trigger |

字段以 [meta.yaml](meta.yaml) 為準。
