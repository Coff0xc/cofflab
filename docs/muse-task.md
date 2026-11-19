# Muse 云电脑任务

这是 **Coff0xc 自己的 CVE 策展库**。机器人是 Muse，跑在它自己的 Linux 云电脑上。权威规范：[ingest-spec.md](ingest-spec.md)。技能文件：`.agents/skills/cve-ingest/SKILL.md`。

Grok 工作流 `.grok/workflows/ingest-cve.rhai` 只在本机 Grok Build 里编排，Muse 不跑它。

## 云电脑一次性准备

```bash
git clone https://github.com/Coff0xc/cve-poc.git
cd cve-poc
```

Muse Code 会读仓库里的 `.agents/skills/cve-ingest/SKILL.md`。消费端 Muse（App/网页）没有技能安装：把该文件全文贴进对话，说「以后收录 CVE 都按这个技能做」。

## Goal（贴进 Muse）

```
你维护 GitHub 仓库 Coff0xc/cve-poc（本机已 clone）。这是我的 CVE 策展库，不是别人 PoC 的镜子。

每次我给你一个 CVE ID 和源 URL，按仓库里 .agents/skills/cve-ingest/SKILL.md 和 docs/ingest-spec.md 收录：
- 只 git clone + 拷文件。禁止执行任何 PoC、exploit.py、poc.py、run.sh、docker compose、扫描器。
- 嵌进 CVE-YYYY-N/sources/<author>-<slug>/。CVE 根目录只放 README.md、meta.yaml、sources/。
- 钉 40 位 commit。CVSS 必须有 version + score + source，没有就 unknown。
- public_rce 默认 false。review.executed 必须 false。
- python tools/check_layout.py 退出码非 0 不准 commit。
- 一次 commit 一个源，git push --ff-only origin main。禁止 force-push。

缺 CVE ID 或 URL 时问我，不要自己满网猎 CVE。
收录日期用 UTC：date -u +%F。
```

## 定时（可选）

不要做「每天扫全网新 CVE」的 cron。没有我给的 ID+URL 就停。

可以做的定时：每 6 小时 `git pull --ff-only`，保持云电脑上的 clone 与 `main` 同步。

## 和 Grok 工作流怎么分工

| | Muse 云电脑 | Grok `/ingest-cve` |
| --- | --- | --- |
| 谁跑 | Muse（Linux 云电脑） | 本机 Grok Build 会话 |
| 输入 | 对话或 Goal 里的 CVE + URL | `{"cve","collected","sources":[{url,id}]}` |
| 提交 | check_layout 通过后 ff-only push | 不 push，人看 diff 再 commit |
| 规范 | `docs/ingest-spec.md` | 同一份 |
