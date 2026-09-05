#!/usr/bin/env python3
"""Finite exact regression for cayley_inverse_multi_edge_resultant_filter.md.

Checks the one-way rational triple filter on high-multiplicity split anchors.
The universal implication is proved in the mathematics note.
"""
from __future__ import annotations

from functools import lru_cache
from itertools import combinations
from math import gcd

import sympy as sp

from cayley_inverse_even_multiplicity import maximal_embedding
from cayley_inverse_reduced_resultant_filter import edge_polynomial, monic_gcd
from cayley_inverse_structural_associates import T, real_cyclotomic_polynomial


@lru_cache(maxsize=None)
def reduced_pair_filter(K: int, e: tuple[int, int], f: tuple[int, int]) -> int:
    if f < e:
        e, f = f, e
    A = edge_polynomial(*e)
    B = edge_polynomial(*f)
    G = monic_gcd(A, B)
    A_red = A.exquo(G)
    B_red = B.exquo(G)
    C = real_cyclotomic_polynomial(K)

    r_gcd = abs(int(sp.resultant(C.as_expr(), G.as_expr(), T)))
    r_coprime = abs(int(sp.resultant(A_red.as_expr(), B_red.as_expr(), T)))
    assert r_gcd != 0 and r_coprime != 0
    return r_gcd * r_coprime


def gcd_all(values: list[int]) -> int:
    g = 0
    for value in values:
        g = gcd(g, value)
    return g


def check_anchor(K: int, p: int, expected_edges: int) -> None:
    d, embedding, _values, edges = maximal_embedding(K, p)
    assert d == expected_edges, (K, p, d, expected_edges)

    pair_filters = {
        (e, f): reduced_pair_filter(K, e, f)
        for e, f in combinations(edges, 2)
    }
    assert all(value % p == 0 for value in pair_filters.values())

    all_pair_gcd = gcd_all(list(pair_filters.values()))
    assert all_pair_gcd == p, (K, p, all_pair_gcd)

    triple_count = 0
    for triple in combinations(edges, 3):
        values = [
            pair_filters[tuple(sorted((e, f)))]
            for e, f in combinations(triple, 2)
        ]
        triple_gcd = gcd_all(values)
        assert triple_gcd == p, (K, p, triple, triple_gcd)
        triple_count += 1

    if K == 29:
        assert set(pair_filters.values()) == {59, 2 * 59, 23 * 59}

    print(
        f"K={K:3d} p={p:<4d} emb={embedding:2d} zero_edges={d} "
        f"pair_filters={len(pair_filters)} triples={triple_count}; "
        f"gcd(all pairs)=p and every triple gcd=p: OK"
    )


def main() -> None:
    check_anchor(29, 59, 3)
    check_anchor(43, 173, 4)
    check_anchor(83, 167, 7)
    check_anchor(89, 179, 8)
    print("cayley inverse multi-edge resultant filter regression: OK")


if __name__ == "__main__":
    main()
