#!/usr/bin/env python3
"""Repository-wide structural, syntax, provenance, and data-integrity gates."""
from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    "README.md", "RESEARCH_INDEX.md", "STATUS.md", "ROADMAP.md", "THEORY.md",
    "HISTORY.md", "HANDBOOK.md", "research/theory.md", "research/ledger.md",
    "research/problems/m1_fluctuation_energy.md",
    "research/engineering/language_migration.md", "references/bibliography.md",
    "code/README.md", "code/core", "code/diagnostics", "code/kloosterman",
    "code/large_m", "code/shape_automaton", "code/sp4", "code/theorems",
    "data/MANIFEST.md", "data/diagnostics", "data/moments", "data/proof",
    "data/rank2_sp4", "data/spectral", "docs/README.md",
    "docs/THEORY_FULL_PRE_REBUILD.md", "docs/HISTORY_FULL_PRE_REBUILD.md",
    "docs/literature", "docs/review", "inputs/r82-legacy",
    "src/python/bgs/finite_field.py", "src/python/bgs/jacobi.py",
    "src/python/bgs/key_geometry.py", "src/python/bgs/twisted_jacobi.py",
    "src/cpp/number_theory/catmap_order.cpp",
    "src/cpp/shape/relation_automaton.cpp",
    "src/cpp/verification/fourth_moment_factorization.cpp",
    "experiments/m1/cross_term_energy.py",
    "experiments/verification/sol6_relation_count.py",
    "experiments/verification/verify_fourth_moment_factorization.py",
    "experiments/verification/verify_second_moment_reduction.py",
    "experiments/verification/verify_twisted_jacobi_moments.py",
    "experiments/verification/verify_twisted_jacobi_scalar_formula.py",
    "results/README.md", "formal/Bgs/K2Reduction.lean", "formal/Bgs/K4Variety.lean",
    "formal/Bgs/M1DegenerateFiber.lean", "formal/Bgs/OpLocal.lean",
    "formal/Bgs/ScaleLaw.lean", "formal/Bgs/TorusLevelSets.lean",
    "paper/main.tex", "paper/main.pdf", "archive/README.md",
    "archive/legacy-workspace/README.md",
]

FORBIDDEN_PATHS = [
    "formal/.lake/build", "formal/.lake/packages", "data/tools", "tools/tectonic.exe",
    "paper/M4D_PROOF.tex", "paper/BGS_COMPLETE.tex", "paper/BGS_PROOF.tex",
]

PYTHON_ROOTS = ("code", "src", "experiments", "tools")


def is_immutable_legacy(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    parts = rel.parts
    return len(parts) >= 2 and parts[0] == "archive" and parts[1] == "legacy-workspace"


def finish(label: str, errors: list[str], summary: str) -> None:
    if errors:
        for error in errors:
            print(f"FAIL [{label}] {error}")
        raise SystemExit(1)
    print(f"PASS [{label}] {summary}")


def check_structure() -> None:
    errors: list[str] = []
    for relative_path in REQUIRED_PATHS:
        if not (ROOT / relative_path).exists():
            errors.append(f"missing required path: {relative_path}")
    for relative_path in FORBIDDEN_PATHS:
        if (ROOT / relative_path).exists():
            errors.append(f"forbidden generated/superseded path present: {relative_path}")

    julia_outside_archive = [
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*.jl")
        if not is_immutable_legacy(path)
    ]
    for path in julia_outside_archive:
        errors.append(f"Julia source outside immutable legacy snapshot: {path}")

    paper_root = ROOT / "paper"
    active_tex = sorted(path.relative_to(ROOT).as_posix() for path in paper_root.rglob("*.tex"))
    if active_tex != ["paper/main.tex"]:
        errors.append(f"active paper TeX set must be exactly ['paper/main.tex'], got {active_tex}")

    finish(
        "structure",
        errors,
        "broad corpus and current layer present; Julia confined to immutable provenance; one active TeX manuscript",
    )


def check_python() -> None:
    errors: list[str] = []
    count = 0
    for root_name in PYTHON_ROOTS:
        directory = ROOT / root_name
        if not directory.exists():
            continue
        for path in directory.rglob("*.py"):
            count += 1
            try:
                ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            except Exception as exc:
                errors.append(f"Python syntax error in {path.relative_to(ROOT)}: {exc}")
    finish("python", errors, f"{count} active/research Python files parse")


def check_json() -> None:
    errors: list[str] = []
    count = 0
    for directory in (ROOT / "results", ROOT / "data"):
        if not directory.exists():
            continue
        for path in directory.rglob("*.json"):
            count += 1
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except Exception as exc:
                errors.append(f"JSON parse error in {path.relative_to(ROOT)}: {exc}")
    finish("json", errors, f"{count} data/result JSON files parse")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        choices=("all", "structure", "python", "json"),
        default="all",
        help="run one independently visible CI gate or the complete set",
    )
    args = parser.parse_args()

    if args.check in ("all", "structure"):
        check_structure()
    if args.check in ("all", "python"):
        check_python()
    if args.check in ("all", "json"):
        check_json()


if __name__ == "__main__":
    main()
