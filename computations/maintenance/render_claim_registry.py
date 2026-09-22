#!/usr/bin/env python3
"""Render the human-readable BGS claim registry from record/claims.json."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "record" / "claims.json"
TARGET = ROOT / "record" / "claim_registry.md"

def esc(value: object) -> str:
    return str(value).replace("|", r"\|").replace("\n", " ")

def render() -> str:
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    rows = sorted(data["claims"], key=lambda row: row["id"])
    out = [
        "# Stable claim registry",
        "",
        "This file is generated from `record/claims.json`. It is a navigation",
        "surface, not an independent status authority; `claim_ledger.md` wins.",
        "",
        data["registry_scope"],
        "",
        "| Claim ID | State | Title | Authoritative source | Boundary / closure |",
        "|---|---|---|---|---|",
    ]
    for row in rows:
        source = row["source"]
        detail = row.get("closure_condition") if row["state"] == "open" else row.get("boundary", "")
        out.append(
            f"| `{esc(row['id'])}` | **{esc(row['state']).upper()}** | "
            f"{esc(row['title'])} | [source](../{source}) | {esc(detail)} |"
        )
    out.extend([
        "",
        "External theorem dependencies are pinned in",
        "`../literature/external_dependencies.json`; the maintained programme DAG is",
        "in `scientific_dependencies.json` and `scientific_dependency_graph.md`.",
        "",
    ])
    return "\n".join(out)

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = render()
    if args.check:
        if not TARGET.is_file() or TARGET.read_text(encoding="utf-8") != expected:
            raise SystemExit("claim registry is stale; run render_claim_registry.py")
        print("claim-registry-render: OK")
        return 0
    TARGET.write_text(expected, encoding="utf-8")
    print(TARGET.relative_to(ROOT))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
