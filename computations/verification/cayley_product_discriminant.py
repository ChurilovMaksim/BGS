#!/usr/bin/env python3
"""Exact finite regression for Cayley multiplicative rigidity/discriminant.

The universal proofs are in mathematics/cayley-arithmetic/cayley_multiplicative_rigidity.md and
mathematics/cayley-arithmetic/cayley_product_discriminant.md.  This producer checks finite
consequences only.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from collections import Counter
import sympy as sp

X, T = sp.symbols("X T")

PROMOTED = {
    11: {23: (192, 20), 67: (0, 0), 89: (16, 4)},
    13: {53: (128, 12), 79: (96, 12), 131: (0, 0), 157: (0, 0), 313: (16, 4)},
}


def q_poly(K: int) -> sp.Poly:
    return sp.Poly(sp.expand(((X + 1) ** K - (X - 1) ** K) / 2), X, domain=sp.ZZ)


def product_squarefree(K: int) -> sp.Poly:
    q = q_poly(K)
    n = K - 1
    g = sp.expand(X**n * q.as_expr().subs(X, T / X))
    R = sp.Poly(sp.resultant(q.as_expr(), g, X), T, domain=sp.ZZ)
    S = sp.Poly(sp.sqf_part(R.as_expr()), T, domain=sp.ZZ)
    _, S = S.primitive()
    if S.LC() < 0:
        S = -S
    return S


def vp(n: int, p: int) -> int:
    n = abs(int(n))
    e = 0
    while n and n % p == 0:
        n //= p
        e += 1
    return e


def subgroup(p: int, K: int) -> list[int]:
    g = int(sp.primitive_root(p))
    h = pow(g, (p - 1) // K, p)
    return [pow(h, j, p) for j in range(K)]


def cayley(p: int, K: int) -> list[int]:
    return [
        (h + 1) * pow((h - 1) % p, -1, p) % p
        for h in subgroup(p, K)
        if h != 1
    ]


def multiplicative_energy(p: int, K: int) -> tuple[int, int]:
    A = cayley(p, K)
    C = Counter((a * b) % p for a in A for b in A)
    return sum(v * v for v in C.values()), max(C.values())


def exponent_multiset(a: int, b: int, K: int) -> tuple[int, ...]:
    return tuple(sorted(((a+b)%K, (a-b)%K, (-a+b)%K, (-a-b)%K)))


def signed_permutation_orbit(a: int, b: int, K: int) -> set[tuple[int, int]]:
    out: set[tuple[int, int]] = set()
    for sa in (1, -1):
        for sb in (1, -1):
            out.add((sa*a % K, sb*b % K))
            out.add((sa*b % K, sb*a % K))
    return out


def check_multiset_lemma(K: int) -> None:
    buckets: dict[tuple[int, ...], list[tuple[int, int]]] = {}
    for a in range(K):
        for b in range(K):
            buckets.setdefault(exponent_multiset(a, b, K), []).append((a, b))
    for pairs in buckets.values():
        orbit = signed_permutation_orbit(*pairs[0], K)
        assert all(pair in orbit for pair in pairs)


def audit(K: int) -> None:
    check_multiset_lemma(K)
    S = product_squarefree(K)
    assert S.degree() == (K*K - 1) // 4
    assert set(sp.factorint(abs(int(S.LC())))).issubset({K})

    D = abs(int(sp.discriminant(S.as_expr(), T)))
    split = {p: e for p, e in sp.factorint(D).items() if p % K == 1}
    baseline = 4 * (K - 1) * (K - 2)

    print(f"K={K}: degree={S.degree()}, split_disc={split}")
    if K in PROMOTED:
        expected_split = {p: e for p, (_, e) in PROMOTED[K].items() if e}
        assert split == expected_split
        for p, (expected_delta, expected_v) in PROMOTED[K].items():
            E, max_mult = multiplicative_energy(p, K)
            delta = E - baseline
            assert delta == expected_delta
            assert vp(D, p) == expected_v
            assert delta <= 16 * expected_v
            print(f"  p={p}: E={E}, Delta_x={delta}, v_p(Disc)={expected_v}, maxmult={max_mult}")


def main() -> None:
    for K in (5, 7, 11, 13):
        audit(K)
    print("cayley product-discriminant regression: OK")


if __name__ == "__main__":
    main()
