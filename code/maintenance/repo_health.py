"""Fast non-mutating health gate for the canonical WoW research repository.

The gate distinguishes two layers:
  * canonical code/results: strict current-path and status requirements;
  * restored research corpus: preservation + syntax/JSON integrity requirements.
"""
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]

CANONICAL_REQUIRED = [
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
]

RESEARCH_CORPUS_REQUIRED = [
    "code/core",
    "code/diagnostics",
    "code/kloosterman",
    "code/large_m",
    "code/shape_automaton",
    "code/sp4",
    "code/theorems",
    "code/utils",
    "code/legacy_verification",
    "data/MANIFEST.md",
    "data/diagnostics",
    "data/legacy",
    "data/moments",
    "data/proof",
    "data/rank2_sp4",
    "data/spectral",
    "docs/README.md",
    "docs/literature",
    "docs/review",
    "docs/archive",
    "docs/THEORY_FULL_PRE_REBUILD.md",
    "docs/HISTORY_FULL_PRE_REBUILD.md",
    "paper/README.md",
    "paper/sections",
    "paper/patches",
    "paper/final",
    "archive/legacy-workspace/README.md",
]

FORBIDDEN_GENERATED = [
    "formal/.lake/build",
    "formal/.lake/packages",
    "tools/tectonic.exe",
    "data/tools",
]

FORBIDDEN_CANONICAL = [
    "code/verification/word_trace_algebra.py",
    "results/verified/word_trace_proof.json",
    "paper/M4D_PROOF.tex",
]

STALE_TOKENS = ("src/", "artifacts/", '"src"', '"artifacts"')
CANONICAL_CODE_DIRS = [
    ROOT / "code" / "math",
    ROOT / "code" / "verification",
    ROOT / "code" / "experiments",
    ROOT / "code" / "maintenance",
]
JSON_ROOTS = [ROOT / "results", ROOT / "data"]


def fail(message: str, errors: list[str]) -> None:
    print(f"FAIL: {message}")
    errors.append(message)


def main() -> int:
    errors: list[str] = []

    required_before = len(errors)
    for rel in CANONICAL_REQUIRED:
        if not (ROOT / rel).exists():
            fail(f"missing canonical path: {rel}", errors)
    for rel in RESEARCH_CORPUS_REQUIRED:
        if not (ROOT / rel).exists():
            fail(f"missing research-corpus path: {rel}", errors)
    if len(errors) == required_before:
        print("canonical + research corpus presence: PASS")

    hygiene_before = len(errors)
    for rel in FORBIDDEN_GENERATED + FORBIDDEN_CANONICAL:
        if (ROOT / rel).exists():
            fail(f"forbidden path exists: {rel}", errors)
    for cache in ROOT.joinpath("code").rglob("__pycache__"):
        fail(f"generated Python cache exists: {cache.relative_to(ROOT)}", errors)
    if len(errors) == hygiene_before:
        print("generated/quarantine hygiene: PASS")

    syntax_before = len(errors)
    python_files = sorted((ROOT / "code").rglob("*.py"))
    for path in python_files:
        try:
            text = path.read_text(encoding="utf-8-sig")
            compile(text, str(path), "exec")
        except Exception as exc:
            fail(f"Python source failure in {path.relative_to(ROOT)}: {exc}", errors)
    if len(errors) == syntax_before:
        print(f"Python syntax corpus: PASS ({len(python_files)} files)")

    path_before = len(errors)
    for directory in CANONICAL_CODE_DIRS:
        if not directory.exists():
            continue
        for path in sorted(directory.rglob("*.py")):
            text = path.read_text(encoding="utf-8-sig")
            rel = path.relative_to(ROOT)
            for token in STALE_TOKENS:
                if token in text:
                    fail(f"stale current-path token {token!r} in canonical {rel}", errors)
    if len(errors) == path_before:
        print("canonical path conventions: PASS")

    json_before = len(errors)
    json_count = 0
    for directory in JSON_ROOTS:
        if not directory.exists():
            continue
        for path in sorted(directory.rglob("*.json")):
            json_count += 1
            try:
                json.loads(path.read_text(encoding="utf-8-sig"))
            except Exception as exc:
                fail(f"invalid JSON {path.relative_to(ROOT)}: {exc}", errors)
    if len(errors) == json_before:
        print(f"JSON corpus: PASS ({json_count} files)")

    if errors:
        print(f"REPOSITORY HEALTH: FAIL ({len(errors)} issue(s))")
        return 1
    print("REPOSITORY HEALTH: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())