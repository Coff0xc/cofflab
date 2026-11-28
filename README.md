**English** | [繁體中文](README.zh-TW.md)

# cofflab

![scope](https://img.shields.io/badge/scope-public%20PoC%20only-blue)

A curated collection of public PoCs for CVE and non-CVE vulnerabilities, maintained by Coff0xc. Each entry records the product, scores, and dates.

Only publicly available material is collected. For authorized security research and defense only.

---

<!-- categories:start -->
## Categories

- [Web / CMS (292)](categories/web.md)
- [AI / LLM (33)](categories/ai.md)
- [Network & Security (263)](categories/net.md)
- [Runtime / Framework / Browser (111)](categories/runtime.md)
- [Database (22)](categories/db.md)
- [OS / System / DevOps (76)](categories/os.md)
<!-- categories:end -->

## Catalog

### Web / CMS (292)

| ID | Product | Score | Affected | Fixed |
| --- | --- | --- | --- | --- |
| [CVE-2026-91618](CVE-2026-91618) | Oracle Application Development Framework (ADF) | 3.1 9.1 (Oracle) | Oracle Application Development Framework (ADF) 12.2.1.4.0 | November 2026 Critical Patch Update |
| [CVE-2026-40128](CVE-2026-40128) | SAP NetWeaver Application Server Java | 3.1 9.0 (SAP) | SAP NetWeaver Application Server Java (Web Container) | SAP Note 3727078 |
| [CVE-2026-61532](CVE-2026-61532) | Chamilo LMS | 3.1 9.0 (GHSA) | Chamilo LMS <1.11.40 and <2.0.3 | 1.11.40 / 2.0.3 |
| [CVE-2026-123488](CVE-2026-123488) | Craft CMS element search | 3.1 9.8 (GHSA / VulnCheck); 4.0 9.3 (GitHub Advisory Database) | 4.0.0–4.18.8 and 5.0.0–5.11.1 (MySQL/MariaDB, emulated PDO prepares) | 4.18.9 / 5.11.2 |
| [CVE-2026-129448](CVE-2026-129448) | Apache Roller XML-RPC | 3.1 9.8 (ingest curator README (unverified against Apache/NVD in this pass)) | Roller 4.0.0–6.1.4 (CVE-2026-82384 lists 6.1.5 only; same bug) | 6.1.6 |
| [CVE-2026-90817](CVE-2026-90817) | Vanderbilt REDCap | 3.1 9.8 (ingest curator README (unverified against vendor/NVD in this pass)) | REDCap 13.3.0+ before 16.0.49 LTS / 17.3.10 LTS / 17.4.4 | 16.0.49 LTS / 17.3.10 LTS / 17.4.4 |
| [CVE-2026-123751](CVE-2026-123751) | WP Duplicate | 3.1 9.8 (CISA-ADP) | WP Duplicate through 1.1.11 | unknown |
| [CVE-2026-126473](CVE-2026-126473) | OpenEMR | 4.0 9.3 (VulnCheck); 3.1 9.1 (VulnCheck) | OpenEMR < 8.4.0 (8.3.0 tested) | 8.4.0 |
| [CVE-2026-111559](CVE-2026-111559) | Batflat CMS | 4.0 9.3 (CERT.pl) | Batflat CMS 1.2.0–1.3.7 | none (project unmaintained) |
| [CVE-2026-126173](CVE-2026-126173) | AutomatorWP Pro Webhooks | 3.1 9.8 (Wordfence) | AutomatorWP Pro Webhooks <= 1.4.4 | 1.4.5 |
| [CVE-2026-48356](CVE-2026-48356) | Adobe Commerce / Magento | 3.1 9.3 (Adobe) | Adobe Commerce / Magento Open Source 2.4.4-2.4.9 | 2.4.9-p2 |
| [CVE-2026-119977](CVE-2026-119977) | WordPress Core | 3.1 8.1 (Wordfence) | WordPress Core 4.7.0-7.1.3 | 7.1.4 |
| [CVE-2026-110447](CVE-2026-110447) | Collabora Online CODE Server | 3.1 9.8 (NVD); 4.0 9.2 (MITRE) | Collabora Online Built-in CODE Server (richdocumentscode) before 26.4.303 | 26.4.303 |
| [CVE-2026-48907](CVE-2026-48907) | Joomla! JCE | 3.1 9.8 (NVD); 4.0 10.0 (Joomla) | Joomla! JCE extension < 2.9.99.5 | 2.9.99.5 |
| [CVE-2026-125423](CVE-2026-125423) | Gitea auto-init | 3.1 8.8 (NVD); 3.1 8.5 (GHSA) | Gitea before 28.4.0 (auto_init=true, Default README template) | 28.4.0 |
| [CVE-2026-63219](CVE-2026-63219) | GeoNetwork | 3.1 8.6 (GHSA) | GeoNetwork before 4.4.12 / 4.2.17 | 4.4.12 / 4.2.17 |
| [CVE-2026-58400](CVE-2026-58400) | GeoNetwork | 3.1 9.1 (GHSA) | GeoNetwork before 4.4.12 / 4.2.17 | 4.4.12 / 4.2.17 |
| [CVE-2026-128046](CVE-2026-128046) | OpenMage LTS | 4.0 9.2 (VulnCheck); 3.1 8.1 (VulnCheck) | OpenMage magento-lts 20.17.0 before 20.18.2 and 21.0.0-beta1 before 21.0.0-beta3 | 20.18.2 / 21.0.0-beta3 |
| [CVE-2026-69157](CVE-2026-69157) | atomic-server | 3.1 9.8 (GHSA) | atomic-server 0.29.0-0.40.1 (GHSA; NVD says to 0.40.2) |  |
| [CVE-2026-130648](CVE-2026-130648) | WWBN AVideo | 3.1 8.7 (GHSA); 4.0 9.3 (NVD) | WWBN AVideo from 6.5 (GHSA; no fixed version listed) |  |
| [CVE-2026-69158](CVE-2026-69158) | atomic-server | 3.1 8.6 (GHSA) | atomic-server <= 0.40.1 |  |
| [CVE-2026-69156](CVE-2026-69156) | atomic-server | 3.1 8.1 (GHSA) | atomic-server 0.30.0-0.40.1 |  |
| [CVE-2026-100397](CVE-2026-100397) | Rucio | 3.1 9.8 (GHSA) | Rucio server < 36.4.1 (per PoC; GHSA lists branch fixes 35.9.1 / 38.6.1 / 40.4.2 / 41.1.1) | 36.4.1 (per PoC); GHSA branches 35.9.1 / 38.6.1 / 40.4.2 / 41.1.1 |
| [CVE-2026-126967](CVE-2026-126967) | SmarterMail | 3.0 8.8 (GHSA) | SmarterMail all builds < 9735 | Build 9735 |
| [CVE-2026-71481](CVE-2026-71481) | altcha | 3.1 7.5 (GHSA) | altcha-org/altcha (Composer) >= 2.0.0, < 2.0.3 (GHSA; PoC claims altcha-lib <= 0.5.x) | 2.0.3 (GHSA); v0.6.0 (per PoC) |
| [CVE-2026-1492](CVE-2026-1492) | User Registration & Membership | 3.1 9.8 (Wordfence) | User Registration & Membership ≤ 5.1.2 | 5.1.3 |
| [CVE-2026-129493](CVE-2026-129493) | Bolo (bolo-solo) | 4.0 8.7 (VulnCheck) | Bolo (bolo-solo) 1.7–2.6.4 | none (unfixed upstream) |
| [CVE-2026-129494](CVE-2026-129494) | CloudPaste | 4.0 8.7 (VulnCheck) | CloudPaste 1.1.0–1.9.1 | none (unfixed upstream) |
| [CVE-2026-129492](CVE-2026-129492) | Bolo (bolo-solo) | 4.0 5.3 (VulnCheck) | Bolo (bolo-solo) 1.7–2.6.4 | none (unfixed upstream) |
| [CVE-2026-129491](CVE-2026-129491) | forum-java | 4.0 5.1 (VulnCheck) | forum-java 20f7e68–63152c4 | none (unfixed upstream) |
| [CVE-2026-130354](CVE-2026-130354) | phpMyFAQ | 4.0 6.9 (VulnCheck) | phpMyFAQ 4.1.0–4.1.11 | 4.1.12 |
| [CVE-2026-130347](CVE-2026-130347) | phpMyFAQ | 4.0 6.3 (VulnCheck) | phpMyFAQ before 4.1.12 (4.2.0-alpha before 4.2.0-RC.2) | 4.1.12 / 4.2.0-RC.2 |
| [CVE-2026-110960](CVE-2026-110960) | Auth Armor | 3.1 9.8 (GHSA) | Auth Armor ≤ 1.0.3 | unknown |
| [CVE-2026-126269](CVE-2026-126269) | NocoDB | 4.0 9.3 (VulnCheck); 3.1 8.7 (VulnCheck) | NocoDB < 2026.09.0 | 2026.09.0 |
| [CVE-2026-126274](CVE-2026-126274) | NocoDB | 4.0 9.3 (VulnCheck); 3.1 8.7 (VulnCheck) | NocoDB < 2026.08.1 | 2026.08.1 |
| [CVE-2026-126273](CVE-2026-126273) | NocoDB | 4.0 9.2 (VulnCheck); 3.1 8.1 (VulnCheck) | NocoDB < 2026.09.0 | 2026.09.0 |
| [CVE-2026-126937](CVE-2026-126937) | Zipline | 4.0 9.2 (VulnCheck); 3.1 8.1 (GHSA) | Zipline ≤ 4.6.4 | 4.6.5 |
| [CVE-2026-124020](CVE-2026-124020) | Control Web Panel | 4.0 9.2 (VulnCheck); 3.1 8.1 (GHSA) | CWP < 1.30.6 (CWP and CWPpro) | 1.30.6 |
| [CVE-2026-119258](CVE-2026-119258) | Swipe WordPress plugin | 3.1 8.1 (GHSA) | Swipe WordPress plugin <= 1.4 | no vendor patch at disclosure |
| [CVE-2026-100105](CVE-2026-100105) | Grafana | 3.1 7.7 (GHSA) | Grafana 12.4.0–12.4.13, 13.0.0–13.0.11, 13.1.0–13.1.8, 13.2.0–13.2.4 | 12.4.14 / 13.0.12 / 13.1.9 / 13.2.5 |
| [CVE-2026-129357](CVE-2026-129357) | Magma NMS | 4.0 2.1 (VulnDB); 3.1 6.3 (VulnDB) | Magma <= 1.9.0 | no upstream fix (synthetic remediation in lab) |
| [CVE-2026-131850](CVE-2026-131850) | ILIAS | 4.0 8.6 (VulnCheck) | ILIAS 11.0 - 11.5.x | 11.6 |
| [CVE-2026-13447](CVE-2026-13447) | MStore API | 3.1 9.8 (Wordfence) | MStore API <= 4.20.0 (lab 4.18.4) | 4.21.1 |
| [CVE-2026-13355](CVE-2026-13355) | Meta Box AIO | 3.1 9.8 (Wordfence) | Meta Box AIO <= 3.11.0; MB Frontend Submission <= 4.5.6; MB User Profile <= 3.11.0 | 3.12.0 |
| [CVE-2026-1357](CVE-2026-1357) | WPvivid Backup & Migration | 3.1 9.8 (Wordfence) | WPvivid Backup & Migration <= 0.9.123 | 0.9.124 |
| [CVE-2026-133117](CVE-2026-133117) | Product Feed for WooCommerce | 4.0 8.8 (VulnCheck); 3.1 8.2 (VulnCheck) | WebToffee Product Feed before 2.4.4 | 2.4.4 |
| [CVE-2026-133092](CVE-2026-133092) | TeamCity | 3.1 8.8 (JetBrains) | JetBrains TeamCity before 2026.2.2, 2026.1.6 | 2026.2.2 / 2026.1.6 |
| [CVE-2026-133086](CVE-2026-133086) | TeamCity | 3.1 8.8 (JetBrains) | JetBrains TeamCity before 2026.2.2, 2026.1.6 | 2026.2.2 / 2026.1.6 |
| [CVE-2026-133087](CVE-2026-133087) | TeamCity | 3.1 8.8 (JetBrains) | JetBrains TeamCity before 2026.2.2, 2026.1.6 | 2026.2.2 / 2026.1.6 |
| [CVE-2026-133172](CVE-2026-133172) | cozy-stack | 4.0 8.7 (VulnCheck); 3.1 8.8 (VulnCheck) | cozy-stack before 1.6.69 | 1.6.69 |
| [CVE-2026-133234](CVE-2026-133234) | stoatchat | 4.0 8.7 (VulnCheck); 3.1 7.5 (VulnCheck) | stoatchat before 0.16.5 | 0.16.5 |
| [CVE-2026-133235](CVE-2026-133235) | Tandoor Recipes | 4.0 8.3 (VulnCheck); 3.1 7.7 (VulnCheck) | Tandoor Recipes before 2.7.4 | 2.7.4 |
| [CVE-2026-133173](CVE-2026-133173) | WatchAlert | 4.0 7.1 (VulnCheck); 3.1 6.5 (VulnCheck) | WatchAlert 2.0.0 through 3.9.20 | 3.9.21 |
| [CVE-2026-133113](CVE-2026-133113) | Gogs | 4.0 7.1 (VulnCheck); 3.1 6.5 (VulnCheck) | Gogs through 0.14.4 | 0.14.5 |
| [CVE-2026-133114](CVE-2026-133114) | WooCommerce Side Cart | 4.0 5.3 (VulnCheck); 3.1 4.3 (VulnCheck) | Caddy WooCommerce Side Cart 3.0.0 before 3.2.1 | 3.2.1 |
| [CVE-2026-133080](CVE-2026-133080) | TeamCity | 3.1 8.8 (JetBrains) | JetBrains TeamCity before 2026.2.2, 2026.1.6 | 2026.2.2 / 2026.1.6 |
| [CVE-2026-133015](CVE-2026-133015) | TeamCity | 3.1 8.8 (JetBrains) | JetBrains TeamCity before 2026.2.1, 2026.1.5 | 2026.2.1 / 2026.1.5 |
| [CVE-2026-133016](CVE-2026-133016) | TeamCity | 3.1 8.8 (JetBrains) | JetBrains TeamCity before 2026.2.1, 2026.1.5 | 2026.2.1 / 2026.1.5 |
| [CVE-2026-133018](CVE-2026-133018) | TeamCity | 3.1 8.8 (JetBrains) | JetBrains TeamCity before 2026.2.1, 2026.1.5 | 2026.2.1 / 2026.1.5 |
| [CVE-2026-133019](CVE-2026-133019) | TeamCity | 3.1 8.8 (JetBrains) | JetBrains TeamCity before 2026.2.1, 2026.1.5 | 2026.2.1 / 2026.1.5 |
| [CVE-2026-133027](CVE-2026-133027) | TeamCity | 3.1 8.8 (JetBrains) | JetBrains TeamCity before 2026.2.1, 2026.1.5 | 2026.2.1 / 2026.1.5 |
| [CVE-2026-133089](CVE-2026-133089) | TeamCity | 3.1 8.1 (JetBrains) | JetBrains TeamCity before 2026.2.2, 2026.1.6 | 2026.2.2 / 2026.1.6 |
| [CVE-2026-22309](CVE-2026-22309) | JTL-Shop | 3.1 9.3 (JTL); 4.0 8.6 (JTL) | JTL-Shop 5.6.0-5.8.3 | 5.8.4 / 5.7.6 / 5.6.6 (2026-11-12) |
| [CVE-2026-91115](CVE-2026-91115) | silverstripe-framework | 3.1 8.8 (GHSA) | Silverstripe Framework 6.0.0-6.2.12 | 6.2.13 |
| [CVE-2026-133095](CVE-2026-133095) | TeamCity | 3.1 8.1 (JetBrains) | JetBrains TeamCity before 2026.2.2, 2026.1.6 | 2026.2.2 / 2026.1.6 |
| [CVE-2026-133017](CVE-2026-133017) | TeamCity | 3.1 8.0 (JetBrains) | JetBrains TeamCity before 2026.2.1, 2026.1.5 | 2026.2.1 / 2026.1.5 |
| [CVE-2026-72898](CVE-2026-72898) | Metabase | 3.1 10.0 (GHSA); 4.0 10.0 (GHSA) | Metabase 58.0-<58.24, 59.0-<59.21, 60.0-<60.17, 61.0-<61.11, 62.0-<62.9, 63.0-<63.5 | 58.24 / 59.21 / 60.17 / 61.11 / 62.9 / 63.5 |
| [CVE-2026-21962](CVE-2026-21962) | Oracle HTTP Server | 3.1 10.0 (Oracle) | Oracle HTTP Server 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0 | Oracle Critical Patch Update January 2026 |
| [CVE-2026-105899](CVE-2026-105899) | ColdFusion | 3.1 10.0 (Adobe) | Adobe ColdFusion 2025 before Update 14, 2023 before Update 26 | 2025 Update 14 / 2023 Update 26 (APSB26-144) |
| [CVE-2026-133083](CVE-2026-133083) | TeamCity | 3.1 8.0 (JetBrains) | JetBrains TeamCity before 2026.2.2, 2026.1.6 | 2026.2.2 / 2026.1.6 |
| [CVE-2026-133091](CVE-2026-133091) | TeamCity | 3.1 8.0 (JetBrains) | JetBrains TeamCity before 2026.2.2, 2026.1.6 | 2026.2.2 / 2026.1.6 |
| [CVE-2026-22310](CVE-2026-22310) | JTL-Shop | 3.1 8.0 (JTL); 4.0 7.6 (JTL) | JTL-Shop 5.5.0-5.8.3 | 5.8.4 / 5.7.6 / 5.6.6 / 5.5.5 (2026-11-11) |
| [CVE-2026-106622](CVE-2026-106622) | ColdFusion | 3.1 10.0 (Adobe) | Adobe ColdFusion 2025 before Update 14, 2023 before Update 26 | 2025 Update 14 / 2023 Update 26 (APSB26-144) |
| [CVE-2026-106624](CVE-2026-106624) | ColdFusion | 3.1 10.0 (Adobe) | Adobe ColdFusion 2025 before Update 14, 2023 before Update 26 | 2025 Update 14 / 2023 Update 26 (APSB26-144) |
| [CVE-2026-22308](CVE-2026-22308) | JTL-Shop | 3.1 9.3 (ENISA); 4.0 8.6 (ENISA) | JTL-Shop 5.0.0-5.8.3 | 5.8.4 / 5.7.6 / 5.6.6 / 5.5.5 (JTL advisory 2026-11-12) |
| [CVE-2026-130158](CVE-2026-130158) | RepoManager | 3.1 9.0 (GitHub) | RepoManager <5.13.3 | 5.13.3 |
| [CVE-2026-130236](CVE-2026-130236) | Auth0 Authorization Extension | 3.1 8.5 (Okta) | Auth0 Authorization Extension <2.13 | 2.13 |
| [CVE-2026-129048](CVE-2026-129048) | WP Photo Album Plus | 3.1 9.9 (Patchstack) | WP Photo Album Plus <=9.3.06.003 | 9.3.07.001 |
| [CVE-2026-14492](CVE-2026-14492) | WP Duplicate – WordPress Migration Plugin | 3.1 9.8 (Wordfence) | WP Duplicate <=1.1.11 | No known patch |
| [CVE-2026-130754](CVE-2026-130754) | LaraDashboard | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | LaraDashboard <=1.5.4 | No fix released (latest 1.5.4) |
| [CVE-2023-54422](CVE-2023-54422) | iDocView | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | iDocView <13.10.1_20231115 | 13.10.1_20231115 |
| [CVE-2023-54419](CVE-2023-54419) | nginxWebUI | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | nginxWebUI 3.0.0-3.5.7 | 3.5.8 |
| [CVE-2022-51027](CVE-2022-51027) | MeterSphere | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | MeterSphere 1.13.0-1.14.6 / 1.15.0-1.16.3 | 1.14.7 / 1.16.4 |
| [CVE-2021-48025](CVE-2021-48025) | OpenSNS | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | OpenSNS 3.2.1 | No known patch |
| [CVE-2021-48023](CVE-2021-48023) | Weaver E-cology | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | Weaver E-cology 9.0 | No known patch |
| [CVE-2018-25443](CVE-2018-25443) | Baidu UEditor | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | Baidu UEditor 1.4.0-1.4.3.3 | No known patch |
| [CVE-2026-114516](CVE-2026-114516) | Etherpad | 3.1 9.8 (GHSA) | Etherpad 1.8.14-3.3.2 | 3.3.3 |
| [CVE-2026-77369](CVE-2026-77369) | Daptin | 3.1 9.6 (GHSA) | Daptin 0.11.4-0.12.29 | 0.12.30 |
| [CVE-2026-71499](CVE-2026-71499) | cf-manager | 3.1 10 (GHSA) | cf-manager <1.1.2 | 1.1.2 |
| [CVE-2026-77367](CVE-2026-77367) | Daptin | 3.1 9.4 (GHSA) | Daptin <0.12.30 | 0.12.30 |
| [CVE-2026-123058](CVE-2026-123058) | JTL-Shop | 4.0 9.2 (ENISA); 3.1 9 (ENISA) | JTL-Shop 5.5.0-5.5.4 / 5.6.0-5.6.5 / 5.7.0-5.7.5 / 5.8.0-5.8.3 | 5.5.5 / 5.6.6 / 5.7.6 / 5.8.4 |
| [CVE-2026-110009](CVE-2026-110009) | Unzer Payments | 3.1 9.8 (Wordfence) | Unzer Payments <=2.2.1 | 無已知補丁（Wordfence 2026-11-18：Patched? No） |
| [CVE-2026-110811](CVE-2026-110811) | Trust Payments Gateway for WooCommerce (JavaScript Library) | 3.1 9.8 (Wordfence) | Trust Payments Gateway for WooCommerce (JavaScript Library) <=1.3.8 | 無已知補丁（Wordfence 2026-11-18：Patched? No） |
| [CVE-2026-124990](CVE-2026-124990) | Masteriyo LMS – LMS Course Builder, Quizzes & Certificates | 3.1 9.8 (Wordfence) | Masteriyo LMS <=3.5.1 | 3.5.2 |
| [CVE-2026-130735](CVE-2026-130735) | Grav | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | Grav 2.0.0 to <2.2.18 | 2.2.18 |
| [CVE-2026-55506](CVE-2026-55506) | Wavelog | 3.1 9.6 (GHSA) | Wavelog <2.5 | 2.5 |
| [CVE-2026-130156](CVE-2026-130156) | Bazarr | 3.1 9.4 (GHSA) | Bazarr <1.6.3-beta.11 | 1.6.3-beta.11 |
| [CVE-2026-55508](CVE-2026-55508) | Wavelog | 3.1 9.4 (GHSA) | Wavelog <2.5 | 2.5 |
| [CVE-2026-130160](CVE-2026-130160) | RepoManager | 3.1 8.8 (GHSA) | RepoManager <5.13.3 | 5.13.3 |
| [CVE-2026-132906](CVE-2026-132906) | TeamCity | 3.1 8.8 (JetBrains) | TeamCity <2026.2 / <2026.1.4 / <2025.11.8 | 2026.2 / 2026.1.4 / 2025.11.8 |
| [CVE-2026-132909](CVE-2026-132909) | TeamCity | 3.1 8.8 (JetBrains) | TeamCity <2026.2 / <2026.1.4 / <2025.11.8 | 2026.2 / 2026.1.4 / 2025.11.8 |
| [CVE-2026-132917](CVE-2026-132917) | TeamCity | 3.1 8.8 (JetBrains) | TeamCity <2026.2 / <2026.1.4 / <2025.11.8 | 2026.2 / 2026.1.4 / 2025.11.8 |
| [CVE-2026-133476](CVE-2026-133476) | Dolibarr | 3.1 8.8 (MITRE) | Dolibarr <24.0.3 | 24.0.3 |
| [CVE-2026-125061](CVE-2026-125061) | JTL PayPal Checkout plugin | 4.0 8.5 (JTL); 3.1 8.7 (JTL) | JTL PayPal Checkout plugin 1.2.0–2.3.1 | 2.3.2 / 2.2.2 |
| [CVE-2026-122676](CVE-2026-122676) | PublishPress Authors | 3.1 8.5 (Patchstack) | PublishPress Authors <=4.18.0 | 4.20.0 |
| [CVE-2026-132913](CVE-2026-132913) | TeamCity | 3.1 8.4 (JetBrains) | TeamCity <2026.2 / <2026.1.4 / <2025.11.8 | 2026.2 / 2026.1.4 / 2025.11.8 |
| [CVE-2026-103035](CVE-2026-103035) | TeamPass | 3.1 8.3 (GHSA) | TeamPass <3.2.1.2 | 3.2.1.2 |
| [CVE-2026-125060](CVE-2026-125060) | JTL-Shop | 4.0 8.8 (JTL); 3.1 8.2 (JTL) | JTL-Shop 5.2.0–5.8.3 | 5.8.4 / 5.7.6 / 5.6.6 / 5.5.5 |
| [CVE-2026-59988](CVE-2026-59988) | django-docutils | 3.1 8.2 (GHSA) | django-docutils <0.30.0 | 0.30.0 |
| [CVE-2026-103026](CVE-2026-103026) | Paymenter | 3.1 8.1 (GHSA) | Paymenter <1.5.7 | 1.5.7 |
| [CVE-2026-132892](CVE-2026-132892) | TeamCity | 3.1 8.1 (JetBrains) | TeamCity <2026.2 | 2026.2 |
| [CVE-2026-132907](CVE-2026-132907) | TeamCity | 3.1 8.1 (JetBrains) | TeamCity <2026.2 / <2026.1.4 / <2025.11.8 | 2026.2 / 2026.1.4 / 2025.11.8 |
| [CVE-2026-129056](CVE-2026-129056) | Authorizer | 3.1 9.8 (Patchstack) | Authorizer <3.17.2 | 3.17.2 |
| [CVE-2026-89095](CVE-2026-89095) | Shortcodes and extra features for Phlox theme | 3.1 8.1 (Wordfence) | Shortcodes and extra features for Phlox theme <=2.17.22 | 2.17.24 |
| [CVE-2026-120556](CVE-2026-120556) | Toocheke Companion | 3.1 8.1 (Wordfence) | Toocheke Companion <=2.38 | 2.39 |
| [CVE-2026-131795](CVE-2026-131795) | Aora | 3.1 8.1 (Patchstack) | Aora <=1.3.5 | 1.3.24 |
| [CVE-2026-132903](CVE-2026-132903) | TeamCity | 3.1 8.1 (JetBrains) | TeamCity <2026.2 / <2026.1.4 / <2025.11.8 | 2026.2 / 2026.1.4 / 2025.11.8 |
| [CVE-2026-109555](CVE-2026-109555) | WP STAGING / WP STAGING Pro | 3.1 8.0 (Wordfence) | WP STAGING <=4.17.0 / WP STAGING Pro <=6.17.0 | 4.18.0 / 6.18.0 |
| [CVE-2026-132914](CVE-2026-132914) | TeamCity | 3.1 8.0 (JetBrains) | TeamCity <2026.2 / <2026.1.4 / <2025.11.8 | 2026.2 / 2026.1.4 / 2025.11.8 |
| [CVE-2026-133500](CVE-2026-133500) | Gladys Assistant | 4.0 8.5 (VulDB); 3.1 9.1 (VulDB) | Gladys Assistant <=4.71.0 | 4.72.0 |
| [CVE-2026-133501](CVE-2026-133501) | Gladys Assistant | 4.0 8.5 (VulDB); 3.1 9.0 (VulDB) | Gladys Assistant <=4.71.0 | 4.72.0 |
| [CVE-2026-128915](CVE-2026-128915) | InstaWP Connect | 3.1 8.5 (Patchstack) | InstaWP Connect <=0.1.4.4 | 0.1.4.5 |
| [CVE-2026-130010](CVE-2026-130010) | Chatterbug Forms | 3.1 8.1 (Wordfence) | Chatterbug Forms <=1.1 | 1.2 |
| [CVE-2026-120681](CVE-2026-120681) | Mang Board | 3.1 9.1 (Wordfence) | Mang Board <=2.4.7 | 2.4.8 |
| [CVE-2026-125085](CVE-2026-125085) | Nexter Extension | 3.1 8.8 (Wordfence) | Nexter Extension <=4.9.0 | 4.9.1 |
| [CVE-2026-118522](CVE-2026-118522) | Video & Photo Gallery for Ultimate Member | 3.1 8.1 (Wordfence) | Video & Photo Gallery for Ultimate Member <=1.1.4 | 1.1.5 |
| [CVE-2026-126716](CVE-2026-126716) | Mega Forms | 3.1 8.1 (Wordfence) | Mega Forms <=1.7.9 | 1.8.0 |
| [CVE-2026-129073](CVE-2026-129073) | miniorange-otp-verification | 3.1 9.8 (Patchstack) | miniorange-otp-verification <=5.6.1 | 5.6.2 |
| [CVE-2026-15826](CVE-2026-15826) | User Profile Builder | 3.1 9.8 (Wordfence) | User Profile Builder <=3.16.4 | 3.16.5 |
| [CVE-2026-129039](CVE-2026-129039) | Newsletters | 3.1 9.8 (Patchstack) | Newsletters <= 4.18.2 | 4.18.3 |
| [CVE-2026-129043](CVE-2026-129043) | Newsletters | 3.1 9.3 (Patchstack) | Newsletters <= 4.18.2 | 4.18.3 |
| [CVE-2026-14914](CVE-2026-14914) | Tegsoft Contact Center | 3.1 10.0 (USOM) | Tegsoft Contact Center before latest-202611161510 | latest-202611161510 |
| [CVE-2026-80188](CVE-2026-80188) | BuddyBoss Addons | 3.1 9.8 (Wordfence) | BuddyBoss Addons <= 1.2.1 | 1.2.2 |
| [CVE-2025-42884](CVE-2025-42884) | SAP NetWeaver Enterprise Portal | 3.1 6.5 (SAP) | SAP NetWeaver Enterprise Portal EP-BASIS 7.50 / EP-RUNTIME 7.50 | Per SAP Note 3660969 |
| [CVE-2026-128049](CVE-2026-128049) | OpenMage Magento LTS | 4.0 9.4 (VulnCheck); 3.1 9.0 (VulnCheck) | OpenMage Magento LTS before 20.18.2; 21.0.0-beta1 before 21.0.0-beta3 | 20.18.2 / 21.0.0-beta3 |
| [CVE-2026-126380](CVE-2026-126380) | Vvveb CMS | 4.0 9.4 (VulnCheck); 3.1 9.1 (VulnCheck) | Vvveb before 1.0.9.0 | 1.0.9.0 |
| [CVE-2026-94565](CVE-2026-94565) | NukeViet CMS | 3.1 9.3 (GHSA) | NukeViet CMS 3.x through 4.6.01 (Contact module) | 4.6.01 |
| [CVE-2026-94567](CVE-2026-94567) | NukeViet CMS | 3.1 9.3 (GHSA) | NukeViet CMS before 4.5.12 and 4.6.02 (SVG upload) | 4.5.12 / 4.6.02 |
| [CVE-2026-94598](CVE-2026-94598) | NukeViet CMS | 3.1 8.2 (GHSA) | NukeViet CMS 4.5.08 through 4.5.12 and 4.6.02 (iframe srcdoc) | 4.5.12 / 4.6.02 |
| [CVE-2026-54064](CVE-2026-54064) | NukeViet CMS | 3.1 8.7 (GHSA) | NukeViet CMS before 4.5.09 (news posting) | 4.5.09 |
| [CVE-2026-54065](CVE-2026-54065) | NukeViet CMS | 3.1 8.7 (GHSA) | NukeViet CMS before 4.5.09 (comment admin edit) | 4.5.09 |
| [CVE-2026-77326](CVE-2026-77326) | MapServer | 3.1 8.6 (GHSA) | MapServer 8.2.0 through 8.6.5 (WMS GetLegendGraphic) | 8.6.5 |
| [CVE-2026-94564](CVE-2026-94564) | NukeViet CMS | 3.1 8.2 (GHSA) | NukeViet CMS before 4.6.01 (Contact module) | 4.6.01 |
| [CVE-2026-133874](CVE-2026-133874) | Iceburg CRM | 4.0 8.6 (VulnCheck); 3.1 8.1 (VulnCheck) | Iceburg CRM through 5.0.0 | No known patch |
| [CVE-2026-120539](CVE-2026-120539) | Restrictions for BuddyPress | 3.1 9.8 (NVD) | <= 1.5.4 (requires BuddyPress and Paid Memberships Pro both active) | 1.5.5 |
| [CVE-2026-3300](CVE-2026-3300) | Everest Forms Pro | 3.1 9.8 (NVD) | <= 1.9.12 (requires Calculation Addon / Complex Calculation enabled) |  |
| [CVE-2026-131754](CVE-2026-131754) | APCu Manager | 3.1 9.8 (NVD) | APCu Manager through 4.6.1 |  |
| [CVE-2026-131782](CVE-2026-131782) | Simple Shopping Cart | 3.1 9.8 (NVD) | Simple Shopping Cart through 5.3.3 |  |
| [CVE-2026-129175](CVE-2026-129175) | Unstable Slope Management Program | 3.1 9.8 (CISA); 4.0 9.3 (CISA) | Unstable Slope Management Program (version not specified in NVD/GHSA) | Fixed on or around 2026-10-19 (per NVD) |
| [CVE-2026-132165](CVE-2026-132165) | Drupal core | unknown | Drupal core <10.6.22, 11.0.0-11.3.21, 11.4.0-11.4.12 | 10.6.22 / 11.3.22 / 11.4.13 |
| [CVE-2026-125294](CVE-2026-125294) | Nexter Blocks Pro | 3.1 9.8 (Wordfence) | Nexter Blocks Pro up to and including 5.0.10 |  |
| [CVE-2026-134433](CVE-2026-134433) | Frappe ERPNext | 4.0 8.4 (VulnCheck); 3.1 8.5 (VulnCheck) | ERPNext before 15.124.2 and 16.x before 16.53.0 | 15.124.2 / 16.53.0 |
| [CVE-2026-134448](CVE-2026-134448) | Dockhand | 4.0 8.6 (VulnCheck); 3.1 8.1 (VulnCheck) | Dockhand 1.0.7 before 1.0.57 | 1.0.57 |
| [CVE-2026-134451](CVE-2026-134451) | Dockhand | 4.0 8.6 (VulnCheck); 3.1 8.1 (VulnCheck) | Dockhand before 1.0.57 | 1.0.57 |
| [CVE-2026-134452](CVE-2026-134452) | Dockhand | 4.0 8.7 (VulnCheck); 3.1 8.8 (VulnCheck) | Dockhand before 1.0.57 | 1.0.57 |
| [CVE-2026-134258](CVE-2026-134258) | Admidio | 4.0 9.3 (VulnCheck); 3.1 8.7 (VulnCheck) | Admidio 5.0.0 before 5.0.18 | 5.0.18 |
| [CVE-2026-134262](CVE-2026-134262) | Admidio | 4.0 9.2 (VulnCheck); 3.1 8.1 (VulnCheck) | Admidio 5.0.0 before 5.0.18 | 5.0.18 |
| [CVE-2026-134250](CVE-2026-134250) | Grav Form plugin | 4.0 8.8 (VulnCheck); 3.1 8.0 (VulnCheck) | Grav Form plugin 1.1.0 before 9.1.40 | 9.1.40 |
| [CVE-2026-134253](CVE-2026-134253) | Grav API plugin | 4.0 8.7 (VulnCheck); 3.1 8.8 (VulnCheck) | Grav API plugin 1.0.0 before 1.1.4 | 1.1.4 |
| [CVE-2026-134282](CVE-2026-134282) | Vikunja | 4.0 8.6 (VulnCheck); 3.1 8.1 (VulnCheck) | Vikunja 0.14.0 before 2.8.0 | 2.8.0 |
| [CVE-2026-134316](CVE-2026-134316) | @better-auth/electron | 4.0 8.6 (VulnCheck); 3.1 8.1 (VulnCheck) | 1.5.0-beta.12 before 1.7.16 and 1.8.0-beta.0 before 1.8.0-beta.5 | 1.7.16 / 1.8.0-beta.5 |
| [CVE-2026-134322](CVE-2026-134322) | better-auth | 4.0 8.6 (VulnCheck); 3.1 8.1 (VulnCheck) | 0.4.12-beta.7 before 1.7.16 and 1.8.0-beta.0 before 1.8.0-beta.5 | 1.7.16 / 1.8.0-beta.5 |
| [CVE-2026-134654](CVE-2026-134654) | Mailflare | 4.0 8.6 (VulnCheck); 3.1 8.1 (VulnCheck) | Mailflare before 48957fb | 48957fb |
| [CVE-2026-129024](CVE-2026-129024) | Everest Forms | 3.1 8.6 (Patchstack) | Everest Forms through 3.6.4 |  |
| [CVE-2026-131701](CVE-2026-131701) | WP Media Folder | 3.1 8.5 (Patchstack) | WP Media Folder through 6.2.8 |  |
| [CVE-2026-131705](CVE-2026-131705) | ProfileGrid | 3.1 8.5 (Patchstack) | ProfileGrid through 6.0.0.6 |  |
| [CVE-2026-131707](CVE-2026-131707) | ProfileGrid | 3.1 8.8 (Patchstack) | ProfileGrid through 6.0.0.6 |  |
| [CVE-2026-131750](CVE-2026-131750) | Everest Forms | 3.1 8.6 (Patchstack) | Everest Forms through 3.6.4 |  |
| [CVE-2026-134804](CVE-2026-134804) | Portainer | 3.1 8.8 (VulnCheck); 4.0 8.7 (VulnCheck) | Portainer 2.39.0 before 2.39.9, 2.40.0 before 2.45.4, 3.0.0 before 3.1.0 | 2.39.9 / 2.45.4 / 3.1.0 |
| [CVE-2026-134836](CVE-2026-134836) | Dashy | 3.1 8.1 (VulnCheck); 4.0 8.6 (VulnCheck) | Dashy 4.0.0 before 4.9.12 | 4.9.12 |
| [CVE-2026-135157](CVE-2026-135157) | Future AGI | 4.0 8.6 (VulnCheck); 3.1 8.1 (VulnCheck) | Future AGI before 1.51.0 | 1.51.0 |
| [CVE-2026-135161](CVE-2026-135161) | Interstellar | 4.0 9.2 (VulnCheck); 3.1 8.6 (VulnCheck) | Interstellar before 6.3.0 | 6.3.0 |
| [CVE-2026-135164](CVE-2026-135164) | Formance Ledger | 4.0 8.7 (VulnCheck); 3.1 8.8 (VulnCheck) | Formance Ledger 2.2.0-beta.3 before 2.4.18 | 2.4.18 |
| [CVE-2026-135208](CVE-2026-135208) | Kerberos Agent | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | Kerberos Agent before 3.14.4 | 3.14.4 |
| [CVE-2026-135174](CVE-2026-135174) | Softaculous Virtualizor | 4.0 9.2 (VulnCheck); 3.1 8.1 (VulnCheck) | Softaculous Virtualizor before 3.2.9 | 3.2.9 |
| [CVE-2026-133469](CVE-2026-133469) | Xen Orchestra | 3.1 9.8 (GHSA) | Xen Orchestra before 6.9.2 / 6.10.1 | 6.9.2 / 6.10.1 |
| [CVE-2026-135429](CVE-2026-135429) | Tabbycat | 4.0 8.8 (VulnCheck); 3.1 9.1 (VulnCheck) | Tabbycat 2.9.0 through 2.12.1 |  |
| [CVE-2026-135436](CVE-2026-135436) | KindleEar | 4.0 8.7 (VulnCheck); 3.1 8.8 (VulnCheck) | KindleEar 3.0.0 through 3.5.3 |  |
| [CVE-2026-95793](CVE-2026-95793) | HPE Morpheus Manager | 3.1 8.8 (HPE) | HPE Morpheus Software 9.1.0-2 and earlier, 9.0.2-3 and earlier, 8.1.2-2 and earlier | 9.1.0-3 / 9.0.2-4 / 8.1.2-3 |
| [CVE-2026-41940](CVE-2026-41940) | cPanel & WHM | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | cPanel & WHM < 11.136.0.5 | 11.136.0.5 |
| [CVE-2026-60137](CVE-2026-60137) | WordPress | 3.1 5.9 (WPScan) | WordPress 6.8.0-6.8.5 (SQL injection); 6.9.x / 7.0.x reachable unauthenticated only via CVE-2026-63030 | 6.8.6 / 6.9.5 / 7.0.2 |
| [CVE-2026-63030](CVE-2026-63030) | WordPress | 3.1 9.8 (WPScan) | WordPress 6.9.0-6.9.4 and 7.0.0-7.0.1 | 6.9.5 / 7.0.2 |
| [CVE-2026-109490](CVE-2026-109490) | Authentication Methods Portal Extension | 3.1 9.3 (Microsoft) | Authentication Methods Portal Extension |  |
| [CVE-2026-113824](CVE-2026-113824) | Microsoft Clarity | 3.1 9.1 (Microsoft) | Microsoft Clarity |  |
| [CVE-2026-135202](CVE-2026-135202) | WP connect WordPress plugins | 3.1 9.8 (Wordfence) | WP connect 插件所列版本：Orders Sync to Airtable for WooCommerce、Add-On for Contact Form 7 to Notion、WP Sync for Notion、Add-On for Contact Form 7 to Airtable、Add-on Brevo for Gravity Forms、Air WP Sync |  |
| [CVE-2026-70193](CVE-2026-70193) | Microsoft Office SharePoint | 3.1 9.9 (Microsoft) | Microsoft Office SharePoint |  |
| [CVE-2026-70305](CVE-2026-70305) | Azure Portal | 3.1 9.6 (Microsoft) | Azure Portal |  |
| [CVE-2026-93700](CVE-2026-93700) | WHMCS | 3.1 9.0 (HackerOne) | WHMCS 8.0.0 and later: 9.1.x before 9.1.2; 9.0.x before 9.0.10; 8.x.x before 8.13.8 | 9.1.2 / 9.0.10 / 8.13.8 |
| [CVE-2026-83542](CVE-2026-83542) | Apache OFBiz | 3.1 9.8 (CISA-ADP) | Apache OFBiz 24.09 before 24.09.08 | 24.09.08 |
| [CVE-2026-131914](CVE-2026-131914) | Idunno.AntiCsrf | 4.0 9.3 (Mandiant) | Idunno.AntiCsrf through 0.9.1 Beta (0.9.1.0) on ASP.NET WebForms | No fix; remove Idunno.AntiCsrf.dll and replace with a supported anti-CSRF mechanism |
| [CVE-2026-129514](CVE-2026-129514) | hexpm | 4.0 10.0 (EEF) | hexpm/hexpm from ab1bbcef7cc8395d1056d3b1aa6a174353492d59 before 379b0a29bcc95164249f38ad7d772a37a8ff9533 (hex.pm service affected from 2016-02-23) | 379b0a29bcc95164249f38ad7d772a37a8ff9533 (deployed to hex.pm 2026-11-23 18:30-18:31 UTC) |
| [CVE-2026-87902](CVE-2026-87902) | WordPress Core | 3.1 8.1 (WordPress) | WordPress 7.1.1 and earlier (all branches) | 7.1.2; fix backported to all branches back to 4.7 |
| [CVE-2026-132224](CVE-2026-132224) | Web Experimentation | 4.0 7.1 (MITRE) | Optimizely Web Experimentation before 2026-11-17 | 2026-11-17 (vendor-side fix; no customer patch to install) |
| [CVE-2026-129242](CVE-2026-129242) | GeoServer | 4.0 8.6 (GHSA) | GeoServer <= 2.27.6, 2.28.0-2.28.5, 3.0.0-3.0.1 | 2.27.7, 2.28.6, 3.0.2 |
| [CVE-2026-109384](CVE-2026-109384) | IvyForms WordPress plugin | 3.1 8.8 (Wordfence) | IvyForms <= 1.5.1 | 1.5.2 |
| [CVE-2026-122247](CVE-2026-122247) | Budibase | 3.1 8.2 (GHSA) | Budibase < 3.50.0 | 3.50.0 (and 4.0.0) |
| [CVE-2026-107904](CVE-2026-107904) | Easy File Uploader (Joomla extension) | 3.1 9.8 (CISA-ADP) | Easy File Uploader < 2.9.7 | 2.9.7 |
| [CVE-2026-128981](CVE-2026-128981) | Apache SeaTunnel Web | 3.1 9.8 (CISA-ADP) | Apache SeaTunnel Web 1.0.2 | None — component unsupported / unmaintained |
| [CVE-2026-135175](CVE-2026-135175) | ZITADEL | 4.0 8.6 (VulnCheck); 3.1 8.1 (VulnCheck) | ZITADEL 4.19.5–4.20.2 | 4.20.3 |
| [CVE-2026-133335](CVE-2026-133335) | VirtueMart | 4.0 9.2 (Joomla) | VirtueMart extension 4.0.0-4.8.7 | 4.8.8 |
| [CVE-2026-129968](CVE-2026-129968) | LiteSpeed Cache Plugin for PrestaShop | 4.0 9.3 (CERT Polska) | LiteSpeed Cache Plugin for PrestaShop (litespeedcache module) before 1.6.2 | 1.6.2 (released 2026-10-30) |
| [CVE-2026-35273](CVE-2026-35273) | Oracle PeopleSoft Enterprise PeopleTools | 3.1 9.8 (Oracle) | PeopleSoft Enterprise PeopleTools 8.61, 8.62 | Oracle Security Alert 補丁（2026-06-10） |
| [CVE-2026-123214](CVE-2026-123214) | Joomla! CMS | 4.0 9.2 (Joomla) | Joomla! CMS 4.0.0–5.4.10, 6.0.0–6.2.0 | 5.4.11 / 6.2.1 |
| [CVE-2026-134838](CVE-2026-134838) | Weblate | 4.0 9.1 (VulnCheck); 3.1 7.4 (VulnCheck) | Weblate before 2026.11 | 2026.11 |
| [CVE-2026-135163](CVE-2026-135163) | Okou | 4.0 9.1 (VulnCheck); 3.1 7.4 (VulnCheck) | Okou API before 1.762.0 | 1.762.0 |
| [CVE-2026-21589](CVE-2026-21589) | Atlassian Data Center | 4.0 9.3 (Atlassian); 3.1 7.5 (NVD) | All versions of Bitbucket Data Center, Confluence Data Center, Jira Software Data Center, Jira Service Management Data Center, Bamboo Data Center, Crowd Data Center, Crucible, Fisheye (before the fixed versions) | Bitbucket 9.4.26 / 10.2.8 / 10.5.1; Confluence 9.2.26 / 10.2.19; Jira Software 9.12.40 / 10.3.26 / 11.3.12; Jira Service Management 5.12.40 / 10.3.26 / 11.3.12; Bamboo 10.2.24 / 12.1.12; Crowd 6.3.7 / 7.0.3 / 7.1.7 / 7.2.4; Crucible 4.9.15; Fisheye 4.9.15 |
| [CVE-2026-49952](CVE-2026-49952) | Discuz! X5.0 | 4.0 9.3 (VulnCheck); 3.1 9.1 (VulnCheck) | Discuz! X5.0 >= 20260320, <= 20260501 |  |
| [CVE-2026-75650](CVE-2026-75650) | Adobe Commerce / Magento Open Source | 3.1 10.0 (Adobe) | Adobe Commerce 2.4.4-2.4.9 (2026-aug and earlier); Adobe Commerce B2B 1.3.3-1.5.3 (2026-aug and earlier); Magento Open Source 2.4.6-2.4.9 (2026-aug and earlier) | Hotfix VULN-39341 (APSB26-146) |
| [CVE-2026-136716](CVE-2026-136716) | Drupal core | unknown | Drupal core <10.6.23, 11.0.0-11.3.22, 11.4.0-11.4.13 | 10.6.23 / 11.3.23 / 11.4.14 |
| [CVE-2024-27923](CVE-2024-27923) | Grav CMS | 3.1 8.8 (GHSA) | Grav < 1.7.43 | 1.7.43 |
| [CVE-2026-117593](CVE-2026-117593) | ITG vSRM | 3.1 9.1 (TR-CERT) | vSRM v14.08.3 至 v14.08.5 之前版本 | v14.08.5 |
| [CVE-2026-119582](CVE-2026-119582) | ITG vSRM | 3.1 9.8 (TR-CERT) | vSRM v14.08.3 至 v14.08.5 之前版本 | v14.08.5 |
| [CVE-2026-125812](CVE-2026-125812) | WP Rocket | 3.1 9.8 (Patchstack) | WP Rocket < 3.24.2 | 3.24.2 |
| [CVE-2026-73373](CVE-2026-73373) | Joomla! CMS | 3.1 9.8 (NVD); 4.0 8.9 (Joomla) | Joomla! CMS 1.0.0–5.4.7、6.0.0–6.1.2 | 5.4.8 / 6.1.3 |
| [CVE-2026-82329](CVE-2026-82329) | JFrog Artifactory | 3.1 9.8 (JFrog) | Artifactory 7.111.4–7.111.20 / 7.117.0–7.117.27 / 7.125.0–7.125.19 / 7.133.0–7.133.28 / 7.146.0–7.146.36 / 7.161.0–7.161.19（自託管；Cloud 不受影響） | 7.111.21 / 7.117.28 / 7.125.20 / 7.133.29 / 7.146.38 / 7.161.20 |
| [CVE-2016-3081](CVE-2016-3081) | Apache Struts | 3.1 8.1 (CISA-ADP) | Struts 2.3.19–2.3.20.2、2.3.21–2.3.24.1、2.3.25–2.3.28（啟用 Dynamic Method Invocation 時） | 2.3.20.3 / 2.3.24.3 / 2.3.28.1 |
| [CVE-2021-3199](CVE-2021-3199) | ONLYOFFICE Document Server | 3.1 9.8 (CISA-ADP) | ONLYOFFICE Document Server 5.6.3 之前（啟用 JWT 時，/upload 經圖片上傳參數） | 5.6.3 |
| [CVE-2023-22894](CVE-2023-22894) | Strapi | 3.1 7.2 (CISA-ADP); 3.1 4.9 (NVD) | Strapi 3.2.1–4.5.5（原始描述；NVD CPE 範圍為 3.2.1 至 4.8.0 之前） | 4.8.0 |
| [CVE-2026-102489](CVE-2026-102489) | Zammad | 4.0 9.4 (DIVD); 3.1 9.8 (NVD) | Zammad 6.3.0–6.5.4（7.0.0–7.1.2 含缺陷但因框架變更不可利用；廠商稱 7.0 及以上不受影響） | 無修復版本（6.5 及更早版本已停止支援、不再接收安全更新；7.0 及以上不受影響；7.2.0 含額外加固） |
| [GHSA-7wwv-x6mc-pxqx](GHSA-7wwv-x6mc-pxqx) | TastyIgniter | 3.1 9.1 (GHSA) | tastyigniter/tastyigniter <= v4.2.4 | v4.3.1 |
| [CVE-2026-137305](CVE-2026-137305) | Grav Form plugin | 3.1 8.8 (VulnCheck); 4.0 8.7 (VulnCheck) | Grav Form plugin <= 9.2.3 (before 9.2.4) | 9.2.4 |
| [GHSA-743w-g9pf-8p94](GHSA-743w-g9pf-8p94) | TastyIgniter | 3.1 9.1 (GHSA) | tastyigniter/tastyigniter <= v4.2.4 | v4.3.1 |
| [CVE-2026-64670](CVE-2026-64670) | @waline/client | 3.1 9.3 (GHSA) | @waline/client <= 3.15.2 | No fixed release yet |
| [GHSA-2grc-qr7q-6m36](GHSA-2grc-qr7q-6m36) | Gogs | 3.1 9.6 (GHSA) | Gogs <= 0.14.3 | 0.14.4 |
| [GHSA-hc35-pcqw-5xjq](GHSA-hc35-pcqw-5xjq) | Gogs | 3.1 9.9 (GHSA) | Gogs <= 0.14.3 | No fixed release yet |
| [GHSA-rj59-9f77-mvg5](GHSA-rj59-9f77-mvg5) | TastyIgniter | 3.1 7.6 (GHSA) | tastyigniter/tastyigniter < 4.3.1 | v4.3.1 |
| [CVE-2026-133336](CVE-2026-133336) | ChronoForms | 4.0 9.5 (Joomla) | ChronoForms 8.0.0–8.0.53 | 8.0.54 |
| [CVE-2026-63305](CVE-2026-63305) | AVideo | 4.0 9.2 (VulnCheck); 3.1 8.1 (VulnCheck) | AVideo < 29.1.0 | 29.1.0 |
| [CVE-2026-64855](CVE-2026-64855) | soapbar | 3.1 8.2 (GHSA) | soapbar < 0.13.0 | 0.13.0 |
| [CVE-2026-65971](CVE-2026-65971) | livewire-powergrid | 3.1 7.6 (GHSA) | power-components/livewire-powergrid >= 6.0.0, < 6.10.4 | 6.10.4 |
| [CVE-2026-77806](CVE-2026-77806) | SPIP | 3.1 9.8 (NVD) | SPIP < 4.4.21 | 4.4.21 |
| [CVE-2026-59191](CVE-2026-59191) | TwigView | 4.0 6.9 (GHSA) | twig-view < 1.3.3；2.0.0–2.1.1 | 1.3.3 / 2.1.2 |
| [CVE-2026-61500](CVE-2026-61500) | Rejetto HFS | 3.1 9.8 (GHSA) | HFS 3.0.0–3.2.0 | 3.2.1 |
| [CVE-2026-115770](CVE-2026-115770) | Pocket ID | 3.1 9.6 (GHSA) | Pocket ID >= 2.2.0, < 2.12.0 | 2.12.0 |
| [CVE-2026-137306](CVE-2026-137306) | Grav Admin plugin | 4.0 7.6 (VulnCheck); 3.1 6.8 (VulnCheck) | Grav Admin plugin before 1.10.65 | 1.10.65 |
| [CVE-2026-129110](CVE-2026-129110) | sysPass | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | sysPass 3.0.1 through 3.2.11 | 未發布（修復 PR #360 已合併，尚未發版） |
| [CVE-2026-109601](CVE-2026-109601) | Frappe Framework | 4.0 8.2 (VulnCheck); 3.1 7.5 (VulnCheck) | Frappe Framework < 15.117.0；16.x < 16.30.0 | 15.117.0 / 16.30.0 |
| [CVE-2026-119145](CVE-2026-119145) | Frappe Framework | 4.0 9.4 (VulnCheck); 3.1 9.9 (VulnCheck) | Frappe < 15.121.0；16.x < 16.34.0 | 15.121.0 / 16.34.0 |
| [CVE-2026-58443](CVE-2026-58443) | Gitea | 3.1 9.6 (GHSA); 3.1 9.1 (NVD) | Gitea ≤ 1.26.4 | 1.27.0 |
| [GHSA-5rq2-4mjm-m7q2](GHSA-5rq2-4mjm-m7q2) | Budibase | 3.1 9.1 (GHSA) | @budibase/server < 4.0.0 | 4.0.0 |
| [GHSA-g9x9-q7qj-6mv5](GHSA-g9x9-q7qj-6mv5) | AVideo | 3.1 8.1 (GHSA) | AVideo ≤ 29.0 |  |
| [GHSA-r2q3-7m4h-63qg](GHSA-r2q3-7m4h-63qg) | Budibase | 3.1 7.7 (GHSA) | @budibase/server < 4.0.0 | 3.50.0 / 4.0.0 |
| [GHSA-vwqr-4mjv-ffrm](GHSA-vwqr-4mjv-ffrm) | Frappe Framework | 3.1 8.5 (GHSA) | Frappe Framework < 15.127.1；16.0.0–< 16.60.1 | 15.127.1 / 16.60.1 |
| [CVE-2026-135279](CVE-2026-135279) | @fastify/express | 3.1 9.1 (GHSA) | @fastify/express < 4.0.14 | 4.0.14 |
| [CVE-2026-63304](CVE-2026-63304) | AVideo | 4.0 9.2 (VulnCheck); 3.1 8.1 (VulnCheck) | AVideo < 29.1.0 | 29.1.0 |
| [CVE-2026-120704](CVE-2026-120704) | GeoServer | 3.1 7.2 (GHSA) | GeoServer <= 2.27.6, 2.28.0-2.28.5, 3.0.0-3.0.1 | 2.27.7, 2.28.6, 3.0.2 |
| [CVE-2026-120705](CVE-2026-120705) | GeoServer | 3.1 8.6 (GHSA) | GeoServer <= 2.27.6, 2.28.0-2.28.5, 3.0.0-3.0.1 | 2.27.7, 2.28.6, 3.0.2 |
| [CVE-2026-129243](CVE-2026-129243) | GeoServer | 4.0 8.8 (GHSA) | GeoServer <= 2.27.6, 2.28.0-2.28.5, 3.0.0-3.0.1 | 2.27.7, 2.28.6, 3.0.2 |
| [CVE-2026-129244](CVE-2026-129244) | GeoServer | 4.0 6.9 (GHSA) | GeoServer <= 2.27.6, 2.28.0-2.28.5, 3.0.0-3.0.1 | 2.27.7, 2.28.6, 3.0.2 |
| [CVE-2026-129245](CVE-2026-129245) | GeoServer | 4.0 9.2 (GHSA) | GeoServer <= 2.27.6, 2.28.0-2.28.5, 3.0.0-3.0.1 | 2.27.7, 2.28.6, 3.0.2 |
| [CVE-2026-76904](CVE-2026-76904) | GeoServer | 3.1 9.8 (NVD) | GeoServer <= 2.27.5, 2.28.0-2.28.4, 3.0.0（PostGIS 12+ 圖層） | 2.27.6, 2.28.5, 3.0.1 |
| [CVE-2026-134639](CVE-2026-134639) | Webmin | 4.0 9.2 (VulnCheck); 3.1 8.1 (VulnCheck) | Webmin through 2.670 (Windows setup.bat) | 無修復版本（截至 2026-11-26，2.670 仍為最新版） |
| [CVE-2026-134447](CVE-2026-134447) | Webmin | 4.0 5.3 (VulnCheck); 3.1 6.1 (GHSA) | Webmin through 2.670 | 未發佈（修復提交 b8e0462，僅在 master） |
| [CVE-2026-134643](CVE-2026-134643) | Webmin | 4.0 8.3 (VulnCheck); 3.1 6.5 (GHSA) | Webmin through 2.670 | 未發佈（修復僅在 master，2.670 仍為最新版） |
| [CVE-2026-73695](CVE-2026-73695) | Control Web Panel (CWP) | 4.0 8.7 (VulnCheck); 3.1 8.8 (VulnCheck); 3.1 9.8 (GHSA) | Control Web Panel < 1.16 | 1.16 |
| [CVE-2026-115867](CVE-2026-115867) | Database for Contact Form 7（WPForms、Elementor 表單外掛） | 3.1 9.8 (Wordfence) | Database for Contact Form 7 ≤ 1.5.5 | 1.5.6 |
| [CVE-2026-137706](CVE-2026-137706) | Smart Portal | 4.0 9.4 (TWCERT); 3.1 9.9 (TWCERT) | Smart Portal（Administrative Information Portal），版本未明 | 無修復版本（截至 2026-11-27，TWCERT 僅建議聯繫廠商處理） |
| [CVE-2026-137491](CVE-2026-137491) | Budibase | 4.0 8.6 (VulnCheck); 3.1 8.1 (VulnCheck) | Budibase < 4.0.0 | 4.0.0 |
| [CVE-2026-137492](CVE-2026-137492) | Budibase | 4.0 8.7 (VulnCheck); 3.1 8.8 (VulnCheck) | Budibase < 4.0.0 | 4.0.0 |
| [CVE-2026-137493](CVE-2026-137493) | Budibase | 4.0 8.6 (VulnCheck); 3.1 8.1 (VulnCheck) | Budibase Server 3.0.0 – < 4.0.0 | 4.0.0 |
| [CVE-2026-137494](CVE-2026-137494) | Budibase | 4.0 8.5 (VulnCheck); 3.1 9.9 (VulnCheck) | Budibase < 4.0.0 | 4.0.0 |
| [CVE-2026-137498](CVE-2026-137498) | Budibase | 4.0 9.9 (VulnCheck); 3.1 10.0 (VulnCheck) | Budibase Server 3.39.18 – < 4.0.0 | 4.0.0 |
| [CVE-2026-137499](CVE-2026-137499) | Budibase | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | Budibase 3.41.0 – < 4.0.0 | 4.0.0 |
| [CVE-2026-106125](CVE-2026-106125) | Sneeit Framework | 3.1 9.8 (Wordfence) | Sneeit Framework ≤ 8.7 | 8.8 |
| [CVE-2026-137544](CVE-2026-137544) | LaraDashboard | 4.0 9.4 (VulnCheck); 3.1 9.1 (VulnCheck) | LaraDashboard < 1.5.0 | 1.5.0 |
| [CVE-2026-137536](CVE-2026-137536) | ToolJet | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | ToolJet < 3.21.94-beta | 3.21.94-beta |
| [CVE-2026-122244](CVE-2026-122244) | Budibase | 3.1 7.7 (GHSA) | Budibase < 3.50.0 | 3.50.0 / 4.0.0 |
| [CVE-2026-77309](CVE-2026-77309) | AIT-GUI | 3.1 8.8 (GHSA) | AIT-GUI 1.0.0–2.5.0 | 2.5.1 |
| [CVE-2026-133938](CVE-2026-133938) | JTL-Shop | 4.0 8.6 (JTL); 3.1 9.3 (JTL) | JTL-Shop 5.2.3–5.8.4（5.2.3–5.4.x 已停更、無修補；5.0.0–5.2.2 不受影響） | 5.8.5；5.7.7；5.6.7；5.5.6 |
| [CVE-2026-133939](CVE-2026-133939) | JTL-Shop | 4.0 8.6 (JTL); 3.1 9.3 (JTL) | JTL-Shop 5.0.0–5.8.4（5.0.x–5.4.x 已停更、無修補） | 5.8.5；5.7.7；5.6.7；5.5.6 |
| [CVE-2026-133941](CVE-2026-133941) | JTL-Shop | 4.0 8.6 (JTL); 3.1 9.3 (JTL) | JTL-Shop 5.6.0–5.8.4（5.5.x 及更早不受影響） | 5.8.5；5.7.7；5.6.7 |
| [CVE-2026-59103](CVE-2026-59103) | MONEO ERP | 4.0 9.3 (OffSeq); 3.1 9.8 (OffSeq) | MONEO ERP ≤ 1.8.45.6（於 1.8.45.6 確認） | 2026-08-03 發布版 |
| [CVE-2026-126984](CVE-2026-126984) | pulp_python | 3.1 10.0 (GHSA) | pulp_python 啟用 pull-through caching 的 Python distribution（有 remote 者） |  |
| [cacti-core-2026-unauthenticated-rce](cacti-core-2026-unauthenticated-rce) | Cacti | unknown | Cacti Core 1.2.31（guest 帳號啟用時） |  |
| [CVE-2026-114607](CVE-2026-114607) | better-auth | 3.1 9.1 (GHSA) | better-auth 1.4.0-beta.18 起，1.7.7 之前（須啟用 Magic Link 與 social 或 Generic OAuth 登入） | 1.7.7 |
| [CVE-2026-134963](CVE-2026-134963) | WPMasterToolKit | 3.1 9.9 (Patchstack) | WPMasterToolKit through 2.26.1 | 2.26.2 |
| [CVE-2026-135930](CVE-2026-135930) | Amelia | 3.1 9.1 (Patchstack) | Amelia through 2.4.14 | 2.4.15 |
| [CVE-2026-135933](CVE-2026-135933) | WebinarIgnition | 3.1 9.8 (Patchstack) | WebinarIgnition through 4.28.1 | 4.28.10 |
| [CVE-2026-134987](CVE-2026-134987) | WordPress File Upload | 3.1 8.6 (Patchstack) | WordPress File Upload ≤ 5.3.1 | 5.3.2 |
| [CVE-2026-134994](CVE-2026-134994) | Revertix | 3.1 9.8 (Patchstack) | Revertix ≤ 1.0.3 | 1.0.4 |
| [CVE-2026-135009](CVE-2026-135009) | Media Library Assistant | 3.1 9.3 (Patchstack) | Media Library Assistant ≤ 3.43 | 3.44 |
| [CVE-2026-135048](CVE-2026-135048) | WP ERP | 3.1 8.8 (Patchstack) | WP ERP ≤ 2.0.0 | 2.0.1 |
| [CVE-2026-124981](CVE-2026-124981) | Mendix OIDC Provider | 4.0 9.4 (Siemens); 3.1 8.7 (Siemens) | Mendix OIDC Provider < V4.3.0 (Mendix 9) / < V6.0.0 (Mendix 10/11) | V4.3.0 (Mendix 9) / V6.0.0 (Mendix 10/11) |
| [CVE-2026-137957](CVE-2026-137957) | n8n | 4.0 5.3 (VulnCheck); 3.1 8.2 (VulnCheck) | n8n < 1.123.96 / < 2.47.6 / < 2.48.3 / < 3.2.2 | 1.123.96 / 2.47.6 / 2.48.3 / 3.2.2 |
| [CVE-2026-137959](CVE-2026-137959) | n8n | 4.0 5.3 (VulnCheck); 3.1 8.2 (VulnCheck) | n8n < 1.123.96 / < 2.47.6 / < 2.48.3 / < 3.2.2 | 1.123.96 / 2.47.6 / 2.48.3 / 3.2.2 |
| [CVE-2026-137964](CVE-2026-137964) | ToolJet | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | ToolJet < 3.21.96-LTS | 3.21.96-LTS |
| [CVE-2026-135968](CVE-2026-135968) | theMarketer | 3.1 8.6 (Patchstack) | theMarketer <= 1.5.9 | 1.6.0 |
| [CVE-2026-136113](CVE-2026-136113) | Hello Clever Gateway for WooCommerce | 3.1 9.3 (Patchstack) | Hello Clever Gateway for WooCommerce ≤ 1.8.4 |  |
| [CVE-2026-136115](CVE-2026-136115) | MemberPress Discord Addon | 3.1 9.8 (Patchstack) | MemberPress Discord Addon ≤ 1.1.5 |  |
| [CVE-2026-136692](CVE-2026-136692) | XunRuiCMS | 3.1 7.3 (VulDB); 4.0 5.5 (VulDB) | XunRuiCMS ≤ 4.7.4 |  |
| [CVE-2026-113774](CVE-2026-113774) | Schema & Structured Data for WP & AMP | 3.1 8.8 (Wordfence) | Schema & Structured Data for WP & AMP ≤ 1.68 | 1.69 |
| [CVE-2026-119071](CVE-2026-119071) | W3 Total Cache | 3.1 8.1 (Wordfence) | W3 Total Cache ≤ 2.11.0 | 2.11.1 |

### AI / LLM (33)

| ID | Product | Score | Affected | Fixed |
| --- | --- | --- | --- | --- |
| [CVE-2026-85228](CVE-2026-85228) | Amazon Deep Java Library (DJL) | 3.1 9.1 (AMZN); 4.0 8.8 (AMZN) | Amazon Deep Java Library (DJL) 0.13.0–0.36.0 | 0.37.0 |
| [CVE-2026-40217](CVE-2026-40217) | BerriAI LiteLLM | 3.1 8.8 (upstream PoC README) | LiteLLM before v1.83.11 (image digest pinning required; some rebuilt tags are not vulnerable) | v1.83.11+ (RestrictedPython) |
| [CVE-2026-130796](CVE-2026-130796) | Flowise | 4.0 8.8 (VulnCheck); 3.1 8.2 (VulnCheck) | 3.1.3-3.1.4 |  |
| [CVE-2026-102895](CVE-2026-102895) | GPUStack | 3.1 9.8 (GHSA) | < 2.2.0 | 2.2.0 |
| [CVE-2026-59726](CVE-2026-59726) | Ruflo MCP Bridge | 3.1 10.0 (GHSA) | Ruflo < 3.16.3 (default docker-compose MCP bridge) | 3.16.3 |
| [CVE-2026-63129](CVE-2026-63129) | mssql-mcp-core | 3.1 8.8 (GHSA) | mssql-mcp-core <= 0.5.0 (also reader <= 0.4.2, writer <= 0.4.2, server <= 0.5.2) | 0.6.0 |
| [CVE-2026-73678](CVE-2026-73678) | Minds Platform | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | MindsDB Minds Platform 26.1.0 and earlier | No fixed release published in CVE record (2026-11-20) |
| [CVE-2026-77312](CVE-2026-77312) | Flyto2 Core | 3.1 10.0 (GitHub) | Flyto2 Core <2.26.8 | 2.26.8 |
| [CVE-2026-77315](CVE-2026-77315) | Flyto2 Core | 3.1 8.5 (GitHub) | Flyto2 Core <2.26.8 | 2.26.8 |
| [CVE-2026-63189](CVE-2026-63189) | Dialoqbase | 3.1 9.8 (GHSA) | Dialoqbase <1.11.5 | 1.11.5 |
| [CVE-2026-76807](CVE-2026-76807) | Todoist MCP Server | 3.1 9.3 (GHSA) | Todoist MCP Server <10.3.3 | 10.3.3 |
| [CVE-2026-130154](CVE-2026-130154) | Zyrabit Platform | 3.1 9.1 (GHSA) | Zyrabit Platform <2.4.4 | 2.4.4 |
| [CVE-2026-77359](CVE-2026-77359) | Jupyter MCP Server | 4.0 9.3 (GHSA) | Jupyter MCP Server <1.0.3 | 1.0.3 |
| [CVE-2026-131304](CVE-2026-131304) | Splunk AI Assistant | 3.1 8.1 (Splunk) | Splunk AI Assistant <2.0.0 | 2.0.0 |
| [CVE-2026-131305](CVE-2026-131305) | Splunk AI Assistant | 3.1 8.1 (Splunk) | Splunk AI Assistant <2.0.0 | 2.0.0 |
| [CVE-2026-93328](CVE-2026-93328) | Google Cloud MCP Toolbox for Databases | 4.0 9.3 (GoogleCloud) | Google Cloud MCP Toolbox for Databases 1.2.0-1.4.0 | past 1.4.0 + allowlists (googleapis/mcp-toolbox#3454) |
| [CVE-2026-133968](CVE-2026-133968) | MONAI Label | 3.1 9.8 (MITRE) | MONAI Label through 0.8.5 | 0.8.6 (security release 2026-11-22; fix PR #1915) |
| [CVE-2026-48705](CVE-2026-48705) | MONAI | 3.1 9.3 (GHSA) | MONAI before 1.6.1 (PydicomReader); MONAILabel deployments using it | MONAI 1.6.1 |
| [CVE-2026-118683](CVE-2026-118683) | MONAI | 4.0 8.6 (VulnCheck) | MONAI 1.2.0 before 1.6.1 | MONAI 1.6.1 |
| [CVE-2026-54039](CVE-2026-54039) | LibreChat | 3.1 8.1 (GHSA) | LibreChat 0.7.0 through 0.8.6 (local registration + social provider) | 0.8.6 |
| [CVE-2026-135211](CVE-2026-135211) | BISHENG | 4.0 9.2 (VulnCheck); 3.1 8.1 (VulnCheck) | BISHENG before 3.0.0 | 3.0.0 |
| [CVE-2026-130169](CVE-2026-130169) | AutoGPT Platform | 3.1 10.0 (GHSA) | AutoGPT Platform 0.6.26 through 0.7.4 | 0.8.0 |
| [CVE-2026-118285](CVE-2026-118285) | Azure Machine Learning | 3.1 9.6 (Microsoft) | Azure Machine Learning |  |
| [CVE-2026-50691](CVE-2026-50691) | Microsoft 365 Copilot | 3.1 9.9 (Microsoft) | Microsoft 365 Copilot |  |
| [CVE-2026-64849](CVE-2026-64849) | MLflow | 3.1 9.3 (GitHub) | MLflow < 3.15.0 | 3.15.0 |
| [CVE-2026-63766](CVE-2026-63766) | GPT-SoVITS | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | GPT-SoVITS through 20250606v2pro | No known patch |
| [CVE-2026-59415](CVE-2026-59415) | Spring AI TypesenseVectorStore | 3.1 10.0 (Spring) | Spring AI 1.0.0–1.0.10, 1.1.0–1.1.9, 2.0.0–2.0.2 | 2.0.3 (OSS); 2.0.2.1 / 1.1.10 / 1.0.11 (Enterprise Support Only) |
| [CVE-2026-33017](CVE-2026-33017) | Langflow | 4.0 9.3 (GHSA); 3.1 9.8 (NVD) | Langflow before 1.9.0 | 1.9.0 |
| [CVE-2026-59822](CVE-2026-59822) | LiteLLM | 4.0 8.8 (GHSA); 3.1 8.2 (NVD) | LiteLLM before 1.84.0 | 1.84.0 |
| [CVE-2026-137308](CVE-2026-137308) | markdownify-mcp | 4.0 8.3 (VulnCheck); 3.1 7.4 (VulnCheck) | markdownify-mcp before 1.2.0 | 1.2.0 |
| [CVE-2026-114612](CVE-2026-114612) | LiteLLM | 3.1 9.9 (GHSA) | LiteLLM 1.91.0 起，1.100.4 之前；另 1.101.x < 1.101.3、1.102.x < 1.102.2、1.103.x < 1.103.1 | 1.100.4；1.101.3；1.102.2；1.103.1；1.104.0-rc.2 |
| [CVE-2026-137953](CVE-2026-137953) | Pydantic Deep | 4.0 8.8 (VulnCheck); 3.1 8.6 (VulnCheck) | Pydantic Deep 0.2.18–< 0.4.0 | 0.4.0 |
| [CVE-2026-136441](CVE-2026-136441) | DBHub | 3.0 9.8 (ZDI) | Bytebase DBHub（MCP server） |  |

### Network & Security (263)

| ID | Product | Score | Affected | Fixed |
| --- | --- | --- | --- | --- |
| [CVE-2026-130151](CVE-2026-130151) | Okta Privileged Access Gateway | 3.1 8.5 (Okta) | Okta Privileged Access Gateway <1.116.3 (RDP support) | 1.116.3 |
| [CVE-2026-95643](CVE-2026-95643) | ManageEngine DDI Central | 3.1 9.1 (Zohocorp) | Zohocorp ManageEngine DDI Central build <6500 | 6500 |
| [CVE-2026-95645](CVE-2026-95645) | ManageEngine DDI Central | 3.1 9.1 (Zohocorp) | Zohocorp ManageEngine DDI Central build <6500 | 6500 |
| [CVE-2026-104935](CVE-2026-104935) | Ivanti Connect Secure | 3.1 8.6 (Ivanti) | Ivanti Connect Secure 25.1.1.2 and prior; 25.1.2.2 and prior; 22.8R2.5 and prior | 25.1.1.3 / 22.8R2.6 |
| [CVE-2026-111357](CVE-2026-111357) | Ivanti Connect Secure | 3.1 7.0 (NVD); 3.1 8.8 (Ivanti) | Ivanti Connect Secure 25.1.1.2 and prior; 25.1.2.2 and prior; 22.8R2.5 and prior | 25.1.1.3 / 22.8R2.6 |
| [CVE-2026-118527](CVE-2026-118527) | Ivanti Connect Secure | 3.1 4.3 (Ivanti) | Ivanti Connect Secure 25.1.1.2 and prior; 25.1.2.2 and prior; 22.8R2.5 and prior | 25.1.1.3 / 22.8R2.6 |
| [CVE-2026-123007](CVE-2026-123007) | F5 NGINX HTTP/2 | 4.0 9.2 (F5); 3.1 8.1 (F5) | NGINX Open Source 1.9.5–1.30.6 and 1.31.0–1.31.8 with HTTP/2 enabled | Open Source 1.30.7 / 1.31.9; NGINX Plus 37.3.0.1 / 37.0.8.1 |
| [CVE-2026-129287](CVE-2026-129287) | N-able N-central | 4.0 8.3 (N-able (CNA)) | before 2026.4.1 Hotfix 3 | 2026.4.1 Hotfix 3 (build 2026.4.1.39) |
| [CVE-2026-119958](CVE-2026-119958) | Windows LDAP | 3.1 9.8 (Microsoft) | Windows 10 1607–Windows 11 26H2、Windows Server 2016–2025 | 2026 年 11 月安全更新 |
| [CVE-2026-123039](CVE-2026-123039) | Check Point Gaia OS | 3.1 7.8 (Check Point) | Gaia OS R81–R82.20（Quantum 網關、Force 防火牆、安全管理/日誌服務器、多域、Maestro） | Jumbo Hotfix：R82.20 Take 14、R82.10 Take 52、R82 Take 132、R81.20 Take 174 |
| [CVE-2026-123158](CVE-2026-123158) | OpenSSH sshd | 3.1 8.1 (MITRE) | OpenSSH < 10.6p2（Linux + musl libc 且無 PAM，如 Alpine Linux） | OpenSSH 10.6p2 |
| [CVE-2026-123218](CVE-2026-123218) | IBM Aspera Faspex 5 | 3.1 9.8 (IBM) | Faspex 5.0.0–5.0.19 | 5.0.19 PL1（Fix Pack 1） |
| [CVE-2026-111560](CVE-2026-111560) | Barracuda ESG / ADC / WAF / WSG | 4.0 8.6 (Mandiant); 3.1 7.2 (NVD) | ESG ≤ 9.4.0.27；ADC ≤ 6.4.0；WAF ≤ 11.0.1；WSG ≤ 16.1.100.100；BMA ≤ 5.5.4.0；WCC ≤ 2.2.1 | ESG 9.4.0.030；其餘產品按廠商通告補丁升級 |
| [CVE-2026-116606](CVE-2026-116606) | Barracuda ESG | 4.0 9.3 (Mandiant); 3.1 9.8 (NVD) | ESG < 9.4.0.030 | 9.4.0.030 |
| [CVE-2026-19868](CVE-2026-19868) | SonicWall SonicOS | 3.1 7.5 (CISA-ADP); 3.1 7.1 (SonicWall) | Gen7 7.3.3-7015 及更早；Gen8 8.2.2-8015 及更早 | Gen7 7.3.4-7013 及更高；Gen8 8.2.3-8015 及更高 |
| [CVE-2026-129271](CVE-2026-129271) | N-able N-central Patch Management | 4.0 8.5 (N-able) | Patch Management Component < 2.14.4.5829 | 2.14.4.5829（隨 N-central 2026.4.1 Hotfix 3，build 2026.4.1.39，2026-11-16） |
| [CVE-2026-129280](CVE-2026-129280) | N-able N-central | 4.0 9.3 (N-able) | N-central < 2026.4.1 HF3 | 2026.4.1 HF3（build 2026.4.1.39，2026-11-16） |
| [CVE-2026-114713](CVE-2026-114713) | UnrealIRCd | 3.1 8.6 (GHSA) | 6.0.0–6.2.7 (5.x EOL also affected) | 6.2.7.1 / hotfix bundle-20261107 |
| [CVE-2026-116779](CVE-2026-116779) | FreeSWITCH | 3.1 9.8 (GHSA) | <= 1.11.2 | 1.11.3 (adds enable-chat-api-proto, off by default) |
| [CVE-2026-119618](CVE-2026-119618) | Apache httpd mod_http2 | 3.1 8.1 (NVD); 3.1 9.8 (Red Hat) | httpd 2.4.55–2.4.70, mod_h2 2.0.8–2.0.42 | 2.4.71, mod_h2 2.0.43 |
| [CVE-2026-126170](CVE-2026-126170) | Fortinet FortiManager / FortiAnalyzer | 3.1 9.8 (Fortinet) | FortiAnalyzer 8.0.0-8.0.2, 7.6.0-7.6.7; FortiAnalyzer Cloud 8.0.1-8.0.2, 7.6.0-7.6.7; FortiAnalyzer-BigData 7.6.0-7.6.2; FortiManager 8.0.0-8.0.2, 7.6.0-7.6.7; FortiManager Cloud 8.0.1-8.0.2, 7.6.0-7.6.7; FortiSASE-Sovereign 25, 25.3, 25.4, 26.2 | 8.0.3, 7.6.8, FortiAnalyzer-BigData 7.6.3 |
| [CVE-2026-124079](CVE-2026-124079) | rConfig Core / Pro | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | rConfig Core >= 8.0.0, < 8.2.19; rConfig Pro < 8.4.1 | rConfig Core 8.2.19 (2026-10-27); rConfig Pro 8.4.1 |
| [CVE-2026-121653](CVE-2026-121653) | Ivanti Endpoint Manager Core | 3.1 9.8 (Ivanti) | Ivanti EPM 2024 SU7 and prior | EPM 2024 SU8 |
| [CVE-2026-111585](CVE-2026-111585) | TeamViewer clients | 3.1 8.8 (TeamViewer) | TeamViewer clients prior to 15.83 (15.82.6 tested) | 15.83 (bulletin TV-2026-1011) |
| [CVE-2026-83548](CVE-2026-83548) | SonicWall SMA1000 | 3.1 10.0 (NVD) | SMA1000 6210 / 7210 / 8200v: 12.4.3-03453 and older, 12.5.0-02835 and older | 12.4.3-03526 and higher, 12.5.0-02952 and higher (platform-hotfix) |
| [CVE-2026-83549](CVE-2026-83549) | SonicWall SMA1000 | 3.1 7.8 (NVD) | SMA1000 6210 / 7210 / 8200v: 12.4.3-03453 and older, 12.5.0-02835 and older | 12.4.3-03526 and higher, 12.5.0-02952 and higher (platform-hotfix) |
| [CVE-2026-123633](CVE-2026-123633) | F5 NGINX HTTP/2 | 4.0 9.2 (F5); 3.1 8.1 (F5) | NGINX Open Source 1.19.7-1.30.6 and 1.31.0-1.31.8 with HTTP/2 proxying | 1.30.7 / 1.31.9 |
| [CVE-2026-110486](CVE-2026-110486) | Eclipse Mosquitto | 3.1 9.8 (NVD) | 2.1.0–2.1.2 (builtin WebSocket listener) | 2.1.3 |
| [CVE-2026-124040](CVE-2026-124040) | CivetWeb HTTP/2 | 4.0 9.2 (VulnCheck); 3.1 8.1 (VulnCheck) | CivetWeb through 1.16, built with USE_HTTP2 and enable_http2 | No fixed release listed (PoC repo ships fix-http2.patch) |
| [CVE-2026-116448](CVE-2026-116448) | Dell PowerStore SDNAS | 3.1 9.8 (GHSA) | Dell PowerStore OS <= 3.6.0.0 with SDNAS enabled (per PoC README; GHSA lists no version range) | PowerStore OS 4.0.0.1 (per PoC README) |
| [CVE-2026-123634](CVE-2026-123634) | F5 NGINX resolver (SSI) | 4.0 9.2 (F5); 3.1 8.1 (F5) | NGINX 0.6.18-1.31.8 (proxy with SSI subrequests) | 1.30.7 / 1.31.9 |
| [CVE-2026-121810](CVE-2026-121810) | F5 NGINX HTTP/3 (QUIC) | 4.0 9.2 (F5); 3.1 8.1 (F5) | NGINX 1.25.0-1.31.8 (HTTP/3) | 1.30.7 / 1.31.9 |
| [CVE-2026-113425](CVE-2026-113425) | F5 NGINX mail proxy | 4.0 9.2 (F5); 3.1 8.1 (F5) | NGINX 0.5.33-1.31.8 (mail proxy) | 1.30.7 / 1.31.9 |
| [CVE-2026-118899](CVE-2026-118899) | F5 NGINX TLS 1.3 | 4.0 8.7 (F5); 3.1 7.5 (F5) | NGINX 1.13.0-1.31.8 (TLS 1.3, http block) | 1.30.7 / 1.31.9 |
| [CVE-2026-116442](CVE-2026-116442) | Dell PowerStore NDMP | 3.1 8.1 (GHSA) | Dell PowerStore OS <= 3.6.0.0 with NDMP enabled (per PoC README; GHSA lists no version range) | PowerStore OS 4.0.0.1 (per PoC README) |
| [CVE-2026-114202](CVE-2026-114202) | ASUS Control Center Express | 4.0 10.0 (NVD) | ASUS Control Center Express all firmware versions prior to patch (PoC tested through v1.7.27) | no fixed version published |
| [CVE-2026-131852](CVE-2026-131852) | OwnTracks Recorder | 3.1 9.8 (GHSA) | OwnTracks Recorder before 1.0.5 | 1.0.5 |
| [CVE-2026-92182](CVE-2026-92182) | pfSense CE | 3.0 8.8 (GHSA) | pfSense CE ≤ 2.8.1 | pfSense CE 2.8.2 |
| [CVE-2026-123640](CVE-2026-123640) | F5 NGINX ssl_preread | 3.1 5.3 (GHSA) | nginx 1.15.2–1.31.8 (ssl_preread) | 1.30.7 / 1.31.9 |
| [CVE-2026-120993](CVE-2026-120993) | F5 NGINX stream SSL | 3.1 5.3 (GHSA) | nginx 1.31.4–1.31.8 (stream SSL + PROXY v2) | 1.31.9 |
| [CVE-2026-125283](CVE-2026-125283) | F5 NGINX alias/try_files | 3.1 5.3 (GHSA) | nginx 0.9.6–1.31.8 (alias + try_files) | 1.30.7 / 1.31.9 |
| [CVE-2026-120967](CVE-2026-120967) | F5 NGINX stream SNI | 3.1 4.8 (GHSA) | nginx 1.25.5–1.31.8 (stream SNI mTLS) | 1.30.7 / 1.31.9 |
| [CVE-2026-129358](CVE-2026-129358) | Magma NMS | 4.0 1.9 (VulDB) | Magma NMS up to 1.9.0 | none (unfixed upstream) |
| [CVE-2026-129351](CVE-2026-129351) | TRENDnet TEW-657BRM | 4.0 10.0 (VulDB); 3.1 10.0 (VulDB) | TEW-657BRM v1.0R firmware 1.00.1 | none (EOL, no vendor fix) |
| [CVE-2026-129353](CVE-2026-129353) | D-Link DIR-600L | 4.0 10.0 (VulDB); 3.1 10.0 (VulDB) | DIR-600L B1 firmware 2.17, 2.17b02 | none (EOL, no vendor fix) |
| [CVE-2026-129354](CVE-2026-129354) | D-Link DIR-600L | 4.0 10.0 (VulDB); 3.1 10.0 (VulDB) | DIR-600L B1 firmware 2.17b02 | none (EOL, no vendor fix) |
| [CVE-2026-110697](CVE-2026-110697) | Quay | 3.1 9.9 (Red Hat) | Quay < 3.9.28; 3.10 < 3.10.28; 3.12 < 3.12.24; 3.14 < 3.14.10; 3.15 < 3.15.9; 3.16 < 3.16.7; 3.17 < 3.17.7; 3.18 < 3.18.3 | 3.9.28 / 3.10.28 / 3.12.24 / 3.14.10 / 3.15.9 / 3.16.7 / 3.17.7 / 3.18.3 |
| [CVE-2026-126147](CVE-2026-126147) | FortiMail | 3.1 9.8 (Fortinet) | FortiMail 8.0.0–8.0.1, 7.6.0–7.6.6, 7.4.0–7.4.8, 7.2.0–7.2.9 | 8.0.2 / 7.6.7 / 7.4.9; migrate off 7.2 |
| [CVE-2026-126148](CVE-2026-126148) | FortiMail | 3.1 9.8 (Fortinet) | FortiMail 8.0.0–8.0.1, 7.6.0–7.6.6 | 8.0.2 / 7.6.7 |
| [CVE-2026-129352](CVE-2026-129352) | TRENDnet TEW-657BRM | 4.0 9.4 (VulDB); 3.1 9.1 (VulDB) | TEW-657BRM v1.0R firmware 1.00.1 | none (EOL, no vendor fix) |
| [CVE-2026-114550](CVE-2026-114550) | libwebsockets | 3.0 8.1 (GHSA) | libwebsockets v4.2–v4.5.8 (MQTT client role) | 5.0.0 |
| [CVE-2026-129355](CVE-2026-129355) | dufs | 4.0 6.9 (VulnDB); 3.1 6.5 (VulnDB) | dufs 0.1.0–0.46.0 | 0.47.0 |
| [CVE-2026-129359](CVE-2026-129359) | Magma orc8r | 4.0 5.5 (VulnDB); 3.1 7.3 (VulnDB) | Magma <= 1.9.0 | no upstream fix (synthetic remediation in lab) |
| [CVE-2026-129360](CVE-2026-129360) | Magma orc8r | 4.0 6.9 (VulnDB); 3.1 7.3 (VulnDB) | Magma <= 1.9.0 | no upstream fix (synthetic remediation in lab) |
| [CVE-2026-76466](CVE-2026-76466) | Cisco Expressway | 3.1 9.8 (Cisco) | Expressway-C / Expressway-E clustered, X15.5.3 and earlier (X14 and earlier too) | X15.5.20 |
| [CVE-2026-13249](CVE-2026-13249) | Honeywell PD45 | 3.1 9.8 (Honeywell) | Honeywell PD45 firmware >= F10.19.010040 and < F10.22.030745 | F10.22.030745 |
| [CVE-2026-13768](CVE-2026-13768) | Gardyn Home Kit / Studio | 4.0 9.5 (ICS-CERT); 3.1 10.0 (ICS-CERT) | Gardyn Home Kit and Studio devices (exposed iothubowner key) | Cloud-side fix deployed (2026-07); devices auto-update firmware when connected |
| [CVE-2026-116440](CVE-2026-116440) | PowerStore SDNAS | 3.1 9.8 (Dell) | Dell PowerStore SDNAS versions before 5.1.0.0-2798105 | 5.1.0.0-2798105 (DSA-2026-479) |
| [CVE-2026-132622](CVE-2026-132622) | GearUP Hyperev | 4.0 9.4 (VulDB); 3.1 9.1 (VulDB) | GearUP Hyperev up to 20261020 |  |
| [CVE-2026-133185](CVE-2026-133185) | goproxy | 4.0 9.1 (VulnCheck); 3.1 7.4 (VulnCheck) | elazarl/goproxy before 1.9.4 | 1.9.4 |
| [CVE-2026-116443](CVE-2026-116443) | PowerStore SDNAS | 3.1 9.8 (Dell) | Dell PowerStore SDNAS versions before 5.1.0.0-2798105 | 5.1.0.0-2798105 (DSA-2026-479) |
| [CVE-2026-116446](CVE-2026-116446) | PowerStore SDNAS | 3.1 9.8 (Dell) | Dell PowerStore SDNAS versions before 5.1.0.0-2798105 | 5.1.0.0-2798105 (DSA-2026-479) |
| [CVE-2026-116449](CVE-2026-116449) | PowerStore SDNAS | 3.1 9.8 (Dell) | Dell PowerStore SDNAS versions before 5.1.0.0-2798105 | 5.1.0.0-2798105 (DSA-2026-479) |
| [CVE-2026-116441](CVE-2026-116441) | PowerStore SDNAS | 3.1 9.6 (Dell) | Dell PowerStore SDNAS versions before 5.1.0.0-2798105 | 5.1.0.0-2798105 (DSA-2026-479) |
| [CVE-2026-111505](CVE-2026-111505) | OpenManage Enterprise | 3.1 8.8 (Dell) | Dell OpenManage Enterprise versions prior to 4.8.0 | 4.8.0 (DSA-2026-467) |
| [CVE-2026-111506](CVE-2026-111506) | PowerStore | 3.1 8.8 (Dell) | Dell PowerStoreT OS 5.1.x versions prior to 5.1.0.0-2798105 | 5.1.0.0-2798105 or later (DSA-2026-479) |
| [CVE-2026-111545](CVE-2026-111545) | PowerStore | 3.1 8.8 (Dell) | Dell PowerStoreT OS 5.1.x versions prior to 5.1.0.0-2798105 | 5.1.0.0-2798105 or later (DSA-2026-479) |
| [CVE-2026-133323](CVE-2026-133323) | MiCollab | 3.1 10.0 (Mitel) | MiCollab 10.3 (10.3.0.18) and earlier | Patch for 10.3 (10.3.0.18) (MISA-2026-0012) |
| [CVE-2026-133303](CVE-2026-133303) | MiCollab | 3.1 9.0 (Mitel) | MiCollab 10.3 (10.3.0.18) and earlier | Patch for 10.3 (10.3.0.18) (MISA-2026-0012) |
| [CVE-2026-133310](CVE-2026-133310) | Wing FTP Server | 4.0 9.2 (VulnCheck); 3.1 8.1 (VulnCheck) | Wing FTP Server before 8.2.8 | 8.2.8 |
| [CVE-2026-116447](CVE-2026-116447) | PowerStore SDNAS | 3.1 8.8 (Dell) | Dell PowerStore SDNAS versions before 5.1.0.0-2798105 | 5.1.0.0-2798105 (DSA-2026-479) |
| [CVE-2026-116411](CVE-2026-116411) | PowerStore | 3.1 8.8 (Dell) | Dell PowerStore SDNAS versions before 5.1.0.0-2798105 | 5.1.0.0-2798105 (DSA-2026-479) |
| [CVE-2026-76460](CVE-2026-76460) | Identity Services Engine | 3.1 10.0 (Cisco) | Cisco ISE 3.1-3.5 and ISE-PIC 3.4-3.5 | 3.1 Patch 12 / 3.2 Patch 11 / 3.3 Patch 12 / 3.4 Patch 7 / 3.5 Patch 4 (2026-09-16) |
| [CVE-2026-84295](CVE-2026-84295) | WS_FTP Server | 3.1 10.0 (Progress) | Progress WS_FTP Server before 2024.0.6 / 2025.0.3 | 2024.0.6 / 2025.0.3 |
| [CVE-2026-77537](CVE-2026-77537) | UniFi Protect | 3.1 10.0 (UI) | UniFi Protect Application before 7.2.105 | 7.2.105 |
| [CVE-2026-95787](CVE-2026-95787) | ArubaOS (AOS-10) | 3.1 10.0 (HPE) | ArubaOS AOS-10 10.8.1.1 and below, 10.7.2.6 and below, 10.4.1.13 and below | 10.8.1.2 / 10.7.2.7 / 10.4.1.14 and above (HPE SBNW05162) |
| [CVE-2026-111507](CVE-2026-111507) | PowerStore | 3.1 8.1 (Dell) | Dell PowerStore versions before 5.1.0.0-2798105 | 5.1.0.0-2798105 (DSA-2026-479) |
| [CVE-2026-111547](CVE-2026-111547) | PowerStore | 3.1 8.1 (Dell) | Dell PowerStore versions before 5.1.0.0-2798105 | 5.1.0.0-2798105 (DSA-2026-479) |
| [CVE-2026-116417](CVE-2026-116417) | PowerScale InsightIQ | 3.1 8.1 (Dell) | Dell PowerScale InsightIQ 6.3.0-6.4.0 | 6.4.1 (DSA-2026-480) |
| [CVE-2026-15409](CVE-2026-15409) | SMA1000 | 3.1 10.0 (SonicWall) | SonicWall SMA1000 12.4.3-03245/03387/03434, 12.5.0-02283/02624/02800 (platform-hotfix) and earlier | 12.4.3-03453 / 12.5.0-02835 and higher (SNWLID-2026-0008) |
| [CVE-2026-109469](CVE-2026-109469) | Entra Device Registration | 3.1 10.0 (Microsoft) | Microsoft Entra Device Registration (hosted service) | Official fix available (Microsoft service-side remediation, MSRC 2026-11-05) |
| [CVE-2026-102255](CVE-2026-102255) | SMA1000 | 3.1 10.0 (SonicWall) | SonicWall SMA1000 12.4.3-03526 and older, 12.5.0-02952 and older (platform-hotfix) | 12.4.3-03670 / 12.5.0-03082 and higher (SNWLID-2026-0017) |
| [CVE-2026-77550](CVE-2026-77550) | UniFi OS Server | 3.1 10.0 (UI) | UniFi OS Server 5.1.21 and earlier; UniFi OS devices 5.1.26 and earlier; Express 4.0.16 and earlier | UniFi OS Server 5.1.37+; devices 5.1.31+; NAS 5.1.32+; Express 4.0.17+ (Bulletin 067) |
| [CVE-2026-77554](CVE-2026-77554) | UniFi Talk Application | 3.1 10.0 (UI) | UniFi Talk Application 5.2.7 and earlier | 5.3.2 or later (Bulletin 067) |
| [CVE-2026-84236](CVE-2026-84236) | Guardium Data Protection | 3.1 9.8 (IBM) | IBM Guardium Data Protection 12.2 | 12.2.4 |
| [CVE-2026-87977](CVE-2026-87977) | Guardium Data Protection | 3.1 9.8 (IBM) | IBM Guardium Data Protection 12.2 | 12.2.4 |
| [CVE-2026-76536](CVE-2026-76536) | Splunk Enterprise | 3.1 9.4 (Splunk) | Splunk Enterprise 10.4-10.4.4, 10.2-10.2.8, 10.0-10.0.11, 9.4-9.4.16 | 10.4.5 / 10.2.9 / 10.0.12 / 9.4.17 (SVD-2026-1103) |
| [CVE-2026-76535](CVE-2026-76535) | Splunk Enterprise | 3.1 9.1 (Splunk) | Splunk Enterprise 10.6.0.5, 10.4-10.4.4, 10.2-10.2.8, 10.0-10.0.11, 9.4-9.4.16 | 10.6.1 / 10.4.5 / 10.2.9 / 10.0.12 / 9.4.17 (SVD-2026-1103) |
| [CVE-2026-82339](CVE-2026-82339) | Guardium Data Protection | 3.1 9.1 (IBM) | IBM Guardium Data Protection 12.2 | 12.2.4 |
| [CVE-2026-76538](CVE-2026-76538) | Splunk Enterprise | 3.1 8.8 (Splunk) | Splunk Enterprise 10.4-10.4.4, 10.2-10.2.8, 10.0-10.0.11, 9.4-9.4.15 | 10.4.5 / 10.2.9 / 10.0.12 / 9.4.16 (SVD-2026-1103) |
| [CVE-2026-76540](CVE-2026-76540) | Splunk Enterprise | 3.1 8.8 (Splunk) | Splunk Enterprise 10.4-10.4.4, 10.2-10.2.8, 10.0-10.0.11, 9.4-9.4.16 | 10.4.5 / 10.2.9 / 10.0.12 / 9.4.17 (SVD-2026-1103) |
| [CVE-2026-84273](CVE-2026-84273) | Guardium Data Protection | 3.1 8.1 (IBM) | IBM Guardium Data Protection 12.2 | 12.2.4 |
| [CVE-2026-85018](CVE-2026-85018) | Guardium Data Protection | 3.1 8.1 (IBM) | IBM Guardium Data Protection 12.2 | 12.2.4 |
| [CVE-2026-82342](CVE-2026-82342) | Guardium Data Protection | 3.1 8.1 (IBM) | IBM Guardium Data Protection 12.2 | 12.2.4 |
| [CVE-2026-76544](CVE-2026-76544) | Splunk Enterprise | 3.1 8.1 (Splunk) | Splunk Enterprise 10.4-10.4.4, 10.2-10.2.8, 10.0-10.0.11, 9.4-9.4.15 | 10.4.5 / 10.2.9 / 10.0.12 / 9.4.16 (SVD-2026-1103) |
| [CVE-2026-132808](CVE-2026-132808) | UniFi Access Application | 3.1 9.9 (Ubiquiti) | UniFi Access Application <4.3.24 | 4.3.24 |
| [CVE-2026-132804](CVE-2026-132804) | UniFi Access Application | 3.1 9.9 (Ubiquiti) | UniFi Access Application <4.3.24 | 4.3.24 |
| [CVE-2026-132803](CVE-2026-132803) | UniFi Access Application | 3.1 9.9 (Ubiquiti) | UniFi Access Application <4.3.24 | 4.3.24 |
| [CVE-2026-132802](CVE-2026-132802) | UniFi Access Application | 3.1 9.9 (Ubiquiti) | UniFi Access Application <4.3.24 | 4.3.24 |
| [CVE-2026-132139](CVE-2026-132139) | DrayTek Vigor2960 | 4.0 9.4 (VulDB); 3.1 9.9 (VulDB) | Vigor2960 1.5.1.0-1.5.1.6 | 1.5.1.7 |
| [CVE-2026-121805](CVE-2026-121805) | F5 BIG-IP | 4.0 9.3 (F5); 3.1 9.8 (F5) | BIG-IP 21.1.0 / 17.5.x / 17.1.x with PEM::subscriber iRule | 21.1.0.4.0.19.3-ENG / 17.5.1.11.0.61.12-ENG / 17.1.3.7.0.21.4-ENG |
| [CVE-2026-120722](CVE-2026-120722) | F5 BIG-IP | 4.0 9.3 (F5); 3.1 9.8 (F5) | BIG-IP 21.1.0 / 17.5.x / 17.1.x with DNS::scrape iRule | 21.1.0.4.0.19.3-ENG / 17.5.1.11.0.61.12-ENG / 17.1.3.7.0.21.4-ENG |
| [CVE-2026-120292](CVE-2026-120292) | F5 BIG-IP | 4.0 9.3 (F5); 3.1 9.8 (F5) | BIG-IP 21.1.0 / 17.5.0-17.5.1 / 17.1.0-17.1.3 with MR::message route iRule | 21.1.0.4.0.19.3-ENG / 17.5.1.11.0.61.12-ENG / 17.1.3.7.0.21.4-ENG |
| [CVE-2026-120285](CVE-2026-120285) | F5 BIG-IP | 4.0 9.3 (F5); 3.1 9.8 (F5) | BIG-IP 21.1.0 / 17.5.0-17.5.1 / 17.1.0-17.1.3 with PSC::ip_address iRule | 21.1.0.4.0.19.3-ENG / 17.5.1.11.0.61.12-ENG / 17.1.3.7.0.21.4-ENG |
| [CVE-2026-116953](CVE-2026-116953) | F5 BIG-IP | 4.0 9.3 (F5); 3.1 9.8 (F5) | BIG-IP 21.1.0 / 17.5.0-17.5.1 / 17.1.0-17.1.3 with GENERICMESSAGE::route iRule | 21.1.0.4.0.19.3-ENG / 17.5.1.11.0.61.12-ENG / 17.1.3.7.0.21.4-ENG |
| [CVE-2026-131287](CVE-2026-131287) | Splunk SOAR | 3.1 9.6 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 |
| [CVE-2026-132142](CVE-2026-132142) | DrayTek Vigor2960 | 4.0 9.4 (VulDB); 3.1 9.1 (VulDB) | Vigor2960 1.5.1.0-1.5.1.6 | 1.5.1.7 |
| [CVE-2026-132143](CVE-2026-132143) | DrayTek Vigor2960 | 4.0 9.4 (VulDB); 3.1 9.9 (VulDB) | Vigor2960 1.5.1.0-1.5.1.6 | 1.5.1.7 |
| [CVE-2026-132141](CVE-2026-132141) | DrayTek Vigor2960 | 4.0 9.4 (VulDB); 3.1 9.9 (VulDB) | Vigor2960 1.5.1.0-1.5.1.6 | 1.5.1.7 |
| [CVE-2026-131253](CVE-2026-131253) | Splunk SOAR | 3.1 9.9 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 |
| [CVE-2026-132807](CVE-2026-132807) | UniFi Access Application | 3.1 9 (Ubiquiti) | UniFi Access Application <4.3.24 | 4.3.24 |
| [CVE-2026-123637](CVE-2026-123637) | BIG-IP | 4.0 9.3 (F5); 3.1 9.8 (F5) | BIG-IP APM 21.1.0 / 17.5.0-17.5.1 / 17.1.0-17.1.3 | 工程熱修復 BIGIP-21.1.0.4.0.19.3-ENG3 / BIGIP-17.5.1.11.0.61.12-ENG3 / BIGIP-17.1.3.7.0.21.4-ENG3（F5 K000163937） |
| [CVE-2026-104099](CVE-2026-104099) | Fabio | 3.1 9.1 (GHSA) | Fabio <1.7.3 | 1.7.3 |
| [CVE-2026-131202](CVE-2026-131202) | Splunk Enterprise Security | 3.1 9.1 (Splunk) | Splunk Enterprise Security <8.7.0 | 8.7.0 |
| [CVE-2026-131199](CVE-2026-131199) | Splunk Enterprise Security | 3.1 8.8 (Splunk) | Splunk Enterprise Security <8.7.0 | 8.7.0 |
| [CVE-2026-131236](CVE-2026-131236) | Splunk Enterprise Security | 3.1 8.8 (Splunk) | Splunk Enterprise Security <8.7.0 | 8.7.0 |
| [CVE-2026-131246](CVE-2026-131246) | Splunk SOAR | 3.1 8.8 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 |
| [CVE-2026-131252](CVE-2026-131252) | Splunk SOAR | 3.1 8.8 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 |
| [CVE-2026-131261](CVE-2026-131261) | Splunk SOAR | 3.1 8.8 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 |
| [CVE-2026-131263](CVE-2026-131263) | Splunk SOAR | 3.1 8.8 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 |
| [CVE-2026-131269](CVE-2026-131269) | Splunk SOAR | 3.1 8.8 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 |
| [CVE-2026-131270](CVE-2026-131270) | Splunk SOAR | 3.1 8.8 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 |
| [CVE-2026-131271](CVE-2026-131271) | Splunk SOAR | 3.1 8.8 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 |
| [CVE-2026-131295](CVE-2026-131295) | Splunk SOAR | 3.1 8.8 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 |
| [CVE-2026-131258](CVE-2026-131258) | Splunk SOAR | 3.1 8.7 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 |
| [CVE-2026-131260](CVE-2026-131260) | Splunk SOAR | 3.1 8.7 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 |
| [CVE-2026-131203](CVE-2026-131203) | Splunk Enterprise Security | 3.1 8.3 (Splunk) | Splunk Enterprise Security <8.7.0 | 8.7.0 |
| [CVE-2026-131209](CVE-2026-131209) | Splunk Enterprise Security | 3.1 8.3 (Splunk) | Splunk Enterprise Security <8.7.0 | 8.7.0 |
| [CVE-2026-131215](CVE-2026-131215) | Splunk Enterprise Security | 3.1 8.3 (Splunk) | Splunk Enterprise Security <8.7.0 | 8.7.0 |
| [CVE-2026-131218](CVE-2026-131218) | Splunk Enterprise Security | 3.1 8.3 (Splunk) | Splunk Enterprise Security <8.7.0 | 8.7.0 |
| [CVE-2026-131293](CVE-2026-131293) | Splunk SOAR | 3.1 8.3 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 |
| [CVE-2026-104129](CVE-2026-104129) | pREST | 3.1 8.1 (GHSA) | pREST <2.4.0 | 2.4.0 |
| [CVE-2026-123891](CVE-2026-123891) | SDDC Manager | 3.1 8.1 (VMware) | SDDC Manager 9.1.x.x / 9.0.x.x / 5.x | 9.1.1.0200 / 9.0.2.0100 / 5.2.5 |
| [CVE-2026-131200](CVE-2026-131200) | Splunk Enterprise Security | 3.1 8.1 (Splunk) | Splunk Enterprise Security <8.7.0 | 8.7.0 |
| [CVE-2026-131210](CVE-2026-131210) | Splunk Enterprise Security | 3.1 8.1 (Splunk) | Splunk Enterprise Security <8.7.0 | 8.7.0 |
| [CVE-2026-131282](CVE-2026-131282) | Splunk SOAR | 3.1 8.1 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 |
| [CVE-2026-131297](CVE-2026-131297) | Splunk SOAR | 3.1 8.1 (Splunk) | Splunk SOAR <8.8.0 | 8.8.0 |
| [CVE-2026-133493](CVE-2026-133493) | DIR-600L | 4.0 9.3 (VulDB); 3.1 10.0 (VulDB) | D-Link DIR-600L 2.17b02 | No fixed firmware confirmed |
| [CVE-2026-20320](CVE-2026-20320) | Cisco BroadWorks | 3.1 7.5 (Cisco) | BroadWorks earlier than RI.2026.07 | RI.2026.07 |
| [CVE-2026-111793](CVE-2026-111793) | Openwave Webtop Media Transcoder | 3.1 4.3 (MITRE) | Webtop Media Transcoder < 1.1.22.0 | 1.1.22.0 |
| [CVE-2026-126262](CVE-2026-126262) | FortiAnalyzer / FortiManager | 3.1 9.8 (Fortinet) | FortiAnalyzer 8.0.0-8.0.1 / 7.6.0-7.6.7 / 7.4.0-7.4.11 / 7.2.0-7.2.12; FortiManager (FA features) 8.0.0 / 7.6.0-7.6.7 / 7.4.0-7.4.11 / 7.2.0-7.2.12 | FortiAnalyzer 8.0.2 / FortiManager 8.0.1 / 7.6.8 / 7.4.12 / 7.2.13 |
| [CVE-2026-126261](CVE-2026-126261) | FortiManager | 3.1 9.8 (Fortinet) | FortiManager 8.0.0 / 7.6.0-7.6.7 / 7.4.0-7.4.5 / 7.2.0-7.2.8 | 8.0.1 / 7.6.8 / 7.4.6 / 7.2.9 |
| [CVE-2026-126259](CVE-2026-126259) | FortiOS | 3.1 9.8 (Fortinet) | FortiOS 8.0.0 / 7.6.0-7.6.7 / 7.4.0-7.4.12 / 7.2.0-7.2.13 / 7.0 all | 8.0.1 / 7.6.8 / 7.4.13 / 7.2.14 (7.0 migrate) |
| [CVE-2026-126254](CVE-2026-126254) | FortiOS / FortiSASE | 3.1 9.6 (Fortinet) | FortiOS 8.0.0-8.0.1 / 7.6.0-7.6.7 / 7.4.0-7.4.12 / 7.2.0-7.2.13; FortiSASE 26.3.1, 26.2/26.1/25.x | 8.0.2 / 7.6.8 / 7.4.13 / 7.2.14; FortiSASE 26.3.2 (26.2 and earlier migrate) |
| [CVE-2026-126253](CVE-2026-126253) | FortiOS / FortiSASE | 3.1 9.3 (Fortinet) | FortiOS 8.0.0-8.0.1 / 7.6.0-7.6.7 / 7.4.0-7.4.12 / 7.2.0-7.2.13 / 7.0.1-7.0.19; FortiSASE 26.3.1, 26.2/26.1/25.x | 8.0.2 / 7.6.8 / 7.4.13 / 7.2.14; FortiSASE 26.3.2 (26.2 and earlier, 7.0 migrate) |
| [CVE-2026-126229](CVE-2026-126229) | FortiManager / FortiAnalyzer | 3.1 9.1 (Fortinet) | FortiManager / FortiAnalyzer 8.0.0-8.0.1 / 7.6.0-7.6.7 / 7.4.0-7.4.11 / 7.2.0-7.2.12 / 7.0 all | 8.0.2 / 7.6.8 / 7.4.12 / 7.2.13 (7.0 migrate) |
| [CVE-2026-126260](CVE-2026-126260) | FortiAnalyzer / FortiManager | 3.1 9.0 (Fortinet) | FortiAnalyzer / FortiManager 8.0.0 / 7.6.0-7.6.7 / 7.4.0-7.4.11 (7.2 not affected) | 8.0.1 / 7.6.8 / 7.4.12 |
| [CVE-2026-133993](CVE-2026-133993) | D-Link DIR-600L | 4.0 9.3 (NVD); 3.1 10.0 (NVD) | 2.17b02 |  |
| [CVE-2026-105016](CVE-2026-105016) | Microsoft QUIC (msquic) | 3.1 9.8 (Microsoft) | Microsoft QUIC (msquic) before the October 13, 2026 fixes; any service built on a vulnerable msquic (HTTP/3 servers, QUIC services) | Microsoft October 13, 2026 updates — Windows 11 builds 10.0.26100.9711 / 10.0.26200.9711 / 10.0.26300.9711 (KB5127648); .NET 8.0.32 / 9.0.21 / 10.0.14 |
| [CVE-2026-133680](CVE-2026-133680) | D-Link DCS-935L | 3.1 9.9 (VulDB); 4.0 8.6 (VulDB) | D-Link DCS-935L 1.10.01 | Unknown — no fixed firmware version identified in VulDB/NVD as of 2026-11-22 |
| [CVE-2026-129794](CVE-2026-129794) | SOES (Simple Open EtherCAT Slave) | 3.1 8.8 (RT-Labs) | SOES up to and including 3.2.0 | 3.2.1 |
| [CVE-2026-129796](CVE-2026-129796) | SOES (Simple Open EtherCAT Slave) | 3.1 8.8 (RT-Labs) | SOES up to and including 3.2.0 | 3.2.1 |
| [CVE-2026-133985](CVE-2026-133985) | TEW-657BRM | 3.1 8.8 (VulDB); 4.0 7.4 (VulDB) | TEW-657BRM 1.00.1 |  |
| [CVE-2026-134352](CVE-2026-134352) | Rclone | 4.0 9.2 (VulnCheck); 3.1 8.1 (VulnCheck) | Rclone from 1.51.0 before 1.76.0 | 1.76.0 |
| [CVE-2026-124010](CVE-2026-124010) | XWEB EVO | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | XWEB EVO before 5.6.2 | 5.6.2 |
| [CVE-2026-124014](CVE-2026-124014) | XWEB EVO | 4.0 8.8 (VulnCheck); 3.1 9.1 (VulnCheck) | XWEB EVO 4.3.0 through 5.8.8 |  |
| [CVE-2026-102764](CVE-2026-102764) | BeyondTrust Remote Support | 4.0 9.3 (NVD) | BeyondTrust Remote Support <= 26.2.3 (self-hosted); Privileged Remote Access shares the affected code | BT26-05-RS patch (supported builds 24.3.1-26.2.3); BeyondTrust-hosted SaaS auto-patched 2026-10-08/09 |
| [CVE-2026-103782](CVE-2026-103782) | Dell Enterprise Sonic Distribution | 3.1 9.9 (Dell) | Dell Enterprise Sonic Distribution prior to 4.6.1 | 4.6.1 |
| [CVE-2026-135171](CVE-2026-135171) | Wing FTP Server | 4.0 9.2 (VulnCheck); 3.1 8.1 (VulnCheck) | Wing FTP Server before 8.2.8 | 8.2.8 |
| [CVE-2026-115873](CVE-2026-115873) | Cribl Stream | 4.0 8.7 (Cribl); 3.1 9.9 (Cribl) | Cribl Stream 4.20.4 and earlier | 4.21.0 |
| [CVE-2026-115899](CVE-2026-115899) | Cribl Stream | 4.0 9.3 (Cribl); 3.1 9.8 (Cribl) | Cribl Stream 4.20.4 and earlier | 4.21.0 |
| [CVE-2026-115901](CVE-2026-115901) | Cribl Stream | 4.0 8.5 (Cribl); 3.1 9.0 (Cribl) | Cribl Stream 4.20.4 and earlier | 4.21.0 |
| [CVE-2026-134882](CVE-2026-134882) | TOTOLINK A7100RU | 4.0 10.0 (VulDB); 3.1 10.0 (VulDB) | TOTOLINK A7100RU 7.4cu.2313_B20191024 |  |
| [CVE-2026-101218](CVE-2026-101218) | Dell Enterprise Sonic Distribution | 3.1 8.2 (Dell) | Dell Enterprise Sonic Distribution before 4.6.1 | 4.6.1 |
| [CVE-2026-103783](CVE-2026-103783) | Dell Enterprise Sonic Distribution | 3.1 8.2 (Dell) | Dell Enterprise Sonic Distribution before 4.6.1 | 4.6.1 |
| [CVE-2026-103788](CVE-2026-103788) | Dell Enterprise Sonic Distribution | 3.1 9.6 (Dell) | Dell Enterprise Sonic Distribution before 4.6.1 | 4.6.1 |
| [CVE-2026-134624](CVE-2026-134624) | N-able MailAssure (SpamExperts) | 4.0 9.3 (N-able) | N-able MailAssure (SpamExperts) before 20261121.1943 | 20261121.1943 |
| [CVE-2026-110631](CVE-2026-110631) | Komodo Periphery | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | Komodo through 2.3.3 (default install: no core_public_keys / passkeys configured) |  |
| [CVE-2026-114203](CVE-2026-114203) | ASUS GPU Tweak III | 4.0 9.3 (ASUS) | ASUS GPU Tweak III V.1.6.9.4 to v2.2.1.1 (Mobile Module service installed) | v2.2.2.3 |
| [CVE-2026-70229](CVE-2026-70229) | Active Directory Domain Services | 3.1 8.1 (Microsoft) | Windows Server with Active Directory Domain Services | 2026 年 10 月安全更新 |
| [CVE-2026-109480](CVE-2026-109480) | Profile Data Roaming Service | 3.1 9.6 (Microsoft) | Profile Data Roaming Service |  |
| [CVE-2026-115900](CVE-2026-115900) | Cribl Stream | 4.0 8.7 (Cribl); 3.1 8.8 (Cribl) | Cribl Stream 4.20.4 and earlier | 4.21.0 |
| [CVE-2026-118286](CVE-2026-118286) | Azure Site Recovery | 3.1 9.1 (Microsoft) | Azure Site Recovery |  |
| [CVE-2026-62841](CVE-2026-62841) | Azure Event Grid | 3.1 10.0 (Microsoft) | Azure Event Grid |  |
| [CVE-2026-69899](CVE-2026-69899) | Azure DevTest Labs | 3.1 9.1 (Microsoft) | Azure DevTest Labs |  |
| [CVE-2026-76418](CVE-2026-76418) | Cisco Secure Firewall ASA / FTD (Remote Access SSL VPN) | 3.1 8.6 (Cisco) | Cisco Secure Firewall ASA Software and Cisco Secure Firewall Threat Defense (FTD) Software with SSL remote access VPN enabled and secondary authentication configured on a tunnel group | ASA 9.16.4.104 / 9.18.4.96 / 9.20.4.50 / 9.22.3.200 / 9.23.1.48 / 9.24.1.27 / 9.24.10.1; FTD 7.0.11 / 7.2.13 / 7.4.9 / 7.6.7 / 7.7.14 / 10.0.3 / 10.1.1 |
| [CVE-2026-105304](CVE-2026-105304) | Zoraxy | 4.0 7.7 (JPCERT); 3.0 8.6 (JPCERT) | Zoraxy <= v3.3.5-rc1 | v3.3.5-rc2 |
| [CVE-2026-121613](CVE-2026-121613) | ifm Camera Products | 4.0 9.3 (CERT VDE); 3.1 9.8 (CERT VDE) | ifm 相機產品 O3D/O3X 系列（固件 1.20.6381 / 1.71.10735 / 1.90.107 / 1.90.119 / 2.0.10412 / 2.10.16，按型號） |  |
| [CVE-2026-80466](CVE-2026-80466) | WAGO Web-Based Management | 4.0 8.7 (CERT VDE); 3.1 8.8 (CERT VDE) | WAGO CC100 / PFC100 G2 / PFC200 G2 / TP600 / Edge Controller / WP400（wago_os_linux < 4.10.0） | 4.10.0 |
| [CVE-2026-86312](CVE-2026-86312) | Apache Solr | 3.1 8.8 (Apache) | Apache Solr 9.0.0 through before 9.11.0 (9.x) and before 10.1.0 (10.x) | 9.11.0 / 10.1.0 |
| [CVE-2026-134753](CVE-2026-134753) | dsniff | 4.0 8.3 (VulnCheck) | dsniff (hackerschoice/dsniff fork), decode_sniffer.c decode_sniffer() |  |
| [CVE-2024-6387](CVE-2024-6387) | OpenSSH | 3.1 8.1 (NVD) | OpenSSH 8.5p1–9.7p1 | 9.8p1 |
| [CVE-2026-86060](CVE-2026-86060) | MikroTik RouterOS | 4.0 9.2 (CERT Polska); 3.1 9.8 (NVD) | RouterOS before 7.24.2 (Stable), before 7.23.4 (Long-term), before 6.49.21 (Long-term) | 7.24.2 (Stable); 7.23.4 (Long-term); 6.49.21 (Long-term) |
| [CVE-2026-88771](CVE-2026-88771) | Citrix NetScaler ADC / Gateway | 4.0 9.5 (Citrix); 3.1 9.8 (NVD) | NetScaler ADC 14.1 before 14.1-73.37, 13.1 before 13.1-64.23, 14.1-FIPS before 14.1-73.37, 13.1-FIPS/NDcPP before 13.1.37.279; NetScaler Gateway 14.1 before 14.1-73.37, 13.1 before 13.1-64.23 | 14.1-73.37 and later; 13.1-64.23 and later; 14.1-73.37 FIPS and later; 13.1.37.279 FIPS/NDcPP and later |
| [CVE-2026-88772](CVE-2026-88772) | Citrix NetScaler ADC / Gateway | 4.0 9.5 (Citrix); 3.1 8.1 (NVD) | NetScaler ADC 14.1 before 14.1-73.37, 13.1 before 13.1-64.23, 14.1-FIPS before 14.1-73.37, 13.1-FIPS/NDcPP before 13.1.37.279; NetScaler Gateway 14.1 before 14.1-73.37, 13.1 before 13.1-64.23; requires DTLS enabled (on by default for VPN virtual servers) | 14.1-73.37 and later; 13.1-64.23 and later; 14.1-73.37 FIPS and later; 13.1.37.279 FIPS/NDcPP and later |
| [CVE-2026-136411](CVE-2026-136411) | BusyBox | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | BusyBox through 1.38.0, tftpd started without a DIR argument (no chroot, no chdir) | Upstream commit b67f7b7d14ac98ca84491718d364b955d21a9cd5 (tftpd: strip leading slashes from the requested file name) |
| [CVE-2026-19586](CVE-2026-19586) | TP-Link Omada Gateways | 4.0 9.3 (CNA); 3.1 9.8 (NVD) | Omada gateways with the SSL VPN (OpenVPN) server enabled; shared checkpsw.sh authentication code across the Omada gateway range | Fixed firmware per model (TP-Link FAQ 5256; 19 models, e.g. ER605 V2 2.4.4 Build 20260630 Rel.14398, ER7406 V1 1.3.4 Build 20260625 Rel.43136) |
| [CVE-2026-24061](CVE-2026-24061) | GNU InetUtils telnetd | 3.1 9.8 (MITRE) | GNU InetUtils telnetd through 2.7 | Upstream fix commit ccba9f748aa8d50a38d7748e2e60362edd6a32cc |
| [CVE-2026-84869](CVE-2026-84869) | ScreenConnect | 3.1 9.9 (ConnectWise) | ScreenConnect client before 26.6.5 (Client Support and Access sessions, cloud and on-premise; servers not impacted) | 26.6.5 |
| [CVE-2026-136126](CVE-2026-136126) | c-icap-server | 4.0 9.2 (VulnCheck); 3.1 8.1 (VulnCheck) | c-icap-server through 0.5.15 and 0.6.5 | unknown |
| [CVE-2026-136404](CVE-2026-136404) | n2n | 4.0 9.3 (VulnCheck); 3.1 9.8 (GHSA) | n2n 3.0 through 3.1.1 | No fixed release yet |
| [CVE-2026-136547](CVE-2026-136547) | RX3 | 4.0 9.3 (VulDB); 3.1 10.0 (VulDB) | Tenda RX3 firmware V16.03.13.11_multi | unknown |
| [CVE-2026-111214](CVE-2026-111214) | pfSense | 4.0 8.6 (VulnCheck); 3.1 7.2 (VulnCheck) | pfSense CE 2.7.0 through 2.9.0; pfSense Plus through 26.07 | 2.9.1 / 26.07.1 |
| [CVE-2026-103406](CVE-2026-103406) | Session Smart Conductor | 3.1 9.8 (Juniper) | Session Smart Conductor 與 Session Smart Router 7.0.5 / 7.1.7 / 7.2.3 之前的所有版本 | 7.0.5 / 7.1.7 / 7.2.3 |
| [CVE-2026-134287](CVE-2026-134287) | OpenRemote | 4.0 9.2 (VulnCheck); 3.1 7.7 (VulnCheck) | OpenRemote core before 1.34.0 | 1.34.0 |
| [CVE-2026-135300](CVE-2026-135300) | Pomerium | 4.0 9.1 (VulnCheck); 3.1 7.4 (VulnCheck) | Pomerium 0.30.0 to before 0.34.0 | 0.34.0 |
| [CVE-2026-18963](CVE-2026-18963) | Keycloak | 3.1 9.1 (Red Hat) | Red Hat build of Keycloak 26.4, 26.6; Red Hat Single Sign-On 7.6 | 26.4.15, 26.6.6 (RHSA-2026:56520, RHSA-2026:56523) |
| [CVE-2026-34197](CVE-2026-34197) | Apache ActiveMQ | 3.1 8.8 (Apache) | Apache ActiveMQ Broker / ActiveMQ before 5.19.4; 6.0.0 before 6.2.3 | 5.19.4 or 6.2.3 |
| [CVE-2026-42945](CVE-2026-42945) | NGINX | 4.0 9.2 (F5); 3.1 8.1 (F5) | NGINX Open Source 0.6.27 through 1.30.0; NGINX Plus R32 through R36 | NGINX Open Source 1.31.0 / 1.30.1; NGINX Plus R36 P4 / R32 P6 |
| [CVE-2023-25914](CVE-2023-25914) | AK-SM 800A | 3.1 8.8 (DIVD) | AK-SM 800A firmware 3.3 及之前版本（NVD CPE） | Danfoss 建議安裝 3.3 補丁（DIVD-2023-00025） |
| [CVE-2023-25915](CVE-2023-25915) | AK-SM 800A | 3.1 9.9 (DIVD); 3.1 8.8 (NVD) | AK-SM 800A firmware 3.3 及之前版本（NVD CPE） | Danfoss 建議安裝 3.3 補丁（DIVD-2023-00025） |
| [CVE-2025-41450](CVE-2025-41450) | AK-SM 8xxA Series | 3.1 8.2 (Danfoss); 3.1 7.5 (NVD) | AK-SM 8xxA Series 4.2 之前版本 | 4.2 |
| [CVE-2026-133275](CVE-2026-133275) | MiCollab | 3.1 5.3 (Mitel) | MiCollab 10.3 (10.3.0.18) and earlier | Patch for 10.3 (10.3.0.18) (MISA-2026-0012) |
| [CVE-2026-133311](CVE-2026-133311) | MiCollab | 3.1 5.9 (Mitel) | MiCollab 10.3 (10.3.0.18) and earlier | Patch for 10.3 (10.3.0.18) (MISA-2026-0012) |
| [CVE-2026-133324](CVE-2026-133324) | MiCollab | 3.1 5.3 (Mitel) | MiCollab 10.3 (10.3.0.18) and earlier | Patch for 10.3 (10.3.0.18) (MISA-2026-0012) |
| [CVE-2026-42588](CVE-2026-42588) | ActiveMQ | 3.1 8.1 (Apache) | ActiveMQ 5.19.7 之前版本；6.0.0–6.2.6 之前版本 | 5.19.7 / 6.2.6 |
| [CVE-2026-136821](CVE-2026-136821) | R32 | 4.0 8.6 (VulDB); 3.1 9.9 (VulDB) | D-Link R32 A1 firmware 1.10B02 | unknown |
| [CVE-2026-136822](CVE-2026-136822) | R32 | 4.0 8.6 (VulDB); 3.1 9.9 (VulDB) | D-Link R32 A1 firmware 1.10B02 | unknown |
| [CVE-2026-136823](CVE-2026-136823) | R32 | 4.0 9.3 (VulDB); 3.1 10.0 (VulDB) | D-Link R32 A1 firmware 1.10B02 | unknown |
| [CVE-2026-137043](CVE-2026-137043) | TOTOLINK N350RT | 3.1 10.0 (VulDB); 4.0 9.3 (VulDB) | TOTOLINK N350RT 9.3.5u.6468_B20250827 / 9.3.5u.6466_B20250825 | No fixed release yet |
| [CVE-2026-135150](CVE-2026-135150) | Eclipse Ditto | 4.0 9.1 (Eclipse) | Eclipse Ditto 1.1.0–3.9.9（nginx 反向代理配置：Helm chart、Docker Compose、Kubernetes、OpenShift）；Helm chart ≤ 4.9.0 | Not patched yet (fix in preparation for 3.9.10 / 3.8.16) |
| [CVE-2026-135788](CVE-2026-135788) | D-Link DIR-X1860 | 3.1 9.9 (VulDB); 4.0 8.6 (VulDB) | DIR-X1860 韌體 4.5.2 (/usr/sbin/anweb) | No fixed release yet |
| [CVE-2026-135789](CVE-2026-135789) | D-Link R95 | 3.1 9.1 (VulDB); 4.0 8.5 (VulDB) | R95 韌體 101B06（GetBluetoothAdapterSettings / GetBluetoothBloodPressure / GetBluetoothDeviceList / GetBluetoothScanDeviceList / SetBluetooth*） | No fixed release yet |
| [CVE-2026-136548](CVE-2026-136548) | Tenda RX3 | 3.1 10.0 (VulDB); 4.0 9.3 (VulDB) | RX3 韌體 16.03.13.11 (/bin/auto_discover) | No fixed release yet |
| [CVE-2026-136549](CVE-2026-136549) | Tenda RX3 | 3.1 10.0 (VulDB); 4.0 9.3 (VulDB) | RX3 韌體 16.03.13.11_multi (/goform/SetRemoteWebCfg) | No fixed release yet |
| [CVE-2026-136550](CVE-2026-136550) | Tenda RX3 | 3.1 9.1 (VulDB); 4.0 8.5 (VulDB) | RX3 韌體 16.03.13.11_multi (/goform/AdvSetMacMtuWan) | No fixed release yet |
| [CVE-2026-136552](CVE-2026-136552) | Tenda RX3 | 3.1 9.1 (VulDB); 4.0 8.5 (VulDB) | RX3 韌體 16.03.13.11_multi (/goform/setIPv6Status) | No fixed release yet |
| [CVE-2026-136553](CVE-2026-136553) | Tenda RX3 | 3.1 10.0 (VulDB); 4.0 9.3 (VulDB) | RX3 韌體 16.03.13.11_multi (/goform/fast_setting_wifi_set) | No fixed release yet |
| [CVE-2026-0322](CVE-2026-0322) | Palo Alto Networks PAN-OS | 4.0 8.6 (Palo Alto Networks); 3.1 7.2 (NVD) | PAN-OS 12.2 < 12.2.4、12.1 < 12.1.4-h12 / 12.1.7-h8 / 12.1.10-h2、11.2 < 11.2.4-h22 / 11.2.7-h21 / 11.2.10-h15 / 11.2.13-h3 / 11.2.16、11.1 < 11.1.4-h37 / 11.1.6-h39 / 11.1.7-h11 / 11.1.10-h35 / 11.1.13-h15 / 11.1.16-h3、10.2 < 10.2.7-h38 / 10.2.10-h41 / 10.2.13-h26 / 10.2.16-h11 / 10.2.18-h12（PA-Series、VM-Series 防火牆與 Panorama） | 12.2.4 / 12.1.10-h2 / 11.2.16 / 11.1.16-h3 / 10.2.18-h12（各分支最新修復版；另有中期 hotfix，見廠商通告） |
| [CVE-2026-105133](CVE-2026-105133) | AhsayCBS | 4.0 6.9 (VulDB); 3.1 7.3 (VulDB) | AhsayCBS up to 9.15.2.69 / 10.3.4.44 | 9.15.2.70 / 10.3.4.45 |
| [CVE-2026-105134](CVE-2026-105134) | AhsayCBS | 4.0 10.0 (VulDB); 3.1 10.0 (VulDB) | AhsayCBS up to 9.15.2.69 / 10.3.4.44 | 9.15.2.70 / 10.3.4.45 |
| [CVE-2026-106931](CVE-2026-106931) | EG Secure Solutions SiteGuard Server Edition | 4.0 8.5 (JPCERT/CC); 3.0 7.8 (JPCERT/CC) | SiteGuard Server Edition Ver2.20 及以上、Ver8.00 Update 5 之前（Apache httpd、Nginx、IIS）；FreeBSD 版 Ver7.00 Update 6 之前；IIS Ver3.10 至 Ver4.00 Update 4 不受影響；需啟用統計功能（預設啟用） | Ver8.00 Update 5；FreeBSD 版 Ver7.00 Update 6 |
| [CVE-2026-114625](CVE-2026-114625) | Arista VeloCloud Orchestrator | 3.1 9.9 (Arista); 4.0 9.4 (Arista) | VeloCloud Orchestrator (VCO) on-prem 5.2.x < 5.2.3.18、6.1.x < 6.1.3.10、6.4.x < 6.4.2.12 | 5.2.3.18 / 6.1.3.10 / 6.4.2.12 |
| [CVE-2026-76519](CVE-2026-76519) | Cisco Secure Email Gateway | 3.1 9.8 (Cisco) | Cisco Secure Email Gateway（AsyncOS 15.5 < 15.5.5-014、16.0 全版本、16.5 < 16.5.0-780），需同時滿足：AMP File Reputation 已啟用並指派至郵件政策，且 Content Scanner Tools < 25.3.0.5525 | AsyncOS 15.5.5-014 / 16.5.0-780，或 Content Scanner Tools ≥ 25.3.0.5525 |
| [CVE-2026-88779](CVE-2026-88779) | Citrix NetScaler ADC / Gateway | 4.0 8.7 (Citrix); 3.1 7.5 (NVD) | NetScaler ADC < 14.1-73.41、< 13.1-64.28、FIPS < 14.1-73.41、< 13.1-37.282；NetScaler Gateway < 14.1-73.41、< 13.1-64.28 | ADC 14.1-73.41 / 13.1-64.28；Gateway 14.1-73.41 / 13.1-64.28 |
| [CVE-2026-135790](CVE-2026-135790) | Panabit Smart Application Gateway TANGr7p10 | 3.1 9.9 (VulDB); 4.0 8.6 (VulDB) | TANGr7p10（/cgi-bin/dashboard/ajax_chart_dump，參數 isntmeye） | No fixed release yet |
| [CVE-2026-135791](CVE-2026-135791) | Panabit Smart Application Gateway TANGr7p10 | 3.1 9.9 (VulDB); 4.0 8.6 (VulDB) | TANGr7p10（/cgi-bin/flowcontrol/ajax_data_pie，函數 edit_data_pie，參數 Name） | No fixed release yet |
| [CVE-2026-135792](CVE-2026-135792) | Panabit Smart Application Gateway TANGr7p10 | 3.1 10.0 (VulDB); 4.0 9.3 (VulDB) | TANGr7p10（user.cgi，函數 send_email_authcode，參數 Username） | No fixed release yet |
| [CVE-2026-135793](CVE-2026-135793) | Panabit Smart Application Gateway TANGr7p10 | 3.1 9.9 (VulDB); 4.0 8.6 (VulDB) | TANGr7p10（/admin/cgi-bin/sac/ajax_sac_ap，函數 import_upgrde/upload_modkey，參數 file/filename） | No fixed release yet |
| [CVE-2026-135794](CVE-2026-135794) | Panabit Smart Application Gateway TANGr7p10 | 3.1 9.9 (VulDB); 4.0 8.6 (VulDB) | TANGr7p10（admin/cgi-bin/sac/ajax_sac_crontab，函數 add_crontab，參數 cmd） | No fixed release yet |
| [CVE-2026-135796](CVE-2026-135796) | Volans NGFW Next-Generation Firewall r5.1 | 3.1 9.9 (VulDB); 4.0 8.6 (VulDB) | r5.1（modules/assets/port_serve_scan.mds，函數 exec/system，參數 task_name/where/path） | No fixed release yet |
| [CVE-2026-135797](CVE-2026-135797) | Volans NGFW Next-Generation Firewall r5.1 | 3.1 10.0 (VulDB); 4.0 9.3 (VulDB) | r5.1（sslvpn/sslvpn_client.php，函數 exec，參數 img） | No fixed release yet |
| [CVE-2015-3306](CVE-2015-3306) | ProFTPD | 3.1 10.0 (CISA-ADP) | ProFTPD 1.3.5（mod_copy 模組啟用時） | 1.3.5a / 1.3.6rc1 |
| [CVE-2015-5477](CVE-2015-5477) | ISC BIND | 3.1 7.5 (CISA-ADP) | ISC BIND 9.x < 9.9.7-P2、9.10.x < 9.10.2-P3 | 9.9.7-P2 / 9.10.2-P3 |
| [CVE-2025-61624](CVE-2025-61624) | Fortinet FortiOS / FortiPAM / FortiProxy | 3.1 6.0 (Fortinet); 3.1 6.5 (NVD) | FortiOS 7.6.0–7.6.4、7.4.0–7.4.9、7.2 / 7.0 / 6.4 全部版本；FortiPAM 1.7.0、1.6–1.0 全部版本；FortiProxy 7.6.0–7.6.4、7.4.0–7.4.11、7.2 / 7.0 全部版本；FortiSwitchManager 7.2.0–7.2.7、7.0.0–7.0.6 | FortiOS 7.6.5 / 7.4.10；FortiPAM 1.7.1；FortiProxy 7.6.5 / 7.4.12；FortiSwitchManager 7.2.8 / 7.0.7；其餘分支需遷移至修復版本 |
| [CVE-2026-104286](CVE-2026-104286) | Fortinet FortiMail | 3.1 9.8 (Fortinet) | FortiMail 8.0.0–8.0.1、7.6.0–7.6.6、7.4.0–7.4.8、7.2.0–7.2.9、7.0 全部版本 | 8.0.2 / 7.6.7 / 7.4.9 / 7.2.10（通告發布時尚未發布）；7.0 需遷移至修復版本 |
| [CVE-2026-96652](CVE-2026-96652) | Plex Media Server | 4.0 5.3 (CISA); 3.1 4.3 (CISA) | Plex Media Server 1.43.3.10861 之前 | 1.43.3.10861 |
| [CVE-2026-96654](CVE-2026-96654) | Plex Media Server | 4.0 6.9 (CISA); 3.1 6.5 (CISA) | Plex Media Server 1.43.3.10861 之前 | 1.43.3.10861 |
| [CVE-2026-96655](CVE-2026-96655) | Plex Media Server | 4.0 5.3 (CISA); 3.1 4.3 (CISA) | Plex Media Server 1.43.3.10861 之前 | 1.43.3.10861 |
| [CVE-2026-96656](CVE-2026-96656) | Plex Media Server | 4.0 8.6 (CISA); 3.1 7.2 (CISA) | Plex Media Server 1.43.3.10861 之前（管理員權限） | 1.43.3.10861 |
| [CVE-2026-16232](CVE-2026-16232) | Check Point SmartConsole | 3.1 9.1 (GHSA) | Security Management / MDS：R77.30、R80–R80.30、R81–R82.10 | Jumbo Hotfix：R82.10 Take 36+ / R82 Take 118+ / R81.20 Take 158+ |
| [CVE-2026-115576](CVE-2026-115576) | NetBird | 3.1 8.8 (GHSA) | NetBird 0.5.0 through 0.75.1 | 0.76.0 |
| [CVE-2026-123685](CVE-2026-123685) | StellarProtect Linux / Stellar Agent (Linux) | 4.0 8.7 (TXOne); 3.1 8.8 (TXOne) | StellarProtect Linux 1.0 and earlier; Stellar Agent (Linux) before 1.2.54 | Stellar Agent (Linux) 1.2.54 |
| [CVE-2026-123689](CVE-2026-123689) | StellarOne | 4.0 8.6 (TXOne); 3.1 8.1 (TXOne) | StellarOne before 5.0.3232 | 5.0.3232 |
| [CVE-2026-133971](CVE-2026-133971) | HPE Networking Management Software (AirWave) | 3.1 9.8 (HPE) | AirWave 8.3.0.7 and below | 8.3.0.8 and above |
| [CVE-2026-133972](CVE-2026-133972) | HPE Networking Management Software (AirWave) | 3.1 9.8 (HPE) | AirWave 8.3.0.7 and below | 8.3.0.8 and above |
| [CVE-2026-66784](CVE-2026-66784) | Submariner | 3.1 8.7 (Red Hat) | Submariner (default Pre-Shared Key mode) | unknown |
| [CVE-2026-137077](CVE-2026-137077) | FreeRDP | 4.0 8.3 (VulnCheck); 3.1 8.2 (GHSA) | FreeRDP <= 3.32.2 | 3.33.0 |
| [CVE-2026-137704](CVE-2026-137704) | DWM-222W | 4.0 8.6 (TWCERT); 3.1 8.8 (TWCERT) | DWM-222W（hardware revision B1）firmware v1.02.00 及更早版本 | v1.02.04 |
| [CVE-2026-137481](CVE-2026-137481) | Traefik | 4.0 7.8 (VulnCheck); 3.1 9.3 (VulnCheck) | Traefik < 2.11.62；3.x < 3.7.18；3.8.0-rc.1（3.0–3.6 已 EOL，不修補） | 2.11.62；3.7.18；3.8.0-rc.2 |
| [CVE-2026-137721](CVE-2026-137721) | OpenScape 4000 and OpenScape 4000 Manager | 3.1 10.0 (Mitel) | OpenScape 4000 V11 R0.22–V11 R2.11，V10 R1.68 及更早版本；OpenScape 4000 Manager V11 R0.22–V11 R2.11，V10 R1.34–V10 R1.68 | V11 R2.14 或更新版本；V11 R1.26 有 PLT HF5；V10 R0.28–V11 R0.22（OpenScape 4000）／V10 R1.34–V11 R0.22（Manager）有修補程式 |
| [CVE-2026-137723](CVE-2026-137723) | OpenScape 4000 and OpenScape 4000 Manager | 3.1 9.6 (Mitel) | OpenScape 4000 V11 R0.22–V11 R2.11，V10 R1.68 及更早版本；OpenScape 4000 Manager V11 R0.22–V11 R2.11，V10 R1.34–V10 R1.68 | V11 R2.14 或更新版本；V11 R1.26 有 PLT HF5；V10 R0.28–V11 R0.22（OpenScape 4000）／V10 R1.34–V11 R0.22（Manager）有修補程式 |
| [CVE-2026-137724](CVE-2026-137724) | OpenScape 4000 and OpenScape 4000 Manager | 3.1 10.0 (Mitel) | OpenScape 4000 V11 R0.22–V11 R2.11，V10 R1.68 及更早版本；OpenScape 4000 Manager V11 R0.22–V11 R2.11，V10 R1.34–V10 R1.68 | V11 R2.14 或更新版本；V11 R1.26 有 PLT HF5；V10 R0.28–V11 R0.22（OpenScape 4000）／V10 R1.34–V11 R0.22（Manager）有修補程式 |
| [CVE-2026-137738](CVE-2026-137738) | RealVNC Server | 3.1 9.8 (GHSA) | RealVNC Server 6.4.0–7.19.0；RealVNC Viewer 8.4.0–8.6.1；RealVNC Classic Viewer 6.4.0–7.18.2；RealVNC Connect App 8.6.1 及更早版本；RealVNC On-Demand Assist 3.4.1 及更早版本；RealVNC Viewer iOS 3.7.0–4.9.5；RealVNC Viewer Android 3.5.0–4.9.5；RealVNC Server iOS 2.8.1 及更早版本；RealVNC Server Android 2.8.3 及更早版本 | RealVNC Server 7.19.1；RealVNC Viewer 8.6.2；RealVNC Classic Viewer 7.18.3；RealVNC Connect App 8.6.2；RealVNC On-Demand Assist 3.5.0；RealVNC Viewer iOS 4.9.6；RealVNC Viewer Android 4.9.6；RealVNC Server iOS 2.8.2；RealVNC Server Android 2.8.4 |
| [CVE-2026-63341](CVE-2026-63341) | aedes | 3.1 7.5 (GHSA) | aedes <= 1.1.0 | 1.1.1 |
| [CVE-2026-80453](CVE-2026-80453) | Dell Secure Connect Gateway - Virtual Edition | 3.1 8.4 (Dell) | Dell Secure Connect Gateway - Virtual Edition < 5.36.00.16 | 5.36.00.16 |
| [CVE-2026-80472](CVE-2026-80472) | Dell Secure Connect Gateway - Virtual Edition | 3.1 8.1 (Dell) | Dell Secure Connect Gateway - Virtual Edition < 5.36.00.16 | 5.36.00.16 |
| [CVE-2026-80477](CVE-2026-80477) | Dell Secure Connect Gateway - Virtual Edition | 3.1 8.4 (Dell) | Dell Secure Connect Gateway - Virtual Edition < 5.36.00.16 | 5.36.00.16 |
| [CVE-2026-80485](CVE-2026-80485) | Secure Connect Gateway - Virtual Edition | 3.1 8.4 (Dell) | Secure Connect Gateway - Virtual Edition < 5.36.00.16 | 5.36.00.16 |
| [CVE-2026-123761](CVE-2026-123761) | PowerDNS Authoritative Server | 3.1 8.2 (Open-Xchange) | PowerDNS Authoritative Server 5.x ≤ 5.0.8 / 5.1.5 | 5.0.9 / 5.1.6 |
| [CVE-2026-80507](CVE-2026-80507) | Dell Secure Connect Gateway - Virtual Edition | 3.1 8.4 (Dell) | Dell Secure Connect Gateway - Virtual Edition < 5.36.00.16 | 5.36.00.16 |
| [CVE-2026-138003](CVE-2026-138003) | TEW-751DR / TEW-733GR | 4.0 9.0 (VulDB); 3.1 9.0 (VulDB) | TEW-751DR / TEW-733GR 1.03B01 |  |
| [CVE-2026-138004](CVE-2026-138004) | TEW-751DR / TEW-733GR | 4.0 9.3 (VulDB); 3.1 10.0 (VulDB) | TEW-751DR / TEW-733GR 1.03B01 |  |

### Runtime / Framework / Browser (111)

| ID | Product | Score | Affected | Fixed |
| --- | --- | --- | --- | --- |
| [CVE-2026-57898](CVE-2026-57898) | Eclipse BaSyx Java Server SDK | 3.1 9.0 (Eclipse) | Eclipse BaSyx Java Server SDK 2.0.0-milestone-05–2.0.0-milestone-12 (MongoDB backend) | 2.0.0-milestone-13 |
| [CVE-2026-114938](CVE-2026-114938) | OpenJDK Base64 (Java4Shell) | 4.0 9.2 (Calif); 3.1 8.1 (Oracle); 3.1 9.8 (Red Hat) | OpenJDK 17.0.6 and later on x86-64 with AVX-512 VBMI (17/21/25/27 lines; Oracle also lists Java 8 Performance Pack 8u511b33-perf) | vendor November 2026 CPU / OpenJDK 17.0.21.1, 21.0.13.1 and equivalent distributor builds |
| [CVE-2026-90436](CVE-2026-90436) | Apache Axis 1.x | 3.1 9.8 (CISA-ADP) | Apache Axis 1.x through 1.4 | 無修復版本（EOL；修復僅存於上游 commit 41f3b4e8） |
| [CVE-2024-27834](CVE-2024-27834) | WebKit (Apple) | 3.1 5.5 (NVD) | Safari < 17.5；iOS/iPadOS < 16.7.8 及 17.x < 17.5；macOS < 14.5；tvOS < 17.5；watchOS < 10.5；WebKitGTK / WPE WebKit < 2.44.2 | Safari 17.5；iOS 16.7.8 / iOS 17.5；iPadOS 16.7.8 / iPadOS 17.5；macOS Sonoma 14.5；tvOS 17.5；watchOS 10.5 |
| [CVE-2026-126187](CVE-2026-126187) | React Server Components / Next.js | 4.0 9.5 (GHSA) | react-server-dom-* 19.0.0–19.3.0; Next.js 16.0.0–16.4.0 (App Router + Cache Components) | react-server-dom-* 19.0.9 / 19.1.10 / 19.2.9 / 19.3.1; Next.js 16.4.1 |
| [CVE-2026-125350](CVE-2026-125350) | Google Chrome | 3.1 8.8 (NVD) | Chrome < 157.0.8103.50 | 157.0.8103.50 / .51 (Windows, macOS), 157.0.8103.50 (Linux, Android), Extended Stable 156.0.8078.96 |
| [CVE-2026-111497](CVE-2026-111497) | Node.js Brotli | 4.0 9.2 (Google); 3.1 9.8 (NVD) | Node.js < 22.23.4, < 24.22.1, < 26.12.1; Bun < 1.4.4; Brotli 1.0.3-1.2.0 | Node.js 22.23.4 / 24.22.1 / 26.12.1; Bun 1.4.4; Brotli 1.2.1 |
| [CVE-2026-129349](CVE-2026-129349) | Apache Shiro DefaultLdapRealm | 4.0 9.1 (Apache) | Apache Shiro through 3.0.0 with DefaultLdapRealm/JndiLdapRealm and authenticationCachingEnabled=true (not the default) | 3.0.1 |
| [CVE-2026-86829](CVE-2026-86829) | Apache Airflow core | 3.1 8.8 (Apache) | apache-airflow-core < 3.4.0 | 3.4.0 (apache/airflow PR #72718) |
| [CVE-2026-115560](CVE-2026-115560) | PHP session upload progress | 4.0 9.2 (PHP) | PHP with session.serialize_handler=php_binary or php_serialize in server config, application switching to php at runtime via ini_set() before session_start(), and session.upload_progress.enabled=1 (PHP default). Validated on php:8.4.27-apache. | 8.5.13 / 8.4.28 / 8.3.37 / 8.2.36 (2026-11-19) |
| [CVE-2026-75604](CVE-2026-75604) | Next.js on Windows | 3.1 9.0 (GHSA) | Next.js 13.4.0–15.5.23 and 16.0.0–16.3.2 on Windows, Pages Router + App Router without Cache Components | 15.5.24 / 16.3.3 |
| [CVE-2026-115893](CVE-2026-115893) | Wasmtime | 3.1 9.9 (GHSA) | Wasmtime < 36.0.19, 37.0.0-42.x, 43.0.0-48.0.6, 49.0.0-49.0.3 (aarch64 Cranelift) | 36.0.19, 48.0.7, 49.0.4 |
| [CVE-2026-109618](CVE-2026-109618) | PHP | 3.1 9.8 (NVD); 4.0 9.2 (PHP) | PHP 5.4.0-8.5.11 | 8.2.35, 8.3.36, 8.4.27, 8.5.12 |
| [CVE-2026-109619](CVE-2026-109619) | PHP | 3.1 8.1 (NVD); 4.0 9.2 (PHP) | PHP 5.4.0-8.5.11 | 8.2.35, 8.3.36, 8.4.27, 8.5.12 |
| [CVE-2026-126910](CVE-2026-126910) | Chrome V8 Maglev | 3.1 8.8 (NVD) | Chrome before 157.0.8103.78 | 157.0.8103.78 |
| [CVE-2026-128134](CVE-2026-128134) | NLTK dot2img | 3.1 7.8 (GHSA) | NLTK before 3.10.4 | 3.10.4 |
| [CVE-2026-130001](CVE-2026-130001) | mustache (Ruby) | 3.1 9.8 (GHSA) | mustache gem <= 1.1.2 | 1.1.3 |
| [CVE-2026-47884](CVE-2026-47884) | Spring Framework XsltView | 3.1 9.8 (GHSA) | Spring Framework 5.2.x–5.3.49, 6.0.x–6.0.30, 6.1.x–6.1.28, 6.2.x–6.2.19, 7.0.0–7.0.8 (XsltView + catch-all /** mapping + implicit view name) | 5.3.50 / 6.0.31 / 6.1.29 / 6.2.20 / 7.0.9 |
| [CVE-2026-131842](CVE-2026-131842) | Poppler pdfdetach | 4.0 5.7 (VulnCheck) | Poppler pdfdetach 24.03.0–26.11.0 | none (upstream work item 1826 open) |
| [CVE-2026-131873](CVE-2026-131873) | Gargoyle | 4.0 6.9 (VulnCheck) | Gargoyle 2023.1–2026.1.1 | Spatterlight 1.5.5 import (commit 45385f1) |
| [CVE-2026-121265](CVE-2026-121265) | SQL::Abstract | 3.1 9.8 (GHSA) | SQL::Abstract < 2.000003 | 2.000003 |
| [CVE-2026-107360](CVE-2026-107360) | rubygem-safemode | 3.1 9.6 (Red Hat) | rubygem-safemode through 2.0.3; Red Hat Satellite 6.16–6.18 | upstream PR #75 (unmerged); rubygem-safemode 1.5.0-3.el8sat / 1.5.0-3.el9sat |
| [CVE-2026-128027](CVE-2026-128027) | FrankenPHP | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | FrankenPHP images built before 2026-02-04 (< 1.1.11) | 1.1.11 |
| [CVE-2026-128014](CVE-2026-128014) | FrankenPHP | 4.0 9.2 (VulnCheck); 3.1 8.1 (GHSA) | FrankenPHP 1.13.1 (Brotli 1.2.0); all builds shipping Brotli < 1.2.1 | 1.13.2 (Brotli 1.2.1) |
| [CVE-2026-123753](CVE-2026-123753) | Apache Axis2/Java | 3.1 9.1 (GHSA) | Apache Axis2/Java < 2.0.2 (PoC tested 2.0.1) | 2.0.2 |
| [CVE-2026-132825](CVE-2026-132825) | Ruby | 3.1 7.4 (MITRE) | Ruby < 3.3.14; 3.4.0-< 3.4.13; 4.0.0-< 4.0.10 | 3.3.14 / 3.4.13 / 4.0.10 |
| [CVE-2026-133168](CVE-2026-133168) | DCMTK | 4.0 8.5 (VulnCheck); 3.1 7.8 (VulnCheck) | DCMTK 3.7.1 | 3.7.2 (patch pending; fix commit c22836c, no release tagged) |
| [CVE-2026-133243](CVE-2026-133243) | node-soap | 4.0 8.8 (VulnCheck); 3.1 8.2 (VulnCheck) | node-soap before 1.14.1 | 1.14.1 |
| [CVE-2026-71164](CVE-2026-71164) | Helidon | 3.1 9.8 (Oracle) | Helidon 3.0.0-3.2.17 (Imperative Web Server) | 3.2.18 (Oracle CSPU Aug 2026) |
| [CVE-2026-133307](CVE-2026-133307) | ClassiCube | 4.0 8.7 (VulnCheck); 3.1 8.8 (VulnCheck) | ClassiCube before 1.4.0 | 1.4.0 |
| [CVE-2026-116499](CVE-2026-116499) | Qiskit SDK | 3.1 8.4 (IBM) | Qiskit SDK v1.4.2-v2.6.2 | 2.6.2 (IBM patched release) |
| [CVE-2026-133254](CVE-2026-133254) | IntelliJ IDEA | 3.1 8.3 (JetBrains) | IntelliJ IDEA before 2026.3, 2026.2.4 | 2026.3 / 2026.2.4 |
| [CVE-2026-130886](CVE-2026-130886) | @fastify/reply-from | 3.1 8.2 (GHSA) | @fastify/reply-from 12.8.1-12.8.3 | 12.8.4 |
| [CVE-2026-92937](CVE-2026-92937) | vm2 | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | vm2 3.11.6 | 3.11.7 |
| [CVE-2026-0881](CVE-2026-0881) | Firefox | 3.1 10.0 (Mozilla) | Firefox <147, Thunderbird <147 | Firefox 147 / Thunderbird 147 (MFSA2026-01) |
| [CVE-2026-92940](CVE-2026-92940) | vm2 | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | vm2 3.11.3-3.11.6 | 3.11.7 |
| [CVE-2026-92941](CVE-2026-92941) | vm2 | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | vm2 3.11.3-<3.11.7 | 3.11.7 |
| [CVE-2026-92946](CVE-2026-92946) | vm2 | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | vm2 before 3.11.7 | 3.11.7 |
| [CVE-2026-92947](CVE-2026-92947) | vm2 | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | vm2 before 3.11.7 | 3.11.7 |
| [CVE-2026-92955](CVE-2026-92955) | vm2 | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | vm2 before 3.11.8 | 3.11.8 |
| [CVE-2026-92956](CVE-2026-92956) | vm2 | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | vm2 3.10.1-3.11.6 | 3.11.7 |
| [CVE-2026-92960](CVE-2026-92960) | vm2 | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | vm2 before 3.11.6 | 3.11.6 |
| [CVE-2026-92953](CVE-2026-92953) | vm2 | 3.1 10.0 (VulnCheck); 4.0 9.3 (VulnCheck) | vm2 3.11.0-3.11.7 | 3.11.8 |
| [CVE-2026-92948](CVE-2026-92948) | vm2 | 3.1 9.9 (VulnCheck); 4.0 9.4 (VulnCheck) | vm2 3.9.6-3.11.6 | 3.11.7 |
| [CVE-2026-92951](CVE-2026-92951) | vm2 | 3.1 9.9 (VulnCheck); 4.0 9.4 (VulnCheck) | vm2 before 3.11.7 | 3.11.7 |
| [CVE-2026-92957](CVE-2026-92957) | vm2 | 3.1 9.9 (VulnCheck); 4.0 9.4 (VulnCheck) | vm2 through 3.11.6 | 3.11.7 |
| [CVE-2026-92944](CVE-2026-92944) | vm2 | 3.1 9.8 (VulnCheck); 4.0 9.3 (VulnCheck) | vm2 3.10.2-3.11.6 | 3.11.7 |
| [CVE-2026-128138](CVE-2026-128138) | NLTK | 3.1 9.8 (GitHub) | NLTK 3.10.3-<3.10.4 | 3.10.4 |
| [CVE-2026-92950](CVE-2026-92950) | vm2 | 3.1 8.6 (VulnCheck); 4.0 9.3 (VulnCheck) | vm2 before 3.11.7 | 3.11.7 |
| [CVE-2026-92954](CVE-2026-92954) | vm2 | 3.1 8.6 (VulnCheck); 4.0 9.2 (VulnCheck) | vm2 3.10.0-3.11.7 | 3.11.8 |
| [CVE-2026-92958](CVE-2026-92958) | vm2 | 3.1 8.5 (VulnCheck); 4.0 8.4 (VulnCheck) | vm2 through 3.11.6 | 3.11.7 |
| [CVE-2026-92943](CVE-2026-92943) | AWS IoT Device SDK for Python | 3.1 8.1 (AMZN); 4.0 9.2 (AMZN) | AWS IoT Device SDK for Python 1.5.3-1.6.0 | 1.6.1 |
| [CVE-2026-130235](CVE-2026-130235) | Okta .NET SDK Abstractions | 3.1 8.7 (Okta) | Okta .NET SDK Abstractions 1.0.0-beta-4.0.7 | 4.0.8 |
| [CVE-2026-130179](CVE-2026-130179) | Okta .NET SDK Abstractions | 3.1 8.5 (Okta) | Okta .NET SDK Abstractions 3.0.0-4.0.7 | 4.0.8 |
| [CVE-2026-61798](CVE-2026-61798) | netty-incubator-codec-ohttp | 3.1 8.1 (GitHub) | netty-incubator-codec-ohttp <0.0.23.Final | 0.0.23.Final |
| [CVE-2026-130234](CVE-2026-130234) | Okta Swift Management SDK | 3.1 8.0 (Okta) | Okta Swift Management SDK <0.1.1 | 0.1.1 |
| [CVE-2026-130756](CVE-2026-130756) | pnpm exe | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | pnpm exe <10.34.8, 11.x <11.28.8 | 10.34.8 / 11.28.8 |
| [CVE-2019-25782](CVE-2019-25782) | ThinkPHP | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | ThinkPHP 5.0.0-5.0.23 | 5.0.24 |
| [CVE-2012-20007](CVE-2012-20007) | ThinkPHP | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | ThinkPHP 2.0-2.2 / 3.0 Lite | No known patch |
| [CVE-2026-83020](CVE-2026-83020) | Oracle Platform Security for Java | 3.1 10 (Oracle) | Oracle Platform Security for Java 12.2.1.4.0 / 14.1.2.0.0 | September 2026 Critical Security Patch Update |
| [CVE-2026-82994](CVE-2026-82994) | Oracle Platform Security for Java | 3.1 9.8 (Oracle) | Oracle Platform Security for Java 12.2.1.4.0 / 14.1.2.0.0 | September 2026 Critical Security Patch Update |
| [CVE-2026-82995](CVE-2026-82995) | Oracle Platform Security for Java | 3.1 9.8 (Oracle) | Oracle Platform Security for Java 12.2.1.4.0 / 14.1.2.0.0 | September 2026 Critical Security Patch Update |
| [CVE-2026-91570](CVE-2026-91570) | Oracle WebLogic Server | 3.1 9.8 (Oracle) | Oracle WebLogic Server 12.2.1.4.0 / 14.1.1.0.0 / 14.1.2.0.0 / 15.1.1.0.0 | November 2026 Critical Patch Update |
| [CVE-2026-91583](CVE-2026-91583) | Oracle WebLogic Server | 3.1 9.8 (Oracle) | Oracle WebLogic Server 12.2.1.4.0 / 14.1.1.0.0 / 14.1.2.0.0 / 15.1.1.0.0 | November 2026 Critical Patch Update |
| [CVE-2026-91585](CVE-2026-91585) | Oracle WebLogic Server | 3.1 9.8 (Oracle) | Oracle WebLogic Server 12.2.1.4.0 / 14.1.1.0.0 / 14.1.2.0.0 / 15.1.1.0.0 | November 2026 Critical Patch Update |
| [CVE-2026-103119](CVE-2026-103119) | Apache Tomcat | 3.1 9.1 (NVD) | Apache Tomcat 11.0.0-M25 to 11.0.26 | 11.0.27 |
| [CVE-2026-133528](CVE-2026-133528) | BeamNG.drive | 4.0 9.3 (VulnCheck); 3.1 8.6 (VulnCheck) | BeamNG.drive <0.40.6 | 0.40.6 |
| [CVE-2026-127064](CVE-2026-127064) | @fastify/reply-from | 3.1 8.2 (OpenJSF) | @fastify/reply-from <12.8.4 | 12.8.4 |
| [CVE-2026-117659](CVE-2026-117659) | InfoScan | 4.0 8.5 (CISA); 3.1 8.1 (CISA) | Dorsett Controls InfoScan <=1.45.0 | 1.46 |
| [CVE-2026-129496](CVE-2026-129496) | PHP | 4.0 9.2 (PHP Group) | PHP 8.2 <8.2.36 / 8.3 <8.3.37 / 8.4 <8.4.28 / 8.5 <8.5.13 | 8.2.36 / 8.3.37 / 8.4.28 / 8.5.13 |
| [CVE-2026-129474](CVE-2026-129474) | PHP | 4.0 9.2 (PHP Group) | PHP 8.5.0–<8.5.13 | 8.5.13 |
| [CVE-2026-126714](CVE-2026-126714) | PHP | 4.0 9.2 (PHP Group) | PHP 8.2 <8.2.36 / 8.3 <8.3.37 / 8.4 <8.4.28 / 8.5 <8.5.13 | 8.2.36 / 8.3.37 / 8.4.28 / 8.5.13 |
| [CVE-2026-129289](CVE-2026-129289) | PHP | 4.0 9.2 (PHP Group) | PHP 8.2 <=8.2.35 / 8.3 <=8.3.36 / 8.4 <=8.4.27 / 8.5 <=8.5.12 | 8.2.36 / 8.3.37 / 8.4.28 / 8.5.13 |
| [CVE-2026-133212](CVE-2026-133212) | @fastify/reply-from | 3.1 9.0 (OpenJSF) | @fastify/reply-from before 12.9.1 | 12.9.1 |
| [CVE-2026-77355](CVE-2026-77355) | isomorphic-git | 3.1 8.8 (GHSA) | isomorphic-git before 1.38.7 (Windows NTFS) | 1.38.7 |
| [CVE-2026-86017](CVE-2026-86017) | isomorphic-git | 3.1 8.0 (GHSA) | isomorphic-git before 1.38.8 (cherry-pick symlink) | 1.38.8 |
| [CVE-2026-104711](CVE-2026-104711) | Apache Struts | 3.1 9.8 (NVD); 3.1 8.1 (Apache) | 2.0.0-2.3.37, 2.5.0-2.5.33, 6.0.0-6.11.0, 7.0.0-7.3.0 | 6.12.0 (6.x), 7.4.0 (7.x) |
| [CVE-2026-133325](CVE-2026-133325) | Apache Tomcat | 3.1 9.8 (NVD) | 11.0.28-11.0.29, 10.1.62, 9.0.124 |  |
| [CVE-2026-95517](CVE-2026-95517) | Apache Tomcat | 3.1 9.1 (NVD) | 11.0.0-M1-11.0.27, 10.1.0-M1-10.1.61, 9.0.13-9.0.123 | 11.0.29, 10.1.62, 9.0.124 |
| [CVE-2026-124626](CVE-2026-124626) | @fastify/express | 3.1 9.1 (NVD) | 4.0.5-4.0.9 | 4.0.10 |
| [CVE-2026-129504](CVE-2026-129504) | @fastify/express | 3.1 9.1 (NVD) | 4.0.0-4.0.9 | 4.0.10 |
| [CVE-2026-133120](CVE-2026-133120) | @fastify/express | 3.1 9.1 (NVD) | < 4.0.10 | 4.0.10 |
| [CVE-2026-133250](CVE-2026-133250) | @fastify/middie | 3.1 9.1 (NVD) | <= 9.3.7 | 9.3.8 |
| [CVE-2026-133867](CVE-2026-133867) | @fastify/express | 3.1 9.1 (NVD) | 4.0.7-4.0.9 | 4.0.10 |
| [CVE-2026-134814](CVE-2026-134814) | binary-parser | 4.0 9.2 (VulnCheck); 3.1 8.1 (GHSA) | binary-parser before 2.3.1 | 2.3.1 |
| [CVE-2026-134815](CVE-2026-134815) | simple-git | 4.0 9.2 (VulnCheck); 3.1 8.1 (VulnCheck) | simple-git before 4.1.0 | 4.1.0 |
| [CVE-2026-125396](CVE-2026-125396) | Ghostscript | 4.0 8.5 (VulnCheck); 3.1 7.8 (VulnCheck) | Ghostscript before 10.08.0 | 10.08.0 |
| [CVE-2026-129975](CVE-2026-129975) | gpgme | 3.1 8.1 (Red Hat) | gpgme |  |
| [CVE-2026-119348](CVE-2026-119348) | Next.js | 4.0 6.3 (GitHub) | Next.js <= 15.5.28 and 16.0.0-16.4.4 (self-hosted) | 15.5.29 / 16.4.5 |
| [CVE-2026-135736](CVE-2026-135736) | FFmpeg | 4.0 9.2 (VulnCheck); 3.1 8.1 (VulnCheck) | FFmpeg 4.4 before 9.1 | 9.1 |
| [CVE-2026-135743](CVE-2026-135743) | FFmpeg | 4.0 9.2 (VulnCheck); 3.1 8.1 (VulnCheck) | FFmpeg 4.3 before 9.1 | 9.1 |
| [CVE-2026-123886](CVE-2026-123886) | Spring Data Elasticsearch | 3.1 8.8 (VMware) | Spring Data Elasticsearch versions before 2a5b65c | 2a5b65c |
| [CVE-2026-42290](CVE-2026-42290) | protobufjs-cli | 3.1 7.8 (GitHub) | protobufjs-cli < 1.2.1 and < 2.0.2 | 1.2.1、2.0.2 |
| [CVE-2026-46595](CVE-2026-46595) | golang.org/x/crypto/ssh | 3.1 10.0 (CISA-ADP) | golang.org/x/crypto < v0.52.0 | v0.52.0 |
| [CVE-2026-134824](CVE-2026-134824) | nektos/act | 4.0 6.8 (VulnCheck) | nektos/act 0.2.92–0.2.97 | 0.2.98 |
| [CVE-2026-105803](CVE-2026-105803) | Git LFS | 4.0 8.6 (GHSA) | Git LFS >= 1.3.0, <= 2.13.3 and >= 3.0.0, < 3.8.1 | 3.8.1 |
| [CVE-2026-134401](CVE-2026-134401) | Google Chrome | 3.1 9.6 (CISA-ADP) | Google Chrome < 158.0.8127.88 | 158.0.8127.88 (Windows/Mac/Linux); Extended Stable 156.0.8078.114 |
| [CVE-2026-65320](CVE-2026-65320) | fastcore | 4.0 9.2 (VulnCheck); 3.1 8.1 (VulnCheck) | fastcore through 2.2.44 | unknown |
| [CVE-2026-136412](CVE-2026-136412) | stream-lua-nginx-module | 4.0 9.2 (VulnCheck); 3.1 8.1 (GHSA) | stream-lua-nginx-module < 0.0.20rc4 | 0.0.20rc4 |
| [CVE-2026-33186](CVE-2026-33186) | gRPC-Go | 3.1 9.1 (GHSA) | gRPC-Go before 1.79.3 | 1.79.3 |
| [CVE-2026-34486](CVE-2026-34486) | Apache Tomcat | 3.1 7.5 (Apache) | 11.0.0-M1 to 11.0.20; 10.1.0-M1 to 10.1.53; 9.0.13 to 9.0.116 | 11.0.21; 10.1.54; 9.0.117 |
| [CVE-2026-66066](CVE-2026-66066) | Ruby on Rails | 4.0 9.5 (GHSA) | Active Storage < 7.2.3.2; >= 8.0.0.beta1, < 8.0.5.1; >= 8.1.0.beta1, < 8.1.3.1 | 7.2.3.2; 8.0.5.1; 8.1.3.1 |
| [CVE-2026-77423](CVE-2026-77423) | JLine3 | 3.1 7.5 (GHSA) | org.jline:jline-builtins >= 3.0.0, < 3.30.15; < 4.3.1 | 3.30.15 / 4.3.1 |
| [CVE-2026-118264](CVE-2026-118264) | labstack Echo | 4.0 9.1 (GHSA) | Echo v4 >= 4.0.0, < 4.16.1；Echo v5 >= 5.0.0, < 5.4.1 | v4.16.1 / v5.4.1 |
| [CVE-2026-47892](CVE-2026-47892) | Spring Framework（WebFlux） | 3.1 9.8 (GHSA) | Spring Framework 5.2.5.RELEASE–5.2.25.RELEASE、5.3.0–5.3.49、6.0.0–6.0.30、6.1.0–6.1.28、6.2.0–6.2.19、7.0.0–7.0.8 | 7.0.9（OSS）；5.2.26.RELEASE / 5.3.50 / 6.0.31 / 6.1.29 / 6.2.20（企業支援） |
| [CVE-2026-63471](CVE-2026-63471) | fastapi-code-generator | 4.0 9.3 (GHSA) | fastapi-code-generator < 0.8.1 | 0.8.1 |
| [CVE-2026-84939](CVE-2026-84939) | Apache FreeMarker | 3.1 9.1 (GHSA) | Apache FreeMarker 2.2.0–2.3.34 | 2.3.35 |
| [CVE-2026-137550](CVE-2026-137550) | Frappe Framework | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | Frappe Framework < 15.122.0；16.x < 16.50.0 | 15.122.0 / 16.50.0 |
| [CVE-2026-22683](CVE-2026-22683) | Windmill | 3.1 8.8 (GHSA); 4.0 8.7 (VulnCheck) | Windmill 1.56.0 起，1.614.0 之前 | 1.615.0 |
| [CVE-2026-23696](CVE-2026-23696) | Windmill | 3.1 9.9 (GHSA); 4.0 9.4 (VulnCheck) | Windmill CE 與 EE 1.276.0 起，1.603.2 之前 | 1.603.3 |
| [CVE-2026-29059](CVE-2026-29059) | Windmill | 3.1 7.5 (NVD); 4.0 6.9 (GHSA) | Windmill < 1.603.3 | 1.603.3 |

### Database (22)

| ID | Product | Score | Affected | Fixed |
| --- | --- | --- | --- | --- |
| [CVE-2026-118383](CVE-2026-118383) | MongoDB Server replication | 4.0 9.5 (MongoDB); 3.1 9.0 (MongoDB); 3.1 10.0 (NVD) | 8.0.x before 8.0.37 (8.0.34 tested); 8.2.12 still reproduced at collection time | 8.0.37 (SERVER-138175, SERVER-138119) |
| [CVE-2026-116366](CVE-2026-116366) | ClickHouse Server | 4.0 9.5 (ClickHouse) | ClickHouse 26.3 < 26.3.62.3-lts, 26.8 < 26.8.36.3-lts, 26.9 < 26.9.27.3-stable, 26.10 < 26.10.3.7-stable | 26.3.62.3-lts / 26.8.36.3-lts / 26.9.27.3-stable / 26.10.3.7-stable (2026-10-30) |
| [CVE-2026-13078](CVE-2026-13078) | MongoDB Server | 3.1 7.7 (MongoDB); 4.0 6.3 (MongoDB) | MongoDB Server 7.0 before 7.0.39, 8.0 before 8.0.28, 8.2 before 8.2.12, 8.3 before 8.3.7 | 7.0.39, 8.0.28, 8.2.12, 8.3.7 |
| [CVE-2026-73504](CVE-2026-73504) | cassandra-jdbc-wrapper | 3.1 5.5 (GHSA) | cassandra-jdbc-wrapper < 4.16.4; >= 5.0.0, < 5.0.2 | 4.16.4 / 5.0.2 |
| [CVE-2026-116244](CVE-2026-116244) | pgAdmin 4 | 3.1 9.6 (NVD); 4.0 7.1 (PostgreSQL) | pgAdmin 4 ≤ 9.18 | 9.19 (2026-10-29) |
| [CVE-2026-126837](CVE-2026-126837) | MongoDB Node.js driver | 4.0 9.1 (MongoDB); 3.1 7.4 (MongoDB) | MongoDB Node.js driver 3.3.3 to < 7.8.0 | 7.8.0 |
| [CVE-2026-119179](CVE-2026-119179) | MongoDB Node.js driver | 4.0 8.3 (MongoDB); 3.1 7.0 (MongoDB) | mongodb >= 6.11.0 < 6.22.0 and >= 7.0.0 < 7.8.0 | 6.22.0 / 7.8.0 |
| [CVE-2026-115290](CVE-2026-115290) | Elasticsearch | 3.1 7.5 (GHSA) | Elasticsearch 8.10.0–8.19.23, 9.0.0–9.4.8, 9.5.0–9.5.5 (remote_cluster_server enabled) | 8.19.24 / 9.4.9 / 9.5.6 |
| [CVE-2026-126755](CVE-2026-126755) | ArangoDB | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | ArangoDB <3.12.11 | 3.12.11 |
| [CVE-2026-116331](CVE-2026-116331) | PostgreSQL | 3.1 8.8 (PostgreSQL) | PostgreSQL < 18.7, 17.12, 16.16, 15.20, 14.25 | 18.7 / 17.12 / 16.16 / 15.20 / 14.25 |
| [CVE-2026-6460](CVE-2026-6460) | PostgreSQL | 3.1 8.8 (PostgreSQL) | PostgreSQL < 18.7, 17.12, 16.16, 15.20, 14.25 | 18.7 / 17.12 / 16.16 / 15.20 / 14.25 |
| [CVE-2026-134292](CVE-2026-134292) | SurrealDB | 4.0 9.3 (NVD); 3.1 9.8 (NVD) | < 4.0.0 | 4.0.0 |
| [CVE-2026-134337](CVE-2026-134337) | ArcadeDB | 4.0 8.7 (VulnCheck); 3.1 8.8 (VulnCheck) | ArcadeDB native-image server builds 26.8.1 before 26.11.1 | 26.11.1 |
| [CVE-2026-134293](CVE-2026-134293) | SurrealDB | 4.0 8.8 (VulnCheck); 3.1 8.2 (VulnCheck) | SurrealDB 3.1.0 before 4.0.0 | 4.0.0 |
| [CVE-2026-134295](CVE-2026-134295) | SurrealDB | 4.0 8.7 (VulnCheck); 3.1 8.8 (VulnCheck) | SurrealDB 3.0.0 before 4.0.0 | 4.0.0 |
| [CVE-2026-134300](CVE-2026-134300) | SurrealDB | 4.0 7.2 (VulnCheck); 3.1 8.1 (VulnCheck) | SurrealDB 2.2.0 before 4.0.0 | 4.0.0 |
| [CVE-2026-134309](CVE-2026-134309) | SurrealDB | 4.0 8.7 (VulnCheck); 3.1 8.8 (VulnCheck) | SurrealDB 1.0.0 before 4.0.0 | 4.0.0 |
| [CVE-2026-134803](CVE-2026-134803) | DBHub | 3.1 8.1 (VulnCheck); 4.0 7.2 (VulnCheck) | DBHub before 1.7.0 | 1.7.0 |
| [CVE-2026-134841](CVE-2026-134841) | pgjdbc (PostgreSQL JDBC Driver) | 3.1 8.1 (pgjdbc) | pgjdbc < 42.7.15 | 42.7.15 |
| [CVE-2026-134842](CVE-2026-134842) | pgjdbc (PostgreSQL JDBC Driver) | 3.1 8.1 (pgjdbc) | pgjdbc < 42.7.15 (preferQueryMode=simple and standard_conforming_strings=off) | 42.7.15 |
| [CVE-2026-132660](CVE-2026-132660) | Postgres Enterprise Manager (PEM) | 4.0 9.4 (EDB) | PEM 7.6.0–10.6.1 (before 10.6.1) | 10.6.1 |
| [CVE-2026-25243](CVE-2026-25243) | Redis | 4.0 7.7 (GHSA); 3.1 8.8 (NVD) | All Redis OSS/CE releases (Redis Software up to and including 8.0.6) | 6.2.22, 7.2.14, 7.4.9, 8.2.6, 8.4.3, 8.6.3 |

### OS / System / DevOps (76)

| ID | Product | Score | Affected | Fixed |
| --- | --- | --- | --- | --- |
| [CVE-2026-65094](CVE-2026-65094) | NVIDIA VIRTIO-Net for BlueField | 3.1 9.0 (NVIDIA) | NVIDIA VIRTIO-Net GA <25.10.6; LTS25 <25.10.2; LTS24 <24.10.50; LTS23 1.7.21 and older (BlueField-3) | 25.10.6 (GA) / 25.10.2 (LTS25) / 24.10.50 (LTS24) / 23.10.23 (LTS23) |
| [CVE-2026-74127](CVE-2026-74127) | AMD Platform Security Processor (PSP) boot ROM | 4.0 9.4 (AMD) | AMD Zen 1 / Zen+ processors (PSP boot ROM) | No fix planned (AMD: boot ROM immutable) |
| [CVE-2024-10441](CVE-2024-10441) | Synology DSM/BSM synoplugind | 3.1 9.8 (upstream PoC README (unverified against vendor advisory in this ingest)) | DSM 6.2.4–7.2.2 and BSM/DSMUC branches before the 2024-11 smallfix | DSM 7.2.2-72806-1 / 7.2.1-69057-6 / 7.2-64570-4 / 7.1.1-42962-7 / 6.2.4-25556-8; BeeStation OS 1.1-65374; DSMUC 3.1.4-23079 |
| [CVE-2026-124194](CVE-2026-124194) | Microsoft Outlook | 3.1 6.5 (Microsoft) | Microsoft 365 Apps 版經典 Outlook、Office LTSC 2021/2024（2026-11-10 前構建） | 2026 年 11 月 10 日 Patch Tuesday Office 更新 |
| [CVE-2026-115731](CVE-2026-115731) | Puppet / OpenVox Server | 4.0 9.4 (Perforce); 3.1 9.9 (NVD) | Puppet Enterprise 2023.8.0–<2023.8.13、2025.0.0–<2025.12.1、2026.0.0–<2026.0.1；OpenVox Server ≤ 9.1.0 / ≤ 8.17.0；OpenVox Agent ≤ 9.2.0 / ≤ 8.31.1 | Puppet Enterprise 2023.8.13 / 2025.12.1 / 2026.0.1；OpenVox Server 9.2.0 / 8.18.0；OpenVox Agent 9.3.0 / 8.32.0；Puppet Core 9.1.3 / 8.22.2 |
| [CVE-2026-98432](CVE-2026-98432) | Linux kernel TCP | 3.1 9.8 (Linux kernel) | Linux kernel since 4.4 (IPv4 TCP) | 6.6.159 and later stable releases (two kfree_rcu() calls) |
| [CVE-2026-76954](CVE-2026-76954) | Synology DSM Auth API | 3.1 9.8 (Synology) | DSM <= 7.2.1-69057-12, 7.2.2-72806, 7.3.2-86009, 7.4.1-90080 | 7.2.1-69057-13, 7.2.2-72806-10, 7.3.2-86009-5, 7.4.1-90080-1 (Synology-SA-26:19) |
| [CVE-2026-124552](CVE-2026-124552) | Webmin Shorewall modules | 4.0 4.8 (VulnCheck); 3.1 4.8 (VulnCheck) | Webmin through 2.670 | Post-2.670 (upstream commit 01b988dbf, webmin/webmin#2908) |
| [CVE-2026-104623](CVE-2026-104623) | SUSE Rancher Manager | 3.1 6.3 (SUSE) | Rancher Manager 2.11.0-2.11.18, 2.12.0-2.12.14, 2.13.0-2.13.10, 2.14.0-2.14.6, 2.15.0-2.15.2 (and older) | 2.11.19 / 2.12.15 / 2.13.11 / 2.14.7 / 2.15.3 |
| [CVE-2026-105437](CVE-2026-105437) | Git three-way merge | 3.1 7.5 (GitLab) | Git <= 2.56.0 (and the 2.50-2.55 series) | Git 2.56.1, and 2.50.2 / 2.51.3 / 2.52.1 / 2.53.1 / 2.54.1 / 2.55.1 |
| [CVE-2026-53362](CVE-2026-53362) | Linux kernel IPv6 fragmentation | 3.1 7.8 (Linux kernel) | Linux kernel 6.12.x (CentOS Stream 10 / RHEL 10, e.g. 6.12.0-242.el10); __ip6_append_data() paged-allocation path | upstream commit 38becddc (fix in stable trees) |
| [CVE-2026-97229](CVE-2026-97229) | GitLab CE/EE | 3.1 10.0 (GitLab) | GitLab CE/EE 19.2 before 19.2.8, 19.3 before 19.3.5, 19.4 before 19.4.2 | 19.2.8, 19.3.5, 19.4.2 |
| [CVE-2026-110264](CVE-2026-110264) | GitLab CE/EE | 3.1 10.0 (GitLab) | GitLab CE/EE 7.0 before 18.11.13, 19.0 before 19.0.10, 19.1 before 19.1.9, 19.2 before 19.2.9, 19.3 before 19.3.6, 19.4 before 19.4.3 | 18.11.13, 19.0.10, 19.1.9, 19.2.9, 19.3.6, 19.4.3, 19.5.1 |
| [CVE-2026-112611](CVE-2026-112611) | Apple CoreGraphics PDF | 3.1 6.1 (NVD) | iOS before 27.2 / 26.7.2, iPadOS before 27.2 / 26.7.2, macOS before 15.8.2 / 26.7.2 | iOS 27.2 / 26.7.2, macOS Sequoia 15.8.2 / Tahoe 26.7.2 |
| [CVE-2026-99288](CVE-2026-99288) | Linux kernel TCP | 3.1 5.9 (NVD) | Linux kernel with vulnerable TCP ehash lookup (before upstream commit 4e2b3ef19e0e) | Upstream commit 4e2b3ef19e0e (inet: reject unhashed sockets during established lookups) |
| [CVE-2026-129987](CVE-2026-129987) | Dokploy | 3.1 9.9 (GHSA) | Dokploy < 0.31.1 (v0.29.0-v0.31.0 per upstream version archaeology) | 0.31.1 |
| [CVE-2026-43499](CVE-2026-43499) | Linux kernel rtmutex | 3.1 7.8 (Linux kernel) | Linux kernel rtmutex path (PoC targets 4.14.186+ on realme RMX3031/MT6893) |  |
| [CVE-2026-112477](CVE-2026-112477) | Apple iOS IOSurface | 3.1 7.0 (NVD) | iOS 26.x (tested on iOS 26.4, arm64e) | iOS 26.7.2 / iPadOS 26.7.2 |
| [CVE-2026-130587](CVE-2026-130587) | OpenFunction | 3.1 9.9 (GHSA) | OpenFunction through 1.2.0 | no vendor fix (upstream issue #532 OPEN) |
| [CVE-2026-126978](CVE-2026-126978) | Philips Hue Bridge | 3.0 8.8 (GHSA) | Philips Hue Bridge gen 2 and gen 3 (all firmware prior to patch) | no fixed version published |
| [CVE-2026-126979](CVE-2026-126979) | Philips Hue Bridge | 3.0 8.8 (GHSA) | Philips Hue Bridge gen 2 and gen 3 (all firmware prior to patch) | no fixed version published |
| [CVE-2026-130335](CVE-2026-130335) | Info-ZIP Zip | 3.1 2.9 (MITRE) | Info-ZIP Zip 3.0, 3.1 beta–3.1c | Debian zip/3.0-16 (quote_arg fix) |
| [CVE-2026-121529](CVE-2026-121529) | FortiClient | 3.1 9.6 (GHSA); 3.1 9.1 (Fortinet) | FortiClient Windows / Windows PAM 7.4.0–7.4.7, 7.2.0–7.2.14; FortiClient Mac 7.4.0–7.4.7 | 7.4.8 / 7.2.15 |
| [CVE-2026-99273](CVE-2026-99273) | Linux kernel (ksmbd) | unknown | Linux < 7.3.2 with CONFIG_SMB_SERVER | mainline a025c4991a7d8; stable 6.12.117 / 6.18.61 / 7.3.2 |
| [CVE-2026-13043](CVE-2026-13043) | WatchGuard Endpoint Security | 4.0 9.3 (WatchGuard) | WatchGuard Endpoint Security < 8.00.26.0012 (Windows) | 8.00.26.0012 |
| [CVE-2026-133274](CVE-2026-133274) | THC-Hydra | 4.0 7.1 (VulnCheck); 3.1 6.5 (VulnCheck) | THC-Hydra through 9.7 | commit 6ab9ad8 (post-9.7, no release tagged) |
| [CVE-2026-133305](CVE-2026-133305) | sqlmap | 4.0 2.3 (VulnCheck); 3.1 4.3 (VulnCheck) | sqlmap before 1.10.11.89 | 1.10.11.89 |
| [CVE-2026-133189](CVE-2026-133189) | Cinder | 3.1 9.6 (Red Hat) | OpenStack Cinder with SSH-based storage drivers | Upstream patch proposed, no fixed release published (2026-11-19) |
| [CVE-2026-130778](CVE-2026-130778) | Incus | 4.0 10.0 (VulnCheck); 3.1 10.0 (VulnCheck) | Incus <7.6.0 | 7.6.0 / 6.0.9 LTS |
| [CVE-2026-130786](CVE-2026-130786) | Incus | 4.0 9.4 (VulnCheck); 3.1 9.9 (VulnCheck) | Incus <7.6.0 | 7.6.0 / 6.0.9 LTS |
| [CVE-2026-132891](CVE-2026-132891) | JetBrains TeamCity | 3.1 9.8 (JetBrains) | TeamCity 2026.1 <2026.1.4, 2025.11 <2025.11.8 | 2026.2 / 2026.1.4 / 2025.11.8 |
| [CVE-2026-123890](CVE-2026-123890) | VMware vCenter | 3.1 9.8 (VMware) | vCenter 9.1.x / 9.0.x / 8.0 / 5.x | 9.1.1.0200 / 9.0.2.0200 / 8.0 U3m / 5.2.5 |
| [CVE-2026-132234](CVE-2026-132234) | TeamCity | 3.1 9.9 (JetBrains) | TeamCity 2026.1 <2026.1.3 / <2025.11.7 | 2026.1.3 / 2025.11.7 |
| [CVE-2026-132233](CVE-2026-132233) | TeamCity | 3.1 9.9 (JetBrains) | TeamCity 2026.1 <2026.1.3 / <2025.11.7 | 2026.1.3 / 2025.11.7 |
| [CVE-2026-132232](CVE-2026-132232) | TeamCity | 3.1 9.9 (JetBrains) | TeamCity 2026.1 <2026.1.3 / <2025.11.7 | 2026.1.3 / 2025.11.7 |
| [CVE-2026-132231](CVE-2026-132231) | TeamCity | 3.1 9.9 (JetBrains) | TeamCity 2026.1 <2026.1.3 / <2025.11.7 | 2026.1.3 / 2025.11.7 |
| [CVE-2026-130784](CVE-2026-130784) | Incus | 4.0 9.4 (VulnCheck); 3.1 9.9 (VulnCheck) | Incus <7.6.0 | 7.6.0 |
| [CVE-2026-130780](CVE-2026-130780) | Incus | 4.0 9.4 (VulnCheck); 3.1 9.9 (VulnCheck) | Incus <7.6.0 | 7.6.0 |
| [CVE-2026-129991](CVE-2026-129991) | Dokploy | 3.1 9.9 (GHSA) | Dokploy <0.31.1 | 0.31.1 |
| [CVE-2026-129316](CVE-2026-129316) | Dokploy | 3.1 9.9 (GHSA) | Dokploy 0.29.13 to <0.31.0 | 0.31.0 |
| [CVE-2026-129986](CVE-2026-129986) | Dokploy | 3.1 9.9 (GHSA) | Dokploy <0.31.1 | 0.31.1 |
| [CVE-2026-129989](CVE-2026-129989) | Dokploy | 3.1 9.9 (GHSA) | Dokploy <0.31.1 | 0.31.1 |
| [CVE-2026-130759](CVE-2026-130759) | Fleet | 4.0 9.4 (VulnCheck); 3.1 9.9 (VulnCheck) | Fleet 4.71.0 to <4.88.2 | 4.88.2 |
| [CVE-2026-130771](CVE-2026-130771) | Incus | 4.0 8.5 (VulnCheck); 3.1 9.9 (VulnCheck) | Incus <7.6.0 | 7.6.0 |
| [CVE-2026-130773](CVE-2026-130773) | Incus | 4.0 9.4 (VulnCheck); 3.1 9.9 (VulnCheck) | Incus <7.6.0 | 7.6.0 |
| [CVE-2026-126752](CVE-2026-126752) | Dagu | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | Dagu 1.23.0 to <2.0.0 | 2.0.0 |
| [CVE-2026-73969](CVE-2026-73969) | AnsibleForms | 3.1 9.8 (GHSA) | AnsibleForms <6.2.1 | 6.2.1 |
| [CVE-2026-130779](CVE-2026-130779) | Incus | 4.0 8.5 (VulnCheck); 3.1 9.6 (VulnCheck) | Incus <7.6.0 | 7.6.0 |
| [CVE-2026-130783](CVE-2026-130783) | Incus | 4.0 9.3 (VulnCheck); 3.1 9.6 (VulnCheck) | Incus <7.6.0 | 7.6.0 |
| [CVE-2026-126088](CVE-2026-126088) | OpenPLC Runtime | 4.0 9.2 (CISA); 3.1 8.1 (CISA) | OpenPLC Runtime <=4.2.4 | 4.3.0 |
| [CVE-2026-111760](CVE-2026-111760) | Git | 3.1 8.0 (GHSA) | Git 2.50.2、2.51.3、2.52.1、2.53.1、2.54.1、2.55.1、2.56.1 之前版本 | 2.50.2、2.51.3、2.52.1、2.53.1、2.54.1、2.55.1、2.56.1 |
| [CVE-2026-97631](CVE-2026-97631) | EDK II | 4.0 9.5 (TianoCore); 3.1 8.8 (Red Hat) | TianoCore EDK II NetworkPkg UefiPxeBcDxe（edk2-stable202608 及更早） | 上游主線 PR #13200/#13302（2026-10-15 合併）；Red Hat RHSA-2026:96240 |
| [CVE-2026-120382](CVE-2026-120382) | Synology DiskStation Manager | 3.1 9.8 (Synology) | DSM before 7.1.1-42962-10 / 7.2.1-69057-14 / 7.2.2-72806-11 / 7.3.2-86009-6 / 7.4.1-90080-2 | 7.4.1-90080-2 / 7.3.2-86009-6 |
| [CVE-2026-77873](CVE-2026-77873) | Lenovo System Update | 4.0 7.0 (Lenovo); 3.1 7.3 (Lenovo) | Lenovo System Update for Windows, tested on 5.08.04.85 | Lenovo System Update 修復版本（LEN-232748） |
| [CVE-2026-77882](CVE-2026-77882) | Lenovo System Update | 4.0 8.5 (Lenovo); 3.1 7.8 (Lenovo) | Lenovo System Update for Windows, tested on 5.08.04.85 | Lenovo System Update 修復版本（LEN-232748） |
| [CVE-2026-99320](CVE-2026-99320) | Linux kernel (IPv6 raw sockets) | 3.1 7.0 (Linux kernel) | Linux kernel with VRF IPv6 output (exploit tuned to kernel 6.1.0-staleroute config) | 上游修復提交 66dfb2cacda7 |
| [CVE-2026-99491](CVE-2026-99491) | Linux kernel (wacom HID driver) | unknown | Linux kernel with wacom HID driver (Android 5.15.178, Redmi K70 vermeer) | 上游修復提交 ef32877368a7（6.12 backport 1178927ffa54） |
| [CVE-2026-41709](CVE-2026-41709) | VMware ESX | 3.1 2.7 (Broadcom) | VMware ESX 9.1.x.x / 9.0.x.x / 8.0; VMware Cloud Foundation 9.1.x.x / 9.0.x.x / 5.x; VMware Telco Cloud Platform 5.0.x / 5.1.x | ESXi-9.1.0.0-25370933 / ESXi-9.0.2.0100-25595025 / ESXi80U3j-25429389; VCF 5.x 5.2.4; TCP KB449886 (VMSA-2026-0006) |
| [CVE-2026-46300](CVE-2026-46300) | Linux kernel (net: skbuff) | 3.1 7.8 (NVD) | Linux kernel：skb_try_coalesce() 合併含共享 frag 的 skb 時丟失 SKBFL_SHARED_FRAG 標記的版本（修復前） | 上游修復提交 2f2b16022a2e（net: skbuff: preserve shared-frag marker during coalescing，stable 各分支另有 backport，見 NVD 補丁鏈接） |
| [CVE-2026-93585](CVE-2026-93585) | EasyVista EV Reach Client Agent | 3.1 8.8 (OTRS) | EV Reach Console < 11.0.14.1127 / Agent < 11.0.16 / Server < 11.0.14.1274 | 11.0.14.1127 / 11.0.16 / 11.0.14.1274 |
| [CVE-2026-59309](CVE-2026-59309) | VMware vCenter Server | 3.1 9.8 (VMware) | vCenter 8.0 prior to 8.0 U3k；9.0.x prior to 9.0.2.0100；9.1.x prior to 9.1.0.0200；6.x/7.x 亦受影響且無補丁 | 8.0 U3k；9.0.2.0100；9.1.0.0200 |
| [CVE-2026-88235](CVE-2026-88235) | Windows TrustedInstaller (CBS) | 3.1 7.8 (Microsoft) | Windows (TrustedInstaller.exe / CBS Session COM) |  |
| [CVE-2026-98260](CVE-2026-98260) | Linux kernel (posix-cpu-timers) | 3.1 7.8 (NVD) | Linux kernel 6.12.38 / 6.12.58 (Android 16, Honor MagicPad3 Pro) |  |
| [CVE-2026-123903](CVE-2026-123903) | VMware vCenter | 3.1 9.8 (Broadcom) | VMware vCenter 9.1.x, 9.0.x, 8.0, 7.0, 5.x（VMware Directory Service，vmdir） | 9.1.2 / 9.0.2.0300 / 8.0 U3m / 5.2.5；7.0 需聯繫 Broadcom 支援 |
| [CVE-2026-31431](CVE-2026-31431) | Linux kernel | 3.1 7.8 (Linux) | Linux kernel built since 2017, before fix commit a664bf3d603d | mainline commit a664bf3d603d |
| [CVE-2026-43284](CVE-2026-43284) | Linux kernel | 3.1 8.8 (Linux) | Linux kernel 4.11 – 7.0.5 (stable branches fixed at 5.10.255, 5.15.205, 6.1.171, 6.6.138, 6.12.87, 6.18.28, 7.0.5) | 5.10.255, 5.15.205, 6.1.171, 6.6.138, 6.12.87, 6.18.28, 7.0.5 (per stable branch) |
| [CVE-2026-59310](CVE-2026-59310) | VMware vCenter Server | 3.1 9.8 (Broadcom) | VMware vCenter Server 7.0, 8.0, 9.0.x, 9.1.x (VMware Cloud Foundation, vSphere Foundation, Telco Cloud Platform, Telco Cloud Infrastructure) | 9.1.0.0300; 9.0.2.0100; 8.0 U3k; 8.0 U2f (7.0: contact Broadcom Support under extended support) |
| [CVE-2026-104007](CVE-2026-104007) | LibreOffice | 4.0 8.5 (The Document Foundation) | LibreOffice 26.2.x（26.2.7 之前）、26.8.x（26.8.2 之前）；需安裝並啟用 Java 執行環境 | 26.2.7 / 26.8.2 |
| [CVE-2026-104692](CVE-2026-104692) | LibreOffice | 4.0 8.5 (The Document Foundation) | LibreOffice 26.2.x（26.2.7 之前）、26.8.x（26.8.2 之前）；需安裝並啟用 Java 執行環境 | 26.2.7 / 26.8.2 |
| [CVE-2026-96951](CVE-2026-96951) | Microsoft Windows Shell | 3.1 8.8 (Microsoft) | Windows Shell（Windows 10 / 11、Windows Server 2019 / 2022 / 2025，見 MSRC 更新清單） | 2026-10-13 安全更新（Windows 11 24H2 10.0.26100.9711、25H2 10.0.26200.9711、Windows 10 22H2 10.0.19045.7807 等） |
| [CVE-2026-102490](CVE-2026-102490) | Zammad | 4.0 9.4 (DIVD); 3.1 7.8 (NVD) | packager.io 打包的 Zammad DEB/RPM 安裝（7.2.2 之前，NVD CPE） | 尚未發布（2026-10-05 通告讀取時仍在制定解決方案） |
| [CVE-2026-110936](CVE-2026-110936) | Siemens Software Center | 4.0 8.4 (Siemens); 3.1 6.7 (Siemens) | Siemens Software Center V4.0.9.8 之前全部版本 | V4.0.9.8 |
| [CVE-2026-131827](CVE-2026-131827) | RustDesk Client for Windows | 3.0 7.8 (ZDI) | RustDesk Client for Windows | PR #17040 已合併（2026-11-16，版本號未註明） |
| [CVE-2026-59831](CVE-2026-59831) | GitHub CLI | 3.1 4.4 (GHSA) | gh 2.10.0–2.95.x | 2.96.0 |
| [CVE-2026-45152](CVE-2026-45152) | uniget | 3.1 7.8 (GHSA) | uniget prior to 0.27.1 | 0.27.1 |
| [CVE-2026-133842](CVE-2026-133842) | Flatpak | 3.1 8.2 (GHSA) | Flatpak < 1.18.5；1.19.x < 1.19.3 | 1.18.6；1.19.4 |


See each CVE directory for details and references.
