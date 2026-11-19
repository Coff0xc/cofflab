[English](README.md) | [中文](README.zh-CN.md) | **日本語**

# Coff0xc CVE キュレーション

![scope](https://img.shields.io/badge/scope-public%20PoC%20only-blue) ![repro](https://img.shields.io/badge/repro-isolated%20sandbox-green)

Coff0xc が管理する CVE 脆弱性と公開 PoC のキュレーション集。各エントリは製品、スコア、日付、および公開資料が実際に実証した内容を記録する。

公開済みの資料のみを収集する。収録は読み取り専用で、実行しない。再現は隔離環境でのみ行う。認可されたセキュリティ研究と防御のみを目的とする。

**再現：** ✅ 完全——隔離サンドボックスでエンドツーエンド再現 · ◐ 部分——部分再現または mock 上で検証 · — 対象なし——利用可能な脆弱な対象なし · 未実施——未再現。

---

## 目次

| ID | 製品 | スコア | 評価 | 再現 |
| --- | --- | --- | --- | --- |
| [CVE-2024-10441](CVE-2024-10441) | Synology DSM/BSM synoplugind | 3.1 9.8（公開 README、ベンダー公告未確認） | パッチ差分分析 + ローカル検証；そのまま使えるリモート exploit はない | ◐ 部分 |
| [CVE-2026-40217](CVE-2026-40217) | BerriAI LiteLLM | 3.1 8.8 PR:L（公開 README） | 認証後のラボ RCE；API キーが必要 | ◐ 部分 |
| [CVE-2026-114938](CVE-2026-114938) | OpenJDK Base64 (Java4Shell) | 4.0 9.2 (Calif)；3.1 8.1 (Oracle)；3.1 9.8 (Red Hat) | トリガー / クラッシュ / リーク / 実験；公開された汎用 RCE はない | ◐ 部分 |
| [CVE-2026-118383](CVE-2026-118383) | MongoDB Server レプリケーション | unknown | ラボでの UAF クラッシュ；コード実行は未実証 | — 対象なし |
| [CVE-2026-123007](CVE-2026-123007) | F5 NGINX HTTP/2 | 4.0 9.2 (F5)；3.1 8.1 (F5) | トリガー + 新規起動した Docker に対する RCE デモのみ | — 対象なし |
| [CVE-2026-123488](CVE-2026-123488) | Craft CMS 要素検索 | 3.1 9.8 (GHSA)；4.0 9.3 (GitHub) | 未認証 SQLi による DB 書き込み / 権限昇格 | ◐ 部分 |
| [CVE-2026-129448](CVE-2026-129448) | Apache Roller XML-RPC | 3.1 9.8（公開の主張、未検証） | フレームワークは gadget の自前用意が必要；ローカル mock のみ | ◐ 部分 |
| [CVE-2026-90817](CVE-2026-90817) | Vanderbilt REDCap | 3.1 9.8（公開の主張、未検証） | 発見者のスクリプト / プレースホルダーのフレームワーク / 一括検出 | ◐ 部分 |
| [CVE-2026-129287](CVE-2026-129287) | N-able N-central | 4.0 8.3 (N-able) | 認証後の帯域外 XXE によるファイル読み取り；クローズドソース機器のためローカル再現不可 | ◐ 部分 |
| [CVE-2026-130796](CVE-2026-130796) | Flowise | 4.0 8.8 (VulnCheck)；3.1 8.2 (VulnCheck) | 未認証での平文 MCP トークン漏洩；付属スクリプトはオフラインの論理シミュレーション | ✅ 完全 |
| [CVE-2026-119958](CVE-2026-119958) | Windows LDAP | 3.1 9.8 (Microsoft) | OOB 書き込み + クラッシュのラボ再現；実際の Windows LDAP での RCE は未実証 | ✅ 完全 |
| [CVE-2026-123039](CVE-2026-123039) | Check Point Gaia OS | 3.1 7.8 (Check Point) | ワールドライタブルなソケット経由の root への権限昇格（ラボ）；実際の Gaia では未検証 | ◐ 部分 |
| [CVE-2026-123158](CVE-2026-123158) | OpenSSH sshd | 3.1 8.1 (MITRE) | パスワード認証バイパスによるログインのラボ再現；実環境での証拠なし | — 対象なし |
| [CVE-2026-123218](CVE-2026-123218) | IBM Aspera Faspex 5 | 3.1 9.8 (IBM) | バージョン確認のみ；バイパスは未実証 | ✅ 完全 |
| [CVE-2026-123751](CVE-2026-123751) | WP Duplicate | 3.1 9.8 (CISA-ADP) | 未実行の exploit スクリプト；実際の WordPress での RCE は未実証 | ◐ 部分 |
| [CVE-2026-124194](CVE-2026-124194) | Microsoft Outlook | 3.1 6.5 (Microsoft) | .msg ファイルのトリガーのみ；実際の Outlook での NTLM 漏洩は未実証 | ◐ 部分 |
| [CVE-2026-90436](CVE-2026-90436) | Apache Axis 1.x | 3.1 9.8 (CISA-ADP) | 未認証クラス生成のラボ再現；デフォルト classpath での RCE は未実証 | ◐ 部分 |
| [CVE-2024-27834](CVE-2024-27834) | WebKit (Apple) | 3.1 5.5 (NVD) | 分析のみ；実行可能な PoC なし | — 対象なし |
| [CVE-2026-111560](CVE-2026-111560) | Barracuda ESG / ADC / WAF / WSG | 4.0 8.6 (Mandiant)；3.1 7.2 (NVD) | ラボでの root コマンド実行（管理者権限が必要）；未認証 root は CVE-2026-116606 との連携でのみ | ◐ 部分 |
| [CVE-2026-115731](CVE-2026-115731) | Puppet / OpenVox Server | 4.0 9.4 (Perforce)；3.1 9.9 (NVD) | アドバイザリで確認されたサーバーコマンド実行（有効な CA 署名クライアント証明書が必要） | — 対象なし |
| [CVE-2026-116606](CVE-2026-116606) | Barracuda ESG | 4.0 9.3 (Mandiant)；3.1 9.8 (NVD) | 未認証の設定復元トリガー；root は CVE-2026-111560 との連携でのみ | ◐ 部分 |
| [CVE-2026-19868](CVE-2026-19868) | SonicWall SonicOS | 3.1 7.5 (CISA-ADP)；3.1 7.1 (SonicWall) | バージョン確認のみ | ✅ 完全 |
| [CVE-2026-129271](CVE-2026-129271) | N-able N-central Patch Management | 4.0 8.5 (N-able) | 認証後のローカル権限昇格（ProductAdmin の認証情報 + コールバックが必要） | — 対象なし |
| [CVE-2026-129280](CVE-2026-129280) | N-able N-central | 4.0 9.3 (N-able) | 未認証の設定書き込み（単一操作のデモ、可逆） | ◐ 部分 |
| [CVE-2026-102895](CVE-2026-102895) | GPUStack | 3.1 9.8 (GHSA) | ラボで検証された未認証の管理者乗っ取り；実利用はベンダー報告であり、この PoC による実証ではない | ◐ 部分 |
| [CVE-2026-114713](CVE-2026-114713) | UnrealIRCd | 3.1 8.6 (GHSA) | サーバー間コマンドインジェクションのラボ PoC；OS レベルの RCE ではない | ✅ 完全 |
| [CVE-2026-116779](CVE-2026-116779) | FreeSWITCH | 3.1 9.8 (GHSA) | ラボで検証された SIP MESSAGE によるコマンド実行；実運用での証拠なし | ◐ 部分 |
| [CVE-2026-119618](CVE-2026-119618) | Apache httpd mod_http2 | 3.1 8.1 (NVD)；3.1 9.8 (Red Hat) | ASan/TSan 下でのヒープ破壊 + クラッシュ；RCE は未実証 | — 対象なし |
| [CVE-2026-126187](CVE-2026-126187) | React Server Components / Next.js | 4.0 9.5 (GHSA) | ラボ Docker アプリでの RCE；トリガーには稀な条件が必要 | ◐ 部分 |
| [CVE-2026-125350](CVE-2026-125350) | Google Chrome | 3.1 8.8 (NVD) | 回帰テストファイルによるレンダラークラッシュ；RCE ペイロードなし | ✅ 完全 |
| [CVE-2026-126473](CVE-2026-126473) | OpenEMR | 4.0 9.3 (VulnCheck)；3.1 9.1 (VulnCheck) | ラボ Docker で公式 8.3.0 イメージに対し未認証で FHIR Patient を作成；8.4.0 はコロン形式の登録を拒否 | 未実施 |
| [CVE-2026-98432](CVE-2026-98432) | Linux カーネル TCP | 3.1 9.8 (Linux kernel) | inet_csk_route_req での KASAN 検証済み UAF クラッシュ；コード実行は未実証 | 未実施 |
| [CVE-2026-111497](CVE-2026-111497) | Node.js Brotli | 4.0 9.2 (Google)；3.1 9.8 (NVD) | 細工した Brotli ストリームによるリモート DoS を検証済み；RCE は分析のみ | 未実施 |
| [CVE-2026-116366](CVE-2026-116366) | ClickHouse Server | 4.0 9.5 (ClickHouse) | 未認証 RCE を主張；ラボでは差分検出 + 武器化 DoS のみ検証 | 未実施 |
| [CVE-2026-126170](CVE-2026-126170) | Fortinet FortiManager / FortiAnalyzer | 3.1 9.8 (Fortinet) | ラボで JRPC JSON インジェクションによる未認証 RCE；7.6.7 と 7.6.8 の差分 | 未実施 |
| [CVE-2026-76954](CVE-2026-76954) | Synology DSM 認証 API | 3.1 9.8 (Synology) | 認証前のスタック SQLi（syno-pam-key.db）；ファイル読み書きはベンダー公告の主張で PoC 未実証 | 未実施 |
| [CVE-2026-129349](CVE-2026-129349) | Apache Shiro DefaultLdapRealm | 4.0 9.1 (Apache) | 一度有効なログイン後の認証バイパス；キャッシュ有効時（非デフォルト）は任意のパスワードで認証 | 未実施 |
| [CVE-2026-124079](CVE-2026-124079) | rConfig Core / Pro | 4.0 9.3 (VulnCheck)；3.1 9.8 (VulnCheck) | ラボで Redis ベースの Horizon キュー汚染による未認証 RCE | 未実施 |
| [CVE-2026-86829](CVE-2026-86829) | Apache Airflow コア | 3.1 8.8 (Apache) | DAG 作成者による XCom デシリアライズ経由のスケジューラ RCE；3.3.2 でラボ検証済み、3.4.0 ではクリーン | 未実施 |
| [CVE-2026-121653](CVE-2026-121653) | Ivanti Endpoint Manager Core | 3.1 9.8 (Ivanti) | ラボで未認証 SQLi → Core DB アカウント経由の OS コマンド実行 | 未実施 |
| [CVE-2026-124552](CVE-2026-124552) | Webmin Shorewall モジュール | 4.0 4.8 (VulnCheck)；3.1 4.8 (VulnCheck) | ラボで格納型 XSS → root コマンド実行（Shorewall モジュール権限 + 管理者の閲覧が必要）；未修正のトラバーサル 0day も実証 | 未実施 |
| [CVE-2026-104623](CVE-2026-104623) | SUSE Rancher Manager | 3.1 6.3 (SUSE) | 認証ユーザーが管理クラスタでシェル Pod を取得；非特権 Pod、API アクセスは制限付き | 未実施 |
| [CVE-2026-105437](CVE-2026-105437) | Git 3方向マージ | 3.1 7.5 (GitLab) | 攻撃者制御コンテンツのマージでヒープオーバーフロー；2.56.0 で SIGSEGV、2.56.1 ではクリーン | 未実施 |
| [CVE-2026-111585](CVE-2026-111585) | TeamViewer クライアント | 3.1 8.8 (TeamViewer) | 実際の 15.82.6 バイナリでの viewer ヒープオーバーフロー + クラッシュ；RCE は主張、クラッシュは実証済み | 未実施 |
| [php-session-upload-progress-2026-rce](php-session-upload-progress-2026-rce) | PHP セッションアップロード進捗 | unknown | ラボでセッションハンドラ不一致による未認証 RCE（php:8.4.27-apache）；未修正、緩和策はアップロード進捗の無効化 | 未実施 |

完全な評価と引用については各 CVE ディレクトリを参照。
