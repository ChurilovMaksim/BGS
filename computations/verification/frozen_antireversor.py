#!/usr/bin/env python3
"""Exact integer certificate for BGS-FM-009, from the submitted PDF.

Only integer/rational arithmetic is used. No eigenvalues, floating-point
approximations, parameter averages, or statistical simulations occur.
This is a source-level transcription of the uploaded 24 September 2026
verify_certificate.py. Its exhaustive cyclotomic screen depends on the
all-order algebraic reduction in mathematics/frozen_common_antireversor_certificate.md.

Run with Python 3.10 or later:
    python -S computations/verification/frozen_antireversor.py \
      --output-dir build/antireversor
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import argparse
import hashlib
import json
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import gcd, isqrt, prod
from pathlib import Path

Vec = tuple[int, int]
Gauss = tuple[int, int]


def add(v: Vec, w: Vec) -> Vec:
    return v[0] + w[0], v[1] + w[1]


def omega(v: Vec, w: Vec) -> int:
    return v[0] * w[1] - v[1] * w[0]


def multiply(c: Gauss, d: Gauss) -> Gauss:
    return c[0]*d[0] - c[1]*d[1], c[0]*d[1] + c[1]*d[0]


def gaussian_add(c: Gauss, d: Gauss) -> Gauss:
    return c[0] + d[0], c[1] + d[1]


def coefficients() -> dict[Vec, Gauss]:
    """The exact coefficients d_v = 4000 c_v of 4000 A_N."""
    result: dict[Vec, Gauss] = {}
    diagonal = {
        1: (200, -20), 2: (0, -10), 5: (0, -5),
        6: (-100, -10), 7: (1800, 0),
        8: (-100, 10), 9: (0, 5)
    }
    for k, c in diagonal.items():
        result[(0, k)] = c
        result[(0, -k)] = (c[0], -c[1])
    r = {
        0: Fraction(1), 1: Fraction(1, 2), -1: Fraction(1, 2),
        6: Fraction(-1, 4), -6: Fraction(-1, 4),
        7: Fraction(-1, 2), -7: Fraction(-1, 2),
        8: Fraction(-1, 4), -8: Fraction(-1, 4)
    }
    for k, value in r.items():
        assert (4*value).denominator == 1
        d = int(4*value)
        result[(1, k)] = (-3*d, -4*d)
        result[(-1, k)] = (-3*d, 4*d)
    assert len(result) == 32
    assert all(result[(-a, -b)] == (c[0], -c[1])
               for (a, b), c in result.items())
    return result


def exponent(v: Vec, w: Vec, u: Vec, sign: int) -> int:
    """sign=+1 corresponds to S; sign=-1 corresponds to S^2."""
    a, b = add(v, w)
    c, d = u
    return (
        5*(2*b*b - a*a) + 5*(2*d*d - c*c)
        + 14*omega(v, w) - 2*a*c + 4*b*d
        + sign*2*omega((a, b), u)
    )


def build() -> tuple[dict[int, int], dict[int, int], list[dict]]:
    coeff = coefficients()
    poly = defaultdict(lambda: (0, 0))
    poly7 = defaultdict(lambda: (0, 0))
    witnesses = []
    words = [
        (-1, 1, "S^2", ((17, 24), (12, 17))),
        (1, -1, "S", ((3, 4), (2, 3)))
    ]
    for v, w, u in product(coeff, repeat=3):
        c = multiply(multiply(coeff[v], coeff[w]), coeff[u])
        for sign, prefactor, label, matrix in words:
            e = exponent(v, w, u, sign)
            assert -5051 <= e <= 5051
            term = (prefactor*c[0], prefactor*c[1])
            poly[e] = gaussian_add(poly[e], term)
            if e == 4211:
                witnesses.append({
                    "word": label, "v": v, "w": w, "u": u,
                    "coefficient": term
                })
            su = (
                matrix[0][0]*u[0] + matrix[0][1]*u[1],
                matrix[1][0]*u[0] + matrix[1][1]*u[1]
            )
            total = add(add(v, w), su)
            direct = (14*omega(v, w) + 14*omega(add(v, w), su)
                      + 5*(2*total[1]*total[1] - total[0]*total[0]))
            assert e == direct
            if total[0] % 7 == 0 and total[1] % 7 == 0:
                assert e % 7 == 0
                poly7[e//7] = gaussian_add(poly7[e//7], term)

    def real_nonzero(raw):
        assert all(c[1] == 0 for c in raw.values())
        return {e: c[0] for e, c in raw.items() if c[0] != 0}

    return real_nonzero(poly), real_nonzero(poly7), witnesses


def f2_divmod(a: int, b: int) -> tuple[int, int]:
    """Polynomial division over F_2, using integer bits as coefficients."""
    if not b:
        raise ZeroDivisionError("zero polynomial")
    quotient = 0
    degree_plus_one = b.bit_length()
    while a and a.bit_length() >= degree_plus_one:
        shift = a.bit_length() - degree_plus_one
        quotient ^= 1 << shift
        a ^= b << shift
    return quotient, a


def f2_remainder(a: int, b: int) -> int:
    if not b:
        raise ZeroDivisionError("zero polynomial")
    degree_plus_one = b.bit_length()
    while a and a.bit_length() >= degree_plus_one:
        a ^= b << (a.bit_length() - degree_plus_one)
    return a


def euler_phi(n: int) -> int:
    if n < 1:
        raise ValueError("n must be positive")
    answer = n
    p = 2
    while p*p <= n:
        if n % p == 0:
            answer = answer//p*(p-1)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        answer = answer//n*(n-1)
    return answer


@lru_cache(None)
def phi_f2(n: int) -> int:
    """Cyclotomic polynomial Phi_n reduced modulo 2, encoded in bits."""
    if n == 1:
        return 3  # X + 1
    prime = next((p for p in range(2, isqrt(n)+1) if n % p == 0), n)
    m = n // prime
    f = phi_f2(m)
    substituted = 0
    while f:
        lowest_bit = f & -f
        exponent = lowest_bit.bit_length() - 1
        substituted |= 1 << (prime*exponent)
        f ^= lowest_bit
    if m % prime == 0:
        return substituted
    quotient, remainder = f2_divmod(substituted, phi_f2(m))
    assert remainder == 0
    return quotient


def root_of_unity_screen(poly: dict[int, int], divisible_by_7: bool) -> dict:
    """Finite necessary test for an odd-order cyclotomic factor over Q.

    For odd n, phi(n) >= sqrt(n). If phi(n) <= degree D, then n <= D^2.
    Bounding the number of distinct odd prime factors of n gives the
    sharper finite upper limit below.
    """
    low = min(poly)
    degree = max(poly) - low
    content = gcd(*(abs(c) for c in poly.values()))
    primitive_mod2 = sum(
        1 << (e-low) for e, c in poly.items() if (c//content) % 2
    )
    assert primitive_mod2 != 0
    primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    primorial = 1
    allowed_primes = []
    for prime in primes:
        if primorial*prime > degree*degree:
            break
        primorial *= prime
        allowed_primes.append(prime)
    else:
        raise AssertionError("extend prime list")
    ratio = prod((Fraction(p, p-1) for p in allowed_primes), start=Fraction(1))
    upper_n = degree*ratio.numerator//ratio.denominator
    candidates = []
    tested = 0
    for n in range(1, upper_n+1, 2):
        if (n % 7 == 0) != divisible_by_7 or euler_phi(n) > degree:
            continue
        cyclotomic = phi_f2(n)
        assert cyclotomic.bit_length()-1 == euler_phi(n)
        tested += 1
        if f2_remainder(primitive_mod2, cyclotomic) == 0:
            candidates.append(n)
    return {
        "minimum_exponent": low,
        "maximum_exponent": max(poly),
        "degree_after_shift": degree,
        "integer_content": content,
        "degree_mod_2": primitive_mod2.bit_length()-1,
        "odd_prime_factor_bound": allowed_primes,
        "finite_upper_n": upper_n,
        "number_of_orders_tested": tested,
        "possible_cyclotomic_orders_mod_2": candidates
    }


def csv_body(poly: dict[int, int]) -> str:
    return "".join(f"{e},{poly[e]}\n" for e in sorted(poly))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()

    poly, poly7, witnesses = build()
    assert len(poly) == 2225 and min(poly) == -238 and max(poly) == 4211
    assert poly[4211] == -8000 and poly[-238] == 1920
    assert len(witnesses) == 4
    assert len(poly7) == 120 and min(poly7) == -18 and max(poly7) == 527
    assert poly7[527] == 16000 and poly7[-18] == -960

    screen = root_of_unity_screen(poly, False)
    screen7 = root_of_unity_screen(poly7, True)
    assert screen["integer_content"] == 160
    assert screen7["integer_content"] == 160
    assert screen["finite_upper_n"] == 13006
    assert screen7["finite_upper_n"] == 1509
    assert screen["possible_cyclotomic_orders_mod_2"] == [1, 3]
    assert screen7["possible_cyclotomic_orders_mod_2"] == [7]

    # Remainder of Q=X^238 P/160 modulo Phi_3=X^2+X+1:
    residues3 = [0, 0, 0]
    for e, c in poly.items():
        residues3[(e+238) % 3] += c//160
    remainder3 = [residues3[0]-residues3[2], residues3[1]-residues3[2]]
    assert remainder3 == [0, -51462]

    # Phi_7 actually divides Q7=X^18 P7/160:
    residues7 = [0]*7
    for e, c in poly7.items():
        residues7[(e+18) % 7] += c//160
    assert len(set(residues7)) == 1

    result = {
        "status": "all exact checks passed",
        "support_size_A": 32,
        "polynomial_P": {
            "number_of_terms": len(poly), **screen,
            "coefficient_z_4211": poly[4211],
            "remainder_Q_mod_Phi3_low_to_high": remainder3,
            "csv_sha256_without_header": hashlib.sha256(csv_body(poly).encode()).hexdigest()
        },
        "polynomial_P7": {
            "number_of_terms": len(poly7), **screen7,
            "coefficient_z_527": poly7[527],
            "Phi7_divides_Q7": True,
            "csv_sha256_without_header": hashlib.sha256(csv_body(poly7).encode()).hexdigest()
        },
        "four_contributors_to_P_z_4211": witnesses,
        "conclusion": (
            "For every odd N>=3 except N=7, Tr([A_N,M_N]^3) is nonzero. "
            "At N=7, A_N=(9/10) I."
        )
    }
    output = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output_dir:
        args.output_dir.mkdir(parents=True, exist_ok=True)
        for name, polynomial in [("certificate_polynomial.csv", poly),
                                  ("certificate_polynomial_7.csv", poly7)]:
            (args.output_dir/name).write_text(
                "exponent,coefficient\n"+csv_body(polynomial), encoding="utf-8"
            )
        (args.output_dir/"certificate_result.json").write_text(output, encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
