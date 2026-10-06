#!/usr/bin/env python3
"""Exact finite regression for cayley_ratio_orbit_factorization.md.

This producer independently constructs one ratio orbit at a time from its
cyclotomic resultant.  It checks the H_r=1+K P_r congruence, the Dedekind-sum
next coefficient, cross-resultant square structure, one-factor fourth-power
discriminants, and (for the default small cases) the global fourth-power
formula.

No finite run is used as a proof of the general theorems.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import combinations
from math import log

from sympy import Poly, Symbol, ZZ, discriminant, expand, integer_nthroot, resultant

X = Symbol("X")
T = Symbol("T")
U = Symbol("U")
Y = Symbol("Y")


def inverse_classes(K: int) -> list[int]:
    seen: set[int] = set()
    reps: list[int] = []
    for r in range(2, K):
        if r in seen:
            continue
        rinv = pow(r, -1, K)
        seen.add(r)
        seen.add(rinv)
        reps.append(min(r, rinv))
    return reps


def dedekind_sum(r: int, K: int) -> Fraction:
    def saw(a: int) -> Fraction:
        a %= K
        if a == 0:
            return Fraction(0)
        return Fraction(a, K) - Fraction(1, 2)

    return sum((saw(a) * saw(r * a) for a in range(1, K)), Fraction(0))


def ratio_H(K: int, r: int) -> Poly:
    phi = sum(X**j for j in range(K))
    D = (X - 1) * (X**r - 1)
    B = expand(U * D - (X**r - X))
    A = resultant(phi, B, X)
    G = Poly(expand(A / K), U, domain=ZZ)
    if G.eval(0) < 0:
        G = -G

    H_expr = 0
    for (e,), coeff in G.terms():
        assert e % 2 == 0, (K, r, e, coeff)
        H_expr += int(coeff) * Y ** (e // 2)
    return Poly(H_expr, Y, domain=ZZ)


def ratio_F_from_H(K: int, H: Poly) -> Poly:
    n = K - 1
    expr = expand(2**n * H.as_expr().subs(Y, T**2 / 4))
    return Poly(expr, T, domain=ZZ)


def check_K(K: int, global_check: bool) -> None:
    n = K - 1
    m = n // 2
    reps = inverse_classes(K)
    assert len(reps) == m

    Hs: dict[int, Poly] = {}
    Ps: dict[int, Poly] = {}
    Is: dict[int, int] = {}

    for r in reps:
        H = ratio_H(K, r)
        assert H.degree() == m
        assert H.LC() == K
        assert H.eval(0) == 1

        coeffs = H.all_coeffs()
        assert all((int(c) % K == 0) for c in coeffs[:-1])
        assert int(coeffs[-1]) == 1

        P = Poly(expand((H.as_expr() - 1) / K), Y, domain=ZZ)
        assert P.degree() == m
        assert P.LC() == 1
        assert P.eval(0) == 0

        if K >= 5:
            expected_b = Fraction((K - 1) * (K - 2), 12) - K * dedekind_sum(r, K)
            assert expected_b.denominator == 1
            actual_b = int(P.nth(m - 1))
            assert actual_b == expected_b.numerator, (K, r, actual_b, expected_b)
        else:
            # At K=3 the constant 1 in H=1+K*P contributes to H's
            # Y^(m-1) coefficient; the Dedekind formula is not for P.
            assert K == 3 and r == 2
            assert H.as_expr() == 1 + 3 * Y and P.as_expr() == Y

        DH = abs(int(discriminant(H.as_expr(), Y)))
        assert DH % (K ** (m - 1)) == 0
        I2 = DH // (K ** (m - 1))
        I, is_square = integer_nthroot(I2, 2)
        assert is_square

        F = ratio_F_from_H(K, H)
        DF = abs(int(discriminant(F.as_expr(), T)))
        assert DF == 2 ** (n * n) * K ** (K - 2) * int(I) ** 4

        Hs[r] = H
        Ps[r] = P
        Is[r] = int(I)

    bvals = [int(Ps[r].nth(m - 1)) for r in reps]
    assert len(set(bvals)) == len(bvals)

    Ms: dict[tuple[int, int], int] = {}
    for r, s in combinations(reps, 2):
        Q = Poly(Ps[s].as_expr() - Ps[r].as_expr(), Y, domain=ZZ)
        assert Q.degree() == m - 1
        M = abs(int(resultant(Hs[r].as_expr(), Q.as_expr(), Y)))
        RH = abs(int(resultant(Hs[r].as_expr(), Hs[s].as_expr(), Y)))
        assert RH == K ** (m + 1) * M

        Fr = ratio_F_from_H(K, Hs[r])
        Fs = ratio_F_from_H(K, Hs[s])
        RF = abs(int(resultant(Fr.as_expr(), Fs.as_expr(), T)))
        assert RF == 2 ** (n * n) * K ** (K + 1) * M**2
        Ms[(r, s)] = M

    if global_check:
        S = Poly(1, T, domain=ZZ)
        for r in reps:
            S *= ratio_F_from_H(K, Hs[r])
        DS = abs(int(discriminant(S.as_expr(), T)))
        J = 1
        for I in Is.values():
            J *= I
        for M in Ms.values():
            J *= M
        predicted = (
            2 ** ((K - 1) ** 4 // 4)
            * K ** (((K - 1) * (K * K - 7)) // 4)
            * J**4
        )
        assert DS == predicted

    residual_logs = []
    for M in Ms.values():
        q = M
        while q % 2 == 0:
            q //= 2
        while q % K == 0:
            q //= K
        residual_logs.append(log(q) if q > 1 else 0.0)

    avg = sum(residual_logs) / len(residual_logs) if residual_logs else 0.0
    print(
        f"K={K:2d} classes={m:2d} "
        f"avg_log_Mprime/K^2={avg/(K*K):.9f}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--extended", action="store_true")
    args = parser.parse_args()

    if args.extended:
        Ks = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    else:
        Ks = [3, 7, 11, 13]

    for K in Ks:
        check_K(K, global_check=(K <= 13))

    print("cayley ratio-orbit factorization regression: OK")


if __name__ == "__main__":
    main()
