#!/usr/bin/env python3
"""Finite exact regression for cayley_inverse_shared_endpoint_torsion.md.

The universal torsion/support-free statements are proved in the mathematics
note.  This script checks project-specific polynomial identities and an
exhaustive K=31 shared-endpoint anchor.
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

Z = sp.symbols("Z")


def edge_polynomial(a: int, b: int) -> sp.Poly:
    assert 0 <= a < b and a != 1 and b != 1
    return sp.Poly(
        2 - v_polynomial(a).as_expr() - v_polynomial(b).as_expr(),
        T,
        domain=sp.ZZ,
    )


def check_trace_difference_factorization(max_index: int = 30) -> None:
    for c in range(max_index + 1):
        if c == 1:
            continue
        for b in range(c + 1, max_index + 1):
            if b == 1:
                continue
            lhs = sp.expand(
                Z**b
                * (
                    trace_polynomial(b).as_expr().subs(T, Z + Z**-1)
                    - trace_polynomial(c).as_expr().subs(T, Z + Z**-1)
                )
            )
            rhs = sp.expand((Z ** (b - c) - 1) * (Z ** (b + c) - 1))
            assert sp.expand(lhs - rhs) == 0, (b, c)
    print(f"trace-difference reciprocal factorization through index {max_index}: OK")


def check_removable_value(max_index: int = 40) -> None:
    for n in range(max_index + 1):
        value = int(v_polynomial(n).eval(2))
        assert value == n * n, (n, value)

    for a, b in combinations([i for i in range(max_index + 1) if i != 1], 2):
        value = int(edge_polynomial(a, b).eval(2))
        assert value == 2 - a * a - b * b
        assert value != 0, (a, b, value)
    print(f"v_n(2)=n^2 and valid edge T=2 exclusion through index {max_index}: OK")


def check_k31_shared_endpoint_support_free() -> None:
    K = 31
    m = (K - 1) // 2
    vertices = [a for a in range(m + 1) if a != 1]
    edges = list(combinations(vertices, 2))
    C = real_cyclotomic_polynomial(K)

    shared_pairs = 0
    nonconstant = 0
    disjoint_nonconstant = 0

    polys = {e: edge_polynomial(*e) for e in edges}
    for i, e in enumerate(edges):
        for f in edges[i + 1 :]:
            G = sp.gcd(polys[e], polys[f])
            if set(e) & set(f):
                shared_pairs += 1
                if G.degree() > 0:
                    nonconstant += 1
                    resultant = abs(
                        int(sp.resultant(C.as_expr(), G.as_expr(), T))
                    )
                    assert resultant == 1, (e, f, G.as_expr(), resultant)
            elif G.degree() > 0:
                disjoint_nonconstant += 1

    assert len(edges) == 105
    assert shared_pairs == 1365
    assert nonconstant == 422
    assert disjoint_nonconstant == 861
    print(
        "K=31 exhaustive shared-endpoint audit: "
        "105 edges, 1365 shared-endpoint pairs, 422 nonconstant gcds, "
        "all |Res(C_K,G)|=1; disjoint nonconstant gcd pairs=861: OK"
    )


def main() -> None:
    check_trace_difference_factorization()
    check_removable_value()
    check_k31_shared_endpoint_support_free()
    print("cayley inverse shared-endpoint torsion regression: OK")


if __name__ == "__main__":
    main()
