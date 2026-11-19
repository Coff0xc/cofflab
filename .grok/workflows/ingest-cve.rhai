let meta = #{
    name: "ingest-cve",
    description: "Ingest a public CVE PoC into this curator repo: pin commit, nest under sources/, write meta, run check_layout. Never execute PoCs.",
    when_to_use: "Adding or refreshing a public PoC in Coff0xc/cve-poc. Use when Muse or Grok should pull a GitHub/Exploit-DB source into the house layout.",
    phases: [
        #{ title: "Plan", detail: "require cve, collected date, sources" },
        #{ title: "Fetch", detail: "advisory lookup plus one snapshot agent per source" },
        #{ title: "Curate", detail: "house README, meta.yaml, SOURCE.yaml, index" },
        #{ title: "Verify", detail: "skeptic then check_layout.py" },
    ],
};

let advisory_schema = #{
    "type": "object",
    "required": ["product", "cvss", "notes"],
    "properties": #{
        "product": #{ "type": "string" },
        "vendor": #{ "type": "string" },
        "affected": #{ "type": "string" },
        "fixed": #{ "type": "string" },
        "notes": #{ "type": "string" },
        "cvss": #{
            "type": "array",
            "maxItems": 6,
            "items": #{
                "type": "object",
                "required": ["version", "score", "source"],
                "properties": #{
                    "version": #{ "type": "string" },
                    "score": #{ "type": "number" },
                    "source": #{ "type": "string" },
                    "vector": #{ "type": "string" },
                },
            },
        },
    },
};

let snap_schema = #{
    "type": "object",
    "required": ["id", "commit", "ok", "issues"],
    "properties": #{
        "id": #{ "type": "string" },
        "commit": #{ "type": "string" },
        "ok": #{ "type": "boolean" },
        "license": #{ "type": "string" },
        "issues": #{ "type": "array", "items": #{ "type": "string" } },
        "dropped": #{ "type": "array", "items": #{ "type": "string" } },
    },
};

let curate_schema = #{
    "type": "object",
    "required": ["ok", "cve_dir", "summary"],
    "properties": #{
        "ok": #{ "type": "boolean" },
        "cve_dir": #{ "type": "string" },
        "summary": #{ "type": "string" },
        "public_rce": #{ "type": "boolean" },
    },
};

let verdict_schema = #{
    "type": "object",
    "required": ["ok", "reason"],
    "properties": #{
        "ok": #{ "type": "boolean" },
        "reason": #{ "type": "string" },
        "fixes": #{ "type": "array", "items": #{ "type": "string" } },
    },
};

let check_schema = #{
    "type": "object",
    "required": ["ok", "log"],
    "properties": #{
        "ok": #{ "type": "boolean" },
        "log": #{ "type": "string" },
    },
};

fn rules_block() {
    let s = "";
    s += "Repo: Coff0xc/cve-poc (this workspace). This is a curator library, not a mirror of other people's repos.\n";
    s += "Read with read_file before writing: docs/ingest-spec.md, docs/source-issues.md, _template/CVE-YYYY-NNNNN/.\n";
    s += "HARD RULES: never execute PoCs, exploit.py, poc.py, run.sh, docker compose, scanners, or any program from a cloned source. git clone and file copy only.\n";
    s += "Never put an upstream README at the CVE root. CVE root may only contain README.md, meta.yaml, sources/.\n";
    s += "Never invent CVSS, dates, or impact. Missing facts stay unknown. public_rce defaults false.\n";
    s += "Drop CLAUDE.md, AGENTS.md, GEMINI.md, nested .git, __pycache__, node_modules.\n";
    s
}

fn looks_like_cve(s) {
    if type_of(s) != "string" { return false; }
    if s.len() < 13 { return false; }
    s.sub_string(0, 4) == "CVE-"
}

let cve = if args == () { () } else { args.cve };
let collected = if args == () { () } else { args.collected };
let raw_sources = if args == () { () } else { args.sources };
if !looks_like_cve(cve) {
    complete(#{ summary: "Pass args.cve as CVE-YYYY-N.", check_ok: false });
}
if type_of(collected) != "string" || collected.len() < 10 {
    complete(#{ summary: "Pass args.collected as UTC YYYY-MM-DD (workflows have no clock).", check_ok: false });
}
if type_of(raw_sources) != "array" || raw_sources.len() == 0 {
    complete(#{ summary: "Pass args.sources as a non-empty array of {url, id}.", check_ok: false });
}

let sources = [];
for item in raw_sources {
    if item != () && type_of(item) == "map" {
        if type_of(item.url) == "string" && type_of(item.id) == "string" {
            if sources.len() < 5 {
                sources.push(item);
            } else {
                log("dropped extra source beyond 5: " + item.id);
            }
        }
    }
}
if sources.len() == 0 {
    complete(#{ summary: "No usable sources after filtering. Each item needs string url and id.", check_ok: false });
}

phase("Plan");
log("ingest " + cve + " sources=" + sources.len().to_string());

phase("Fetch");
let adv_prompt = rules_block();
adv_prompt += "CVE id: " + json_encode(cve) + "\n";
adv_prompt += "Look up vendor advisory, NVD, and GHSA with web/GitHub tools. Do not use a PoC README as the only score source.\n";
adv_prompt += "Return product, vendor, affected, fixed, cvss array (each with version, score, source; vector if known), and notes for conflicts.\n";
adv_prompt += "If a score has no version or source, omit that entry. Empty cvss is valid after you searched.\n";

let fetch_jobs = [];
fetch_jobs.push(#{
    prompt: adv_prompt,
    label: "advisory:" + cve,
    capability_mode: "read-only",
    output_schema: advisory_schema,
});

for src in sources {
    let dest = cve + "/sources/" + src.id;
    let sp = rules_block();
    sp += "Snapshot source id=" + json_encode(src.id) + " url=" + json_encode(src.url) + " into " + json_encode(dest) + "/\n";
    sp += "Steps: (1) git clone --depth 1 the url into a temp dir. (2) git rev-parse HEAD and keep the 40-char sha. (3) Copy the tree into " + json_encode(dest) + "/ excluding .git and the drop list. (4) Do not overwrite an existing house README.md or meta.yaml at the CVE root. (5) Do not write SOURCE.yaml yet.\n";
    sp += "If files vanish after copy (AV), keep the git blob, record an issue, do not pretend the upstream lacked them.\n";
    sp += "Return ok, id, commit (40-char or n/a), license (SPDX or unknown), issues[], dropped[].\n";
    fetch_jobs.push(#{
        prompt: sp,
        label: "snap:" + src.id,
        capability_mode: "execute",
        output_schema: snap_schema,
    });
}

let fetch_results = parallel(fetch_jobs);
let advisory = ();
if fetch_results.len() > 0 {
    let ar = fetch_results[0];
    if ar != () && ar.success { advisory = ar.output; }
}

let snaps = [];
let idx = 0;
for fr in fetch_results {
    if idx > 0 {
        if fr != () && fr.success && fr.output != () && fr.output.ok != false {
            snaps.push(fr.output);
        } else {
            log("snapshot failed slot " + idx.to_string());
        }
    }
    idx += 1;
}
if snaps.len() == 0 {
    complete(#{ summary: "All snapshots failed. Nothing curated.", cve: cve, check_ok: false });
}

phase("Curate");
let curate_prompt = rules_block();
curate_prompt += "CVE=" + json_encode(cve) + " collected=" + json_encode(collected) + "\n";
curate_prompt += "Advisory JSON: " + json_encode(advisory) + "\n";
curate_prompt += "Successful snapshots JSON: " + json_encode(snaps) + "\n";
curate_prompt += "Write " + json_encode(cve) + "/meta.yaml, " + json_encode(cve) + "/README.md (Chinese curator, no exploit steps), each sources/<id>/SOURCE.yaml, update root README.md index row (score column MUST include CVSS version and source, never a bare number), and NOTICE for licenses.\n";
curate_prompt += "If the CVE dir already existed, append sources and do not overwrite prior curator conclusions unless the new evidence contradicts them; record that in meta.yaml notes.\n";
curate_prompt += "demonstrated only from the ingest-spec enum. public_rce=false unless the source itself claims success on a non-lab target AND does not limit itself to fresh Docker/local.\n";
curate_prompt += "review.executed must be false. Return ok, cve_dir, summary, public_rce.\n";

let cur = agent(curate_prompt, #{
    label: "curate:" + cve,
    capability_mode: "read-write",
    output_schema: curate_schema,
});
if cur == () || !cur.success || cur.output == () {
    complete(#{ summary: "Curator agent failed.", cve: cve, check_ok: false });
}
if cur.output.ok == false {
    complete(#{ summary: "Curator agent returned ok=false.", cve: cve, check_ok: false });
}

phase("Verify");
let sk_prompt = rules_block();
sk_prompt += "Adversarially review the curator files for " + json_encode(cve) + ". Use read_file/grep on " + cve + "/README.md, " + cve + "/meta.yaml, sources/*/SOURCE.yaml, and the repo root README.md.\n";
sk_prompt += "Set ok=true only if: CVE root has only README.md meta.yaml sources/; scores have version+source; public_rce is false unless you independently read a source README that claims non-lab RCE without Docker/fresh-heap caveats; no exploit steps in the house README; SOURCE.yaml has commit and license.\n";
sk_prompt += "Default ok=false if evidence is missing. Return reason and optional fixes[].\n";

let sk = agent(sk_prompt, #{
    label: "skeptic:" + cve,
    capability_mode: "read-only",
    output_schema: verdict_schema,
});

if sk != () && sk.success && sk.output != () && sk.output.ok != true {
    let rp = rules_block();
    rp += "Repair curator files for " + json_encode(cve) + " using these skeptic fixes: " + json_encode(sk.output) + "\n";
    rp += "Do not execute PoCs. Keep public_rce false unless the skeptic found hard evidence.\n";
    let repair = agent(rp, #{
        label: "repair:" + cve,
        capability_mode: "read-write",
        output_schema: curate_schema,
    });
    if repair == () || !repair.success {
        log("repair agent failed; continuing to layout check");
    }
}

let chk_prompt = "";
chk_prompt += "Run: python tools/check_layout.py\n";
chk_prompt += "Do not run any other program. Do not execute files under CVE-*/sources/.\n";
chk_prompt += "Return ok=true only if the command exits 0. Put the full stdout/stderr in log.\n";
let chk = agent(chk_prompt, #{
    label: "check-layout",
    capability_mode: "execute",
    output_schema: check_schema,
});

let check_ok = false;
let check_log = "checker did not run";
if chk != () && chk.success && chk.output != () {
    check_ok = chk.output.ok == true;
    if chk.output.log != () { check_log = chk.output.log; }
}

let report = "";
report += "# ingest-cve " + cve + "\n\n";
report += "- collected: " + collected + "\n";
report += "- snapshots_ok: " + snaps.len().to_string() + "\n";
report += "- check_ok: " + check_ok.to_string() + "\n";
report += "- check_log:\n\n```\n" + check_log + "\n```\n";
report += "\nNot pushed. Commit yourself after reading the diff: one commit per CVE/source.\n";
let report_path = write_scratch_file("ingest-report.md", report);

complete(#{
    summary: cve + " ingest check_ok=" + check_ok.to_string(),
    cve: cve,
    check_ok: check_ok,
    sources: snaps.len(),
    path: report_path,
});
