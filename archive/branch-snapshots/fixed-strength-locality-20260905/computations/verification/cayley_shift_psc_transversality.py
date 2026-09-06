#!/usr/bin/env python3
"""Exact regression for cayley_shift_psc_transversality.md.

Checks:
  1. generic exact monic polynomial examples verify the first nonzero shift
     coefficient against psc_d times the explicit reduced-resultant factors;
  2. split cyclotomic row examples verify that the first nonzero shift
     coefficient and first nonzero principal subresultant occur at the same
     gcd degree and differ by a nonzero residue-field unit.

The finite checks are regression only; the theorem is proved in the note.
"""
from __future__ import annotations

import sympy as sp

from cayley_product_row_real_trace_ideal import TAU, T, trace_cofactor_pair

Z = sp.symbols("Z")


def psc_at_gcd_degree(f: sp.Poly, g: sp.Poly, d: int) -> int | sp.Expr:
    subs = [sp.Poly(s, T, domain=f.domain) for s in sp.subresultants(f, g, T)]
    matches = [s for s in subs if s.degree() == d]
    assert matches, (d, [s.degree() for s in subs])
    return matches[-1].nth(d)


def check_generic_exact() -> None:
    examples = (
        # (G,A,B,psi)
        (
            T - 2,
            (T + 1) * (T + 3),
            (T + 4) * (T + 5),
            T**2 + T + 1,
        ),
        (
            (T - 1) * (T + 2),
            (T + 3) * (T + 5),
            (T + 4) * (T + 7),
            T**3 + 2 * T + 3,
        ),
        (
            (T - 1) * (T - 2) * (T + 1),
            T**2 + T + 5,
            T**2 + 3 * T + 7,
            T**2 + 2,
        ),
    )

    for G_expr, A_expr, B_expr, psi_expr in examples:
        G = sp.Poly(sp.expand(G_expr), T, domain=sp.ZZ)
        A = sp.Poly(sp.expand(A_expr), T, domain=sp.ZZ)
        B = sp.Poly(sp.expand(B_expr), T, domain=sp.ZZ)
        psi = sp.Poly(sp.expand(psi_expr), T, domain=sp.ZZ)
        f = sp.Poly(sp.expand(G.as_expr() * A.as_expr()), T, domain=sp.ZZ)
        g = sp.Poly(sp.expand(G.as_expr() * B.as_expr()), T, domain=sp.ZZ)
        assert f.LC() == g.LC() == G.LC() == A.LC() == B.LC() == 1
        assert sp.gcd(A, B).degree() == 0
        d = G.degree()

        R = sp.Poly(
            sp.resultant(
                f.as_expr(),
                g.as_expr() + Z * psi.as_expr(),
                T,
            ),
            Z,
            domain=sp.ZZ,
        )
        assert all(R.nth(j) == 0 for j in range(d))
        c_d = R.nth(d)
        assert c_d != 0

        psc_d = psc_at_gcd_degree(f, g, d)
        res_A_G = sp.resultant(A.as_expr(), G.as_expr(), T)
        res_G_psi = sp.resultant(G.as_expr(), psi.as_expr(), T)
        predicted_abs = sp.expand(psc_d * res_A_G * res_G_psi)
        assert sp.expand(c_d**2 - predicted_abs**2) == 0, (
            d,
            c_d,
            predicted_abs,
        )

    print("generic shift/PSC leading coefficient identity: OK")


def tau_embedding(K: int, p: int, embedding_power: int = 1) -> int:
    assert p % K == 1
    primitive = int(sp.primitive_root(p))
    assert 1 <= embedding_power < K
    zeta = pow(primitive, embedding_power * ((p - 1) // K), p)
    assert zeta != 1 and pow(zeta, K, p) == 1
    return (zeta + pow(zeta, -1, p)) % p


def eval_tau(expr: sp.Expr, tau: int, p: int) -> int:
    poly = sp.Poly(expr, TAU, domain=sp.ZZ)
    total = 0
    for (degree,), coefficient in poly.terms():
        total = (total + int(coefficient) * pow(tau, degree, p)) % p
    return total


def specialize(poly: sp.Poly, tau: int, p: int) -> sp.Poly:
    expr = sp.Integer(0)
    for (degree,), coefficient in poly.terms():
        expr += eval_tau(coefficient, tau, p) * T**degree
    return sp.Poly(expr, T, modulus=p)


def alpha_mod(K: int, r: int, tau: int, p: int) -> int:
    alpha_expr = sp.chebyshevu(r - 1, TAU / 2)
    # Chebyshev expression is integral after expansion for this substitution.
    alpha_expr = sp.Poly(sp.expand(alpha_expr), TAU, domain=sp.ZZ).as_expr()
    return eval_tau(alpha_expr, tau, p)


def check_split_row(K: int, p: int, r: int, expected_d: int | None = None, embedding_power: int = 1) -> int:
    modulus, P_raw, Q_raw = trace_cofactor_pair(K, r)
    del modulus
    tau = tau_embedding(K, p, embedding_power)
    P = specialize(P_raw, tau, p)
    Q = specialize(Q_raw, tau, p)
    d = sp.gcd(P, Q).degree()
    if expected_d is not None:
        assert d == expected_d, (K, p, r, d, expected_d)

    q_lc = int(Q.LC()) % p
    q_monic = sp.Poly(pow(q_lc, -1, p) * Q.as_expr(), T, modulus=p)
    assert q_monic.LC() % p == 1

    alpha = alpha_mod(K, r, tau, p)
    assert alpha % p != 0
    inv_alpha = pow(alpha, -1, p)

    # Q_Z(T), after fixed leading-coefficient normalization, is q(T+Z/alpha).
    q_shift = q_monic.as_expr().subs(T, T + inv_alpha * Z)
    resultant = sp.Poly(
        sp.resultant(P.as_expr(), q_shift, T),
        Z,
        modulus=p,
    )

    # The first nonzero Z coefficient is exactly at the gcd degree.
    assert all(int(resultant.nth(j)) % p == 0 for j in range(d))
    c_d = int(resultant.nth(d)) % p
    assert c_d != 0, (K, p, r, d)

    psc_d = int(psc_at_gcd_degree(P, q_monic, d)) % p
    assert psc_d != 0, (K, p, r, d)

    print(
        f"K={K:2d} p={p:4d} r={r:2d} embedding={embedding_power} tau={tau} gcd_degree={d} "
        f"c_d={c_d} psc_d={psc_d}: OK"
    )
    return d


def find_degree_one_anchor() -> tuple[int, int, int]:
    # Small deterministic scan only; all polynomials have degree <=6 here.
    for K in (7, 11, 13):
        for p in list(sp.primerange(K + 1, 600)):
            if p % K != 1:
                continue
            for r in range(2, K):
                modulus, P_raw, Q_raw = trace_cofactor_pair(K, r)
                del modulus
                tau = tau_embedding(K, p)
                P = specialize(P_raw, tau, p)
                Q = specialize(Q_raw, tau, p)
                if sp.gcd(P, Q).degree() == 1:
                    return K, p, r
    raise AssertionError("no small gcd-degree-one row anchor found")


def main() -> None:
    check_generic_exact()

    # Project-specific fixed anchors for degree 0 and inverse degrees 2/4.
    check_split_row(11, 23, 10, expected_d=0)
    check_split_row(7, 29, 6, expected_d=0)
    check_split_row(11, 23, 10, expected_d=2, embedding_power=2)
    check_split_row(23, 47, 22, expected_d=4)

    K, p, r = find_degree_one_anchor()
    d = check_split_row(K, p, r, expected_d=1)
    assert d == 1
    print(f"small degree-one row anchor discovered deterministically: K={K}, p={p}, r={r}")

    print("cayley shift/PSC transversality regression: OK")


if __name__ == "__main__":
    main()
