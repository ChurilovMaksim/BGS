#!/usr/bin/env python3
"""Exact regression for cayley_inverse_pair_sum_factorization.md.

For r=-1, construct F(X)=P(tau+X), the shift resultant

    R(Z)=Res_X(F(X),F(Z-X)),

remove the diagonal factor D(Z)=2^m F(Z/2), recover the monic square root
S(Z) exactly in Z[tau][Z], and contract the two-scalar ideal (S(0),S'(0))
to Z with Smith normal form.

The default anchors K=7,11,13 are suitable for CI.  --extended adds K=17;
that full resultant is intentionally slower and is not part of the quick gate.
"""
from __future__ import annotations

import argparse

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

from cayley_product_row_reflection import even_odd_pair
from cayley_product_row_real_trace_ideal import TAU, reduce_real, strip_2K

X, Z, Y = sp.symbols("X Z Y")


def reduce_real_q(expr: sp.Expr, modulus: sp.Poly) -> sp.Expr:
    """Canonical reduction in Q[tau]/(C_K), used during square extraction."""
    return sp.Poly(sp.expand(expr), TAU, domain=sp.QQ).rem(
        sp.Poly(modulus.as_expr(), TAU, domain=sp.QQ)
    ).as_expr()


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
    """Polynomial division in (Z[tau]/C_K)[Z] for a monic denominator."""
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
    """Recover the unique monic square root in Q[tau]/C_K and prove integrality."""
    assert square.degree() % 2 == 0 and square.LC() == 1
    n = square.degree() // 2
    coeffs = [sp.Integer(0)] * (n + 1)
    coeffs[n] = sp.Integer(1)

    def qcoeff(degree: int) -> sp.Expr:
        return reduce_real_q(square.nth(degree), modulus)

    # Determine coefficients from the top down.  At degree n+k the only
    # still-unknown contribution is 2*s_k*s_n=2*s_k.
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
        coeffs[k] = reduce_real_q((qcoeff(degree) - known) / 2, modulus)

    root_expr = sp.expand(sum(coeffs[k] * Z**k for k in range(n + 1)))

    # The universal pair-sum theorem predicts an integral square root. Verify
    # that the reconstructed rational coefficients actually lie in Z[tau].
    integral_expr = sp.Integer(0)
    for (degree,), coeff in sp.Poly(root_expr, Z).terms():
        reduced = sp.Poly(reduce_real_q(coeff, modulus), TAU, domain=sp.QQ)
        assert all(c.q == 1 for c in reduced.all_coeffs()), (degree, reduced)
        integral_expr += sp.Poly(
            reduced.as_expr(), TAU, domain=sp.ZZ
        ).as_expr() * Z**degree

    root = reduce_z_polynomial(integral_expr, modulus)
    difference = sp.Poly(sp.expand(square.as_expr() - root.as_expr() ** 2), Z)
    for (degree,), coeff in difference.terms():
        assert reduce_real_q(coeff, modulus) == 0, (degree, coeff)
    return root


def contract_two_scalar_ideal(
    modulus: sp.Poly,
    s0: sp.Expr,
    s1: sp.Expr,
) -> tuple[int, list[int]]:
    m = modulus.degree()
    columns: list[sp.Matrix] = []
    for generator in (s0, s1):
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


def pair_sum_data(K: int) -> tuple[int, int, int, int]:
    modulus, E, O = even_odd_pair(K)

    # Reconstruct F(X)=E(X^2)+X O(X^2).
    F = sp.Poly(
        sp.expand(E.as_expr().subs(Y, X**2) + X * O.as_expr().subs(Y, X**2)),
        X,
    )
    m = (K - 1) // 2
    assert F.degree() == m and F.LC() == 1

    resultant_raw = sp.resultant(
        F.as_expr(),
        F.as_expr().subs(X, Z - X),
        X,
    )
    resultant = reduce_z_polynomial(resultant_raw, modulus)
    assert resultant.degree() == m * m and resultant.LC() == 1

    diagonal = reduce_z_polynomial(
        2**m * F.as_expr().subs(X, Z / 2), modulus
    )
    quotient, remainder = divide_by_monic_mod_c(resultant, diagonal, modulus)
    assert remainder.is_zero

    pair_sum = monic_square_root_mod_c(quotient, modulus)
    expected_degree = m * (m - 1) // 2
    assert pair_sum.degree() == expected_degree and pair_sum.LC() == 1

    # Verify the full factorization once more after reconstructing S.
    factorization_error = sp.Poly(
        sp.expand(
            resultant.as_expr()
            - diagonal.as_expr() * pair_sum.as_expr() ** 2
        ),
        Z,
    )
    for (degree,), coeff in factorization_error.terms():
        assert reduce_real_q(coeff, modulus) == 0, (degree, coeff)

    # The constant pair-sum coefficient equals +-Res(E,O).
    res_eo = reduce_real(sp.resultant(E.as_expr(), O.as_expr(), Y), modulus)
    s0 = reduce_real(pair_sum.nth(0), modulus)
    s1 = reduce_real(pair_sum.nth(1), modulus)
    assert reduce_real(s0**2 - res_eo**2, modulus) == 0

    full, invariants = contract_two_scalar_ideal(modulus, s0, s1)
    return full, strip_2K(full, K), expected_degree, len(invariants)


def check_anchor(K: int, expected_full: int, expected_stripped: int) -> None:
    full, stripped, degree, smith_rank = pair_sum_data(K)
    assert full == expected_full, (K, full, expected_full)
    assert stripped == expected_stripped, (K, stripped, expected_stripped)
    print(
        f"K={K:2d} degS={degree:2d} Theta={full} "
        f"Theta'={stripped} smith_rank={smith_rank}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--extended", action="store_true")
    args = parser.parse_args()

    for K, full, stripped in (
        (7, 7, 1),
        (11, 11**2, 1),
        (13, 5 * 13**3, 5),
    ):
        check_anchor(K, full, stripped)

    if args.extended:
        check_anchor(17, 17**4, 1)

    print("cayley inverse pair-sum factorization regression: OK")


if __name__ == "__main__":
    main()
