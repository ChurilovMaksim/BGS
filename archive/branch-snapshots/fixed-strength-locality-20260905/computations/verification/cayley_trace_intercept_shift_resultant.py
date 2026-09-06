#!/usr/bin/env python3
"""Exact finite regression for cayley_trace_intercept_rigidity.md.

For a normalized row ratio r this script forms the scalar shift-resultant

    R_{K,r}(Z) = Res_T(P_1(T), R_r(alpha_r*T + beta_r + Z)),

extracts c_0,c_1,c_2, contracts their ideal from Z[tau] to Z by Smith
normal form, and checks small anchors against the exact real-trace support.

The full resultant has Z-degree m^2 and becomes expensive as K grows.
The default anchors are deliberately small; finite regression is not the
proof of the universal shift-resultant criterion.
"""
from __future__ import annotations

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

TAU, T, U, Z = sp.symbols("TAU T U Z")


def real_cyclotomic_polynomial(K: int, var: sp.Symbol = T) -> sp.Poly:
    assert K >= 7 and K % 2 == 1
    m = (K - 1) // 2
    expr = sp.Integer(1) + 2 * sum(
        sp.chebyshevt(a, var / 2) for a in range(1, m + 1)
    )
    poly = sp.Poly(sp.expand(expr), var, domain=sp.ZZ)
    assert poly.degree() == m and poly.LC() == 1
    return poly


def coefficient_modulus(K: int) -> sp.Poly:
    return sp.Poly(
        real_cyclotomic_polynomial(K).as_expr().subs(T, TAU),
        TAU,
        domain=sp.ZZ,
    )


def reduce_real(expr: sp.Expr, modulus: sp.Poly) -> sp.Expr:
    return sp.Poly(sp.expand(expr), TAU, domain=sp.ZZ).rem(modulus).as_expr()


def reduce_multivar(
    expr: sp.Expr, modulus: sp.Poly, *variables: sp.Symbol
) -> sp.Expr:
    poly = sp.Poly(sp.expand(expr), *variables)
    out = sp.Integer(0)
    for exponents, coefficient in poly.terms():
        term = reduce_real(coefficient, modulus)
        for variable, exponent in zip(variables, exponents):
            term *= variable**exponent
        out += term
    return sp.expand(out)


def synthetic_divide(
    poly_expr: sp.Expr,
    variable: sp.Symbol,
    root: sp.Expr,
    modulus: sp.Poly,
) -> sp.Expr:
    """Divide a monic O^+[variable] polynomial known to vanish at root."""
    poly = sp.Poly(sp.expand(poly_expr), variable)
    degree = poly.degree()
    coefficients = [sp.Integer(0)] * (degree + 1)
    for (exponent,), coefficient in poly.terms():
        coefficients[exponent] = reduce_real(coefficient, modulus)

    quotient = [sp.Integer(0)] * degree
    quotient[degree - 1] = coefficients[degree]
    for j in range(degree - 1, 0, -1):
        quotient[j - 1] = reduce_real(
            coefficients[j] + root * quotient[j], modulus
        )

    remainder = reduce_real(coefficients[0] + root * quotient[0], modulus)
    assert sp.expand(remainder) == 0
    return sp.expand(
        sum(quotient[j] * variable**j for j in range(degree))
    )


def shift_resultant_coefficients(
    K: int, r: int
) -> tuple[sp.Poly, list[sp.Expr], int]:
    modulus = coefficient_modulus(K)
    C = real_cyclotomic_polynomial(K).as_expr()
    H_T = sp.expand((T - 2) * C)

    source = synthetic_divide(H_T, T, TAU, modulus)

    alpha = reduce_real(sp.chebyshevu(r - 1, TAU / 2), modulus)
    beta = reduce_real(-2 * sp.chebyshevu(r - 2, TAU / 2), modulus)
    target_trace = reduce_real(2 * sp.chebyshevt(r, TAU / 2), modulus)
    assert reduce_real(alpha * TAU + beta - target_trace, modulus) == 0

    H_U = H_T.subs(T, U)
    target_valid = synthetic_divide(H_U, U, target_trace, modulus)
    shifted_target = reduce_multivar(
        target_valid.subs(U, alpha * T + beta + Z),
        modulus,
        T,
        Z,
    )

    m = (K - 1) // 2
    assert sp.Poly(source, T).degree() == m
    assert sp.Poly(shifted_target, T, Z).degree(T) == m
    assert sp.Poly(shifted_target, T, Z).degree(Z) == m

    resultant = sp.resultant(source, shifted_target, T)
    resultant = reduce_multivar(resultant, modulus, Z)
    resultant_poly = sp.Poly(resultant, Z)
    assert resultant_poly.degree() == m * m

    coefficients = [
        reduce_real(resultant_poly.nth(j), modulus) for j in range(3)
    ]
    assert coefficients[0] != 0
    return modulus, coefficients, resultant_poly.degree()


def ideal_contraction_exponent(
    K: int, modulus: sp.Poly, generators: list[sp.Expr]
) -> tuple[int, list[int]]:
    m = (K - 1) // 2
    columns: list[sp.Matrix] = []
    for generator in generators:
        for j in range(m):
            reduced = sp.Poly(
                reduce_real(generator * TAU**j, modulus),
                TAU,
                domain=sp.ZZ,
            )
            columns.append(
                sp.Matrix([int(reduced.nth(k)) for k in range(m)])
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
    return invariants[-1], invariants


def strip_2K(n: int, K: int) -> int:
    n = abs(int(n))
    for q in (2, K):
        while n and n % q == 0:
            n //= q
    return n


def check_anchor(
    K: int,
    r: int,
    expected_full: int,
    expected_stripped: int,
) -> None:
    modulus, coefficients, degree_z = shift_resultant_coefficients(K, r)
    full, invariants = ideal_contraction_exponent(K, modulus, coefficients)
    stripped = strip_2K(full, K)
    assert full == expected_full, (K, r, full, expected_full)
    assert stripped == expected_stripped, (
        K,
        r,
        stripped,
        expected_stripped,
    )
    print(
        f"K={K:2d} r={r:2d} degZ={degree_z:2d} "
        f"Omega3={full} Omega3'={stripped} "
        f"smith_rank={len(invariants)}"
    )


def main() -> None:
    for K, r, full, stripped in (
        (7, 2, 7**3, 1),
        (11, 7, 11**5, 1),
        (13, 3, 13**6, 1),
        (13, 12, 2**4 * 5**2 * 13**6, 5**2),
    ):
        check_anchor(K, r, full, stripped)

    print("cayley trace-intercept shift-resultant regression: OK")


if __name__ == "__main__":
    main()
