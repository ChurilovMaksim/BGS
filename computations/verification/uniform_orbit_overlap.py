#!/usr/bin/env python3
"""Exact integer certificate for BGS-TRACE-125.

Recomputes the 32 Fourier modes, the mass sigma, the lag-1 overlap, the
exponent-1 box count, the archimedean integer, the quadratic seeds, and the
exhaustive support scan at N=u_5. Scans at n=7, 9 and 11 repeat the count
on indices already covered by the quadratic argument. No floating comparison
is used. A pass does not prove BGS-TRACE-005.
"""
from __future__ import annotations

from fractions import Fraction

D = 4000
SIGMA = Fraction(66033, 160000)
GAMMA = Fraction(-7, 2000000)
SIGMA_EFF = Fraction(1650797, 4000000)


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


def r_num(k: int) -> int:
    if k == 0:
        return 4
    ak = abs(k)
    if ak == 1:
        return 2
    if ak == 7:
        return -2
    if ak in (6, 8):
        return -1
    return 0


def f_num(k: int, ell: int) -> tuple[int, int]:
    if ell == 0:
        re = (2000 if abs(k) == 7 else 0) + r_num(k) * 100
        if k == 0:
            re -= 400
        im = 5 * (r_num(k + 1) - r_num(k - 1))
        return re, im
    if ell == 1:
        return -3 * r_num(k), -4 * r_num(k)
    if ell == -1:
        return -3 * r_num(k), 4 * r_num(k)
    return 0, 0


def modes() -> list[tuple[int, int, int, int]]:
    found = []
    for k in range(-9, 10):
        for ell in range(-1, 2):
            re, im = f_num(k, ell)
            cre, cim = f_num(-k, -ell)
            if cre != re or cim != -im:
                raise RuntimeError(f"Hermitian symmetry failed at {(k, ell)}")
            if re or im:
                found.append((k, ell, re, im))
    if len(found) != 32:
        raise RuntimeError(f"mode count {len(found)}")
    return found


def sigma_of(rows: list[tuple[int, int, int, int]]) -> Fraction:
    total = Fraction(0)
    for _k, _ell, re, im in rows:
        total += Fraction(re, D) ** 2 + Fraction(im, D) ** 2
    return total


def box_hits(forward: bool) -> list[tuple[int, int]]:
    hits = []
    for k in range(-9, 10):
        for ell in range(-1, 2):
            if forward:
                x, y = 3 * k + 2 * ell, 4 * k + 3 * ell
            else:
                x, y = 3 * k - 2 * ell, -4 * k + 3 * ell
            if abs(x) <= 9 and abs(y) <= 1:
                hits.append((k, ell))
    return hits


def exact_lag_one(rows: list[tuple[int, int, int, int]]) -> Fraction:
    table = {(k, ell): (re, im) for k, ell, re, im in rows}
    real = Fraction(0)
    imag = 0
    pairs = []
    for k, ell, re, im in rows:
        image = (-(3 * k + 2 * ell), -(4 * k + 3 * ell))
        if image not in table:
            continue
        re2, im2 = table[image]
        real += Fraction(re2 * re - im2 * im, D * D)
        imag += re2 * im + im2 * re
        pairs.append(((k, ell), image))
    if imag != 0 or len(pairs) != 2:
        raise RuntimeError(f"lag-1 data {real} {imag} {pairs}")
    if set(pairs) != {((1, -1), (-1, -1)), ((-1, 1), (1, 1))}:
        raise RuntimeError(f"lag-1 pairs {pairs}")
    return real


def mod(n: int, x: int) -> int:
    return x % n


def matrix_power(r: int) -> tuple[int, int, int, int]:
    a, b, c, d = 1, 0, 0, 1
    for _ in range(r):
        a, b, c, d = 3 * a + 2 * c, 3 * b + 2 * d, 4 * a + 3 * c, 4 * b + 3 * d
    return a, b, c, d


def scan(n: int, pell: list[tuple[int, int]], rows: list[tuple[int, int, int, int]]) -> dict[int, tuple[Fraction, int]]:
    modulus = pell[n][0]
    table = {(k, ell): (re, im) for k, ell, re, im in rows}
    out = {}
    for r in range(1, n):
        a, b, c, d = matrix_power(r)
        real = Fraction(0)
        imag = 0
        count = 0
        for k, ell, re, im in rows:
            x = mod(modulus, -(a * k + b * ell))
            y = mod(modulus, -(c * k + d * ell))
            # Mode labels lie in [-9, 9] x [-1, 1], and modulus >= 41.
            for kw, lw, re2, im2 in rows:
                if mod(modulus, kw) == x and mod(modulus, lw) == y:
                    real += Fraction(re2 * re - im2 * im, D * D)
                    imag += re2 * im + im2 * re
                    count += 1
        if imag != 0:
            raise RuntimeError(f"imaginary overlap at n={n}, r={r}")
        out[r] = (real, count)
    return out


def require_scan(n: int, found: dict[int, tuple[Fraction, int]]) -> None:
    for r, (value, count) in found.items():
        if r in (1, n - 1):
            if value != GAMMA or count != 2:
                raise RuntimeError(f"n={n} r={r} -> {value}, count {count}")
        elif value != 0 or count != 0:
            raise RuntimeError(f"unexpected hit n={n} r={r} -> {value}, count {count}")


def algebraic_seeds(pell: list[tuple[int, int]]) -> None:
    if pell[4] != (17, 12) or pell[5] != (41, 29) or pell[7] != (239, 169):
        raise RuntimeError(f"Pell seeds {pell[4]} {pell[5]} {pell[7]}")
    if 104 * 104 * 2 - 128 * 128 != 5248:
        raise RuntimeError("archimedean integer")
    if 66033 * 25 - 28 != 1650797 or 160000 * 25 != 4000000:
        raise RuntimeError("coefficient identity")
    if 49 * 17 * 17 - 144 * 17 - 243 != 11470:
        raise RuntimeError("quadratic seed")
    if 98 * 17 - 95 != 1571:
        raise RuntimeError("quadratic step")
    if 7 * (7 * 17 * 17 - 10 * 17 + 19) != (7 * 17 - 5) ** 2 + 108:
        raise RuntimeError("positivity identity")
    if 2 * (2 * 4 * 9 + 5) != 154:
        raise RuntimeError("right-hand side")
    if not (163 < pell[7][0] and 154 < pell[7][0]):
        raise RuntimeError("middle threshold")
    # Cleared expansions, as integer coefficient identities.
    if 81 - 2 * 16 != 49 or -2 * 72 != -144 or -81 - 2 * 81 != -243:
        raise RuntimeError("squared Pell comparison")
    # f(s+1)-f(s)-(98s-95) = 49(2s+1)-144-(98s-95), and both coefficients vanish.
    if 49 * 2 - 98 != 0 or 49 - 144 + 95 != 0:
        raise RuntimeError("difference coefficients")
    for n in range(5, 32, 2):
        u, v = pell[n - 3]
        left_x = pell[n][0] - (10 * u + 9)
        right_x = 2 * u + 5 * pell[n - 4][0] - 9
        left_y = pell[n][0] - (u + 18 * v + 1)
        right_y = 2 * pell[n - 5][0] - 1
        if left_x != right_x or left_y != right_y or left_x < 2 or left_y < 1:
            raise RuntimeError(f"size identity at n={n}")
        if n >= 7:
            uu, vv = pell[n - 1]
            if 9 * uu + vv + 9 >= 5 * pell[n][0]:
                raise RuntimeError(f"|a| room at n={n}")
            if uu + 18 * vv + 1 >= 6 * pell[n][0]:
                raise RuntimeError(f"|b| room at n={n}")
    for a in range(1, 5):
        for b in range(0, 6):
            if b * b == 2 * a * a:
                raise RuntimeError(f"2-adic exception {a}, {b}")


def main() -> None:
    pell = pell_through(40)
    rows = modes()
    sigma = sigma_of(rows)
    if sigma != SIGMA:
        raise RuntimeError(f"sigma {sigma}")
    gamma = exact_lag_one(rows)
    if gamma != GAMMA:
        raise RuntimeError(f"gamma {gamma}")
    if sigma + 2 * gamma != SIGMA_EFF:
        raise RuntimeError(f"effective mass {sigma + 2 * gamma}")
    forward = box_hits(True)
    inverse = box_hits(False)
    if set(forward) != {(0, 0), (1, -1), (-1, 1)}:
        raise RuntimeError(f"forward box {forward}")
    if set(inverse) != {(0, 0), (1, 1), (-1, -1)}:
        raise RuntimeError(f"inverse box {inverse}")
    algebraic_seeds(pell)
    for n in (5, 7, 9, 11):
        require_scan(n, scan(n, pell, rows))
    print("uniform-orbit-overlap: pass")


if __name__ == "__main__":
    main()
