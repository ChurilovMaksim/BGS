#!/usr/bin/env python3
"""Exact integer certificate for BGS-TRACE-117.

Recomputes the Pell companion through n=203, the 32-mode majorant of
||A_N||, the phase-polynomial identity, the uniform rational comparison
for odd n from 7 through 201, the separate n=5 endpoint, and the direct
Abel gap at every odd n in that range.  The same direct gap is required
to fail at the sentinel n=203.  No floating comparison is used.  A pass
does not prove BGS-TRACE-005.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
MAJORANT = Fraction(184981, 160000)
TAU = Fraction(1, 10**80)
XDEN_UNIT = 10**80 * 160000


def pell_through(n: int) -> list[tuple[int, int]]:
    """Return (u_m, v_m) for m = 0..n.

    u_m stays odd.  v_m is even for every m >= 2 (v_2 = 2); do not require
    v odd.
    """
    rows = [(1, 0)]
    u, v = 1, 0
    for m in range(1, n + 1):
        u, v = u + 2 * v, u + v
        sign = -1 if m % 2 else 1
        if u * u - 2 * v * v != sign:
            raise RuntimeError(f"norm failed at m={m}")
        if u % 2 == 0:
            raise RuntimeError(f"u parity failed at m={m}")
        if m >= 3:
            u_m2, _ = rows[m - 2]
            u_m3, _ = rows[m - 3]
            if u != 5 * u_m2 + 2 * u_m3:
                raise RuntimeError(f"recurrence identity failed at m={m}")
        rows.append((u, v))
    return rows


def r_coeff(k: int) -> Fraction:
    if k == 0:
        return Fraction(1)
    if abs(k) == 1:
        return Fraction(1, 2)
    if abs(k) == 7:
        return Fraction(-1, 2)
    if abs(k) in (6, 8):
        return Fraction(-1, 4)
    return Fraction(0)


def f_coeff(k: int, l: int) -> tuple[Fraction, Fraction]:
    """Real and imaginary parts of fCoeff in TraceStatement.lean.

    The sine contribution is (r(k-1) - r(k+1)) / (200 i) = -i times that
    real number, hence imaginary part (r(k+1) - r(k-1)) / 200.
    """
    re = im = Fraction(0)
    if l == 0:
        if abs(k) == 7:
            re += Fraction(1, 2)
        re += r_coeff(k) / 10
        im += -(r_coeff(k - 1) - r_coeff(k + 1)) / 200
        if k == 0:
            re -= Fraction(1, 10)
    elif l == 1:
        rc = r_coeff(k)
        re += rc * Fraction(-3, 1000)
        im += rc * Fraction(-4, 1000)
    elif l == -1:
        rc = r_coeff(k)
        re += rc * Fraction(-3, 1000)
        im += rc * Fraction(4, 1000)
    return re, im


def isqrt(n: int) -> int:
    """Floor square root by integer Newton iteration. No binary floating point."""
    if n < 0:
        raise RuntimeError("isqrt of a negative integer")
    if n < 2:
        return n
    x = 1 << ((n.bit_length() + 1) // 2)
    while True:
        y = (x + n // x) // 2
        if y >= x:
            if x * x > n or (x + 1) * (x + 1) <= n:
                raise RuntimeError("isqrt missed the floor")
            return x
        x = y


def majorant() -> tuple[Fraction, int]:
    total = Fraction(0)
    count = 0
    mode70 = None
    for k in range(-9, 10):
        for ell in range(-1, 2):
            re, im = f_coeff(k, ell)
            if re == 0 and im == 0:
                continue
            count += 1
            mag2 = re * re + im * im
            p, q = mag2.numerator, mag2.denominator
            # sqrt(p/q) < (isqrt(p*q)+1)/q
            upper = Fraction(isqrt(p * q) + 1, q)
            if upper * upper <= mag2:
                raise RuntimeError(f"majorant is not strict at {(k, ell)}")
            total += upper
            if (k, ell) == (7, 0):
                mode70 = (re, im)
    if count != 32 or mode70 != (Fraction(9, 20), Fraction(0)):
        raise RuntimeError(f"unexpected Fourier data: count={count}, (7,0)={mode70}")
    if total != MAJORANT:
        raise RuntimeError(f"majorant changed: {total}")
    return total, count


def phase_identity() -> None:
    x, z, k, ell = sp.symbols("x z k ell")

    def q(a, b):
        return -sp.Rational(1, 8) * (3 * a**2 - 2 * a * b + 3 * b**2)

    h = sp.Rational(1, 2)
    phase_mw = sp.expand(q(x, z - ell) + k * (z - h * ell))
    n = 3 * k + 2 * ell
    shift = 4 * k + 3 * ell
    phase_wm = sp.expand(n * (x + h * shift) + q(x + shift, z))
    displayed = sp.expand(
        -k * ell / 2
        + k * z
        - sp.Rational(3, 8) * ell**2
        - ell * x / 4
        + sp.Rational(3, 4) * ell * z
        - sp.Rational(3, 8) * x**2
        + x * z / 4
        - sp.Rational(3, 8) * z**2
    )
    if sp.expand(phase_wm - phase_mw) != 0 or sp.expand(phase_mw - displayed) != 0:
        raise RuntimeError("conjugation phases differ")


def x_parts(capital_n: int) -> tuple[int, int]:
    return capital_n * 184981, XDEN_UNIT


def rho_of(n: int, capital_n: int) -> Fraction:
    x_num, x_den = x_parts(capital_n)
    if x_den <= (n + 1) * x_num:
        raise RuntimeError(f"rho is not a positive contraction at n={n}")
    return Fraction(n * x_num, x_den - x_num)


def direct_lower(n: int, capital_n: int) -> Fraction:
    rho = rho_of(n, capital_n)
    return (1 - rho) ** 2 * (1 - Fraction(2 * n, capital_n))


def cleared_direct(n: int, capital_n: int) -> bool:
    x_num, x_den = x_parts(capital_n)
    if x_den <= (n + 1) * x_num:
        return False
    left = 4 * (x_den - (n + 1) * x_num) ** 2 * (capital_n - 2 * n)
    right = 3 * capital_n * (x_den - x_num) ** 2
    return left > right


def uniform_and_endpoint(rows: list[tuple[int, int]]) -> dict:
    if Fraction(7, 100) >= Fraction(1, 4) or Fraction(9, 35) >= 1:
        raise RuntimeError("induction constants are not contractive")
    if 10 * 4 >= 41 or 14 * 4 >= 239:
        raise RuntimeError("pure-cat bases failed")
    if rows[5][0] != 41 or rows[7][0] != 239:
        raise RuntimeError("u_5 or u_7 mismatch")
    # n=5 endpoint: 124 (xDen - 6 xNum)^2 > 123 (xDen - xNum)^2.
    x_num5, x_den5 = x_parts(41)
    if x_den5 <= 6 * x_num5:
        raise RuntimeError("n=5 rho sign")
    if 124 * (x_den5 - 6 * x_num5) ** 2 <= 123 * (x_den5 - x_num5) ** 2:
        raise RuntimeError("n=5 cleared gap failed")
    # Uniform comparison at n=201 against delta_7 = 14/239.
    capital = rows[201][0]
    x_num, x_den = x_parts(capital)
    if x_den <= 202 * x_num:
        raise RuntimeError("n=201 rho sign")
    left = 300 * (x_den - 202 * x_num) ** 2
    right = 239 * (x_den - x_num) ** 2
    if left <= right:
        raise RuntimeError("uniform gap failed")
    for n in range(7, 201, 2):
        u_n = rows[n][0]
        u_next = rows[n + 2][0]
        if (n + 2) * u_n >= n * u_next:
            raise RuntimeError(f"delta is not decreasing at n={n}")
        if rho_of(n, u_n) >= rho_of(n + 2, u_next):
            raise RuntimeError(f"rho is not increasing at n={n}")
    count = 0
    for n in range(5, 202, 2):
        if direct_lower(n, rows[n][0]) <= Fraction(3, 4):
            raise RuntimeError(f"direct gap failed at n={n}")
        if not cleared_direct(n, rows[n][0]):
            raise RuntimeError(f"cleared direct gap failed at n={n}")
        count += 1
    if count != 99:
        raise RuntimeError(f"odd dimension count {count}")
    # Sentinel: the one-term bound is still signed, and it no longer beats 3/4.
    if not (0 < rho_of(203, rows[203][0]) < 1):
        raise RuntimeError("sentinel rho left the contraction range")
    if direct_lower(203, rows[203][0]) > Fraction(3, 4):
        raise RuntimeError("sentinel n=203 unexpectedly still beats 3/4")
    return {
        "uniform_margin_digits": len(str(left - right)),
        "odd_dimension_count": count,
        "sentinel_below_three_quarters": True,
    }


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    phase_identity()
    major, count = majorant()
    rows = pell_through(203)
    extra = uniform_and_endpoint(rows)
    capital_n, capital_v = rows[201]
    if capital_n.bit_length() < 250:
        raise RuntimeError("u_201 has unexpected size")
    result = {
        "schema": "bgs-kick-blind-spike-v2",
        "claim": "BGS-TRACE-117",
        "status": "passed",
        "odd_n_first": 5,
        "odd_n_last": 201,
        "odd_dimension_count": extra["odd_dimension_count"],
        "sentinel_n": 203,
        "sentinel_below_three_quarters": True,
        "u_5": "41",
        "u_7": "239",
        "u_201": str(capital_n),
        "v_201": str(capital_v),
        "u_201_decimal_digits": len(str(capital_n)),
        "norm_201": str(capital_n * capital_n - 2 * capital_v * capital_v),
        "fourier_modes": count,
        "mode_7_0": "9/20",
        "majorant": "184981/160000",
        "uniform_margin_digits": extra["uniform_margin_digits"],
        "sources_sha256": {
            "computations/verification/kick_blind_spike.py": sha256(Path(__file__)),
            "computations/cpp/kick_blind_spike.cpp": sha256(
                ROOT / "computations/cpp/kick_blind_spike.cpp"
            ),
            "formalization/Bgs/KickBlindRational.lean": sha256(
                ROOT / "formalization/Bgs/KickBlindRational.lean"
            ),
        },
        "nonclaims": [
            "BGS-TRACE-005 remains open",
            "BGS-BGS-001 remains open",
            "the kicked statement is 99 explicit dimensions, not the N to infinity limit",
            "n=203 is a failure of this one-term lower bound, not a proved drop of L_N",
        ],
    }
    text = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
