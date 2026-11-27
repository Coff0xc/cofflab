# cofflab — methods

A curated library of public CVE proof-of-concept records. Every entry is a
directory named after its CVE or GHSA identifier, holding a `meta.yaml`,
a `README.md`, and one `sources/` subdirectory per source. This note
describes how entries get in, how they are verified, and what the
dataset does not claim. It is the methods note for the dataset; the
enforceable ingestion rules live in the local `ingest-spec.md`, and the
machine-readable field definitions live in `dataset/SCHEMA.md`.

## Scale (snapshot 2026-11-27)

747 entries. 103 in CISA KEV. 47 flagged as exploited in the wild.
670 with EPSS scores. 4 with a fully reproduced exploit (`repro: Full`).
Categories: web 263, network & security 249, runtime / framework /
browser 108, OS / system / DevOps 75, AI / LLM 30, database 22.
The library grows hourly; the numbers above are a snapshot, not a
promise. `catalog.json` always carries the current counts.

## Where entries come from

Sources, in the order they are preferred: vendor advisory, GHSA
advisory, ZDI advisory, VulnCheck, VulDB, NVD record, researcher
article. PoC repositories (GitHub, Exploit-DB, Packet Storm) are used
when their code can be read and verified. The hunt priority is:
CISA KEV entries with a public PoC first, then confirmed in-the-wild
exploitation with a public PoC, then CVSS 9.0 and above with a public
PoC, then other recent high-severity vulnerabilities.

Confirmed in-the-wild exploitation is ingestible with no CVSS floor
and no public PoC: the entry then cites the vendor advisory,
researcher article, or threat-intelligence report, and its `meta.yaml`
states that no public exploit PoC exists yet.

## Verification

No PoC code is executed during ingestion. Verification is read-only:
the PoC is fetched and read, checked against the NVD / CVE record
(description, affected versions, CWE, CVSS), and rejected when it is
an empty skeleton, a placeholder, a pure mirror, a duplicate, or a
claim mismatch (a PoC that tests a different flaw than the CVE
describes). Each source is pinned to its exact 40-character commit in
`SOURCE.yaml`; non-git sources carry a `content_sha256` instead.
One commit per source. No force-push.

When a PoC is verified real but its clone is blocked by the
execution-risk check, the entry is ingested from an advisory source
instead and the PoC code is not taken. This is the auto-switch rule;
entries ingested this way say so in their notes.

Reproduction is a separate step, done only in an isolated environment.
`review.executed` records whether a PoC was actually executed, and
`repro` records the outcome (`Full`, `Partial`, `No target`,
`Pending`). Full-reproduction material lives in `repro/`.

## What the dataset does not claim

- A PoC being in the library does not mean it was executed here.
  Most entries are verified by reading only. `verified` in
  `catalog.json` is derived: it is true when a PoC was executed
  (`review.executed`) or the reproduction is `Full`.
- CVSS scores come from several authorities (CNA, NVD, CISA-ADP) and
  can disagree for one CVE. Every score in `meta.yaml` carries its
  version, value, and source; the catalog table shows them all.
- EPSS scores lag for the newest CVEs: entries the FIRST model has
  not scored yet have no EPSS value.
- Source concentration: a large share of the PoC sources point at a
  single upstream PoC monorepo. Every such source carries a
  `content_sha256` seal and a local mirror exists for byte-level
  verification, but the concentration itself is a limitation, not a
  feature.
- In-the-wild flags come from the curated exploitation-reports file,
  not from `meta.yaml` notes. An entry is flagged only when a report
  names it; absence of a flag is absence of a report, not proof of
  no exploitation.

## Files

- `README.md` (English, primary) and `README.zh-TW.md` (Traditional
  Chinese): the catalog tables, one per category, five columns
  (ID, Product, Score, Affected, Fixed).
- `categories/`: one page per category, same five columns.
- `catalog.json`: the machine-readable catalog (five table columns
  plus repro, review_executed, kev, in_the_wild, verified, tags,
  epss).
- `dataset/cofflab.jsonl` and `dataset/cofflab.csv`: one row per
  entry, same records as `catalog.json`, for direct loading.
- `dataset/SCHEMA.md`: the field dictionary for the machine-readable
  files.
- `repro/`: reproduction material for the `Full` entries.
- `CITATION.cff`: citation metadata. Releases are versioned by date
  (for example `2026.11.27`); a Zenodo DOI is issued per release
  once the GitHub–Zenodo integration is enabled.

## Contributing

The library is curated by its maintainer. External submissions are
not currently accepted; the contribution templates are an open policy
question. See `SECURITY.md` for reporting a bad entry (a backdoored
source, a wrong PoC, a claim mismatch): report it, do not fix it
silently, and do not ingest from the reported source.
