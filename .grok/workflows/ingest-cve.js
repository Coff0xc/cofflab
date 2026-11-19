/**
 * ---
 * name: ingest-cve
 * description: Ingest a public CVE PoC into this curator repo: pin commit, nest under sources/, write meta, run check_layout. Never execute PoCs.
 * when_to_use: Adding or refreshing a public PoC in Coff0xc/cve-poc. Use when Muse or Grok should pull a GitHub/Exploit-DB source into the house layout.
 * phase: Plan -- require cve, collected date, sources
 * phase: Fetch -- advisory lookup plus one snapshot agent per source
 * phase: Curate -- house README, meta.yaml, SOURCE.yaml, index
 * phase: Verify -- skeptic then check_layout.py
 * ---
 */

const RULES =
  "Repo: Coff0xc/cve-poc (this workspace). This is a curator library, not a mirror of other people's repos.\n" +
  "Read with read_file before writing: docs/ingest-spec.md, docs/source-issues.md, _template/CVE-YYYY-NNNNN/.\n" +
  "HARD RULES: never execute PoCs, exploit.py, poc.py, run.sh, docker compose, scanners, or any program from a cloned source. git clone and file copy only.\n" +
  "Never put an upstream README at the CVE root. CVE root may only contain README.md, meta.yaml, sources/.\n" +
  "Never invent CVSS, dates, or impact. Missing facts stay unknown. public_rce defaults false.\n" +
  "Drop CLAUDE.md, AGENTS.md, GEMINI.md, nested .git, __pycache__, node_modules.\n";

const advisorySchema = {
  type: "object",
  required: ["product", "cvss", "notes"],
  properties: {
    product: { type: "string" },
    vendor: { type: "string" },
    affected: { type: "string" },
    fixed: { type: "string" },
    notes: { type: "string" },
    cvss: {
      type: "array",
      maxItems: 6,
      items: {
        type: "object",
        required: ["version", "score", "source"],
        properties: {
          version: { type: "string" },
          score: { type: "number" },
          source: { type: "string" },
          vector: { type: "string" },
        },
      },
    },
  },
};

const snapSchema = {
  type: "object",
  required: ["id", "commit", "ok", "issues"],
  properties: {
    id: { type: "string" },
    commit: { type: "string" },
    ok: { type: "boolean" },
    license: { type: "string" },
    issues: { type: "array", items: { type: "string" } },
    dropped: { type: "array", items: { type: "string" } },
  },
};

const curateSchema = {
  type: "object",
  required: ["ok", "cve_dir", "summary"],
  properties: {
    ok: { type: "boolean" },
    cve_dir: { type: "string" },
    summary: { type: "string" },
    public_rce: { type: "boolean" },
  },
};

const verdictSchema = {
  type: "object",
  required: ["ok", "reason"],
  properties: {
    ok: { type: "boolean" },
    reason: { type: "string" },
    fixes: { type: "array", items: { type: "string" } },
  },
};

const checkSchema = {
  type: "object",
  required: ["ok", "log"],
  properties: {
    ok: { type: "boolean" },
    log: { type: "string" },
  },
};

function looksLikeCve(s) {
  return typeof s === "string" && s.length >= 13 && s.startsWith("CVE-");
}

export default async function ingestCve(args) {
  const cve = args?.cve;
  const collected = args?.collected;
  const raw = args?.sources;
  if (!looksLikeCve(cve)) {
    return { summary: "Pass args.cve as CVE-YYYY-N.", check_ok: false };
  }
  if (typeof collected !== "string" || collected.length < 10) {
    return { summary: "Pass args.collected as UTC YYYY-MM-DD (workflows have no clock).", check_ok: false };
  }
  if (!Array.isArray(raw) || raw.length === 0) {
    return { summary: "Pass args.sources as a non-empty array of {url, id}.", check_ok: false };
  }

  const sources = [];
  for (const item of raw) {
    if (item && typeof item.url === "string" && typeof item.id === "string") {
      if (sources.length < 5) {
        sources.push({ url: item.url, id: item.id });
      }
    }
  }
  if (sources.length === 0) {
    return { summary: "No usable sources after filtering. Each item needs string url and id.", check_ok: false };
  }

  const advPrompt =
    RULES +
    "CVE id: " +
    JSON.stringify(cve) +
    "\nLook up vendor advisory, NVD, and GHSA with web/GitHub tools. Do not use a PoC README as the only score source.\n" +
    "Return product, vendor, affected, fixed, cvss array (each with version, score, source; vector if known), and notes for conflicts.\n" +
    "If a score has no version or source, omit that entry. Empty cvss is valid after you searched.\n";

  const fetchPromises = [
    host
      .agent(advPrompt, {
        label: "Fetch/advisory",
        readonly: true,
        schema: advisorySchema,
      })
      .wait(),
  ];
  for (const src of sources) {
    const dest = cve + "/sources/" + src.id;
    const sp =
      RULES +
      "Snapshot source id=" +
      JSON.stringify(src.id) +
      " url=" +
      JSON.stringify(src.url) +
      " into " +
      JSON.stringify(dest) +
      "/\nSteps: (1) git clone --depth 1 the url into a temp dir. (2) git rev-parse HEAD and keep the 40-char sha. (3) Copy the tree into " +
      JSON.stringify(dest) +
      "/ excluding .git and the drop list. (4) Do not overwrite an existing house README.md or meta.yaml at the CVE root. (5) Do not write SOURCE.yaml yet.\n" +
      "If files vanish after copy (AV), keep the git blob, record an issue, do not pretend the upstream lacked them.\n" +
      "Return ok, id, commit (40-char or n/a), license (SPDX or unknown), issues[], dropped[].\n";
    fetchPromises.push(
      host
        .agent(sp, {
          label: "Fetch/snap-" + src.id,
          schema: snapSchema,
        })
        .wait(),
    );
  }

  const fetchResults = await Promise.all(fetchPromises);
  const advisory = fetchResults[0]?.status === "completed" ? fetchResults[0].structured : null;
  const snaps = [];
  for (let i = 1; i < fetchResults.length; i++) {
    const fr = fetchResults[i];
    const out = fr?.structured;
    if (fr?.status === "completed" && out && out.ok !== false) {
      snaps.push(out);
    }
  }
  if (snaps.length === 0) {
    return { summary: "All snapshots failed. Nothing curated.", cve, check_ok: false };
  }

  const curatePrompt =
    RULES +
    "CVE=" +
    JSON.stringify(cve) +
    " collected=" +
    JSON.stringify(collected) +
    "\nAdvisory JSON: " +
    JSON.stringify(advisory) +
    "\nSuccessful snapshots JSON: " +
    JSON.stringify(snaps) +
    "\nWrite " +
    JSON.stringify(cve) +
    "/meta.yaml, " +
    JSON.stringify(cve) +
    "/README.md (Chinese curator, no exploit steps), each sources/<id>/SOURCE.yaml, update root README.md index row (score column MUST include CVSS version and source, never a bare number), and NOTICE for licenses.\n" +
    "If the CVE dir already existed, append sources and do not overwrite prior curator conclusions unless the new evidence contradicts them; record that in meta.yaml notes.\n" +
    "demonstrated only from the ingest-spec enum. public_rce=false unless the source itself claims success on a non-lab target AND does not limit itself to fresh Docker/local.\n" +
    "review.executed must be false. Return ok, cve_dir, summary, public_rce.\n";

  const cur = await host
    .agent(curatePrompt, {
      label: "Curate/write",
      schema: curateSchema,
    })
    .wait();
  if (cur?.status !== "completed" || !cur.structured || cur.structured.ok === false) {
    return { summary: "Curator agent failed.", cve, check_ok: false };
  }

  const skPrompt =
    RULES +
    "Adversarially review the curator files for " +
    JSON.stringify(cve) +
    ". Use read_file/grep on " +
    JSON.stringify(cve + "/README.md") +
    ", " +
    JSON.stringify(cve + "/meta.yaml") +
    ", sources/*/SOURCE.yaml, and the repo root README.md.\n" +
    "Set ok=true only if: CVE root has only README.md meta.yaml sources/; scores have version+source; public_rce is false unless you independently read a source README that claims non-lab RCE without Docker/fresh-heap caveats; no exploit steps in the house README; SOURCE.yaml has commit and license.\n" +
    "Default ok=false if evidence is missing. Return reason and optional fixes[].\n";

  const sk = await host
    .agent(skPrompt, {
      label: "Verify/skeptic",
      readonly: true,
      schema: verdictSchema,
    })
    .wait();

  if (sk?.status === "completed" && sk.structured && sk.structured.ok !== true) {
    const rp =
      RULES +
      "Repair curator files for " +
      JSON.stringify(cve) +
      " using these skeptic fixes: " +
      JSON.stringify(sk.structured) +
      "\nDo not execute PoCs. Keep public_rce false unless the skeptic found hard evidence.\n";
    await host
      .agent(rp, {
        label: "Verify/repair",
        schema: curateSchema,
      })
      .wait();
  }

  const chk = await host
    .agent(
      "Run: python tools/check_layout.py\nDo not run any other program. Do not execute files under CVE-*/sources/.\nReturn ok=true only if the command exits 0. Put the full stdout/stderr in log.\n",
      {
        label: "Verify/check-layout",
        schema: checkSchema,
      },
    )
    .wait();

  const checkOk = chk?.status === "completed" && chk.structured?.ok === true;
  const checkLog = chk?.structured?.log ?? "checker did not run";

  return {
    summary: cve + " ingest check_ok=" + String(checkOk),
    cve,
    check_ok: checkOk,
    sources: snaps.length,
    check_log: checkLog,
  };
}
