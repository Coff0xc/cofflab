# 運行環境 / 框架 / 瀏覽器（113）

[回到完整目錄](../README.zh-TW.md) · [所有分類](README.zh-TW.md)

### 運行環境 / 框架 / 瀏覽器 (113)

| ID | 產品 | 評分 | 影響版本 | 修復版本 |
| --- | --- | --- | --- | --- |
| [CVE-2026-57898](../CVE-2026-57898) | Eclipse BaSyx Java Server SDK | 3.1 9.0 (Eclipse) | Eclipse BaSyx Java Server SDK 2.0.0-milestone-05–2.0.0-milestone-12 (MongoDB backend) | 2.0.0-milestone-13 |
| [CVE-2026-114938](../CVE-2026-114938) | OpenJDK Base64（Java4Shell） | 4.0 9.2 (Calif); 3.1 8.1 (Oracle); 3.1 9.8 (Red Hat) | OpenJDK 17.0.6 and later on x86-64 with AVX-512 VBMI (17/21/25/27 lines; Oracle also lists Java 8 Performance Pack 8u511b33-perf) | vendor November 2026 CPU / OpenJDK 17.0.21.1, 21.0.13.1 and equivalent distributor builds |
| [CVE-2026-90436](../CVE-2026-90436) | Apache Axis 1.x | 3.1 9.8 (CISA-ADP) | Apache Axis 1.x through 1.4 | 無修復版本（EOL；修復僅存於上游 commit 41f3b4e8） |
| [CVE-2024-27834](../CVE-2024-27834) | WebKit (Apple) | 3.1 5.5 (NVD) | Safari < 17.5；iOS/iPadOS < 16.7.8 及 17.x < 17.5；macOS < 14.5；tvOS < 17.5；watchOS < 10.5；WebKitGTK / WPE WebKit < 2.44.2 | Safari 17.5；iOS 16.7.8 / iOS 17.5；iPadOS 16.7.8 / iPadOS 17.5；macOS Sonoma 14.5；tvOS 17.5；watchOS 10.5 |
| [CVE-2026-126187](../CVE-2026-126187) | React Server Components / Next.js | 4.0 9.5 (GHSA) | react-server-dom-* 19.0.0–19.3.0; Next.js 16.0.0–16.4.0 (App Router + Cache Components) | react-server-dom-* 19.0.9 / 19.1.10 / 19.2.9 / 19.3.1; Next.js 16.4.1 |
| [CVE-2026-125350](../CVE-2026-125350) | Google Chrome | 3.1 8.8 (NVD) | Chrome < 157.0.8103.50 | 157.0.8103.50 / .51 (Windows, macOS), 157.0.8103.50 (Linux, Android), Extended Stable 156.0.8078.96 |
| [CVE-2026-111497](../CVE-2026-111497) | Node.js Brotli | 4.0 9.2 (Google); 3.1 9.8 (NVD) | Node.js < 22.23.4, < 24.22.1, < 26.12.1; Bun < 1.4.4; Brotli 1.0.3-1.2.0 | Node.js 22.23.4 / 24.22.1 / 26.12.1; Bun 1.4.4; Brotli 1.2.1 |
| [CVE-2026-129349](../CVE-2026-129349) | Apache Shiro DefaultLdapRealm | 4.0 9.1 (Apache) | Apache Shiro through 3.0.0 with DefaultLdapRealm/JndiLdapRealm and authenticationCachingEnabled=true (not the default) | 3.0.1 |
| [CVE-2026-86829](../CVE-2026-86829) | Apache Airflow 核心 | 3.1 8.8 (Apache) | apache-airflow-core < 3.4.0 | 3.4.0 (apache/airflow PR #72718) |
| [CVE-2026-115560](../CVE-2026-115560) | PHP session 上传进度 | 4.0 9.2 (PHP) | PHP with session.serialize_handler=php_binary or php_serialize in server config, application switching to php at runtime via ini_set() before session_start(), and session.upload_progress.enabled=1 (PHP default). Validated on php:8.4.27-apache. | 8.5.13 / 8.4.28 / 8.3.37 / 8.2.36 (2026-11-19) |
| [CVE-2026-75604](../CVE-2026-75604) | Windows 上的 Next.js | 3.1 9.0 (GHSA) | Next.js 13.4.0–15.5.23 and 16.0.0–16.3.2 on Windows, Pages Router + App Router without Cache Components | 15.5.24 / 16.3.3 |
| [CVE-2026-115893](../CVE-2026-115893) | Wasmtime | 3.1 9.9 (GHSA) | Wasmtime < 36.0.19, 37.0.0-42.x, 43.0.0-48.0.6, 49.0.0-49.0.3 (aarch64 Cranelift) | 36.0.19, 48.0.7, 49.0.4 |
| [CVE-2026-109618](../CVE-2026-109618) | PHP | 3.1 9.8 (NVD); 4.0 9.2 (PHP) | PHP 5.4.0-8.5.11 | 8.2.35, 8.3.36, 8.4.27, 8.5.12 |
| [CVE-2026-109619](../CVE-2026-109619) | PHP | 3.1 8.1 (NVD); 4.0 9.2 (PHP) | PHP 5.4.0-8.5.11 | 8.2.35, 8.3.36, 8.4.27, 8.5.12 |
| [CVE-2026-126910](../CVE-2026-126910) | Chrome V8 Maglev | 3.1 8.8 (NVD) | Chrome before 157.0.8103.78 | 157.0.8103.78 |
| [CVE-2026-128134](../CVE-2026-128134) | NLTK dot2img | 3.1 7.8 (GHSA) | NLTK before 3.10.4 | 3.10.4 |
| [CVE-2026-130001](../CVE-2026-130001) | mustache (Ruby) | 3.1 9.8 (GHSA) | mustache gem <= 1.1.2 | 1.1.3 |
| [CVE-2026-47884](../CVE-2026-47884) | Spring Framework XsltView | 3.1 9.8 (GHSA) | Spring Framework 5.2.x–5.3.49, 6.0.x–6.0.30, 6.1.x–6.1.28, 6.2.x–6.2.19, 7.0.0–7.0.8 (XsltView + catch-all /** mapping + implicit view name) | 5.3.50 / 6.0.31 / 6.1.29 / 6.2.20 / 7.0.9 |
| [CVE-2026-131842](../CVE-2026-131842) | Poppler pdfdetach | 4.0 5.7 (VulnCheck) | Poppler pdfdetach 24.03.0–26.11.0 | none (upstream work item 1826 open) |
| [CVE-2026-131873](../CVE-2026-131873) | Gargoyle | 4.0 6.9 (VulnCheck) | Gargoyle 2023.1–2026.1.1 | Spatterlight 1.5.5 import (commit 45385f1) |
| [CVE-2026-121265](../CVE-2026-121265) | SQL::Abstract | 3.1 9.8 (GHSA) | SQL::Abstract < 2.000003 | 2.000003 |
| [CVE-2026-107360](../CVE-2026-107360) | rubygem-safemode | 3.1 9.6 (Red Hat) | rubygem-safemode through 2.0.3; Red Hat Satellite 6.16–6.18 | upstream PR #75 (unmerged); rubygem-safemode 1.5.0-3.el8sat / 1.5.0-3.el9sat |
| [CVE-2026-128027](../CVE-2026-128027) | FrankenPHP | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | FrankenPHP images built before 2026-02-04 (< 1.1.11) | 1.1.11 |
| [CVE-2026-128014](../CVE-2026-128014) | FrankenPHP | 4.0 9.2 (VulnCheck); 3.1 8.1 (GHSA) | FrankenPHP 1.13.1 (Brotli 1.2.0); all builds shipping Brotli < 1.2.1 | 1.13.2 (Brotli 1.2.1) |
| [CVE-2026-123753](../CVE-2026-123753) | Apache Axis2/Java | 3.1 9.1 (GHSA) | Apache Axis2/Java < 2.0.2 (PoC tested 2.0.1) | 2.0.2 |
| [CVE-2026-132825](../CVE-2026-132825) | Ruby | 3.1 7.4 (MITRE) | Ruby < 3.3.14; 3.4.0-< 3.4.13; 4.0.0-< 4.0.10 | 3.3.14 / 3.4.13 / 4.0.10 |
| [CVE-2026-133168](../CVE-2026-133168) | DCMTK | 4.0 8.5 (VulnCheck); 3.1 7.8 (VulnCheck) | DCMTK 3.7.1 | 3.7.2 (patch pending; fix commit c22836c, no release tagged) |
| [CVE-2026-133243](../CVE-2026-133243) | node-soap | 4.0 8.8 (VulnCheck); 3.1 8.2 (VulnCheck) | node-soap before 1.14.1 | 1.14.1 |
| [CVE-2026-71164](../CVE-2026-71164) | Helidon | 3.1 9.8 (Oracle) | Helidon 3.0.0-3.2.17 (Imperative Web Server) | 3.2.18 (Oracle CSPU Aug 2026) |
| [CVE-2026-133307](../CVE-2026-133307) | ClassiCube | 4.0 8.7 (VulnCheck); 3.1 8.8 (VulnCheck) | ClassiCube before 1.4.0 | 1.4.0 |
| [CVE-2026-116499](../CVE-2026-116499) | Qiskit SDK | 3.1 8.4 (IBM) | Qiskit SDK v1.4.2-v2.6.2 | 2.6.2 (IBM patched release) |
| [CVE-2026-133254](../CVE-2026-133254) | IntelliJ IDEA | 3.1 8.3 (JetBrains) | IntelliJ IDEA before 2026.3, 2026.2.4 | 2026.3 / 2026.2.4 |
| [CVE-2026-130886](../CVE-2026-130886) | @fastify/reply-from | 3.1 8.2 (GHSA) | @fastify/reply-from 12.8.1-12.8.3 | 12.8.4 |
| [CVE-2026-92937](../CVE-2026-92937) | vm2 | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | vm2 3.11.6 | 3.11.7 |
| [CVE-2026-0881](../CVE-2026-0881) | Firefox | 3.1 10.0 (Mozilla) | Firefox <147, Thunderbird <147 | Firefox 147 / Thunderbird 147 (MFSA2026-01) |
| [CVE-2026-92940](../CVE-2026-92940) | vm2 | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | vm2 3.11.3-3.11.6 | 3.11.7 |
| [CVE-2026-92941](../CVE-2026-92941) | vm2 | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | vm2 3.11.3-<3.11.7 | 3.11.7 |
| [CVE-2026-92946](../CVE-2026-92946) | vm2 | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | vm2 before 3.11.7 | 3.11.7 |
| [CVE-2026-92947](../CVE-2026-92947) | vm2 | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | vm2 before 3.11.7 | 3.11.7 |
| [CVE-2026-92955](../CVE-2026-92955) | vm2 | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | vm2 before 3.11.8 | 3.11.8 |
| [CVE-2026-92956](../CVE-2026-92956) | vm2 | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | vm2 3.10.1-3.11.6 | 3.11.7 |
| [CVE-2026-92960](../CVE-2026-92960) | vm2 | 3.1 10.0 (VulnCheck); 4.0 10.0 (VulnCheck) | vm2 before 3.11.6 | 3.11.6 |
| [CVE-2026-92953](../CVE-2026-92953) | vm2 | 3.1 10.0 (VulnCheck); 4.0 9.3 (VulnCheck) | vm2 3.11.0-3.11.7 | 3.11.8 |
| [CVE-2026-92948](../CVE-2026-92948) | vm2 | 3.1 9.9 (VulnCheck); 4.0 9.4 (VulnCheck) | vm2 3.9.6-3.11.6 | 3.11.7 |
| [CVE-2026-92951](../CVE-2026-92951) | vm2 | 3.1 9.9 (VulnCheck); 4.0 9.4 (VulnCheck) | vm2 before 3.11.7 | 3.11.7 |
| [CVE-2026-92957](../CVE-2026-92957) | vm2 | 3.1 9.9 (VulnCheck); 4.0 9.4 (VulnCheck) | vm2 through 3.11.6 | 3.11.7 |
| [CVE-2026-92944](../CVE-2026-92944) | vm2 | 3.1 9.8 (VulnCheck); 4.0 9.3 (VulnCheck) | vm2 3.10.2-3.11.6 | 3.11.7 |
| [CVE-2026-128138](../CVE-2026-128138) | NLTK | 3.1 9.8 (GitHub) | NLTK 3.10.3-<3.10.4 | 3.10.4 |
| [CVE-2026-92950](../CVE-2026-92950) | vm2 | 3.1 8.6 (VulnCheck); 4.0 9.3 (VulnCheck) | vm2 before 3.11.7 | 3.11.7 |
| [CVE-2026-92954](../CVE-2026-92954) | vm2 | 3.1 8.6 (VulnCheck); 4.0 9.2 (VulnCheck) | vm2 3.10.0-3.11.7 | 3.11.8 |
| [CVE-2026-92958](../CVE-2026-92958) | vm2 | 3.1 8.5 (VulnCheck); 4.0 8.4 (VulnCheck) | vm2 through 3.11.6 | 3.11.7 |
| [CVE-2026-92943](../CVE-2026-92943) | AWS IoT Device SDK for Python | 3.1 8.1 (AMZN); 4.0 9.2 (AMZN) | AWS IoT Device SDK for Python 1.5.3-1.6.0 | 1.6.1 |
| [CVE-2026-130235](../CVE-2026-130235) | Okta .NET SDK Abstractions | 3.1 8.7 (Okta) | Okta .NET SDK Abstractions 1.0.0-beta-4.0.7 | 4.0.8 |
| [CVE-2026-130179](../CVE-2026-130179) | Okta .NET SDK Abstractions | 3.1 8.5 (Okta) | Okta .NET SDK Abstractions 3.0.0-4.0.7 | 4.0.8 |
| [CVE-2026-61798](../CVE-2026-61798) | netty-incubator-codec-ohttp | 3.1 8.1 (GitHub) | netty-incubator-codec-ohttp <0.0.23.Final | 0.0.23.Final |
| [CVE-2026-130234](../CVE-2026-130234) | Okta Swift Management SDK | 3.1 8.0 (Okta) | Okta Swift Management SDK <0.1.1 | 0.1.1 |
| [CVE-2026-130756](../CVE-2026-130756) | pnpm exe | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | pnpm exe <10.34.8, 11.x <11.28.8 | 10.34.8 / 11.28.8 |
| [CVE-2019-25782](../CVE-2019-25782) | ThinkPHP | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | ThinkPHP 5.0.0-5.0.23 | 5.0.24 |
| [CVE-2012-20007](../CVE-2012-20007) | ThinkPHP | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | ThinkPHP 2.0-2.2 / 3.0 Lite | No known patch |
| [CVE-2026-83020](../CVE-2026-83020) | Oracle Platform Security for Java | 3.1 10 (Oracle) | Oracle Platform Security for Java 12.2.1.4.0 / 14.1.2.0.0 | September 2026 Critical Security Patch Update |
| [CVE-2026-82994](../CVE-2026-82994) | Oracle Platform Security for Java | 3.1 9.8 (Oracle) | Oracle Platform Security for Java 12.2.1.4.0 / 14.1.2.0.0 | September 2026 Critical Security Patch Update |
| [CVE-2026-82995](../CVE-2026-82995) | Oracle Platform Security for Java | 3.1 9.8 (Oracle) | Oracle Platform Security for Java 12.2.1.4.0 / 14.1.2.0.0 | September 2026 Critical Security Patch Update |
| [CVE-2026-91570](../CVE-2026-91570) | Oracle WebLogic Server | 3.1 9.8 (Oracle) | Oracle WebLogic Server 12.2.1.4.0 / 14.1.1.0.0 / 14.1.2.0.0 / 15.1.1.0.0 | November 2026 Critical Patch Update |
| [CVE-2026-91583](../CVE-2026-91583) | Oracle WebLogic Server | 3.1 9.8 (Oracle) | Oracle WebLogic Server 12.2.1.4.0 / 14.1.1.0.0 / 14.1.2.0.0 / 15.1.1.0.0 | November 2026 Critical Patch Update |
| [CVE-2026-91585](../CVE-2026-91585) | Oracle WebLogic Server | 3.1 9.8 (Oracle) | Oracle WebLogic Server 12.2.1.4.0 / 14.1.1.0.0 / 14.1.2.0.0 / 15.1.1.0.0 | November 2026 Critical Patch Update |
| [CVE-2026-103119](../CVE-2026-103119) | Apache Tomcat | 3.1 9.1 (NVD) | Apache Tomcat 11.0.0-M25 to 11.0.26 | 11.0.27 |
| [CVE-2026-133528](../CVE-2026-133528) | BeamNG.drive | 4.0 9.3 (VulnCheck); 3.1 8.6 (VulnCheck) | BeamNG.drive <0.40.6 | 0.40.6 |
| [CVE-2026-127064](../CVE-2026-127064) | @fastify/reply-from | 3.1 8.2 (OpenJSF) | @fastify/reply-from <12.8.4 | 12.8.4 |
| [CVE-2026-117659](../CVE-2026-117659) | InfoScan | 4.0 8.5 (CISA); 3.1 8.1 (CISA) | Dorsett Controls InfoScan <=1.45.0 | 1.46 |
| [CVE-2026-129496](../CVE-2026-129496) | PHP | 4.0 9.2 (PHP Group) | PHP 8.2 <8.2.36 / 8.3 <8.3.37 / 8.4 <8.4.28 / 8.5 <8.5.13 | 8.2.36 / 8.3.37 / 8.4.28 / 8.5.13 |
| [CVE-2026-129474](../CVE-2026-129474) | PHP | 4.0 9.2 (PHP Group) | PHP 8.5.0–<8.5.13 | 8.5.13 |
| [CVE-2026-126714](../CVE-2026-126714) | PHP | 4.0 9.2 (PHP Group) | PHP 8.2 <8.2.36 / 8.3 <8.3.37 / 8.4 <8.4.28 / 8.5 <8.5.13 | 8.2.36 / 8.3.37 / 8.4.28 / 8.5.13 |
| [CVE-2026-129289](../CVE-2026-129289) | PHP | 4.0 9.2 (PHP Group) | PHP 8.2 <=8.2.35 / 8.3 <=8.3.36 / 8.4 <=8.4.27 / 8.5 <=8.5.12 | 8.2.36 / 8.3.37 / 8.4.28 / 8.5.13 |
| [CVE-2026-133212](../CVE-2026-133212) | @fastify/reply-from | 3.1 9.0 (OpenJSF) | @fastify/reply-from before 12.9.1 | 12.9.1 |
| [CVE-2026-77355](../CVE-2026-77355) | isomorphic-git | 3.1 8.8 (GHSA) | isomorphic-git before 1.38.7 (Windows NTFS) | 1.38.7 |
| [CVE-2026-86017](../CVE-2026-86017) | isomorphic-git | 3.1 8.0 (GHSA) | isomorphic-git before 1.38.8 (cherry-pick symlink) | 1.38.8 |
| [CVE-2026-104711](../CVE-2026-104711) | Apache Struts | 3.1 9.8 (NVD); 3.1 8.1 (Apache) | 2.0.0-2.3.37, 2.5.0-2.5.33, 6.0.0-6.11.0, 7.0.0-7.3.0 | 6.12.0 (6.x), 7.4.0 (7.x) |
| [CVE-2026-133325](../CVE-2026-133325) | Apache Tomcat | 3.1 9.8 (NVD) | 11.0.28-11.0.29, 10.1.62, 9.0.124 |  |
| [CVE-2026-95517](../CVE-2026-95517) | Apache Tomcat | 3.1 9.1 (NVD) | 11.0.0-M1-11.0.27, 10.1.0-M1-10.1.61, 9.0.13-9.0.123 | 11.0.29, 10.1.62, 9.0.124 |
| [CVE-2026-124626](../CVE-2026-124626) | @fastify/express | 3.1 9.1 (NVD) | 4.0.5-4.0.9 | 4.0.10 |
| [CVE-2026-129504](../CVE-2026-129504) | @fastify/express | 3.1 9.1 (NVD) | 4.0.0-4.0.9 | 4.0.10 |
| [CVE-2026-133120](../CVE-2026-133120) | @fastify/express | 3.1 9.1 (NVD) | < 4.0.10 | 4.0.10 |
| [CVE-2026-133250](../CVE-2026-133250) | @fastify/middie | 3.1 9.1 (NVD) | <= 9.3.7 | 9.3.8 |
| [CVE-2026-133867](../CVE-2026-133867) | @fastify/express | 3.1 9.1 (NVD) | 4.0.7-4.0.9 | 4.0.10 |
| [CVE-2026-134814](../CVE-2026-134814) | binary-parser | 4.0 9.2 (VulnCheck); 3.1 8.1 (GHSA) | binary-parser before 2.3.1 | 2.3.1 |
| [CVE-2026-134815](../CVE-2026-134815) | simple-git | 4.0 9.2 (VulnCheck); 3.1 8.1 (VulnCheck) | simple-git before 4.1.0 | 4.1.0 |
| [CVE-2026-125396](../CVE-2026-125396) | Ghostscript | 4.0 8.5 (VulnCheck); 3.1 7.8 (VulnCheck) | Ghostscript before 10.08.0 | 10.08.0 |
| [CVE-2026-129975](../CVE-2026-129975) | gpgme | 3.1 8.1 (Red Hat) | gpgme |  |
| [CVE-2026-119348](../CVE-2026-119348) | Next.js | 4.0 6.3 (GitHub) | Next.js <= 15.5.28 and 16.0.0-16.4.4 (self-hosted) | 15.5.29 / 16.4.5 |
| [CVE-2026-135736](../CVE-2026-135736) | FFmpeg | 4.0 9.2 (VulnCheck); 3.1 8.1 (VulnCheck) | FFmpeg 4.4 before 9.1 | 9.1 |
| [CVE-2026-135743](../CVE-2026-135743) | FFmpeg | 4.0 9.2 (VulnCheck); 3.1 8.1 (VulnCheck) | FFmpeg 4.3 before 9.1 | 9.1 |
| [CVE-2026-123886](../CVE-2026-123886) | Spring Data Elasticsearch | 3.1 8.8 (VMware) | Spring Data Elasticsearch versions before 2a5b65c | 2a5b65c |
| [CVE-2026-42290](../CVE-2026-42290) | protobufjs-cli | 3.1 7.8 (GitHub) | protobufjs-cli < 1.2.1 and < 2.0.2 | 1.2.1、2.0.2 |
| [CVE-2026-46595](../CVE-2026-46595) | golang.org/x/crypto/ssh | 3.1 10.0 (CISA-ADP) | golang.org/x/crypto < v0.52.0 | v0.52.0 |
| [CVE-2026-134824](../CVE-2026-134824) | nektos/act | 4.0 6.8 (VulnCheck) | nektos/act 0.2.92–0.2.97 | 0.2.98 |
| [CVE-2026-105803](../CVE-2026-105803) | Git LFS | 4.0 8.6 (GHSA) | Git LFS >= 1.3.0, <= 2.13.3 and >= 3.0.0, < 3.8.1 | 3.8.1 |
| [CVE-2026-134401](../CVE-2026-134401) | Google Chrome | 3.1 9.6 (CISA-ADP) | Google Chrome < 158.0.8127.88 | 158.0.8127.88 (Windows/Mac/Linux); Extended Stable 156.0.8078.114 |
| [CVE-2026-65320](../CVE-2026-65320) | fastcore | 4.0 9.2 (VulnCheck); 3.1 8.1 (VulnCheck) | fastcore through 2.2.44 | unknown |
| [CVE-2026-136412](../CVE-2026-136412) | stream-lua-nginx-module | 4.0 9.2 (VulnCheck); 3.1 8.1 (GHSA) | stream-lua-nginx-module < 0.0.20rc4 | 0.0.20rc4 |
| [CVE-2026-33186](../CVE-2026-33186) | gRPC-Go | 3.1 9.1 (GHSA) | gRPC-Go before 1.79.3 | 1.79.3 |
| [CVE-2026-34486](../CVE-2026-34486) | Apache Tomcat | 3.1 7.5 (Apache) | 11.0.0-M1 to 11.0.20; 10.1.0-M1 to 10.1.53; 9.0.13 to 9.0.116 | 11.0.21; 10.1.54; 9.0.117 |
| [CVE-2026-66066](../CVE-2026-66066) | Ruby on Rails | 4.0 9.5 (GHSA) | Active Storage < 7.2.3.2; >= 8.0.0.beta1, < 8.0.5.1; >= 8.1.0.beta1, < 8.1.3.1 | 7.2.3.2; 8.0.5.1; 8.1.3.1 |
| [CVE-2026-77423](../CVE-2026-77423) | JLine3 | 3.1 7.5 (GHSA) | org.jline:jline-builtins >= 3.0.0, < 3.30.15; < 4.3.1 | 3.30.15 / 4.3.1 |
| [CVE-2026-118264](../CVE-2026-118264) | labstack Echo | 4.0 9.1 (GHSA) | Echo v4 >= 4.0.0, < 4.16.1；Echo v5 >= 5.0.0, < 5.4.1 | v4.16.1 / v5.4.1 |
| [CVE-2026-47892](../CVE-2026-47892) | Spring Framework（WebFlux） | 3.1 9.8 (GHSA) | Spring Framework 5.2.5.RELEASE–5.2.25.RELEASE、5.3.0–5.3.49、6.0.0–6.0.30、6.1.0–6.1.28、6.2.0–6.2.19、7.0.0–7.0.8 | 7.0.9（OSS）；5.2.26.RELEASE / 5.3.50 / 6.0.31 / 6.1.29 / 6.2.20（企業支援） |
| [CVE-2026-63471](../CVE-2026-63471) | fastapi-code-generator | 4.0 9.3 (GHSA) | fastapi-code-generator < 0.8.1 | 0.8.1 |
| [CVE-2026-84939](../CVE-2026-84939) | Apache FreeMarker | 3.1 9.1 (GHSA) | Apache FreeMarker 2.2.0–2.3.34 | 2.3.35 |
| [CVE-2026-137550](../CVE-2026-137550) | Frappe Framework | 4.0 9.3 (VulnCheck); 3.1 9.8 (VulnCheck) | Frappe Framework < 15.122.0；16.x < 16.50.0 | 15.122.0 / 16.50.0 |
| [CVE-2026-22683](../CVE-2026-22683) | Windmill | 3.1 8.8 (GHSA); 4.0 8.7 (VulnCheck) | Windmill 1.56.0 起，1.614.0 之前 | 1.615.0 |
| [CVE-2026-23696](../CVE-2026-23696) | Windmill | 3.1 9.9 (GHSA); 4.0 9.4 (VulnCheck) | Windmill CE 與 EE 1.276.0 起，1.603.2 之前 | 1.603.3 |
| [CVE-2026-29059](../CVE-2026-29059) | Windmill | 3.1 7.5 (NVD); 4.0 6.9 (GHSA) | Windmill < 1.603.3 | 1.603.3 |
| [CVE-2026-138154](../CVE-2026-138154) | POSTAL 2 | 4.0 9.3 (VulnCheck); 3.1 8.6 (GHSA) | POSTAL 2 build < 26810491（Windows，Steam Workshop 模組） | POSTAL 2 build 26810491 |
| [CVE-2026-101590](../CVE-2026-101590) | Helidon | 3.1 9.1 (Oracle) | Helidon 4.0.0–4.5.5 | October 2026 Critical Patch Update |
