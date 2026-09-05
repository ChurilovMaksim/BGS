#!/usr/bin/env python3
"""Exact regression for cayley_inverse_resultant_transversality.md.

Checks:
  1. the universal simple-common-root directional derivative formula over Z;
  2. the inverse translation specialization;
  3. exact finite-field trichotomy deg gcd(E,O)=0,1,2 on cyclotomic anchors.

Finite checks are regression only; the universal statements are proved in the
mathematics note.
"""
from __future__ import annotations

import sympy as sp

from cayley_product_row_reflection import even_odd_pair
from cayley_product_row_real_trace_ideal import TAU

Y, t = sp.symbols("Y t")


def check_universal_derivative() -> None:
    cases = (
        (
            2,
            (Y + 1) * (Y + 3),
            Y + 4,
            Y + 2,
            Y**2 + 1,
        ),
        (
            1,
            2 * (Y + 3),
            3 * (Y + 5),
            Y**2 + 2,
            2 * Y + 1,
        ),
        (
            -1,
            (Y + 2) * (Y**2 + Y + 3),
            5 * (Y + 4) * (Y + 6),
            3 * Y + 2,
            Y**3 + 1,
        ),
    )

    for y, A, B, phi, psi in cases:
        f = sp.expand((Y - y) * A)
        g = sp.expand((Y - y) * B)
        direct = sp.expand(
            sp.diff(sp.resultant(f + t * phi, g + t * psi, Y), t).subs(t, 0)
        )
        predicted = sp.expand(
            (-1) ** (sp.degree(f, Y) - 1)
            * sp.resultant(A, B, Y)
            * (
                sp.diff(f, Y).subs(Y, y) * psi.subs(Y, y)
                - sp.diff(g, Y).subs(Y, y) * phi.subs(Y, y)
            )
        )
        assert sp.expand(direct - predicted) == 0

    print("generic simple-common-root resultant derivative: OK")


def check_inverse_specialization() -> None:
    for y in (1, 2, 3):
        A = (Y + 2) * (Y + 5)
        B = Y + 7
        E = sp.expand((Y - y) * A)
        O = sp.expand((Y - y) * B)
        phi = sp.expand((O + 2 * Y * sp.diff(O, Y)) / 2)
        psi = sp.diff(E, Y)

        direct = sp.expand(
            sp.diff(sp.resultant(E + t * phi, O + t * psi, Y), t).subs(t, 0)
        )
        predicted = sp.expand(
            (-1) ** (sp.degree(E, Y) - 1)
            * sp.resultant(A, B, Y)
            * (
                sp.diff(E, Y).subs(Y, y) ** 2
                - y * sp.diff(O, Y).subs(Y, y) ** 2
            )
        )
        assert sp.expand(direct - predicted) == 0

    print("generic inverse translation derivative specialization: OK")


def tau_embedding(K: int, p: int) -> int:
    assert p % K == 1
    generator = int(sp.primitive_root(p))
    zeta = pow(generator, (p - 1) // K, p)
    assert zeta != 1 and pow(zeta, K, p) == 1
    return (zeta + pow(zeta, -1, p)) % p


def eval_tau_coefficient(expr: sp.Expr, tau: int, p: int) -> int:
    poly = sp.Poly(expr, TAU, domain=sp.ZZ)
    value = 0
    for (degree,), coefficient in poly.terms():
        value = (value + int(coefficient) * pow(tau, degree, p)) % p
    return value


def specialize_poly(poly: sp.Poly, tau: int, p: int) -> sp.Poly:
    expr = sp.Integer(0)
    for (degree,), coefficient in poly.terms():
        expr += eval_tau_coefficient(coefficient, tau, p) * Y**degree
    return sp.Poly(expr, Y, modulus=p)


def directional_resultant_coefficients(
    E: sp.Poly,
    O: sp.Poly,
    p: int,
) -> tuple[int, int]:
    inv2 = pow(2, -1, p)
    phi = sp.Poly(
        inv2 * (O.as_expr() + 2 * Y * sp.diff(O.as_expr(), Y)),
        Y,
        modulus=p,
    )
    psi = sp.Poly(sp.diff(E.as_expr(), Y), Y, modulus=p)
    resultant = sp.Poly(
        sp.resultant(
            E.as_expr() + t * phi.as_expr(),
            O.as_expr() + t * psi.as_expr(),
            Y,
        ),
        t,
        modulus=p,
    )
    return int(resultant.nth(0)) % p, int(resultant.nth(1)) % p


def unique_linear_root(poly: sp.Poly, p: int) -> int:
    assert poly.degree() == 1
    a = int(poly.nth(1)) % p
    b = int(poly.nth(0)) % p
    return (-b * pow(a, -1, p)) % p


def check_finite_anchor(K: int, p: int, expected_gcd_degree: int) -> None:
    modulus, E_raw, O_raw = even_odd_pair(K)
    del modulus
    tau = tau_embedding(K, p)
    E = specialize_poly(E_raw, tau, p)
    O = specialize_poly(O_raw, tau, p)
    gcd = sp.gcd(E, O)
    degree = gcd.degree()
    assert degree == expected_gcd_degree, (K, p, degree, expected_gcd_degree)

    rho0, rho1 = directional_resultant_coefficients(E, O, p)

    if degree == 0:
        assert rho0 != 0
    elif degree == 1:
        assert rho0 == 0 and rho1 != 0
        y = unique_linear_root(gcd, p)
        divisor = sp.Poly(Y - y, Y, modulus=p)
        A, remA = sp.div(E, divisor, domain=sp.GF(p))
        B, remB = sp.div(O, divisor, domain=sp.GF(p))
        assert remA.is_zero and remB.is_zero
        res_ab = int(sp.resultant(A.as_expr(), B.as_expr(), Y)) % p
        e_prime = int(sp.Poly(sp.diff(E.as_expr(), Y), Y, modulus=p).eval(y)) % p
        o_prime = int(sp.Poly(sp.diff(O.as_expr(), Y), Y, modulus=p).eval(y)) % p
        predicted = (
            (-1) ** (E.degree() - 1)
            * res_ab
            * (e_prime * e_prime - y * o_prime * o_prime)
        ) % p
        assert rho1 == predicted, (K, p, rho1, predicted)
    else:
        assert rho0 == 0 and rho1 == 0

    print(
        f"K={K:2d} p={p:4d} deg_gcd={degree} "
        f"rho0={rho0} rho1={rho1}: OK"
    )


def main() -> None:
    check_universal_derivative()
    check_inverse_specialization()

    # Exact split finite-field trichotomy.
    check_finite_anchor(11, 23, 0)
    check_finite_anchor(7, 29, 1)
    check_finite_anchor(23, 47, 2)

    print("cayley inverse resultant transversality regression: OK")


if __name__ == "__main__":
    main()
