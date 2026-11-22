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

### Web / CMS (146)

| ID | 製品 | スコア | 影響バージョン | 修正バージョン | 評価 | CVE ステータス | 再現 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [CVE-2026-91618](CVE-2026-91618) | Oracle Application Development Framework (ADF) | 3.1 9.1 (Oracle) | Oracle Application Development Framework (ADF) 12.2.1.4.0 | November 2026 Critical Patch Update | Oracle ADF セキュリティフレームワークの未認証アクセス；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-40128](CVE-2026-40128) | SAP NetWeaver Application Server Java | 3.1 9.0 (SAP) | SAP NetWeaver Application Server Java (Web Container) | SAP Note 3727078 | SAP NetWeaver AS Java ログオン処理の未認証パストラバーサル；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-61532](CVE-2026-61532) | Chamilo LMS | 3.1 9.0 (GHSA) | Chamilo LMS <1.11.40 and <2.0.3 | 1.11.40 / 2.0.3 | Chamilo LMS コースバックアップ取り込みのパストラバーサルによるコード実行；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-123488](CVE-2026-123488) | Craft CMS 要素検索 | 3.1 9.8 (GHSA)；4.0 9.3 (GitHub) | 4.0.0–4.18.8 and 5.0.0–5.11.1 (MySQL/MariaDB, emulated PDO prepares) | 4.18.9 / 5.11.2 | 未認証 SQLi による DB 書き込み / 権限昇格 | 確認済み | ◐ 部分 |
| [CVE-2026-129448](CVE-2026-129448) | Apache Roller XML-RPC | 3.1 9.8 (public claim, unverified) | Roller 4.0.0–6.1.4 (CVE-2026-82384 lists 6.1.5 only; same bug) | 6.1.6 | フレームワークは gadget の自前用意が必要；ローカル mock のみ | 未検証 | ◐ 部分 |
| [CVE-2026-90817](CVE-2026-90817) | Vanderbilt REDCap | 3.1 9.8 (public claim, unverified) | REDCap 13.3.0+ before 16.0.49 LTS / 17.3.10 LTS / 17.4.4 | 16.0.49 LTS / 17.3.10 LTS / 17.4.4 | 発見者のスクリプト / プレースホルダーのフレームワーク / 一括検出 | 未検証 | ◐ 部分 |
| [CVE-2026-123751](CVE-2026-123751) | WP Duplicate | 3.1 9.8 (CISA-ADP) | WP Duplicate through 1.1.11 | unknown | 未実行の exploit スクリプト；実際の WordPress での RCE は未実証 | 確認済み | ◐ 部分 |
| [CVE-2026-126473](CVE-2026-126473) | OpenEMR | 4.0 9.3 (VulnCheck)；3.1 9.1 (VulnCheck) | OpenEMR < 8.4.0 (8.3.0 tested) | 8.4.0 | ラボ Docker で公式 8.3.0 イメージに対し未認証で FHIR Patient を作成；8.4.0 はコロン形式の登録を拒否 | 確認済み | — 対象なし |
| [CVE-2026-111559](CVE-2026-111559) | Batflat CMS | 4.0 9.3 (CERT.pl) | Batflat CMS 1.2.0–1.3.7 | none (project unmaintained) | /contact フォームの SSTI による未認証 RCE；curl PoC のみ、修正なし（プロジェクトは保守終了） | 確認済み | 未実施 |
| [CVE-2026-126173](CVE-2026-126173) | AutomatorWP Pro Webhooks | 3.1 9.8 (Wordfence) | AutomatorWP Pro Webhooks <= 1.4.4 | 1.4.5 | 未認証の任意パスワードリセット/管理者奪取（ラボ）；1.4.5 で修正 | 確認済み | 未実施 |
| [CVE-2026-48356](CVE-2026-48356) | Adobe Commerce / Magento | 3.1 9.3 (Adobe) | Adobe Commerce / Magento Open Source 2.4.4-2.4.9 | 2.4.9-p2 | 低権限 REST トークンでファイルアップロードから webshell 経由 RCE（ラボ）；Sansec SA-2026-0027 | 確認済み | 未実施 |
| [CVE-2026-119977](CVE-2026-119977) | WordPress コア | 3.1 8.1 (Wordfence) | WordPress Core 4.7.0-7.1.3 | 7.1.4 | アップグレードウィンドウの TOCTOU で攻撃者の wp-config.php を配置；設定奪取から RCE（ラボ）；KEV 収載 | 確認済み | ◐ 部分 |
| [CVE-2026-110447](CVE-2026-110447) | Collabora Online 内蔵 CODE Server | 3.1 9.8 (NVD)；4.0 9.2 (MITRE) | Collabora Online Built-in CODE Server (richdocumentscode) before 26.4.303 | 26.4.303 | proxy.php 経由の未認証コマンドインジェクション；1-day PoC；KEV 収載、実地での悪用を確認 | 確認済み | — 対象なし |
| [CVE-2026-48907](CVE-2026-48907) | Joomla! JCE | 3.1 9.8 (NVD)；4.0 10.0 (Joomla) | Joomla! JCE extension < 2.9.99.5 | 2.9.99.5 | 未認証で JCE プロファイルを作成し PHP をアップロードして RCE；KEV 収載 | 確認済み | 未実施 |
| [CVE-2026-125423](CVE-2026-125423) | Gitea 自動初期化 | 3.1 8.8 (NVD)；3.1 8.5 (GHSA) | Gitea before 28.4.0 (auto_init=true, Default README template) | 28.4.0 | ラボ RCE：auto-init レース＋シンボリックリンクで hook 上書き；リポジトリ作成権限が必要 | 確認済み | 未実施 |
| [CVE-2026-63219](CVE-2026-63219) | GeoNetwork | 3.1 8.6 (GHSA) | GeoNetwork before 4.4.12 / 4.2.17 | 4.4.12 / 4.2.17 | 未認証 XSLT フォーマッタアップロード；スクリプトはリバースシェルを主張、未実行 | 確認済み | 未実施 |
| [CVE-2026-58400](CVE-2026-58400) | GeoNetwork | 3.1 9.1 (GHSA) | GeoNetwork before 4.4.12 / 4.2.17 | 4.4.12 / 4.2.17 | Saxon が XSLT から Java 実行を許可；63219 と同一チェーン、未実行 | 確認済み | 未実施 |
| [CVE-2026-128046](CVE-2026-128046) | OpenMage LTS | 4.0 9.2 (VulnCheck)；3.1 8.1 (VulnCheck) | OpenMage magento-lts 20.17.0 before 20.18.2 and 21.0.0-beta1 before 21.0.0-beta3 | 20.18.2 / 21.0.0-beta3 | 未認証ゲストの .phar アップロードがラボで実行される；.phar を PHP に紐付け media/custom_options/ を公開する構成が必要 | 確認済み | 未実施 |
| [CVE-2026-69157](CVE-2026-69157) | atomic-server | 3.1 9.8 (GHSA) | atomic-server 0.29.0-0.40.1 (GHSA; NVD says to 0.40.2) |  | 未認証 /setup 招待で Drive 全書き込み権限；スクリプトは主張のみ、未検証 | 確認済み | 未実施 |
| [CVE-2026-130648](CVE-2026-130648) | WWBN AVideo | 3.1 8.7 (GHSA)；4.0 9.3 (NVD) | WWBN AVideo from 6.5 (GHSA; no fixed version listed) |  | javascript: videoLink による格納型 XSS；スクリプトは主張のみ、未検証 | 確認済み | 未実施 |
| [CVE-2026-69158](CVE-2026-69158) | atomic-server | 3.1 8.6 (GHSA) | atomic-server <= 0.40.1 |  | 未認証 /bookmark 完全応答 SSRF；スクリプトは主張のみ、未検証 | 確認済み | 未実施 |
| [CVE-2026-69156](CVE-2026-69156) | atomic-server | 3.1 8.1 (GHSA) | atomic-server 0.30.0-0.40.1 |  | internalId による任意ファイル読み取り；PoC の未認証主張は GHSA と矛盾 | 確認済み | 未実施 |
| [CVE-2026-100397](CVE-2026-100397) | Rucio | 3.1 9.8 (GHSA) | Rucio server < 36.4.1 (per PoC; GHSA lists branch fixes 35.9.1 / 38.6.1 / 40.4.2 / 41.1.1) | 36.4.1 (per PoC); GHSA branches 35.9.1 / 38.6.1 / 40.4.2 / 41.1.1 | SSH チャレンジトークンで任意アカウントになりすまし；未認証の管理者なりすまし、未検証 | 確認済み | 未実施 |
| [CVE-2026-126967](CVE-2026-126967) | SmarterMail | 3.0 8.8 (GHSA) | SmarterMail all builds < 9735 | Build 9735 | 認証後ファイルストレージ traversal で ASPX ウェブシェルを SYSTEM 権限で書き込み；スクリプトは主張のみ、未検証 | 確認済み | 未実施 |
| [CVE-2026-71481](CVE-2026-71481) | altcha | 3.1 7.5 (GHSA) | altcha-org/altcha (Composer) >= 2.0.0, < 2.0.3 (GHSA; PoC claims altcha-lib <= 0.5.x) | 2.0.3 (GHSA); v0.6.0 (per PoC) | 欠落/空の HMAC 署名が受理される；1 リクエストで CAPTCHA 回避、未検証 | 確認済み | 未実施 |
| [CVE-2026-1492](CVE-2026-1492) | User Registration & Membership | 3.1 9.8 (Wordfence) | User Registration & Membership ≤ 5.1.2 | 5.1.3 | 未認証で会員登録の role パラメータから管理者アカウントを作成；5.1.3 で修正 | 確認済み | 未実施 |
| [CVE-2026-129493](CVE-2026-129493) | Bolo | 4.0 8.7 (VulnCheck) | Bolo (bolo-solo) 1.7–2.6.4 | none (unfixed upstream) | 未認証で公開 GET /articles から記事閲覧パスワードが漏洩 | 確認済み | 未実施 |
| [CVE-2026-129494](CVE-2026-129494) | CloudPaste | 4.0 8.7 (VulnCheck) | CloudPaste 1.1.0–1.9.1 | none (unfixed upstream) | 未認証で POST /api/proxy/link から WebDAV 認証情報が漏洩 | 確認済み | 未実施 |
| [CVE-2026-129492](CVE-2026-129492) | Bolo | 4.0 5.3 (VulnCheck) | Bolo (bolo-solo) 1.7–2.6.4 | none (unfixed upstream) | 未認証の格納型 XSS（commentOriginalCommentName）、セッション窃取 | 確認済み | 未実施 |
| [CVE-2026-129491](CVE-2026-129491) | forum-java | 4.0 5.1 (VulnCheck) | forum-java 20f7e68–63152c4 | none (unfixed upstream) | 認証済み格納型 XSS（コメント返信ダイアログ）、セッション窃取 | 確認済み | 未実施 |
| [CVE-2026-130354](CVE-2026-130354) | phpMyFAQ | 4.0 6.9 (VulnCheck) | phpMyFAQ 4.1.0–4.1.11 | 4.1.12 | 未認証で WebAuthn 登録により有効なアカウントを作成、承認とドメインホワイトリストを回避 | 確認済み | 未実施 |
| [CVE-2026-130347](CVE-2026-130347) | phpMyFAQ | 4.0 6.3 (VulnCheck) | phpMyFAQ before 4.1.12 (4.2.0-alpha before 4.2.0-RC.2) | 4.1.12 / 4.2.0-RC.2 | パスワードリセットで外部 ID（OIDC/LDAP/SSO）アカウントの認証を回避、IdP の MFA を迂回 | 確認済み | 未実施 |
| [CVE-2026-110960](CVE-2026-110960) | Auth Armor | 3.1 9.8 (GHSA) | Auth Armor ≤ 1.0.3 | unknown | 未認証で漏洩した API 認証情報と登録リセットによりアカウントを乗っ取り；修正バージョン不明 | 確認済み | 未実施 |
| [CVE-2026-126269](CVE-2026-126269) | NocoDB | 4.0 9.3 (VulnCheck) | NocoDB < 2026.09.0 | 2026.09.0 | 添付 MIME 許可リストの部分一致で text/html が同一オリジンで描画される格納型 XSS；2026.09.0 で修正 | 確認済み | 未実施 |
| [CVE-2026-126274](CVE-2026-126274) | NocoDB | 4.0 9.3 (VulnCheck) | NocoDB < 2026.08.1 | 2026.08.1 | テーブル/列タイトルが削除ダイアログで innerHTML 経由で描画される格納型 XSS；2026.08.1 で修正 | 確認済み | 未実施 |
| [CVE-2026-126273](CVE-2026-126273) | NocoDB | 4.0 9.2 (VulnCheck) | NocoDB < 2026.09.0 | 2026.09.0 | 最初の未認証サインアップが未完了の管理者ブートストラップでスーパー管理者を取得；2026.09.0 で修正 | 確認済み | 未実施 |
| [CVE-2026-126937](CVE-2026-126937) | Zipline | 4.0 9.2 (VulnCheck); 3.1 8.1 (GHSA) | Zipline ≤ 4.6.4 | 4.6.5 | 初期設定 TOCTOU 競合で SUPERADMIN を複数作成可能；ラボ証拠あり、未検証 | 確認済み | 未実施 |
| [CVE-2026-124020](CVE-2026-124020) | Control Web Panel | 4.0 9.2 (VulnCheck); 3.1 8.1 (GHSA) | CWP < 1.30.6 (CWP and CWPpro) | 1.30.6 | Host ヘッダーによるパスワードリセット汚染で回復コード奪取；アカウント乗っ取り、RCE は主張のみ、未検証 | 確認済み | 未実施 |
| [CVE-2026-119258](CVE-2026-119258) | Swipe WordPress plugin | 3.1 8.1 (GHSA) | Swipe WordPress plugin <= 1.4 | no vendor patch at disclosure | 未認証 AJAX ハンドラが任意の有効セッションにセッション Cookie を発行；管理者乗っ取り、未検証 | 確認済み | 未実施 |
| [CVE-2026-100105](CVE-2026-100105) | Grafana | 3.1 7.7 (GHSA) | Grafana 12.4.0–12.4.13, 13.0.0–13.0.11, 13.1.0–13.1.8, 13.2.0–13.2.4 | 12.4.14 / 13.0.12 / 13.1.9 / 13.2.5 | レガシースキーマへのダウングレードで連絡先の認可を回避；アラートペイロードが転送される、ラボ証拠あり | 確認済み | 未実施 |
| [CVE-2026-129357](CVE-2026-129357) | Magma NMS | 4.0 2.1 (VulnDB); 3.1 6.3 (VulnDB) | Magma <= 1.9.0 | no upstream fix (synthetic remediation in lab) | host 組織の読み取り専用メンバーが 1 回の POST で SUPERUSER を作成；ラボ証拠あり | 確認済み | 未実施 |
| [CVE-2026-131850](CVE-2026-131850) | ILIAS | 4.0 8.6 (VulnCheck) | ILIAS 11.0 - 11.5.x | 11.6 | 管理者の ORDER BY SQLi（登録コード表）；ブールプローブとブラインド抽出、未検証 | 確認済み | 未実施 |
| [CVE-2026-13447](CVE-2026-13447) | MStore API | 3.1 9.8 (Wordfence) | MStore API <= 4.20.0 (lab 4.18.4) | 4.21.1 | 未認証 JWT 偽造で管理者乗っ取り；署名検証なし、ラボ 4.18.4 で検証済み | 確認済み | 未実施 |
| [CVE-2026-13355](CVE-2026-13355) | Meta Box AIO | 3.1 9.8 (Wordfence) | Meta Box AIO <= 3.11.0; MB Frontend Submission <= 4.5.6; MB User Profile <= 3.11.0 | 3.12.0 | 未認証でフロントエンド送信の連鎖により管理者アカウント作成；公開 mbfs フォームが必要、未検証 | 確認済み | 未実施 |
| [CVE-2026-1357](CVE-2026-1357) | WPvivid Backup & Migration | 3.1 9.8 (Wordfence) | WPvivid Backup & Migration <= 0.9.123 | 0.9.124 | RSA フェイルオープンとパストラバーサルで未認証の任意 PHP アップロード；生成済み API トークンが必要、Docker ラボで RCE | 確認済み | 未実施 |
| [CVE-2026-133117](CVE-2026-133117) | Product Feed for WooCommerce | 4.0 8.8 (VulnCheck); 3.1 8.2 (VulnCheck) | WebToffee Product Feed before 2.4.4 | 2.4.4 | ハードコードされた cron ソルトによる未認証の管理操作トリガー、未検証 | 確認済み | 未実施 |
| [CVE-2026-133092](CVE-2026-133092) | TeamCity | 3.1 8.8 (JetBrains) | JetBrains TeamCity before 2026.2.2, 2026.1.6 | 2026.2.2 / 2026.1.6 | Git サブモジュール URL による RCE（検出型 PoC、未検証） | 確認済み | 未実施 |
| [CVE-2026-133086](CVE-2026-133086) | TeamCity | 3.1 8.8 (JetBrains) | JetBrains TeamCity before 2026.2.2, 2026.1.6 | 2026.2.2 / 2026.1.6 | Kotlin DSL サンドボックスの URL ストリームハンドラによる RCE（検出型 PoC、未検証） | 確認済み | 未実施 |
| [CVE-2026-133087](CVE-2026-133087) | TeamCity | 3.1 8.8 (JetBrains) | JetBrains TeamCity before 2026.2.2, 2026.1.6 | 2026.2.2 / 2026.1.6 | Kotlin DSL サンドボックスのタイムゾーンコールバックによる RCE（検出型 PoC、未検証） | 確認済み | 未実施 |
| [CVE-2026-133172](CVE-2026-133172) | cozy-stack | 4.0 8.7 (VulnCheck); 3.1 8.8 (VulnCheck) | cozy-stack before 1.6.69 | 1.6.69 | 共有ドライブ移動の認可バイパスによる他テナントのファイル露出、未検証 | 確認済み | 未実施 |
| [CVE-2026-133234](CVE-2026-133234) | stoatchat | 4.0 8.7 (VulnCheck); 3.1 7.5 (VulnCheck) | stoatchat before 0.16.5 | 0.16.5 | JXL デコードの無制限によるメモリ枯渇 DoS、未検証 | 確認済み | 未実施 |
| [CVE-2026-133235](CVE-2026-133235) | Tandoor Recipes | 4.0 8.3 (VulnCheck); 3.1 7.7 (VulnCheck) | Tandoor Recipes before 2.7.4 | 2.7.4 | Nextcloud WebDAV 経由の SSRF で内部ホストに到達、未検証 | 確認済み | 未実施 |
| [CVE-2026-133173](CVE-2026-133173) | WatchAlert | 4.0 7.1 (VulnCheck); 3.1 6.5 (VulnCheck) | WatchAlert 2.0.0 through 3.9.20 | 3.9.21 | テナント横断 IDOR による監視認証情報の漏洩、未検証 | 確認済み | 未実施 |
| [CVE-2026-133113](CVE-2026-133113) | Gogs | 4.0 7.1 (VulnCheck); 3.1 6.5 (VulnCheck) | Gogs through 0.14.4 | 0.14.5 | PR マージ API による保護ブランチのバイパス、未検証 | 確認済み | 未実施 |
| [CVE-2026-133114](CVE-2026-133114) | WooCommerce Side Cart | 4.0 5.3 (VulnCheck); 3.1 4.3 (VulnCheck) | Caddy WooCommerce Side Cart 3.0.0 before 3.2.1 | 3.2.1 | saved-items エンドポイントの認可欠如による非公開商品データの露出、未検証 | 確認済み | 未実施 |
| [CVE-2026-133080](CVE-2026-133080) | TeamCity | 3.1 8.8 (JetBrains) | JetBrains TeamCity before 2026.2.2, 2026.1.6 | 2026.2.2 / 2026.1.6 | Maven リポジトリ設定経由のリモートコード実行；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-133015](CVE-2026-133015) | TeamCity | 3.1 8.8 (JetBrains) | JetBrains TeamCity before 2026.2.1, 2026.1.5 | 2026.2.1 / 2026.1.5 | Kotlin DSL ブートクラスパスライブラリ経由のリモートコード実行；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-133016](CVE-2026-133016) | TeamCity | 3.1 8.8 (JetBrains) | JetBrains TeamCity before 2026.2.1, 2026.1.5 | 2026.2.1 / 2026.1.5 | Kotlin DSL スクリプト定義経由のリモートコード実行；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-133018](CVE-2026-133018) | TeamCity | 3.1 8.8 (JetBrains) | JetBrains TeamCity before 2026.2.1, 2026.1.5 | 2026.2.1 / 2026.1.5 | Kotlin DSL UI パッチコールバック経由のリモートコード実行；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-133019](CVE-2026-133019) | TeamCity | 3.1 8.8 (JetBrains) | JetBrains TeamCity before 2026.2.1, 2026.1.5 | 2026.2.1 / 2026.1.5 | Kotlin DSL コンテキストパラメータコールバック経由のリモートコード実行；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-133027](CVE-2026-133027) | TeamCity | 3.1 8.8 (JetBrains) | JetBrains TeamCity before 2026.2.1, 2026.1.5 | 2026.2.1 / 2026.1.5 | トークン認証のユーザ名処理による権限昇格；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-133089](CVE-2026-133089) | TeamCity | 3.1 8.1 (JetBrains) | JetBrains TeamCity before 2026.2.2, 2026.1.6 | 2026.2.2 / 2026.1.6 | TFS ヘルパープロセスの未認証コマンドサーバ；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-22309](CVE-2026-22309) | JTL-Shop | 3.1 9.3 (JTL); 4.0 8.6 (JTL) | JTL-Shop 5.6.0-5.8.3 | 5.8.4 / 5.7.6 / 5.6.6 (2026-11-12) | 訪問者トラッキングのクローラ User-Agent 経由の格納型 XSS；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-91115](CVE-2026-91115) | silverstripe-framework | 3.1 8.8 (GHSA) | Silverstripe Framework 6.0.0-6.2.12 | 6.2.13 | Silverstripe i18nTextCollectorTask の安全でないクラスインスタンス化；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-133095](CVE-2026-133095) | TeamCity | 3.1 8.1 (JetBrains) | JetBrains TeamCity before 2026.2.2, 2026.1.6 | 2026.2.2 / 2026.1.6 | TeamCity Hub 統合設定の CSRF；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-133017](CVE-2026-133017) | TeamCity | 3.1 8.0 (JetBrains) | JetBrains TeamCity before 2026.2.1, 2026.1.5 | 2026.2.1 / 2026.1.5 | TeamCity Git VCS ルート設定経由のリモートコード実行；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-72898](CVE-2026-72898) | Metabase | 3.1 10.0 (GHSA); 4.0 10.0 (GHSA) | Metabase 58.0-<58.24, 59.0-<59.21, 60.0-<60.17, 61.0-<61.11, 62.0-<62.9, 63.0-<63.5 | 58.24 / 59.21 / 60.17 / 61.11 / 62.9 / 63.5 | 未認証 SQL インジェクションによる管理者権限奪取；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-21962](CVE-2026-21962) | Oracle HTTP Server | 3.1 10.0 (Oracle) | Oracle HTTP Server 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0 | Oracle Critical Patch Update January 2026 | Oracle HTTP Server / WebLogic プロキシプラグインの認証バイパス；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-105899](CVE-2026-105899) | ColdFusion | 3.1 10.0 (Adobe) | Adobe ColdFusion 2025 before Update 14, 2023 before Update 26 | 2025 Update 14 / 2023 Update 26 (APSB26-144) | ColdFusion の無制限ファイルアップロードによるリモートコード実行；検出型 PoC、未検証 | 確認済み | ◐ 部分 |
| [CVE-2026-133083](CVE-2026-133083) | TeamCity | 3.1 8.0 (JetBrains) | JetBrains TeamCity before 2026.2.2, 2026.1.6 | 2026.2.2 / 2026.1.6 | TeamCity Server Health レポートの格納型 XSS；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-133091](CVE-2026-133091) | TeamCity | 3.1 8.0 (JetBrains) | JetBrains TeamCity before 2026.2.2, 2026.1.6 | 2026.2.2 / 2026.1.6 | TeamCity ユーザーページの格納型 XSS；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-22310](CVE-2026-22310) | JTL-Shop | 3.1 8.0 (JTL); 4.0 7.6 (JTL) | JTL-Shop 5.5.0-5.8.3 | 5.8.4 / 5.7.6 / 5.6.6 / 5.5.5 (2026-11-11) | JTL-Shop 404 リダイレクトの格納型 XSS；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-106622](CVE-2026-106622) | ColdFusion | 3.1 10.0 (Adobe) | Adobe ColdFusion 2025 before Update 14, 2023 before Update 26 | 2025 Update 14 / 2023 Update 26 (APSB26-144) | ColdFusion の SSRF；検出型 PoC、未検証 | 確認済み | ◐ 部分 |
| [CVE-2026-106624](CVE-2026-106624) | ColdFusion | 3.1 10.0 (Adobe) | Adobe ColdFusion 2025 before Update 14, 2023 before Update 26 | 2025 Update 14 / 2023 Update 26 (APSB26-144) | ColdFusion のコードインジェクションによるリモートコード実行；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-22308](CVE-2026-22308) | JTL-Shop | 3.1 9.3 (ENISA); 4.0 8.6 (ENISA) | JTL-Shop 5.0.0-5.8.3 | 5.8.4 / 5.7.6 / 5.6.6 / 5.5.5 (JTL advisory 2026-11-12) | JTL-Shop の OPC プレビューモード経由の反射型 XSS；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-130158](CVE-2026-130158) | RepoManager | 3.1 9.0 (GitHub) | RepoManager <5.13.3 | 5.13.3 | RepoManager のホスト報告パッケージメタデータ経由の格納型 XSS；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-130236](CVE-2026-130236) | Auth0 Authorization Extension | 3.1 8.5 (Okta) | Auth0 Authorization Extension <2.13 | 2.13 | Auth0 Authorization Extension の API 認証とルール生成の不備；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-129048](CVE-2026-129048) | WP Photo Album Plus | 3.1 9.9 (Patchstack) | WP Photo Album Plus <=9.3.06.003 | 9.3.07.001 | WP Photo Album Plus のリモートコードインクルージョン；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-14492](CVE-2026-14492) | WP Duplicate – WordPress Migration Plugin | 3.1 9.8 (Wordfence) | WP Duplicate <=1.1.11 | No known patch | WP Duplicate の未認証任意ファイルアップロードによる RCE；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-130754](CVE-2026-130754) | LaraDashboard | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | LaraDashboard <=1.5.4 | No fix released (latest 1.5.4) | LaraDashboard OAuth ログインの未検証メールによる任意アカウント乗っ取り；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2023-54422](CVE-2023-54422) | iDocView | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | iDocView <13.10.1_20231115 | 13.10.1_20231115 | iDocView /html/2word の未認証任意ファイルアップロードによる RCE；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2023-54419](CVE-2023-54419) | nginxWebUI | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | nginxWebUI 3.0.0-3.5.7 | 3.5.8 | nginxWebUI の認証バイパスによる runCmd コマンド実行；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2022-51027](CVE-2022-51027) | MeterSphere | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | MeterSphere 1.13.0-1.14.6 / 1.15.0-1.16.3 | 1.14.7 / 1.16.4 | MeterSphere の認証前プラグインエンドポイントのコードインジェクションによる RCE；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2021-48025](CVE-2021-48025) | OpenSNS | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | OpenSNS 3.2.1 | No known patch | OpenSNS shareBox の未認証コードインジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2021-48023](CVE-2021-48023) | Weaver E-cology | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | Weaver E-cology 9.0 | No known patch | Weaver E-cology uploadOperation.jsp の未認証任意ファイルアップロードによる RCE；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2018-25443](CVE-2018-25443) | Baidu UEditor | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | Baidu UEditor 1.4.0-1.4.3.3 | No known patch | Baidu UEditor catchimage の未認証任意ファイルアップロードによる RCE；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-114516](CVE-2026-114516) | Etherpad | 3.1 9.8 (GHSA) | Etherpad 1.8.14-3.3.2 | 3.3.3 | Etherpad の認証前パストラバーサルによる任意ファイル読み取り；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-77369](CVE-2026-77369) | Daptin | 3.1 9.6 (GHSA) | Daptin 0.11.4-0.12.29 | 0.12.30 | Daptin YJS コラボレーションエンドポイントのアクセス制御不備により制限行の読み書きが可能；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-71499](CVE-2026-71499) | cf-manager | 3.1 10 (GHSA) | cf-manager <1.1.2 | 1.1.2 | cf-manager の SSRF による任意 Worker コード実行；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-77367](CVE-2026-77367) | Daptin | 3.1 9.4 (GHSA) | Daptin <0.12.30 | 0.12.30 | Daptin sort パラメータの未認証 SQL インジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-123058](CVE-2026-123058) | JTL-Shop | 4.0 9.2 (ENISA); 3.1 9 (ENISA) | JTL-Shop 5.5.0-5.5.4 / 5.6.0-5.6.5 / 5.7.0-5.7.5 / 5.8.0-5.8.3 | 5.5.5 / 5.6.6 / 5.7.6 / 5.8.4 | JTL-Shop Web インストーラーの認証欠如による未認証乗っ取り；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-110009](CVE-2026-110009) | Unzer Payments | 3.1 9.8 (Wordfence) | Unzer Payments <=2.2.1 | 无已知补丁（Wordfence 2026-11-18：Patched? No） | Unzer Payments の未認証の認証バイパスによるアカウント乗っ取り；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-110811](CVE-2026-110811) | Trust Payments Gateway for WooCommerce (JavaScript Library) | 3.1 9.8 (Wordfence) | Trust Payments Gateway for WooCommerce (JavaScript Library) <=1.3.8 | 无已知补丁（Wordfence 2026-11-18：Patched? No） | Trust Payments Gateway の未認証の認証バイパスによる管理者乗っ取り；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-124990](CVE-2026-124990) | Masteriyo LMS – LMS Course Builder, Quizzes & Certificates | 3.1 9.8 (Wordfence) | Masteriyo LMS <=3.5.1 | 3.5.2 | Masteriyo LMS の PHP オブジェクトインジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-130735](CVE-2026-130735) | Grav | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | Grav 2.0.0 to <2.2.18 | 2.2.18 | Grav の Twig インジェクションによるコード実行；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-55506](CVE-2026-55506) | Wavelog | 3.1 9.6 (GHSA) | Wavelog <2.5 | 2.5 | Wavelog QSL 画像ファイル名のパストラバーサルによる任意ファイル削除；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-130156](CVE-2026-130156) | Bazarr | 3.1 9.4 (GHSA) | Bazarr <1.6.3-beta.11 | 1.6.3-beta.11 | Bazarr 字幕操作のパストラバーサルによる任意ファイル読み書き；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-55508](CVE-2026-55508) | Wavelog | 3.1 9.4 (GHSA) | Wavelog <2.5 | 2.5 | Wavelog OQRS の未認証 SQL インジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-130160](CVE-2026-130160) | RepoManager | 3.1 8.8 (GHSA) | RepoManager <5.13.3 | 5.13.3 | RepoManager の認証済み OS コマンドインジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-132906](CVE-2026-132906) | TeamCity | 3.1 8.8 (JetBrains) | TeamCity <2026.2 / <2026.1.4 / <2025.11.8 | 2026.2 / 2026.1.4 / 2025.11.8 | TeamCity の Kotlin DSL サンドボックス逃逸による RCE；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-132909](CVE-2026-132909) | TeamCity | 3.1 8.8 (JetBrains) | TeamCity <2026.2 / <2026.1.4 / <2025.11.8 | 2026.2 / 2026.1.4 / 2025.11.8 | TeamCity の Mercurial リポジトリ内容による RCE；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-132917](CVE-2026-132917) | TeamCity | 3.1 8.8 (JetBrains) | TeamCity <2026.2 / <2026.1.4 / <2025.11.8 | 2026.2 / 2026.1.4 / 2025.11.8 | TeamCity の Kotlin DSL ファイル書き込みバイパスによる RCE；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-133476](CVE-2026-133476) | Dolibarr | 3.1 8.8 (MITRE) | Dolibarr <24.0.3 | 24.0.3 | Dolibarr の SQL フィルタバイパスによるアカウント乗っ取り；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-125061](CVE-2026-125061) | JTL PayPal Checkout plugin | 4.0 8.5 (JTL); 3.1 8.7 (JTL) | JTL PayPal Checkout plugin 1.2.0–2.3.1 | 2.3.2 / 2.2.2 | JTL PayPal Checkout プラグインの格納型 XSS；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-122676](CVE-2026-122676) | PublishPress Authors | 3.1 8.5 (Patchstack) | PublishPress Authors <=4.18.0 | 4.20.0 | PublishPress Authors のブラインド SQL インジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-132913](CVE-2026-132913) | TeamCity | 3.1 8.4 (JetBrains) | TeamCity <2026.2 / <2026.1.4 / <2025.11.8 | 2026.2 / 2026.1.4 / 2025.11.8 | TeamCity の P4 コードレビューにおける格納型 XSS；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-103035](CVE-2026-103035) | TeamPass | 3.1 8.3 (GHSA) | TeamPass <3.2.1.2 | 3.2.1.2 | TeamPass のフォルダ権限バイパスによる認証情報ツリーの奪取；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-125060](CVE-2026-125060) | JTL-Shop | 4.0 8.8 (JTL); 3.1 8.2 (JTL) | JTL-Shop 5.2.0–5.8.3 | 5.8.4 / 5.7.6 / 5.6.6 / 5.5.5 | JTL-Shop のチェックアウトにおける配送先住所の IDOR；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-59988](CVE-2026-59988) | django-docutils | 3.1 8.2 (GHSA) | django-docutils <0.30.0 | 0.30.0 | django-docutils の信頼できない RST レンダリングによるファイル読み取り・SSRF・格納型 XSS；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-103026](CVE-2026-103026) | Paymenter | 3.1 8.1 (GHSA) | Paymenter <1.5.7 | 1.5.7 | Paymenter の Livewire 確認アクションによる未認証のサーバー状態改ざん；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-132892](CVE-2026-132892) | TeamCity | 3.1 8.1 (JetBrains) | TeamCity <2026.2 | 2026.2 | TeamCity の認可フローによる権限昇格；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-132907](CVE-2026-132907) | TeamCity | 3.1 8.1 (JetBrains) | TeamCity <2026.2 / <2026.1.4 / <2025.11.8 | 2026.2 / 2026.1.4 / 2025.11.8 | TeamCity のプロジェクト閲覧者による親プロジェクトの GitHub App 認証情報のリダイレクト；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-129056](CVE-2026-129056) | Authorizer | 3.1 9.8 (Patchstack) | Authorizer <3.17.2 | 3.17.2 | Authorizer の権限割り当ての不備による権限昇格；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-89095](CVE-2026-89095) | Shortcodes and extra features for Phlox theme | 3.1 8.1 (Wordfence) | Shortcodes and extra features for Phlox theme <=2.17.22 | 2.17.24 | Phlox テーマ用プラグインのローカルファイルインクルージョン；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-120556](CVE-2026-120556) | Toocheke Companion | 3.1 8.1 (Wordfence) | Toocheke Companion <=2.38 | 2.39 | Toocheke Companion の認可欠如による任意の投稿・添付ファイル削除；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-131795](CVE-2026-131795) | Aora | 3.1 8.1 (Patchstack) | Aora <=1.3.5 | 1.3.24 | Aora テーマの PHP ローカルファイルインクルージョン；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-132903](CVE-2026-132903) | TeamCity | 3.1 8.1 (JetBrains) | TeamCity <2026.2 / <2026.1.4 / <2025.11.8 | 2026.2 / 2026.1.4 / 2025.11.8 | TeamCity の認可欠如によるクラウドエージェントの起動・停止；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-109555](CVE-2026-109555) | WP STAGING / WP STAGING Pro | 3.1 8.0 (Wordfence) | WP STAGING <=4.17.0 / WP STAGING Pro <=6.17.0 | 4.18.0 / 6.18.0 | WP STAGING の PHP オブジェクトインジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-132914](CVE-2026-132914) | TeamCity | 3.1 8.0 (JetBrains) | TeamCity <2026.2 / <2026.1.4 / <2025.11.8 | 2026.2 / 2026.1.4 / 2025.11.8 | TeamCity の Issue Log タブにおける格納型 XSS；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-133500](CVE-2026-133500) | Gladys Assistant | 4.0 8.5 (VulDB); 3.1 9.1 (VulDB) | Gladys Assistant <=4.71.0 | 4.72.0 | Gladys Assistant のバックアップ復元エンドポイントにおける OS コマンドインジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-133501](CVE-2026-133501) | Gladys Assistant | 4.0 8.5 (VulDB); 3.1 9.0 (VulDB) | Gladys Assistant <=4.71.0 | 4.72.0 | Gladys Assistant のバックアップ復元ハンドラにおけるパストラバーサル；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-128915](CVE-2026-128915) | InstaWP Connect | 3.1 8.5 (Patchstack) | InstaWP Connect <=0.1.4.4 | 0.1.4.5 | InstaWP Connect のブラインド SQL インジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-130010](CVE-2026-130010) | Chatterbug Forms | 3.1 8.1 (Wordfence) | Chatterbug Forms <=1.1 | 1.2 | Chatterbug Forms の未認証任意ファイル削除；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-120681](CVE-2026-120681) | Mang Board | 3.1 9.1 (Wordfence) | Mang Board <=2.4.7 | 2.4.8 | Mang Board の未認証任意掲示板投稿削除；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-125085](CVE-2026-125085) | Nexter Extension | 3.1 8.8 (Wordfence) | Nexter Extension <=4.9.0 | 4.9.1 | Nexter Extension の権限昇格による管理者化；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-118522](CVE-2026-118522) | Video & Photo Gallery for Ultimate Member | 3.1 8.1 (Wordfence) | Video & Photo Gallery for Ultimate Member <=1.1.4 | 1.1.5 | Video & Photo Gallery for Ultimate Member の任意ファイル削除；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-126716](CVE-2026-126716) | Mega Forms | 3.1 8.1 (Wordfence) | Mega Forms <=1.7.9 | 1.8.0 | Mega Forms の未認証任意ファイル削除；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-129073](CVE-2026-129073) | miniorange-otp-verification | 3.1 9.8 (Patchstack) | miniorange-otp-verification <=5.6.1 | 5.6.2 | miniOrange OTP 検証プラグインの代替経路による認証バイパス；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-15826](CVE-2026-15826) | User Profile Builder | 3.1 9.8 (Wordfence) | User Profile Builder <=3.16.4 | 3.16.5 | User Profile Builder の型混同による未認証認証バイパス；検出型 PoC、未検証；Wordfence が攻撃ブロックを報告 | 確認済み | 未実施 |
| [CVE-2026-129039](CVE-2026-129039) | Newsletters | 3.1 9.8 (Patchstack) | Newsletters <= 4.18.2 | 4.18.3 | Newsletters のデシリアライゼーションによるオブジェクトインジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-129043](CVE-2026-129043) | Newsletters | 3.1 9.3 (Patchstack) | Newsletters <= 4.18.2 | 4.18.3 | Newsletters の SQL インジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-14914](CVE-2026-14914) | Tegsoft Contact Center | 3.1 10.0 (USOM) | Tegsoft Contact Center before latest-202611161510 | latest-202611161510 | Tegsoft Contact Center の無制限ファイルアップロードによる Web シェル；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-80188](CVE-2026-80188) | BuddyBoss Addons | 3.1 9.8 (Wordfence) | BuddyBoss Addons <= 1.2.1 | 1.2.2 | BuddyBoss Addons の未検証ソーシャルログイン ID トークンによる未認証アカウント乗っ取り；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2025-42884](CVE-2025-42884) | SAP NetWeaver Enterprise Portal | 3.1 6.5 (SAP) | SAP NetWeaver Enterprise Portal EP-BASIS 7.50 / EP-RUNTIME 7.50 | Per SAP Note 3660969 | SAP NetWeaver Enterprise Portal における JNDI インジェクション；CISA KEV 2026-11-20 収録、公開 PoC なし | 確認済み | 未実施 |
| [CVE-2026-128049](CVE-2026-128049) | OpenMage Magento LTS | 4.0 9.4 (VulnCheck); 3.1 9.0 (VulnCheck) | OpenMage Magento LTS before 20.18.2; 21.0.0-beta1 before 21.0.0-beta3 | 20.18.2 / 21.0.0-beta3 | OAuth 確認アクションにおける CSRF、form-key 検証なしの GET リクエスト；検出用 PoC のみ、未検証 | 確認済み | 未実施 |
| [CVE-2026-126380](CVE-2026-126380) | Vvveb CMS | 4.0 9.4 (VulnCheck); 3.1 9.1 (VulnCheck) | Vvveb before 1.0.9.0 | 1.0.9.0 | 認証済み管理者による .phar アップロードでメディアの拒否リストを回避し、ポリグロット webshell を配置可能；検出用 PoC のみ、未検証 | 確認済み | 未実施 |
| [CVE-2026-94565](CVE-2026-94565) | NukeViet CMS | 3.1 9.3 (GHSA) | NukeViet CMS 3.x through 4.6.01 (Contact module) | 4.6.01 | 未認証の訪問者が Contact モジュール経由でスラッシュ付きイベントハンドラ属性を含むメッセージを送信し stored XSS；検出用 PoC のみ、未検証 | 確認済み | 未実施 |
| [CVE-2026-94567](CVE-2026-94567) | NukeViet CMS | 3.1 9.3 (GHSA) | NukeViet CMS before 4.5.12 and 4.6.02 (SVG upload) | 4.5.12 / 4.6.02 | SVG アップロードで内部 DTD エンティティに script 要素を隠し stored XSS；検出用 PoC のみ、未検証 | 確認済み | 未実施 |
| [CVE-2026-94598](CVE-2026-94598) | NukeViet CMS | 3.1 8.2 (GHSA) | NukeViet CMS 4.5.08 through 4.5.12 and 4.6.02 (iframe srcdoc) | 4.5.12 / 4.6.02 | iframe srcdoc 値にサニタイザマーカーを偽造し stored XSS；検出用 PoC のみ、未検証 | 確認済み | 未実施 |
| [CVE-2026-54064](CVE-2026-54064) | NukeViet CMS | 3.1 8.7 (GHSA) | NukeViet CMS before 4.5.09 (news posting) | 4.5.09 | ニュース投稿権限を持つユーザーがフォームフィード付きイベントハンドラで filterAttr() を回避し stored XSS；検出用 PoC のみ、未検証 | 確認済み | 未実施 |
| [CVE-2026-54065](CVE-2026-54065) | NukeViet CMS | 3.1 8.7 (GHSA) | NukeViet CMS before 4.5.09 (comment admin edit) | 4.5.09 | 認証済み管理者がコメント attach 値のパストラバーサルでアプリケーションファイルを削除可能；検出用 PoC のみ、未検証 | 確認済み | 未実施 |
| [CVE-2026-77326](CVE-2026-77326) | MapServer | 3.1 8.6 (GHSA) | MapServer 8.2.0 through 8.6.5 (WMS GetLegendGraphic) | 8.6.5 | 未認証の攻撃者が WMS GetLegendGraphic でヒープバッファオーバーフローを起こしプロセスをクラッシュ；クラッシュ PoC のみ、RCE は未実証 | 確認済み | 未実施 |
| [CVE-2026-94564](CVE-2026-94564) | NukeViet CMS | 3.1 8.2 (GHSA) | NukeViet CMS before 4.6.01 (Contact module) | 4.6.01 | 未認証の訪問者が URL 属性内の先行ゼロ付き数値 HTML エンティティで stored XSS；検出用 PoC のみ、未検証 | 確認済み | 未実施 |
| [CVE-2026-133874](CVE-2026-133874) | Iceburg CRM | 4.0 8.6 (VulnCheck); 3.1 8.1 (VulnCheck) | Iceburg CRM through 5.0.0 | No known patch | 認証済みユーザーが saveRecord() で未認可モジュールに書き込み、管理者に昇格可能；検出用 PoC のみ、未検証 | 確認済み | 未実施 |
| [CVE-2026-120539](CVE-2026-120539) | Restrictions for BuddyPress | 3.1 9.8 (NVD) | <= 1.5.4 (requires BuddyPress and Paid Memberships Pro both active) | 1.5.5 | 未認証コードインジェクション：リクエスト URI が {${...}} 補間経由で eval() に入る；検出型 PoC がインジェクションをトリガーしマーカーを返す | 確認済み | 未実施 |
| [CVE-2026-3300](CVE-2026-3300) | Everest Forms Pro | 3.1 9.8 (NVD) | <= 1.9.12 (requires Calculation Addon / Complex Calculation enabled) |  | 未認証 PHP コードインジェクション（Calculation Addon）；PoC がインジェクションをトリガーし PWNED を返す；2026-04-13 から実利用 | 確認済み | 未実施 |

### AI / LLM (20)

| ID | 製品 | スコア | 影響バージョン | 修正バージョン | 評価 | CVE ステータス | 再現 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [CVE-2026-85228](CVE-2026-85228) | Amazon Deep Java Library (DJL) | 3.1 9.1 (AMZN); 4.0 8.8 (AMZN) | Amazon Deep Java Library (DJL) 0.13.0–0.36.0 | 0.37.0 | DJL テンソルバッファ検証の整数オーバーフロー；未認証の情報漏洩/サービス拒否；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-40217](CVE-2026-40217) | BerriAI LiteLLM | 3.1 8.8 PR:L (public README) | LiteLLM before v1.83.11 (image digest pinning required; some rebuilt tags are not vulnerable) | v1.83.11+ (RestrictedPython) | 認証後のラボ RCE；API キーが必要 | 確認済み | ◐ 部分 |
| [CVE-2026-130796](CVE-2026-130796) | Flowise | 4.0 8.8 (VulnCheck)；3.1 8.2 (VulnCheck) | 3.1.3-3.1.4 |  | 未認証での平文 MCP トークン漏洩；付属スクリプトはオフラインの論理シミュレーション | 確認済み | ✅ 完全 |
| [CVE-2026-102895](CVE-2026-102895) | GPUStack | 3.1 9.8 (GHSA) | < 2.2.0 | 2.2.0 | ラボで検証された未認証の管理者乗っ取り；実利用はベンダー報告であり、この PoC による実証ではない | 確認済み | ◐ 部分 |
| [CVE-2026-59726](CVE-2026-59726) | Ruflo MCP Bridge | 3.1 10.0 (GHSA) | Ruflo < 3.16.3 (default docker-compose MCP bridge) | 3.16.3 | MCP bridge の terminal_execute による未認証 RCE；Exploit-DB で検証済み autopwn | 確認済み | 未実施 |
| [CVE-2026-63129](CVE-2026-63129) | mssql-mcp-core | 3.1 8.8 (GHSA) | mssql-mcp-core <= 0.5.0 (also reader <= 0.4.2, writer <= 0.4.2, server <= 0.5.2) | 0.6.0 | MCP ツール呼び出しの未パラメータ化による SQLi；xp_cmdshell は主張のみ、未検証 | 確認済み | 未実施 |
| [CVE-2026-73678](CVE-2026-73678) | Minds Platform | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | MindsDB Minds Platform 26.1.0 and earlier | No fixed release published in CVE record (2026-11-20) | 未認証リモートコード実行（Agent scratchpad exec()）；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-77312](CVE-2026-77312) | Flyto2 Core | 3.1 10.0 (GitHub) | Flyto2 Core <2.26.8 | 2.26.8 | Flyto2 Core の無防備な data/file モジュール経由の任意ファイル書き込み；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-77315](CVE-2026-77315) | Flyto2 Core | 3.1 8.5 (GitHub) | Flyto2 Core <2.26.8 | 2.26.8 | Flyto2 Core の http.paginate 経由の二次 SSRF；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-63189](CVE-2026-63189) | Dialoqbase | 3.1 9.8 (GHSA) | Dialoqbase <1.11.5 | 1.11.5 | Dialoqbase の未認証パストラバーサルによる任意ファイル読み取り；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-76807](CVE-2026-76807) | Todoist MCP Server | 3.1 9.3 (GHSA) | Todoist MCP Server <10.3.3 | 10.3.3 | Todoist MCP Server の DNS リバインディングによる Web サイトからの Todoist データ書き込み・削除；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-130154](CVE-2026-130154) | Zyrabit Platform | 3.1 9.1 (GHSA) | Zyrabit Platform <2.4.4 | 2.4.4 | Zyrabit import_to_vault のパストラバーサルによる任意ファイル読み書き；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-77359](CVE-2026-77359) | Jupyter MCP Server | 4.0 9.3 (GHSA) | Jupyter MCP Server <1.0.3 | 1.0.3 | Jupyter MCP Server の DNS リバインディングによるバックエンド乗っ取り；通告内に再現可能な PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-131304](CVE-2026-131304) | Splunk AI Assistant | 3.1 8.1 (Splunk) | Splunk AI Assistant <2.0.0 | 2.0.0 | Splunk AI Assistant のテナント横断データアクセス；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-131305](CVE-2026-131305) | Splunk AI Assistant | 3.1 8.1 (Splunk) | Splunk AI Assistant <2.0.0 | 2.0.0 | Splunk AI Assistant の機能設定の未認証変更；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-93328](CVE-2026-93328) | Google Cloud MCP Toolbox for Databases | 4.0 9.3 (GoogleCloud) | Google Cloud MCP Toolbox for Databases 1.2.0-1.4.0 | past 1.4.0 + allowlists (googleapis/mcp-toolbox#3454) | Google Cloud MCP Toolbox のクラウドストレージにおけるパストラバーサルと認可欠落により、未認証でホストファイルを漏洩させ任意のローカルファイルを上書き可能；ラボ再現 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-133968](CVE-2026-133968) | MONAI Label | 3.1 9.8 (MITRE) | MONAI Label through 0.8.5 | Fix PR #1915 merged 2026-10-19; no tagged release as of 2026-11-21 | データストアのアップロードにおけるパストラバーサルによる任意ファイル書き込み、RCE に至る可能性；2026 年 9 月から実際に悪用、公開 PoC なし | 確認済み | 未実施 |
| [CVE-2026-48705](CVE-2026-48705) | MONAI | 3.1 9.3 (GHSA) | MONAI before 1.6.1 (PydicomReader); MONAILabel deployments using it | MONAI 1.6.1 | NaN／inf を含む DICOM により MONAILabel サーバがクラッシュし推論が破損；クラッシュ型 PoC、当リポジトリでは未検証 | 確認済み | 未実施 |
| [CVE-2026-118683](CVE-2026-118683) | MONAI | 4.0 8.6 (VulnCheck) | MONAI 1.2.0 before 1.6.1 | MONAI 1.6.1 | 悪意ある bundle の logging.conf がワークフロー構築時に fileConfig により評価されコード実行；検出用 PoC のみ、未検証 | 確認済み | 未実施 |
| [CVE-2026-54039](CVE-2026-54039) | LibreChat | 3.1 8.1 (GHSA) | LibreChat 0.7.0 through 0.8.6 (local registration + social provider) | 0.8.6 | 未認証の攻撃者が登録時に provider 値を偽造しアカウント乗っ取り；検出用 PoC のみ、未検証 | 確認済み | 未実施 |

### ネットワークとセキュリティ (148)

| ID | 製品 | スコア | 影響バージョン | 修正バージョン | 評価 | CVE ステータス | 再現 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [CVE-2026-130151](CVE-2026-130151) | Okta Privileged Access Gateway | 3.1 8.5 (Okta) | Okta Privileged Access Gateway <1.116.3 (RDP support) | 1.116.3 | Okta 特権アクセスゲートウェイの FreeRDP スマートカード処理によるコマンド実行；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-95643](CVE-2026-95643) | ManageEngine DDI Central | 3.1 9.1 (Zohocorp) | Zohocorp ManageEngine DDI Central build <6500 | 6500 | DDI Central Telnet 機能における IPv6 スコープ識別子を介した認証済み PowerShell コマンドインジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-95645](CVE-2026-95645) | ManageEngine DDI Central | 3.1 9.1 (Zohocorp) | Zohocorp ManageEngine DDI Central build <6500 | 6500 | DDI Central Windows エージェント clear_blocked_domains の認証済みコマンドインジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-104935](CVE-2026-104935) | Ivanti Connect Secure | 3.1 8.6 (Ivanti) | Ivanti Connect Secure 25.1.1.2 and prior; 25.1.2.2 and prior; 22.8R2.5 and prior | 25.1.1.3 / 22.8R2.6 | Ivanti Connect Secure の認証バイパス；実利用確認済み（KEV 2026-10-13）、公開 PoC なし | 確認済み | — 対象なし |
| [CVE-2026-111357](CVE-2026-111357) | Ivanti Connect Secure | 3.1 7.0 (NVD); 3.1 8.8 (Ivanti) | Ivanti Connect Secure 25.1.1.2 and prior; 25.1.2.2 and prior; 22.8R2.5 and prior | 25.1.1.3 / 22.8R2.6 | Ivanti Connect Secure の重要機能における認証欠如によるローカル権限昇格；実利用確認済み（KEV 2026-10-30）、公開 PoC なし | 確認済み | — 対象なし |
| [CVE-2026-118527](CVE-2026-118527) | Ivanti Connect Secure | 3.1 4.3 (Ivanti) | Ivanti Connect Secure 25.1.1.2 and prior; 25.1.2.2 and prior; 22.8R2.5 and prior | 25.1.1.3 / 22.8R2.6 | Ivanti Connect Secure の予測可能なファイル名による既知の場所へのファイルアップロード；実利用確認済み（KEV 2026-10-30）、公開 PoC なし | 確認済み | — 対象なし |
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
| [CVE-2026-83548](CVE-2026-83548) | SonicWall SMA1000 | 3.1 10.0 (NVD) | SMA1000 6210 / 7210 / 8200v: 12.4.3-03453 and older, 12.5.0-02835 and older | 12.4.3-03526 and higher, 12.5.0-02952 and higher (platform-hotfix) | 未認証 SSRF→CouchDB RCE→root の一式ツール；ベンダーも実利用を確認、CISA KEV | 確認済み | — 対象なし |
| [CVE-2026-83549](CVE-2026-83549) | SonicWall SMA1000 | 3.1 7.8 (NVD) | SMA1000 6210 / 7210 / 8200v: 12.4.3-03453 and older, 12.5.0-02835 and older | 12.4.3-03526 and higher, 12.5.0-02952 and higher (platform-hotfix) | 認証後 AMC コマンドインジェクション→root；同一ツール、CISA KEV | 確認済み | — 対象なし |
| [CVE-2026-123633](CVE-2026-123633) | F5 NGINX HTTP/2 | 4.0 9.2 (F5)；3.1 8.1 (F5) | NGINX Open Source 1.19.7-1.30.6 and 1.31.0-1.31.8 with HTTP/2 proxying | 1.30.7 / 1.31.9 | UAF トリガー＋ret2libc RCE を主張するスクリプト、未検証 | 確認済み | 未実施 |
| [CVE-2026-110486](CVE-2026-110486) | Eclipse Mosquitto | 3.1 9.8 (NVD) | 2.1.0–2.1.2 (builtin WebSocket listener) | 2.1.3 | 空 WebSocket フレームによるパーサー非同期トリガー；RCE 未証明 | 確認済み | 未実施 |
| [CVE-2026-124040](CVE-2026-124040) | CivetWeb HTTP/2 | 4.0 9.2 (VulnCheck)；3.1 8.1 (VulnCheck) | CivetWeb through 1.16, built with USE_HTTP2 and enable_http2 | No fixed release listed (PoC repo ships fix-http2.patch) | HPACK ポイズニングでメソッド／パスをリテラルヘッダー ACL から隠蔽；RCE は作者の特権デモコールバック内のみ | 確認済み | 未実施 |
| [CVE-2026-116448](CVE-2026-116448) | Dell PowerStore SDNAS | 3.1 9.8 (GHSA) | Dell PowerStore OS <= 3.6.0.0 with SDNAS enabled (per PoC README; GHSA lists no version range) | PowerStore OS 4.0.0.1 (per PoC README) | SDNAS 診断 API の OS コマンドインジェクション；RCE スクリプトは主張のみ、未検証 | 確認済み | 未実施 |
| [CVE-2026-123634](CVE-2026-123634) | F5 NGINX リゾルバ (SSI) | 4.0 9.2 (F5)；3.1 8.1 (F5) | NGINX 0.6.18-1.31.8 (proxy with SSI subrequests) | 1.30.7 / 1.31.9 | リゾルバ UAF クラッシュ（Docker ラボ）；exploit スクリプト付き、未検証 | 確認済み | 未実施 |
| [CVE-2026-121810](CVE-2026-121810) | F5 NGINX HTTP/3 (QUIC) | 4.0 9.2 (F5)；3.1 8.1 (F5) | NGINX 1.25.0-1.31.8 (HTTP/3) | 1.30.7 / 1.31.9 | HTTP/3 QUIC UAF クラッシュ（Docker ラボ）；exploit スクリプト付き、未検証 | 確認済み | 未実施 |
| [CVE-2026-113425](CVE-2026-113425) | F5 NGINX メールプロキシ | 4.0 9.2 (F5)；3.1 8.1 (F5) | NGINX 0.5.33-1.31.8 (mail proxy) | 1.30.7 / 1.31.9 | メールプロキシ UAF クラッシュ（Docker ラボ）；exploit スクリプト付き、未検証 | 確認済み | 未実施 |
| [CVE-2026-118899](CVE-2026-118899) | F5 NGINX TLS 1.3 | 4.0 8.7 (F5)；3.1 7.5 (F5) | NGINX 1.13.0-1.31.8 (TLS 1.3, http block) | 1.30.7 / 1.31.9 | TLS 1.3 無限ループ DoS（Docker ラボ）；exploit スクリプト付き、未検証 | 確認済み | 未実施 |
| [CVE-2026-116442](CVE-2026-116442) | Dell PowerStore NDMP | 3.1 8.1 (GHSA) | Dell PowerStore OS <= 3.6.0.0 with NDMP enabled (per PoC README; GHSA lists no version range) | PowerStore OS 4.0.0.1 (per PoC README) | NDMP リプレイ認証バイパス；PoC は認証前 NDMP 応答のみ示す | 確認済み | 未実施 |
| [CVE-2026-114202](CVE-2026-114202) | ASUS Control Center Express | 4.0 10.0 (NVD) | ASUS Control Center Express all firmware versions prior to patch (PoC tested through v1.7.27) | no fixed version published | ハードコード JWT 秘密鍵による管理者トークン偽造；鍵は自前で抽出、未検証 | 確認済み | 未実施 |
| [CVE-2026-131852](CVE-2026-131852) | OwnTracks Recorder | 3.1 9.8 (GHSA) | OwnTracks Recorder before 1.0.5 | 1.0.5 | location tid による格納型フォーマット文字列；ポインタ漏洩と持続 DoS（ラボ）、未検証 | 確認済み | 未実施 |
| [CVE-2026-92182](CVE-2026-92182) | pfSense CE | 3.0 8.8 (GHSA) | pfSense CE ≤ 2.8.1 | pfSense CE 2.8.2 | 低権限アカウントが管理者専用 XMLRPC メソッドに到達；root RCE、未検証 | 確認済み | 未実施 |
| [CVE-2026-123640](CVE-2026-123640) | F5 NGINX ssl_preread | 3.1 5.3 (GHSA) | nginx 1.15.2–1.31.8 (ssl_preread) | 1.30.7 / 1.31.9 | ssl_preread SNI 検証不足；誤ルーティング/範囲外読み取り（Docker ラボ）、未検証 | 確認済み | 未実施 |
| [CVE-2026-120993](CVE-2026-120993) | F5 NGINX stream SSL | 3.1 5.3 (GHSA) | nginx 1.31.4–1.31.8 (stream SSL + PROXY v2) | 1.31.9 | PROXY v2 + 動的証明書の NULL デリファレンス；ワーカー crash（Docker ラボ）、未検証 | 確認済み | 未実施 |
| [CVE-2026-125283](CVE-2026-125283) | F5 NGINX alias/try_files | 3.1 5.3 (GHSA) | nginx 0.9.6–1.31.8 (alias + try_files) | 1.30.7 / 1.31.9 | alias + try_files 整数アンダーフロー；範囲外読み取り（Docker ラボ）、未検証 | 確認済み | 未実施 |
| [CVE-2026-120967](CVE-2026-120967) | F5 NGINX stream SNI | 3.1 4.8 (GHSA) | nginx 1.25.5–1.31.8 (stream SNI mTLS) | 1.30.7 / 1.31.9 | stream SNI mTLS チェックが遅すぎる；保護バックエンドへ回避（ラボ）、未検証 | 確認済み | 未実施 |
| [CVE-2026-129358](CVE-2026-129358) | Magma NMS | 4.0 1.9 (VulDB) | Magma NMS up to 1.9.0 | none (unfixed upstream) | 組織名がインライン CONFIG スクリプトにエスケープ無しで描画される格納型 XSS | 確認済み | 未実施 |
| [CVE-2026-129351](CVE-2026-129351) | TRENDnet TEW-657BRM | 4.0 10.0 (VulDB) | TEW-657BRM v1.0R firmware 1.00.1 | none (EOL, no vendor fix) | 未認証の長い .htm パスで sprintf が GOT を破壊；EOL、ベンダー修正なし | 確認済み | 未実施 |
| [CVE-2026-129353](CVE-2026-129353) | D-Link DIR-600L | 4.0 10.0 (VulDB) | DIR-600L B1 firmware 2.17, 2.17b02 | none (EOL, no vendor fix) | 未認証で id/password の無制限 strcpy によるスタックオーバーフロー；EOL、ベンダー修正なし | 確認済み | 未実施 |
| [CVE-2026-129354](CVE-2026-129354) | D-Link DIR-600L | 4.0 10.0 (VulDB) | DIR-600L B1 firmware 2.17b02 | none (EOL, no vendor fix) | 未認証で SOAPAction ヘッダーによる HNAP hnap_main のスタックオーバーフロー；EOL、ベンダー修正なし | 確認済み | 未実施 |
| [CVE-2026-110697](CVE-2026-110697) | Quay | 3.1 9.9 (Red Hat) | Quay < 3.9.28; 3.10 < 3.10.28; 3.12 < 3.12.24; 3.14 < 3.14.10; 3.15 < 3.15.9; 3.16 < 3.16.7; 3.17 < 3.17.7; 3.18 < 3.18.3 | 3.9.28 / 3.10.28 / 3.12.24 / 3.14.10 / 3.15.9 / 3.16.7 / 3.17.7 / 3.18.3 | ロボット一覧の SQL LIKE ワイルドカード注入で他テナントのロボットトークンが漏洩；各ブランチの修正版で対応 | 確認済み | 未実施 |
| [CVE-2026-126147](CVE-2026-126147) | FortiMail | 3.1 9.8 (Fortinet) | FortiMail 8.0.0–8.0.1, 7.6.0–7.6.6, 7.4.0–7.4.8, 7.2.0–7.2.9 | 8.0.2 / 7.6.7 / 7.4.9; migrate off 7.2 | 管理インターフェースのパストラバーサルで任意ファイル書き込みからコマンド実行；8.0.2/7.6.7/7.4.9 で修正 | 確認済み | 未実施 |
| [CVE-2026-126148](CVE-2026-126148) | FortiMail | 3.1 9.8 (Fortinet) | FortiMail 8.0.0–8.0.1, 7.6.0–7.6.6 | 8.0.2 / 7.6.7 | HA 参加要求の hostname/peer-ip 経由で OS コマンドインジェクション；8.0.2/7.6.7 で修正 | 確認済み | 未実施 |
| [CVE-2026-129352](CVE-2026-129352) | TRENDnet TEW-657BRM | 4.0 9.4 (VulDB) | TEW-657BRM v1.0R firmware 1.00.1 | none (EOL, no vendor fix) | 認証済みで multipart 先頭行の無制限 strncpy によるスタックオーバーフロー；EOL、ベンダー修正なし | 確認済み | 未実施 |
| [CVE-2026-114550](CVE-2026-114550) | libwebsockets | 3.0 8.1 (GHSA) | libwebsockets v4.2–v4.5.8 (MQTT client role) | 5.0.0 | MQTT PUBACK の範囲外書き込みでリストと関数ポインタを書き換え；ラボ証拠あり、未検証 | 確認済み | 未実施 |
| [CVE-2026-129355](CVE-2026-129355) | dufs | 4.0 6.9 (VulnDB); 3.1 6.5 (VulnDB) | dufs 0.1.0–0.46.0 | 0.47.0 | WebDAV COPY が削除権限なしに既存ファイルを上書き；ラボ証拠あり | 確認済み | 未実施 |
| [CVE-2026-129359](CVE-2026-129359) | Magma orc8r | 4.0 5.5 (VulnDB); 3.1 7.3 (VulnDB) | Magma <= 1.9.0 | no upstream fix (synthetic remediation in lab) | ハードコードされたサービス間認証情報で任意の gRPC 呼び出し元が信頼される；ラボ証拠あり | 確認済み | 未実施 |
| [CVE-2026-129360](CVE-2026-129360) | Magma orc8r | 4.0 6.9 (VulnDB); 3.1 7.3 (VulnDB) | Magma <= 1.9.0 | no upstream fix (synthetic remediation in lab) | オペレーター身份が偽装可能な証明書シリアルヘッダーに従う；ラボ証拠あり | 確認済み | 未実施 |
| [CVE-2026-76466](CVE-2026-76466) | Cisco Expressway | 3.1 9.8 (Cisco) | Expressway-C / Expressway-E clustered, X15.5.3 and earlier (X14 and earlier too) | X15.5.20 | クラスタ Expressway のハードコード Erlang クッキーによる未認証 root RCE；ラボ検証済み、F6 が実利用を確認 | 確認済み | — 対象なし |
| [CVE-2026-13249](CVE-2026-13249) | Honeywell PD45 プリンタ | 3.1 9.8 (Honeywell) | Honeywell PD45 firmware >= F10.19.010040 and < F10.22.030745 | F10.22.030745 | プリンタ Web 管理で未認証の任意ファイルアップロード；正確なアップロード URI は未公開、運用者の URL 指定が必要、未検証 | 確認済み | 未実施 |
| [CVE-2026-13768](CVE-2026-13768) | Gardyn スマートガーデン | 4.0 9.5 (ICS-CERT); 3.1 10.0 (ICS-CERT) | Gardyn Home Kit and Studio devices (exposed iothubowner key) | Cloud-side fix deployed (2026-07); devices auto-update firmware when connected | 漏洩した IoT Hub オーナーキーで全艦隊を列挙し upgrade() コマンドインジェクションで RCE；クラウド側で修正済み、未検証 | 確認済み | 未実施 |
| [CVE-2026-116440](CVE-2026-116440) | PowerStore SDNAS | 3.1 9.8 (Dell) | Dell PowerStore SDNAS versions before 5.1.0.0-2798105 | 5.1.0.0-2798105 (DSA-2026-479) | SDNAS の未認証リモートバッファオーバーフロー；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-132622](CVE-2026-132622) | GearUP Hyperev | 4.0 9.4 (VulDB); 3.1 9.1 (VulDB) | GearUP Hyperev up to 20261020 |  | WLAN スキャンのコマンドインジェクション（遅延検出）、未検証 | 確認済み | 未実施 |
| [CVE-2026-133185](CVE-2026-133185) | goproxy | 4.0 9.1 (VulnCheck); 3.1 7.4 (VulnCheck) | elazarl/goproxy before 1.9.4 | 1.9.4 | math/rand シード予測による TLS リーフ秘密鍵の漏洩、未検証 | 確認済み | 未実施 |
| [CVE-2026-116443](CVE-2026-116443) | PowerStore SDNAS | 3.1 9.8 (Dell) | Dell PowerStore SDNAS versions before 5.1.0.0-2798105 | 5.1.0.0-2798105 (DSA-2026-479) | NAS TFTP サービスのスタックバッファオーバーフロー；クラッシュ検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-116446](CVE-2026-116446) | PowerStore SDNAS | 3.1 9.8 (Dell) | Dell PowerStore SDNAS versions before 5.1.0.0-2798105 | 5.1.0.0-2798105 (DSA-2026-479) | NAS NFS サービスの範囲外メモリアクセス；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-116449](CVE-2026-116449) | PowerStore SDNAS | 3.1 9.8 (Dell) | Dell PowerStore SDNAS versions before 5.1.0.0-2798105 | 5.1.0.0-2798105 (DSA-2026-479) | SDNAS の OS コマンドインジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-116441](CVE-2026-116441) | PowerStore SDNAS | 3.1 9.6 (Dell) | Dell PowerStore SDNAS versions before 5.1.0.0-2798105 | 5.1.0.0-2798105 (DSA-2026-479) | ストレージプロセッサ相互接続ドライバの範囲外書き込み；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-111505](CVE-2026-111505) | OpenManage Enterprise | 3.1 8.8 (Dell) | Dell OpenManage Enterprise versions prior to 4.8.0 | 4.8.0 (DSA-2026-467) | OpenManage Enterprise の OS コマンドインジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-111506](CVE-2026-111506) | PowerStore | 3.1 8.8 (Dell) | Dell PowerStoreT OS 5.1.x versions prior to 5.1.0.0-2798105 | 5.1.0.0-2798105 or later (DSA-2026-479) | PowerStore の認証欠如；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-111545](CVE-2026-111545) | PowerStore | 3.1 8.8 (Dell) | Dell PowerStoreT OS 5.1.x versions prior to 5.1.0.0-2798105 | 5.1.0.0-2798105 or later (DSA-2026-479) | PowerStore の SQL インジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-133323](CVE-2026-133323) | MiCollab | 3.1 10.0 (Mitel) | MiCollab 10.3 (10.3.0.18) and earlier | Patch for 10.3 (10.3.0.18) (MISA-2026-0012) | MiCollab AWV のブラインドコマンドインジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-133303](CVE-2026-133303) | MiCollab | 3.1 9.0 (Mitel) | MiCollab 10.3 (10.3.0.18) and earlier | Patch for 10.3 (10.3.0.18) (MISA-2026-0012) | MiCollab AWV の XML インジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-133310](CVE-2026-133310) | Wing FTP Server | 4.0 9.2 (VulnCheck); 3.1 8.1 (VulnCheck) | Wing FTP Server before 8.2.8 | 8.2.8 | Wing FTP Server の NUL バイトファイルマスク回避；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-116447](CVE-2026-116447) | PowerStore SDNAS | 3.1 8.8 (Dell) | Dell PowerStore SDNAS versions before 5.1.0.0-2798105 | 5.1.0.0-2798105 (DSA-2026-479) | PowerStore SDNAS のローカル権限昇格；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-116411](CVE-2026-116411) | PowerStore | 3.1 8.8 (Dell) | Dell PowerStore SDNAS versions before 5.1.0.0-2798105 | 5.1.0.0-2798105 (DSA-2026-479) | PowerStore のサーバサイドリクエストフォージェリ；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-76460](CVE-2026-76460) | Identity Services Engine | 3.1 10.0 (Cisco) | Cisco ISE 3.1-3.5 and ISE-PIC 3.4-3.5 | 3.1 Patch 12 / 3.2 Patch 11 / 3.3 Patch 12 / 3.4 Patch 7 / 3.5 Patch 4 (2026-09-16) | Cisco ISE API の認証バイパス；検出型 PoC、未検証 | 確認済み | ◐ 部分 |
| [CVE-2026-84295](CVE-2026-84295) | WS_FTP Server | 3.1 10.0 (Progress) | Progress WS_FTP Server before 2024.0.6 / 2025.0.3 | 2024.0.6 / 2025.0.3 | WS_FTP Server の認証欠如；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-77537](CVE-2026-77537) | UniFi Protect | 3.1 10.0 (UI) | UniFi Protect Application before 7.2.105 | 7.2.105 | UniFi Protect のコマンドインジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-95787](CVE-2026-95787) | ArubaOS (AOS-10) | 3.1 10.0 (HPE) | ArubaOS AOS-10 10.8.1.1 and below, 10.7.2.6 and below, 10.4.1.13 and below | 10.8.1.2 / 10.7.2.7 / 10.4.1.14 and above (HPE SBNW05162) | ArubaOS PAPI プロトコルの認証バイパス；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-111507](CVE-2026-111507) | PowerStore | 3.1 8.1 (Dell) | Dell PowerStore versions before 5.1.0.0-2798105 | 5.1.0.0-2798105 (DSA-2026-479) | Dell PowerStore の認可バイパス；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-111547](CVE-2026-111547) | PowerStore | 3.1 8.1 (Dell) | Dell PowerStore versions before 5.1.0.0-2798105 | 5.1.0.0-2798105 (DSA-2026-479) | Dell PowerStore の境界外読み取り；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-116417](CVE-2026-116417) | PowerScale InsightIQ | 3.1 8.1 (Dell) | Dell PowerScale InsightIQ 6.3.0-6.4.0 | 6.4.1 (DSA-2026-480) | Dell PowerScale InsightIQ の弱いパスワード要件；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-15409](CVE-2026-15409) | SMA1000 | 3.1 10.0 (SonicWall) | SonicWall SMA1000 12.4.3-03245/03387/03434, 12.5.0-02283/02624/02800 (platform-hotfix) and earlier | 12.4.3-03453 / 12.5.0-02835 and higher (SNWLID-2026-0008) | SonicWall SMA1000 の認証前 SSRF；検出型 PoC、未検証 | 確認済み | ◐ 部分 |
| [CVE-2026-109469](CVE-2026-109469) | Entra Device Registration | 3.1 10.0 (Microsoft) | Microsoft Entra Device Registration (hosted service) | Official fix available (Microsoft service-side remediation, MSRC 2026-11-05) | Entra デバイス登録のユーザー制御キーによる認可バイパス；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-102255](CVE-2026-102255) | SMA1000 | 3.1 10.0 (SonicWall) | SonicWall SMA1000 12.4.3-03526 and older, 12.5.0-02952 and older (platform-hotfix) | 12.4.3-03670 / 12.5.0-03082 and higher (SNWLID-2026-0017) | SonicWall SMA1000 の認証前 SSRF（意図しないフォワードプロキシ経由）；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-77550](CVE-2026-77550) | UniFi OS Server | 3.1 10.0 (UI) | UniFi OS Server 5.1.21 and earlier; UniFi OS devices 5.1.26 and earlier; Express 4.0.16 and earlier | UniFi OS Server 5.1.37+; devices 5.1.31+; NAS 5.1.32+; Express 4.0.17+ (Bulletin 067) | UniFi OS Server の CRLF インジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-77554](CVE-2026-77554) | UniFi Talk Application | 3.1 10.0 (UI) | UniFi Talk Application 5.2.7 and earlier | 5.3.2 or later (Bulletin 067) | UniFi Talk アプリケーションのコマンドインジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-84236](CVE-2026-84236) | Guardium Data Protection | 3.1 9.8 (IBM) | IBM Guardium Data Protection 12.2 | 12.2.4 | IBM Guardium Data Protection のデシリアライゼーションによる RCE；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-87977](CVE-2026-87977) | Guardium Data Protection | 3.1 9.8 (IBM) | IBM Guardium Data Protection 12.2 | 12.2.4 | IBM Guardium Data Protection の SQL インジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-76536](CVE-2026-76536) | Splunk Enterprise | 3.1 9.4 (Splunk) | Splunk Enterprise 10.4-10.4.4, 10.2-10.2.8, 10.0-10.0.11, 9.4-9.4.16 | 10.4.5 / 10.2.9 / 10.0.12 / 9.4.17 (SVD-2026-1103) | Splunk Enterprise のクラスタ構成 REST API 経由の認証バイパス；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-76535](CVE-2026-76535) | Splunk Enterprise | 3.1 9.1 (Splunk) | Splunk Enterprise 10.6.0.5, 10.4-10.4.4, 10.2-10.2.8, 10.0-10.0.11, 9.4-9.4.16 | 10.6.1 / 10.4.5 / 10.2.9 / 10.0.12 / 9.4.17 (SVD-2026-1103) | Splunk Enterprise の RapidDiag REST API 経由の認証バイパス；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-82339](CVE-2026-82339) | Guardium Data Protection | 3.1 9.1 (IBM) | IBM Guardium Data Protection 12.2 | 12.2.4 | IBM Guardium Data Protection の SharePoint S-TAP RelayService における認証欠如；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-76538](CVE-2026-76538) | Splunk Enterprise | 3.1 8.8 (Splunk) | Splunk Enterprise 10.4-10.4.4, 10.2-10.2.8, 10.0-10.0.11, 9.4-9.4.15 | 10.4.5 / 10.2.9 / 10.0.12 / 9.4.16 (SVD-2026-1103) | Splunk Enterprise のデータモデルアクセラレーション経由の REST API からの SPL インジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-76540](CVE-2026-76540) | Splunk Enterprise | 3.1 8.8 (Splunk) | Splunk Enterprise 10.4-10.4.4, 10.2-10.2.8, 10.0-10.0.11, 9.4-9.4.16 | 10.4.5 / 10.2.9 / 10.0.12 / 9.4.17 (SVD-2026-1103) | Splunk Enterprise の REST API 経由の不適切な認可；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-84273](CVE-2026-84273) | Guardium Data Protection | 3.1 8.1 (IBM) | IBM Guardium Data Protection 12.2 | 12.2.4 | IBM Guardium Data Protection のデータソース機能におけるパストラバーサル；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-85018](CVE-2026-85018) | Guardium Data Protection | 3.1 8.1 (IBM) | IBM Guardium Data Protection 12.2 | 12.2.4 | IBM Guardium Data Protection の GDP Terraform プロバイダにおける不適切な TLS 証明書検証；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-82342](CVE-2026-82342) | Guardium Data Protection | 3.1 8.1 (IBM) | IBM Guardium Data Protection 12.2 | 12.2.4 | IBM Guardium Data Protection の PROXY プロトコル v1 ヘッダ経由のスタックベースバッファオーバーフロー；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-76544](CVE-2026-76544) | Splunk Enterprise | 3.1 8.1 (Splunk) | Splunk Enterprise 10.4-10.4.4, 10.2-10.2.8, 10.0-10.0.11, 9.4-9.4.15 | 10.4.5 / 10.2.9 / 10.0.12 / 9.4.16 (SVD-2026-1103) | Splunk Enterprise のメトリックアラートフィルタ経由の SPL インジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-132808](CVE-2026-132808) | UniFi Access Application | 3.1 9.9 (Ubiquiti) | UniFi Access Application <4.3.24 | 4.3.24 | UniFi Access の認可不備により管理下デバイスでコマンド実行；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-132804](CVE-2026-132804) | UniFi Access Application | 3.1 9.9 (Ubiquiti) | UniFi Access Application <4.3.24 | 4.3.24 | UniFi Access の SSRF により UniFi OS 内で権限昇格；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-132803](CVE-2026-132803) | UniFi Access Application | 3.1 9.9 (Ubiquiti) | UniFi Access Application <4.3.24 | 4.3.24 | UniFi Access の認証後 SQL インジェクションにより権限昇格；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-132802](CVE-2026-132802) | UniFi Access Application | 3.1 9.9 (Ubiquiti) | UniFi Access Application <4.3.24 | 4.3.24 | UniFi Access のリンク解決不備により root としてコード実行；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-132139](CVE-2026-132139) | DrayTek Vigor2960 | 4.0 9.4 (VulDB); 3.1 9.9 (VulDB) | Vigor2960 1.5.1.0-1.5.1.6 | 1.5.1.7 | DrayTek Vigor2960 setSWMProfile のスタックバッファオーバーフロー；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-121805](CVE-2026-121805) | F5 BIG-IP | 4.0 9.3 (F5); 3.1 9.8 (F5) | BIG-IP 21.1.0 / 17.5.x / 17.1.x with PEM::subscriber iRule | 21.1.0.4.0.19.3-ENG / 17.5.1.11.0.61.12-ENG / 17.1.3.7.0.21.4-ENG | BIG-IP PEM::subscriber iRule 処理のスタックバッファオーバーフロー；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-120722](CVE-2026-120722) | F5 BIG-IP | 4.0 9.3 (F5); 3.1 9.8 (F5) | BIG-IP 21.1.0 / 17.5.x / 17.1.x with DNS::scrape iRule | 21.1.0.4.0.19.3-ENG / 17.5.1.11.0.61.12-ENG / 17.1.3.7.0.21.4-ENG | BIG-IP DNS::scrape iRule 処理のスタックバッファオーバーフロー；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-120292](CVE-2026-120292) | F5 BIG-IP | 4.0 9.3 (F5); 3.1 9.8 (F5) | BIG-IP 21.1.0 / 17.5.0-17.5.1 / 17.1.0-17.1.3 with MR::message route iRule | 21.1.0.4.0.19.3-ENG / 17.5.1.11.0.61.12-ENG / 17.1.3.7.0.21.4-ENG | BIG-IP MR::message route iRule 処理のスタックバッファオーバーフロー；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-120285](CVE-2026-120285) | F5 BIG-IP | 4.0 9.3 (F5); 3.1 9.8 (F5) | BIG-IP 21.1.0 / 17.5.0-17.5.1 / 17.1.0-17.1.3 with PSC::ip_address iRule | 21.1.0.4.0.19.3-ENG / 17.5.1.11.0.61.12-ENG / 17.1.3.7.0.21.4-ENG | BIG-IP PSC::ip_address iRule 処理のスタックバッファオーバーフロー；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-116953](CVE-2026-116953) | F5 BIG-IP | 4.0 9.3 (F5); 3.1 9.8 (F5) | BIG-IP 21.1.0 / 17.5.0-17.5.1 / 17.1.0-17.1.3 with GENERICMESSAGE::route iRule | 21.1.0.4.0.19.3-ENG / 17.5.1.11.0.61.12-ENG / 17.1.3.7.0.21.4-ENG | BIG-IP GENERICMESSAGE::route iRule 処理のスタックバッファオーバーフロー；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-131287](CVE-2026-131287) | Splunk SOAR | 3.1 9.6 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 | Splunk SOAR のリポジトリ横断 playbook 参照による RCE；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-132142](CVE-2026-132142) | DrayTek Vigor2960 | 4.0 9.4 (VulDB); 3.1 9.1 (VulDB) | Vigor2960 1.5.1.0-1.5.1.6 | 1.5.1.7 | DrayTek Vigor2960 dataflowstatus のスタックバッファオーバーフロー；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-132143](CVE-2026-132143) | DrayTek Vigor2960 | 4.0 9.4 (VulDB); 3.1 9.9 (VulDB) | Vigor2960 1.5.1.0-1.5.1.6 | 1.5.1.7 | DrayTek Vigor2960 doWebBackup のスタックバッファオーバーフロー；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-132141](CVE-2026-132141) | DrayTek Vigor2960 | 4.0 9.4 (VulDB); 3.1 9.9 (VulDB) | Vigor2960 1.5.1.0-1.5.1.6 | 1.5.1.7 | DrayTek Vigor2960 jsonstatus のスタックバッファオーバーフロー；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-131253](CVE-2026-131253) | Splunk SOAR | 3.1 9.9 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 | Splunk SOAR App Wizard のコードインジェクションによる RCE；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-132807](CVE-2026-132807) | UniFi Access Application | 3.1 9 (Ubiquiti) | UniFi Access Application <4.3.24 | 4.3.24 | UniFi Access の不適切な証明書検証による機密情報漏洩と不正変更；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-123637](CVE-2026-123637) | BIG-IP | 4.0 9.3 (F5); 3.1 9.8 (F5) | BIG-IP APM 21.1.0 / 17.5.0-17.5.1 / 17.1.0-17.1.3 | 工程热修复 BIGIP-21.1.0.4.0.19.3-ENG3 / BIGIP-17.5.1.11.0.61.12-ENG3 / BIGIP-17.1.3.7.0.21.4-ENG3（F5 K000163937） | F5 BIG-IP APM のスタックバッファオーバーフローによる TMM クラッシュと RCE；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-104099](CVE-2026-104099) | Fabio | 3.1 9.1 (GHSA) | Fabio <1.7.3 | 1.7.3 | Fabio の正規化されていないパスによるアクセス制御バイパス；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-131202](CVE-2026-131202) | Splunk Enterprise Security | 3.1 9.1 (Splunk) | Splunk Enterprise Security <8.7.0 | 8.7.0 | Splunk Enterprise Security の REST API パストラバーサルによる RCE；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-131199](CVE-2026-131199) | Splunk Enterprise Security | 3.1 8.8 (Splunk) | Splunk Enterprise Security <8.7.0 | 8.7.0 | Splunk ES の任意 SPL コマンド実行；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-131236](CVE-2026-131236) | Splunk Enterprise Security | 3.1 8.8 (Splunk) | Splunk Enterprise Security <8.7.0 | 8.7.0 | Splunk ES の格納型 SPL インジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-131246](CVE-2026-131246) | Splunk SOAR | 3.1 8.8 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 | Splunk SOAR の承認バイパスによる外部プロンプト漏洩；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-131252](CVE-2026-131252) | Splunk SOAR | 3.1 8.8 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 | Splunk SOAR のテナント横断資産改ざん；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-131261](CVE-2026-131261) | Splunk SOAR | 3.1 8.8 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 | Splunk SOAR の悪意あるアプリのインストールによる任意コード実行；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-131263](CVE-2026-131263) | Splunk SOAR | 3.1 8.8 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 | Splunk SOAR のコネクタアプリによる任意ファイル書き込みからの RCE；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-131269](CVE-2026-131269) | Splunk SOAR | 3.1 8.8 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 | Splunk SOAR のアプリ検証による任意コード実行；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-131270](CVE-2026-131270) | Splunk SOAR | 3.1 8.8 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 | Splunk SOAR のリポジトリパストラバーサルによる任意ファイル書き込み；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-131271](CVE-2026-131271) | Splunk SOAR | 3.1 8.8 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 | Splunk SOAR のスラッシュコマンドによる権限外の認証情報漏洩；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-131295](CVE-2026-131295) | Splunk SOAR | 3.1 8.8 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 | Splunk SOAR の権限外子プレイブック実行；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-131258](CVE-2026-131258) | Splunk SOAR | 3.1 8.7 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 | Splunk SOAR のノート格納型 XSS；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-131260](CVE-2026-131260) | Splunk SOAR | 3.1 8.7 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 | Splunk SOAR のコンテナ取り込みによる格納型 XSS；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-131203](CVE-2026-131203) | Splunk Enterprise Security | 3.1 8.3 (Splunk) | Splunk Enterprise Security <8.7.0 | 8.7.0 | Splunk ES のリスク除外マクロ改ざんによる SPL 実行；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-131209](CVE-2026-131209) | Splunk Enterprise Security | 3.1 8.3 (Splunk) | Splunk Enterprise Security <8.7.0 | 8.7.0 | Splunk ES の UEBA エンティティリスクスコアによる SPL インジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-131215](CVE-2026-131215) | Splunk Enterprise Security | 3.1 8.3 (Splunk) | Splunk Enterprise Security <8.7.0 | 8.7.0 | Splunk ES の UEBA 検出除外ルールによる SPL インジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-131218](CVE-2026-131218) | Splunk Enterprise Security | 3.1 8.3 (Splunk) | Splunk Enterprise Security <8.7.0 | 8.7.0 | Splunk ES の Mission Control ダッシュボードにおける SPL インジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-131293](CVE-2026-131293) | Splunk SOAR | 3.1 8.3 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 | Splunk SOAR のプレイブック実行データの権限外読み書き；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-104129](CVE-2026-104129) | pREST | 3.1 8.1 (GHSA) | pREST <2.4.0 | 2.4.0 | pREST の _groupby パラメータによる SQL インジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-123891](CVE-2026-123891) | SDDC Manager | 3.1 8.1 (VMware) | SDDC Manager 9.1.x.x / 9.0.x.x / 5.x | 9.1.1.0200 / 9.0.2.0100 / 5.2.5 | SDDC Manager の SQL インジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-131200](CVE-2026-131200) | Splunk Enterprise Security | 3.1 8.1 (Splunk) | Splunk Enterprise Security <8.7.0 | 8.7.0 | Splunk ES の脅威インテリジェンス検索生成による SPL 実行；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-131210](CVE-2026-131210) | Splunk Enterprise Security | 3.1 8.1 (Splunk) | Splunk Enterprise Security <8.7.0 | 8.7.0 | Splunk ES の UEBA 検出除外ルックアップによる SPL インジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-131282](CVE-2026-131282) | Splunk SOAR | 3.1 8.1 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 | Splunk SOAR の診断ログバンドルからのパスワードリセット認証情報の漏洩；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-131297](CVE-2026-131297) | Splunk SOAR | 3.1 8.1 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 | Splunk SOAR の IdP バインド欠如による他プロバイダーのユーザーとしての認証；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-133493](CVE-2026-133493) | DIR-600L | 4.0 9.3 (VulDB); 3.1 10.0 (VulDB) | D-Link DIR-600L 2.17b02 | No fixed firmware confirmed | D-Link DIR-600L の gena.cgi による OS コマンドインジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-20320](CVE-2026-20320) | Cisco BroadWorks | 3.1 7.5 (Cisco) | BroadWorks earlier than RI.2026.07 | RI.2026.07 | Cisco BroadWorks OCI パーサの未認証 XXE；実利用確認済み（KEV 2026-11-10）、公開 PoC なし | 確認済み | 未実施 |
| [CVE-2026-111793](CVE-2026-111793) | Openwave Webtop Media Transcoder | 3.1 4.3 (MITRE) | Webtop Media Transcoder < 1.1.22.0 | 1.1.22.0 | Openwave Webtop Media Transcoder のファイル種別制限バイパス；実利用確認済み（KEV 2026-11-10）、公開 PoC なし | 確認済み | 未実施 |
| [CVE-2026-126262](CVE-2026-126262) | FortiAnalyzer / FortiManager | 3.1 9.8 (Fortinet) | FortiAnalyzer 8.0.0-8.0.1 / 7.6.0-7.6.7 / 7.4.0-7.4.11 / 7.2.0-7.2.12; FortiManager (FA features) 8.0.0 / 7.6.0-7.6.7 / 7.4.0-7.4.11 / 7.2.0-7.2.12 | FortiAnalyzer 8.0.2 / FortiManager 8.0.1 / 7.6.8 / 7.4.12 / 7.2.13 | FortiAnalyzer／FortiManager の OFTP サービスにおける SQL インジェクション；バージョン確認ツールのみ、未検証 | 確認済み | 未実施 |
| [CVE-2026-126261](CVE-2026-126261) | FortiManager | 3.1 9.8 (Fortinet) | FortiManager 8.0.0 / 7.6.0-7.6.7 / 7.4.0-7.4.5 / 7.2.0-7.2.8 | 8.0.1 / 7.6.8 / 7.4.6 / 7.2.9 | FortiManager FGFM サービスにおける登録パスワード検証前の不適切な認可；バージョン確認ツールのみ、未検証 | 確認済み | 未実施 |
| [CVE-2026-126259](CVE-2026-126259) | FortiOS | 3.1 9.8 (Fortinet) | FortiOS 8.0.0 / 7.6.0-7.6.7 / 7.4.0-7.4.12 / 7.2.0-7.2.13 / 7.0 all | 8.0.1 / 7.6.8 / 7.4.13 / 7.2.14 (7.0 migrate) | FortiOS 高可用クラスタにおける認証の欠如；バージョン確認ツールのみ、未検証 | 確認済み | 未実施 |
| [CVE-2026-126254](CVE-2026-126254) | FortiOS / FortiSASE | 3.1 9.6 (Fortinet) | FortiOS 8.0.0-8.0.1 / 7.6.0-7.6.7 / 7.4.0-7.4.12 / 7.2.0-7.2.13; FortiSASE 26.3.1, 26.2/26.1/25.x | 8.0.2 / 7.6.8 / 7.4.13 / 7.2.14; FortiSASE 26.3.2 (26.2 and earlier migrate) | FortiOS／FortiSASE BGP デーモンにおける数値切り捨て；バージョン確認ツールのみ、未検証 | 確認済み | 未実施 |
| [CVE-2026-126253](CVE-2026-126253) | FortiOS / FortiSASE | 3.1 9.3 (Fortinet) | FortiOS 8.0.0-8.0.1 / 7.6.0-7.6.7 / 7.4.0-7.4.12 / 7.2.0-7.2.13 / 7.0.1-7.0.19; FortiSASE 26.3.1, 26.2/26.1/25.x | 8.0.2 / 7.6.8 / 7.4.13 / 7.2.14; FortiSASE 26.3.2 (26.2 and earlier, 7.0 migrate) | FortiOS／FortiSASE OSPF デーモンにおける認証バイパス；バージョン確認ツールのみ、未検証 | 確認済み | 未実施 |
| [CVE-2026-126229](CVE-2026-126229) | FortiManager / FortiAnalyzer | 3.1 9.1 (Fortinet) | FortiManager / FortiAnalyzer 8.0.0-8.0.1 / 7.6.0-7.6.7 / 7.4.0-7.4.11 / 7.2.0-7.2.12 / 7.0 all | 8.0.2 / 7.6.8 / 7.4.12 / 7.2.13 (7.0 migrate) | FortiManager／FortiAnalyzer dmserver におけるユーザー制御キーによる認可バイパス；バージョン確認ツールのみ、未検証 | 確認済み | 未実施 |
| [CVE-2026-126260](CVE-2026-126260) | FortiAnalyzer / FortiManager | 3.1 9.0 (Fortinet) | FortiAnalyzer / FortiManager 8.0.0 / 7.6.0-7.6.7 / 7.4.0-7.4.11 (7.2 not affected) | 8.0.1 / 7.6.8 / 7.4.12 | FortiAnalyzer／FortiManager の OFTP サービスにおけるサーバーサイドリクエストフォージェリ；バージョン確認ツールのみ、未検証 | 確認済み | 未実施 |
| [CVE-2026-133993](CVE-2026-133993) | D-Link DIR-600L | 4.0 9.3 (NVD); 3.1 10.0 (NVD) | 2.17b02 |  | gena.cgi GENA ハンドラの service 引数によるスタックバッファオーバーフロー；検出型 PoC のみ | 確認済み | 未実施 |

### ランタイム / フレームワーク / ブラウザ (79)

| ID | 製品 | スコア | 影響バージョン | 修正バージョン | 評価 | CVE ステータス | 再現 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [CVE-2026-57898](CVE-2026-57898) | Eclipse BaSyx Java Server SDK | 3.1 9.0 (Eclipse) | Eclipse BaSyx Java Server SDK 2.0.0-milestone-05–2.0.0-milestone-12 (MongoDB backend) | 2.0.0-milestone-13 | Eclipse BaSyx AAS サムネイル API の未認証任意ファイル書き込み（MongoDB バックエンド）；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-114938](CVE-2026-114938) | OpenJDK Base64 (Java4Shell) | 4.0 9.2 (Calif)；3.1 8.1 (Oracle)；3.1 9.8 (Red Hat) | OpenJDK 17.0.6 and later on x86-64 with AVX-512 VBMI (17/21/25/27 lines; Oracle also lists Java 8 Performance Pack 8u511b33-perf) | vendor November 2026 CPU / OpenJDK 17.0.21.1, 21.0.13.1 and equivalent distributor builds | トリガー / クラッシュ / リーク / 実験；公開された汎用 RCE はない | 確認済み | ◐ 部分 |
| [CVE-2026-90436](CVE-2026-90436) | Apache Axis 1.x | 3.1 9.8 (CISA-ADP) | Apache Axis 1.x through 1.4 | 无修复版本（EOL；修复仅存于上游 commit 41f3b4e8） | 未認証クラス生成のラボ再現；デフォルト classpath での RCE は未実証 | 確認済み | ◐ 部分 |
| [CVE-2024-27834](CVE-2024-27834) | WebKit (Apple) | 3.1 5.5 (NVD) | Safari < 17.5；iOS/iPadOS < 16.7.8 及 17.x < 17.5；macOS < 14.5；tvOS < 17.5；watchOS < 10.5；WebKitGTK / WPE WebKit < 2.44.2 | Safari 17.5；iOS 16.7.8 / iOS 17.5；iPadOS 16.7.8 / iPadOS 17.5；macOS Sonoma 14.5；tvOS 17.5；watchOS 10.5 | 分析のみ；実行可能な PoC なし | 確認済み | — 対象なし |
| [CVE-2026-126187](CVE-2026-126187) | React Server Components / Next.js | 4.0 9.5 (GHSA) | react-server-dom-* 19.0.0–19.3.0; Next.js 16.0.0–16.4.0 (App Router + Cache Components) | react-server-dom-* 19.0.9 / 19.1.10 / 19.2.9 / 19.3.1; Next.js 16.4.1 | ラボ Docker アプリでの RCE；トリガーには稀な条件が必要 | 確認済み | ◐ 部分 |
| [CVE-2026-125350](CVE-2026-125350) | Google Chrome | 3.1 8.8 (NVD) | Chrome < 157.0.8103.50 | 157.0.8103.50 / .51 (Windows, macOS), 157.0.8103.50 (Linux, Android), Extended Stable 156.0.8078.96 | 回帰テストファイルによるレンダラークラッシュ；RCE ペイロードなし | 確認済み | ✅ 完全 |
| [CVE-2026-111497](CVE-2026-111497) | Node.js Brotli | 4.0 9.2 (Google)；3.1 9.8 (NVD) | Node.js < 22.23.4, < 24.22.1, < 26.12.1; Bun < 1.4.4; Brotli 1.0.3-1.2.0 | Node.js 22.23.4 / 24.22.1 / 26.12.1; Bun 1.4.4; Brotli 1.2.1 | 細工した Brotli ストリームによるリモート DoS を検証済み；RCE は分析のみ | 確認済み | ◐ 部分 |
| [CVE-2026-129349](CVE-2026-129349) | Apache Shiro DefaultLdapRealm | 4.0 9.1 (Apache) | Apache Shiro through 3.0.0 with DefaultLdapRealm/JndiLdapRealm and authenticationCachingEnabled=true (not the default) | 3.0.1 | 一度有効なログイン後の認証バイパス；キャッシュ有効時（非デフォルト）は任意のパスワードで認証 | 確認済み | ◐ 部分 |
| [CVE-2026-86829](CVE-2026-86829) | Apache Airflow コア | 3.1 8.8 (Apache) | apache-airflow-core < 3.4.0 | 3.4.0 (apache/airflow PR #72718) | DAG 作成者による XCom デシリアライズ経由のスケジューラ RCE；3.3.2 でラボ検証済み、3.4.0 ではクリーン | 確認済み | ◐ 部分 |
| [CVE-2026-115560](CVE-2026-115560) | PHP セッションアップロード進捗 | 4.0 9.2 (PHP) | PHP with session.serialize_handler=php_binary or php_serialize in server config, application switching to php at runtime via ini_set() before session_start(), and session.upload_progress.enabled=1 (PHP default). Validated on php:8.4.27-apache. | 8.5.13 / 8.4.28 / 8.3.37 / 8.2.36 (2026-11-19) | ラボでセッションハンドラ不一致による未認証 RCE（php:8.4.27-apache）；8.5.13/8.4.28/8.3.37/8.2.36 で修正、緩和策はアップロード進捗の無効化 | 確認済み | ◐ 部分 |
| [CVE-2026-75604](CVE-2026-75604) | Windows 上の Next.js | 3.1 9.0 (GHSA) | Next.js 13.4.0–15.5.23 and 16.0.0–16.3.2 on Windows, Pages Router + App Router without Cache Components | 15.5.24 / 16.3.3 | Server Actions 暗号化鍵の漏洩による未認証 RCE；Windows ホストと Pages/App Router が必要、ラボで next@16.2.11 を検証 | 確認済み | — 対象なし |
| [CVE-2026-115893](CVE-2026-115893) | Wasmtime | 3.1 9.9 (GHSA) | Wasmtime < 36.0.19, 37.0.0-42.x, 43.0.0-48.0.6, 49.0.0-49.0.3 (aarch64 Cranelift) | 36.0.19, 48.0.7, 49.0.4 | aarch64 JIT サンドボックス脱出からホストでのコード実行（ラボ）；49.0.3 で 5/5 成功、49.0.4 は拒否 | 確認済み | 未実施 |
| [CVE-2026-109618](CVE-2026-109618) | PHP | 3.1 9.8 (NVD)；4.0 9.2 (PHP) | PHP 5.4.0-8.5.11 | 8.2.35, 8.3.36, 8.4.27, 8.5.12 | 事前認証 RCE チェーン A/B/C を公開（D/E は有料）；PHP 5.4–8.5.11 でラボ検証；KEV 収載 | 確認済み | ◐ 部分 |
| [CVE-2026-109619](CVE-2026-109619) | PHP | 3.1 8.1 (NVD)；4.0 9.2 (PHP) | PHP 5.4.0-8.5.11 | 8.2.35, 8.3.36, 8.4.27, 8.5.12 | FPM ワーカーの跨リクエスト残留状態による UAF/情報漏洩 RCE（ラボ）；KEV 収載 | 確認済み | — 対象なし |
| [CVE-2026-126910](CVE-2026-126910) | Chrome V8 Maglev | 3.1 8.8 (NVD) | Chrome before 157.0.8103.78 | 157.0.8103.78 | ラボで型混乱 stale load を実証；RCE 未達、開発者フラグ要 | 確認済み | 未実施 |
| [CVE-2026-128134](CVE-2026-128134) | NLTK dot2img | 3.1 7.8 (GHSA) | NLTK before 3.10.4 | 3.10.4 | ローカル PATH ハイジャック実証；README の 7.3/3.9.2 は GHSA 7.8/3.10.4 と矛盾 | 確認済み | 未実施 |
| [CVE-2026-130001](CVE-2026-130001) | mustache (Ruby) | 3.1 9.8 (GHSA) | mustache gem <= 1.1.2 | 1.1.3 | テンプレートの無制限メソッド呼び出しによる RCE；スクリプトは主張のみ、未検証 | 確認済み | 未実施 |
| [CVE-2026-47884](CVE-2026-47884) | Spring Framework XsltView | 3.1 9.8 (GHSA) | Spring Framework 5.2.x–5.3.49, 6.0.x–6.0.30, 6.1.x–6.1.28, 6.2.x–6.2.19, 7.0.0–7.0.8 (XsltView + catch-all /** mapping + implicit view name) | 5.3.50 / 6.0.31 / 6.1.29 / 6.2.20 / 7.0.9 | 攻撃者指定ビュー名が XsltView で解決；SSRF と XSLT Java 拡張による RCE、未検証 | 確認済み | 未実施 |
| [CVE-2026-131842](CVE-2026-131842) | Poppler pdfdetach | 4.0 5.7 (VulnCheck) | Poppler pdfdetach 24.03.0–26.11.0 | none (upstream work item 1826 open) | pdfdetach のパストラバーサル、埋め込みファイルが出力先以外に書き出される | 確認済み | 未実施 |
| [CVE-2026-131873](CVE-2026-131873) | Gargoyle | 4.0 6.9 (VulnCheck) | Gargoyle 2023.1–2026.1.1 | Spatterlight 1.5.5 import (commit 45385f1) | Plus インタプリタ ReadAction() のスタックオーバーフロー、細工した .plus ファイルでクラッシュ | 確認済み | 未実施 |
| [CVE-2026-121265](CVE-2026-121265) | SQL::Abstract | 3.1 9.8 (GHSA) | SQL::Abstract < 2.000003 | 2.000003 | 配列の列値が insert/update/generate でリテラル SQL として扱われ未認証で注入；2.000003 で修正 | 確認済み | 未実施 |
| [CVE-2026-107360](CVE-2026-107360) | rubygem-safemode | 3.1 9.6 (Red Hat) | rubygem-safemode through 2.0.3; Red Hat Satellite 6.16–6.18 | upstream PR #75 (unmerged); rubygem-safemode 1.5.0-3.el8sat / 1.5.0-3.el9sat | 複合代入式で safemode Jail の許可リストを回避し任意の無引数メソッドを実行；上流の修正 PR は未マージ | 確認済み | 未実施 |
| [CVE-2026-128027](CVE-2026-128027) | FrankenPHP | 4.0 9.3 (VulnCheck) | FrankenPHP images built before 2026-02-04 (< 1.1.11) | 1.1.11 | 古いベースイメージ層が認証前 CMS スタックオーバーフローの libcrypto を同梱；1.1.11 で修正 | 確認済み | 未実施 |
| [CVE-2026-128014](CVE-2026-128014) | FrankenPHP | 4.0 9.2 (VulnCheck); 3.1 8.1 (GHSA) | FrankenPHP 1.13.1 (Brotli 1.2.0); all builds shipping Brotli < 1.2.1 | 1.13.2 (Brotli 1.2.1) | 同梱 Brotli 1.2.0 の無限デコードループ；未認証ワーカー DoS、ラボ証拠あり | 確認済み | 未実施 |
| [CVE-2026-123753](CVE-2026-123753) | Apache Axis2/Java | 3.1 9.1 (GHSA) | Apache Axis2/Java < 2.0.2 (PoC tested 2.0.1) | 2.0.2 | WS-Addressing ReplyTo/FaultTo SSRF、SOAP レスポンス全体の漏洩；ラボ証拠あり | 確認済み | 未実施 |
| [CVE-2026-132825](CVE-2026-132825) | Ruby | 3.1 7.4 (MITRE) | Ruby < 3.3.14; 3.4.0-< 3.4.13; 4.0.0-< 4.0.10 | 3.3.14 / 3.4.13 / 4.0.10 | シングルバイトエンコーディングの大文字小文字変換でヒープ範囲外書き込み 1 バイト；ASAN クラッシュと glibc チャンク破損、ラボ証拠あり | 確認済み | 未実施 |
| [CVE-2026-133168](CVE-2026-133168) | DCMTK | 4.0 8.5 (VulnCheck); 3.1 7.8 (VulnCheck) | DCMTK 3.7.1 | 3.7.2 (patch pending; fix commit c22836c, no release tagged) | JPEG エンコーダの平面変換でのヒープバッファオーバーフロー、未検証 | 確認済み | 未実施 |
| [CVE-2026-133243](CVE-2026-133243) | node-soap | 4.0 8.8 (VulnCheck); 3.1 8.2 (VulnCheck) | node-soap before 1.14.1 | 1.14.1 | WSDL.xmlToObject のプロトタイプ汚染；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-71164](CVE-2026-71164) | Helidon | 3.1 9.8 (Oracle) | Helidon 3.0.0-3.2.17 (Imperative Web Server) | 3.2.18 (Oracle CSPU Aug 2026) | Helidon Imperative Web Server のリモートコード実行；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-133307](CVE-2026-133307) | ClassiCube | 4.0 8.7 (VulnCheck); 3.1 8.8 (VulnCheck) | ClassiCube before 1.4.0 | 1.4.0 | ClassiCube Png_Decode のヒープ範囲外書き込み；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-116499](CVE-2026-116499) | Qiskit SDK | 3.1 8.4 (IBM) | Qiskit SDK v1.4.2-v2.6.2 | 2.6.2 (IBM patched release) | Qiskit SDK QPY ロードのデシリアライゼーションによるリモートコード実行；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-133254](CVE-2026-133254) | IntelliJ IDEA | 3.1 8.3 (JetBrains) | IntelliJ IDEA before 2026.3, 2026.2.4 | 2026.3 / 2026.2.4 | IntelliJ IDEA Code Provenance プラグイン経由のコード実行；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-130886](CVE-2026-130886) | @fastify/reply-from | 3.1 8.2 (GHSA) | @fastify/reply-from 12.8.1-12.8.3 | 12.8.4 | @fastify/reply-from プロキシのパストラバーサル；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-92937](CVE-2026-92937) | vm2 | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | vm2 3.11.6 | 3.11.7 | vm2 のサンドボックスエスケープによるリモートコード実行；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-0881](CVE-2026-0881) | Firefox | 3.1 10.0 (Mozilla) | Firefox <147, Thunderbird <147 | Firefox 147 / Thunderbird 147 (MFSA2026-01) | Firefox メッセージングシステムのサンドボックスエスケープ；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-92940](CVE-2026-92940) | vm2 | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | vm2 3.11.3-3.11.6 | 3.11.7 | vm2 globalAgent によるホスト HTTPS 認証情報の漏洩；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-92941](CVE-2026-92941) | vm2 | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | vm2 3.11.3-<3.11.7 | 3.11.7 | vm2 の TLS トラストストア改ざん；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-92946](CVE-2026-92946) | vm2 | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | vm2 before 3.11.7 | 3.11.7 | vm2 require.external によるリモートコード実行；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-92947](CVE-2026-92947) | vm2 | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | vm2 before 3.11.7 | 3.11.7 | vm2 Buffer プール経由のメモリ漏洩；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-92955](CVE-2026-92955) | vm2 | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | vm2 before 3.11.8 | 3.11.8 | vm2 NodeVM のサンドボックスエスケープ；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-92956](CVE-2026-92956) | vm2 | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | vm2 3.10.1-3.11.6 | 3.11.7 | vm2 WebAssembly のサンドボックスエスケープ；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-92960](CVE-2026-92960) | vm2 | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | vm2 before 3.11.6 | 3.11.6 | vm2 os/dns によるプロセス全体の状態漏洩；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-92953](CVE-2026-92953) | vm2 | 3.1 10.0 (VulnCheck); 4.0 9.3 (VulnCheck) | vm2 3.11.0-3.11.7 | 3.11.8 | vm2 の TypedArray 経由のプロトタイプ汚染；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-92948](CVE-2026-92948) | vm2 | 3.1 9.9 (VulnCheck); 4.0 9.4 (VulnCheck) | vm2 3.9.6-3.11.6 | 3.11.7 | vm2 の node:test 経由のサンドボックスエスケープ；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-92951](CVE-2026-92951) | vm2 | 3.1 9.9 (VulnCheck); 4.0 9.4 (VulnCheck) | vm2 before 3.11.7 | 3.11.7 | vm2 のモジュール許可リストバイパス；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-92957](CVE-2026-92957) | vm2 | 3.1 9.9 (VulnCheck); 4.0 9.4 (VulnCheck) | vm2 through 3.11.6 | 3.11.7 | vm2 の node: プレフィックスによる NodeVM 組み込み拒否リストバイパス；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-92944](CVE-2026-92944) | vm2 | 3.1 9.8 (VulnCheck); 4.0 9.3 (VulnCheck) | vm2 3.10.2-3.11.6 | 3.11.7 | vm2 の Promise プロテクタ経由のサンドボックスエスケープ；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-128138](CVE-2026-128138) | NLTK | 3.1 9.8 (GitHub) | NLTK 3.10.3-<3.10.4 | 3.10.4 | NLTK java() の JVM/JAR サンドボックスバイパス；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-92950](CVE-2026-92950) | vm2 | 3.1 8.6 (VulnCheck); 4.0 9.3 (VulnCheck) | vm2 before 3.11.7 | 3.11.7 | vm2 の CLI require 経由のサンドボックスエスケープ；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-92954](CVE-2026-92954) | vm2 | 3.1 8.6 (VulnCheck); 4.0 9.2 (VulnCheck) | vm2 3.10.0-3.11.7 | 3.11.8 | vm2 のホスト Promise 経由のサービス拒否；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-92958](CVE-2026-92958) | vm2 | 3.1 8.5 (VulnCheck); 4.0 8.4 (VulnCheck) | vm2 through 3.11.6 | 3.11.7 | vm2 の fs/promises 経由の拒否リストバイパス；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-92943](CVE-2026-92943) | AWS IoT Device SDK for Python | 3.1 8.1 (AMZN); 4.0 9.2 (AMZN) | AWS IoT Device SDK for Python 1.5.3-1.6.0 | 1.6.1 | AWS IoT Device SDK for Python のホスト不一致を伴う証明書検証不備；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-130235](CVE-2026-130235) | Okta .NET SDK Abstractions | 3.1 8.7 (Okta) | Okta .NET SDK Abstractions 1.0.0-beta-4.0.7 | 4.0.8 | Okta .NET SDK Abstractions の不適切なリクエスト URL 検証（SSWS トークン漏洩）；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-130179](CVE-2026-130179) | Okta .NET SDK Abstractions | 3.1 8.5 (Okta) | Okta .NET SDK Abstractions 3.0.0-4.0.7 | 4.0.8 | Okta .NET SDK Abstractions の認証情報の上書き；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-61798](CVE-2026-61798) | netty-incubator-codec-ohttp | 3.1 8.1 (GitHub) | netty-incubator-codec-ohttp <0.0.23.Final | 0.0.23.Final | netty-incubator-codec-ohttp の toString() 経由の HPKE 秘密鍵漏洩；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-130234](CVE-2026-130234) | Okta Swift Management SDK | 3.1 8.0 (Okta) | Okta Swift Management SDK <0.1.1 | 0.1.1 | Okta Swift Management SDK のパスパラメータエンコーディング不備；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-130756](CVE-2026-130756) | pnpm exe | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | pnpm exe <10.34.8, 11.x <11.28.8 | 10.34.8 / 11.28.8 | pnpm exe が漏洩した eMudhra 中間 CA を信頼；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2019-25782](CVE-2019-25782) | ThinkPHP | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | ThinkPHP 5.0.0-5.0.23 | 5.0.24 | ThinkPHP 5.0 の _method __construct によるコードインジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2012-20007](CVE-2012-20007) | ThinkPHP | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | ThinkPHP 2.0-2.2 / 3.0 Lite | No known patch | ThinkPHP Dispatcher PATH_INFO の eval インジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-83020](CVE-2026-83020) | Oracle Platform Security for Java | 3.1 10 (Oracle) | Oracle Platform Security for Java 12.2.1.4.0 / 14.1.2.0.0 | September 2026 Critical Security Patch Update | Oracle Platform Security for Java の未認証乗っ取り；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-82994](CVE-2026-82994) | Oracle Platform Security for Java | 3.1 9.8 (Oracle) | Oracle Platform Security for Java 12.2.1.4.0 / 14.1.2.0.0 | September 2026 Critical Security Patch Update | Oracle Platform Security for Java の LDAP 経由の未認証乗っ取り；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-82995](CVE-2026-82995) | Oracle Platform Security for Java | 3.1 9.8 (Oracle) | Oracle Platform Security for Java 12.2.1.4.0 / 14.1.2.0.0 | September 2026 Critical Security Patch Update | Oracle Platform Security for Java の SOAP 経由の未認証乗っ取り；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-91570](CVE-2026-91570) | Oracle WebLogic Server | 3.1 9.8 (Oracle) | Oracle WebLogic Server 12.2.1.4.0 / 14.1.1.0.0 / 14.1.2.0.0 / 15.1.1.0.0 | November 2026 Critical Patch Update | Oracle WebLogic Server の TopLink 経由の HTTP による未認証乗っ取り；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-91583](CVE-2026-91583) | Oracle WebLogic Server | 3.1 9.8 (Oracle) | Oracle WebLogic Server 12.2.1.4.0 / 14.1.1.0.0 / 14.1.2.0.0 / 15.1.1.0.0 | November 2026 Critical Patch Update | Oracle WebLogic Server の TopLink 経由の HTTP による未認証乗っ取り；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-91585](CVE-2026-91585) | Oracle WebLogic Server | 3.1 9.8 (Oracle) | Oracle WebLogic Server 12.2.1.4.0 / 14.1.1.0.0 / 14.1.2.0.0 / 15.1.1.0.0 | November 2026 Critical Patch Update | Oracle WebLogic Server の TopLink 経由の TCP による未認証乗っ取り；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-103119](CVE-2026-103119) | Apache Tomcat | 3.1 9.1 (NVD) | Apache Tomcat 11.0.0-M25 to 11.0.26 | 11.0.27 | Apache Tomcat の AJP レスポンス混同によるデータ漏洩；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-133528](CVE-2026-133528) | BeamNG.drive | 4.0 9.3 (VulnCheck); 3.1 8.6 (VulnCheck) | BeamNG.drive <0.40.6 | 0.40.6 | BeamNG.drive の LuaJIT サンドボックス逃逸による RCE；実 exploit（drbloop2000）＋検出型 PoC（fankh）、未検証 | 確認済み | 未実施 |
| [CVE-2026-127064](CVE-2026-127064) | @fastify/reply-from | 3.1 8.2 (OpenJSF) | @fastify/reply-from <12.8.4 | 12.8.4 | @fastify/reply-from のセミコロン付きパスによるパストラバーサル；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-117659](CVE-2026-117659) | InfoScan | 4.0 8.5 (CISA); 3.1 8.1 (CISA) | Dorsett Controls InfoScan <=1.45.0 | 1.46 | InfoScan Electron クライアントの TLS 証明書検証欠如；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-129496](CVE-2026-129496) | PHP | 4.0 9.2 (PHP Group) | PHP 8.2 <8.2.36 / 8.3 <8.3.37 / 8.4 <8.4.28 / 8.5 <8.5.13 | 8.2.36 / 8.3.37 / 8.4.28 / 8.5.13 | PHP のタイムゾーンキャッシュの use-after-free によるリモートコード実行；ラボ型 PoC、本倉では未検証 | 確認済み | 未実施 |
| [CVE-2026-129474](CVE-2026-129474) | PHP | 4.0 9.2 (PHP Group) | PHP 8.5.0–<8.5.13 | 8.5.13 | PHP ガベージコレクタのマジックメソッドバックトレース Use-After-Free；トリガー型 PoC、RCE 未実証・未検証 | 確認済み | 未実施 |
| [CVE-2026-126714](CVE-2026-126714) | PHP | 4.0 9.2 (PHP Group) | PHP 8.2 <8.2.36 / 8.3 <8.3.37 / 8.4 <8.4.28 / 8.5 <8.5.13 | 8.2.36 / 8.3.37 / 8.4.28 / 8.5.13 | PHP セッションファイルの部分上書きによるデシリアライゼーション RCE；Docker ラボに参考エクスプロイト付、ラボ内 RCE のみ・未検証 | 確認済み | 未実施 |
| [CVE-2026-129289](CVE-2026-129289) | PHP | 4.0 9.2 (PHP Group) | PHP 8.2 <=8.2.35 / 8.3 <=8.3.36 / 8.4 <=8.4.27 / 8.5 <=8.5.12 | 8.2.36 / 8.3.37 / 8.4.28 / 8.5.13 | 再利用されたバックエンド接続における未読リクエストボディによる PHP-FPM リクエストスマグリング；トリガー型 PoC、RCE 未実証・未検証 | 確認済み | 未実施 |
| [CVE-2026-133212](CVE-2026-133212) | @fastify/reply-from | 3.1 9.0 (OpenJSF) | @fastify/reply-from before 12.9.1 | 12.9.1 | ボディなしリクエストで Content-Length を転送することによる HTTP リクエストスマグリング；検出用 PoC のみ、未検証 | 確認済み | 未実施 |
| [CVE-2026-77355](CVE-2026-77355) | isomorphic-git | 3.1 8.8 (GHSA) | isomorphic-git before 1.38.7 (Windows NTFS) | 1.38.7 | 悪意のあるリポジトリが Windows NTFS 予約パス別名で .git メタデータを汚染；検出用 PoC のみ、未検証 | 確認済み | 未実施 |
| [CVE-2026-86017](CVE-2026-86017) | isomorphic-git | 3.1 8.0 (GHSA) | isomorphic-git before 1.38.8 (cherry-pick symlink) | 1.38.8 | cherry-pick がシンボリックリンクをたどり攻撃者の blob をワークツリー外に書き込む；検出用 PoC のみ、未検証 | 確認済み | 未実施 |
| [CVE-2026-104711](CVE-2026-104711) | Apache Struts | 3.1 9.8 (NVD); 3.1 8.1 (Apache) | 2.0.0-2.3.37, 2.5.0-2.5.33, 6.0.0-6.11.0, 7.0.0-7.3.0 | 6.12.0 (6.x), 7.4.0 (7.x) | legacy RestfulActionMapper の OGNL インジェクション；PoC は Docker lab で eval と exec を実証、出力は X_Matched_Action に反映；exec には lab の guard 緩和が必要 | 確認済み | 未実施 |
| [CVE-2026-133325](CVE-2026-133325) | Apache Tomcat | 3.1 9.8 (NVD) | 11.0.28-11.0.29, 10.1.62, 9.0.124 |  | Apache Tomcat のエンティティ認証を伴わない鍵交換；PoC はバージョン指紋検出のみで、鍵交換攻撃は実施しない（MITM 位置が必要）；PoC の主張範囲は勧告と不一致、未検証 | 確認済み | 未実施 |
| [CVE-2026-95517](CVE-2026-95517) | Apache Tomcat | 3.1 9.1 (NVD) | 11.0.0-M1-11.0.27, 10.1.0-M1-10.1.61, 9.0.13-9.0.123 | 11.0.29, 10.1.62, 9.0.124 | Apache Tomcat EncryptInterceptor の完全性チェック欠如；PoC はトークンのビットフリップ改ざん検出のみ | 確認済み | 未実施 |

### データベース (11)

| ID | 製品 | スコア | 影響バージョン | 修正バージョン | 評価 | CVE ステータス | 再現 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [CVE-2026-118383](CVE-2026-118383) | MongoDB Server レプリケーション | unknown | 8.0.x before 8.0.37 (8.0.34 tested); 8.2.12 still reproduced at collection time | 8.0.37 (SERVER-138175, SERVER-138119) | ラボでの UAF クラッシュ；コード実行は未実証 | 確認済み | — 対象なし |
| [CVE-2026-116366](CVE-2026-116366) | ClickHouse Server | 4.0 9.5 (ClickHouse) | ClickHouse 26.3 < 26.3.62.3-lts, 26.8 < 26.8.36.3-lts, 26.9 < 26.9.27.3-stable, 26.10 < 26.10.3.7-stable | 26.3.62.3-lts / 26.8.36.3-lts / 26.9.27.3-stable / 26.10.3.7-stable (2026-10-30) | 未認証 RCE を主張；ラボでは差分検出 + 武器化 DoS のみ検証 | 確認済み | ◐ 部分 |
| [CVE-2026-13078](CVE-2026-13078) | MongoDB Server | 3.1 7.7 (MongoDB)；4.0 6.3 (MongoDB) | MongoDB Server 7.0 before 7.0.39, 8.0 before 8.0.28, 8.2 before 8.2.12, 8.3 before 8.3.7 | 7.0.39, 8.0.28, 8.2.12, 8.3.7 | 低権限認証ユーザーが MozJS モジュールローダー経由でローカルファイルを漏洩；RCE ではない | 確認済み | 未実施 |
| [CVE-2026-73504](CVE-2026-73504) | cassandra-jdbc-wrapper | 3.1 5.5 (GHSA) | cassandra-jdbc-wrapper < 4.16.4; >= 5.0.0, < 5.0.2 | 4.16.4 / 5.0.2 | 認証トークンが DEBUG ログに平文で記録；4.16.4/5.0.2 で修正、ラボ証拠あり | 確認済み | 未実施 |
| [CVE-2026-116244](CVE-2026-116244) | pgAdmin 4 | 3.1 9.6 (NVD)；4.0 7.1 (PostgreSQL) | pgAdmin 4 ≤ 9.18 | 9.19 (2026-10-29) | サービスモードの libpq が pgAdmin サービスアカウントの Kerberos 認証情報で攻撃者の DB に接続；9.19 で修正 | 確認済み | 未実施 |
| [CVE-2026-126837](CVE-2026-126837) | MongoDB Node.js driver | 4.0 9.1 (MongoDB); 3.1 7.4 (MongoDB) | MongoDB Node.js driver 3.3.3 to < 7.8.0 | 7.8.0 | SRV 親ドメイン検証の回避で DB トラフィックを攻撃者へ；認証情報漏洩、ラボ証拠あり | 確認済み | 未実施 |
| [CVE-2026-119179](CVE-2026-119179) | MongoDB Node.js driver | 4.0 8.3 (MongoDB); 3.1 7.0 (MongoDB) | mongodb >= 6.11.0 < 6.22.0 and >= 7.0.0 < 7.8.0 | 6.22.0 / 7.8.0 | CSOT タイムアウト後に未読応答付き接続がプールへ；リクエスト横断のデータ漏洩、未検証 | 確認済み | 未実施 |
| [CVE-2026-115290](CVE-2026-115290) | Elasticsearch | 3.1 7.5 (GHSA) | Elasticsearch 8.10.0–8.19.23, 9.0.0–9.4.8, 9.5.0–9.5.5 (remote_cluster_server enabled) | 8.19.24 / 9.4.9 / 9.5.6 | リモートクラスターサーバーの認証前デシリアライズによる未認証再帰 DoS；ラボ証拠あり | 確認済み | 未実施 |
| [CVE-2026-126755](CVE-2026-126755) | ArangoDB | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | ArangoDB <3.12.11 | 3.12.11 | ArangoDB の認証バイパス；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-116331](CVE-2026-116331) | PostgreSQL | 3.1 8.8 (PostgreSQL) | PostgreSQL < 18.7, 17.12, 16.16, 15.20, 14.25 | 18.7 / 17.12 / 16.16 / 15.20 / 14.25 | PostgreSQL の min/max 集計における型混同により、オブジェクト作成者が任意のコードを実行可能；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-6460](CVE-2026-6460) | PostgreSQL | 3.1 8.8 (PostgreSQL) | PostgreSQL < 18.7, 17.12, 16.16, 15.20, 14.25 | 18.7 / 17.12 / 16.16 / 15.20 / 14.25 | PostgreSQL の型混同により、オブジェクト作成者が ALTER ... SET DATA TYPE 経由で任意のコードを実行可能；検出型 PoC、未検証 | 確認済み | 未実施 |

### OS / システム / DevOps (50)

| ID | 製品 | スコア | 影響バージョン | 修正バージョン | 評価 | CVE ステータス | 再現 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [CVE-2026-65094](CVE-2026-65094) | NVIDIA VIRTIO-Net for BlueField | 3.1 9.0 (NVIDIA) | NVIDIA VIRTIO-Net GA <25.10.6; LTS25 <25.10.2; LTS24 <24.10.50; LTS23 1.7.21 and older (BlueField-3) | 25.10.6 (GA) / 25.10.2 (LTS25) / 24.10.50 (LTS24) / 23.10.23 (LTS23) | NVIDIA VIRTIO-Net for BlueField の任意書き込みによるコード実行；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-74127](CVE-2026-74127) | AMD Platform Security Processor (PSP) boot ROM | 4.0 9.4 (AMD) | AMD Zen 1 / Zen+ processors (PSP boot ROM) | No fix planned (AMD: boot ROM immutable) | Zen 1/Zen+ PSP ブート ROM 署名検証バイパス；Google が実機で PoC を検証済み、修正予定なし | 確認済み | — 対象なし |
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
| [CVE-2026-129987](CVE-2026-129987) | Dokploy | 3.1 9.9 (GHSA) | Dokploy < 0.31.1 (v0.29.0-v0.31.0 per upstream version archaeology) | 0.31.1 | 認証後 RCE：DB パスワード変更のコマンドインジェクション；全チェーンは主張のみ、未検証 | 確認済み | 未実施 |
| [CVE-2026-43499](CVE-2026-43499) | Linux カーネル rtmutex | 3.1 7.8 (Linux kernel) | Linux kernel rtmutex path (PoC targets 4.14.186+ on realme RMX3031/MT6893) |  | realme RMX3031 カーネル LPE stage1；root は主張のみ、未検証 | 確認済み | 未実施 |
| [CVE-2026-112477](CVE-2026-112477) | Apple iOS IOSurface | 3.1 7.0 (NVD) | iOS 26.x (tested on iOS 26.4, arm64e) | iOS 26.7.2 / iPadOS 26.7.2 | IOSurface UAF stale-read プリミティブ；研究 PoC、権限昇格は未実証 | 確認済み | 未実施 |
| [CVE-2026-130587](CVE-2026-130587) | OpenFunction | 3.1 9.9 (GHSA) | OpenFunction through 1.2.0 | no vendor fix (upstream issue #532 OPEN) | テナント PodSpec が operator ワークロードにそのまま複製；ノード脱出、ベンダー修正なし | 確認済み | 未実施 |
| [CVE-2026-126978](CVE-2026-126978) | Philips Hue Bridge | 3.0 8.8 (GHSA) | Philips Hue Bridge gen 2 and gen 3 (all firmware prior to patch) | no fixed version published | HAP ペアリング TLV8 ヒープオーバーフロー；隣接ネットワーク、認証前、未検証 | 確認済み | 未実施 |
| [CVE-2026-126979](CVE-2026-126979) | Philips Hue Bridge | 3.0 8.8 (GHSA) | Philips Hue Bridge gen 2 and gen 3 (all firmware prior to patch) | no fixed version published | ChaCha20 長さアンダーフローで HAP 認証を回避；隣接ネットワーク、未検証 | 確認済み | 未実施 |
| [CVE-2026-130335](CVE-2026-130335) | Info-ZIP Zip | 3.1 2.9 (MITRE) | Info-ZIP Zip 3.0, 3.1 beta–3.1c | Debian zip/3.0-16 (quote_arg fix) | zip -T 実行時に細工したアーカイブ名でコマンドインジェクション；ローカル前提条件あり | 確認済み | 未実施 |
| [CVE-2026-121529](CVE-2026-121529) | FortiClient | 3.1 9.6 (GHSA); 3.1 9.1 (Fortinet) | FortiClient Windows / Windows PAM 7.4.0–7.4.7, 7.2.0–7.2.14; FortiClient Mac 7.4.0–7.4.7 | 7.4.8 / 7.2.15 | ローカル API の Origin 検証欠如；被害者ブラウザ経由で RCE（モデル実験）、未検証 | 確認済み | 未実施 |
| [CVE-2026-99273](CVE-2026-99273) | Linux カーネル (ksmbd) | unknown | Linux < 7.3.2 with CONFIG_SMB_SERVER | mainline a025c4991a7d8; stable 6.12.117 / 6.18.61 / 7.3.2 | ksmbd 応答バッファ外 2 バイトのヒープ範囲外書き込み；KASAN 証拠、スコア未割当 | 確認済み | 未実施 |
| [CVE-2026-13043](CVE-2026-13043) | WatchGuard エンドポイントセキュリティ | 4.0 9.3 (WatchGuard) | WatchGuard Endpoint Security < 8.00.26.0012 (Windows) | 8.00.26.0012 | ローカル管理者がドライバハンドシェイクを偽造し特権 IOCTL へ；MSR 読み取りで KASLR を回避、任意プロセスメモリ読み取り | 確認済み | 未実施 |
| [CVE-2026-133274](CVE-2026-133274) | THC-Hydra | 4.0 7.1 (VulnCheck); 3.1 6.5 (VulnCheck) | THC-Hydra through 9.7 | commit 6ab9ad8 (post-9.7, no release tagged) | hydra-http-form.c の Set-Cookie 解析でスタックバッファオーバーフロー；悪意あるサーバが Hydra クライアントをクラッシュ、未検証 | 確認済み | 未実施 |
| [CVE-2026-133305](CVE-2026-133305) | sqlmap | 4.0 2.3 (VulnCheck); 3.1 4.3 (VulnCheck) | sqlmap before 1.10.11.89 | 1.10.11.89 | クロスホストリダイレクトによる Cookie / Authorization ヘッダの漏洩、未検証 | 確認済み | 未実施 |
| [CVE-2026-133189](CVE-2026-133189) | Cinder | 3.1 9.6 (Red Hat) | OpenStack Cinder with SSH-based storage drivers | Upstream patch proposed, no fixed release published (2026-11-19) | Cinder SSH ストレージドライバのコマンドインジェクション；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-130778](CVE-2026-130778) | Incus | 4.0 10.0 (VulnCheck); 3.1 10.0 (VulnCheck) | Incus <7.6.0 | 7.6.0 / 6.0.9 LTS | Incus mTLS 証明書チェーン認証バイパス；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-130786](CVE-2026-130786) | Incus | 4.0 9.4 (VulnCheck); 3.1 9.9 (VulnCheck) | Incus <7.6.0 | 7.6.0 / 6.0.9 LTS | Incus OCI 設定インジェクションによりホストで root コマンド実行；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-132891](CVE-2026-132891) | JetBrains TeamCity | 3.1 9.8 (JetBrains) | TeamCity 2026.1 <2026.1.4, 2025.11 <2025.11.8 | 2026.2 / 2026.1.4 / 2025.11.8 | TeamCity の外部プルリクエストによる RCE；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-123890](CVE-2026-123890) | VMware vCenter | 3.1 9.8 (VMware) | vCenter 9.1.x / 9.0.x / 8.0 / 5.x | 9.1.1.0200 / 9.0.2.0200 / 8.0 U3m / 5.2.5 | VMware vCenter ディレクトリサービスの認証バイパス；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-132234](CVE-2026-132234) | TeamCity | 3.1 9.9 (JetBrains) | TeamCity 2026.1 <2026.1.3 / <2025.11.7 | 2026.1.3 / 2025.11.7 | TeamCity Mercurial VCS root 設定のパラメータインジェクションによる RCE；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-132233](CVE-2026-132233) | TeamCity | 3.1 9.9 (JetBrains) | TeamCity 2026.1 <2026.1.3 / <2025.11.7 | 2026.1.3 / 2025.11.7 | TeamCity ビルド属性インジェクションによる RCE；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-132232](CVE-2026-132232) | TeamCity | 3.1 9.9 (JetBrains) | TeamCity 2026.1 <2026.1.3 / <2025.11.7 | 2026.1.3 / 2025.11.7 | TeamCity Perforce 設定のパラメータインジェクションによる RCE；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-132231](CVE-2026-132231) | TeamCity | 3.1 9.9 (JetBrains) | TeamCity 2026.1 <2026.1.3 / <2025.11.7 | 2026.1.3 / 2025.11.7 | TeamCity Perforce 設定の文字マッピングによる RCE；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-130784](CVE-2026-130784) | Incus | 4.0 9.4 (VulnCheck); 3.1 9.9 (VulnCheck) | Incus <7.6.0 | 7.6.0 | Incus のデフォルトプロジェクトリソース継承の認可バイパスによるホスト root コード実行；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-130780](CVE-2026-130780) | Incus | 4.0 9.4 (VulnCheck); 3.1 9.9 (VulnCheck) | Incus <7.6.0 | 7.6.0 | Incus マイグレーションのパストラバーサルによるホスト任意パス書き込み；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-129991](CVE-2026-129991) | Dokploy | 3.1 9.9 (GHSA) | Dokploy <0.31.1 | 0.31.1 | Dokploy バックアッププレフィックスのコマンドインジェクションによるホスト RCE；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-129316](CVE-2026-129316) | Dokploy | 3.1 9.9 (GHSA) | Dokploy 0.29.13 to <0.31.0 | 0.31.0 | Dokploy WebSocket ハンドラの認可欠如によるメンバーからホスト root への権限昇格；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-129986](CVE-2026-129986) | Dokploy | 3.1 9.9 (GHSA) | Dokploy <0.31.1 | 0.31.1 | Dokploy mount.deleteFileMount のコマンドインジェクションによるホスト RCE；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-129989](CVE-2026-129989) | Dokploy | 3.1 9.9 (GHSA) | Dokploy <0.31.1 | 0.31.1 | Dokploy Nixpacks publishDirectory のコマンドインジェクションによるホスト RCE；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-130759](CVE-2026-130759) | Fleet | 4.0 9.4 (VulnCheck); 3.1 9.9 (VulnCheck) | Fleet 4.71.0 to <4.88.2 | 4.88.2 | Fleet SAML SSO の認証バイパス；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-130771](CVE-2026-130771) | Incus | 4.0 8.5 (VulnCheck); 3.1 9.9 (VulnCheck) | Incus <7.6.0 | 7.6.0 | Incus バックアップ/イメージ メタデータによるホストファイル読み書き；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-130773](CVE-2026-130773) | Incus | 4.0 9.4 (VulnCheck); 3.1 9.9 (VulnCheck) | Incus <7.6.0 | 7.6.0 | Incus デフォルトプロジェクトへのリソース作成の認可バイパス；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-126752](CVE-2026-126752) | Dagu | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | Dagu 1.23.0 to <2.0.0 | 2.0.0 | Dagu の未認証 RCE；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-73969](CVE-2026-73969) | AnsibleForms | 3.1 9.8 (GHSA) | AnsibleForms <6.2.1 | 6.2.1 | AnsibleForms のハードコードされた JWT 署名鍵による認証バイパス；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-130779](CVE-2026-130779) | Incus | 4.0 8.5 (VulnCheck); 3.1 9.6 (VulnCheck) | Incus <7.6.0 | 7.6.0 | Incus カスタムボリュームのバックアップ・スナップショット名のパストラバーサルによるホストディレクトリ削除；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-130783](CVE-2026-130783) | Incus | 4.0 9.3 (VulnCheck); 3.1 9.6 (VulnCheck) | Incus <7.6.0 | 7.6.0 | Incus 操作イベントによるトークン漏洩と認可欠如による完全な乗っ取り；検出型 PoC、未検証 | 確認済み | 未実施 |
| [CVE-2026-126088](CVE-2026-126088) | OpenPLC Runtime | 4.0 9.2 (CISA); 3.1 8.1 (CISA) | OpenPLC Runtime <=4.2.4 | 4.3.0 | OpenPLC Runtime の競合状態による未認証の管理者アカウント作成；検出型 PoC、未検証 | 確認済み | 未実施 |


完全な評価と引用については各 CVE ディレクトリを参照。
