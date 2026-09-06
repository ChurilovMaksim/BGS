#!/usr/bin/env python3
"""Active finite regressions for the twisted-Jacobi implementation.

Two independent numerical contracts are checked:

* selected matrix entries from a BLAS matrix product are compared with direct
  scalar character sums;
* standardized fourth moments are compared with the preserved R82 q-curves.

The checks are finite floating-point implementation regressions.  They are not
asymptotic theorems and do not establish BGS/GOE local statistics.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "computations" / "python"))

from bgs.finite_field import primitive_root  # noqa: E402
from bgs.jacobi import dlog_table  # noqa: E402
from bgs.twisted_jacobi import build_closed_form, find_design_eigenvalue  # noqa: E402

REFERENCE = ROOT / "evidence" / "reference" / "r82"
RELATIVE_TOLERANCE = 5e-10
MOMENT_TOLERANCE = 5e-10
Q_PROBES = (1, 2, 3, 5, 7)
EXPECTED_REFERENCE_HASHES = {
    "closed_form.json": "f0003f946e2ef2b17e00f9830534f16f9fe432749eafe325d194af0c5aa88ffa",
    "q_curve_N199.npz": "6c1b8bbe82073c0c0f1d0ce1f8808a45f0117c1826e980c7c09444edc64ca893",
    "q_curve_N3571.npz": "c77758459ce1a7804199e8459bab7081b009bdc702b5d0b7a528e3234a366c33",
}


def verify_reference_hashes() -> dict[str, str]:
    observed: dict[str, str] = {}
    for name, expected in EXPECTED_REFERENCE_HASHES.items():
        path = REFERENCE / name
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != expected:
            raise AssertionError(f"{name}: SHA-256 {digest} != audited {expected}")
        observed[name] = digest
    return observed


def sampled_entries(dimension: int) -> list[tuple[int, int]]:
    if dimension <= 16:
        return [(i, j) for i in range(dimension) for j in range(dimension)]

    pairs = {
        (0, 0),
        (0, dimension - 1),
        (dimension - 1, 0),
        (dimension - 1, dimension - 1),
        (dimension // 2, dimension // 2),
        (1, 2),
        (2, 1),
    }
    rng = np.random.default_rng(20260902)
    while len(pairs) < 32:
        pairs.add(
            (
                int(rng.integers(0, dimension)),
                int(rng.integers(0, dimension)),
            )
        )
    return sorted(pairs)


def scalar_formula_design(prime: int, subgroup_order: int) -> dict[str, object]:
    eigenvalue = find_design_eigenvalue(prime, subgroup_order)
    generator = primitive_root(prime)
    dlog = dlog_table(prime, generator)

    character_indices = np.array(
        [
            k
            for k in range(prime - 1)
            if k % subgroup_order == 1 and k % 2 == 0
        ],
        dtype=np.int64,
    )
    x_values = np.arange(2, prime, dtype=np.int64)
    log_x = dlog[x_values]
    log_x_minus_one = dlog[(x_values - 1) % prime]

    pairs = sampled_entries(len(character_indices))
    left_indices = sorted({i for i, _ in pairs})
    right_indices = sorted({j for _, j in pairs})
    left_position = {i: row for row, i in enumerate(left_indices)}
    right_position = {j: row for row, j in enumerate(right_indices)}

    # Only rows/columns needed by the deterministic sample are materialized.
    # This preserves an independent BLAS-vs-direct accumulation check without
    # building the full O(m^2) output matrix at the large design.
    left = np.exp(
        -2j
        * np.pi
        * np.outer(character_indices[left_indices], log_x)
        / (prime - 1)
    )
    right = np.exp(
        2j
        * np.pi
        * np.outer(character_indices[right_indices], log_x_minus_one)
        / (prime - 1)
    )

    max_abs = 0.0
    max_rel = 0.0
    worst: list[int] | None = None
    for q in Q_PROBES:
        additive = np.exp(2j * np.pi * (q * x_values % prime) / prime)
        block = (left * additive) @ right.T

        for i, j in pairs:
            scalar_left = np.exp(
                -2j
                * np.pi
                * int(character_indices[i])
                * log_x
                / (prime - 1)
            )
            scalar_right = np.exp(
                2j
                * np.pi
                * int(character_indices[j])
                * log_x_minus_one
                / (prime - 1)
            )
            direct = np.sum(scalar_left * scalar_right * additive)
            matrix_value = block[left_position[i], right_position[j]]
            deviation = abs(matrix_value - direct)
            relative = deviation / max(abs(direct), 1e-15)
            if deviation > max_abs:
                max_abs = float(deviation)
                worst = [int(q), int(i), int(j)]
            max_rel = max(max_rel, float(relative))

    return {
        "N": prime,
        "K": subgroup_order,
        "a": int(eigenvalue),
        "matrix_dimension": int(len(character_indices)),
        "q_values_checked": list(Q_PROBES),
        "entries_checked_per_q": len(pairs),
        "max_abs_deviation": max_abs,
        "max_relative_deviation": max_rel,
        "relative_tolerance": RELATIVE_TOLERANCE,
        "worst_q_i_j": worst,
        "pass": bool(max_rel <= RELATIVE_TOLERANCE),
    }


def deterministic_q_sample(prime: int) -> list[int]:
    candidates = {
        1,
        2,
        3,
        5,
        7,
        11,
        17,
        prime // 7,
        prime // 3,
        prime // 2,
        prime - 2,
        prime - 1,
    }
    return sorted(q for q in candidates if 0 < q < prime)


def moment_curve_design(
    reference_design: dict[str, object], full_curve: bool
) -> dict[str, object]:
    prime = int(reference_design["N"])
    subgroup_order = int(reference_design["K"])
    eigenvalue = find_design_eigenvalue(prime, subgroup_order)
    if eigenvalue != int(reference_design["a"]):
        raise AssertionError(
            f"N={prime}: design eigenvalue {eigenvalue} != reference {reference_design['a']}"
        )

    with np.load(REFERENCE / f"q_curve_N{prime}.npz") as curve:
        q_array = curve["q"].astype(int)
        mu4_array = curve["mu4"].astype(float)
    measured = dict(zip(q_array.tolist(), mu4_array.tolist()))

    if full_curve or prime <= 199:
        q_values = sorted(measured)
    else:
        q_values = [q for q in deterministic_q_sample(prime) if q in measured]

    scale = int(reference_design["scale_c"])
    inverse_scale = pow(scale, prime - 2, prime)
    internal_q = [inverse_scale * q % prime for q in q_values]
    closed, dimension = build_closed_form(
        prime,
        subgroup_order,
        eigenvalue,
        int(reference_design["k0"]),
        bool(reference_design["parity_odd"]),
        internal_q,
    )

    deviations = np.array(
        [
            abs(closed[inverse_scale * q % prime]["mu4"] - measured[q])
            for q in q_values
        ],
        dtype=float,
    )
    max_deviation = float(deviations.max(initial=0.0))
    return {
        "N": prime,
        "K": subgroup_order,
        "a": int(eigenvalue),
        "matrix_dimension": int(dimension),
        "reference_levels": int(len(measured)),
        "levels_checked_now": int(len(q_values)),
        "full_curve_rerun": bool(full_curve or prime <= 199),
        "max_abs_mu4_deviation": max_deviation,
        "mean_abs_mu4_deviation": float(deviations.mean()) if len(deviations) else 0.0,
        "absolute_tolerance": MOMENT_TOLERANCE,
        "pass": bool(max_deviation <= MOMENT_TOLERANCE),
    }


def run(full_curves: bool) -> dict[str, object]:
    hashes = verify_reference_hashes()
    scalar = [
        scalar_formula_design(461, 23),
        scalar_formula_design(19489, 29),
    ]

    reference = json.loads((REFERENCE / "closed_form.json").read_text(encoding="utf-8"))
    moments = [
        moment_curve_design(design, full_curve=full_curves)
        for design in reference["designs"]
    ]
    passed = all(row["pass"] for row in scalar + moments)
    return {
        "producer": "computations/verification/twisted_jacobi_regression.py",
        "scope": (
            "Finite floating-point implementation/reference regression; "
            "not an asymptotic theorem and not a BGS local-statistics result."
        ),
        "reference_sha256": hashes,
        "scalar_formula": scalar,
        "moment_curve": moments,
        "verdict": "PASS" if passed else "FAIL",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--full-curves",
        action="store_true",
        help="recompute every q in the N=3571 preserved curve (slow); default samples it",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="optional JSON output path; stdout is always emitted",
    )
    args = parser.parse_args()

    result = run(full_curves=args.full_curves)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    if result["verdict"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
