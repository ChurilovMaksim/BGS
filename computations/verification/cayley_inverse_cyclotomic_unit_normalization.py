#!/usr/bin/env python3
"""Exact regression for cayley_inverse_cyclotomic_unit_normalization.md.

Finite controls only.  The universal identities are proved in the mathematics
note.

Checks:
  * x_a=(tau-2) lambda_a exactly in Z[tau], lambda_a=v_a-1;
  * every valid lambda_a has norm +-1 at K=31;
  * P_(a,b)=t_a+t_b-2tau=-(tau-2)w_(a,b) exactly;
  * simultaneous zero edges give direct trace Laurent relations of l1-weight 8;
  * the unit-ratio Laurent presentation has l1-weights <=8 and <=32;
  * cross-class K=59 and structural K=31,89,229 anchors vanish at one embedding;
  * the K=229 structural weight-eight edge relations are indecomposable modulo p
    as positive multisets of 2K-th roots.
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


def check_exact_edge_scaling(edges: list[tuple[int, int]]) -> None:
    two = sp.Poly(2, T, domain=sp.ZZ)
    tau = sp.Poly(T, T, domain=sp.ZZ)
    scalar = sp.Poly(T - 2, T, domain=sp.ZZ)
    for a, b in edges:
        w = two - v_polynomial(a) - v_polynomial(b)
        P = trace_polynomial(a) + trace_polynomial(b) - 2 * tau
        assert (P + scalar * w).is_zero, (a, b)
    print(f"exact P_e=-(tau-2)w_e scaling on {len(edges)} controls: OK")


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


def trace_edge_laurent(edge: tuple[int, int]) -> ExponentDict:
    a, b = edge
    out: defaultdict[int, int] = defaultdict(int)
    for exponent, coefficient in (
        (a, 1),
        (-a, 1),
        (b, 1),
        (-b, 1),
        (1, -2),
        (-1, -2),
    ):
        out[exponent] += coefficient
    return clean(dict(out))


def trace_difference_laurent(
    e: tuple[int, int],
    f: tuple[int, int],
) -> ExponentDict:
    return add(trace_edge_laurent(e), trace_edge_laurent(f), -1)


def l1_weight(poly: ExponentDict) -> int:
    return sum(abs(c) for c in poly.values())


def embedded_2k_root(K: int, p: int, generator: int, j: int, h: int) -> int:
    y0 = pow(generator, (p - 1) // (2 * K), p)
    y = pow(y0, j, p)
    if pow(y, K, p) != p - 1:
        y = (-y) % p
    assert pow(y, K, p) == p - 1
    assert pow(y, 2, p) == h
    return y


def eval_laurent(poly: ExponentDict, root: int, p: int, order: int) -> int:
    return sum(
        coefficient * pow(root, exponent % order, p)
        for exponent, coefficient in poly.items()
    ) % p


def positive_2k_multiset(poly: ExponentDict, K: int) -> list[int]:
    """Encode signed K-root terms as positive 2K-root exponents."""
    exponents: list[int] = []
    for exponent, coefficient in poly.items():
        if coefficient > 0:
            exponents.extend([(2 * exponent) % (2 * K)] * coefficient)
        elif coefficient < 0:
            exponents.extend(
                [(K + 2 * exponent) % (2 * K)] * (-coefficient)
            )
    assert len(exponents) == l1_weight(poly)
    return exponents


def assert_indec_pos_relation(
    poly: ExponentDict,
    K: int,
    p: int,
    y: int,
) -> None:
    exponents = positive_2k_multiset(poly, K)
    values = [pow(y, exponent, p) for exponent in exponents]
    assert sum(values) % p == 0
    n = len(values)
    assert n <= 12  # bounded exhaustive regression only
    for mask in range(1, (1 << n) - 1):
        subtotal = 0
        for i, value in enumerate(values):
            if mask >> i & 1:
                subtotal += value
        assert subtotal % p != 0, (K, p, mask, exponents)


def check_split_anchor(
    K: int,
    p: int,
    expected_edges: list[tuple[int, int]],
    expected_kind: str,
    *,
    check_indec: bool = False,
) -> None:
    generator, h0, j, centered, units = find_embedding(K, p, expected_edges)
    h = pow(h0, j, p)
    y = embedded_2k_root(K, p, generator, j, h)

    for a, b in expected_edges:
        # x_a=(tau-2)lambda_a, so a zero centred pair is exactly
        # lambda_a/lambda_b=-1.
        ratio = units[a] * pow(units[b], -1, p) % p
        assert ratio == p - 1, (K, p, j, (a, b), ratio)

        # Direct trace normal form in the primitive K-th root.
        P = trace_edge_laurent((a, b))
        assert len(P) <= 6
        assert l1_weight(P) == 8
        assert eval_laurent(P, h, p, K) == 0

        # Unit-ratio form in a primitive 2K-th root.
        A = sign_numerator((a, b))
        assert len(A) <= 8
        assert l1_weight(A) <= 8
        assert eval_laurent(A, y, p, 2 * K) == 0

        if check_indec:
            assert_indec_pos_relation(P, K, p, y)

    for e, f in zip(expected_edges, expected_edges[1:]):
        # Row operation on the direct trace ideal: the universal 2tau terms
        # cancel and the difference remains weight eight.
        Q = trace_difference_laurent(e, f)
        assert len(Q) <= 8
        assert l1_weight(Q) <= 8
        assert eval_laurent(Q, h, p, K) == 0

        # Supplementary quotient-unit relation.
        B = ratio_difference_numerator(e, f)
        assert len(B) <= 32
        assert l1_weight(B) <= 32
        assert eval_laurent(B, y, p, 2 * K) == 0

        a, b = e
        c, d = f
        r_e = units[a] * pow(units[b], -1, p) % p
        r_f = units[c] * pow(units[d], -1, p) % p
        assert r_e * pow(r_f, -1, p) % p == 1

    trace_sizes = [len(trace_edge_laurent(edge)) for edge in expected_edges]
    trace_weights = [l1_weight(trace_edge_laurent(edge)) for edge in expected_edges]
    difference_sizes = [
        len(trace_difference_laurent(e, f))
        for e, f in zip(expected_edges, expected_edges[1:])
    ]
    print(
        f"K={K:3d} p={p:<16d} emb={j:3d} {expected_kind}: "
        f"trace_support={trace_sizes}/weight={trace_weights}; "
        f"difference_support={difference_sizes}; "
        f"indec={check_indec}: OK"
    )


def main() -> None:
    check_exact_root_normalization(31)
    check_exact_root_normalization(59)
    check_unit_norms(31)
    check_exact_edge_scaling([(2, 11), (5, 12), (8, 26), (9, 10)])

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

    # Much larger structural control.  Each individual weight-eight relation
    # is indecomposable modulo p, guarding against a naive weight=>conductor
    # inference in the split finite-characteristic regime.
    check_split_anchor(
        229,
        966_684_838_398_077,
        [(44, 91), (48, 89)],
        "large structural associate",
        check_indec=True,
    )

    print("cayley inverse cyclotomic-unit normalization regression: OK")


if __name__ == "__main__":
    main()
