#!/usr/bin/env python3
"""Project-side regression for cayley_inverse_torsion_factors_support_free.md.

This does NOT verify the external minimal vanishing-sum theorem.  It checks the
load-bearing inverse-edge facts used around that theorem:
  * after collecting exponents, every valid edge has at most six terms;
  * distinct collected exponents differ by a nonzero integer of absolute value
    < K, so a conductor prime K cannot disappear from a ratio order;
  * the real prime-conductor reciprocal lift equals Phi_K;
  * the elementary coprime-conductor cyclotomic resultant is +-1 on controls.
"""
from __future__ import annotations

from collections import defaultdict
from math import gcd

import sympy as sp

from cayley_inverse_structural_associates import T, real_cyclotomic_polynomial

Z = sp.symbols("Z")


def collected_edge_terms(a: int, b: int) -> dict[int, int]:
    terms: defaultdict[int, int] = defaultdict(int)
    for exponent, coefficient in (
        (a, 1),
        (-a, 1),
        (b, 1),
        (-b, 1),
        (1, -2),
        (-1, -2),
    ):
        terms[exponent] += coefficient
    return {e: c for e, c in terms.items() if c}


def check_edge_exponent_geometry(K: int) -> None:
    m = (K - 1) // 2
    vertices = [a for a in range(m + 1) if a != 1]
    count = 0
    for i, a in enumerate(vertices):
        for b in vertices[i + 1 :]:
            terms = collected_edge_terms(a, b)
            exponents = sorted(terms)
            assert 1 <= len(exponents) <= 6
            assert all(c != 0 for c in terms.values())
            for r_index, r in enumerate(exponents):
                for s in exponents[r_index + 1 :]:
                    difference = s - r
                    assert 0 < difference < K, (K, a, b, r, s)
            count += 1
    print(f"K={K}: {count} valid edges have <=6 collected terms and exponent spread <K: OK")


def check_real_reciprocal_lift(K: int) -> None:
    C = real_cyclotomic_polynomial(K)
    m = (K - 1) // 2
    lift = sp.Poly(sp.expand(Z**m * C.as_expr().subs(T, Z + Z**-1)), Z, domain=sp.ZZ)
    phi = sp.Poly(sp.cyclotomic_poly(K, Z), Z, domain=sp.ZZ)
    assert lift == phi
    print(f"K={K}: z^m C_K(z+z^-1)=Phi_K(z): OK")


def check_coprime_cyclotomic_resultants() -> None:
    for K in (7, 11, 13):
        phi_k = sp.Poly(sp.cyclotomic_poly(K, Z), Z, domain=sp.ZZ)
        for n in range(2, 25):
            if gcd(K, n) != 1:
                continue
            phi_n = sp.Poly(sp.cyclotomic_poly(n, Z), Z, domain=sp.ZZ)
            resultant = abs(int(sp.resultant(phi_n.as_expr(), phi_k.as_expr(), Z)))
            assert resultant == 1, (K, n, resultant)
    print("coprime-conductor cyclotomic resultant controls through n=24: OK")


def main() -> None:
    for K in (7, 11, 31, 59):
        check_edge_exponent_geometry(K)
    for K in (7, 11, 13, 31):
        check_real_reciprocal_lift(K)
    check_coprime_cyclotomic_resultants()
    print("cayley inverse torsion-factor support-free regression: OK")


if __name__ == "__main__":
    main()
