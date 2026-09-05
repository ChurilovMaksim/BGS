#!/usr/bin/env python3
"""Finite exact regression for cayley_inverse_signature_torsion.md.

The universal theorem is proved in the mathematics note.  This script checks
its algebraic identities and the exact K=31 census/support-free anchors.
"""
from __future__ import annotations

from itertools import combinations

import sympy as sp

from cayley_inverse_structural_associates import (
    T,
    real_cyclotomic_polynomial,
    trace_polynomial,
    v_polynomial,
)

Y = sp.symbols("Y")


def q(n: int) -> sp.Expr:
    return Y**n + Y**-n


def edge_polynomial(a: int, b: int) -> sp.Poly:
    assert 0 <= a < b and a != 1 and b != 1
    return sp.Poly(
        2 - v_polynomial(a).as_expr() - v_polynomial(b).as_expr(),
        T,
        domain=sp.ZZ,
    )


def signature(edge: tuple[int, int]) -> frozenset[int]:
    a, b = edge
    return frozenset((a + b, b - a))


def check_half_angle_identity(max_index: int = 24) -> None:
    for a in range(max_index + 1):
        if a == 1:
            continue
        for b in range(a + 1, max_index + 1):
            if b == 1:
                continue
            lhs = sp.expand(
                trace_polynomial(a).as_expr().subs(T, Y**2 + Y**-2)
                + trace_polynomial(b).as_expr().subs(T, Y**2 + Y**-2)
            )
            rhs = sp.expand(q(a + b) * q(b - a))
            numerator, _ = sp.fraction(sp.cancel(lhs - rhs))
            assert sp.expand(numerator) == 0, (a, b)
    print(f"half-angle product identity through index {max_index}: OK")


def check_trace_equality_factorization(max_index: int = 24) -> None:
    for r in range(1, max_index + 1):
        for s in range(1, r):
            lhs = sp.expand(Y**r * (q(r) - q(s)))
            rhs = sp.expand((Y ** (r - s) - 1) * (Y ** (r + s) - 1))
            assert sp.expand(lhs - rhs) == 0, (r, s)
    print(f"q_r-q_s reciprocal factorization through index {max_index}: OK")


def check_k31_census() -> None:
    K = 31
    m = (K - 1) // 2
    vertices = [a for a in range(m + 1) if a != 1]
    edges = list(combinations(vertices, 2))
    polys = {e: edge_polynomial(*e) for e in edges}
    C = real_cyclotomic_polynomial(K)

    disjoint_nonconstant = 0
    signature_intersection = 0
    signature_disjoint = 0

    for i, e in enumerate(edges):
        for f in edges[i + 1 :]:
            if set(e) & set(f):
                continue
            G = sp.gcd(polys[e], polys[f])
            if G.degree() <= 0:
                continue
            disjoint_nonconstant += 1
            if signature(e) & signature(f):
                signature_intersection += 1
                resultant = abs(int(sp.resultant(C.as_expr(), G.as_expr(), T)))
                assert resultant == 1, (e, f, G.as_expr(), resultant)
            else:
                signature_disjoint += 1

    assert disjoint_nonconstant == 861
    assert signature_intersection == 255
    assert signature_disjoint == 606
    print(
        "K=31 disjoint nonconstant-gcd census: total=861, "
        "signature-intersection=255 (all |Res(C_K,G)|=1), "
        "signature-disjoint=606: OK"
    )


def main() -> None:
    check_half_angle_identity()
    check_trace_equality_factorization()
    check_k31_census()
    print("cayley inverse signature-torsion regression: OK")


if __name__ == "__main__":
    main()
