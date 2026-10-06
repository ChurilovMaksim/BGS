#!/usr/bin/env python3
"""Exact finite regression for cayley_product_row_real_trace_ideal.md.

The computation lives in the maximal real cyclotomic field
Q(tau), tau=zeta+zeta^-1.  The full trace polynomial contains the a=0 trace
2; after removing the unique forced invalid root tau, both row polynomials keep
fixed degree modulo every split prime p != K.  We compute the first three
subresultants, form their coefficient ideal, and recover its contraction to Z
as the largest Smith invariant of O^+/J.

Default anchors are fast enough for CI. ``--extended`` adds the K=23 case.
Finite regression is not a proof of the growing-K split-divisor bound.
"""
from __future__ import annotations

import argparse

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

TAU, T = sp.symbols("TAU T")


def real_cyclotomic_polynomial(K: int) -> sp.Poly:
    """Minimal polynomial C_K of tau=zeta+zeta^-1 for odd prime K."""
    assert K >= 3 and K % 2 == 1
    m = (K - 1) // 2
    expr = sp.Integer(1) + 2 * sum(
        sp.chebyshevt(a, T / 2) for a in range(1, m + 1)
    )
    poly = sp.Poly(sp.expand(expr), T, domain=sp.ZZ)
    assert poly.degree() == m and poly.LC() == 1
    return poly


def coefficient_modulus(K: int) -> sp.Poly:
    """The same C_K, with TAU as coefficient-field generator."""
    return sp.Poly(
        real_cyclotomic_polynomial(K).as_expr().subs(T, TAU),
        TAU,
        domain=sp.ZZ,
    )


def reduce_real(expr: sp.Expr, modulus: sp.Poly) -> sp.Expr:
    return sp.Poly(sp.expand(expr), TAU, domain=sp.ZZ).rem(modulus).as_expr()


def reduce_T_polynomial(expr: sp.Expr, modulus: sp.Poly) -> sp.Poly:
    poly = sp.Poly(sp.expand(expr), T)
    reduced = sum(
        reduce_real(coeff, modulus) * T**degree
        for (degree,), coeff in poly.terms()
    )
    return sp.Poly(sp.expand(reduced), T)


def synthetic_divide_by_tau(poly: sp.Poly, modulus: sp.Poly) -> sp.Poly:
    """Divide an integral O^+[T] polynomial known to vanish at T=TAU."""
    degree = poly.degree()
    coeffs = [sp.Integer(0)] * (degree + 1)
    for (e,), coeff in poly.terms():
        coeffs[e] = reduce_real(coeff, modulus)

    quotient = [sp.Integer(0)] * degree
    quotient[degree - 1] = coeffs[degree]
    for j in range(degree - 1, 0, -1):
        quotient[j - 1] = reduce_real(
            coeffs[j] + TAU * quotient[j], modulus
        )

    remainder = reduce_real(coeffs[0] + TAU * quotient[0], modulus)
    assert remainder == 0
    return reduce_T_polynomial(
        sum(quotient[j] * T**j for j in range(degree)), modulus
    )


def trace_cofactor_pair(K: int, r: int) -> tuple[sp.Poly, sp.Poly, sp.Poly]:
    """Return coefficient modulus and the two degree-m valid-trace polynomials."""
    modulus = coefficient_modulus(K)
    C_T = real_cyclotomic_polynomial(K).as_expr()
    H = sp.expand((T - 2) * C_T)

    alpha = reduce_real(sp.chebyshevu(r - 1, TAU / 2), modulus)
    beta = reduce_real(-2 * sp.chebyshevu(r - 2, TAU / 2), modulus)

    source_full = reduce_T_polynomial(H, modulus)
    target_full = reduce_T_polynomial(H.subs(T, alpha * T + beta), modulus)

    P = synthetic_divide_by_tau(source_full, modulus)
    Q = synthetic_divide_by_tau(target_full, modulus)
    m = (K - 1) // 2
    assert P.degree() == Q.degree() == m

    # alpha is a cyclotomic unit.  Its real-field norm must be +-1.
    norm_alpha = sp.resultant(modulus.as_expr(), alpha, TAU)
    assert abs(int(norm_alpha)) == 1, (K, r, norm_alpha)
    return modulus, P, Q


def selected_subresultant_coefficients(K: int, r: int) -> tuple[sp.Poly, list[sp.Expr]]:
    if K < 7:
        raise ValueError("three-subresultant integral construction requires K>=7")
    modulus, P, Q = trace_cofactor_pair(K, r)
    raw = sp.subresultants(P.as_expr(), Q.as_expr(), T)
    reduced: list[sp.Poly] = []
    for expr in raw:
        reduced.append(reduce_T_polynomial(expr, modulus))

    selected = reduced[-3:]
    assert [poly.degree() for poly in selected] == [2, 1, 0], (
        K,
        r,
        [poly.degree() for poly in reduced],
    )

    coeffs: list[sp.Expr] = []
    for poly in selected:
        for coeff in poly.all_coeffs():
            coeff = reduce_real(coeff, modulus)
            if coeff != 0:
                coeffs.append(coeff)
    assert coeffs
    return modulus, coeffs


def strip_2K(n: int, K: int) -> int:
    n = abs(int(n))
    for q in (2, K):
        while n and n % q == 0:
            n //= q
    return n


def real_trace_ideal_exponent(K: int, r: int) -> tuple[int, int, list[int]]:
    """Return (prime-to-2K Lambda, full Lambda, Smith invariants)."""
    modulus, coeffs = selected_subresultant_coefficients(K, r)
    m = (K - 1) // 2

    columns: list[sp.Matrix] = []
    for coeff in coeffs:
        for j in range(m):
            reduced = sp.Poly(
                reduce_real(coeff * TAU**j, modulus), TAU, domain=sp.ZZ
            )
            columns.append(
                sp.Matrix([int(reduced.nth(k)) for k in range(m)])
            )

    lattice = sp.Matrix.hstack(*columns)
    assert lattice.rows == m
    smith = smith_normal_form(lattice, domain=sp.ZZ)
    invariants = [
        abs(int(smith[j, j]))
        for j in range(min(smith.rows, smith.cols))
        if smith[j, j] != 0
    ]
    assert len(invariants) == m, (K, r, len(invariants), m)
    assert all(
        invariants[j + 1] % invariants[j] == 0
        for j in range(len(invariants) - 1)
    )

    full = invariants[-1]
    return strip_2K(full, K), full, invariants


def prime_to_2K_order_three_support(K: int, r: int) -> int:
    """Split order-three support, including the trivial small-degree cases.

    No full integral ideal or Smith invariants are assigned at K=3,5.
    """
    if not sp.isprime(K) or K == 2 or not 2 <= r < K:
        raise ValueError("require odd prime K and normalized 2<=r<K")
    if K in (3, 5):
        return 1
    return real_trace_ideal_exponent(K, r)[0]


def check_anchor(K: int, r: int, stripped: int, full: int) -> None:
    observed, observed_full, invariants = real_trace_ideal_exponent(K, r)
    assert observed == stripped, (K, r, observed, stripped)
    assert observed_full == full, (K, r, observed_full, full)
    print(
        f"K={K:2d} r={r:2d} Lambda3={observed_full} "
        f"Lambda3'={observed} smith_rank={len(invariants)}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--extended", action="store_true")
    args = parser.parse_args()

    for K in (3, 5):
        for r in range(2, K):
            assert prime_to_2K_order_three_support(K, r) == 1

    for K, r, stripped, full in (
        (7, 2, 1, 7),
        (11, 7, 1, 11**2),
        (13, 3, 1, 13**3),
        (13, 12, 5**2, 2**4 * 5**2 * 13**3),
        (17, 10, 103, 2**2 * 17**5 * 103),
    ):
        check_anchor(K, r, stripped, full)

    if args.extended:
        check_anchor(23, 18, 47**3 * 139, 23**8 * 47**3 * 139)

    print("cayley product-row real-trace ideal regression: OK")


if __name__ == "__main__":
    main()
