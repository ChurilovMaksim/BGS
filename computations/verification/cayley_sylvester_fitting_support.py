#!/usr/bin/env python3
"""Exact regression for cayley_sylvester_fitting_support.md.

The arithmetic representation remains the small PSC triple.  This verifier
checks the intrinsic linear-algebra statement behind it:

    nullity Sylv(P,Q) = deg gcd(P,Q),

and therefore order-three support is precisely the corank>=3/Fitting locus.
"""
from __future__ import annotations

import math
import sympy as sp

from cayley_product_row_real_trace_ideal import TAU, T, trace_cofactor_pair


def sylvester_map_matrix(P: sp.Poly, Q: sp.Poly) -> sp.Matrix:
    m = P.degree()
    assert Q.degree() == m
    cols: list[sp.Matrix] = []
    for base in (P, Q):
        for j in range(m):
            shifted = sp.Poly(T**j * base.as_expr(), T, domain=base.domain)
            cols.append(sp.Matrix([shifted.nth(k) for k in range(2 * m)]))
    return sp.Matrix.hstack(*cols)


def rank_mod_p(M: sp.Matrix, p: int) -> int:
    a = [[int(M[i, j]) % p for j in range(M.cols)] for i in range(M.rows)]
    rank = 0
    col = 0
    while rank < M.rows and col < M.cols:
        pivot = next((i for i in range(rank, M.rows) if a[i][col] % p), None)
        if pivot is None:
            col += 1
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, p)
        a[rank] = [(x * inv) % p for x in a[rank]]
        for i in range(M.rows):
            if i == rank:
                continue
            factor = a[i][col] % p
            if factor:
                a[i] = [
                    (a[i][j] - factor * a[rank][j]) % p
                    for j in range(M.cols)
                ]
        rank += 1
        col += 1
    return rank


def check_generic_kernel() -> None:
    examples = (
        ((T - 1), (T + 2) * (T + 3), (T + 4) * (T + 5)),
        ((T - 1) * (T + 2), (T + 3) * (T + 5), (T + 4) * (T + 7)),
        (
            (T - 1) * (T - 2) * (T + 1),
            T**2 + T + 5,
            T**2 + 3 * T + 7,
        ),
    )
    for G, A, B in examples:
        P = sp.Poly(sp.expand(G * A), T, domain=sp.QQ)
        Q = sp.Poly(sp.expand(G * B), T, domain=sp.QQ)
        assert P.degree() == Q.degree()
        g = sp.gcd(P, Q).degree()
        M = sylvester_map_matrix(P, Q)
        nullity = M.cols - M.rank()
        assert nullity == g

        n = M.rows
        compound_rank = math.comb(M.rank(), n - 2) if M.rank() >= n - 2 else 0
        assert (compound_rank == 0) == (g >= 3)
    print("generic Sylvester nullity/Fitting criterion: OK")


def tau_embedding(K: int, p: int, embedding_power: int = 1) -> int:
    assert p % K == 1
    primitive = int(sp.primitive_root(p))
    assert 1 <= embedding_power < K
    zeta = pow(primitive, embedding_power * ((p - 1) // K), p)
    return (zeta + pow(zeta, -1, p)) % p


def eval_tau(expr: sp.Expr, tau: int, p: int) -> int:
    poly = sp.Poly(expr, TAU, domain=sp.ZZ)
    return sum(
        int(c) * pow(tau, d, p) for (d,), c in poly.terms()
    ) % p


def specialize(poly: sp.Poly, tau: int, p: int) -> sp.Poly:
    expr = sum(
        eval_tau(c, tau, p) * T**d for (d,), c in poly.terms()
    )
    return sp.Poly(expr, T, modulus=p)


def first_pscs(P: sp.Poly, Q: sp.Poly, count: int = 3) -> list[int]:
    seq = [sp.Poly(s, T, modulus=int(P.domain.mod)) for s in sp.subresultants(P, Q, T)]
    p = int(P.domain.mod)
    out: list[int] = []
    for j in range(count):
        matching = [s for s in seq if s.degree() == j]
        out.append(0 if not matching else int(matching[-1].nth(j)) % p)
    return out


def check_split_row(K: int, p: int, r: int, expected_g: int | None = None, embedding_power: int = 1) -> int:
    _, P0, Q0 = trace_cofactor_pair(K, r)
    tau = tau_embedding(K, p, embedding_power)
    P = specialize(P0, tau, p)
    Q = specialize(Q0, tau, p)
    g = sp.gcd(P, Q).degree()
    if expected_g is not None:
        assert g == expected_g, (K, p, r, g, expected_g)

    M = sylvester_map_matrix(P, Q)
    rank = rank_mod_p(M, p)
    nullity = 2 * P.degree() - rank
    assert nullity == g

    psc = first_pscs(P, Q)
    assert (all(x == 0 for x in psc)) == (g >= 3)

    n = M.rows
    compound_rank = math.comb(rank, n - 2) if rank >= n - 2 else 0
    assert (compound_rank == 0) == (g >= 3)
    print(
        f"K={K:2d} p={p:4d} r={r:2d} embedding={embedding_power} tau={tau} gcd={g} "
        f"rank={rank}/{n} psc012={psc}: OK"
    )
    return g


def find_degree_one_anchor() -> tuple[int, int, int]:
    for K in (7, 11, 13):
        for p in sp.primerange(K + 1, 600):
            if p % K != 1:
                continue
            tau = tau_embedding(K, p)
            for r in range(2, K):
                _, P0, Q0 = trace_cofactor_pair(K, r)
                P = specialize(P0, tau, p)
                Q = specialize(Q0, tau, p)
                if sp.gcd(P, Q).degree() == 1:
                    return K, p, r
    raise AssertionError("no small degree-one anchor found")


def main() -> None:
    check_generic_kernel()

    check_split_row(11, 23, 10, expected_g=0)
    K, p, r = find_degree_one_anchor()
    check_split_row(K, p, r, expected_g=1)
    check_split_row(7, 29, 6, expected_g=0)
    check_split_row(11, 23, 10, expected_g=2, embedding_power=2)
    check_split_row(23, 47, 22, expected_g=4)

    print("cayley Sylvester/Fitting support regression: OK")


if __name__ == "__main__":
    main()
