#!/usr/bin/env python3
"""Finite exact regressions for the arithmetic identities in BGS-FM-010.

Only integer and Fraction arithmetic; no spectra of the kicked U_N or
asymptotic/statistical claim is tested. The all-N proof is in the note.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction as F
from math import gcd
from pathlib import Path


def mul(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return (a[0] * b[0] + a[1] * b[2],
            a[0] * b[1] + a[1] * b[3],
            a[2] * b[0] + a[3] * b[2],
            a[2] * b[1] + a[3] * b[3])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    C = (3, 2, 4, 3)
    assert mul((1, 1, 2, 1), (1, 1, 2, 1)) == C
    tested = scalar_returns = 0
    examples = []
    for n in range(3, 106, 2):
        power = (1, 0, 0, 1)
        p_power = (1, 0, 0, 1)
        u, v = 1, 0
        for m in range(1, 25):
            power = mul(power, C)
            p_power = mul(p_power, (1, 1, 2, 1))
            u, v = u + 2 * v, u + v
            assert u * u - 2 * v * v == (-1) ** m
            assert p_power == (u, v, 2 * v, u)
            lhs = (power[0] - 1, power[1], power[2], power[3] - 1)
            if m % 2:
                rhs = tuple(2 * u * x for x in p_power)
            else:
                rhs = tuple(2 * v * x for x in mul(p_power, (0, 1, 2, 0)))
            assert lhs == rhs
            fixed = sum(
                ((power[0] - 1) * x + power[1] * y) % n == 0
                and (power[2] * x + (power[3] - 1) * y) % n == 0
                for x in range(n) for y in range(n)
            )
            predicted = gcd(n, u if m % 2 else v) ** 2
            assert fixed == predicted and predicted >= 1
            if fixed == n * n:
                scalar_returns += 1
                if len(examples) < 12:
                    examples.append([n, m])
            tested += 1
    # Distinct Fourier modes at N>=19: 9/20 minus every other
    # negative real contribution, including both off-diagonal signs.
    negative_real = 4 * F(1, 40) + 2 * F(3, 1000) * (
        F(1) + F(1, 2) + F(1, 2))
    delta = F(9, 20) - negative_real
    assert negative_real == F(14, 125) and delta == F(169, 500)
    result = {
        "status": "finite exact regression passed",
        "dimensions": 52,
        "powers_per_dimension": 24,
        "fixed_point_cases": tested,
        "scalar_unperturbed_cases": scalar_returns,
        "first_scalar_unperturbed_cases": examples,
        "orbit_real_margin": str(delta),
        "scope": "Checks finite Weyl fixed points and one rational orbit margin. "
                 "It does not evaluate Tr(U_N^m) or prove their nonvanishing.",
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2) + "\n",
                               encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
