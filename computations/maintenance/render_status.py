#!/usr/bin/env python3
"""Render the programme status page and the generated registry family tables.

STATUS.md (repository root) is rendered in full from record/claims.json,
record/errata.json and record/claim_integration_epochs.json.
mathematics/results.md keeps its hand-written analytical text; only the
closing family tables between the GENERATED markers are rendered here,
from record/claims.json, and the hand-written prose is carried through
byte-for-byte.

Both surfaces are navigation, not status authorities: registered status
is controlled by record/claims.json (see SOURCE_OF_TRUTH.md), and the
dated narrative of status changes lives in record/claim_ledger.md.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CLAIMS = ROOT / "record" / "claims.json"
ERRATA = ROOT / "record" / "errata.json"
EPOCHS = ROOT / "record" / "claim_integration_epochs.json"
STATUS = ROOT / "STATUS.md"
RESULTS = ROOT / "mathematics" / "results.md"

STATES = ("proved", "verification-pending", "conditional", "open", "refuted")
BEGIN = "<!-- BEGIN GENERATED: registered family tables (render_status.py). Do not edit this section by hand. -->"
END = "<!-- END GENERATED: registered family tables (render_status.py) -->"

def esc(value: object) -> str:
    return str(value).replace("|", r"\|").replace("\n", " ")

def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))

def area_of(claim_id: str) -> str:
    return claim_id.split("-")[1]

def registry_rows() -> list[dict]:
    return sorted(load(CLAIMS)["claims"], key=lambda row: row["id"])

def render_status() -> str:
    claims_data = load(CLAIMS)
    rows = sorted(claims_data["claims"], key=lambda row: row["id"])
    by_state = Counter(row["state"] for row in rows)
    areas = sorted({area_of(row["id"]) for row in rows})
    by_area_state = {area: Counter() for area in areas}
    for row in rows:
        by_area_state[area_of(row["id"])][row["state"]] += 1
    open_rows = [row for row in rows if row["state"] == "open"]
    errata = load(ERRATA)
    epochs = load(EPOCHS)
    extension = epochs["external_dependency_extension"]
    out = [
        "# Programme status",
        "",
        "This file is generated from `record/claims.json`, `record/errata.json`",
        "and `record/claim_integration_epochs.json` by",
        "`computations/maintenance/render_status.py`. Do not edit it by hand.",
        "",
        "It is the single current-status page of the programme, and it is a",
        "navigation surface, not a status authority. Registered statuses are",
        "controlled by [`record/claims.json`](record/claims.json); see",
        "[`SOURCE_OF_TRUTH.md`](SOURCE_OF_TRUTH.md) for how disagreements",
        "between surfaces are resolved. The dated narrative of status changes",
        "and scope is [`record/claim_ledger.md`](record/claim_ledger.md).",
        "",
        "## Registered claims",
        "",
        f"Registry schema `{claims_data['schema']}`; registry updated",
        f"**{claims_data['updated']}**. **{len(rows)} registered claims.**",
        "",
        "| Registered state | Claims |",
        "|---|---:|",
    ]
    for state in STATES:
        out.append(f"| {state} | {by_state.get(state, 0)} |")
    out.append(f"| **Total** | **{len(rows)}** |")
    out += [
        "",
        "“Proved” reports the project registry at its stated scope, not",
        "external refereeing. The complete per-claim surface is the generated",
        "[`record/claim_registry.md`](record/claim_registry.md).",
        "",
        "## Claims by family and state",
        "",
        "| Family | " + " | ".join(STATES) + " | Total |",
        "|---|" + "---:|" * (len(STATES) + 1),
    ]
    for area in areas:
        counts = by_area_state[area]
        cells = " | ".join(str(counts.get(state, 0)) for state in STATES)
        out.append(f"| {area} | {cells} | {sum(counts.values())} |")
    totals = " | ".join(str(by_state.get(state, 0)) for state in STATES)
    out.append(f"| **Total** | {totals} | **{len(rows)}** |")
    out += [
        "",
        "## Open programme obligations",
        "",
        f"{len(open_rows)} registered claims are open. Their closure",
        "conditions are registered per claim in `record/claims.json` and",
        "rendered in full in the [claim registry](record/claim_registry.md).",
        "",
        "| Claim | Title | Authoritative source |",
        "|---|---|---|",
    ]
    for row in open_rows:
        out.append(
            f"| `{row['id']}` | {esc(row['title'])} | "
            f"[{row['source']}]({row['source']}) |"
        )
    out += [
        "",
        "## Corrections",
        "",
        f"Errata registry schema `{errata['schema']}`; updated",
        f"**{errata['updated']}**; **{len(errata['entries'])} registered entries**.",
        "The status authority for corrections is",
        f"`{errata['status_authority']}`; the generated reader-facing index",
        "is [`ERRATA.md`](ERRATA.md).",
        "",
        "## Registry integration record",
        "",
        f"Epoch record schema `{epochs['schema']}`, base epoch",
        f"`{epochs['base_epoch']}`, reviewed **{epochs['reviewed_on']}**.",
        f"It records {len(epochs['after_wave3'])} follow-on claims adopted after",
        f"wave 3 and {len(epochs['historical_claim_amendments'])} historical claim",
        "amendments admitted through the epoch amendment channel, and an",
        f"external-dependency extension of {len(extension['added_ids'])} external IDs.",
        "",
        "## Reading the status surfaces",
        "",
        "- [Source of truth](SOURCE_OF_TRUTH.md) — the authority order for",
        "  resolving disagreements between surfaces.",
        "- [Claim ledger](record/claim_ledger.md) — dated narrative of",
        "  status changes and evidentiary scope.",
        "- [Claim registry](record/claim_registry.md) — the complete",
        "  generated per-claim view of the registry.",
        "- [Theorem families and their limits](mathematics/results.md) —",
        "  analytical index of the theorem families, with generated",
        "  registry family tables.",
        "- [Open questions](mathematics/open_questions.md) — the maintained",
        "  open-problem surface.",
        "- [Corpus atlas](docs/corpus_atlas.md) — generated navigation",
        "  over the whole corpus.",
        "",
    ]
    return "\n".join(out)

def render_results_block(rows: list[dict]) -> str:
    by_state = Counter(row["state"] for row in rows)
    areas = sorted({area_of(row["id"]) for row in rows})
    summary = ", ".join(f"{by_state.get(state, 0)} {state}" for state in STATES)
    out = [
        BEGIN,
        "",
        "## Registered theorem families (generated)",
        "",
        "This closing section is generated from `../record/claims.json`",
        "by `../computations/maintenance/render_status.py`; the analytical",
        "text above it is hand-written and preserved. Registered status is",
        "controlled by claims.json; the complete per-claim surface, with",
        "boundaries and closure conditions, is the generated",
        "[claim registry](../record/claim_registry.md).",
        "",
        f"**{len(rows)} registered claims: {summary}.**",
    ]
    for area in areas:
        area_rows = [row for row in rows if area_of(row["id"]) == area]
        noun = "claim" if len(area_rows) == 1 else "claims"
        out += [
            "",
            f"### {area} family ({len(area_rows)} {noun})",
            "",
            "| Claim | State | Title |",
            "|---|---|---|",
        ]
        for row in area_rows:
            out.append(
                f"| `{row['id']}` | **{row['state'].upper()}** | "
                f"{esc(row['title'])} |"
            )
    out += ["", END]
    return "\n".join(out) + "\n"

def render_results() -> str:
    if not RESULTS.is_file():
        raise SystemExit("mathematics/results.md is missing; refusing to render")
    current = RESULTS.read_text(encoding="utf-8")
    if current.count(BEGIN) > 1 or current.count(END) > 1:
        raise SystemExit("mathematics/results.md: duplicated GENERATED markers")
    if BEGIN in current:
        if END not in current or current.index(END) < current.index(BEGIN):
            raise SystemExit("mathematics/results.md: malformed GENERATED markers")
        prose = current[: current.index(BEGIN)]
    else:
        prose = current
    return prose.rstrip("\n") + "\n\n" + render_results_block(registry_rows())

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    targets = [(STATUS, render_status()), (RESULTS, render_results())]
    if args.check:
        stale = [
            str(path.relative_to(ROOT))
            for path, expected in targets
            if not path.is_file() or path.read_text(encoding="utf-8") != expected
        ]
        if stale:
            raise SystemExit(
                "status surfaces are stale; run render_status.py: "
                + ", ".join(stale)
            )
        print("status-render: OK")
        return 0
    for path, text in targets:
        path.write_text(text, encoding="utf-8")
        print(path.relative_to(ROOT))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
