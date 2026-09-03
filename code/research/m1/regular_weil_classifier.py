#!/usr/bin/env python3
"""Exact exponent/divisor classifier for the regular M1 Weil step.

For a primitive annihilator character omega of order m and d != 0,
we rewrite the restricted rational character sum as the complete polynomial
sum omega(P_{r,s,d}(y)). A Q_d(y)^m domain-mask factor is inserted so that
all inadmissible points contribute zero without changing admissible values.

This script proves only the finite exponent classification used to check the
hypotheses of the standard multiplicative-character Weil bound. It does not
prove that external theorem or the assembled M1 energy estimate.
"""
from __future__ import annotations

import json
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent

CATEGORIES = ("generic", "d=1", "d=-1")


def root_multiplicities_mod_m(m: int, r: int, s: int, category: str) -> dict[str, int]:
    if m <= 1:
        raise ValueError("m must exceed 1 for a nontrivial character")
    r %= m
    s %= m
    nr = (-r) % m
    ns = (-s) % m

    # Q_d^m forces every excluded root to remain a zero of the polynomial,
    # but contributes 0 modulo m to root multiplicities. Thus only these
    # residues matter for the m-th-power obstruction.
    if category == "generic":
        return {"-d": r, "0": nr, "1-d": s, "1": ns}
    if category == "d=1":
        # 0 and 1-d collide.
        return {"-1": r, "0": (nr + s) % m, "1": ns}
    if category == "d=-1":
        # -d and 1 collide.
        return {"0": nr, "1": (r + ns) % m, "2": s}
    raise ValueError(category)


def classify_m(m: int) -> dict:
    rows = []
    failures = []
    for category in CATEGORIES:
        expected_roots = 4 if category == "generic" else 3
        max_weil_constant = expected_roots - 1
        nontrivial_pairs = 0
        for r in range(m):
            for s in range(m):
                if r == 0 and s == 0:
                    continue
                nontrivial_pairs += 1
                residues = root_multiplicities_mod_m(m, r, s, category)
                not_mth_power = any(v % m != 0 for v in residues.values())
                if not not_mth_power:
                    failures.append({"category": category, "r": r, "s": s, "residues": residues})
        rows.append(
            {
                "category": category,
                "distinct_domain_roots": expected_roots,
                "weil_constant_e_minus_1": max_weil_constant,
                "nontrivial_twist_pairs_checked": nontrivial_pairs,
            }
        )
    return {
        "m": m,
        "all_nontrivial_pairs_not_mth_power": not failures,
        "failures": failures,
        "categories": rows,
    }


def compile_cpp(build_dir: Path) -> Path:
    exe = build_dir / "m1_regular_weil_classifier"
    subprocess.run(
        [
            "g++", "-std=c++17", "-O2", "-Wall", "-Wextra", "-pedantic",
            str(HERE / "regular_weil_classifier.cpp"), "-o", str(exe),
        ],
        check=True,
    )
    return exe


def run_cpp(exe: Path, ms: list[int]) -> dict:
    proc = subprocess.run(
        [str(exe), *map(str, ms)], check=True, text=True, capture_output=True
    )
    return json.loads(proc.stdout)


def main() -> None:
    ms = [4, 18, 20, 210]
    py = [classify_m(m) for m in ms]
    with tempfile.TemporaryDirectory(prefix="wow-m1-weil-") as td:
        cpp = run_cpp(compile_cpp(Path(td)), ms)

    python_summary = {
        str(row["m"]): row["all_nontrivial_pairs_not_mth_power"] for row in py
    }
    cpp_summary = cpp["all_nontrivial_pairs_not_mth_power"]
    result = {
        "status": "EXACT_EXPONENT_CLASSIFICATION_EXTERNAL_WEIL_THEOREM_REQUIRED",
        "mathematical_reduction": {
            "character_order": "m=(N-1)/K; omega is chosen primitive of order m",
            "domain_mask": "Q_d(y)^m with Q_d=y(y-1)(y+d)(y+d-1)",
            "generic_distinct_roots": 4,
            "generic_weil_constant": 3,
            "d_pm_1_distinct_roots": 3,
            "d_pm_1_weil_constant": 2,
            "consequence_if_standard_weil_theorem_applies": "|A_{r,s}(d)| <= 3 sqrt(N) for every d != 0 and nontrivial (r,s)",
        },
        "python": py,
        "cpp17": cpp,
        "dual_implementation_pass": python_summary == cpp_summary and all(python_summary.values()),
        "not_claimed": [
            "proof of the external Weil theorem",
            "assembled cross-twist M1 bound",
            "general BGS theorem",
        ],
    }
    out = HERE.parents[2] / "results" / "research" / "m1" / "regular_weil_classifier.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"dual_implementation_pass": result["dual_implementation_pass"]}, indent=2))
    if not result["dual_implementation_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
