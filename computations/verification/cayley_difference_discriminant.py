#!/usr/bin/env python3
"""Exact regression for the Cayley difference-discriminant theorem.

The proof lives in mathematics/cayley_difference_discriminant.md.  This script
checks finite symbolic consequences only; it is not a substitute for the proof.

Default promoted cases K=11,13 are fast.  Use --extended for K=5,7,11,13,17,19.
"""

from __future__ import annotations

import argparse
from collections import Counter
from math import gcd
from sympy import Poly, Symbol, discriminant, factorint, primitive, resultant, sqf_part
from sympy import primerange

X = Symbol("X")
T = Symbol("T")

PROMOTED = {
    11: {23: 240, 67: 48, 89: 32},
    13: {53: 208, 79: 176, 131: 48, 157: 48, 313: 48},
}


def q_poly(K: int) -> Poly:
    expr = ((X + 1) ** K - (X - 1) ** K) // 2
    return Poly(expr, X)


def squarefree_difference_poly(K: int) -> Poly:
    q = q_poly(K)
    shifted = q.as_expr().subs(X, X - T)
    r = Poly(resultant(q.as_expr(), shifted, X), T)
    # The diagonal contributes exactly T^(K-1).
    r_nz = r.exquo(Poly(T ** (K - 1), T))
    sf = Poly(sqf_part(r_nz.as_expr()), T)
    _, sf_primitive = primitive(sf)
    # normalize positive leading coefficient
    if sf_primitive.LC() < 0:
        sf_primitive = -sf_primitive
    return sf_primitive


def vp(n: int, p: int) -> int:
    n = abs(int(n))
    e = 0
    while n and n % p == 0:
        n //= p
        e += 1
    return e


def subgroup_order_K(p: int, K: int) -> list[int]:
    assert (p - 1) % K == 0
    for g in range(2, p):
        h = pow(g, (p - 1) // K, p)
        if h != 1 and pow(h, K, p) == 1:
            return [pow(h, j, p) for j in range(K)]
    raise RuntimeError("failed to find order-K subgroup generator")


def cayley_excess(p: int, K: int) -> int:
    H = subgroup_order_K(p, K)
    A = []
    for h in H:
        if h == 1:
            continue
        A.append(((h + 1) * pow((h - 1) % p, p - 2, p)) % p)
    reps = Counter()
    for a in A:
        for b in A:
            d = (a - b) % p
            if d:
                reps[d] += 1
    energy_nz = sum(m * m for m in reps.values())
    baseline = (K - 1) * (2 * K - 5)
    return energy_nz - baseline


def check_K(K: int) -> None:
    S = squarefree_difference_poly(K)
    expected_degree = (K - 1) ** 2 // 2
    assert S.degree() == expected_degree, (K, S.degree(), expected_degree)

    D = abs(int(discriminant(S.as_expr(), T)))
    assert D != 0

    # Leading coefficient must have no prime support away from K.
    lc_fac = factorint(abs(int(S.LC())))
    assert set(lc_fac).issubset({K}), (K, lc_fac)

    fac = factorint(D)
    split = {p: e for p, e in fac.items() if p % K == 1}

    print(f"K={K} degree={S.degree()} lc={S.LC()}")
    print("  split discriminant factors:", split)

    if K in PROMOTED:
        assert set(split) == set(PROMOTED[K]), (K, split, PROMOTED[K])
        for p, expected_delta in PROMOTED[K].items():
            delta = cayley_excess(p, K)
            assert delta == expected_delta, (K, p, delta, expected_delta)
            assert delta <= 4 * vp(D, p), (K, p, delta, vp(D, p))
            print(f"  p={p}: Delta={delta}, v_p(Disc)={vp(D,p)}, ratio={delta/(4*vp(D,p)):.6f}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--extended", action="store_true")
    args = parser.parse_args()
    Ks = [5, 7, 11, 13, 17, 19] if args.extended else [11, 13]
    for K in Ks:
        check_K(K)
    print("cayley difference-discriminant regression: OK")


if __name__ == "__main__":
    main()
