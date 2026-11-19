# 收录机器人

权威规范：[ingest-spec.md](ingest-spec.md)。上一批错：[source-issues.md](source-issues.md)。

## Muse（云电脑，主机器人）

Goal / 定时：见 [muse-task.md](muse-task.md)。规范只认本仓库 [ingest-spec.md](ingest-spec.md)。

Linux 云电脑 clone `Coff0xc/cve-poc`，按规范拉取。禁止执行 PoC。`python tools/check_layout.py` 通过后自动 `git push --ff-only origin main`。失败不准提交。本仓库不放 `.agents/`、`.grok/`。

## 手写

1. 读规范。
2. 按 `_template/CVE-YYYY-NNNNN/` 落盘。
3. 跑 `python tools/check_layout.py`，失败不准提交。
