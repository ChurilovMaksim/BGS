#!/usr/bin/env python3
"""Verify the exact k=4 pair-key geometry by independent finite constructions.

This is a finite regression/certification script, not an asymptotic proof. It
checks the complete difference distribution B(t), the exact |V4| formula, the
fourth-moment Fourier identity, and the character-twist collapse.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src" / "python"))

from bgs.key_geometry import (  # noqa: E402
    KeyRecord,
    direct_difference_distribution,
    expected_coupling_classes,
    explicit_key_table,
    fast_difference_distribution,
    original_pair_key_table,
    records_as_map,
    sigma_mean_variance,
    subgroup_elements,
    variety_count_formula,
    zero_difference_main_term,
)


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
    factors = prime_divisors(prime - 1)
    for generator in range(2, prime):
        if all(
            pow(generator, (prime - 1) // factor, prime) != 1
            for factor in factors
        ):
            return generator
    raise RuntimeError(f"primitive root not found modulo {prime}")


def annihilator_character_table(
    prime: int, subgroup_order: int
) -> tuple[np.ndarray, np.ndarray, int]:
    generator = primitive_root(prime)
    dlog = np.zeros(prime, dtype=np.int64)
    value = 1
    for exponent in range(prime - 1):
        dlog[value] = exponent
        value = value * generator % prime

    exponents = np.arange(0, prime - 1, subgroup_order, dtype=np.int64)
    characters = np.zeros((len(exponents), prime), dtype=np.complex128)
    nonzero = np.arange(1, prime, dtype=np.int64)
    characters[:, nonzero] = np.exp(
        2j * np.pi * np.outer(exponents, dlog[nonzero]) / (prime - 1)
    )
    return characters, exponents, generator


def verify_twist_collapse(
    prime: int,
    subgroup_order: int,
    records: list[KeyRecord],
    distribution: np.ndarray,
) -> dict[str, object]:
    """Check sum_tau A_tau*A_tau=m^2 B in time and Fourier domains."""
    characters, exponents, generator = annihilator_character_table(
        prime, subgroup_order
    )
    dimension = len(exponents)
    amplitudes = np.zeros(
        (dimension * dimension, prime), dtype=np.complex128
    )

    for record in records:
        twist = (
            characters[:, record.u][:, None]
            * characters[:, record.v][None, :]
        ).reshape(-1)
        amplitudes[:, record.difference] += record.multiplicity * twist

    fourier = np.fft.fft(amplitudes, axis=1)
    frequency_left = np.sum(fourier**2, axis=0)
    frequency_right = dimension**2 * np.fft.fft(distribution)
    frequency_abs = float(np.max(np.abs(frequency_left - frequency_right)))
    frequency_rel = frequency_abs / max(
        float(np.max(np.abs(frequency_right))), 1.0
    )

    time_left = np.sum(np.fft.ifft(fourier**2, axis=1), axis=0)
    time_right = dimension**2 * distribution
    time_abs = float(np.max(np.abs(time_left - time_right)))
    time_rel = time_abs / max(float(np.max(np.abs(time_right))), 1.0)

    return {
        "primitive_root": generator,
        "character_order": dimension,
        "character_generator_exponent": int(exponents[1]) if dimension > 1 else 0,
        "frequency_identity_max_abs_deviation": frequency_abs,
        "frequency_identity_max_relative_deviation": frequency_rel,
        "time_identity_max_abs_deviation": time_abs,
        "time_identity_max_relative_deviation": time_rel,
        "pass": bool(frequency_rel < 1e-12 and time_rel < 1e-12),
    }


def jacobi_fourth_moment(
    prime: int, subgroup_order: int, q: int
) -> tuple[int, int, float]:
    characters, exponents, generator = annihilator_character_table(
        prime, subgroup_order
    )
    x_values = np.arange(2, prime, dtype=np.int64)

    phase = np.exp(2j * np.pi * q * x_values / prime)
    jacobi = (
        np.conj(characters[:, x_values]) * phase
    ) @ characters[:, (x_values - 1) % prime].T
    return generator, len(exponents), float(np.sum(np.abs(jacobi) ** 4))


def verify_design(
    prime: int,
    subgroup_generator: int,
    subgroup_order: int,
    q_values: tuple[int, ...],
) -> dict[str, object]:
    subgroup = subgroup_elements(
        prime=prime,
        generator=subgroup_generator,
        order=subgroup_order,
    )
    records = explicit_key_table(prime)
    fast_distribution, fast_classes = fast_difference_distribution(prime, subgroup)

    expected_classes = expected_coupling_classes(prime, subgroup_order)
    class_formula_ok = fast_classes == expected_classes
    variety_formula = variety_count_formula(prime, subgroup_order)
    variety_count = int(fast_distribution.sum())

    geometry_checks: dict[str, object] = {
        "explicit_key_count": len(records),
        "expected_key_count": (prime - 2) * (prime - 3) + 1,
        "class_totals_match_closed_form": class_formula_ok,
        "V4_closed_form": variety_formula,
        "V4_matches_closed_form": variety_count == variety_formula,
        "fast_vs_original_pair_collapse": "NOT_RUN_AT_THIS_SIZE",
        "fast_vs_direct_key_loop": "NOT_RUN_AT_THIS_SIZE",
    }

    if prime <= 53:
        original_records = original_pair_key_table(prime)
        if records_as_map(original_records) != records_as_map(records):
            raise AssertionError(
                "original pair collapse and explicit key table disagree"
            )

        direct_distribution, direct_classes = direct_difference_distribution(
            prime, subgroup, records
        )
        if not np.array_equal(direct_distribution, fast_distribution):
            raise AssertionError(
                "direct key loop and fast H^2 distribution disagree"
            )
        if direct_classes != fast_classes:
            raise AssertionError("direct and fast coupling classes disagree")
        geometry_checks["fast_vs_original_pair_collapse"] = True
        geometry_checks["fast_vs_direct_key_loop"] = True

    if prime <= 199:
        twist_collapse: dict[str, object] = verify_twist_collapse(
            prime, subgroup_order, records, fast_distribution
        )
    else:
        twist_collapse = {
            "status": "NOT_RUN_AT_THIS_SIZE",
            "reason": (
                "The exact identity is independently checked through N=199; "
                "this larger anchor uses the validated H^2 geometry plus a "
                "direct Jacobi fourth-moment check."
            ),
            "pass": True,
        }

    q_checks: list[dict[str, object]] = []
    primitive_root_value = 0
    dimension = 0
    for q in q_values:
        primitive_root_value, dimension, left_side = jacobi_fourth_moment(
            prime, subgroup_order, q
        )
        root = np.exp(2j * np.pi * q * np.arange(prime) / prime)
        sigma = np.dot(fast_distribution, root)
        right_side = dimension**2 * sigma
        deviation = float(abs(left_side - right_side))
        relative = deviation / max(abs(left_side), 1.0)
        q_checks.append(
            {
                "q": q,
                "sum_abs_jacobi_fourth": left_side,
                "sigma_four_real": float(sigma.real),
                "sigma_four_imag": float(sigma.imag),
                "m_squared_sigma_four_real": float(right_side.real),
                "absolute_deviation": deviation,
                "relative_deviation": relative,
                "pass": bool(relative < 1e-10),
            }
        )

    mean_sigma, variance_sigma = sigma_mean_variance(fast_distribution)
    std_sigma = variance_sigma**0.5
    b0_main, b0_error_bound, quadratic_character_sum = zero_difference_main_term(
        prime, subgroup
    )
    b0_remainder = int(fast_distribution[0]) - b0_main
    mean_structure_bound_ok = abs(b0_remainder) <= b0_error_bound + 1e-12
    coupled_energy = int(
        sum(int(value) * int(value) for value in fast_distribution.tolist())
    )

    passed = bool(
        class_formula_ok
        and variety_count == variety_formula
        and twist_collapse["pass"]
        and mean_structure_bound_ok
        and all(check["pass"] for check in q_checks)
    )

    return {
        "N": prime,
        "a": subgroup_generator,
        "K": subgroup_order,
        "m": dimension,
        "primitive_root": primitive_root_value,
        "geometry_cross_checks": geometry_checks,
        "diagonal_key_multiplicity": prime - 2,
        "constraint_variety_count": variety_count,
        "Z0": int(fast_distribution[0]),
        "coupled_energy_sum_B_squared": coupled_energy,
        "coupling_classes": fast_classes,
        "twist_sum_collapse": twist_collapse,
        "B0_mean_structure": {
            "deterministic_part": b0_main,
            "generic_cubic_remainder": b0_remainder,
            "uniform_abs_bound": b0_error_bound,
            "quadratic_character_sum_H_without_1": quadratic_character_sum,
            "pass": bool(mean_structure_bound_ok),
        },
        "mean_sigma4_nonzero_q": mean_sigma,
        "std_sigma4_nonzero_q": std_sigma,
        "mean_sigma4_over_N_squared": mean_sigma / prime**2,
        "std_sigma4_over_NK": std_sigma / (prime * subgroup_order),
        "relative_std_over_K_over_N": (
            (std_sigma / mean_sigma) / (subgroup_order / prime)
        ),
        "difference_distribution_B": fast_distribution.tolist(),
        "q_checks": q_checks,
        "pass": passed,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    designs = [
        (23, 2, 11, (1,)),
        (53, 10, 13, (1, 7)),
        (199, 139, 11, (1, 7)),
        (461, 23, 23, (1,)),
    ]
    rows = [verify_design(*design) for design in designs]
    result = {
        "producer": "experiments/verification/verify_fourth_moment_factorization.py",
        "claim": (
            "Finite verification of the complete k=4 pair-key distribution, "
            "its exact coupling totals, the V4 closed form, the twist collapse, "
            "and the fourth-moment Fourier identity."
        ),
        "formula": "sum_{chi,psi}|J(chi,psi;q)|^4=m^2 sum_t B(t)e_N(qt)",
        "exact_V4_formula": (
            "(K^2+1)N^2-(6K^2+3K)N+13K^2-3K"
        ),
        "historical_bug_guard": (
            "The diagonal key is handled separately and both ordered mixed "
            "classes are required; this guards against the Run-93.2 omission."
        ),
        "independence": {
            "python": (
                "original-pair collapse, explicit key table and direct key loop "
                "are cross-checked at small N; the H^2 algorithm supplies the "
                "larger exact anchors"
            ),
            "cpp": (
                "the C++20 verifier independently repeats the geometry and q "
                "checks and uses direct DFT/convolution for twist collapse"
            ),
        },
        "interpretation": (
            "All statements here are finite identities/regressions. The "
            "asymptotic variance estimate remains open."
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
