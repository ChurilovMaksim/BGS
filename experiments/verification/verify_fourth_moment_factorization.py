#!/usr/bin/env python3
"""Verify the finite fourth-moment factorization and its coupled key geometry.

For an annihilator character family S of size m, the checked identity is

    sum_{chi,psi in S} |J(chi,psi;q)|^4 = m^2 * Sigma_4(q).

The same finite geometry is also resolved into the exact difference
histogram

    B(t) = # {((x,y),(z,w)) : coupled keys and x-y+z-w=t},

so that |V4| = sum_t B(t), Z0 = B(0), and the coupled energy is
sum_t B(t)^2.  B(t) is computed twice:

1. directly from all ordered pairs (x,y),(z,w);
2. from the collapsed key table, where the diagonal key (1,1) has
   multiplicity N-2 and every off-diagonal key has multiplicity one.

The two constructions must agree entry-by-entry.  This catches precisely the
ordered diagonal/off-diagonal bookkeeping error found in the historical Run
93.2 producer.
"""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np


@dataclass(frozen=True)
class KeyRecord:
    first_key: int
    second_key: int
    difference: int
    multiplicity: int

    @property
    def is_diagonal(self) -> bool:
        return self.first_key == 1 and self.second_key == 1


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


def subgroup_elements(generator: int, order: int, prime: int) -> np.ndarray:
    values = {pow(generator, exponent, prime) for exponent in range(order)}
    if len(values) != order:
        raise ValueError(
            f"generator {generator} does not have order {order} modulo {prime}"
        )
    return np.array(sorted(values), dtype=np.int64)


def pair_geometry(prime: int) -> tuple[np.ndarray, ...]:
    x_values = np.arange(2, prime, dtype=np.int64)
    x_grid, y_grid = np.meshgrid(x_values, x_values, indexing="ij")
    pair_x = x_grid.ravel()
    pair_y = y_grid.ravel()

    inverse_y = np.array(
        [pow(int(y), prime - 2, prime) for y in pair_y], dtype=np.int64
    )
    inverse_y_minus_one = np.array(
        [pow(int(y - 1), prime - 2, prime) for y in pair_y], dtype=np.int64
    )

    first_key = pair_x * inverse_y % prime
    second_key = (pair_x - 1) * inverse_y_minus_one % prime
    difference = (pair_x - pair_y) % prime
    return pair_x, pair_y, first_key, second_key, difference


def direct_difference_distribution(
    prime: int,
    subgroup: np.ndarray,
    first_key: np.ndarray,
    second_key: np.ndarray,
    difference: np.ndarray,
) -> np.ndarray:
    """Compute B(t) directly from all ordered pairs of original pairs."""
    distribution = np.zeros(prime, dtype=np.int64)
    batch_size = 256
    for start in range(0, len(first_key), batch_size):
        stop = min(start + batch_size, len(first_key))
        first_products = first_key[start:stop, None] * first_key[None, :] % prime
        second_products = (
            second_key[start:stop, None] * second_key[None, :] % prime
        )
        admissible = np.isin(first_products, subgroup) & np.isin(
            second_products, subgroup
        )
        difference_sums = (
            difference[start:stop, None] + difference[None, :]
        ) % prime
        np.add.at(distribution, difference_sums[admissible], 1)
    return distribution


def collapsed_key_table(
    prime: int,
    first_key: np.ndarray,
    second_key: np.ndarray,
    difference: np.ndarray,
) -> list[KeyRecord]:
    """Collapse original pairs to their key-table multiplicities.

    The only repeated key should be (1,1), arising from x=y.  All such pairs
    have difference zero and collapse to a single record of multiplicity N-2.
    Off-diagonal keys are required to be injective in these finite checks.
    """
    records: dict[tuple[int, int], KeyRecord] = {}
    for first, second, delta in zip(first_key, second_key, difference):
        key = (int(first), int(second))
        delta_int = int(delta)
        previous = records.get(key)
        if previous is None:
            records[key] = KeyRecord(key[0], key[1], delta_int, 1)
            continue
        if key != (1, 1) or previous.difference != 0 or delta_int != 0:
            raise AssertionError(f"unexpected repeated off-diagonal key: {key}")
        records[key] = KeyRecord(1, 1, 0, previous.multiplicity + 1)

    diagonal = records.get((1, 1))
    if diagonal is None or diagonal.multiplicity != prime - 2:
        raise AssertionError(
            f"diagonal multiplicity is {diagonal}; expected {prime - 2}"
        )
    return list(records.values())


def key_table_difference_distribution(
    prime: int,
    subgroup: np.ndarray,
    records: list[KeyRecord],
) -> tuple[np.ndarray, dict[str, int]]:
    """Compute B(t) from collapsed keys, keeping ordered coupling classes."""
    in_subgroup = np.zeros(prime, dtype=bool)
    in_subgroup[subgroup] = True
    distribution = np.zeros(prime, dtype=np.int64)
    classes = {
        "off_to_off": 0,
        "diagonal_to_off": 0,
        "off_to_diagonal": 0,
        "diagonal_to_diagonal": 0,
    }

    for left in records:
        for right in records:
            if not in_subgroup[left.first_key * right.first_key % prime]:
                continue
            if not in_subgroup[left.second_key * right.second_key % prime]:
                continue

            weight = left.multiplicity * right.multiplicity
            target = (left.difference + right.difference) % prime
            distribution[target] += weight

            if left.is_diagonal and right.is_diagonal:
                classes["diagonal_to_diagonal"] += weight
            elif left.is_diagonal:
                classes["diagonal_to_off"] += weight
            elif right.is_diagonal:
                classes["off_to_diagonal"] += weight
            else:
                classes["off_to_off"] += weight

    return distribution, classes


def jacobi_fourth_moment(
    prime: int,
    subgroup_order: int,
    q: int,
) -> tuple[int, int, float]:
    generator = primitive_root(prime)
    dlog = np.zeros(prime, dtype=np.int64)
    value = 1
    for exponent in range(prime - 1):
        dlog[value] = exponent
        value = value * generator % prime

    character_indices = np.arange(0, prime - 1, subgroup_order, dtype=np.int64)
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
    return generator, dimension, float(np.sum(np.abs(jacobi) ** 4))


def verify_design(
    prime: int,
    subgroup_generator: int,
    subgroup_order: int,
    q_values: tuple[int, ...],
) -> dict[str, object]:
    subgroup = subgroup_elements(subgroup_generator, subgroup_order, prime)
    _, _, first_key, second_key, difference = pair_geometry(prime)

    direct_distribution = direct_difference_distribution(
        prime, subgroup, first_key, second_key, difference
    )
    records = collapsed_key_table(prime, first_key, second_key, difference)
    key_distribution, coupling_classes = key_table_difference_distribution(
        prime, subgroup, records
    )

    distribution_equal = bool(np.array_equal(direct_distribution, key_distribution))
    if not distribution_equal:
        raise AssertionError("direct and collapsed key-table B(t) disagree")

    variety_count = int(direct_distribution.sum())
    zero_difference_count = int(direct_distribution[0])
    coupled_energy = int(np.dot(direct_distribution, direct_distribution))
    diagonal_weight = prime - 2
    expected_ordered_mixed = diagonal_weight * (subgroup_order - 1) * (
        subgroup_order - 2
    )

    q_checks: list[dict[str, object]] = []
    primitive = None
    dimension = None
    for q in q_values:
        primitive, dimension, left_side = jacobi_fourth_moment(
            prime, subgroup_order, q
        )
        roots = np.exp(2j * np.pi * q * np.arange(prime) / prime)
        sigma_four = np.dot(direct_distribution, roots)
        right_side = dimension**2 * sigma_four
        absolute_deviation = float(abs(left_side - right_side))
        relative_deviation = absolute_deviation / max(abs(left_side), 1.0)
        q_checks.append(
            {
                "q": q,
                "sum_abs_jacobi_fourth": left_side,
                "sigma_four_real": float(sigma_four.real),
                "sigma_four_imag": float(sigma_four.imag),
                "m_squared_sigma_four_real": float(right_side.real),
                "absolute_deviation": absolute_deviation,
                "relative_deviation": relative_deviation,
                "pass": bool(relative_deviation < 1e-11),
            }
        )

    mixed_classes_correct = (
        coupling_classes["diagonal_to_off"] == expected_ordered_mixed
        and coupling_classes["off_to_diagonal"] == expected_ordered_mixed
    )
    diagonal_class_correct = (
        coupling_classes["diagonal_to_diagonal"] == diagonal_weight**2
    )

    return {
        "N": prime,
        "a": subgroup_generator,
        "K": subgroup_order,
        "m": int(dimension),
        "primitive_root": int(primitive),
        "original_pair_count": int((prime - 2) ** 2),
        "collapsed_key_count": len(records),
        "diagonal_key_multiplicity": diagonal_weight,
        "distribution_methods_agree": distribution_equal,
        "constraint_variety_count": variety_count,
        "Z0": zero_difference_count,
        "coupled_energy_sum_B_squared": coupled_energy,
        "coupling_classes": coupling_classes,
        "expected_each_ordered_diagonal_off_class": expected_ordered_mixed,
        "ordered_diagonal_off_classes_correct": bool(mixed_classes_correct),
        "diagonal_diagonal_class_correct": bool(diagonal_class_correct),
        "difference_distribution_B": direct_distribution.tolist(),
        "q_checks": q_checks,
        "pass": bool(
            distribution_equal
            and mixed_classes_correct
            and diagonal_class_correct
            and all(check["pass"] for check in q_checks)
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    designs = [
        (23, 2, 11, (1,)),
        (53, 10, 13, (1, 7)),
    ]
    rows = [verify_design(*design) for design in designs]
    result = {
        "producer": "experiments/verification/verify_fourth_moment_factorization.py",
        "claim": (
            "Finite-design verification of the fourth-moment factorization, "
            "the complete difference distribution B(t), and the collapsed "
            "key-table multiplicities."
        ),
        "formula": "sum_{chi,psi in S}|J(chi,psi;q)|^4 = m^2 sum_t B(t)e_N(qt)",
        "implementation": (
            "self-contained Python; B(t) is built independently from original "
            "pair tuples and from a collapsed key table"
        ),
        "historical_bug_guard": (
            "Both ordered diagonal/off-diagonal classes are required.  The "
            "historical Run 93.2 producer inserted only one of them."
        ),
        "interpretation": (
            "The general algebraic reduction is exact, but these finite checks "
            "do not prove the asymptotic estimate on the constraint variety."
        ),
        "results": rows,
        "verdict": "PASS" if all(row["pass"] for row in rows) else "FAIL",
    }

    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
