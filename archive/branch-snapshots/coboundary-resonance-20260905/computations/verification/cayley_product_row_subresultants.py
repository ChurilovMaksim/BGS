#!/usr/bin/env python3
"""Exact finite regression for cayley_product_row_subresultants.md.

The universal theorem is proved in the mathematics note.  This script constructs
projective fixed-product row polynomials over Z[zeta_K], computes the first three
subresultants of two Galois-normalized rows, takes absolute cyclotomic norms of
all nonzero coefficients, and forms their rational gcd after stripping 2 and K.

Default anchors are deliberately modest enough for CI.  ``--extended`` adds the
slower K=23 example.  No finite run proves the growing-K divisor bound.
"""
from __future__ import annotations

import argparse
from functools import reduce
from math import gcd

import sympy as sp

X, U = sp.symbols("X U")


def phi_expr(K: int) -> sp.Expr:
    return sum(X**j for j in range(K))


def reduce_cyclotomic(expr: sp.Expr, K: int) -> sp.Expr:
    """Reduce a Laurent-free integer polynomial modulo Phi_K."""
    phi = sp.Poly(phi_expr(K), X, domain=sp.ZZ)
    poly = sp.Poly(sp.expand(expr), X, domain=sp.ZZ)
    return sp.Poly(poly.rem(phi), X, domain=sp.ZZ).as_expr()


def monomial(K: int, exponent: int) -> sp.Expr:
    return X ** (exponent % K)


def row_polynomial(K: int, i: int) -> sp.Poly:
    """Return R_i(U)=prod_a(D_{i,a} U-N_i) over trace classes a~ -a.

    The invalid trace class a=+-i is omitted.  Coefficients are represented as
    reduced polynomials in X modulo Phi_K.
    """
    i %= K
    assert i != 0
    m = (K - 1) // 2
    N = 1 - monomial(K, 2 * i)

    expr = sp.Integer(1)
    for a in range(m + 1):
        if a == i or (-a) % K == i:
            continue
        trace = sp.Integer(2) if a == 0 else monomial(K, a) + monomial(K, -a)
        D = monomial(K, i) * trace - 2
        expr *= U * D - N
        # Keep coefficient swell controlled after each factor.
        poly_u = sp.Poly(sp.expand(expr), U)
        expr = sum(
            reduce_cyclotomic(coeff, K) * U**degree
            for (degree,), coeff in poly_u.terms()
        )

    out = sp.Poly(sp.expand(expr), U)
    assert out.degree() == m
    return out


def subresultants_in_cyclotomic_ring(K: int, r: int) -> list[sp.Poly]:
    A = row_polynomial(K, 1)
    B = row_polynomial(K, r)
    # SymPy treats coefficients as rational functions in X; reduce every
    # subresultant coefficient back into the cyclotomic integer basis.
    raw = sp.subresultants(A.as_expr(), B.as_expr(), U)
    out: list[sp.Poly] = []
    for expr in raw:
        poly = sp.Poly(sp.expand(expr), U)
        reduced = sum(
            reduce_cyclotomic(sp.cancel(coeff), K) * U**degree
            for (degree,), coeff in poly.terms()
        )
        out.append(sp.Poly(sp.expand(reduced), U))
    return out


def absolute_norm(K: int, coeff: sp.Expr) -> int:
    coeff = reduce_cyclotomic(coeff, K)
    if coeff == 0:
        return 0
    value = sp.resultant(phi_expr(K), coeff, X)
    return abs(int(value))


def strip_2K(n: int, K: int) -> int:
    n = abs(int(n))
    for q in (2, K):
        while n and n % q == 0:
            n //= q
    return n


def higher_intersection_integer(K: int, r: int) -> tuple[int, list[int]]:
    subs = subresultants_in_cyclotomic_ring(K, r)
    degrees = [poly.degree() for poly in subs]
    m = (K - 1) // 2
    # All promoted anchors have the normal subresultant degree sequence.  This
    # assertion protects the indexing below against a silent CAS convention
    # change or accidental row degeneration.
    assert degrees == [m, m] + list(range(m - 1, -1, -1)), (K, r, degrees)

    # The final three nonzero polynomial subresultants have U-degrees 2,1,0.
    selected = subs[-3:]
    assert [poly.degree() for poly in selected] == [2, 1, 0]

    norms: list[int] = []
    for poly in selected:
        for coeff in poly.all_coeffs():
            norm = absolute_norm(K, coeff)
            if norm:
                norms.append(norm)
    assert norms
    g = reduce(gcd, norms)
    return strip_2K(g, K), degrees


def check_anchor(K: int, r: int, expected: int) -> None:
    observed, degrees = higher_intersection_integer(K, r)
    assert observed == expected, (K, r, observed, expected)
    print(f"K={K:2d} r={r:2d} G3'={observed} degrees={degrees}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--extended", action="store_true")
    args = parser.parse_args()

    # Independently recomputed exact anchors from the proof-development pass.
    for K, r, expected in (
        (7, 2, 1),
        (11, 2, 1),
        (13, 3, 3**3),
        (13, 12, 5**8),
        (17, 10, 103**2),
    ):
        check_anchor(K, r, expected)

    if args.extended:
        check_anchor(23, 18, 47**20 * 139**2)

    print("cayley product-row subresultant regression: OK")


if __name__ == "__main__":
    main()
