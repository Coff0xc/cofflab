# Reproduction archive (repro/)

This directory archives reproduction evidence for entries whose repro status is **Full**. Only Full entries are archived here; entries with any other repro status (Pending, Partial, No target) have no directory here.

Repro status is recorded in `catalog.json` (field `repro`) and in the local `repro-status.json` tool file; this directory holds the evidence behind the Full verdicts. The PoC / exploit code itself is NOT archived here — it lives in each entry's `sources/` directory. What is archived here is the reproduction report and the sandbox run logs (the commands that were run and their output), i.e. the evidence that the reproduction was actually performed.

## Entries

| Entry | What was reproduced | Evidence |
|---|---|---|
| [CVE-2026-123218](../CVE-2026-123218/) | Detector fully verified (version-check; 29 unit tests pass; VULNERABLE / PATCHED boundary versions correct). The authorization bypass itself has no public exploit code and was not reproduced. | [report](CVE-2026-123218/CVE-2026-123218.md), [run log](CVE-2026-123218/runs/foxcornlab-faspex-scanner/run.log) |
| [CVE-2026-19868](../CVE-2026-19868/) | Detector fully verified (version-check; 25 unit tests pass; 4 boundary versions correct). The SAML bypass itself was not tested. | [report](CVE-2026-19868/CVE-2026-19868.md), [run log](CVE-2026-19868/runs/foxcornlab-sonicos-scanner/run.log) |
| [CVE-2026-126170](../CVE-2026-126170/) | Full lab reproduction (model lab, not a real Fortinet device): vulnerable model 7.6.7 injects and executes; fixed model 7.6.8 is safe; mitigations hold. | [report](CVE-2026-126170/CVE-2026-126170.md), [vuln run](CVE-2026-126170/runs/googlesky-poc/vuln/run.log), [fixed run](CVE-2026-126170/runs/googlesky-poc/fixed/run.log) |
| [CVE-2026-105437](../CVE-2026-105437/) | Full lab reproduction (crash): `git merge-tree --write-tree` segfaults (SIGSEGV, rc=139) on git 2.43.0 with the malicious attributes; benign attributes merge normally. | [report](CVE-2026-105437/CVE-2026-105437.md), [run log](CVE-2026-105437/runs/googlesky-poc/run.log) |

## Notes

- All four reproductions were performed on 2026-11-19 (UTC) in an isolated sandbox (`run-in-sandbox.sh`), read-only with respect to the host; nothing here was installed or imported on the host.
- The reports were written in Simplified Chinese and converted to Traditional Chinese on archival (2026-11-26) with OpenCC; the wording is unchanged. Their internal `~/workspace/poc-repro/...` paths refer to the pre-archive location.
- These are evidence logs of past sandbox runs, not code to execute. Do not run anything from this directory outside an isolated sandbox.
- Adding a new entry here: the entry must first be repro Full (see `repro-status.json`); archive its report and run logs under `repro/<ID>/` and add one row to the table above.
