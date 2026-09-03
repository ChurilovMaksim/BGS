#!/usr/bin/env python3
"""Cross-check vectorized twisted-Jacobi entries against direct scalar sums."""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src" / "python"))

from bgs.twisted_jacobi import (
    multiplicative_order,
    primitive_root,
    square_roots_mod_prime,
)

OUTPUT = ROOT / "results" / "verified" / "twisted_jacobi_scalar_formula.json"
TRACE = 3
Q_PROBES = (1, 2, 3, 5, 7)
RELATIVE_TOLERANCE = 5e-10


def find_design_eigenvalue(prime: int, subgroup_order: int) -> int:
    inverse_two = pow(2, prime - 2, prime)
    for root in square_roots_mod_prime(TRACE * TRACE - 4, prime):
        candidate = (TRACE + root) * inverse_two % prime
        if multiplicative_order(candidate, prime) == subgroup_order:
            return candidate
    raise ValueError(f"no order-{subgroup_order} eigenvalue at N={prime}")


def character_data(prime: int, subgroup_order: int):
    generator = primitive_root(prime)
    dlog = np.zeros(prime, dtype=np.int64)
    value = 1
    for exponent in range(prime - 1):
        dlog[value] = exponent
        value = value * generator % prime

    # This regression follows the preserved R87.1 residue/parity sector.
    character_indices = np.array(
        [
            k
            for k in range(prime - 1)
            if k % subgroup_order == 1 and k % 2 == 0
        ],
        dtype=np.int64,
    )
    x_values = np.arange(2, prime, dtype=np.int64)
    return dlog, character_indices, x_values


def sampled_entries(dimension: int) -> list[tuple[int, int]]:
    """Use all small-matrix entries and a deterministic large-matrix sample."""
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


def verify_design(prime: int, subgroup_order: int) -> dict[str, object]:
    started = time.time()
    eigenvalue = find_design_eigenvalue(prime, subgroup_order)
    dlog, character_indices, x_values = character_data(prime, subgroup_order)
    log_x = dlog[x_values]
    log_x_minus_one = dlog[(x_values - 1) % prime]

    left_matrix = np.exp(
        -2j
        * np.pi
        * np.outer(character_indices, log_x)
        / (prime - 1)
    )
    right_matrix = np.exp(
        2j
        * np.pi
        * np.outer(character_indices, log_x_minus_one)
        / (prime - 1)
    )

    pairs = sampled_entries(len(character_indices))
    max_abs_deviation = 0.0
    max_rel_deviation = 0.0
    worst_case: list[int] | None = None

    for q in Q_PROBES:
        additive = np.exp(2j * np.pi * (q * x_values % prime) / prime)
        vectorized = (left_matrix * additive) @ right_matrix.T

        for i, j in pairs:
            left = np.exp(
                -2j
                * np.pi
                * int(character_indices[i])
                * log_x
                / (prime - 1)
            )
            right = np.exp(
                2j
                * np.pi
                * int(character_indices[j])
                * log_x_minus_one
                / (prime - 1)
            )
            direct = np.sum(left * right * additive)
            deviation = abs(vectorized[i, j] - direct)
            relative = deviation / max(abs(direct), 1e-15)

            if deviation > max_abs_deviation:
                max_abs_deviation = float(deviation)
                worst_case = [int(q), int(i), int(j)]
            max_rel_deviation = max(max_rel_deviation, float(relative))

    return {
        "N": prime,
        "K": subgroup_order,
        "a": int(eigenvalue),
        "matrix_dimension": int(len(character_indices)),
        "q_values_checked": list(Q_PROBES),
        "entries_checked_per_q": len(pairs),
        "max_abs_deviation": max_abs_deviation,
        "max_relative_deviation": max_rel_deviation,
        "relative_tolerance": RELATIVE_TOLERANCE,
        "worst_q_i_j": worst_case,
        "wall_seconds": round(time.time() - started, 2),
        "pass": bool(max_rel_deviation <= RELATIVE_TOLERANCE),
    }


def main() -> None:
    rows = [verify_design(461, 23), verify_design(19489, 29)]
    result = {
        "producer": "experiments/verification/verify_twisted_jacobi_scalar_formula.py",
        "scope": "finite implementation cross-check; not an asymptotic theorem",
        "results": rows,
        "verdict": "PASS" if all(row["pass"] for row in rows) else "FAIL",
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
