#!/usr/bin/env python3
"""Exact integer certificate for BGS-TRACE-118.

Recomputes the 32-mode Hilbert--Schmidt mass, the rational majorant of
||A_N||, the Pell numbers through n=205, the support resonances of C^r
modulo u_203, and the cleared Abel comparison at N=u_203.  The same
third-order majorant is required to be at least 1 at n=205.  No floating
comparison is used.  A pass does not prove BGS-TRACE-005.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MAJORANT = Fraction(184981, 160000)
SIGMA = Fraction(66033, 160000)
GAMMA = Fraction(-7, 2000000)
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
        if u % 2 == 0:
            raise RuntimeError(f"u parity failed at m={m}")
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
    re = im = Fraction(0)
    if l == 0:
        if abs(k) == 7:
            re += Fraction(1, 2)
        re += r_coeff(k) / 10
        im += (r_coeff(k + 1) - r_coeff(k - 1)) / 200
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


def majorant() -> tuple[Fraction, int, Fraction]:
    total = Fraction(0)
    sigma = Fraction(0)
    count = 0
    mode70 = None
    for k in range(-9, 10):
        for ell in range(-1, 2):
            re, im = f_coeff(k, ell)
            cre, cim = f_coeff(-k, -ell)
            if cre != re or cim != -im:
                raise RuntimeError(f"Hermitian symmetry failed at {(k, ell)}")
            if re == 0 and im == 0:
                continue
            count += 1
            mag2 = re * re + im * im
            sigma += mag2
            p, q = mag2.numerator, mag2.denominator
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
    if sigma != SIGMA:
        raise RuntimeError(f"sigma changed: {sigma}")
    return total, count, sigma


def support_modes() -> list[tuple[int, int, Fraction, Fraction]]:
    modes = []
    for k in range(-9, 10):
        for ell in range(-1, 2):
            re, im = f_coeff(k, ell)
            if re or im:
                modes.append((k, ell, re, im))
    return modes


def exact_lag_one() -> None:
    """Hand classification: C(k, ell) lands in the negative box only twice."""
    hits = []
    for k in range(-9, 10):
        for ell in range(-1, 2):
            ck, cell = 3 * k + 2 * ell, 4 * k + 3 * ell
            if abs(ck) <= 9 and abs(cell) <= 1:
                hits.append(((k, ell), (ck, cell)))
    expected = {
        ((-1, 1), (-1, -1)),
        ((1, -1), (1, 1)),
        ((0, 0), (0, 0)),
    }
    if set(hits) != expected:
        raise RuntimeError(f"lag-one box hits changed: {hits}")


def archimedean_square() -> None:
    # (17+12√2)(2-√2) = 10+7√2, and (10+7√2)^2 - (18+√2)^2 = 104√2 - 128.
    if 34 - 24 != 10 or -17 + 24 != 7:
        raise RuntimeError("fourth-power expansion failed")
    if 104 * 104 * 2 <= 128 * 128:
        raise RuntimeError("archimedean square failed")


def gamma_by_hand() -> Fraction:
    """c_(1,1) c_(-1,1) + c_(-1,-1) c_(1,-1) = -7/2000000."""
    c11 = f_coeff(1, 1)
    cm11 = f_coeff(-1, 1)
    cm1m1 = f_coeff(-1, -1)
    c1m1 = f_coeff(1, -1)
    def mul(a, b):
        return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])
    p = mul(c11, cm11)
    q = mul(cm1m1, c1m1)
    total = (p[0] + q[0], p[1] + q[1])
    if total[1] != 0 or total[0] != GAMMA:
        raise RuntimeError(f"hand gamma changed: {total}")
    if SIGMA + 2 * GAMMA != SIGMA_EFF:
        raise RuntimeError("sigma_eff mismatch")
    return total[0]


def resonances(rows: list[tuple[int, int]]) -> dict:
    n = 203
    capital = rows[n][0]
    modes = support_modes()
    coeff = {(k, ell): (re, im) for k, ell, re, im in modes}
    # Pell coefficients modulo N, up to index 2*(n-1).
    umod = [0] * (2 * (n - 1) + 1)
    vmod = [0] * (2 * (n - 1) + 1)
    for m in range(0, 2 * (n - 1) + 1):
        uu, vv = rows[m]
        umod[m] = uu % capital
        vmod[m] = vv % capital
    # C^n = I mod N.
    u2n, v2n = rows[2 * n]
    if (u2n - 1) % capital or v2n % capital:
        raise RuntimeError("C^n is not I mod u_n")
    found = []
    for r in range(1, n):
        uu, vv = umod[2 * r], vmod[2 * r]
        gre = gim = Fraction(0)
        for k, ell, _, _ in modes:
            x = (uu * k + vv * ell) % capital
            y = (uu * ell + 2 * vv * k) % capital
            for k2, ell2, _, _ in modes:
                if (x + k2) % capital == 0 and (y + ell2) % capital == 0:
                    re_w, im_w = coeff[(k, ell)]
                    re_v, im_v = coeff[(k2, ell2)]
                    gre += re_v * re_w - im_v * im_w
                    gim += re_v * im_w + im_v * re_w
                    found.append((r, (k, ell), (k2, ell2)))
        if r not in (1, n - 1):
            if gre != 0 or gim != 0:
                raise RuntimeError(f"unexpected correlation at r={r}")
        else:
            if gre != GAMMA or gim != 0:
                raise RuntimeError(f"gamma({r}) changed: {gre}+{gim}i")
    expected = {
        (1, (-1, 1), (1, 1)),
        (1, (1, -1), (-1, -1)),
        (202, (1, 1), (-1, 1)),
        (202, (-1, -1), (1, -1)),
    }
    got = {(r, w, v) for r, w, v in found}
    if got != expected:
        raise RuntimeError(f"resonance list changed: {sorted(got)}")
    return {"hit_count": len(found), "lags": [1, n - 1]}


def size_bounds(rows: list[tuple[int, int]]) -> None:
    u200, v200 = rows[200]
    u202, v202 = rows[202]
    u203 = rows[203][0]
    if not (10 * u200 + 9 < u203):
        raise RuntimeError("size bound t<=100 on X failed")
    if not (u200 + 18 * v200 + 1 < u203):
        raise RuntimeError("size bound t<=100 on Y failed")
    if not (9 * u202 + v202 + 9 < 5 * u203):
        raise RuntimeError("size bound t=101 on X failed")
    if not (u202 + 18 * v202 + 1 < 6 * u203):
        raise RuntimeError("size bound t=101 on Y failed")
    if not (u203 > 326):
        raise RuntimeError("u_203 is not larger than the quadratic gap")
    # |a|<=4 and |b|<=5, so |2(2 a k' - b ell')| <= 2(18*4+5) = 154.
    if not (u203 > 154):
        raise RuntimeError("u_203 does not dominate the linear form")


def cleared_parts(n: int, capital: int, sigma_eff: Fraction) -> tuple[int, int, int]:
    """Return (den3, num_e, scale) for the exact second-moment comparison."""
    ten = 10
    den2 = 8 * ten ** 166
    num2 = n * sigma_eff.numerator * capital * capital
    if sigma_eff.denominator != 4000000:
        raise RuntimeError("sigma_eff denominator drifted")
    den3 = 6 * ten ** 240 * B_DEN ** 3
    num3 = n ** 3 * capital ** 3 * B_NUM ** 3
    scale = 3 * (2 ** 96) * (5 ** 86)
    if scale * den2 != den3:
        raise RuntimeError("denominator scale is inexact")
    num_e = num2 * scale + num3
    if den3 <= num_e:
        raise RuntimeError("epsilon is not strictly less than 1")
    return den3, num_e, scale


def quadrature_gap(n: int, capital: int, sigma_eff: Fraction) -> bool:
    den3, num_e, _ = cleared_parts(n, capital, sigma_eff)
    left = 4 * (capital - 2 * n) * (den3 - num_e) ** 2
    right = 3 * capital * den3 ** 2
    return left > right


def fraction_gap(n: int, capital: int, sigma_eff: Fraction) -> bool:
    theta = Fraction(capital, 10 ** 80)
    eps2 = n * sigma_eff * theta * theta / 2
    eps3 = (n * theta * MAJORANT) ** 3 / 6
    if eps2 + eps3 >= 1:
        return False
    lower = (1 - Fraction(2 * n, capital)) * (1 - eps2 - eps3) ** 2
    return lower > Fraction(3, 4)


def one_term_fails(n: int, capital: int) -> bool:
    x_num = capital * B_NUM
    x_den = 10 ** 80 * B_DEN
    if x_den <= (n + 1) * x_num:
        return True
    left = 4 * (x_den - (n + 1) * x_num) ** 2 * (capital - 2 * n)
    right = 3 * capital * (x_den - x_num) ** 2
    return left <= right


def sentinel_vacuous(n: int, capital: int) -> bool:
    # (n θ B)^3 / 6 >= 1
    left = (n * capital * B_NUM) ** 3
    right = 6 * (10 ** 80) ** 3 * B_DEN ** 3
    return left >= right


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    archimedean_square()
    exact_lag_one()
    gamma_by_hand()
    _, count, sigma = majorant()
    rows = pell_through(410)
    if rows[5][0] != 41 or rows[7][0] != 239 or rows[9][0] != 1393:
        raise RuntimeError("Pell bases changed")
    size_bounds(rows)
    scan = resonances(rows)
    capital = rows[203][0]
    if not quadrature_gap(203, capital, SIGMA_EFF):
        raise RuntimeError("quadrature gap failed at n=203")
    if not fraction_gap(203, capital, SIGMA_EFF):
        raise RuntimeError("fraction gap disagrees with the cleared form")
    if not one_term_fails(203, capital):
        raise RuntimeError("one-term bound unexpectedly still beats 3/4")
    if not sentinel_vacuous(205, rows[205][0]):
        raise RuntimeError("n=205 remainder is still below 1")
    # The coarser Lean majorants must also clear 3/4.
    theta = Fraction(capital, 10 ** 80)
    eps2 = 203 * SIGMA_EFF * theta * theta / 2
    eps3 = (203 * theta * MAJORANT) ** 3 / 6
    delta = Fraction(406, capital)
    if not (eps2 < Fraction(1, 1000) and eps3 < Fraction(1, 25) and delta < Fraction(1, 1000)):
        raise RuntimeError("coarse majorants are not inside the Lean budget")
    coarse = (1 - Fraction(1, 1000)) * (1 - Fraction(1, 25) - Fraction(1, 1000)) ** 2
    if coarse <= Fraction(3, 4):
        raise RuntimeError("coarse product does not beat 3/4")
    den3, num_e, _ = cleared_parts(203, capital, SIGMA_EFF)
    margin = 4 * (capital - 406) * (den3 - num_e) ** 2 - 3 * capital * den3 ** 2
    if margin <= 0:
        raise RuntimeError("margin is not positive")
    sources = {
        "python": "computations/verification/orbit_orthogonal_spike.py",
        "cpp": "computations/cpp/orbit_orthogonal_spike.cpp",
        "lean": "formalization/Bgs/OrbitOrthogonalRational.lean",
        "proof": "mathematics/fixed-map/orbit_orthogonal_kick_spike.md",
    }
    payload = {
        "schema": "bgs-orbit-orthogonal-spike-v1",
        "claim": "BGS-TRACE-118",
        "n": 203,
        "u_203_digits": len(str(capital)),
        "u_203": str(capital),
        "norm_203": -1,
        "mode_count": count,
        "sigma": "66033/160000",
        "gamma_lag_one": "-7/2000000",
        "sigma_eff": "1650797/4000000",
        "majorant": "184981/160000",
        "resonances": scan,
        "quadrature_beats_three_quarters": True,
        "one_term_beats_three_quarters": False,
        "sentinel_205_remainder_at_least_one": True,
        "margin_digits": len(str(margin)),
        "coarse_eps2_below": "1/1000",
        "coarse_eps3_below": "1/25",
        "sources_sha256": {name: sha256(ROOT / rel) for name, rel in sources.items()},
        "nonclaim": (
            "Does not prove BGS-TRACE-005, BGS-BGS-001, the limit, "
            "a gap at a generic odd dimension, or a positive lower bound at n=205."
        ),
    }
    text = json.dumps(payload, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
