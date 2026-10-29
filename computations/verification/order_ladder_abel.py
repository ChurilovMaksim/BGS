#!/usr/bin/env python3
"""Exact integer certificate for BGS-TRACE-120.

Recomputes the exponential majorants, the cleared Abel comparisons, the
two digit windows, the gcd of C^t-I, the agreement of the divisibility
order with matrix powering, the witnesses N=35, p=5 and p=7, the 32-mode
majorant, and an exact cyclotomic evaluation of |Tr M_p^m|^2 at p=5 and
p=7. No floating comparison is used. A pass does not prove BGS-TRACE-005.
"""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MAJORANT = Fraction(184981, 160000)


def series_upper(z: Fraction, n: int) -> Fraction:
    term = Fraction(1)
    total = Fraction(0)
    for j in range(n):
        total += term
        term *= z / (j + 1)
    return total + term / (1 - z / (n + 1))


def partial_sum(z: Fraction, n: int) -> Fraction:
    term = Fraction(1)
    total = Fraction(0)
    for j in range(n + 1):
        total += term
        term *= z / (j + 1)
    return total


def isqrt(n: int) -> int:
    if n < 2:
        return n
    x = 1 << ((n.bit_length() + 1) // 2)
    while True:
        y = (x + n // x) // 2
        if y >= x:
            return x
        x = y


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
        im += -(r_coeff(k - 1) - r_coeff(k + 1)) / 200
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


def majorant() -> None:
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
            upper = Fraction(isqrt(p * q) + 1, q)
            if upper * upper <= mag2:
                raise RuntimeError(f"majorant is not strict at {(k, ell)}")
            total += upper
            if (k, ell) == (7, 0):
                mode70 = (re, im)
    if count != 32 or mode70 != (Fraction(9, 20), Fraction(0)) or total != MAJORANT:
        raise RuntimeError(f"majorant changed: count={count} total={total} mode={mode70}")


def pell(n: int) -> list[tuple[int, int]]:
    rows = [(1, 0)]
    u, v = 1, 0
    for m in range(1, n + 1):
        u, v = u + 2 * v, u + v
        sign = -1 if m % 2 else 1
        if u * u - 2 * v * v != sign:
            raise RuntimeError(f"norm failed at {m}")
        if u % 2 == 0:
            raise RuntimeError(f"u even at {m}")
        rows.append((u, v))
    return rows


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def check_gcd(rows: list[tuple[int, int]]) -> None:
    for t in range(1, 41):
        u, v = rows[t]
        u2 = u * u + 2 * v * v
        v2 = 2 * u * v
        g = 0
        for entry in (u2 - 1, v2, 2 * v2):
            g = gcd(g, abs(entry))
        expect = 2 * u if t % 2 else 2 * v
        if g != expect:
            raise RuntimeError(f"gcd at t={t}: {g} != {expect}")
        if gcd(u, v) != 1:
            raise RuntimeError(f"coprime failed at t={t}")


def mat_mul(a, b, n: int):
    return [
        [
            (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % n,
            (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % n,
        ],
        [
            (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % n,
            (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % n,
        ],
    ]


def mat_pow(base, exp: int, n: int):
    result = [[1, 0], [0, 1]]
    while exp:
        if exp & 1:
            result = mat_mul(result, base, n)
        base = mat_mul(base, base, n)
        exp >>= 1
    return result


IDENTITY = [[1, 0], [0, 1]]
C = [[3, 2], [4, 3]]


def divisibility_order(n: int, rows: list[tuple[int, int]]) -> int:
    for t in range(1, len(rows)):
        u, v = rows[t]
        if t % 2 == 1 and u % n == 0:
            return t
        if t % 2 == 0 and v % n == 0:
            return t
    raise RuntimeError(f"no divisibility order for {n}")


def matrix_order(n: int, cap: int = 20000) -> int:
    m = [[1, 0], [0, 1]]
    for t in range(1, cap + 1):
        m = mat_mul(m, C, n)
        if m == IDENTITY:
            return t
    raise RuntimeError(f"no matrix order for {n}")


def check_orders(rows: list[tuple[int, int]]) -> tuple[int, int, int]:
    short = long = 0
    for n in range(3, 301, 2):
        div = divisibility_order(n, rows)
        mat = matrix_order(n)
        if div != mat:
            raise RuntimeError(f"order mismatch at {n}: {div} != {mat}")
        if 12 * div <= 5 * n:
            short += 1
        # Trial division labels the census only. It is not a hypothesis of the theorems.
        prime = not any(n % d == 0 for d in range(2, int(n**0.5) + 1))
        if prime and (n == 3 or 2 * div >= n + 1):
            long += 1
    return short, long, 149


def witnesses(rows: list[tuple[int, int]]) -> None:
    if divisibility_order(35, rows) != 6:
        raise RuntimeError("order of 35")
    if divisibility_order(5, rows) != 6:
        raise RuntimeError("order of 5")
    if divisibility_order(7, rows) != 3:
        raise RuntimeError("order of 7")
    if any(u == 35 for u, _ in rows[:20]):
        raise RuntimeError("35 is a Pell value")
    if not (12 * 6 <= 5 * 35 and 8 * 6 <= 3 * 35):
        raise RuntimeError("35 windows")
    if not (47 * 3 > 35 * 4):
        raise RuntimeError("one-return comparison")
    if mat_pow(C, 6, 35) != IDENTITY or mat_pow(C, 5, 35) == IDENTITY:
        raise RuntimeError("matrix order 35")
    c3 = [[c % 3 for c in row] for row in C]
    c3sq = mat_mul(c3, c3, 3)
    if c3sq != [[2, 0], [0, 2]]:
        raise RuntimeError("C^2 mod 3")
    if matrix_order(3) != 4:
        raise RuntimeError("order of 3")
    if 12 * 3 <= 5 * 7 or 2 * 3 >= 8:
        raise RuntimeError("p=7 was not supposed to meet either hypothesis")


def comparisons() -> None:
    if series_upper(Fraction(5, 6), 2) != Fraction(361, 156):
        raise RuntimeError("5/6 majorant")
    if series_upper(Fraction(3, 4), 2) != Fraction(17, 8):
        raise RuntimeError("3/4 majorant")
    if partial_sum(Fraction(1), 6) != Fraction(1957, 720):
        raise RuntimeError("e partial")
    if partial_sum(Fraction(2), 5) != Fraction(109, 15):
        raise RuntimeError("e^2 partial")
    if partial_sum(Fraction(6, 7), 4) != Fraction(5647, 2401):
        raise RuntimeError("6/7 partial")
    q = Fraction(17, 8)
    geometric = sum(q ** (-k) for k in range(1, 5))
    if geometric != Fraction(70600, 83521):
        raise RuntimeError(f"four-term sum {geometric}")
    checks = [
        361 * 3 < 156 * 7,
        1957 * 7 > 720 * 19,
        109 > 15 * 7,
        7 * 7 < 12 * 5,
        5 * 4 < 7 * 3,
        41 * 7 < 5 * 60,
        361 * 70600 > 300 * 83521,
        2401 * 4 < 3246 * 3,
        156 * 4 > 205 * 3,
        Fraction(1, 3) < Fraction(41, 60),
    ]
    if not all(checks):
        raise RuntimeError("a cleared comparison failed")
    b = 184981
    n = 10**39
    if not b * n * (30 * n + 1) < 160000 * 10**80:
        raise RuntimeError("short window")
    p = 10**26
    left = b * p**4 * 420
    right = 26 * (p - 2) * (160000 * 10**80 - b * p)
    if not left < right:
        raise RuntimeError("long window")
    # The defect bound increases: compare three sample points by the same formula.
    def defect_num_den(s: int) -> tuple[int, int]:
        return b * s**4, 2 * (s - 2) * (160000 * 10**80 - b * s)

    prev = None
    for s in (3, 5, 10**6, 10**20, 10**26):
        num, den = defect_num_den(s)
        if prev is not None and num * prev[1] <= prev[0] * den:
            raise RuntimeError(f"defect not increasing at {s}")
        prev = (num, den)


def poly_trim(a: list[int]) -> list[int]:
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def poly_add(a: list[int], b: list[int]) -> list[int]:
    n = max(len(a), len(b))
    return poly_trim(
        [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)]
    )


def reduce_mod(a: list[int], mod: list[int]) -> list[int]:
    a = list(a)
    deg = len(mod) - 1
    while len(a) - 1 >= deg:
        coef = a[-1]
        if coef:
            k = len(a) - 1 - deg
            for i, c in enumerate(mod):
                a[k + i] -= coef * c
        a.pop()
        if not a:
            a = [0]
    return poly_trim(a)


def poly_mul(a: list[int], b: list[int], mod: list[int]) -> list[int]:
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return reduce_mod(r, mod)


def propagator(p: int, mod: list[int]):
    inv8 = pow(8, -1, p)
    matrices = [[[0] for _ in range(p)] for _ in range(p)]
    for x in range(p):
        for y in range(p):
            quad = (-inv8 * (3 * x * x - 2 * x * y + 3 * y * y)) % p
            matrices[x][y] = reduce_mod([0] * quad + [1], mod) if quad else [1]
    return matrices


def mul_mat(a, b, mod: list[int], p: int):
    out = [[[0] for _ in range(p)] for _ in range(p)]
    for i in range(p):
        for j in range(p):
            acc = [0]
            for k in range(p):
                acc = poly_add(acc, poly_mul(a[i][k], b[k][j], mod))
            out[i][j] = acc
    return out


def conj_cyclo(a: list[int], p: int, mod: list[int]) -> list[int]:
    # omega |-> omega^{p-1} = -1 - omega - ... - omega^{p-2}.
    base = [-1] * (p - 1)
    cur = [1]
    out = [0]
    for coef in a:
        if coef:
            out = poly_add(out, poly_mul([coef], cur, mod))
        cur = poly_mul(cur, base, mod)
    return out


def kernel_count(p: int, m: int) -> int:
    matrix = mat_pow(C, m, p)
    count = 0
    for x in range(p):
        for y in range(p):
            if (matrix[0][0] * x + matrix[0][1] * y - x) % p == 0 and (
                matrix[1][0] * x + matrix[1][1] * y - y
            ) % p == 0:
                count += 1
    return count


def cyclotomic_traces() -> None:
    for p, last in ((5, 6), (7, 6)):
        mod = [1] * p
        step = propagator(p, mod)
        current = [[[1] if i == j else [0] for j in range(p)] for i in range(p)]
        for m in range(1, last + 1):
            current = mul_mat(current, step, mod, p)
            trace = [0]
            for i in range(p):
                trace = poly_add(trace, current[i][i])
            trace = reduce_mod(trace, mod)
            norm = poly_mul(trace, conj_cyclo(trace, p, mod), mod)
            if len(norm) != 1 or norm[0] < 0:
                raise RuntimeError(f"nonconstant norm at p={p} m={m}: {norm}")
            if norm[0] % (p**m) != 0:
                raise RuntimeError(f"denominator at p={p} m={m}")
            square = norm[0] // (p**m)
            fixed = kernel_count(p, m)
            if square != fixed or fixed not in (1, p * p):
                raise RuntimeError(f"|Tr|^2={square} #Fix={fixed} at p={p} m={m}")


def main() -> None:
    majorant()
    rows = pell(6000)
    check_gcd(rows)
    short, long, odd_count = check_orders(rows)
    if odd_count != 149 or short < 1 or long < 1:
        raise RuntimeError(f"census {short} {long} {odd_count}")
    witnesses(rows)
    comparisons()
    cyclotomic_traces()
    proof = ROOT / "mathematics/fixed-map/order_ladder_abel.md"
    if "BGS-TRACE-120" not in proof.read_text(encoding="utf-8"):
        raise RuntimeError("claim id missing from the proof")
    print(
        "order-ladder-abel: pass "
        f"short_le_300={short} long_primes_le_300={long} majorant=184981/160000"
    )


if __name__ == "__main__":
    main()
