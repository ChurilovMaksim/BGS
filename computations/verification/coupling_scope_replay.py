#!/usr/bin/env python3
"""Replay the maintained finite checks accompanying the coupling-scope notes."""

from pathlib import Path
import subprocess
import sys


CHECKS = (
    "check_finite_pell_range.py",
    "check_oldspace_phase_rank.py",
    "check_day115_pell_cubic.py",
    "check_day117_pell_fejer.py",
    "crt_splitting_check.py",
    "axial_fourier_range_check.py",
    "check_day117_pell_fejer_hs.py",
)


def main():
    checker_dir = Path(__file__).resolve().with_name("coupling_scope_audit")
    python = [sys.executable] + (["-" + "O" * sys.flags.optimize] if sys.flags.optimize else [])
    for name in CHECKS:
        print(f"== {name} ==", flush=True)
        subprocess.run([*python, str(checker_dir / name)], check=True)
    print(f"Passed {len(CHECKS)} finite checks. No asymptotic claim is certified.")


if __name__ == "__main__":
    main()
