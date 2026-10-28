#!/usr/bin/env python3
"""Exact integer certificate for BGS-TRACE-119.

Recomputes the 32-mode archimedean bound, the pigeonhole diameter at
degree <= 11, the norm obstruction at diameter 186, the gap comparison
4860*beta^5 < 1, the window activities through degree 11, the degree
tail at x < 7/2, and the cleared Abel comparison at N = u_205 with
room 1/12.  No floating comparison is used.  A pass does not prove
BGS-TRACE-005.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MAJORANT = Fraction(184981, 160000)
SIGMA = Fraction(66033, 160000)
SIGMA_EFF = Fraction(1650797, 4000000)
B_NUM = 184981
B_DEN = 160000


def pell_through(n: int) -> list[tuple[int, int]]:
    rows = [(1, 0)]
    u, v = 1, 0
    for m in range(1, n + 1):
        u, v = u + 2 * v, u + v
        sign = -1 if m % 2 else 1
        if u * u - 2 * v * v != sign:
            raise RuntimeError(f"norm failed at m={m}")
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


def f_coeff(k: int, ell: int) -> tuple[Fraction, Fraction]:
    re = im = Fraction(0)
    if ell == 0:
        if abs(k) == 7:
            re += Fraction(1, 2)
        re += r_coeff(k) / 10
        im += (r_coeff(k + 1) - r_coeff(k - 1)) / 200
        if k == 0:
            re -= Fraction(1, 10)
    elif ell == 1:
        rc = r_coeff(k)
        re += rc * Fraction(-3, 1000)
        im += rc * Fraction(-4, 1000)
    elif ell == -1:
        rc = r_coeff(k)
        re += rc * Fraction(-3, 1000)
        im += rc * Fraction(4, 1000)
    return re, im


def positive(a: int, b: int) -> bool:
    """a + b*sqrt(2) > 0."""
    if b >= 0:
        if a >= 0:
            return (a, b) != (0, 0)
        return 2 * b * b > a * a
    return a > 0 and a * a > 2 * b * b


def abs_le_18(p: int, q: int) -> bool:
    """|p + q*sqrt(2)| <= 18."""
    aa = p * p + 2 * q * q - 324
    bb = 2 * p * q
    return not positive(aa, bb)


def mode_bound() -> int:
    count = 0
    sigma = Fraction(0)
    total = Fraction(0)
    for k in range(-9, 10):
        for ell in range(-1, 2):
            re, im = f_coeff(k, ell)
            cre, cim = f_coeff(-k, -ell)
            if cre != re or cim != -im:
                raise RuntimeError(f"Hermitian symmetry failed at {(k, ell)}")
            if re == 0 and im == 0:
                continue
            count += 1
            sigma += re * re + im * im
            if not abs_le_18(2 * k, ell) or not abs_le_18(2 * k, -ell):
                raise RuntimeError(f"archimedean mode exceeds 18 at {(k, ell)}")
            mag2 = re * re + im * im
            # The same strict square-root step as TRACE-118, recomputed so
            # the constant B used below is the majorant of this support.
            p, q = mag2.numerator, mag2.denominator
            root = math.isqrt(p * q)
            upper = Fraction(root + 1, q)
            if upper * upper <= mag2:
                raise RuntimeError(f"majorant is not strict at {(k, ell)}")
            total += upper
    if count != 32:
        raise RuntimeError(f"expected 32 modes, found {count}")
    if sigma != SIGMA:
        raise RuntimeError(f"sigma changed: {sigma}")
    if total != MAJORANT:
        raise RuntimeError(f"majorant changed: {total}")
    return count


def pigeonhole() -> None:
    worst = 0
    for m in range(1, 12):
        ceiling = (205 + m - 1) // m
        if (ceiling - 1) * m >= 205 or ceiling * m < 205:
            raise RuntimeError(f"ceiling arithmetic failed at m={m}")
        diameter = 205 - ceiling
        worst = max(worst, diameter)
        if 4 * (m - 1) > 40:
            raise RuntimeError("gap diameter escaped the activity window")
    if worst != 186:
        raise RuntimeError(f"pigeonhole diameter is {worst}, not 186")


def norm_block(rows: list[tuple[int, int]], capital: int) -> None:
    u, v = rows[372]
    c = (18 * 11) ** 2
    left = 2 * capital * capital
    if c * u >= left:
        raise RuntimeError("norm block: archimedean side is not smaller than 2N^2")
    diff = left - c * u
    if diff * diff <= 2 * (c * v) ** 2:
        raise RuntimeError("norm block failed at m=11, D=186")


def gap_block(rows: list[tuple[int, int]]) -> None:
    u, v = rows[10]
    if (u, v) != (3363, 2378):
        raise RuntimeError(f"unexpected Pell pair at m=10: {(u, v)}")
    c = 162 * 30
    if c * u <= 1:
        raise RuntimeError("gap comparison is on the wrong side of 1")
    right = c * u - 1
    if 2 * (c * v) ** 2 <= right * right:
        raise RuntimeError("4860 beta^5 is not strictly less than 1")
    # KT <= 30 for every cut of an 11-mode diagram.
    worst = 0
    for k in range(1, 11):
        for t in range(1, 12 - k):
            worst = max(worst, k * t)
    if worst != 30:
        raise RuntimeError(f"worst KT is {worst}")


def activity(capital: int) -> tuple[Fraction, Fraction, Fraction]:
    theta = Fraction(capital, 10**80)
    theta_b = theta * MAJORANT
    x = 205 * theta_b
    if not (x < Fraction(7, 2) < 13):
        raise RuntimeError("x is not inside the tail interval")
    phi2 = 205 * (2**2 - 1**2) * theta_b**2 / 2
    phi3 = Fraction(0)
    for m in range(3, 12):
        w = 4 * (m - 1) + 1
        phi3 += 205 * (w**m - (w - 1) ** m) * theta_b**m / math.factorial(m)
    if not (phi2 < Fraction(9, 100)):
        raise RuntimeError("Phi_2 is not below 9/100")
    if not (phi3 < Fraction(1, 23)):
        raise RuntimeError("Phi_(>=3) is not below 1/23")
    if Fraction(9, 100) + Fraction(1, 23) >= Fraction(7, 50):
        raise RuntimeError("coarse activity sum is not below 7/50")
    tail_bar = (Fraction(7, 2) ** 12) / math.factorial(12) * 13 / (13 - Fraction(7, 2))
    if not (tail_bar < Fraction(1, 100)):
        raise RuntimeError("tail majorant at 7/2 is not below 1/100")
    rem = (Fraction(7, 50) ** 2) / (2 * (1 - Fraction(7, 50) / 3))
    err = rem + Fraction(1, 23) + Fraction(1, 100)
    if err != Fraction(2097, 32890):
        raise RuntimeError(f"coarse error changed: {err}")
    if not (err < Fraction(1, 12)):
        raise RuntimeError("coarse error is not below 1/12")
    return phi2, phi3, x


def abel(capital: int) -> int:
    den = 8 * 10**166
    num = 205 * 1650797 * capital * capital
    if 11 * den <= 12 * num:
        raise RuntimeError("1 - eps2 - 1/12 is not positive")
    left = 4 * (capital - 410) * (11 * den - 12 * num) ** 2
    right = 3 * capital * (12 * den) ** 2
    if left <= right:
        raise RuntimeError("Abel comparison failed")
    return left - right


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    count = mode_bound()
    pigeonhole()
    rows = pell_through(372)
    capital = rows[205][0]
    if rows[205][0] * rows[205][0] - 2 * rows[205][1] * rows[205][1] != -1:
        raise RuntimeError("norm at n=205 failed")
    norm_block(rows, capital)
    gap_block(rows)
    phi2, phi3, _ = activity(capital)
    margin = abel(capital)
    sources = {
        "python": "computations/verification/positive_time_spike.py",
        "cpp": "computations/cpp/positive_time_spike.cpp",
        "lean": "formalization/Bgs/PositiveTimeRational.lean",
        "proof": "mathematics/fixed-map/positive_time_spike.md",
    }
    payload = {
        "schema": "bgs-positive-time-spike-v1",
        "claim": "BGS-TRACE-119",
        "n": 205,
        "u_205_digits": len(str(capital)),
        "u_205": str(capital),
        "norm_205": -1,
        "mode_count": count,
        "sigma": "66033/160000",
        "sigma_eff": "1650797/4000000",
        "majorant": "184981/160000",
        "pigeonhole_diameter": 186,
        "indecomposable_gap_at_most": 4,
        "phi2_below": "9/100",
        "phi3_below": "1/23",
        "error_below": "1/12",
        "coarse_error": "2097/32890",
        "abel_clears_three_quarters": True,
        "margin_digits": len(str(margin)),
        "phi2": str(phi2),
        "phi3": str(phi3),
        "sources_sha256": {name: sha256(ROOT / rel) for name, rel in sources.items()},
        "nonclaim": (
            "Does not prove BGS-TRACE-005, BGS-BGS-001, the limit, "
            "a gap at a generic odd dimension, or a positive lower bound at n=207. "
            "The n=207 second-order disk remains below 3/4."
        ),
    }
    text = json.dumps(payload, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(
        f"positive_time_spike passed u_205_digits={len(str(capital))} "
        f"modes={count} gap<=4 error<1/12 margin_digits={len(str(margin))}"
    )


if __name__ == "__main__":
    main()
