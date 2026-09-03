#!/usr/bin/env python3
"""Independently verify the finite fourth-moment factorization.

The checked identity is

    sum_{chi,psi in S} |J(chi,psi;q)|^4 = m^2 * Sigma_4(q),

where ``Sigma_4`` is evaluated directly from the two product constraints.
The program is intentionally self-contained and imports nothing from the raw
historical workspace.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def prime_divisors(value: int) -> list[int]:
    divisors: list[int] = []
    candidate = 2
    while candidate * candidate <= value:
        if value % candidate == 0:
            divisors.append(candidate)
            while value % candidate == 0:
                value //= candidate
        candidate += 1
    if value > 1:
        divisors.append(value)
    return divisors


def primitive_root(prime: int) -> int:
    divisors = prime_divisors(prime - 1)
    for generator in range(2, prime):
        if all(
            pow(generator, (prime - 1) // divisor, prime) != 1
            for divisor in divisors
        ):
            return generator
    raise ValueError(f"primitive root not found modulo {prime}")


def verify_case(
    prime: int,
    subgroup_generator: int,
    subgroup_order: int,
    q: int,
) -> dict[str, object]:
    generator = primitive_root(prime)
    dlog = np.zeros(prime, dtype=np.int64)
    value = 1
    for exponent in range(prime - 1):
        dlog[value] = exponent
        value = value * generator % prime

    character_indices = np.arange(
        0, prime - 1, subgroup_order, dtype=np.int64
    )
    dimension = len(character_indices)
    x_values = np.arange(2, prime, dtype=np.int64)

    first_character = np.exp(
        2j
        * np.pi
        * np.outer(character_indices, dlog[x_values])
        / (prime - 1)
    )
    second_character = np.exp(
        2j
        * np.pi
        * np.outer(character_indices, dlog[(x_values - 1) % prime])
        / (prime - 1)
    )
    additive_phase = np.exp(2j * np.pi * q * x_values / prime)
    jacobi = (np.conj(first_character) * additive_phase) @ second_character.T
    left_side = float(np.sum(np.abs(jacobi) ** 4))

    x_grid, y_grid = np.meshgrid(x_values, x_values, indexing="ij")
    pair_x = x_grid.ravel()
    pair_y = y_grid.ravel()
    inverse_y = np.array(
        [pow(int(y), prime - 2, prime) for y in pair_y],
        dtype=np.int64,
    )
    inverse_y_minus_one = np.array(
        [pow(int(y - 1), prime - 2, prime) for y in pair_y],
        dtype=np.int64,
    )

    first_key = pair_x * inverse_y % prime
    second_key = (pair_x - 1) * inverse_y_minus_one % prime
    pair_phase = np.exp(
        2j * np.pi * q * ((pair_x - pair_y) % prime) / prime
    )
    subgroup = np.array(
        sorted(
            {
                pow(subgroup_generator, exponent, prime)
                for exponent in range(subgroup_order)
            }
        ),
        dtype=np.int64,
    )

    sigma_four = 0j
    constraint_variety_count = 0
    batch_size = 256
    for start in range(0, len(pair_x), batch_size):
        stop = start + batch_size
        first_products = first_key[start:stop, None] * first_key[None, :] % prime
        second_products = (
            second_key[start:stop, None] * second_key[None, :] % prime
        )
        admissible = np.isin(first_products, subgroup) & np.isin(
            second_products, subgroup
        )
        constraint_variety_count += int(admissible.sum())
        sigma_four += np.sum(
            admissible
            * pair_phase[start:stop, None]
            * pair_phase[None, :]
        )

    right_side = dimension**2 * sigma_four
    absolute_deviation = float(abs(left_side - right_side))
    relative_deviation = absolute_deviation / max(abs(left_side), 1.0)

    return {
        "N": prime,
        "a": subgroup_generator,
        "K": subgroup_order,
        "m": int(dimension),
        "q": q,
        "primitive_root": generator,
        "sum_abs_jacobi_fourth": left_side,
        "sigma_four_real": float(sigma_four.real),
        "sigma_four_imag": float(sigma_four.imag),
        "m_squared_sigma_four_real": float(right_side.real),
        "absolute_deviation": absolute_deviation,
        "relative_deviation": relative_deviation,
        "constraint_variety_count": constraint_variety_count,
        "pass": bool(relative_deviation < 1e-11),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    cases = [
        (23, 2, 11, 1),
        (53, 10, 13, 1),
        (53, 10, 13, 7),
    ]
    rows = [verify_case(*case) for case in cases]
    result = {
        "producer": "experiments/verification/verify_fourth_moment_factorization.py",
        "claim": (
            "Finite-design verification of the fourth-moment "
            "character-orthogonality factorization."
        ),
        "formula": "sum_{chi,psi in S}|J(chi,psi;q)|^4 = m^2 Sigma_4(q)",
        "implementation": (
            "clean independent Python evaluation; no imports from "
            "archive/legacy-workspace"
        ),
        "interpretation": (
            "The general algebraic identity is derived in research/theory.md; "
            "these finite checks do not prove the required asymptotic bound."
        ),
        "results": rows,
        "verdict": "PASS" if all(row["pass"] for row in rows) else "FAIL",
    }

    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
