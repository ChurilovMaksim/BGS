#!/usr/bin/env python3
"""Exact finite regression for cayley_product_row_reflection.md.

For r=-1 the real-trace row cofactor is a reflection of itself.  After shifting
by tau we split P(tau+Z)=E(Z^2)+Z O(Z^2), compute the first two fixed-degree
subresultants of E,O, and form their coefficient ideal in Z[tau].  Its Smith
exponent gives the displayed finite Xi anchors.

The default cases are small; --extended adds K=29,31 and a direct finite-field
check of I_{-1}(31,1303)=4.  No finite run proves a growing-K prime bound.
"""
from __future__ import annotations

import argparse
from collections import Counter

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

from cayley_product_row_real_trace_ideal import (
    TAU,
    T,
    coefficient_modulus,
    real_cyclotomic_polynomial,
    reduce_real,
    strip_2K,
    trace_cofactor_pair,
)

Z, Y = sp.symbols("Z Y")


def reduce_var_polynomial(expr: sp.Expr, var: sp.Symbol, modulus: sp.Poly) -> sp.Poly:
    poly = sp.Poly(sp.expand(expr), var)
    reduced = sum(
        reduce_real(coeff, modulus) * var**degree
        for (degree,), coeff in poly.terms()
    )
    return sp.Poly(sp.expand(reduced), var)


def even_odd_pair(K: int) -> tuple[sp.Poly, sp.Poly, sp.Poly]:
    modulus, P, Q = trace_cofactor_pair(K, K - 1)

    # Exact reflection Q(T)=-P(2*tau-T).
    reflected = reduce_var_polynomial(-P.as_expr().subs(T, 2 * TAU - T), T, modulus)
    q_reduced = reduce_var_polynomial(Q.as_expr(), T, modulus)
    assert reflected == q_reduced

    F = reduce_var_polynomial(P.as_expr().subs(T, TAU + Z), Z, modulus)
    even = sp.Integer(0)
    odd = sp.Integer(0)
    for (degree,), coeff in F.terms():
        if degree % 2 == 0:
            even += coeff * Y ** (degree // 2)
        else:
            odd += coeff * Y ** ((degree - 1) // 2)

    E = reduce_var_polynomial(even, Y, modulus)
    O = reduce_var_polynomial(odd, Y, modulus)
    m = (K - 1) // 2
    if m % 2 == 0:
        assert E.LC() == 1 and E.degree() == m // 2
    else:
        assert O.LC() == 1 and O.degree() == (m - 1) // 2
    return modulus, E, O


def reflection_ideal_exponent(K: int) -> tuple[int, int, list[int]]:
    if K < 7:
        raise ValueError("reflection subresultant integral construction requires K>=7")
    modulus, E, O = even_odd_pair(K)
    raw = sp.subresultants(E.as_expr(), O.as_expr(), Y)
    reduced = [reduce_var_polynomial(expr, Y, modulus) for expr in raw]

    # Corank >=2 / gcd degree >=2 is detected by the final degree-1 and
    # degree-0 fixed-degree subresultants. At K=7 these are the monic
    # input O=S_1 (top-index convention) and the resultant S_0.
    selected = reduced[-2:]
    assert [poly.degree() for poly in selected] == [1, 0], (
        K,
        [poly.degree() for poly in reduced],
    )

    coeffs: list[sp.Expr] = []
    for poly in selected:
        for coeff in poly.all_coeffs():
            coeff = reduce_real(coeff, modulus)
            if coeff != 0:
                coeffs.append(coeff)
    assert coeffs

    m = (K - 1) // 2
    columns: list[sp.Matrix] = []
    for coeff in coeffs:
        for j in range(m):
            reduced_coeff = sp.Poly(
                reduce_real(coeff * TAU**j, modulus), TAU, domain=sp.ZZ
            )
            columns.append(
                sp.Matrix([int(reduced_coeff.nth(k)) for k in range(m)])
            )

    lattice = sp.Matrix.hstack(*columns)
    smith = smith_normal_form(lattice, domain=sp.ZZ)
    invariants = [
        abs(int(smith[j, j]))
        for j in range(min(smith.rows, smith.cols))
        if smith[j, j] != 0
    ]
    assert len(invariants) == m
    assert all(
        invariants[j + 1] % invariants[j] == 0
        for j in range(len(invariants) - 1)
    )
    full = invariants[-1]
    return strip_2K(full, K), full, invariants


def prime_to_2K_reflection_support(K: int) -> int:
    """Split support including trivial small orders, without fictitious ideals."""
    if not sp.isprime(K) or K == 2:
        raise ValueError("require odd prime K")
    if K in (3, 5):
        return 1
    return reflection_ideal_exponent(K)[0]


def check_chebyshev_fibre(K: int) -> None:
    C = real_cyclotomic_polynomial(K).as_expr()
    lhs = sp.expand(2 * (sp.chebyshevt(K, T / 2) - 1))
    rhs = sp.expand((T - 2) * C**2)
    assert sp.Poly(lhs - rhs, T, domain=sp.ZZ).is_zero


def direct_inverse_row_intersection(K: int, p: int) -> int:
    """Maximum common-parameter count for ratio -1, finite split regression."""
    assert (p - 1) % K == 0
    g = int(sp.primitive_root(p))
    h = pow(g, (p - 1) // K, p)

    def c(z: int) -> int:
        return (z + 1) * pow((z - 1) % p, -1, p) % p

    powers = [pow(h, a, p) for a in range(K)]
    rows: dict[int, set[int]] = {}
    for i in range(1, K):
        values: set[int] = set()
        for a in range(1, K):
            b = (2 * i - a) % K
            if b == 0:
                continue
            values.add((c(powers[a]) + c(powers[b])) % p)
        rows[i] = values

    best = 0
    for i in range(1, K):
        j = (-i) % K
        if j == 0:
            continue
        best = max(best, len(rows[i] & rows[j]))
    return best


def check_anchor(K: int, stripped: int, full: int) -> None:
    check_chebyshev_fibre(K)
    observed, observed_full, invariants = reflection_ideal_exponent(K)
    assert observed == stripped, (K, observed, stripped)
    assert observed_full == full, (K, observed_full, full)
    print(
        f"K={K:2d} Xi={observed_full} Xi'={observed} "
        f"smith_rank={len(invariants)}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--extended", action="store_true")
    args = parser.parse_args()

    for K in (3, 5):
        assert prime_to_2K_reflection_support(K) == 1
    check_anchor(7, 1, 1)

    for K, stripped, full in (
        (13, 5, 5 * 13),
        (17, 1, 17**2),
        (19, 37, 19**3 * 37),
        (23, 47 * 137, 23**4 * 47 * 137),
    ):
        check_anchor(K, stripped, full)

    if args.extended:
        check_anchor(
            29,
            59**2 * 173 * 463,
            29**5 * 59**2 * 173 * 463,
        )
        check_anchor(
            31,
            5 * 61**2 * 311 * 557 * 929 * 1303,
            5 * 31**6 * 61**2 * 311 * 557 * 929 * 1303,
        )
        observed_I = direct_inverse_row_intersection(31, 1303)
        assert observed_I == 4, observed_I
        print("K=31 p=1303 inverse-row intersection: I=4")

    print("cayley inverse-row reflection regression: OK")


if __name__ == "__main__":
    main()
