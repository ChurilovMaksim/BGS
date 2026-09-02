"""Fast non-mutating health gate for the canonical WoW repository."""
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]

REQUIRED = [
    "README.md",
    "STATUS.md",
    "THEORY.md",
    "HISTORY.md",
    "HANDBOOK.md",
    "requirements.txt",
    "research/README.md",
    "research/M1.md",
    "code/math/twisted_jacobi.py",
    "code/math/jacobi.py",
    "code/verification/baseline_r82.py",
    "code/verification/h3_k2_exact_reduction.py",
    "code/verification/theorem_ii_new_primes.py",
    "results/verified/baseline_r82.json",
    "results/verified/h3_k2_exact_reduction.json",
    "results/verified/theorem_ii_new_primes.json",
    "inputs/r82-legacy/theorems/I_torus_rigidity/q_curve_N199.npz",
    "inputs/r82-legacy/theorems/I_torus_rigidity/q_curve_N3571.npz",
    "inputs/r82-legacy/theorems/II_twisted_jacobi/closed_form.json",
    "formal/Bgs/K2Reduction.lean",
    "paper/README.md",
    "archive/README.md",
    "archive/legacy-workspace/README.md",
]

FORBIDDEN_ACTIVE = [
    "code/verification/word_trace_algebra.py",
    "results/verified/word_trace_proof.json",
    "formal/.lake/build",
    "formal/.lake/packages",
    "tools/tectonic.exe",
    "paper/M4D_PROOF.tex",
    "paper/final/mobius_fiber_theorem.tex",
]

STALE_TOKENS = ("src/", "artifacts/", '"src"', '"artifacts"')
RESULT_JSON_DIRS = [ROOT / "results" / "verified", ROOT / "results" / "numerical"]


def fail(message: str, errors: list[str]) -> None:
    print(f"FAIL: {message}")
    errors.append(message)


def main() -> int:
    errors: list[str] = []

    for rel in REQUIRED:
        if not (ROOT / rel).exists():
            fail(f"missing required path: {rel}", errors)
    if not errors:
        print("required paths: PASS")

    hygiene_before = len(errors)
    for rel in FORBIDDEN_ACTIVE:
        if (ROOT / rel).exists():
            fail(f"forbidden active path exists: {rel}", errors)
    for cache in ROOT.joinpath("code").rglob("__pycache__"):
        fail(f"generated Python cache exists: {cache.relative_to(ROOT)}", errors)
    if len(errors) == hygiene_before:
        print("active-tree hygiene: PASS")

    syntax_before = len(errors)
    for path in sorted((ROOT / "code").rglob("*.py")):
        text = path.read_text(encoding="utf-8-sig")
        rel = path.relative_to(ROOT)
        if not str(rel).startswith("code/maintenance/"):
            for token in STALE_TOKENS:
                if token in text:
                    fail(f"stale path token {token!r} in {rel}", errors)
        try:
            compile(text, str(path), "exec")
        except SyntaxError as exc:
            fail(f"syntax error in {rel}: {exc}", errors)
    if len(errors) == syntax_before:
        print("active Python syntax/path conventions: PASS")

    json_before = len(errors)
    for directory in RESULT_JSON_DIRS:
        if not directory.exists():
            continue
        for path in sorted(directory.glob("*.json")):
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except Exception as exc:
                fail(f"invalid result JSON {path.relative_to(ROOT)}: {exc}", errors)
    if len(errors) == json_before:
        print("current result JSON: PASS")

    if errors:
        print(f"REPOSITORY HEALTH: FAIL ({len(errors)} issue(s))")
        return 1
    print("REPOSITORY HEALTH: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
