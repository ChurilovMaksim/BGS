#!/usr/bin/env python3
"""Exact finite regression for cayley_inverse_prime_ideal_vs_rational_modulus.md.

The universal theorem is proved in the mathematics note.  This script checks
that calibrated split inverse edges vanish at exactly one conjugate pair of
full cyclotomic residue embeddings, rather than modulo the rational ideal pO.
"""
from __future__ import annotations

import sympy as sp


def primitive_k_root(K: int, p: int) -> int:
    assert sp.isprime(K) and sp.isprime(p) and p % K == 1
    exponent = (p - 1) // K
    for g in range(2, 200):
        h = pow(g, exponent, p)
        if h != 1:
            assert pow(h, K, p) == 1
            return h
    raise RuntimeError((K, p))


def edge_value(h: int, j: int, a: int, b: int, p: int) -> int:
    z = pow(h, j, p)
    zinv = pow(z, -1, p)
    return (
        pow(z, a, p)
        + pow(zinv, a, p)
        + pow(z, b, p)
        + pow(zinv, b, p)
        - 2 * z
        - 2 * zinv
    ) % p


def check_anchor(
    K: int,
    p: int,
    edge: tuple[int, int],
    expected_conjugate_exponents: set[int],
    label: str,
) -> None:
    h = primitive_k_root(K, p)
    zeros = {
        j
        for j in range(1, K)
        if edge_value(h, j, edge[0], edge[1], p) == 0
    }
    assert zeros == expected_conjugate_exponents, (
        K,
        p,
        edge,
        zeros,
        expected_conjugate_exponents,
    )
    assert len(zeros) == 2
    assert len(zeros) < K - 1
    j = min(zeros)
    assert K - j in zeros
    print(
        f"K={K:3d} p={p:<16d} {label}: edge={edge} "
        f"zero full embeddings={sorted(zeros)}; not rational-modulus: OK"
    )


def main() -> None:
    check_anchor(
        59,
        21_713,
        (8, 26),
        {3, 56},
        "cross-class",
    )
    check_anchor(
        89,
        143_207_231,
        (16, 35),
        {23, 66},
        "structural associate",
    )
    check_anchor(
        229,
        966_684_838_398_077,
        (44, 91),
        {91, 138},
        "large structural associate",
    )
    print("cayley inverse prime-ideal versus rational-modulus regression: OK")


if __name__ == "__main__":
    main()
