#!/usr/bin/env python3
"""Exact regression for cayley_inverse_pair_sum_factorization.md.

Two mechanisms are checked.

1. Small K: form the full inverse shift resultant

       R(Z)=Res_X(F(X),F(Z-X)),

   divide by D(Z)=2^m F(Z/2), recover the monic square root S(Z), and
   verify R=D*S^2.

2. Scalable path: translate only to first order,

       F(X+eps/2)=E_eps(X^2)+X O_eps(X^2),  eps^2=0,

   and compute rho_0,rho_1 from Res(E_eps,O_eps).  These are +-S(0),+-S'(0).
   Contract the two-scalar ideal by Smith normal form.

The default gate checks the full factorization through K=13 and the much
cheaper translated-resultant support through K=23.  --extended-full also runs
the old full-resultant route at K=17.
"""
from __future__ import annotations

import argparse

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

from cayley_product_row_reflection import even_odd_pair
from cayley_product_row_real_trace_ideal import TAU, reduce_real, strip_2K

X, Z, Y = sp.symbols("X Z Y")


def reduce_real_q(expr: sp.Expr, modulus: sp.Poly) -> sp.Expr:
    return sp.Poly(sp.expand(expr), TAU, domain=sp.QQ).rem(
        sp.Poly(modulus.as_expr(), TAU, domain=sp.QQ)
    ).as_expr()


def integral_real(expr: sp.Expr, modulus: sp.Poly) -> sp.Expr:
    reduced = sp.Poly(reduce_real_q(expr, modulus), TAU, domain=sp.QQ)
    assert all(c.q == 1 for c in reduced.all_coeffs()), reduced
    return sp.Poly(reduced.as_expr(), TAU, domain=sp.ZZ).as_expr()


def reduce_z_polynomial(expr: sp.Expr, modulus: sp.Poly) -> sp.Poly:
    poly = sp.Poly(sp.expand(expr), Z)
    reduced = sum(
        reduce_real(coeff, modulus) * Z**degree
        for (degree,), coeff in poly.terms()
    )
    return sp.Poly(sp.expand(reduced), Z)


def divide_by_monic_mod_c(
    numerator: sp.Poly,
    denominator: sp.Poly,
    modulus: sp.Poly,
) -> tuple[sp.Poly, sp.Poly]:
    denominator = reduce_z_polynomial(denominator.as_expr(), modulus)
    assert reduce_real(denominator.LC(), modulus) == 1
    remainder = reduce_z_polynomial(numerator.as_expr(), modulus)
    quotient_expr = sp.Integer(0)
    ddeg = denominator.degree()

    while not remainder.is_zero and remainder.degree() >= ddeg:
        shift = remainder.degree() - ddeg
        lc = reduce_real(remainder.LC(), modulus)
        term = lc * Z**shift
        quotient_expr = reduce_z_polynomial(
            quotient_expr + term, modulus
        ).as_expr()
        remainder = reduce_z_polynomial(
            remainder.as_expr() - term * denominator.as_expr(), modulus
        )

    return reduce_z_polynomial(quotient_expr, modulus), remainder


def monic_square_root_mod_c(square: sp.Poly, modulus: sp.Poly) -> sp.Poly:
    assert square.degree() % 2 == 0 and square.LC() == 1
    n = square.degree() // 2
    coeffs = [sp.Integer(0)] * (n + 1)
    coeffs[n] = sp.Integer(1)

    for k in range(n - 1, -1, -1):
        degree = n + k
        known = sp.Integer(0)
        for i in range(n + 1):
            j = degree - i
            if not (0 <= j <= n):
                continue
            if (i == k and j == n) or (i == n and j == k):
                continue
            known += coeffs[i] * coeffs[j]
        target = reduce_real_q(square.nth(degree), modulus)
        coeffs[k] = reduce_real_q((target - known) / 2, modulus)

    integral_expr = sp.Integer(0)
    for k, coeff in enumerate(coeffs):
        integral_expr += integral_real(coeff, modulus) * Z**k

    root = reduce_z_polynomial(integral_expr, modulus)
    error = sp.Poly(sp.expand(square.as_expr() - root.as_expr() ** 2), Z)
    for (degree,), coeff in error.terms():
        assert reduce_real_q(coeff, modulus) == 0, (degree, coeff)
    return root


def contract_two_scalar_ideal(
    modulus: sp.Poly,
    scalar0: sp.Expr,
    scalar1: sp.Expr,
) -> tuple[int, list[int]]:
    m = modulus.degree()
    columns: list[sp.Matrix] = []
    for generator in (scalar0, scalar1):
        generator = reduce_real(generator, modulus)
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


def full_pair_sum_scalars(K: int) -> tuple[sp.Poly, sp.Expr, sp.Expr, int]:
    modulus, E, O = even_odd_pair(K)
    F = sp.Poly(
        sp.expand(E.as_expr().subs(Y, X**2) + X * O.as_expr().subs(Y, X**2)),
        X,
    )
    m = (K - 1) // 2
    assert F.degree() == m and F.LC() == 1

    resultant = reduce_z_polynomial(
        sp.resultant(F.as_expr(), F.as_expr().subs(X, Z - X), X), modulus
    )
    assert resultant.degree() == m * m and resultant.LC() == 1

    diagonal = reduce_z_polynomial(2**m * F.as_expr().subs(X, Z / 2), modulus)
    quotient, remainder = divide_by_monic_mod_c(resultant, diagonal, modulus)
    assert remainder.is_zero

    pair_sum = monic_square_root_mod_c(quotient, modulus)
    expected_degree = m * (m - 1) // 2
    assert pair_sum.degree() == expected_degree and pair_sum.LC() == 1

    error = sp.Poly(
        sp.expand(
            resultant.as_expr() - diagonal.as_expr() * pair_sum.as_expr() ** 2
        ),
        Z,
    )
    for (degree,), coeff in error.terms():
        assert reduce_real_q(coeff, modulus) == 0, (degree, coeff)

    s0 = reduce_real(pair_sum.nth(0), modulus)
    s1 = reduce_real(pair_sum.nth(1), modulus)
    res_eo = reduce_real(sp.resultant(E.as_expr(), O.as_expr(), Y), modulus)
    assert reduce_real(s0**2 - res_eo**2, modulus) == 0
    return modulus, s0, s1, expected_degree


def translated_resultant_scalars(K: int) -> tuple[sp.Poly, sp.Expr, sp.Expr]:
    """Compute rho(0),rho'(0) from the half-degree translation resultant."""
    modulus, E, O = even_odd_pair(K)
    e = E.as_expr()
    o = O.as_expr()

    # F(X+Z/2)=F(X)+(Z/2)F'(X)+O(Z^2).
    # Even/odd parts of F'(X) are
    #   O(Y)+2Y O'(Y),  2 E'(Y),
    # hence the first-order deformations below.
    e_direction = sp.expand((o + 2 * Y * sp.diff(o, Y)) / 2)
    o_direction = sp.diff(e, Y)

    rho = sp.resultant(
        e + Z * e_direction,
        o + Z * o_direction,
        Y,
    )
    rho_poly = sp.Poly(sp.expand(rho), Z)
    rho0 = integral_real(rho_poly.nth(0), modulus)
    rho1 = integral_real(rho_poly.nth(1), modulus)
    return modulus, rho0, rho1


def check_full_factorization(K: int) -> None:
    modulus, s0, s1, degree = full_pair_sum_scalars(K)
    _, rho0, rho1 = translated_resultant_scalars(K)

    # The translated resultant equals the monic pair-sum polynomial up to one
    # global sign.  Check that the two low coefficient vectors are proportional
    # by the same sign without choosing a convention-dependent sign formula.
    assert reduce_real(s0**2 - rho0**2, modulus) == 0
    assert reduce_real(s0 * rho1 - s1 * rho0, modulus) == 0
    print(f"K={K:2d} full pair-sum factorization: degS={degree} OK")


def check_support_anchor(
    K: int,
    expected_full: int,
    expected_stripped: int,
) -> None:
    modulus, rho0, rho1 = translated_resultant_scalars(K)
    full, invariants = contract_two_scalar_ideal(modulus, rho0, rho1)
    stripped = strip_2K(full, K)
    assert full == expected_full, (K, full, expected_full)
    assert stripped == expected_stripped, (K, stripped, expected_stripped)
    print(
        f"K={K:2d} Theta={full} Theta'={stripped} "
        f"smith_rank={len(invariants)}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--extended-full", action="store_true")
    args = parser.parse_args()

    # Mechanistically direct full-resultant/square-root controls.
    for K in (7, 11, 13):
        check_full_factorization(K)
    if args.extended_full:
        check_full_factorization(17)

    # Faster half-degree translated-resultant controls.
    for K, full, stripped in (
        (7, 7, 1),
        (11, 11**2, 1),
        (13, 5 * 13**3, 5),
        (17, 17**4, 1),
        (19, 37 * 19**4, 37),
        (23, 23**6 * 47**2 * 137, 47**2 * 137),
    ):
        check_support_anchor(K, full, stripped)

    print("cayley inverse pair-sum factorization regression: OK")


if __name__ == "__main__":
    main()
