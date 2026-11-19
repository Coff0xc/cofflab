# cve-poc

Coff0xc 维护的 CVE 漏洞与公开 PoC 策展库。上游代码嵌在 `sources/`，目录、评分、日期、成色以本仓库的 `meta.yaml` 为准。

收录机器人只读拉取、按规范改造、**不执行** PoC。规范：[docs/ingest-spec.md](docs/ingest-spec.md)。上一批抓取出错：[docs/source-issues.md](docs/source-issues.md)。收完跑 `python tools/check_layout.py`。

## 布局

```text
CVE-<年>-<编号>/
  README.md          # 本仓库策展（中文）
  meta.yaml          # 机器可读事实
  sources/<作者>-<简称>/
    SOURCE.yaml      # 上游 url、commit、许可证、issues
    ...              # 上游快照
```

单源也放进 `sources/`。CVE 根目录只允许上面三个名字。模板：[`_template/CVE-YYYY-NNNNN/`](_template/CVE-YYYY-NNNNN/)。

## 收录

| CVE | 产品 | 评分 | 公开成色 | 来源 |
| --- | --- | --- | --- | --- |
| [CVE-2026-114938](CVE-2026-114938) | OpenJDK Base64（Java4Shell） | 4.0 9.2 (Calif)；3.1 8.1 (Oracle)；3.1 9.8 (Red Hat) | 触发 / 崩溃 / 泄露 / 实验；无公开通用 RCE | 5 源，见该目录 |
| [CVE-2026-118383](CVE-2026-118383) | MongoDB Server 复制 | unknown | 实验室 UAF 崩溃，未证实代码执行 | googlesky |
| [CVE-2026-123007](CVE-2026-123007) | F5 NGINX HTTP/2 | 4.0 9.2 (F5)；3.1 8.1 (F5) | 触发 + 仅新鲜 Docker 的 RCE 演示 | sfewer-r7 |
| [CVE-2026-123488](CVE-2026-123488) | Craft CMS 元素搜索 | 3.1 9.8 (GHSA)；4.0 9.3 (GitHub) | 未认证 SQLi 写库 / 提权 | fixedbyreboot |

## 规则

- 只收已经公开的 PoC/exp。来源不限于 GitHub。
- 收录前只读检查，不执行。检查结果写在 `SOURCE.yaml.review`。
- 假 PoC 藏木马是常见套路；只在有权测试的隔离环境里由人运行。
- 第三方代码版权归原作者，见 [NOTICE](NOTICE) 与各 `SOURCE.yaml`。

## 免责

仅供授权安全研究与防御使用。
