#!/usr/bin/env python3
"""Exact finite checks for the 2026-11-18 BGS torsion-history intake.

These checks verify modular identities and the literal midpoint cubic jet.
They are not certificates of an asymptotic spectral theorem.
"""
from fractions import Fraction as F
import json

BASE_COMMIT = "3d21de1f3cca6470e352f4272cf354ee2eb39d4e"
S = ((3, 4), (2, 3))


def multiply_mod(a, b, n):
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(2)) % n for j in range(2))
        for i in range(2)
    )


def power_mod(a, k, n):
    out = ((1, 0), (0, 1))
    while k:
        if k & 1:
            out = multiply_mod(out, a, n)
        a = multiply_mod(a, a, n)
        k //= 2
    return out


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(a, c):
    return tuple(c * x for x in a)


def product(a, b):
    return tuple(
        sum(a[j] * b[i - j] for j in range(i + 1))
        for i in range(4)
    )


def literal_jet(c):
    """The theta^0..theta^3 coefficients of centered g(theta,phi).

    The scalar c equals cos(phi-alpha_0), sampled at four right angles.
    """
    one = (F(1), F(0), F(0), F(0))
    cos7 = (F(1), F(0), -F(49, 2), F(0))
    cos1 = (F(1), F(0), -F(1, 2), F(0))
    sin1 = (F(0), F(1), F(0), -F(1, 6))
    r = product(add(one, scale(cos7, -1)), add(one, cos1))
    shifted_r = product(add(one, cos7), add(one, scale(cos1, -1)))
    return add(
        add(
            add(cos7, scale(r, F(1, 10))),
            scale(product(r, sin1), F(1, 100)),
        ),
        add(scale(shifted_r, c / 100), scale(one, -F(1, 10))),
    )


def main():
    assert power_mod(S, 3, 10 ** 12) == ((99, 140), (70, 99))
    assert (99 - 1) % 7 == 140 % 7 == 70 % 7 == 0

    rows = []
    for j in range(2, 11):
        n = 7 ** j
        r = 3 * 7 ** (j - 1)
        assert power_mod(S, r, n) == ((1, 0), (0, 1))
        inv2 = pow(2, -1, n)
        # The raw midpoint cocycle vanishes on the 49 torsion labels.
        assert inv2 * (n // 7) ** 2 % n == 0
        assert 49 * (n // 49) == n
        assert 4 * r < 2 * n
        rows.append({
            "j": j,
            "N": n,
            "return_length": r,
            "sector_rank": n // 49,
        })

    phases = (-F(3, 5), F(4, 5), F(3, 5), -F(4, 5))
    jets = []
    for c in phases:
        jet = literal_jet(c)
        expected = (F(9, 10), F(0), -F(98, 5) + c / 100, F(49, 100))
        assert jet == expected
        jets.append(str(-500 * jet[2]))
    assert jets == ["9803", "9796", "9797", "9804"]
    assert F(1) - F(1, 49) == F(48, 49)

    return {
        "status": "passed",
        "base_commit": BASE_COMMIT,
        "tested_torsion_powers": rows,
        "literal_centered_midpoint_jet": {
            "constant": "9/10",
            "linear": "0",
            "quadratic_coefficient": "-98/5+cos(phi-alpha_0)/100",
            "cubic_coefficient": "49/100",
            "minus_500_quadratic_grid": jets,
        },
        "zero_kick_interference_over_N_squared": "48/49",
        "scope": "finite exact algebra only; no asymptotic or algebraic-nonvanishing certificate",
    }


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, ensure_ascii=False))
