# 收录机器人

权威规范：[ingest-spec.md](ingest-spec.md)。上一批错：[source-issues.md](source-issues.md)。

## Muse（云电脑，主机器人）

技能：`.agents/skills/cve-ingest/SKILL.md`（Muse Code 读仓库里这份）。

Goal / 定时怎么贴：见 [muse-task.md](muse-task.md)。

Linux 云电脑 clone `Coff0xc/cve-poc`，按技能拉取。禁止执行 PoC。`python tools/check_layout.py` 通过后自动 `git push --ff-only origin main`。失败不准提交。

## Grok Build（本机策展）

工作流：`.grok/workflows/ingest-cve.js`（daemon）和 `ingest-cve.rhai`（shell）。授信本仓库目录后 `/ingest-cve`。

```text
{"cve":"CVE-YYYY-N","collected":"YYYY-MM-DD","sources":[{"url":"https://github.com/org/repo","id":"author-slug"}]}
```

最多 5 个源。不 push。看完 diff 再自己提交。

## 手写

1. 读规范。
2. 按 `_template/CVE-YYYY-NNNNN/` 落盘。
3. 跑 `python tools/check_layout.py`，失败不准提交。
