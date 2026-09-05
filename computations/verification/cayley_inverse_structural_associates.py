#!/usr/bin/env python3
"""Exact regression for cayley_inverse_structural_associates.md.

Checks three independent layers:
  1. the four residue-class Laurent identities as formal affine-exponent
     dictionaries, valid for symbolic r;
  2. exact integer resultant norms for the K=89 and K=229 structural pairs;
  3. the complete K=229 same-embedding finite-field witness.

Finite computations are certificates/regressions only; the universal theorem is
proved in the mathematics note.
"""
from __future__ import annotations

from collections import defaultdict
from functools import lru_cache
import sympy as sp

T = sp.symbols("T")
Exponent = tuple[int, int]  # (coefficient of r, constant)


def clean(A: dict[Exponent, int]) -> dict[Exponent, int]:
    return {e: c for e, c in A.items() if c}


def add(
    A: dict[Exponent, int],
    B: dict[Exponent, int],
    scale: int = 1,
) -> dict[Exponent, int]:
    C: defaultdict[Exponent, int] = defaultdict(int)
    C.update(A)
    for e, c in B.items():
        C[e] += scale * c
    return clean(dict(C))


def mul(
    A: dict[Exponent, int],
    B: dict[Exponent, int],
) -> dict[Exponent, int]:
    C: defaultdict[Exponent, int] = defaultdict(int)
    for (ar, ac), a in A.items():
        for (br, bc), b in B.items():
            C[(ar + br, ac + bc)] += a * b
    return clean(dict(C))


def scale_index(a: int, b: int) -> dict[Exponent, int]:
    """S_(a*r+b)=y^(a*r+b)-y^(-a*r-b)."""
    return {(a, b): 1, (-a, -b): -1}


def square(A: dict[Exponent, int]) -> dict[Exponent, int]:
    return mul(A, A)


D2 = square(scale_index(0, 1))


def w_numerator(a: tuple[int, int], b: tuple[int, int]) -> dict[Exponent, int]:
    """D^2*w_(a,b)=2D^2-S_a^2-S_b^2."""
    two_d2 = {e: 2 * c for e, c in D2.items()}
    return add(add(two_d2, square(scale_index(*a)), -1), square(scale_index(*b)), -1)


def family_data(s: int):
    if s == 1:
        return (
            ((1, -2), (2, 3)),
            ((1, 2), (2, 1)),
            ((1, -1), (2, 2)),
            ((1, 1), (2, 0)),
        )
    if s == 2:
        return (
            ((1, 1), (2, -1)),
            ((1, 3), (2, 3)),
            ((1, 0), (2, 0)),
            ((1, 2), (2, 2)),
        )
    if s == 3:
        return (
            ((1, -2), (2, -1)),
            ((1, 0), (2, 3)),
            ((1, -1), (2, 0)),
            ((1, 1), (2, 2)),
        )
    if s == 4:
        return (
            ((1, -1), (2, 1)),
            ((1, 3), (2, -1)),
            ((1, 0), (2, 2)),
            ((1, 2), (2, 0)),
        )
    raise ValueError(s)


def q_family(s: int) -> dict[Exponent, int]:
    if s == 1:
        return {
            (-7, -7): 1,
            (-7, -3): -1,
            (-5, -5): -1,
            (-5, 3): 1,
            (-3, 1): 1,
            (-3, 5): -1,
        }
    if s == 2:
        return {
            (-7, -6): -1,
            (-7, -2): 1,
            (-5, -6): 1,
            (-5, 2): -1,
            (-3, -2): -1,
            (-3, 2): 1,
        }
    if s == 3:
        return {
            (-7, -5): -1,
            (-7, -1): 1,
            (-5, -7): 1,
            (-5, 1): -1,
            (-3, -5): -1,
            (-3, -1): 1,
        }
    if s == 4:
        return {
            (-7, -4): 1,
            (-7, 0): -1,
            (-5, -8): -1,
            (-5, 0): 1,
            (-3, -8): 1,
            (-3, -4): -1,
        }
    raise ValueError(s)


def check_laurent_families() -> None:
    for s in range(1, 5):
        e, f, numerator_eta, denominator_eta = family_data(s)
        lhs = mul(
            w_numerator(*e),
            mul(
                scale_index(*denominator_eta[0]),
                scale_index(*denominator_eta[1]),
            ),
        )
        rhs = mul(
            w_numerator(*f),
            mul(
                scale_index(*numerator_eta[0]),
                scale_index(*numerator_eta[1]),
            ),
        )
        N = add(lhs, rhs, -1)
        cyclotomic_factor = {(10, 2 * s): 1, (0, 0): -1}
        predicted = mul(cyclotomic_factor, q_family(s))
        assert N == predicted, (s, N, predicted)
        assert len(N) == 12
        print(f"s={s}: N_s=(y^(2K)-1)Q_s formal affine-exponent identity: OK")


@lru_cache(maxsize=None)
def real_cyclotomic_polynomial(K: int) -> sp.Poly:
    m = (K - 1) // 2
    expr = sp.Integer(1) + 2 * sum(
        sp.chebyshevt(a, T / 2) for a in range(1, m + 1)
    )
    poly = sp.Poly(sp.expand(expr), T, domain=sp.ZZ)
    assert poly.degree() == m and poly.LC() == 1
    return poly


@lru_cache(maxsize=None)
def trace_polynomial(n: int) -> sp.Poly:
    return sp.Poly(sp.expand(2 * sp.chebyshevt(n, T / 2)), T, domain=sp.ZZ)


@lru_cache(maxsize=None)
def v_polynomial(n: int) -> sp.Poly:
    if n == 0:
        return sp.Poly(0, T, domain=sp.ZZ)
    q, rem = sp.div(
        trace_polynomial(n) - sp.Poly(2, T, domain=sp.ZZ),
        sp.Poly(T - 2, T, domain=sp.ZZ),
        domain=sp.ZZ,
    )
    assert rem.is_zero
    return q


def edge_norm(K: int, a: int, b: int) -> int:
    C = real_cyclotomic_polynomial(K)
    w = sp.Poly(2, T, domain=sp.ZZ) - v_polynomial(a) - v_polynomial(b)
    return abs(int(sp.resultant(C.as_expr(), w.as_expr(), T)))


def check_norm_anchors() -> None:
    p89 = 143_207_231
    assert edge_norm(89, 16, 35) == p89
    assert edge_norm(89, 20, 33) == p89

    p229_small = 33_893
    p229_large = 966_684_838_398_077
    M229 = p229_small * p229_large
    assert sp.isprime(p229_small) and sp.isprime(p229_large)
    assert p229_small % 229 == 1 and p229_large % 229 == 1
    assert edge_norm(229, 44, 91) == M229
    assert edge_norm(229, 48, 89) == M229
    print(f"K=89 structural norm={p89}: OK")
    print(f"K=229 structural norm={M229}={p229_small}*{p229_large}: OK")


def zero_edges(K: int, p: int, h: int) -> list[tuple[int, int]]:
    m = (K - 1) // 2
    hp = [1] * K
    for a in range(1, K):
        hp[a] = hp[a - 1] * h % p

    trace = [0] * (m + 1)
    trace[0] = 2 % p
    for a in range(1, m + 1):
        trace[a] = (hp[a] + hp[K - a]) % p
    assert len(set(trace)) == len(trace)

    tau = trace[1]
    centered = {
        a: (trace[a] - tau) % p
        for a in range(m + 1)
        if a != 1
    }
    assert 0 not in centered.values()

    vertices = sorted(centered)
    return [
        (a, b)
        for i, a in enumerate(vertices)
        for b in vertices[i + 1 :]
        if (centered[a] + centered[b]) % p == 0
    ]


def check_k229_witness() -> None:
    K = 229
    p = 966_684_838_398_077
    h = 667_250_341_372_998  # real embedding exponent j=91
    assert sp.isprime(p)
    assert p % K == 1
    assert p > K**4
    assert h != 1 and pow(h, K, p) == 1  # K prime -> exact order K
    edges = zero_edges(K, p, h)
    assert edges == [(44, 91), (48, 89)], edges
    assert 2 * len(edges) == 4
    print(
        "PASS K=229 p=966684838398077 emb=91 "
        f"p/K^4={p / K**4:.12f} "
        "zero_edges=(44,91),(48,89) I_inverse=4"
    )


def main() -> None:
    check_laurent_families()
    check_norm_anchors()
    check_k229_witness()
    print("cayley inverse structural associates regression: OK")


if __name__ == "__main__":
    main()
