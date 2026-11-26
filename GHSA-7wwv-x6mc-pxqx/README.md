# GHSA-7wwv-x6mc-pxqx — TastyIgniter 媒體管理器無限制檔案上傳遠端程式碼執行

| 項 | 值 |
| --- | --- |
| 產品 | TastyIgniter |
| CWE | 未列（通告未列 CWE） |
| 影響版本 | tastyigniter/tastyigniter <= v4.2.4 |
| 修復版本 | v4.3.1 |
| CVSS | 3.1 9.1 (GHSA) |
| 公開成色 | GHSA 通告含可直接照做的 PoC 步驟；CVE 編號未獲 NVD 證實 |

公開材料實際證明了什麼：GHSA 通告載明媒體管理器接受 .htaccess 上傳，管理員可藉此將 .jpg 重新對映為 PHP 處理器，再上傳內容為 PHP shell 的 test.jpg 即執行任意 PHP 命令；通告附完整請求步驟與執行截圖。本倉未運行 PoC。

## 來源

| 目錄 | 上游 | 許可證 | 成色 |
| --- | --- | --- | --- |
| [sources/ghsa-advisory](sources/ghsa-advisory) | [api.github.com — GHSA-7wwv-x6mc-pxqx](https://api.github.com/repos/tastyigniter/tastyigniter/security-advisories/GHSA-7wwv-x6mc-pxqx) | unknown | trigger |

字段以 [meta.yaml](meta.yaml) 為準。
