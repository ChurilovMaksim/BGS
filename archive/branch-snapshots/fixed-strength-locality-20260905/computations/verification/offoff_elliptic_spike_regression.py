#!/usr/bin/env python3
"""Exact regression for mathematics/offoff_elliptic_spike_theorem.md.

The general proof uses elliptic monodromy and trace-sheaf quasi-orthogonality;
this script checks only the algebraic identities and finite point-count anchors.
"""
from __future__ import annotations

from collections import Counter
import sympy as sp

A, B, T = sp.symbols("A B T")
S, D = sp.symbols("S D")
ALPHA = (S + D) / 2
BETA = (S - D) / 2


def symbolic_checks() -> None:
    Ta = (ALPHA * A - 1) / (A - ALPHA)
    Tb = (BETA * B - 1) / (B - BETA)
    num = sp.factor(sp.together(2 / (A - B) + 2 / (Ta - Tb) - T).as_numer_denom()[0])

    q = sp.factor(sp.discriminant(num, B))
    disc_q = sp.factor(sp.discriminant(q, A))

    R = (
        D**2 * T**4
        + 2 * D * (S**2 - D**2 - 4) * T**3
        + 4 * (5 * D**2 - S**2 + 4) * T**2
        - 64 * D * T
        + 64
    )
    expected_disc_q_core = (
        D**2
        * (D * T - 2) ** 4
        * (S - D - 2) ** 2
        * (S - D + 2) ** 2
        * (S + D - 2) ** 2
        * (S + D + 2) ** 2
        * R
    )
    ratio = sp.cancel(disc_q / expected_disc_q_core)
    assert ratio != 0 and not ratio.has(A, B, T, S, D), ratio

    disc_R = sp.factor(sp.discriminant(R, T))
    expected_disc_R = (
        2**16
        * D**2
        * S**2
        * (S - D - 2) ** 2
        * (S - D + 2) ** 2
        * (S + D - 2) ** 2
        * (S + D + 2) ** 2
    )
    assert sp.factor(disc_R - expected_disc_R) == 0
    assert sp.factor(R.subs(T, 2 / D) - 16 / D**2) == 0

    Lm = (BETA - 1) * (A - 1) - (ALPHA - 1) * (B - 1)
    Lp = (BETA + 1) * (A + 1) - (ALPHA + 1) * (B + 1)
    at_spike = sp.factor(num.subs(T, 2 / D))
    assert sp.factor(at_spike / (Lm * Lp) - 8 / D) == 0

    support = sp.Poly(sp.expand((D * T - 2) * R), T)
    assert support.all_coeffs() == [
        D**3,
        -2 * D**4 + 2 * D**2 * S**2 - 10 * D**2,
        24 * D**3 - 8 * D * S**2 + 32 * D,
        -104 * D**2 + 8 * S**2 - 32,
        192 * D,
        -128,
    ]

    # Diagonal special stratum D=0: forbidden A=B factor plus bilinear residual.
    diagonal = sp.factor(num.subs(D, 0))
    expected_diag = (A - B) * (
        8 * A * B
        + A * S**2 * T - 4 * A * S - 4 * A * T
        - B * S**2 * T - 4 * B * S + 4 * B * T
        + 8
    )
    assert sp.factor(diagonal - expected_diag) == 0

    # Exactly h1=1, h2!=1.
    beta = sp.symbols("beta")
    Tb1 = (beta * B - 1) / (B - beta)
    one_num = sp.factor(
        sp.together(2 / (A - B) + 2 / (-A - Tb1) - T).as_numer_denom()[0]
    )
    one_q = sp.factor(sp.discriminant(one_num, B))
    one_disc = sp.factor(sp.discriminant(one_q, A))
    expected_one = 2**16 * T**6 * (beta - 1) ** 2 * (beta + 1) ** 2 * (
        T**2 + 8 * beta * T + 16
    )
    assert sp.factor(one_disc - expected_one) == 0


def inv(x: int, p: int) -> int:
    return pow(x % p, -1, p)


def cayley(h: int, p: int) -> int:
    return (h + 1) * inv(h - 1, p) % p


def Tmob(alpha: int, a: int, p: int) -> int | None:
    if a == alpha:
        return None
    return (alpha * a - 1) * inv(a - alpha, p) % p


def off_class_histogram(p: int, alpha: int, beta: int) -> Counter[int]:
    out: Counter[int] = Counter()
    for a in range(p):
        if a in (1, p - 1, alpha):
            continue
        ta = Tmob(alpha, a, p)
        assert ta is not None
        for b in range(p):
            if b in (1, p - 1, beta) or a == b:
                continue
            tb = Tmob(beta, b, p)
            assert tb is not None
            if ta == tb:
                continue
            value = (
                2 * inv(a - b, p)
                + 2 * inv(ta - tb, p)
            ) % p
            out[value] += 1
    return out


def subgroup(p: int, K: int) -> list[int]:
    g = int(sp.primitive_root(p))
    h = pow(g, (p - 1) // K, p)
    return [pow(h, j, p) for j in range(K)]


def finite_spike_check(p: int, K: int) -> None:
    H = subgroup(p, K)
    checked = 0
    for h1 in H:
        for h2 in H:
            if h1 == 1 or h2 == 1 or h1 == h2 or h1 * h2 % p == 1:
                continue
            alpha, beta = cayley(h1, p), cayley(h2, p)
            d = (alpha - beta) % p
            t0 = 2 * inv(d, p) % p
            hist = off_class_histogram(p, alpha, beta)
            assert hist[t0] == 2 * p - 8, (p, K, h1, h2, hist[t0], 2 * p - 8)
            checked += 1
            # Several representatives are enough for regression; the proof is symbolic.
            if checked >= 4:
                print(f"p={p}, K={K}: checked {checked} generic spike fibers = 2p-8")
                return
    raise AssertionError("no generic parameter found")


def main() -> None:
    symbolic_checks()
    finite_spike_check(53, 13)
    finite_spike_check(199, 11)
    print("off/off elliptic spike regression: OK")


if __name__ == "__main__":
    main()
