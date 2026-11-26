# GHSA-743w-g9pf-8p94 — TastyIgniter 郵件範本 SSTI 遠端程式碼執行

| 項 | 值 |
| --- | --- |
| 產品 | TastyIgniter |
| CWE | 未列（通告未列 CWE） |
| 影響版本 | tastyigniter/tastyigniter <= v4.2.4 |
| 修復版本 | v4.3.1 |
| CVSS | 3.1 9.1 (GHSA) |
| 公開成色 | GHSA 通告含可直接照做的 PoC 步驟；CVE 編號未獲 NVD 證實 |

公開材料實際證明了什麼：GHSA 通告載明具 Admin.MailTemplates 權限的管理員可在郵件範本寫入 `@php echo shell_exec('echo "RCE Executed";id'); @endphp`，儲存後經 `X-IGNITER-REQUEST-HANDLER: onTestTemplate` 執行，於日誌查看執行結果，通告附執行截圖。本倉未運行 PoC。

## 來源

| 目錄 | 上游 | 許可證 | 成色 |
| --- | --- | --- | --- |
| [sources/ghsa-advisory](sources/ghsa-advisory) | [api.github.com — GHSA-743w-g9pf-8p94](https://api.github.com/repos/tastyigniter/TastyIgniter/security-advisories/GHSA-743w-g9pf-8p94) | unknown | trigger |

字段以 [meta.yaml](meta.yaml) 為準。
