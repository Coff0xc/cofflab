# cve-poc

CVE PoC / exploit 收藏。只放 CVE 的 PoC 与 exploit，不放其他的。

## 命名规范

- 顶层一个目录一个 CVE：`CVE-<年份>-<编号>/`，如 `CVE-2026-123007/`。
- 只有一个来源：文件直接放在 CVE 目录下，保持原仓库结构。
- 多个来源：`CVE-<编号>/<作者>-<简称>/`，作者与简称小写、连字符连接，如 `CVE-2026-114938/ikow-poc/`。
- 每个 CVE 目录只放该 CVE 的 PoC/exp 与来源自述，不放无关文件。

## 收录

| CVE | 产品 | 评分 | 内容 | 来源 |
| --- | --- | --- | --- | --- |
| CVE-2024-10441 | Synology DSM/BSM | 9.8 | patch-diff 还原 + 本地 LD_PRELOAD 验证，远程触发需先把 .so 放上目标；已进 KEV | Ntn10/cve-2024-10441-synology-rce |
| CVE-2026-40217 | BerriAI LiteLLM | 8.8 | 字节码改写绕过沙箱拿 root，docker-compose 钉住易受攻击镜像；已进 KEV | learner202649/CVE-2026-40217-PoC |
| CVE-2026-114938 | OpenJDK Base64（Java4Shell） | 9.2 | 5 个来源：触发器、崩溃/泄露复现、分析套件、教学实验、版本检测；完整 RCE 链未公开 | 见 [CVE-2026-114938/README.md](CVE-2026-114938/README.md) |
| CVE-2026-118383 | MongoDB Server | 9.5 | 副本集 UAF 崩溃复现 + Podman 实验环境；证实的是崩溃，未证实代码执行 | googlesky/CVE-2026-118383 |
| CVE-2026-123007 | F5 NGINX HTTP/2 | 9.2 | 作者本人发的完整 RCE 利用 + 最小触发器 | sfewer-r7/CVE-2026-123007 |
| CVE-2026-123488 | Craft CMS | 9.8 | 单文件利用，堆叠语句置 admin=1 | fixedbyreboot/CVE-2026-123488-POC |
| CVE-2026-129448 | Apache Roller | 9.8 | 2 个来源：检测+利用框架（RCE 需自备 ysoserial）与本地 mock 实验环境；与 CVE-2026-82384 同一漏洞 | 见 [CVE-2026-129448/README.md](CVE-2026-129448/README.md) |
| CVE-2026-90817 | Vanderbilt REDCap | 9.8 | 3 个来源：发现者自述利用、待填占位的利用框架、批量检测；已进 KEV | 见 [CVE-2026-90817/README.md](CVE-2026-90817/README.md) |

## 规则

- 只收公开 PoC/exp；收录前只读检查代码，不执行。
- 来源不限于 GitHub：Exploit-DB、Packet Storm、研究员博客、厂商通告等都收。
- 之后狩猎到的 CVE PoC/exp 都放进这个仓库，按上面的命名规范来。
- 假 PoC 藏木马是常见套路，跑之前先读代码；只在自己有权测试的机器和隔离环境里用。

## 免责

仅供授权安全研究与防御使用。
