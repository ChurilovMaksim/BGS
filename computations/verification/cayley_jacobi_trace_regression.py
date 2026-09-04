#!/usr/bin/env python3
"""Finite numerical regression for the exact Cayley--Jacobi trace identity.

Mathematical theorem (proved separately in
mathematics/cayley_jacobi_trace_average.md):

    hat(1_A)(r) = K * Tr M_S(2r),

where A=c(H\{1}), S=H^perp and M_S is the full annihilator normalized
Twisted-Jacobi matrix in the maintained convention.

This script checks only finite floating-point evaluations of that exact identity
and its second/fourth Parseval consequences.  It does not prove the theorem,
Bombieri--Vinogradov, the double-averaged asymptotic, a CLT, or BGS.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "computations" / "python"))

from bgs.finite_field import multiplicative_order, primitive_root  # noqa: E402
from bgs.jacobi import annihilator_indices, dlog_table, jacobi_matrix  # noqa: E402

IDENTITY_TOL = 5e-10
MOMENT_TOL = 5e-9


def subgroup_generator(prime: int, order: int) -> int:
    g = primitive_root(prime)
    h = pow(g, (prime - 1) // order, prime)
    if multiplicative_order(h, prime) != order:
        raise AssertionError("failed to construct exact-order subgroup generator")
    return h


def cayley_values(prime: int, order: int, h: int) -> list[int]:
    values: list[int] = []
    z = h
    for _ in range(1, order):
        if z == 1:
            raise AssertionError("subgroup generator returned early to 1")
        values.append((z + 1) * pow((z - 1) % prime, -1, prime) % prime)
        z = z * h % prime
    if z != 1 or len(values) != order - 1 or len(set(values)) != order - 1:
        raise AssertionError("Cayley set construction failed")
    return values


def direct_fourier(prime: int, values: list[int], r: int) -> complex:
    residues = np.asarray(values, dtype=np.int64)
    phases = np.exp(2j * np.pi * ((r * residues) % prime) / prime)
    return complex(phases.sum())


def full_trace_value(
    prime: int,
    order: int,
    h: int,
    dlog: np.ndarray,
    annihilator: np.ndarray,
    r: int,
) -> complex:
    twisted_q = (2 * r) % prime
    jacobi = jacobi_matrix(prime, order, h, dlog, annihilator, twisted_q)
    inverse_two = pow(2, prime - 2, prime)
    half_q = inverse_two * twisted_q % prime
    phase = np.exp(-2j * np.pi * half_q / prime)
    normalized_trace = phase * np.trace(jacobi) / (prime - 1)
    return complex(order * normalized_trace)


def additive_energy(prime: int, values: list[int]) -> int:
    counts: Counter[int] = Counter()
    for a in values:
        for b in values:
            counts[(a - b) % prime] += 1
    return sum(m * m for m in counts.values())


def audit_design(
    prime: int,
    order: int,
    *,
    all_frequencies: bool,
    sample_frequencies: tuple[int, ...] = (),
) -> dict[str, object]:
    if (prime - 1) % order:
        raise AssertionError("order must divide prime-1")

    g = primitive_root(prime)
    dlog = dlog_table(prime, g)
    h = subgroup_generator(prime, order)
    annihilator = annihilator_indices(prime, order, h, dlog)
    if len(annihilator) != (prime - 1) // order:
        raise AssertionError("annihilator dimension mismatch")

    values = cayley_values(prime, order, h)
    frequencies = list(range(prime)) if all_frequencies else sorted(
        {q % prime for q in sample_frequencies}
    )
    if not frequencies:
        raise AssertionError("empty frequency audit")

    max_identity_error = 0.0
    max_trace_imaginary = 0.0
    trace_scaled: dict[int, complex] = {}
    for r in frequencies:
        direct = direct_fourier(prime, values, r)
        scaled_trace = full_trace_value(
            prime, order, h, dlog, annihilator, r
        )
        trace_scaled[r] = scaled_trace
        max_identity_error = max(max_identity_error, abs(direct - scaled_trace))
        # The exact theorem says K*Tr M(2r)=hat(1_A)(r), which is real because A=-A.
        max_trace_imaginary = max(max_trace_imaginary, abs(scaled_trace.imag))

    if max_identity_error > IDENTITY_TOL:
        raise AssertionError(
            f"Cayley/Jacobi trace identity regression failed at (p,K)=({prime},{order}): "
            f"max error {max_identity_error}"
        )
    if max_trace_imaginary > IDENTITY_TOL:
        raise AssertionError(
            f"scaled full trace is not numerically real at (p,K)=({prime},{order})"
        )

    result: dict[str, object] = {
        "p": prime,
        "K": order,
        "annihilator_dimension": len(annihilator),
        "frequencies_checked": len(frequencies),
        "max_fourier_trace_error": max_identity_error,
        "max_scaled_trace_imaginary_part": max_trace_imaginary,
    }

    if all_frequencies:
        ordered = np.asarray([trace_scaled[q] / order for q in range(prime)])
        observed_second = float(np.sum(np.abs(ordered) ** 2))
        observed_fourth = float(np.sum(np.abs(ordered) ** 4))
        energy = additive_energy(prime, values)
        expected_second = prime * (order - 1) / (order**2)
        expected_fourth = prime * energy / (order**4)
        second_error = abs(observed_second - expected_second)
        fourth_error = abs(observed_fourth - expected_fourth)
        if second_error > MOMENT_TOL * max(1.0, abs(expected_second)):
            raise AssertionError(
                f"second trace moment mismatch at (p,K)=({prime},{order})"
            )
        if fourth_error > MOMENT_TOL * max(1.0, abs(expected_fourth)):
            raise AssertionError(
                f"fourth trace moment mismatch at (p,K)=({prime},{order})"
            )
        q0_expected = (order - 1) / order
        q0_observed = trace_scaled[0] / order
        if abs(q0_observed - q0_expected) > IDENTITY_TOL:
            raise AssertionError("q=0 normalized trace mismatch")
        result.update(
            {
                "additive_energy": energy,
                "sum_abs_trace_squared": observed_second,
                "expected_sum_abs_trace_squared": expected_second,
                "sum_abs_trace_fourth": observed_fourth,
                "expected_sum_abs_trace_fourth": expected_fourth,
                "q0_trace": float(q0_observed.real),
                "expected_q0_trace": q0_expected,
            }
        )

    return result


def main() -> None:
    result = {
        "producer": "computations/verification/cayley_jacobi_trace_regression.py",
        "arithmetic": "finite-field exact set construction + complex128 Jacobi/Fourier evaluation",
        "scope": (
            "Finite regression of the exact full-annihilator Cayley/Jacobi trace identity. "
            "All frequencies are checked at (53,13) and (199,11); a distinct larger "
            "collision-rich design (461,23) is checked on deterministic frequencies. "
            "No asymptotic theorem is inferred from these floating-point checks."
        ),
        "tolerances": {
            "identity_absolute": IDENTITY_TOL,
            "moment_relative": MOMENT_TOL,
        },
        "audits": [
            audit_design(53, 13, all_frequencies=True),
            audit_design(199, 11, all_frequencies=True),
            audit_design(
                461,
                23,
                all_frequencies=False,
                sample_frequencies=(0, 1, 2, 17, 73, 230, 459, 460),
            ),
        ],
        "verdict": "PASS",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
