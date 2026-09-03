#!/usr/bin/env python3
"""Fast structural, Python-syntax, and JSON-integrity check for the active tree."""
from __future__ import annotations

import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    "README.md",
    "STATUS.md",
    "ROADMAP.md",
    "research/theory.md",
    "research/ledger.md",
    "research/problems/m1_fluctuation_energy.md",
    "references/bibliography.md",
    "src/python/bgs/jacobi.py",
    "src/python/bgs/twisted_jacobi.py",
    "experiments/verification/verify_twisted_jacobi_moments.py",
    "experiments/verification/verify_second_moment_reduction.py",
    "experiments/verification/verify_twisted_jacobi_scalar_formula.py",
    "experiments/verification/verify_fourth_moment_factorization.py",
    "experiments/m1/cross_term_energy.py",
    "src/cpp/m1/cross_term_energy.cpp",
    "src/cpp/verification/fourth_moment_factorization.cpp",
    "results/README.md",
    "archive/README.md",
    "archive/legacy-workspace/README.md",
]

# These names belong to the old workspace and must not reappear at the active root.
FORBIDDEN_ACTIVE_PATHS = [
    "code",
    "data",
    "docs",
    "inputs",
    "HANDBOOK.md",
    "HISTORY.md",
    "THEORY.md",
]


def main() -> None:
    errors: list[str] = []

    for relative_path in REQUIRED_PATHS:
        if not (ROOT / relative_path).exists():
            errors.append(f"missing required path: {relative_path}")

    for relative_path in FORBIDDEN_ACTIVE_PATHS:
        if (ROOT / relative_path).exists():
            errors.append(f"old active surface still present: {relative_path}")

    for path in ROOT.rglob("*.py"):
        if "archive" in path.parts:
            continue
        try:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except Exception as exc:
            errors.append(f"Python syntax error in {path.relative_to(ROOT)}: {exc}")

    results_root = ROOT / "results"
    if results_root.exists():
        for path in results_root.rglob("*.json"):
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except Exception as exc:
                errors.append(f"JSON parse error in {path.relative_to(ROOT)}: {exc}")

    if errors:
        for error in errors:
            print(f"FAIL {error}")
        raise SystemExit(1)

    print("PASS active structure, Python syntax, and result JSON integrity")


if __name__ == "__main__":
    main()
