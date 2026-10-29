#!/usr/bin/env python3
"""Exact integer certificate for BGS-TRACE-121.

Recomputes the exponential bounds, the cleared Abel comparisons, the
10^25 kick window, the Pell induction through u_207, the order witnesses,
the prime-power kernel law, the trichotomy for every odd prime through
500, and the half-order congruences for every odd prime through 10^6.
No floating comparison is used. A pass does not prove BGS-TRACE-005.
"""
from __future__ import annotations

from fractions import Fraction


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


def require(cond: bool, message: str) -> None:
    if not cond:
        raise SystemExit("order-trichotomy-abel: " + message)


def check_series() -> None:
    ey = series_upper(Fraction(6, 7), 4)
    ea = series_upper(Fraction(2, 7), 4)
    eb = series_upper(Fraction(6, 49), 4)
    half = partial_sum(Fraction(16, 17), 4)
    require(ey == Fraction(23441, 9947), "e^{6/7} majorant")
    require(ea == Fraction(45187, 33957), "e^{2/7} majorant")
    require(eb == Fraction(31780817, 28118111), "e^{6/49} majorant")
    require(half == Fraction(213457, 83521), "e^{16/17} partial")
    require(half > Fraction(1687, 667), "partial above 1687/667")
    seven = Fraction(48, 49) / (ey - 1) + Fraction(1, 49) / (ea - 1)
    tower = Fraction(48, 49) / (ey - 1) + Fraction(1, 49) / (eb - 1)
    require(seven == Fraction(19796077, 25256270), "p=7 lower bound")
    require(tower == Fraction(7238798455, 8237425794), "7-power lower bound")
    require(seven > Fraction(3, 4), "p=7 above 3/4")
    require(tower > Fraction(3, 4), "7-power above 3/4")
    require(seven - Fraction(13, 420) > Fraction(3, 4), "kicked p=7")
    require(tower - Fraction(13, 420) > Fraction(3, 4), "kicked 7-power")
    room = Fraction(667, 1020) + Fraction(1, 34)
    require(room == Fraction(41, 60), "41/60 assembly")
    pure = Fraction(83521, 129936) + Fraction(17, 256) + Fraction(1, 578)
    require(pure == Fraction(427139065, 600824064), "split-tower ceiling")
    require(pure < Fraction(5, 7), "split tower below 5/7")
    long = Fraction(7, 12) + Fraction(11, 120) + Fraction(1, 242)
    require(long == Fraction(3287, 4840), "long-tower ceiling")
    require(long < Fraction(5, 7), "long tower below 5/7")
    require(long + Fraction(13, 420) == Fraction(72173, 101640), "long kick sum")
    require(Fraction(72173, 101640) < Fraction(5, 7), "kicked long tower")
    p3 = Fraction(1, 6) + Fraction(3, 16) + Fraction(1, 18)
    p5 = Fraction(1, 6) + Fraction(5, 48) + Fraction(1, 50)
    require(p3 == Fraction(59, 144) and p3 + Fraction(13, 420) < Fraction(5, 7), "p=3")
    require(p5 == Fraction(349, 1200) and p5 + Fraction(13, 420) < Fraction(5, 7), "p=5")
    require(5 * 25 - 12 * 5 - 12 == 53, "square gap")


def check_window() -> None:
    margin = Fraction(5, 7) - Fraction(427139065, 600824064)
    require(margin == Fraction(14146865, 4205768448), "split margin")
    b = 184981
    c = 160000
    n = 10**25
    numerator = b * n**4 * margin.denominator
    denominator = 2 * (n - 2) * (c * 10**80 - b * n) * margin.numerator
    require(numerator < denominator, "10^25 window")


def pell(n: int) -> list[tuple[int, int]]:
    u, v = 1, 0
    out = [(u, v)]
    for _ in range(n):
        u, v = u + 2 * v, u + v
        out.append((u, v))
    return out


def valuation(n: int, p: int) -> int:
    count = 0
    while n % p == 0:
        n //= p
        count += 1
    return count


def check_witnesses() -> None:
    row = pell(30)
    require(valuation(row[8][1], 3) == 1, "delta(3)")
    require(valuation(row[12][1], 5) == 1, "delta(5)")
    require(row[12] == (19601, 13860), "lambda^6")
    require(valuation(row[6][1], 7) == 1, "delta(7)")
    require(row[6] == (99, 70), "lambda^3")
    require(row[1][0] % 13 != 0 and row[2][1] % 13 != 0, "13 small")
    require(row[7][0] % 13 != 0 and row[14][1] == 13 * 6214, "t(13)")
    require(valuation(row[28][1], 13) == 2, "delta(13)")
    require(row[15][0] == 31 * 8897, "u_15")
    require(row[1][0] % 31 != 0 and row[3][0] % 31 != 0 and row[5][0] % 31 != 0, "31 small")
    require(valuation(row[30][1], 31) == 2, "delta(31)")


def check_pell() -> None:
    u, v = 1, 0
    history = [1]
    for n in range(1, 208):
        u, v = u + 2 * v, u + v
        history.append(u)
        if n >= 4:
            require(u >= 5 * history[n - 2], f"growth {n}")
        if n >= 5 and n % 2 == 1:
            require(12 * n <= 5 * u, f"short Pell {n}")
        require(u % 2 == 1, f"odd {n}")
    require(len(str(u)) == 79 and u > 10**39, "u_207")


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1 if d == 2 else 2
    return True


def legendre(p: int) -> int:
    return 1 if p % 8 in (1, 7) else -1


def matrix_order(p: int) -> int:
    a, b, c, d = 1, 0, 0, 1
    for t in range(1, p + 2):
        # Right-multiply [[a, b], [c, d]] by C.
        a, b, c, d = (
            (3 * a + 4 * b) % p,
            (2 * a + 3 * b) % p,
            (3 * c + 4 * d) % p,
            (2 * c + 3 * d) % p,
        )
        if (a, b, c, d) == (1, 0, 0, 1):
            return t
    raise SystemExit(f"no order at {p}")


def lam_pow(m: int, mod: int) -> tuple[int, int]:
    u, v = 1, 0
    bu, bv = 3 % mod, 2 % mod
    e = m
    while e:
        if e & 1:
            u, v = (u * bu + 2 * v * bv) % mod, (u * bv + v * bu) % mod
        bu, bv = (bu * bu + 2 * bv * bv) % mod, (2 * bu * bv) % mod
        e >>= 1
    return u, v


def closed_kernel(p: int, k: int, delta: int, t: int, m: int) -> int:
    n = p**k
    if m % t != 0:
        return 1
    j = 0
    q = m // t
    while q % p == 0:
        q //= p
        j += 1
    rho = min(k, delta + j)
    return p ** (2 * rho)


def brute_kernel(u: int, v: int, modulus: int) -> int:
    a = (u - 1) % modulus
    b = v % modulus
    count = 0
    for x in range(modulus):
        rhs = (-a * x) % modulus
        if b == 0:
            if rhs != 0:
                continue
            if a == 0:
                count += modulus
            else:
                aa, bb = a, modulus
                while bb:
                    aa, bb = bb, aa % bb
                count += aa
        else:
            g = 0
            aa, bb = b, modulus
            while bb:
                aa, bb = bb, aa % bb
            g = aa
            if rhs % g != 0:
                continue
            inv = pow(b // g, -1, modulus // g)
            y0 = (rhs // g) * inv % (modulus // g)
            for step in range(g):
                y = y0 + (modulus // g) * step
                if (2 * b * x + a * y) % modulus == 0:
                    count += 1
    return count


def check_primes() -> None:
    seen_half = []
    for p in range(3, 501):
        if not is_prime(p):
            continue
        t = matrix_order(p)
        eps = legendre(p)
        modulus = p - eps
        require(modulus % t == 0, f"divisibility {p}")
        require(2 * t != p + 1, f"vacuous half {p}")
        if eps == 1:
            require(((p - 1) // 2) % t == 0, f"split divisor {p}")
            require(t != p - 1, f"vacuous split full {p}")
        else:
            require(((p + 1) // t) % 2 == 1, f"inert cofactor {p}")
        if t == modulus:
            kind = "long"
            require(eps == -1, f"long split {p}")
        elif eps == 1 and t * 2 == p - 1:
            kind = "half"
            seen_half.append(p)
        elif t * 3 <= modulus:
            kind = "short"
        else:
            raise SystemExit(f"unclassified {p}")
        if kind == "short" and p >= 5:
            require(12 * t <= 5 * p, f"short inequality {p}")
        if kind == "long":
            require(t == p + 1, f"long inequality {p}")
    require(seen_half[0] == 7 and all(p >= 17 for p in seen_half[1:]), "half range")


def sieve(limit: int) -> list[int]:
    mark = bytearray(b"\x01") * (limit + 1)
    mark[0] = mark[1] = 0
    p = 2
    while p * p <= limit:
        if mark[p]:
            start = p * p
            mark[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
        p += 1
    return [n for n in range(3, limit + 1, 2) if mark[n]]


def order_of_lambda(p: int, eps: int) -> int:
    modulus = (p - 1) // 2 if eps == 1 else p + 1
    t = modulus
    n = modulus
    d = 2
    while d * d <= n:
        if n % d == 0:
            while t % d == 0:
                u, v = lam_pow(t // d, p)
                if u == 1 and v == 0:
                    t //= d
                else:
                    break
            while n % d == 0:
                n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        while t % n == 0:
            u, v = lam_pow(t // n, p)
            if u == 1 and v == 0:
                t //= n
            else:
                break
    return t


def check_half_order(limit: int = 10**6) -> None:
    for p in sieve(limit):
        eps = legendre(p)
        if eps == 1:
            u, v = lam_pow((p - 1) // 2, p)
            require(u == 1 and v == 0, f"split congruence {p}")
        else:
            u, v = lam_pow((p + 1) // 2, p)
            require(u == p - 1 and v == 0, f"inert congruence {p}")
        t = order_of_lambda(p, eps)
        if p <= 500:
            require(t == matrix_order(p), f"order agreement {p}")
        require(2 * t != p + 1, f"half order {p}")
        if eps == 1:
            require(((p - 1) // 2) % t == 0, f"split scan {p}")
            require(t != p - 1, f"split full scan {p}")
        else:
            require(((p + 1) // t) % 2 == 1, f"cofactor scan {p}")
            require(t % 2 == 0, f"inert parity {p}")
        if p >= 5 and 3 * t <= p - eps:
            if t % 4 == 0:
                order_3q = t
            elif t % 2 == 0:
                order_3q = 2 * t
            else:
                order_3q = 4 * t
            require(12 * order_3q <= 15 * p, f"three-short {p}")


def check_kernels() -> None:
    for p in range(3, 81):
        if not is_prime(p):
            continue
        t = matrix_order(p)
        mod = p**4
        _u, v = lam_pow(t, mod)
        delta = 4 if v == 0 else valuation(v, p)
        require(1 <= delta <= 4, f"depth range {p}")
        for k in (1, 2, 3):
            modulus = p**k
            limit = min(modulus, 4 * p, 2 * t * p)
            for m in range(1, limit + 1):
                if modulus > 1000:
                    continue
                u, vv = lam_pow(m, modulus)
                got = brute_kernel(u, vv, modulus)
                expect = closed_kernel(p, k, delta, t, m)
                require(got == expect, f"kernel p={p} k={k} m={m}")


def main() -> None:
    check_series()
    check_window()
    check_witnesses()
    check_pell()
    check_primes()
    check_half_order()
    check_kernels()
    print("order-trichotomy-abel: pass")


if __name__ == "__main__":
    main()
