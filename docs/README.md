# 收录机器人

1. 读 [ingest-spec.md](ingest-spec.md)（拉取 + 改造，必须遵守）。
2. 读 [source-issues.md](source-issues.md)（上一批抓到的上游问题和入库错误，不要再犯）。
3. 按 `_template/CVE-YYYY-NNNNN/` 落盘。
4. 跑 `python tools/check_layout.py`，失败不准提交。
