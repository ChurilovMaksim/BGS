#!/usr/bin/env python3
"""Compare the historical Möbius-fiber assembly with the correct key-table one.

The historical M1 route eliminated the original pair variables and then summed
characters over the Möbius graph

    v_d(u) = ((d-1)u+1)/(d+1-u).

That eliminated graph is not the same finite set as the original pair-key
image.  In particular, (u,v)=(1,1) is a saturation artifact for d!=0 and the
true diagonal key has multiplicity N-2 at d=0.

This diagnostic builds both assemblies independently and checks the exact
correction formula.  The historical energy is retained only as a falsifier;
the current M1 object is the key-table assembly.
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
    factors = prime_divisors(prime - 1)
    for generator in range(2, prime):
        if all(
            pow(generator, (prime - 1) // factor, prime) != 1
            for factor in factors
        ):
            return generator
    raise RuntimeError(f"primitive root not found modulo {prime}")


def character_table(
    prime: int, subgroup_order: int
) -> tuple[np.ndarray, np.ndarray, int]:
    """Return every multiplicative character trivial on the order-K subgroup."""
    generator = primitive_root(prime)
    dlog = np.full(prime, -1, dtype=np.int64)
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


def historical_mobius_amplitudes(
    prime: int, characters: np.ndarray
) -> np.ndarray:
    """Reproduce the historical graph sum A_hist(tau,d)."""
    dimension = characters.shape[0]
    amplitudes = np.zeros((dimension * dimension, prime), dtype=np.complex128)
    all_u = np.arange(1, prime, dtype=np.int64)

    for d in range(prime):
        denominator = (d + 1 - all_u) % prime
        valid = denominator != 0
        u = all_u[valid]
        denominator = denominator[valid]
        numerator = ((d - 1) * u + 1) % prime
        inverse = np.array(
            [pow(int(value), prime - 2, prime) for value in denominator],
            dtype=np.int64,
        )
        v = numerator * inverse % prime
        nonzero_v = v != 0
        u = u[nonzero_v]
        v = v[nonzero_v]
        amplitudes[:, d] = (characters[:, u] @ characters[:, v].T).reshape(-1)

    return amplitudes


def correct_key_amplitudes(
    prime: int, characters: np.ndarray
) -> np.ndarray:
    """Build A_key(tau,d) from the original pairs (x,y), including multiplicity."""
    dimension = characters.shape[0]
    amplitudes = np.zeros((dimension * dimension, prime), dtype=np.complex128)

    for x in range(2, prime):
        for y in range(2, prime):
            u = x * pow(y, prime - 2, prime) % prime
            v = (x - 1) * pow(y - 1, prime - 2, prime) % prime
            d = (x - y) % prime
            twist_values = (
                characters[:, u][:, None] * characters[:, v][None, :]
            ).reshape(-1)
            amplitudes[:, d] += twist_values

    return amplitudes


def circular_convolutions(amplitudes: np.ndarray) -> np.ndarray:
    fourier = np.fft.fft(amplitudes, axis=1)
    return np.fft.ifft(fourier**2, axis=1)


def assembly_energy(amplitudes: np.ndarray, dimension: int) -> dict[str, float]:
    convolutions = circular_convolutions(amplitudes)
    summed = convolutions.sum(axis=0)
    total_raw = float(np.vdot(summed, summed).real)
    diagonal_raw = float(np.sum(np.abs(convolutions) ** 2).real)
    cross_raw = total_raw - diagonal_raw
    return {
        "total_raw": total_raw,
        "diagonal_raw": diagonal_raw,
        "cross_raw": cross_raw,
        "cross_over_diagonal": cross_raw / diagonal_raw,
        "normalized_energy": total_raw / dimension**4,
    }


def verify_correction(
    prime: int,
    exponents: np.ndarray,
    historical: np.ndarray,
    correct: np.ndarray,
) -> dict[str, object]:
    """Check A_hist-A_key exactly up to floating-point roundoff."""
    dimension = len(exponents)
    expected = np.ones_like(historical)

    # At d=0 the true key table contains the diagonal key with multiplicity N-2.
    # The historical graph instead sums u over F_N^*\{1} with v=1.
    for first in range(dimension):
        for second in range(dimension):
            flat = first * dimension + second
            if first == 0:
                expected[flat, 0] = 0.0
            else:
                expected[flat, 0] = -(prime - 1)

    observed = historical - correct
    max_abs = float(np.max(np.abs(observed - expected)))

    historical_fourier = np.fft.fft(historical, axis=1)
    correct_fourier = np.fft.fft(correct, axis=1)
    fourier_difference = historical_fourier - correct_fourier

    expected_fourier = np.zeros_like(fourier_difference)
    # First character trivial: delta(d)=1 for d!=0 and 0 at d=0.
    # Its DFT equals N-1 at xi=0 and -1 otherwise.
    for second in range(dimension):
        flat = second
        expected_fourier[flat, 0] = prime - 1
        expected_fourier[flat, 1:] = -1
    # First character nontrivial: delta(0)=-(N-1), delta(d)=1 otherwise.
    # Its DFT is 0 at xi=0 and -N elsewhere.
    for first in range(1, dimension):
        for second in range(dimension):
            flat = first * dimension + second
            expected_fourier[flat, 0] = 0
            expected_fourier[flat, 1:] = -prime

    fourier_max_abs = float(
        np.max(np.abs(fourier_difference - expected_fourier))
    )
    return {
        "time_domain_max_abs_residual": max_abs,
        "fourier_domain_max_abs_residual": fourier_max_abs,
        "formula": {
            "d_nonzero": "A_hist(tau,d)=A_key(tau,d)+1 for every twist pair",
            "d_zero_first_twist_trivial": "A_hist=A_key=N-2",
            "d_zero_first_twist_nontrivial": "A_hist=-1, A_key=N-2",
        },
        "pass": bool(max_abs < 1e-10 and fourier_max_abs < 1e-9),
    }


def analyse_design(prime: int, subgroup_order: int) -> dict[str, object]:
    if (prime - 1) % subgroup_order != 0:
        raise ValueError("K must divide N-1")

    characters, exponents, generator = character_table(prime, subgroup_order)
    dimension = len(exponents)
    historical = historical_mobius_amplitudes(prime, characters)
    correct = correct_key_amplitudes(prime, characters)

    correction = verify_correction(prime, exponents, historical, correct)
    historical_energy = assembly_energy(historical, dimension)
    correct_energy = assembly_energy(correct, dimension)

    # The exact twist collapse says sum_tau(A_tau*A_tau)=m^2 B.  Therefore
    # the normalized correct energy is the integer sum_t B(t)^2; rounding is
    # only used after checking that numerical noise is tiny.
    rounded_correct_energy = int(round(correct_energy["normalized_energy"]))
    integer_residual = abs(
        correct_energy["normalized_energy"] - rounded_correct_energy
    )

    return {
        "N": prime,
        "K": subgroup_order,
        "m": dimension,
        "primitive_root": generator,
        "correction_identity": correction,
        "historical_mobius_energy": historical_energy,
        "correct_key_table_energy": correct_energy,
        "correct_energy_integer_sum_B_squared": rounded_correct_energy,
        "correct_energy_integer_residual": integer_residual,
        "historical_over_correct_energy": (
            historical_energy["normalized_energy"]
            / correct_energy["normalized_energy"]
        ),
        "pass": bool(correction["pass"] and integer_residual < 1e-3),
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
    rows = [analyse_design(*map(int, item.split(","))) for item in designs]
    result = {
        "producer": "experiments/m1/cross_term_energy.py",
        "status": "EXACT FINITE DIAGNOSTIC; HISTORICAL ASSEMBLY RETRACTED",
        "claim": (
            "Compares the historical Mobius graph with the exact pair-key "
            "assembly and checks their closed-form difference."
        ),
        "conclusion": (
            "The historical Mobius object is not the current M1 object.  "
            "Current work must use the pair-key assembly and its exact B(t) "
            "collapse."
        ),
        "results": rows,
        "verdict": "PASS" if all(row["pass"] for row in rows) else "FAIL",
    }

    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.out is not None:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
