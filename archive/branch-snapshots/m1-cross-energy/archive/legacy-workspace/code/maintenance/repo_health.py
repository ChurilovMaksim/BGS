"""Fast repository health check for the post-R82 BGS workspace.

This checker validates repository structure rather than scientific claims. It is
safe to run before and after edits and never mutates the workspace.
"""
from __future__ import annotations

import compileall
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

REQUIRED = [
    "README.md",
    "HANDBOOK.md",
    "THEORY.md",
    "HISTORY.md",
    "data/MANIFEST.md",
    "code/core/catmap_core.py",
    "code/theorems/theorem_ii_twisted_jacobi.py",
    "code/large_m/fourth_mixed_moment.py",
    "code/verification/baseline_r82.py",
    "formal/Bgs/K2Reduction.lean",
    "formal/Bgs/K4Variety.lean",
]

FORBIDDEN_GENERATED = [
    "formal/.lake/build",
    "formal/.lake/packages",
]


def check_required() -> list[str]:
    return [p for p in REQUIRED if not (ROOT / p).exists()]


def check_generated() -> list[str]:
    return [p for p in FORBIDDEN_GENERATED if (ROOT / p).exists()]


def check_python_compile() -> bool:
    ok_code = compileall.compile_dir(ROOT / "code", quiet=1, force=True)
    ok_patches = compileall.compile_dir(ROOT / "paper" / "patches", quiet=1, force=True)
    return bool(ok_code and ok_patches)


def main() -> int:
    problems: list[str] = []

    missing = check_required()
    if missing:
        problems.extend(f"missing required path: {p}" for p in missing)

    generated = check_generated()
    if generated:
        problems.extend(
            f"generated build tree should not be tracked/preserved: {p}"
            for p in generated
        )

    python_ok = check_python_compile()
    if not python_ok:
        problems.append("Python compileall failed")

    print(f"root: {ROOT}")
    print(f"required paths: {'PASS' if not missing else 'FAIL'}")
    print(f"generated-tree hygiene: {'PASS' if not generated else 'FAIL'}")
    print(f"python compileall: {'PASS' if python_ok else 'FAIL'}")

    if problems:
        print("\nPROBLEMS")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print("\nREPOSITORY HEALTH: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
