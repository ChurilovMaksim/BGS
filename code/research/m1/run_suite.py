#!/usr/bin/env python3
"""Run the M1 cross-twist research suite with Python/C++ anchor checks."""
from __future__ import annotations

import argparse
import json
import math
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))

from cross_twist_energy import build_key_tensor, energy_summary  # noqa: E402

ANCHORS = [
    # N=53 is a historical subgroup calibration, not a trace-3 split prime.
    (53, 10, 13, "historical subgroup calibration"),
    (199, 63, 11, "trace-3 split design"),
    (461, 23, 23, "trace-3 split design / new anchor"),
]

SWEEP = [
    (11, 5, 5),
    (29, 7, 7),
    (89, 11, 22),
    (139, 65, 23),
    (199, 63, 11),
    (211, 34, 21),
    (281, 39, 28),
    (461, 23, 23),
    (541, 174, 45),
    (709, 172, 59),
    (859, 278, 39),
    (911, 69, 35),
    (919, 318, 51),
    (1009, 384, 63),
]


def lucas_trace3(k: int) -> int:
    """L_k = alpha^k + alpha^-k for alpha + alpha^-1 = 3."""
    if k == 0:
        return 2
    if k == 1:
        return 3
    a, b = 2, 3
    for _ in range(1, k):
        a, b = b, 3 * b - a
    return b


def trace3_order_certificate(N: int, a: int, K: int) -> dict:
    is_trace3_root = (a * a - 3 * a + 1) % N == 0
    if not is_trace3_root:
        return {"applicable": False}
    L = lucas_trace3(K)
    lam = (3.0 + math.sqrt(5.0)) / 2.0
    return {
        "applicable": True,
        "N_divides_LK_minus_2": (L - 2) % N == 0,
        "LK_minus_2_mod_N": (L - 2) % N,
        "logarithmic_lower_bound_logN_over_loglambda": math.log(N) / math.log(lam),
        "K": K,
    }


def compile_cpp(build_dir: Path) -> Path:
    exe = build_dir / "m1_cross_twist_energy"
    cmd = [
        "g++",
        "-std=c++17",
        "-O2",
        "-Wall",
        "-Wextra",
        "-pedantic",
        str(HERE / "cross_twist_energy.cpp"),
        "-o",
        str(exe),
    ]
    subprocess.run(cmd, check=True)
    return exe


def run_cpp(exe: Path, N: int, a: int, K: int) -> dict:
    proc = subprocess.run(
        [str(exe), str(N), str(a), str(K)],
        check=True,
        text=True,
        capture_output=True,
    )
    return json.loads(proc.stdout)


def compare_anchor(py: dict, cpp: dict) -> dict:
    checks = {
        "V4_count_exact": py["counts"]["V4_count"] == cpp["V4_count"],
        "full_energy_abs_diff": abs(py["full_twist_energy"]["energy"] - cpp["full_energy"]),
        "delta_abs_diff": abs(py["full_twist_energy"]["delta_vs_trivial"] - cpp["delta_vs_trivial"]),
        "cross_fraction_abs_diff": abs(
            py["full_twist_energy"]["cross_fraction_of_full"] - cpp["cross_fraction_of_full"]
        ),
        "regular_maxA_abs_diff": abs(
            py["singular_fiber"]["max_nontrivial_abs_A_regular_d_nonzero"]
            - cpp["max_nontrivial_abs_A_regular_d_nonzero"]
        ),
    }
    checks["passed"] = bool(
        checks["V4_count_exact"]
        and checks["full_energy_abs_diff"] < 1e-6
        and checks["delta_abs_diff"] < 1e-12
        and checks["cross_fraction_abs_diff"] < 1e-12
        and checks["regular_maxA_abs_diff"] < 1e-9
    )
    return checks


def slim_case(N: int, a: int, K: int) -> dict:
    W, meta = build_key_tensor(N, a, K)
    s = energy_summary(W, compute_gram=False)
    full = s["full_twist_energy"]
    sing = s["singular_fiber"]
    return {
        "N": N,
        "a": a,
        "K": K,
        "m": meta["m"],
        "delta_vs_trivial": full["delta_vs_trivial"],
        "K2_delta": K * K * full["delta_vs_trivial"],
        "cross_fraction_of_full": full["cross_fraction_of_full"],
        "regular_delta_vs_trivial": sing["regular_only_delta_vs_trivial"],
        "K2_regular_delta": K * K * sing["regular_only_delta_vs_trivial"],
        "regular_cross_fraction_of_full": sing["regular_only_cross_fraction_of_full"],
        "max_regular_A_over_sqrtN": sing["max_nontrivial_abs_A_regular_d_nonzero"] / math.sqrt(N),
        "regular_3sqrtN_falsifier_pass": sing["max_nontrivial_abs_A_regular_d_nonzero"] <= 3.0 * math.sqrt(N) + 1e-9,
        "HH_mass_identity_error": sing["regular_coset_mass_identity_max_integer_error"],
        "singular_regular_B_identity_error": sing["direct_singular_regular_decomposition_max_integer_error"],
        "trace3_order_certificate": trace3_order_certificate(N, a, K),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "results" / "research" / "m1" / "cross_twist_suite.json",
    )
    args = parser.parse_args()

    anchors = []
    with tempfile.TemporaryDirectory(prefix="wow-m1-") as td:
        exe = compile_cpp(Path(td))
        for N, a, K, label in ANCHORS:
            W, meta = build_key_tensor(N, a, K)
            py = {
                "meta": meta,
                **energy_summary(W, compute_gram=True),
            }
            cpp = run_cpp(exe, N, a, K)
            anchors.append(
                {
                    "label": label,
                    "N": N,
                    "a": a,
                    "K": K,
                    "m": meta["m"],
                    "V4_count": py["counts"]["V4_count"],
                    "B_l2_energy_exact_integer": py["counts"]["B_l2_energy_exact_integer"],
                    "delta_vs_trivial": py["full_twist_energy"]["delta_vs_trivial"],
                    "cross_fraction_of_full": py["full_twist_energy"]["cross_fraction_of_full"],
                    "python_projector_max_abs_error": py["projector_identity"]["max_abs_B_reconstruction_error"],
                    "cpp_projector_max_abs_error": cpp["projector_max_abs_error"],
                    "cross_gram": py["full_twist_energy"]["cross_gram"],
                    "A_tau_d0": py["singular_fiber"]["A_tau_d0_expected"],
                    "max_nontrivial_abs_A_regular_d_nonzero": py["singular_fiber"]["max_nontrivial_abs_A_regular_d_nonzero"],
                    "HH_regular_mass": py["singular_fiber"]["HH_regular_mass"],
                    "HH_regular_mass_expected": py["singular_fiber"]["HH_regular_mass_expected"],
                    "regular_delta_vs_trivial": py["singular_fiber"]["regular_only_delta_vs_trivial"],
                    "regular_cross_fraction_of_full": py["singular_fiber"]["regular_only_cross_fraction_of_full"],
                    "dual_implementation_comparison": compare_anchor(py, cpp),
                    "trace3_order_certificate": trace3_order_certificate(N, a, K),
                }
            )

    sweep = [slim_case(*case) for case in SWEEP]
    result = {
        "status": "ACTIVE_RESEARCH_DIAGNOSTIC_NOT_A_PROOF",
        "purpose": "exact M1 projector/cross-twist assembly and falsifier suite",
        "implementations": {
            "python": "code/research/m1/cross_twist_energy.py",
            "cpp17": "code/research/m1/cross_twist_energy.cpp",
            "orchestrator": "code/research/m1/run_suite.py",
        },
        "anchor_cases": anchors,
        "sweep": sweep,
        "suite_checks": {
            "all_dual_impl_anchors_pass": all(x["dual_implementation_comparison"]["passed"] for x in anchors),
            "all_coset_mass_identities_pass": all(x["HH_mass_identity_error"] == 0 for x in sweep),
            "all_singular_regular_B_identities_pass": all(x["singular_regular_B_identity_error"] == 0 for x in sweep),
            "regular_3sqrtN_falsifier_pass_all_sampled": all(x["regular_3sqrtN_falsifier_pass"] for x in sweep),
            "all_applicable_trace3_order_certificates_pass": all(
                (not x["trace3_order_certificate"]["applicable"])
                or x["trace3_order_certificate"]["N_divides_LK_minus_2"]
                for x in sweep
            ),
        },
        "interpretation": {
            "exact": [
                "weighted key-table reconstruction",
                "quotient-character projector reconstruction at tested finite N within floating tolerance",
                "integer singular/regular B decomposition",
                "regular quotient-coset total-mass formula",
            ],
            "empirical_only": [
                "regular-fiber 3 sqrt(N) envelope on sampled cases",
                "observed K-scaling of full/regular energy corrections",
            ],
            "not_claimed": [
                "M1 asymptotic bound",
                "cross-twist orthogonality",
                "general BGS theorem",
            ],
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result["suite_checks"], indent=2, sort_keys=True))
    if not all(result["suite_checks"].values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
