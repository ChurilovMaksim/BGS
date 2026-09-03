#!/usr/bin/env python3
"""Verify the finite second-moment character-orthogonality reduction."""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src" / "python"))

from bgs.jacobi import dlog_table
from bgs.twisted_jacobi import primitive_root

OUTPUT = ROOT / "results" / "verified" / "second_moment_reduction.json"


def subgroup(prime: int, order: int, generator: int) -> list[int]:
    """Return the unique subgroup of the requested order."""
    step = pow(generator, (prime - 1) // order, prime)
    values: list[int] = []
    value = 1
    for _ in range(order):
        values.append(value)
        value = value * step % prime
    return values


def constraint_pairs(prime: int, subgroup_values: list[int]) -> list[tuple[int, int]]:
    """Build the off-diagonal pair set appearing in the exact reduction."""
    subgroup_set = set(subgroup_values)
    pairs: list[tuple[int, int]] = []
    for x in range(2, prime):
        for y in range(2, prime):
            if x == y:
                continue
            if x * pow(y, prime - 2, prime) % prime not in subgroup_set:
                continue
            ratio_shifted = (x - 1) * pow(y - 1, prime - 2, prime) % prime
            if ratio_shifted not in subgroup_set:
                continue
            pairs.append((x, y))
    return pairs


def verify_design(prime: int, eigenvalue: int, subgroup_order: int) -> dict[str, object]:
    generator = primitive_root(prime)
    dlog = dlog_table(prime, generator)
    pairs = constraint_pairs(prime, subgroup(prime, subgroup_order, generator))

    expected_count = (subgroup_order - 1) * (subgroup_order - 2)
    if len(pairs) != expected_count:
        raise AssertionError(
            f"constraint count mismatch at N={prime}: {len(pairs)} != {expected_count}"
        )

    pair_x = np.array([x for x, _ in pairs], dtype=np.int64)
    pair_y = np.array([y for _, y in pairs], dtype=np.int64)
    differences = (pair_x - pair_y) % prime

    eigen_exponent = int(dlog[eigenvalue])
    annihilator_step = (prime - 1) // math.gcd(eigen_exponent, prime - 1)
    character_indices = np.array(
        [k for k in range(prime - 1) if k % annihilator_step == 0],
        dtype=np.int64,
    )
    dimension = len(character_indices)

    x_values = np.arange(2, prime, dtype=np.int64)
    left = np.exp(
        -2j * np.pi * np.outer(character_indices, dlog[x_values]) / (prime - 1)
    )
    right = np.exp(
        2j
        * np.pi
        * np.outer(character_indices, dlog[(x_values - 1) % prime])
        / (prime - 1)
    )

    off_diagonal_sums = np.array(
        [
            np.exp(2j * np.pi * (q * differences % prime) / prime).sum()
            for q in range(1, prime)
        ]
    )

    maximum_deviation = 0.0
    for q in (1, 2, 3):
        phase = np.exp(2j * np.pi * (q * x_values % prime) / prime)
        jacobi = (left * phase) @ right.T
        measured = float((np.abs(jacobi) ** 2).sum())
        predicted = dimension**2 * (
            (prime - 2) + off_diagonal_sums[q - 1].real
        )
        maximum_deviation = max(maximum_deviation, abs(measured - predicted))

    return {
        "N": prime,
        "a": eigenvalue,
        "K": subgroup_order,
        "m": int(dimension),
        "constraint_pair_count": len(pairs),
        "expected_pair_count": expected_count,
        "identity_max_abs_deviation": float(maximum_deviation),
        "pass": bool(maximum_deviation < 1e-8),
    }


def main() -> None:
    rows = [
        verify_design(53, 10, 13),
        verify_design(199, 139, 11),
    ]
    result = {
        "producer": "experiments/verification/verify_second_moment_reduction.py",
        "scope": "finite exact reduction check; not an asymptotic theorem",
        "results": rows,
        "verdict": "PASS" if all(row["pass"] for row in rows) else "FAIL",
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
