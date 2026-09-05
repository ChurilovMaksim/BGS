#!/usr/bin/env python3
"""Exact finite regression for cayley_inverse_reduced_resultant_filter.md.

The universal scalar implication is proved in the mathematics note.  This file
checks finite consequences only:
  * exhaustive gcd factors are support-free for K=31,37,41,43;
  * all distinct K=31 gcd factors lift to products of cyclotomic polynomials;
  * calibrated cross-class and structural ordinary resultants factor as recorded;
  * reciprocal z-lifts have resultant equal to the square of the real-trace
    resultant on the displayed anchors.
"""
from __future__ import annotations

from functools import lru_cache

import sympy as sp

from cayley_inverse_structural_associates import (
    T,
    real_cyclotomic_polynomial,
    v_polynomial,
)

Z = sp.symbols("Z")


@lru_cache(maxsize=None)
def edge_polynomial(a: int, b: int) -> sp.Poly:
    assert 0 <= a < b and a != 1 and b != 1
    return sp.Poly(
        2 - v_polynomial(a).as_expr() - v_polynomial(b).as_expr(),
        T,
        domain=sp.ZZ,
    )


def valid_edges(K: int) -> list[tuple[int, int]]:
    assert sp.isprime(K) and K >= 7 and K % 2 == 1
    m = (K - 1) // 2
    vertices = [a for a in range(m + 1) if a != 1]
    return [
        (a, b)
        for i, a in enumerate(vertices)
        for b in vertices[i + 1 :]
    ]


def monic_gcd(A: sp.Poly, B: sp.Poly) -> sp.Poly:
    G = sp.gcd(A, B)
    if G.degree() <= 0:
        return sp.Poly(1, T, domain=sp.ZZ)
    # Every maintained edge polynomial is primitive with leading coefficient
    # +-1, so Gauss's lemma makes the monic gcd integral.
    G = G.monic()
    assert all(c.q == 1 for c in G.all_coeffs())
    return sp.Poly(G.as_expr(), T, domain=sp.ZZ)


def support_free_gcd_audit(K: int) -> tuple[int, int, int, set[tuple[int, ...]]]:
    C = real_cyclotomic_polynomial(K)
    edges = valid_edges(K)
    polys = {e: edge_polynomial(*e) for e in edges}
    nonconstant = 0
    max_degree = 0
    distinct: set[tuple[int, ...]] = set()

    for i, e in enumerate(edges):
        for f in edges[i + 1 :]:
            G = monic_gcd(polys[e], polys[f])
            if G.degree() == 0:
                continue
            nonconstant += 1
            max_degree = max(max_degree, G.degree())
            distinct.add(tuple(int(c) for c in G.all_coeffs()))
            r = abs(int(sp.resultant(C.as_expr(), G.as_expr(), T)))
            assert r == 1, (K, e, f, G.as_expr(), r)

    pair_count = len(edges) * (len(edges) - 1) // 2
    print(
        f"K={K}: edges={len(edges)} pairs={pair_count} "
        f"nonconstant_gcd_pairs={nonconstant} max_gcd_degree={max_degree}: "
        "all |Res(C_K,G)|=1"
    )
    return len(edges), nonconstant, max_degree, distinct


def reciprocal_lift(G: sp.Poly) -> sp.Poly:
    d = G.degree()
    expr = sp.expand(Z**d * G.as_expr().subs(T, Z + Z**-1))
    return sp.Poly(expr, Z, domain=sp.ZZ)


def cyclotomic_coefficient_map(limit: int) -> dict[tuple[int, ...], int]:
    out: dict[tuple[int, ...], int] = {}
    for n in range(1, limit + 1):
        P = sp.Poly(sp.cyclotomic_poly(n, Z), Z, domain=sp.ZZ)
        out[tuple(int(c) for c in P.all_coeffs())] = n
    return out


def check_k31_gcds_are_torsion_factors(
    distinct_gcds: set[tuple[int, ...]],
) -> None:
    cyclotomic = cyclotomic_coefficient_map(4 * 31)
    orders_seen: set[int] = set()

    for coeffs in distinct_gcds:
        G = sp.Poly.from_list(list(coeffs), gens=T, domain=sp.ZZ)
        L = reciprocal_lift(G)
        unit, factors = sp.factor_list(L.as_expr())
        assert abs(int(unit)) == 1
        for factor, exponent in factors:
            F = sp.Poly(factor, Z, domain=sp.ZZ)
            if F.LC() == -1:
                F = -F
            key = tuple(int(c) for c in F.all_coeffs())
            assert key in cyclotomic, (G.as_expr(), F.as_expr())
            orders_seen.add(cyclotomic[key])
            assert exponent >= 1

    assert len(distinct_gcds) == 15, len(distinct_gcds)
    assert max(orders_seen) <= 8, orders_seen
    print(
        "K=31: all 15 distinct nonconstant gcds lift to products of "
        f"cyclotomic polynomials; orders={sorted(orders_seen)}"
    )


def factor_dict(n: int) -> dict[int, int]:
    return {int(p): int(e) for p, e in sp.factorint(abs(int(n))).items()}


def real_resultant(e: tuple[int, int], f: tuple[int, int]) -> int:
    A = edge_polynomial(*e)
    B = edge_polynomial(*f)
    G = monic_gcd(A, B)
    assert G.degree() == 0, (e, f, G.as_expr())
    return abs(int(sp.resultant(A.as_expr(), B.as_expr(), T)))


def reciprocal_resultant(e: tuple[int, int], f: tuple[int, int]) -> int:
    A = reciprocal_lift(edge_polynomial(*e))
    B = reciprocal_lift(edge_polynomial(*f))
    return abs(int(sp.resultant(A.as_expr(), B.as_expr(), Z)))


def check_resultant_anchor(
    K: int,
    e: tuple[int, int],
    f: tuple[int, int],
    expected_factors: dict[int, int],
    label: str,
) -> None:
    R = real_resultant(e, f)
    factors = factor_dict(R)
    assert factors == expected_factors, (K, e, f, factors, expected_factors)

    Rz = reciprocal_resultant(e, f)
    assert Rz == R * R, (K, e, f, R, Rz)
    print(
        f"K={K:3d} {label}: e={e} f={f} "
        f"Res_T={R} factors={factors}; reciprocal Res_Z=Res_T^2: OK"
    )


def main() -> None:
    _, n31, _, distinct31 = support_free_gcd_audit(31)
    assert n31 == 1283
    check_k31_gcds_are_torsion_factors(distinct31)

    support_free_gcd_audit(37)
    support_free_gcd_audit(41)
    support_free_gcd_audit(43)

    check_resultant_anchor(
        59,
        (8, 26),
        (9, 10),
        {283: 1, 21713: 1},
        "cross-class",
    )
    check_resultant_anchor(
        73,
        (2, 3),
        (8, 34),
        {13: 2, 6571: 1, 19301: 1},
        "cross-class",
    )
    check_resultant_anchor(
        97,
        (4, 13),
        (22, 30),
        {23: 1, 443: 1, 69259: 1},
        "cross-class",
    )
    check_resultant_anchor(
        89,
        (16, 35),
        (20, 33),
        {143207231: 1},
        "structural associate",
    )
    check_resultant_anchor(
        229,
        (44, 91),
        (48, 89),
        {33893: 1, 966684838398077: 1},
        "large structural associate",
    )

    print("cayley inverse reduced resultant filter regression: OK")


if __name__ == "__main__":
    main()
