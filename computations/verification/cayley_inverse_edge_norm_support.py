#!/usr/bin/env python3
"""Exact inverse-row reduced edge-norm support checks.

The rational norm gcd is used only as a candidate filter.  A candidate split
prime is promoted only after a same-embedding finite-field check finds two
zero pair sums for one primitive K-th-root embedding.

Default mode is intentionally bounded for CI:
  * K=31 support reproduces {311,1303};
  * K=41, p=2908049 calibrates a norm-gcd false positive;
  * K=89 checks the two reduced edge norms in the p>K^4 witness.

Use --sweep K [K ...] for explicit finite support enumeration.  Large K can be
slow because SymPy factorization/resultants are reference implementations, not
the intended scalable kernel.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from functools import lru_cache

import sympy as sp

T = sp.symbols("T")


def is_odd_prime(K: int) -> bool:
    return K >= 7 and K % 2 == 1 and bool(sp.isprime(K))


@lru_cache(maxsize=None)
def real_cyclotomic_polynomial(K: int) -> sp.Poly:
    assert is_odd_prime(K)
    m = (K - 1) // 2
    expr = sp.Integer(1) + 2 * sum(
        sp.chebyshevt(a, T / 2) for a in range(1, m + 1)
    )
    poly = sp.Poly(sp.expand(expr), T, domain=sp.ZZ)
    assert poly.degree() == m and poly.LC() == 1
    return poly


@lru_cache(maxsize=None)
def trace_polynomial(n: int) -> sp.Poly:
    assert n >= 0
    return sp.Poly(sp.expand(2 * sp.chebyshevt(n, T / 2)), T, domain=sp.ZZ)


@lru_cache(maxsize=None)
def v_polynomial(n: int) -> sp.Poly:
    """Return v_n=(t_n-2)/(T-2) as an integral polynomial; v_0=0."""
    if n == 0:
        return sp.Poly(0, T, domain=sp.ZZ)
    q, rem = sp.div(
        trace_polynomial(n) - sp.Poly(2, T, domain=sp.ZZ),
        sp.Poly(T - 2, T, domain=sp.ZZ),
        domain=sp.ZZ,
    )
    assert rem.is_zero
    return sp.Poly(q, T, domain=sp.ZZ)


@lru_cache(maxsize=None)
def reduced_edge_polynomial(K: int, a: int, b: int) -> sp.Poly:
    m = (K - 1) // 2
    assert 0 <= a <= m and 0 <= b <= m and a < b
    assert a != 1 and b != 1
    w = sp.Poly(2, T, domain=sp.ZZ) - v_polynomial(a) - v_polynomial(b)
    assert w.degree() < m
    return sp.Poly(w, T, domain=sp.ZZ)


@lru_cache(maxsize=None)
def reduced_edge_norm(K: int, a: int, b: int) -> int:
    C = real_cyclotomic_polynomial(K)
    w = reduced_edge_polynomial(K, a, b)
    return abs(int(sp.resultant(C.as_expr(), w.as_expr(), T)))


def valid_edges(K: int) -> list[tuple[int, int]]:
    m = (K - 1) // 2
    vertices = [a for a in range(m + 1) if a != 1]
    return [
        (a, b)
        for i, a in enumerate(vertices)
        for b in vertices[i + 1 :]
    ]


def split_prime_factors(n: int, K: int) -> set[int]:
    if n == 0:
        raise RuntimeError("characteristic-zero reduced edge norm vanished")
    factors = sp.factorint(abs(int(n)))
    return {
        int(p)
        for p in factors
        if p != K and p % K == 1 and sp.isprime(p)
    }


def candidate_edge_map(K: int) -> dict[int, list[tuple[int, int]]]:
    by_prime: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for a, b in valid_edges(K):
        for p in split_prime_factors(reduced_edge_norm(K, a, b), K):
            by_prime[p].append((a, b))
    return dict(by_prime)


def has_disjoint_pair(edges: list[tuple[int, int]]) -> bool:
    for i, (a, b) in enumerate(edges):
        for c, d in edges[i + 1 :]:
            if len({a, b, c, d}) == 4:
                return True
    return False


def primitive_k_root(K: int, p: int) -> int:
    assert p % K == 1 and sp.isprime(p)
    exponent = (p - 1) // K
    for g in range(2, 200):
        h = pow(g, exponent, p)
        if h != 1:
            assert pow(h, K, p) == 1
            return h
    raise RuntimeError(f"failed to find K-th root for K={K}, p={p}")


def centered_roots(K: int, p: int, h: int) -> dict[int, int]:
    m = (K - 1) // 2
    hp = [1] * K
    for a in range(1, K):
        hp[a] = hp[a - 1] * h % p

    def trace(a: int) -> int:
        if a == 0:
            return 2 % p
        return (hp[a] + hp[K - a]) % p

    tau = trace(1)
    roots = {
        a: (trace(a) - tau) % p
        for a in range(m + 1)
        if a != 1
    }
    if any(x == 0 for x in roots.values()):
        raise RuntimeError("valid centered trace root vanished")
    if len(set(roots.values())) != len(roots):
        raise RuntimeError("valid centered trace roots not distinct")
    return roots


def zero_edges_for_embedding(K: int, p: int, h: int) -> list[tuple[int, int]]:
    roots = centered_roots(K, p, h)
    vertices = sorted(roots)
    return [
        (a, b)
        for i, a in enumerate(vertices)
        for b in vertices[i + 1 :]
        if (roots[a] + roots[b]) % p == 0
    ]


def same_embedding_support(
    K: int, p: int
) -> tuple[bool, int | None, list[tuple[int, int]]]:
    h0 = primitive_k_root(K, p)
    m = (K - 1) // 2
    for j in range(1, m + 1):
        h = pow(h0, j, p)
        zero = zero_edges_for_embedding(K, p, h)
        if len(zero) >= 2:
            if not has_disjoint_pair(zero):
                raise RuntimeError("two zero edges unexpectedly share a vertex")
            return True, j, zero
    return False, None, []


def support_for_K(
    K: int,
) -> tuple[list[int], dict[int, list[tuple[int, int]]]]:
    by_prime = candidate_edge_map(K)
    candidates = {
        p: edges for p, edges in by_prime.items() if has_disjoint_pair(edges)
    }
    support: list[int] = []
    witnesses: dict[int, list[tuple[int, int]]] = {}
    for p in sorted(candidates):
        ok, _j, zero = same_embedding_support(K, p)
        if ok:
            support.append(p)
            witnesses[p] = zero
    return support, witnesses


def check_default() -> None:
    support31, witness31 = support_for_K(31)
    assert support31 == [311, 1303], support31
    assert 1303 in witness31 and len(witness31[1303]) == 2
    print(f"K=31 exact inverse split support: {support31}")

    candidates41 = candidate_edge_map(41)
    p_false = 2_908_049
    assert p_false in candidates41
    assert has_disjoint_pair(candidates41[p_false])
    ok, _, _ = same_embedding_support(41, p_false)
    assert not ok
    print(
        "K=41 p=2908049: norm-gcd candidate but "
        "same-embedding inverse support = false"
    )

    p89 = 143_207_231
    n1 = reduced_edge_norm(89, 16, 35)
    n2 = reduced_edge_norm(89, 20, 33)
    assert n1 == p89 and n2 == p89, (n1, n2)
    ok, j, zero = same_embedding_support(89, p89)
    assert ok and set(zero) == {(16, 35), (20, 33)}, (j, zero)
    assert p89 > 89**4
    print(
        "K=89 p=143207231: "
        f"N(w_16,35)=N(w_20,33)={p89}; "
        f"same embedding j={j}; I_inverse={2 * len(zero)}; "
        f"p/K^4={p89 / 89**4:.12f}"
    )
    print("cayley inverse reduced edge-norm support regression: OK")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--sweep",
        nargs="+",
        type=int,
        help="exact finite support sweep for the listed prime K; may be slow",
    )
    args = parser.parse_args()

    if not args.sweep:
        check_default()
        return

    for K in args.sweep:
        if not is_odd_prime(K):
            raise SystemExit(f"K={K} is not an odd prime >=7")
        support, witnesses = support_for_K(K)
        print(f"K={K}: {support}")
        for p in support:
            print(f"  p={p} zero_edges={witnesses[p]}")
    print("explicit sweep complete; finite data only")


if __name__ == "__main__":
    main()
