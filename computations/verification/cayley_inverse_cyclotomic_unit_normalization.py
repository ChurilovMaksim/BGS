#!/usr/bin/env python3
"""Exact regression for cayley_inverse_cyclotomic_unit_normalization.md.

Finite controls only.  The universal identities are proved in the mathematics
note.

Checks:
  * x_a=(tau-2) lambda_a exactly in Z[tau], lambda_a=v_a-1;
  * every valid lambda_a has norm +-1 at K=31;
  * zero-edge unit ratios R=lambda_a/lambda_b are -1 at one embedding for
    cross-class K=59 and structural K=31,89 anchors;
  * cleared Laurent sign equations use <=8 monomials;
  * cleared Laurent ratio-difference equations use <=32 monomials and vanish
    at the same 2K-th-root embedding.
"""
from __future__ import annotations

from collections import defaultdict

import sympy as sp

from cayley_inverse_structural_associates import (
    T,
    real_cyclotomic_polynomial,
    trace_polynomial,
    v_polynomial,
)

ExponentDict = dict[int, int]


def lambda_polynomial(a: int) -> sp.Poly:
    return v_polynomial(a) - sp.Poly(1, T, domain=sp.ZZ)


def check_exact_root_normalization(K: int) -> None:
    C = real_cyclotomic_polynomial(K)
    m = (K - 1) // 2

    for a in range(m + 1):
        if a == 1:
            continue
        lhs = trace_polynomial(a) - sp.Poly(T, T, domain=sp.ZZ)
        rhs = sp.Poly(T - 2, T, domain=sp.ZZ) * lambda_polynomial(a)
        remainder = sp.rem(
            lhs.as_expr() - rhs.as_expr(),
            C.as_expr(),
            domain=sp.ZZ,
        )
        assert sp.Poly(remainder, T, domain=sp.ZZ).is_zero

    # The omitted class is exactly the zero normalized root.
    assert lambda_polynomial(1).is_zero
    print(f"K={K}: exact centred-root normalization for all valid classes: OK")


def check_unit_norms(K: int) -> None:
    C = real_cyclotomic_polynomial(K)
    m = (K - 1) // 2
    for a in range(m + 1):
        if a == 1:
            continue
        norm = int(sp.resultant(C.as_expr(), lambda_polynomial(a).as_expr(), T))
        assert abs(norm) == 1, (K, a, norm)
    print(f"K={K}: all valid lambda_a have exact norm +-1: OK")


def primitive_data(K: int, p: int) -> tuple[int, int]:
    assert sp.isprime(K) and sp.isprime(p) and p % K == 1
    generator = int(sp.primitive_root(p))
    h0 = pow(generator, (p - 1) // K, p)
    assert h0 != 1 and pow(h0, K, p) == 1
    return generator, h0


def centered_and_units(
    K: int,
    p: int,
    h: int,
) -> tuple[int, dict[int, int], dict[int, int]]:
    m = (K - 1) // 2
    powers = [1] * K
    for a in range(1, K):
        powers[a] = powers[a - 1] * h % p

    trace = [0] * (m + 1)
    trace[0] = 2 % p
    for a in range(1, m + 1):
        trace[a] = (powers[a] + powers[K - a]) % p
    assert len(set(trace)) == len(trace)

    tau = trace[1]
    ramified_scalar = (tau - 2) % p
    assert ramified_scalar != 0
    inv_scalar = pow(ramified_scalar, -1, p)

    centered = {
        a: (trace[a] - tau) % p
        for a in range(m + 1)
        if a != 1
    }
    units = {
        a: centered[a] * inv_scalar % p
        for a in centered
    }
    assert 0 not in centered.values()
    assert 0 not in units.values()
    return tau, centered, units


def zero_edges(centered: dict[int, int], p: int) -> list[tuple[int, int]]:
    inverse = {x: a for a, x in centered.items()}
    out: list[tuple[int, int]] = []
    for a, x in centered.items():
        b = inverse.get((-x) % p)
        if b is not None and a < b:
            out.append((a, b))
    return sorted(out)


def find_embedding(
    K: int,
    p: int,
    expected_edges: list[tuple[int, int]],
) -> tuple[int, int, int, dict[int, int], dict[int, int]]:
    generator, h0 = primitive_data(K, p)
    m = (K - 1) // 2
    target = set(expected_edges)
    for j in range(1, m + 1):
        _tau, centered, units = centered_and_units(K, p, pow(h0, j, p))
        edges = zero_edges(centered, p)
        if set(edges) == target:
            return generator, h0, j, centered, units
    raise RuntimeError((K, p, expected_edges))


def clean(A: ExponentDict) -> ExponentDict:
    return {e: c for e, c in A.items() if c}


def add(A: ExponentDict, B: ExponentDict, scale: int = 1) -> ExponentDict:
    C: defaultdict[int, int] = defaultdict(int)
    C.update(A)
    for e, c in B.items():
        C[e] += scale * c
    return clean(dict(C))


def mul(A: ExponentDict, B: ExponentDict) -> ExponentDict:
    C: defaultdict[int, int] = defaultdict(int)
    for e, a in A.items():
        for f, b in B.items():
            C[e + f] += a * b
    return clean(dict(C))


def S(n: int) -> ExponentDict:
    if n == 0:
        return {}
    return {n: 1, -n: -1}


def lambda_numerator(a: int) -> ExponentDict:
    return mul(S(a - 1), S(a + 1))


def sign_numerator(edge: tuple[int, int]) -> ExponentDict:
    a, b = edge
    return add(lambda_numerator(a), lambda_numerator(b))


def ratio_difference_numerator(
    e: tuple[int, int],
    f: tuple[int, int],
) -> ExponentDict:
    a, b = e
    c, d = f
    left = mul(lambda_numerator(a), lambda_numerator(d))
    right = mul(lambda_numerator(b), lambda_numerator(c))
    return add(left, right, -1)


def embedded_2k_root(K: int, p: int, generator: int, j: int, h: int) -> int:
    y0 = pow(generator, (p - 1) // (2 * K), p)
    y = pow(y0, j, p)
    if pow(y, K, p) != p - 1:
        y = (-y) % p
    assert pow(y, K, p) == p - 1
    assert pow(y, 2, p) == h
    return y


def eval_laurent(poly: ExponentDict, y: int, p: int, K: int) -> int:
    return sum(
        coefficient * pow(y, exponent % (2 * K), p)
        for exponent, coefficient in poly.items()
    ) % p


def check_split_anchor(
    K: int,
    p: int,
    expected_edges: list[tuple[int, int]],
    expected_kind: str,
) -> None:
    generator, h0, j, centered, units = find_embedding(K, p, expected_edges)
    h = pow(h0, j, p)
    y = embedded_2k_root(K, p, generator, j, h)

    for a, b in expected_edges:
        # x_a=(tau-2)lambda_a, so a zero centred pair is exactly
        # lambda_a/lambda_b=-1.
        ratio = units[a] * pow(units[b], -1, p) % p
        assert ratio == p - 1, (K, p, j, (a, b), ratio)

        A = sign_numerator((a, b))
        assert len(A) <= 8
        assert all(abs(c) == 1 for c in A.values())
        assert eval_laurent(A, y, p, K) == 0

    for e, f in zip(expected_edges, expected_edges[1:]):
        B = ratio_difference_numerator(e, f)
        assert len(B) <= 32
        assert all(abs(c) == 1 for c in B.values())
        assert eval_laurent(B, y, p, K) == 0

        a, b = e
        c, d = f
        r_e = units[a] * pow(units[b], -1, p) % p
        r_f = units[c] * pow(units[d], -1, p) % p
        assert r_e * pow(r_f, -1, p) % p == 1

    sign_sizes = [len(sign_numerator(edge)) for edge in expected_edges]
    ratio_sizes = [
        len(ratio_difference_numerator(e, f))
        for e, f in zip(expected_edges, expected_edges[1:])
    ]
    print(
        f"K={K:2d} p={p:<9d} emb={j:2d} {expected_kind}: "
        f"R_e=-1; sign_terms={sign_sizes}; ratio_terms={ratio_sizes}: OK"
    )


def main() -> None:
    check_exact_root_normalization(31)
    check_exact_root_normalization(59)
    check_unit_norms(31)

    # Additional nonunit characteristic-zero associate class.
    check_split_anchor(
        31,
        1303,
        [(2, 11), (5, 12)],
        "associate",
    )

    # Calibrated nonassociate cross-class event.
    check_split_anchor(
        59,
        21713,
        [(8, 26), (9, 10)],
        "cross-class",
    )

    # Universal structural associate family at a large split prime.
    check_split_anchor(
        89,
        143_207_231,
        [(16, 35), (20, 33)],
        "structural associate",
    )

    print("cayley inverse cyclotomic-unit normalization regression: OK")


if __name__ == "__main__":
    main()
