[English](README.md) | [中文](README.zh-CN.md) | **日本語**

# Coff0xc CVE キュレーション

Coff0xc が管理する CVE 脆弱性と公開 PoC のキュレーション集。各エントリは製品、スコア、日付、および公開資料が実際に実証した内容を記録する。

公開済みの資料のみを収集する。収録は読み取り専用で、実行しない。再現は隔離環境でのみ行う。認可されたセキュリティ研究と防御のみを目的とする。

## 目次

| CVE | 製品 | スコア | 評価 |
| --- | --- | --- | --- |
| [CVE-2024-10441](CVE-2024-10441) | Synology DSM/BSM synoplugind | 3.1 9.8（公開 README、ベンダー公告未確認） | パッチ差分分析 + ローカル検証；そのまま使えるリモート exploit はない |
| [CVE-2026-40217](CVE-2026-40217) | BerriAI LiteLLM | 3.1 8.8 PR:L（公開 README） | 認証後のラボ RCE；API キーが必要 |
| [CVE-2026-114938](CVE-2026-114938) | OpenJDK Base64 (Java4Shell) | 4.0 9.2 (Calif)；3.1 8.1 (Oracle)；3.1 9.8 (Red Hat) | トリガー / クラッシュ / リーク / 実験；公開された汎用 RCE はない |
| [CVE-2026-118383](CVE-2026-118383) | MongoDB Server レプリケーション | unknown | ラボでの UAF クラッシュ；コード実行は未実証 |
| [CVE-2026-123007](CVE-2026-123007) | F5 NGINX HTTP/2 | 4.0 9.2 (F5)；3.1 8.1 (F5) | トリガー + 新規起動した Docker に対する RCE デモのみ |
| [CVE-2026-123488](CVE-2026-123488) | Craft CMS 要素検索 | 3.1 9.8 (GHSA)；4.0 9.3 (GitHub) | 未認証 SQLi による DB 書き込み / 権限昇格 |
| [CVE-2026-129448](CVE-2026-129448) | Apache Roller XML-RPC | 3.1 9.8（公開の主張、未検証） | フレームワークは gadget の自前用意が必要；ローカル mock のみ |
| [CVE-2026-90817](CVE-2026-90817) | Vanderbilt REDCap | 3.1 9.8（公開の主張、未検証） | 発見者のスクリプト / プレースホルダーのフレームワーク / 一括検出 |
| [CVE-2026-129287](CVE-2026-129287) | N-able N-central | 4.0 8.3 (N-able) | 認証後の帯域外 XXE によるファイル読み取り；クローズドソース機器のためローカル再現不可 |
| [CVE-2026-130796](CVE-2026-130796) | Flowise | 4.0 8.8 (VulnCheck)；3.1 8.2 (VulnCheck) | 未認証での平文 MCP トークン漏洩；付属スクリプトはオフラインの論理シミュレーション |
| [CVE-2026-119958](CVE-2026-119958) | Windows LDAP | 3.1 9.8 (Microsoft) | OOB 書き込み + クラッシュのラボ再現；実際の Windows LDAP での RCE は未実証 |
| [CVE-2026-123039](CVE-2026-123039) | Check Point Gaia OS | 3.1 7.8 (Check Point) | ワールドライタブルなソケット経由の root への権限昇格（ラボ）；実際の Gaia では未検証 |
| [CVE-2026-123158](CVE-2026-123158) | OpenSSH sshd | 3.1 8.1 (MITRE) | パスワード認証バイパスによるログインのラボ再現；実環境での証拠なし |
| [CVE-2026-123218](CVE-2026-123218) | IBM Aspera Faspex 5 | 3.1 9.8 (IBM) | バージョン確認のみ；バイパスは未実証 |
| [CVE-2026-123751](CVE-2026-123751) | WP Duplicate | 3.1 9.8 (CISA-ADP) | 未実行の exploit スクリプト；実際の WordPress での RCE は未実証 |
| [CVE-2026-124194](CVE-2026-124194) | Microsoft Outlook | 3.1 6.5 (Microsoft) | .msg ファイルのトリガーのみ；実際の Outlook での NTLM 漏洩は未実証 |
| [CVE-2026-90436](CVE-2026-90436) | Apache Axis 1.x | 3.1 9.8 (CISA-ADP) | 未認証クラス生成のラボ再現；デフォルト classpath での RCE は未実証 |
| [CVE-2024-27834](CVE-2024-27834) | WebKit (Apple) | 3.1 5.5 (NVD) | 分析のみ；実行可能な PoC なし |
| [CVE-2026-111560](CVE-2026-111560) | Barracuda ESG / ADC / WAF / WSG | 4.0 8.6 (Mandiant)；3.1 7.2 (NVD) | ラボでの root コマンド実行（管理者権限が必要）；未認証 root は CVE-2026-116606 との連携でのみ |
| [CVE-2026-115731](CVE-2026-115731) | Puppet / OpenVox Server | 4.0 9.4 (Perforce)；3.1 9.9 (NVD) | アドバイザリで確認されたサーバーコマンド実行（有効な CA 署名クライアント証明書が必要） |
| [CVE-2026-116606](CVE-2026-116606) | Barracuda ESG | 4.0 9.3 (Mandiant)；3.1 9.8 (NVD) | 未認証の設定復元トリガー；root は CVE-2026-111560 との連携でのみ |
| [CVE-2026-19868](CVE-2026-19868) | SonicWall SonicOS | 3.1 7.5 (CISA-ADP)；3.1 7.1 (SonicWall) | バージョン確認のみ |
| [CVE-2026-129271](CVE-2026-129271) | N-able N-central Patch Management | 4.0 8.5 (N-able) | 認証後のローカル権限昇格（ProductAdmin の認証情報 + コールバックが必要） |
| [CVE-2026-129280](CVE-2026-129280) | N-able N-central | 4.0 9.3 (N-able) | 未認証の設定書き込み（単一操作のデモ、可逆） |
| [CVE-2026-102895](CVE-2026-102895) | GPUStack | 3.1 9.8 (GHSA) | ラボで検証された未認証の管理者乗っ取り；実利用はベンダー報告であり、この PoC による実証ではない |
| [CVE-2026-114713](CVE-2026-114713) | UnrealIRCd | 3.1 8.6 (GHSA) | サーバー間コマンドインジェクションのラボ PoC；OS レベルの RCE ではない |
| [CVE-2026-116779](CVE-2026-116779) | FreeSWITCH | 3.1 9.8 (GHSA) | ラボで検証された SIP MESSAGE によるコマンド実行；実運用での証拠なし |
| [CVE-2026-119618](CVE-2026-119618) | Apache httpd mod_http2 | 3.1 8.1 (NVD)；3.1 9.8 (Red Hat) | ASan/TSan 下でのヒープ破壊 + クラッシュ；RCE は未実証 |
| [CVE-2026-126187](CVE-2026-126187) | React Server Components / Next.js | 4.0 9.5 (GHSA) | ラボ Docker アプリでの RCE；トリガーには稀な条件が必要 |
| [CVE-2026-125350](CVE-2026-125350) | Google Chrome | 3.1 8.8 (NVD) | 回帰テストファイルによるレンダラークラッシュ；RCE ペイロードなし |

完全な評価と引用については各 CVE ディレクトリを参照。
