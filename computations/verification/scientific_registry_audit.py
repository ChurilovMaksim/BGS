#!/usr/bin/env python3
"""Fail-closed consistency audit for BGS scientific metadata.

This validates repository governance and cross-layer references. It does not
prove mathematical claims and must never be reported as such.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CLAIMS = ROOT / "record" / "claims.json"
DEPS = ROOT / "record" / "scientific_dependencies.json"
EXTERNAL = ROOT / "literature" / "external_dependencies.json"
GENERATED = ROOT / "record" / "generated_sources.json"
EVIDENCE = ROOT / "evidence" / "index.json"
ENVIRONMENT = ROOT / "environment" / "runtime-manifest.json"
PAPERS = ROOT / "papers"
TOPICS = ROOT / "record" / "mathematics_topics.json"

ERRATA_RE = re.compile(r"^ERR-[0-9]{3}$")
CLAIM_RE = re.compile(r"^BGS-[A-Z]+-[0-9]{3}$")
EXTERNAL_RE = re.compile(r"^EXT-[A-Z0-9]+-[A-Z0-9-]+$")
ALLOWED_STATES = {"proved", "conditional", "open", "verification-pending"}

def fail(message: str) -> None:
    raise SystemExit("scientific-registry-audit: " + message)

def load(path: Path) -> dict:
    if not path.is_file():
        fail(f"missing required JSON: {path.relative_to(ROOT)}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"invalid JSON {path.relative_to(ROOT)}: {exc}")

def require_path(rel: str, *, allow_build: bool = False) -> None:
    if allow_build and rel.startswith("build/"):
        return
    path = ROOT / rel
    if not path.exists():
        fail(f"registered path does not exist: {rel}")

def audit_claims() -> tuple[dict[str, dict], set[str]]:
    data = load(CLAIMS)
    if not data.get("registry_scope"):
        fail("record/claims.json is missing registry_scope")
    rows = data.get("claims")
    if not isinstance(rows, list) or not rows:
        fail("record/claims.json has no claims")
    by_id: dict[str, dict] = {}
    for row in rows:
        cid = row.get("id")
        if not isinstance(cid, str) or not CLAIM_RE.fullmatch(cid):
            fail(f"invalid claim id: {cid!r}")
        if cid in by_id:
            fail(f"duplicate claim id: {cid}")
        by_id[cid] = row
        if row.get("state") not in ALLOWED_STATES:
            fail(f"{cid}: invalid state {row.get('state')!r}")
        if not row.get("ledger_status"):
            fail(f"{cid}: missing ledger_status")
        if "EXTERNAL" in row["ledger_status"] and not row.get("external_dependencies"):
            fail(f"{cid}: external-theorem status lacks external_dependencies")
        source = row.get("source")
        if not isinstance(source, str):
            fail(f"{cid}: missing source")
        require_path(source)
        source_text = (ROOT / source).read_text(encoding="utf-8", errors="replace")
        if cid not in source_text:
            fail(f"{cid}: stable claim id is not anchored in source {source}")
        for field in ("evidence", "verifiers", "formalization", "manuscript"):
            values = row.get(field, [])
            if not isinstance(values, list):
                fail(f"{cid}: {field} must be a list")
            for rel in values:
                require_path(rel)
        if row["state"] == "open" and not row.get("closure_condition"):
            fail(f"{cid}: open claim lacks closure_condition")
        if not row.get("boundary"):
            fail(f"{cid}: missing boundary")
    if by_id.get("BGS-BGS-001", {}).get("state") != "open":
        fail("BGS-BGS-001 must remain OPEN unless the claim ledger is deliberately revised")
    return by_id, set(by_id)

def audit_external(claims: dict[str, dict]) -> set[str]:
    data = load(EXTERNAL)
    rows = data.get("dependencies")
    if not isinstance(rows, list):
        fail("external dependency registry is malformed")
    ids: set[str] = set()
    for row in rows:
        eid = row.get("id")
        if not isinstance(eid, str) or not EXTERNAL_RE.fullmatch(eid):
            fail(f"invalid external dependency id: {eid!r}")
        if eid in ids:
            fail(f"duplicate external dependency id: {eid}")
        ids.add(eid)
        for key in ("title", "identifier", "pinned_version", "locator", "checked_on", "mapping"):
            if not row.get(key):
                fail(f"{eid}: missing {key}")
        for rel in row.get("project_sources", []):
            require_path(rel)
    for cid, row in claims.items():
        for eid in row.get("external_dependencies", []):
            if eid not in ids:
                fail(f"{cid}: unknown external dependency {eid}")
    return ids

def audit_graph(claims: dict[str, dict]) -> None:
    ids = set(claims)
    expected: set[tuple[str, str, str]] = set()
    graph: dict[str, list[str]] = {cid: [] for cid in ids}
    for cid, row in claims.items():
        for dep in row.get("dependencies", []):
            if dep not in ids:
                fail(f"{cid}: unknown claim dependency {dep}")
            if dep == cid:
                fail(f"{cid}: self dependency")
            expected.add((dep, cid, "scientific-prerequisite"))
            graph[dep].append(cid)

    data = load(DEPS)
    actual = {
        (edge.get("from"), edge.get("to"), edge.get("type"))
        for edge in data.get("edges", [])
    }
    if actual != expected:
        fail("scientific_dependencies.json edges do not match record/claims.json")

    visiting: set[str] = set()
    visited: set[str] = set()
    def dfs(node: str) -> None:
        if node in visiting:
            fail(f"cycle in scientific dependency graph at {node}")
        if node in visited:
            return
        visiting.add(node)
        for nxt in graph[node]:
            dfs(nxt)
        visiting.remove(node)
        visited.add(node)
    for node in sorted(ids):
        dfs(node)

def audit_papers(claims_by_id: dict[str, dict], claim_ids: set[str], external_ids: set[str]) -> None:
    if not PAPERS.is_dir():
        fail("papers/ is missing")
    manifests = sorted(PAPERS.glob("*/paper.json"))
    if len(manifests) < 4:
        fail("expected at least four focused publication manifests")
    for path in manifests:
        data = load(path)
        if data.get("status") != "candidate-scope":
            fail(f"{path.relative_to(ROOT)}: unexpected status")
        for cid in data.get("claims", []):
            if cid not in claim_ids:
                fail(f"{path.relative_to(ROOT)}: unknown claim {cid}")
            if claims_by_id[cid]["state"] == "open":
                fail(f"{path.relative_to(ROOT)}: OPEN claim {cid} cannot be listed as an included result")
        for cid in data.get("excluded_open_claims", []):
            if cid not in claim_ids:
                fail(f"{path.relative_to(ROOT)}: unknown excluded claim {cid}")
        for eid in data.get("external_dependencies", []):
            if eid not in external_ids:
                fail(f"{path.relative_to(ROOT)}: unknown external dependency {eid}")
        for rel in data.get("authoritative_sources", []):
            require_path(rel)
        if not (path.parent / "README.md").is_file():
            fail(f"{path.parent.relative_to(ROOT)}: missing README.md")
        if not (path.parent / "OUTLINE.md").is_file():
            fail(f"{path.parent.relative_to(ROOT)}: missing OUTLINE.md")

def audit_python_pins() -> None:
    req = ROOT / "requirements.txt"
    require_path("requirements.txt")
    lines = [
        line.strip() for line in req.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]
    bad = [line for line in lines if not re.fullmatch(r"[A-Za-z0-9_.-]+==[^<>=!~; ]+", line)]
    if bad:
        fail("requirements.txt contains non-exact runtime pin(s): " + ", ".join(bad))
    python_version = (ROOT / ".python-version").read_text(encoding="utf-8").strip()
    env = load(ENVIRONMENT)
    if python_version != str(env["python"]["ci"]):
        fail(".python-version and runtime-manifest Python version disagree")

def audit_generated_and_environment() -> None:
    data = load(GENERATED)
    for rule in data.get("rules", []):
        require_path(rule["producer"])
        for rel in rule.get("generated", []):
            require_path(rel, allow_build=True)
        for rel in rule.get("authoritative_sources", []):
            require_path(rel)

    env = load(ENVIRONMENT)
    require_path(env["python"]["requirements"])
    require_path(env["lean"]["toolchain_file"])
    require_path(env["lean"]["manifest"])
    require_path(env["manuscript"]["builder"])

    evidence = load(EVIDENCE)
    for item in evidence.get("classes", {}).values():
        prefix = item.get("canonical_prefix") or item.get("future_prefix")
        if prefix:
            require_path(prefix.rstrip("/"))

def audit_errata() -> None:
    data=load(ROOT / "record" / "errata.json")
    rows=data.get("entries")
    if not isinstance(rows,list) or not rows:
        fail("record/errata.json has no entries")
    ids=set()
    for row in rows:
        eid=row.get("id")
        if not isinstance(eid,str) or not ERRATA_RE.fullmatch(eid):
            fail(f"invalid erratum id: {eid!r}")
        if eid in ids:
            fail(f"duplicate erratum id: {eid}")
        ids.add(eid)
        for key in ("title","disposition","downstream","authority"):
            if not row.get(key):
                fail(f"{eid}: missing {key}")
        require_path(row["authority"])

def audit_topics() -> None:
    data = load(TOPICS)
    topics = data.get("topics")
    if not isinstance(topics, dict) or not topics:
        fail("mathematics topic map is missing")
    registered: set[str] = set()
    for name, paths in topics.items():
        if not isinstance(paths, list) or not paths:
            fail(f"mathematics topic {name!r} is empty")
        topic_readme = ROOT / "mathematics" / "topics" / name / "README.md"
        if not topic_readme.is_file():
            fail(f"missing topic README: {topic_readme.relative_to(ROOT)}")
        for rel in paths:
            require_path(rel)
            registered.add(rel)
    maintained = {
        str(path.relative_to(ROOT))
        for path in (ROOT / "mathematics").glob("*.md")
        if path.name not in {"README.md", "results.md", "results_20260907_addendum.md", "open_questions.md"}
    }
    if registered != maintained:
        missing = sorted(maintained - registered)
        stale = sorted(registered - maintained)
        fail(f"mathematics topic map mismatch; missing={missing}, stale={stale}")

def audit_governance_surface() -> None:
    required = [
        "CITATION.cff", "CONTRIBUTING.md", "REVIEWING.md", "SOURCE_OF_TRUTH.md",
        "ROADMAP.md", "RELEASES.md", "CHANGELOG.md", "ERRATA.md",
        "LICENSE_POLICY.md", ".zenodo.json", ".github/CODEOWNERS",
        ".github/pull_request_template.md", ".github/main-branch-policy.json",
        "record/branch_protection_policy.md", "record/scientific_dependency_graph.md",
        "record/history/2026/INDEX.md", "evidence/executions/README.md",
        "environment/README.md", "papers/README.md", "mathematics/topics/README.md",
        "record/claim_registry.md", "computations/maintenance/render_claim_registry.py",
        "record/errata.json", "computations/maintenance/render_errata.py",
        ".github/ISSUE_TEMPLATE/proof-obligation.yml",
        ".github/ISSUE_TEMPLATE/correction.yml",
        ".github/ISSUE_TEMPLATE/config.yml",
    ]
    for rel in required:
        require_path(rel)

def main() -> int:
    claims, claim_ids = audit_claims()
    external_ids = audit_external(claims)
    audit_graph(claims)
    audit_papers(claims, claim_ids, external_ids)
    audit_python_pins()
    audit_generated_and_environment()
    audit_errata()
    audit_topics()
    audit_governance_surface()
    print(
        f"scientific-registry-audit: OK "
        f"({len(claim_ids)} claims, {len(external_ids)} external dependencies)"
    )
    return 0

if __name__ == "__main__":
    sys.exit(main())
