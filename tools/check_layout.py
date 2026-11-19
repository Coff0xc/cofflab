#!/usr/bin/env python3
"""Validate CVE directory layout against docs/ingest-spec.md. Stdlib only."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CVE_DIR_RE = re.compile(r"^CVE-\d{4}-\d+$")
ALLOWED_ROOT = {"README.md", "meta.yaml", "sources"}
REQUIRED_META_KEYS = (
    "id:",
    "product:",
    "cvss:",
    "demonstrated:",
    "public_rce:",
    "collected:",
    "sources:",
)
REQUIRED_SOURCE_KEYS = (
    "id:",
    "upstream:",
    "commit:",
    "collected:",
    "license:",
    "review:",
    "issues:",
)
DROP_NAMES = {
    "CLAUDE.md",
    "AGENTS.md",
    "GEMINI.md",
}
DEMONSTRATED = {
    "version-check",
    "trigger",
    "crash",
    "leak",
    "lab-repro",
    "rce-local",
    "sqli-read",
    "sqli-write",
    "priv-esc",
    "dos",
}


def fail(errors: list[str], path: Path, msg: str) -> None:
    errors.append(f"{path.as_posix()}: {msg}")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_cve(cve_dir: Path, errors: list[str]) -> None:
    names = {p.name for p in cve_dir.iterdir()}
    extra = names - ALLOWED_ROOT
    if extra:
        fail(errors, cve_dir, f"root extra files/dirs {sorted(extra)}")
    for required in ALLOWED_ROOT:
        if required not in names:
            fail(errors, cve_dir, f"missing {required}")
            return

    meta = cve_dir / "meta.yaml"
    text = read_text(meta)
    for key in REQUIRED_META_KEYS:
        if key not in text:
            fail(errors, meta, f"missing key {key}")
    if "id:" in text:
        first = next(
            (line.split(":", 1)[1].strip() for line in text.splitlines() if line.startswith("id:")),
            "",
        )
        if first != cve_dir.name:
            fail(errors, meta, f"id {first!r} != directory {cve_dir.name}")

    demonstrated_line = next(
        (line for line in text.splitlines() if line.startswith("demonstrated:")),
        "",
    )
    for token in re.findall(r"[A-Za-z0-9\-]+", demonstrated_line.split(":", 1)[-1]):
        if token not in DEMONSTRATED and token not in {"[]"}:
            fail(errors, meta, f"illegal demonstrated value {token!r}")

    sources = cve_dir / "sources"
    children = [p for p in sources.iterdir() if p.is_dir()]
    if not children:
        fail(errors, sources, "no source directories")
    for src in children:
        source_yaml = src / "SOURCE.yaml"
        if not source_yaml.is_file():
            fail(errors, src, "missing SOURCE.yaml")
            continue
        stext = read_text(source_yaml)
        for key in REQUIRED_SOURCE_KEYS:
            if key not in stext:
                fail(errors, source_yaml, f"missing key {key}")
        if "executed: true" in stext.replace(" ", ""):
            fail(errors, source_yaml, "review.executed must stay false")

    for path in cve_dir.rglob("*"):
        if path.name in DROP_NAMES:
            fail(errors, path, "file is on the drop list")
        if path.name == "README.md" and path.parent == cve_dir:
            body = read_text(path)
            if "http://exploit/" in body:
                fail(errors, path, "curator README copied a broken upstream link")


def main() -> int:
    errors: list[str] = []
    cve_dirs = sorted(p for p in ROOT.iterdir() if p.is_dir() and CVE_DIR_RE.match(p.name))
    if not cve_dirs:
        errors.append("no CVE-* directories")
    for cve_dir in cve_dirs:
        check_cve(cve_dir, errors)

    root_readme = ROOT / "README.md"
    if root_readme.is_file():
        body = read_readme_scores(root_readme)
        for line in body:
            errors.append(line)
    else:
        errors.append("missing root README.md")

    if errors:
        print("FAIL")
        for item in errors:
            print(f"  {item}")
        return 1
    print(f"OK {len(cve_dirs)} CVE directories")
    return 0


def read_readme_scores(path: Path) -> list[str]:
    issues: list[str] = []
    for line in read_text(path).splitlines():
        if "CVE-" not in line or not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3 or "CVE-" not in cells[0]:
            continue
        score = cells[2]
        if re.fullmatch(r"\d+(\.\d+)?", score):
            issues.append(
                f"{path.as_posix()}: index score {score!r} has no CVSS version/source"
            )
    return issues


if __name__ == "__main__":
    sys.exit(main())
