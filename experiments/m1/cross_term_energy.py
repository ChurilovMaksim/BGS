#!/usr/bin/env python3
"""Measure the missing cross-twist energy in the historical M1 fiber assembly.

This program deliberately reproduces the historical Möbius-fiber object before
attempting to repair it.  Its output is a diagnostic/falsifier, not a proof of
an asymptotic law and not yet a proof that this historical assembly is exactly
the current fourth-moment object.
"""
from __future__ import annotations

import argparse
import json
import math
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
    raise RuntimeError(f"primitive root not found modulo {prime}")


def dlog_table(prime: int, generator: int) -> np.ndarray:
    table = np.full(prime, -1, dtype=np.int64)
    value = 1
    for exponent in range(prime - 1):
        table[value] = exponent
        value = value * generator % prime
    return table


def annihilator_characters(
    prime: int, subgroup_order: int
) -> tuple[np.ndarray, np.ndarray, int]:
    """Return all characters trivial on the order-K subgroup."""
    generator = primitive_root(prime)
    dlog = dlog_table(prime, generator)
    exponents = np.arange(0, prime - 1, subgroup_order, dtype=np.int64)

    characters = np.zeros((len(exponents), prime), dtype=np.complex128)
    nonzero = np.arange(1, prime, dtype=np.int64)
    characters[:, nonzero] = np.exp(
        2j * np.pi * np.outer(exponents, dlog[nonzero]) / (prime - 1)
    )
    return characters, exponents, generator


def fiber_sums(
    prime: int, subgroup_order: int
) -> tuple[np.ndarray, int, np.ndarray, int]:
    """Build the historical fiber sums ``A_(psi1,psi2)(d)`` exactly as stated."""
    characters, exponents, generator = annihilator_characters(
        prime, subgroup_order
    )
    dimension = len(exponents)
    sums = np.zeros((dimension * dimension, prime), dtype=np.complex128)
    u_values = np.arange(1, prime, dtype=np.int64)

    for d in range(prime):
        denominator = (d - u_values + 1) % prime
        valid_denominator = denominator != 0
        u = u_values[valid_denominator]
        denominator = denominator[valid_denominator]

        numerator = (u * ((d - 1) % prime) + 1) % prime
        inverse_denominator = np.array(
            [pow(int(value), prime - 2, prime) for value in denominator],
            dtype=np.int64,
        )
        v = numerator * inverse_denominator % prime

        nonzero_v = v != 0
        u = u[nonzero_v]
        v = v[nonzero_v]
        sums[:, d] = (characters[:, u] @ characters[:, v].T).reshape(-1)

    return sums, dimension, exponents, generator


def analyse_design(prime: int, subgroup_order: int) -> dict[str, object]:
    if (prime - 1) % subgroup_order != 0:
        raise ValueError("K must divide N-1")

    fiber, dimension, exponents, generator = fiber_sums(prime, subgroup_order)

    # Circular convolution F_tau = A_tau * A_tau using NumPy's FFT convention.
    convolution = np.fft.ifft(np.fft.fft(fiber, axis=1) ** 2, axis=1)
    summed_convolution = convolution.sum(axis=0)

    total_raw = float(np.vdot(summed_convolution, summed_convolution).real)
    diagonal_raw = float(np.sum(np.abs(convolution) ** 2).real)
    cross_raw = total_raw - diagonal_raw

    trivial_diagonal_raw = float(np.vdot(convolution[0], convolution[0]).real)
    nontrivial_diagonal_raw = diagonal_raw - trivial_diagonal_raw
    nontrivial_sum = convolution[1:].sum(axis=0)
    trivial_nontrivial_cross_raw = float(
        2.0 * np.real(np.vdot(convolution[0], nontrivial_sum))
    )
    nontrivial_total_raw = float(np.vdot(nontrivial_sum, nontrivial_sum).real)
    nontrivial_cross_raw = nontrivial_total_raw - nontrivial_diagonal_raw

    historical_bound = 4.0 * math.sqrt(prime)
    violation_rows: list[dict[str, object]] = []
    for flat_index in range(1, dimension * dimension):
        first, second = divmod(flat_index, dimension)
        for d in range(prime):
            absolute_value = float(abs(fiber[flat_index, d]))
            if absolute_value > historical_bound + 1e-8:
                violation_rows.append(
                    {
                        "d": d,
                        "twist_indices": [first, second],
                        "character_exponents": [
                            int(exponents[first]),
                            int(exponents[second]),
                        ],
                        "abs_A": absolute_value,
                    }
                )

    normalized_energy = total_raw / dimension**4
    reconstructed_energy = (diagonal_raw + cross_raw) / dimension**4
    return {
        "N": prime,
        "K": subgroup_order,
        "m": int(dimension),
        "primitive_root": generator,
        "twist_pair_count": int(dimension * dimension),
        "character_convention": (
            "psi_k(x)=exp(2pi i k log_g(x)/(N-1)); "
            "k is a multiple of K; psi(0)=0"
        ),
        "fiber_model": "v_d(u)=((d-1)u+1)/(d+1-u), pole and v=0 omitted",
        "normalized_energy": normalized_energy,
        "reconstructed_energy": reconstructed_energy,
        "reconstruction_abs_error": abs(normalized_energy - reconstructed_energy),
        "diagonal_raw": diagonal_raw,
        "cross_raw": cross_raw,
        "cross_over_total": cross_raw / total_raw,
        "cross_over_diagonal": cross_raw / diagonal_raw,
        "trivial_diagonal_raw": trivial_diagonal_raw,
        "nontrivial_diagonal_raw": nontrivial_diagonal_raw,
        "trivial_nontrivial_cross_raw": trivial_nontrivial_cross_raw,
        "nontrivial_nontrivial_cross_raw": nontrivial_cross_raw,
        "max_abs_nontrivial_fiber_sum": float(np.max(np.abs(fiber[1:]))),
        "historical_4sqrtN_bound": historical_bound,
        "bound_violation_count": len(violation_rows),
        "bound_violations": violation_rows,
        "cross_terms_nonzero": bool(
            abs(cross_raw) > 1e-8 * max(1.0, total_raw)
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--design",
        action="append",
        default=[],
        help="design as N,K; may be supplied more than once",
    )
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    designs = args.design or ["53,13", "199,11"]
    rows = [
        analyse_design(*map(int, design.split(","))) for design in designs
    ]
    result = {
        "producer": "experiments/m1/cross_term_energy.py",
        "status": "DIAGNOSTIC; EXACT FOR THE IMPLEMENTED HISTORICAL ASSEMBLY",
        "claim": (
            "Tests the historical Mobius-fiber twist assembly.  It diagnoses "
            "missing cross terms and exceptional fibers; it does not prove "
            "the desired M1 asymptotic estimate."
        ),
        "results": rows,
    }

    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.out is not None:
        args.out.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
