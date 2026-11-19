# Coff0xc CVE 策展

Coff0xc 维护的 CVE 漏洞与公开 PoC 策展库。每条记录写的是我的判定：产品、评分、日期、公开材料实际证明了什么。依据在该 CVE 目录的 `README.md` 和 `meta.yaml`。

只收已经公开的材料，入库只读、不执行。仅供授权安全研究与防御。

## 目录

| CVE | 产品 | 评分 | 我的判定 |
| --- | --- | --- | --- |
| [CVE-2024-10441](CVE-2024-10441) | Synology DSM/BSM synoplugind | 3.1 9.8（公开 README，未复核厂商公告） | 补丁对比 + 本地验证，没有现成远程 exploit |
| [CVE-2026-40217](CVE-2026-40217) | BerriAI LiteLLM | 3.1 8.8 PR:L（公开 README） | 认证后实验室 RCE，需要 API key |
| [CVE-2026-114938](CVE-2026-114938) | OpenJDK Base64（Java4Shell） | 4.0 9.2 (Calif)；3.1 8.1 (Oracle)；3.1 9.8 (Red Hat) | 触发 / 崩溃 / 泄露 / 实验；没有公开通用 RCE |
| [CVE-2026-118383](CVE-2026-118383) | MongoDB Server 复制 | unknown | 实验室 UAF 崩溃，未证实代码执行 |
| [CVE-2026-123007](CVE-2026-123007) | F5 NGINX HTTP/2 | 4.0 9.2 (F5)；3.1 8.1 (F5) | 触发 + 仅新鲜 Docker 的 RCE 演示 |
| [CVE-2026-123488](CVE-2026-123488) | Craft CMS 元素搜索 | 3.1 9.8 (GHSA)；4.0 9.3 (GitHub) | 未认证 SQLi 写库 / 提权 |
| [CVE-2026-129448](CVE-2026-129448) | Apache Roller XML-RPC | 3.1 9.8（公开声称，未核验） | 框架需自备 gadget；本地 mock |
| [CVE-2026-90817](CVE-2026-90817) | Vanderbilt REDCap | 3.1 9.8（公开声称，未核验） | 发现者脚本 / 占位框架 / 批量检测 |

点进 CVE 目录看完整判定和引用。评分必须带 CVSS 版本和出处，没有就写 unknown。

## 怎么读

```text
CVE-<年>-<编号>/
  README.md     我的结论（中文）
  meta.yaml     机器可读事实
  sources/      引用的公开材料，各带 SOURCE.yaml
```

`sources/` 里的代码版权归原作者，许可证见 [NOTICE](NOTICE) 和各 `SOURCE.yaml`。本仓库自己的说明文字为 MIT，见 [LICENSE](LICENSE)。

收录规范：[docs/ingest-spec.md](docs/ingest-spec.md)。问题请向厂商报告产品漏洞；本仓库的元数据问题开 GitHub issue。
