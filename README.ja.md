[English](README.md) | [中文](README.zh-CN.md) | **日本語**

# cofflab

![scope](https://img.shields.io/badge/scope-public%20PoC%20only-blue) ![repro](https://img.shields.io/badge/repro-isolated%20sandbox-green)

Coff0xc が管理する公開 PoC のキュレーション集。CVE と CVE 以外の脆弱性を対象とする。各エントリは製品、スコア、日付、公開資料が実際に実証した内容、および隔離サンドボックスでの再現状況を記録する。

公開済みの資料のみを収集する。収録は読み取り専用で、実行しない。再現は[隔離環境](REPRO.md)でのみ行う。認可されたセキュリティ研究と防御のみを目的とする。

**再現：**
- ✅ 完全——隔離サンドボックスでエンドツーエンド再現
- ◐ 部分——部分再現または mock 上で検証
- — 対象なし——利用可能な脆弱な対象なし
- 未実施——未再現

---

## 目次

### Web / CMS (14)

| ID | 製品 | スコア | 影響バージョン | 修正バージョン | 評価 | CVE ステータス | 再現 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [CVE-2026-123488](CVE-2026-123488) | Craft CMS 要素検索 | 3.1 9.8 (GHSA)；4.0 9.3 (GitHub) | 4.0.0–4.18.8 and 5.0.0–5.11.1 (MySQL/MariaDB, emulated PDO prepares) | 4.18.9 / 5.11.2 | 未認証 SQLi による DB 書き込み / 権限昇格 | 確認済み | ◐ 部分 |
| [CVE-2026-129448](CVE-2026-129448) | Apache Roller XML-RPC | 3.1 9.8 (public claim, unverified) | Roller 4.0.0–6.1.4 (CVE-2026-82384 lists 6.1.5 only; same bug) | 6.1.6 | フレームワークは gadget の自前用意が必要；ローカル mock のみ | 未検証 | ◐ 部分 |
| [CVE-2026-90817](CVE-2026-90817) | Vanderbilt REDCap | 3.1 9.8 (public claim, unverified) | REDCap 13.3.0+ before 16.0.49 LTS / 17.3.10 LTS / 17.4.4 | 16.0.49 LTS / 17.3.10 LTS / 17.4.4 | 発見者のスクリプト / プレースホルダーのフレームワーク / 一括検出 | 未検証 | ◐ 部分 |
| [CVE-2026-123751](CVE-2026-123751) | WP Duplicate | 3.1 9.8 (CISA-ADP) | WP Duplicate through 1.1.11 | unknown | 未実行の exploit スクリプト；実際の WordPress での RCE は未実証 | 確認済み | ◐ 部分 |
| [CVE-2026-126473](CVE-2026-126473) | OpenEMR | 4.0 9.3 (VulnCheck)；3.1 9.1 (VulnCheck) | OpenEMR < 8.4.0 (8.3.0 tested) | 8.4.0 | ラボ Docker で公式 8.3.0 イメージに対し未認証で FHIR Patient を作成；8.4.0 はコロン形式の登録を拒否 | 確認済み | — 対象なし |
| [CVE-2026-111559](CVE-2026-111559) | Batflat CMS | 4.0 9.3 (CERT.pl) | Batflat CMS 1.2.0–1.3.7 | none (project unmaintained) | /contact フォームの SSTI による未認証 RCE；curl PoC のみ、修正なし（プロジェクトは保守終了） | 確認済み | 未実施 |
| [CVE-2026-126173](CVE-2026-126173) | AutomatorWP Pro Webhooks | 3.1 9.8 (Wordfence) | AutomatorWP Pro Webhooks <= 1.4.4 | 1.4.5 | 未認証の任意パスワードリセット/管理者奪取（ラボ）；1.4.5 で修正 | 確認済み | 未実施 |
| [CVE-2026-48356](CVE-2026-48356) | Adobe Commerce / Magento | 3.1 9.3 (Adobe) | Adobe Commerce / Magento Open Source 2.4.4-2.4.9 | 2.4.9-p2 | 低権限 REST トークンでファイルアップロードから webshell 経由 RCE（ラボ）；Sansec SA-2026-0027 | 確認済み | 未実施 |
| [CVE-2026-119977](CVE-2026-119977) | WordPress コア | 3.1 8.1 (Wordfence) | WordPress Core 4.7.0-7.1.3 | 7.1.4 | アップグレードウィンドウの TOCTOU で攻撃者の wp-config.php を配置；設定奪取から RCE（ラボ）；KEV 収載 | 確認済み | 未実施 |
| [CVE-2026-110447](CVE-2026-110447) | Collabora Online 内蔵 CODE Server | 3.1 9.8 (NVD)；4.0 9.2 (MITRE) | Collabora Online Built-in CODE Server (richdocumentscode) before 26.4.303 | 26.4.303 | proxy.php 経由の未認証コマンドインジェクション；1-day PoC；KEV 収載、実地での悪用を確認 | 確認済み | 未実施 |
| [CVE-2026-48907](CVE-2026-48907) | Joomla! JCE | 3.1 9.8 (NVD)；4.0 10.0 (Joomla) | Joomla! JCE extension < 2.9.99.5 | 2.9.99.5 | 未認証で JCE プロファイルを作成し PHP をアップロードして RCE；KEV 収載 | 確認済み | 未実施 |
| [CVE-2026-125423](CVE-2026-125423) | Gitea 自動初期化 | 3.1 8.8 (NVD)；3.1 8.5 (GHSA) | Gitea before 28.4.0 (auto_init=true, Default README template) | 28.4.0 | ラボ RCE：auto-init レース＋シンボリックリンクで hook 上書き；リポジトリ作成権限が必要 | 確認済み | 未実施 |
| [CVE-2026-63219](CVE-2026-63219) | GeoNetwork | 3.1 8.6 (GHSA) | GeoNetwork before 4.4.12 / 4.2.17 | 4.4.12 / 4.2.17 | 未認証 XSLT フォーマッタアップロード；スクリプトはリバースシェルを主張、未実行 | 確認済み | 未実施 |
| [CVE-2026-58400](CVE-2026-58400) | GeoNetwork | 3.1 9.1 (GHSA) | GeoNetwork before 4.4.12 / 4.2.17 | 4.4.12 / 4.2.17 | Saxon が XSLT から Java 実行を許可；63219 と同一チェーン、未実行 | 確認済み | 未実施 |

### AI / LLM (4)

| ID | 製品 | スコア | 影響バージョン | 修正バージョン | 評価 | CVE ステータス | 再現 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [CVE-2026-40217](CVE-2026-40217) | BerriAI LiteLLM | 3.1 8.8 PR:L (public README) | LiteLLM before v1.83.11 (image digest pinning required; some rebuilt tags are not vulnerable) | v1.83.11+ (RestrictedPython) | 認証後のラボ RCE；API キーが必要 | 確認済み | ◐ 部分 |
| [CVE-2026-130796](CVE-2026-130796) | Flowise | 4.0 8.8 (VulnCheck)；3.1 8.2 (VulnCheck) | 3.1.3-3.1.4 |  | 未認証での平文 MCP トークン漏洩；付属スクリプトはオフラインの論理シミュレーション | 確認済み | ✅ 完全 |
| [CVE-2026-102895](CVE-2026-102895) | GPUStack | 3.1 9.8 (GHSA) | < 2.2.0 | 2.2.0 | ラボで検証された未認証の管理者乗っ取り；実利用はベンダー報告であり、この PoC による実証ではない | 確認済み | ◐ 部分 |
| [CVE-2026-59726](CVE-2026-59726) | Ruflo MCP Bridge | 3.1 10.0 (GHSA) | Ruflo < 3.16.3 (default docker-compose MCP bridge) | 3.16.3 | MCP bridge の terminal_execute による未認証 RCE；Exploit-DB で検証済み autopwn | 確認済み | 未実施 |

### ネットワークとセキュリティ (21)

| ID | 製品 | スコア | 影響バージョン | 修正バージョン | 評価 | CVE ステータス | 再現 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [CVE-2026-123007](CVE-2026-123007) | F5 NGINX HTTP/2 | 4.0 9.2 (F5)；3.1 8.1 (F5) | NGINX Open Source 1.9.5–1.30.6 and 1.31.0–1.31.8 with HTTP/2 enabled | Open Source 1.30.7 / 1.31.9; NGINX Plus 37.3.0.1 / 37.0.8.1 | トリガー + 新規起動した Docker に対する RCE デモのみ | 確認済み | — 対象なし |
| [CVE-2026-129287](CVE-2026-129287) | N-able N-central | 4.0 8.3 (N-able) | before 2026.4.1 Hotfix 3 | 2026.4.1 Hotfix 3 (build 2026.4.1.39) | 認証後の帯域外 XXE によるファイル読み取り；クローズドソース機器のためローカル再現不可 | 確認済み | ◐ 部分 |
| [CVE-2026-119958](CVE-2026-119958) | Windows LDAP | 3.1 9.8 (Microsoft) | Windows 10 1607–Windows 11 26H2、Windows Server 2016–2025 | 2026 年 11 月安全更新 | OOB 書き込み + クラッシュのラボ再現；実際の Windows LDAP での RCE は未実証 | 確認済み | ✅ 完全 |
| [CVE-2026-123039](CVE-2026-123039) | Check Point Gaia OS | 3.1 7.8 (Check Point) | Gaia OS R81–R82.20（Quantum 网关、Force 防火墙、安全管理/日志服务器、多域、Maestro） | Jumbo Hotfix：R82.20 Take 14、R82.10 Take 52、R82 Take 132、R81.20 Take 174 | ワールドライタブルなソケット経由の root への権限昇格（ラボ）；実際の Gaia では未検証 | 確認済み | ◐ 部分 |
| [CVE-2026-123158](CVE-2026-123158) | OpenSSH sshd | 3.1 8.1 (MITRE) | OpenSSH < 10.6p2（Linux + musl libc 且无 PAM，如 Alpine Linux） | OpenSSH 10.6p2 | パスワード認証バイパスによるログインのラボ再現；実環境での証拠なし | 確認済み | — 対象なし |
| [CVE-2026-123218](CVE-2026-123218) | IBM Aspera Faspex 5 | 3.1 9.8 (IBM) | Faspex 5.0.0–5.0.19 | 5.0.19 PL1（Fix Pack 1） | バージョン確認のみ；バイパスは未実証 | 確認済み | ✅ 完全 |
| [CVE-2026-111560](CVE-2026-111560) | Barracuda ESG / ADC / WAF / WSG | 4.0 8.6 (Mandiant)；3.1 7.2 (NVD) | ESG ≤ 9.4.0.27；ADC ≤ 6.4.0；WAF ≤ 11.0.1；WSG ≤ 16.1.100.100；BMA ≤ 5.5.4.0；WCC ≤ 2.2.1 | ESG 9.4.0.030；其余产品按厂商通告补丁升级 | ラボでの root コマンド実行（管理者権限が必要）；未認証 root は CVE-2026-116606 との連携でのみ | 確認済み | ◐ 部分 |
| [CVE-2026-116606](CVE-2026-116606) | Barracuda ESG | 4.0 9.3 (Mandiant)；3.1 9.8 (NVD) | ESG < 9.4.0.030 | 9.4.0.030 | 未認証の設定復元トリガー；root は CVE-2026-111560 との連携でのみ | 確認済み | ◐ 部分 |
| [CVE-2026-19868](CVE-2026-19868) | SonicWall SonicOS | 3.1 7.5 (CISA-ADP)；3.1 7.1 (SonicWall) | Gen7 7.3.3-7015 及更早；Gen8 8.2.2-8015 及更早 | Gen7 7.3.4-7013 及更高；Gen8 8.2.3-8015 及更高 | バージョン確認のみ | 確認済み | ✅ 完全 |
| [CVE-2026-129271](CVE-2026-129271) | N-able N-central Patch Management | 4.0 8.5 (N-able) | Patch Management Component < 2.14.4.5829 | 2.14.4.5829（随 N-central 2026.4.1 Hotfix 3，build 2026.4.1.39，2026-11-16） | 認証後のローカル権限昇格（ProductAdmin の認証情報 + コールバックが必要） | 確認済み | — 対象なし |
| [CVE-2026-129280](CVE-2026-129280) | N-able N-central | 4.0 9.3 (N-able) | N-central < 2026.4.1 HF3 | 2026.4.1 HF3（build 2026.4.1.39，2026-11-16） | 未認証の設定書き込み（単一操作のデモ、可逆） | 確認済み | ◐ 部分 |
| [CVE-2026-114713](CVE-2026-114713) | UnrealIRCd | 3.1 8.6 (GHSA) | 6.0.0–6.2.7 (5.x EOL also affected) | 6.2.7.1 / hotfix bundle-20261107 | サーバー間コマンドインジェクションのラボ PoC；OS レベルの RCE ではない | 確認済み | ✅ 完全 |
| [CVE-2026-116779](CVE-2026-116779) | FreeSWITCH | 3.1 9.8 (GHSA) | <= 1.11.2 | 1.11.3 (adds enable-chat-api-proto, off by default) | ラボで検証された SIP MESSAGE によるコマンド実行；実運用での証拠なし | 確認済み | ◐ 部分 |
| [CVE-2026-119618](CVE-2026-119618) | Apache httpd mod_http2 | 3.1 8.1 (NVD)；3.1 9.8 (Red Hat) | httpd 2.4.55–2.4.70, mod_h2 2.0.8–2.0.42 | 2.4.71, mod_h2 2.0.43 | ASan/TSan 下でのヒープ破壊 + クラッシュ；RCE は未実証 | 確認済み | — 対象なし |
| [CVE-2026-126170](CVE-2026-126170) | Fortinet FortiManager / FortiAnalyzer | 3.1 9.8 (Fortinet) | FortiAnalyzer 8.0.0-8.0.2, 7.6.0-7.6.7; FortiAnalyzer Cloud 8.0.1-8.0.2, 7.6.0-7.6.7; FortiAnalyzer-BigData 7.6.0-7.6.2; FortiManager 8.0.0-8.0.2, 7.6.0-7.6.7; FortiManager Cloud 8.0.1-8.0.2, 7.6.0-7.6.7; FortiSASE-Sovereign 25, 25.3, 25.4, 26.2 | 8.0.3, 7.6.8, FortiAnalyzer-BigData 7.6.3 | ラボで JRPC JSON インジェクションによる未認証 RCE；7.6.7 と 7.6.8 の差分 | 確認済み | ✅ 完全 |
| [CVE-2026-124079](CVE-2026-124079) | rConfig Core / Pro | 4.0 9.3 (VulnCheck)；3.1 9.8 (VulnCheck) | rConfig Core >= 8.0.0, < 8.2.19; rConfig Pro < 8.4.1 | rConfig Core 8.2.19 (2026-10-27); rConfig Pro 8.4.1 | ラボで Redis ベースの Horizon キュー汚染による未認証 RCE | 確認済み | ◐ 部分 |
| [CVE-2026-121653](CVE-2026-121653) | Ivanti Endpoint Manager Core | 3.1 9.8 (Ivanti) | Ivanti EPM 2024 SU7 and prior | EPM 2024 SU8 | ラボで未認証 SQLi → Core DB アカウント経由の OS コマンド実行 | 確認済み | ◐ 部分 |
| [CVE-2026-111585](CVE-2026-111585) | TeamViewer クライアント | 3.1 8.8 (TeamViewer) | TeamViewer clients prior to 15.83 (15.82.6 tested) | 15.83 (bulletin TV-2026-1011) | 実際の 15.82.6 バイナリでの viewer ヒープオーバーフロー + クラッシュ；RCE は主張、クラッシュは実証済み | 確認済み | ◐ 部分 |
| [CVE-2026-83548](CVE-2026-83548) | SonicWall SMA1000 | 3.1 10.0 (NVD) | SMA1000 6210 / 7210 / 8200v: 12.4.3-03453 and older, 12.5.0-02835 and older | 12.4.3-03526 and higher, 12.5.0-02952 and higher (platform-hotfix) | 未認証 SSRF→CouchDB RCE→root の一式ツール；ベンダーも実利用を確認、CISA KEV | 確認済み | 未実施 |
| [CVE-2026-83549](CVE-2026-83549) | SonicWall SMA1000 | 3.1 7.8 (NVD) | SMA1000 6210 / 7210 / 8200v: 12.4.3-03453 and older, 12.5.0-02835 and older | 12.4.3-03526 and higher, 12.5.0-02952 and higher (platform-hotfix) | 認証後 AMC コマンドインジェクション→root；同一ツール、CISA KEV | 確認済み | 未実施 |
| [CVE-2026-123633](CVE-2026-123633) | F5 NGINX HTTP/2 | 4.0 9.2 (F5)；3.1 8.1 (F5) | NGINX Open Source 1.19.7-1.30.6 and 1.31.0-1.31.8 with HTTP/2 proxying | 1.30.7 / 1.31.9 | UAF トリガー＋ret2libc RCE を主張するスクリプト、未検証 | 確認済み | 未実施 |

### ランタイム / フレームワーク / ブラウザ (15)

| ID | 製品 | スコア | 影響バージョン | 修正バージョン | 評価 | CVE ステータス | 再現 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [CVE-2026-114938](CVE-2026-114938) | OpenJDK Base64 (Java4Shell) | 4.0 9.2 (Calif)；3.1 8.1 (Oracle)；3.1 9.8 (Red Hat) | OpenJDK 17.0.6 and later on x86-64 with AVX-512 VBMI (17/21/25/27 lines; Oracle also lists Java 8 Performance Pack 8u511b33-perf) | vendor November 2026 CPU / OpenJDK 17.0.21.1, 21.0.13.1 and equivalent distributor builds | トリガー / クラッシュ / リーク / 実験；公開された汎用 RCE はない | 確認済み | ◐ 部分 |
| [CVE-2026-90436](CVE-2026-90436) | Apache Axis 1.x | 3.1 9.8 (CISA-ADP) | Apache Axis 1.x through 1.4 | 无修复版本（EOL；修复仅存于上游 commit 41f3b4e8） | 未認証クラス生成のラボ再現；デフォルト classpath での RCE は未実証 | 確認済み | ◐ 部分 |
| [CVE-2024-27834](CVE-2024-27834) | WebKit (Apple) | 3.1 5.5 (NVD) | Safari < 17.5；iOS/iPadOS < 16.7.8 及 17.x < 17.5；macOS < 14.5；tvOS < 17.5；watchOS < 10.5；WebKitGTK / WPE WebKit < 2.44.2 | Safari 17.5；iOS 16.7.8 / iOS 17.5；iPadOS 16.7.8 / iPadOS 17.5；macOS Sonoma 14.5；tvOS 17.5；watchOS 10.5 | 分析のみ；実行可能な PoC なし | 確認済み | — 対象なし |
| [CVE-2026-126187](CVE-2026-126187) | React Server Components / Next.js | 4.0 9.5 (GHSA) | react-server-dom-* 19.0.0–19.3.0; Next.js 16.0.0–16.4.0 (App Router + Cache Components) | react-server-dom-* 19.0.9 / 19.1.10 / 19.2.9 / 19.3.1; Next.js 16.4.1 | ラボ Docker アプリでの RCE；トリガーには稀な条件が必要 | 確認済み | ◐ 部分 |
| [CVE-2026-125350](CVE-2026-125350) | Google Chrome | 3.1 8.8 (NVD) | Chrome < 157.0.8103.50 | 157.0.8103.50 / .51 (Windows, macOS), 157.0.8103.50 (Linux, Android), Extended Stable 156.0.8078.96 | 回帰テストファイルによるレンダラークラッシュ；RCE ペイロードなし | 確認済み | ✅ 完全 |
| [CVE-2026-111497](CVE-2026-111497) | Node.js Brotli | 4.0 9.2 (Google)；3.1 9.8 (NVD) | Node.js < 22.23.4, < 24.22.1, < 26.12.1; Bun < 1.4.4; Brotli 1.0.3-1.2.0 | Node.js 22.23.4 / 24.22.1 / 26.12.1; Bun 1.4.4; Brotli 1.2.1 | 細工した Brotli ストリームによるリモート DoS を検証済み；RCE は分析のみ | 確認済み | ◐ 部分 |
| [CVE-2026-129349](CVE-2026-129349) | Apache Shiro DefaultLdapRealm | 4.0 9.1 (Apache) | Apache Shiro through 3.0.0 with DefaultLdapRealm/JndiLdapRealm and authenticationCachingEnabled=true (not the default) | 3.0.1 | 一度有効なログイン後の認証バイパス；キャッシュ有効時（非デフォルト）は任意のパスワードで認証 | 確認済み | ◐ 部分 |
| [CVE-2026-86829](CVE-2026-86829) | Apache Airflow コア | 3.1 8.8 (Apache) | apache-airflow-core < 3.4.0 | 3.4.0 (apache/airflow PR #72718) | DAG 作成者による XCom デシリアライズ経由のスケジューラ RCE；3.3.2 でラボ検証済み、3.4.0 ではクリーン | 確認済み | ◐ 部分 |
| [php-session-upload-progress-2026-rce](php-session-upload-progress-2026-rce) | PHP セッションアップロード進捗 | unknown | PHP with session.serialize_handler=php_binary or php_serialize in server config, application switching to php at runtime via ini_set() before session_start(), and session.upload_progress.enabled=1 (PHP default). Validated on php:8.4.27-apache. | No patch as of 2026-10-24; official mitigation is session.upload_progress.enabled=0 | ラボでセッションハンドラ不一致による未認証 RCE（php:8.4.27-apache）；未修正、緩和策はアップロード進捗の無効化 | 確認済み | ◐ 部分 |
| [CVE-2026-75604](CVE-2026-75604) | Windows 上の Next.js | 3.1 9.0 (GHSA) | Next.js 13.4.0–15.5.23 and 16.0.0–16.3.2 on Windows, Pages Router + App Router without Cache Components | 15.5.24 / 16.3.3 | Server Actions 暗号化鍵の漏洩による未認証 RCE；Windows ホストと Pages/App Router が必要、ラボで next@16.2.11 を検証 | 確認済み | 未実施 |
| [CVE-2026-115893](CVE-2026-115893) | Wasmtime | 3.1 9.9 (GHSA) | Wasmtime < 36.0.19, 37.0.0-42.x, 43.0.0-48.0.6, 49.0.0-49.0.3 (aarch64 Cranelift) | 36.0.19, 48.0.7, 49.0.4 | aarch64 JIT サンドボックス脱出からホストでのコード実行（ラボ）；49.0.3 で 5/5 成功、49.0.4 は拒否 | 確認済み | 未実施 |
| [CVE-2026-109618](CVE-2026-109618) | PHP | 3.1 9.8 (NVD)；4.0 9.2 (PHP) | PHP 5.4.0-8.5.11 | 8.2.35, 8.3.36, 8.4.27, 8.5.12 | 事前認証 RCE チェーン A/B/C を公開（D/E は有料）；PHP 5.4–8.5.11 でラボ検証；KEV 収載 | 確認済み | 未実施 |
| [CVE-2026-109619](CVE-2026-109619) | PHP | 3.1 8.1 (NVD)；4.0 9.2 (PHP) | PHP 5.4.0-8.5.11 | 8.2.35, 8.3.36, 8.4.27, 8.5.12 | FPM ワーカーの跨リクエスト残留状態による UAF/情報漏洩 RCE（ラボ）；KEV 収載 | 確認済み | 未実施 |
| [CVE-2026-126910](CVE-2026-126910) | Chrome V8 Maglev | 3.1 8.8 (NVD) | Chrome before 157.0.8103.78 | 157.0.8103.78 | ラボで型混乱 stale load を実証；RCE 未達、開発者フラグ要 | 確認済み | 未実施 |
| [CVE-2026-128134](CVE-2026-128134) | NLTK dot2img | 3.1 7.8 (GHSA) | NLTK before 3.10.4 | 3.10.4 | ローカル PATH ハイジャック実証；README の 7.3/3.9.2 は GHSA 7.8/3.10.4 と矛盾 | 確認済み | 未実施 |

### データベース (3)

| ID | 製品 | スコア | 影響バージョン | 修正バージョン | 評価 | CVE ステータス | 再現 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [CVE-2026-118383](CVE-2026-118383) | MongoDB Server レプリケーション | unknown | 8.0.x before 8.0.37 (8.0.34 tested); 8.2.12 still reproduced at collection time | 8.0.37 (SERVER-138175, SERVER-138119) | ラボでの UAF クラッシュ；コード実行は未実証 | 確認済み | — 対象なし |
| [CVE-2026-116366](CVE-2026-116366) | ClickHouse Server | 4.0 9.5 (ClickHouse) | ClickHouse 26.3 < 26.3.62.3-lts, 26.8 < 26.8.36.3-lts, 26.9 < 26.9.27.3-stable, 26.10 < 26.10.3.7-stable | 26.3.62.3-lts / 26.8.36.3-lts / 26.9.27.3-stable / 26.10.3.7-stable (2026-10-30) | 未認証 RCE を主張；ラボでは差分検出 + 武器化 DoS のみ検証 | 確認済み | ◐ 部分 |
| [CVE-2026-13078](CVE-2026-13078) | MongoDB Server | 3.1 7.7 (MongoDB)；4.0 6.3 (MongoDB) | MongoDB Server 7.0 before 7.0.39, 8.0 before 8.0.28, 8.2 before 8.2.12, 8.3 before 8.3.7 | 7.0.39, 8.0.28, 8.2.12, 8.3.7 | 低権限認証ユーザーが MozJS モジュールローダー経由でローカルファイルを漏洩；RCE ではない | 確認済み | 未実施 |

### OS / システム / DevOps (13)

| ID | 製品 | スコア | 影響バージョン | 修正バージョン | 評価 | CVE ステータス | 再現 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [CVE-2024-10441](CVE-2024-10441) | Synology DSM/BSM synoplugind | 3.1 9.8 (public README, vendor advisory not verified) | DSM 6.2.4–7.2.2 and BSM/DSMUC branches before the 2024-11 smallfix | DSM 7.2.2-72806-1 / 7.2.1-69057-6 / 7.2-64570-4 / 7.1.1-42962-7 / 6.2.4-25556-8; BeeStation OS 1.1-65374; DSMUC 3.1.4-23079 | パッチ差分分析 + ローカル検証；そのまま使えるリモート exploit はない | 未検証 | ◐ 部分 |
| [CVE-2026-124194](CVE-2026-124194) | Microsoft Outlook | 3.1 6.5 (Microsoft) | Microsoft 365 Apps 版经典 Outlook、Office LTSC 2021/2024（2026-11-10 前构建） | 2026 年 11 月 10 日 Patch Tuesday Office 更新 | .msg ファイルのトリガーのみ；実際の Outlook での NTLM 漏洩は未実証 | 確認済み | ◐ 部分 |
| [CVE-2026-115731](CVE-2026-115731) | Puppet / OpenVox Server | 4.0 9.4 (Perforce)；3.1 9.9 (NVD) | Puppet Enterprise 2023.8.0–<2023.8.13、2025.0.0–<2025.12.1、2026.0.0–<2026.0.1；OpenVox Server ≤ 9.1.0 / ≤ 8.17.0；OpenVox Agent ≤ 9.2.0 / ≤ 8.31.1 | Puppet Enterprise 2023.8.13 / 2025.12.1 / 2026.0.1；OpenVox Server 9.2.0 / 8.18.0；OpenVox Agent 9.3.0 / 8.32.0；Puppet Core 9.1.3 / 8.22.2 | アドバイザリで確認されたサーバーコマンド実行（有効な CA 署名クライアント証明書が必要） | 確認済み | — 対象なし |
| [CVE-2026-98432](CVE-2026-98432) | Linux カーネル TCP | 3.1 9.8 (Linux kernel) | Linux kernel since 4.4 (IPv4 TCP) | 6.6.159 and later stable releases (two kfree_rcu() calls) | inet_csk_route_req での KASAN 検証済み UAF クラッシュ；コード実行は未実証 | 確認済み | — 対象なし |
| [CVE-2026-76954](CVE-2026-76954) | Synology DSM 認証 API | 3.1 9.8 (Synology) | DSM <= 7.2.1-69057-12, 7.2.2-72806, 7.3.2-86009, 7.4.1-90080 | 7.2.1-69057-13, 7.2.2-72806-10, 7.3.2-86009-5, 7.4.1-90080-1 (Synology-SA-26:19) | 認証前のスタック SQLi（syno-pam-key.db）；ファイル読み書きはベンダー公告の主張で PoC 未実証 | 確認済み | ◐ 部分 |
| [CVE-2026-124552](CVE-2026-124552) | Webmin Shorewall モジュール | 4.0 4.8 (VulnCheck)；3.1 4.8 (VulnCheck) | Webmin through 2.670 | Post-2.670 (upstream commit 01b988dbf, webmin/webmin#2908) | ラボで格納型 XSS → root コマンド実行（Shorewall モジュール権限 + 管理者の閲覧が必要）；未修正のトラバーサル 0day も実証 | 確認済み | ◐ 部分 |
| [CVE-2026-104623](CVE-2026-104623) | SUSE Rancher Manager | 3.1 6.3 (SUSE) | Rancher Manager 2.11.0-2.11.18, 2.12.0-2.12.14, 2.13.0-2.13.10, 2.14.0-2.14.6, 2.15.0-2.15.2 (and older) | 2.11.19 / 2.12.15 / 2.13.11 / 2.14.7 / 2.15.3 | 認証ユーザーが管理クラスタでシェル Pod を取得；非特権 Pod、API アクセスは制限付き | 確認済み | ◐ 部分 |
| [CVE-2026-105437](CVE-2026-105437) | Git 3方向マージ | 3.1 7.5 (GitLab) | Git <= 2.56.0 (and the 2.50-2.55 series) | Git 2.56.1, and 2.50.2 / 2.51.3 / 2.52.1 / 2.53.1 / 2.54.1 / 2.55.1 | 攻撃者制御コンテンツのマージでヒープオーバーフロー；2.56.0 で SIGSEGV、2.56.1 ではクリーン | 確認済み | ✅ 完全 |
| [CVE-2026-53362](CVE-2026-53362) | Linux カーネル IPv6 フラグメンテーション | 3.1 7.8 (Linux kernel) | Linux kernel 6.12.x (CentOS Stream 10 / RHEL 10, e.g. 6.12.0-242.el10); __ip6_append_data() paged-allocation path | upstream commit 38becddc (fix in stable trees) | ラボで CentOS/RHEL 10（カーネル 6.12.x）からコンテナ脱出して root 取得；IPv4 の同系 CVE-2026-53366 は対象外 | 確認済み | 未実施 |
| [CVE-2026-97229](CVE-2026-97229) | GitLab CE/EE | 3.1 10.0 (GitLab) | GitLab CE/EE 19.2 before 19.2.8, 19.3 before 19.3.5, 19.4 before 19.4.2 | 19.2.8, 19.3.5, 19.4.2 | 未認証 CI lint 正規表現の OOB 書き込みで system() 実行（git 権限、19.4.1 CE、ラボ）；悪意ある CI 設定の植え付けには書き込み権限が必要 | 確認済み | 未実施 |
| [CVE-2026-110264](CVE-2026-110264) | GitLab CE/EE | 3.1 10.0 (GitLab) | GitLab CE/EE 7.0 before 18.11.13, 19.0 before 19.0.10, 19.1 before 19.1.9, 19.2 before 19.2.9, 19.3 before 19.3.6, 19.4 before 19.4.3 | 18.11.13, 19.0.10, 19.1.9, 19.2.9, 19.3.6, 19.4.3, 19.5.1 | .org レンダリングで Onigmo 整数オーバーフローを誘発；oracle/差分のみ、完全なシェルは未実証 | 確認済み | 未実施 |
| [CVE-2026-112611](CVE-2026-112611) | Apple CoreGraphics PDF | 3.1 6.1 (NVD) | iOS before 27.2 / 26.7.2, iPadOS before 27.2 / 26.7.2, macOS before 15.8.2 / 26.7.2 | iOS 27.2 / 26.7.2, macOS Sequoia 15.8.2 / Tahoe 26.7.2 | デバイスで PDF 指定アドレス書き込みプリミティブを検証；コード実行は未達 | 確認済み | 未実施 |
| [CVE-2026-99288](CVE-2026-99288) | Linux カーネル TCP | 3.1 5.9 (NVD) | Linux kernel with vulnerable TCP ehash lookup (before upstream commit 4e2b3ef19e0e) | Upstream commit 4e2b3ef19e0e (inet: reject unhashed sockets during established lookups) | アドバイザリの仕組みから再実装したレーストリガー；カーネルパニックには精密なプリエンプション要 | 確認済み | 未実施 |


完全な評価と引用については各 CVE ディレクトリを参照。
