#!/usr/bin/env python3
"""Exact algebraic regression for cayley_inverse_sparse_unlikely_intersection.md.

This script does NOT verify the external Bombieri--Masser--Zannier / Amoroso--
Leroux--Sombra theorem.  It checks only the project-specific algebra wrapped
around that theorem:
  * the cleared fixed torus equations are coprime for all three zero patterns;
  * the all-ones point makes each two-equation ideal proper;
  * the quotient-torus pullbacks are exactly the inverse edge Laurent equations.
"""
from __future__ import annotations

import sympy as sp

X, Y, U, V, Z, x = sp.symbols("X Y U V Z x")


def interior_equations() -> tuple[sp.Expr, sp.Expr]:
    l1 = X + X**-1 + Y + Y**-1 - 2 * Z - 2 * Z**-1
    l2 = U + U**-1 + V + V**-1 - 2 * Z - 2 * Z**-1
    return l1, l2


def one_zero_equations() -> tuple[sp.Expr, sp.Expr]:
    l0 = 2 + Y + Y**-1 - 2 * Z - 2 * Z**-1
    l2 = U + U**-1 + V + V**-1 - 2 * Z - 2 * Z**-1
    return l0, l2


def two_zero_equations() -> tuple[sp.Expr, sp.Expr]:
    m1 = 2 + Y + Y**-1 - 2 * Z - 2 * Z**-1
    m2 = 2 + V + V**-1 - 2 * Z - 2 * Z**-1
    return m1, m2


def cleared_coprime_checks() -> None:
    l1, l2 = interior_equations()
    f1 = sp.Poly(sp.expand(X * Y * Z * l1), X, Y, U, V, Z, domain=sp.QQ)
    f2 = sp.Poly(sp.expand(U * V * Z * l2), X, Y, U, V, Z, domain=sp.QQ)
    assert sp.gcd(f1, f2).total_degree() == 0
    assert l1.subs({X: 1, Y: 1, U: 1, V: 1, Z: 1}) == 0
    assert l2.subs({X: 1, Y: 1, U: 1, V: 1, Z: 1}) == 0

    l0, l2b = one_zero_equations()
    f0 = sp.Poly(sp.expand(Y * Z * l0), Y, U, V, Z, domain=sp.QQ)
    f2b = sp.Poly(sp.expand(U * V * Z * l2b), Y, U, V, Z, domain=sp.QQ)
    assert sp.gcd(f0, f2b).total_degree() == 0
    assert l0.subs({Y: 1, U: 1, V: 1, Z: 1}) == 0
    assert l2b.subs({Y: 1, U: 1, V: 1, Z: 1}) == 0

    m1, m2 = two_zero_equations()
    g1 = sp.Poly(sp.expand(Y * Z * m1), Y, V, Z, domain=sp.QQ)
    g2 = sp.Poly(sp.expand(V * Z * m2), Y, V, Z, domain=sp.QQ)
    assert sp.gcd(g1, g2).total_degree() == 0
    assert m1.subs({Y: 1, V: 1, Z: 1}) == 0
    assert m2.subs({Y: 1, V: 1, Z: 1}) == 0

    print("fixed torus equations: cleared gcd=1 and properness controls: OK")


def edge_laurent(a: int, b: int) -> sp.Expr:
    return x**a + x**-a + x**b + x**-b - 2 * x - 2 * x**-1


def exact_zero(expr: sp.Expr) -> bool:
    numerator, _denominator = sp.fraction(sp.cancel(expr))
    return sp.expand(numerator) == 0


def pullback_checks() -> None:
    l1, l2 = interior_equations()
    a, b, c, d = 8, 26, 9, 10
    pull1 = l1.subs({X: x**a, Y: x**b, U: x**c, V: x**d, Z: x})
    pull2 = l2.subs({X: x**a, Y: x**b, U: x**c, V: x**d, Z: x})
    assert exact_zero(pull1 - edge_laurent(a, b))
    assert exact_zero(pull2 - edge_laurent(c, d))

    l0, l2b = one_zero_equations()
    b, c, d = 7, 8, 11
    pull0 = l0.subs({Y: x**b, U: x**c, V: x**d, Z: x})
    pull2b = l2b.subs({Y: x**b, U: x**c, V: x**d, Z: x})
    assert exact_zero(pull0 - edge_laurent(0, b))
    assert exact_zero(pull2b - edge_laurent(c, d))

    m1, m2 = two_zero_equations()
    b, d = 7, 11
    pullm1 = m1.subs({Y: x**b, V: x**d, Z: x})
    pullm2 = m2.subs({Y: x**b, V: x**d, Z: x})
    assert exact_zero(pullm1 - edge_laurent(0, b))
    assert exact_zero(pullm2 - edge_laurent(0, d))

    print("quotient-torus pullbacks for interior/one-zero/two-zero patterns: OK")


def main() -> None:
    cleared_coprime_checks()
    pullback_checks()
    print("cayley inverse sparse unlikely-intersection geometry regression: OK")


if __name__ == "__main__":
    main()
