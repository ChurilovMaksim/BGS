#!/usr/bin/env python3
"""Exact integer certificate for BGS-TRACE-122.

Recomputes the square-free exponential bounds, the seven-family rational
function, the semiprime corners, the orders below 30, and a finite
semiprime sandwich. No floating comparison is used. A pass does not prove
BGS-TRACE-005.
"""
from __future__ import annotations

from fractions import Fraction
from math import gcd


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
        raise SystemExit("crt-composite-abel: " + message)


def ru(z: Fraction, degree: int = 8) -> Fraction:
    return 1 / (partial_sum(z, degree) - 1)


def rl(z: Fraction, degree: int = 4) -> Fraction:
    return 1 / (series_upper(z, degree) - 1)


class Poly:
    def __init__(self, coeffs: list[Fraction]) -> None:
        self.c = [Fraction(x) for x in coeffs]
        self.trim()

    def trim(self) -> None:
        while len(self.c) > 1 and self.c[-1] == 0:
            self.c.pop()

    def __add__(self, other: "Poly") -> "Poly":
        n = max(len(self.c), len(other.c))
        out = [Fraction(0)] * n
        for i, val in enumerate(self.c):
            out[i] += val
        for i, val in enumerate(other.c):
            out[i] += val
        return Poly(out)

    def __sub__(self, other: "Poly") -> "Poly":
        return self + Poly([-x for x in other.c])

    def __mul__(self, other: "Poly") -> "Poly":
        out = [Fraction(0)] * (len(self.c) + len(other.c) - 1)
        for i, a in enumerate(self.c):
            for j, b in enumerate(other.c):
                out[i + j] += a * b
        return Poly(out)

    def __neg__(self) -> "Poly":
        return Poly([-x for x in self.c])


class RF:
    def __init__(self, num: Poly, den: Poly) -> None:
        self.n = num
        self.d = den

    def __add__(self, other: "RF") -> "RF":
        return RF(self.n * other.d + other.n * self.d, self.d * other.d)

    def __sub__(self, other: "RF") -> "RF":
        return self + RF(-other.n, other.d)


def monic_integer(poly: Poly) -> tuple[int, ...]:
    den = 1
    for coeff in poly.c:
        den = den * coeff.denominator // gcd(den, coeff.denominator)
    vals = [int(coeff * den) for coeff in poly.c]
    content = 0
    for val in vals:
        content = gcd(content, abs(val))
    require(content > 0, "zero polynomial")
    if vals[-1] < 0:
        content = -content
    return tuple(val // content for val in vals)


def pell(n: int) -> list[tuple[int, int]]:
    u, v = 1, 0
    rows = [(u, v)]
    for _ in range(n):
        u, v = u + 2 * v, u + v
        rows.append((u, v))
    return rows


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


ORDERS = {3: 4, 5: 6, 7: 3, 11: 12, 13: 14, 17: 8, 19: 20, 23: 11, 29: 10}
WITNESSES = {
    3: 12,
    5: 70,
    7: 7,
    11: 13860,
    13: 80782,
    17: 408,
    19: 15994428,
    23: 8119,
    29: 2378,
}


def check_orders() -> None:
    rows = pell(29)
    for p, t in ORDERS.items():
        witness = rows[t][0] if t % 2 else rows[t][1]
        require(witness == WITNESSES[p], f"witness {p}")
        require(witness % p == 0, f"divisible {p}")
        for m in range(1, t):
            earlier = rows[m][0] if m % 2 else rows[m][1]
            require(earlier % p != 0, f"smaller index {p},{m}")
        eps = legendre(p)
        modulus = p - eps
        require(modulus % t == 0, f"splitting {p}")
        if t * 3 <= modulus:
            kind = "short"
        elif t == modulus or (eps == -1 and 2 * t == p + 1):
            kind = "long"
        elif eps == 1 and 2 * t == p - 1:
            kind = "half"
        else:
            raise SystemExit(f"unclassified {p}")
        expect = {
            3: "long",
            5: "long",
            7: "half",
            11: "long",
            13: "long",
            17: "half",
            19: "long",
            23: "half",
            29: "short",
        }[p]
        require(kind == expect, f"class {p}")
    require(all(p >= 29 or ORDERS[p] * 3 > (p - legendre(p)) for p in ORDERS), "no short prime below 29")


def check_arithmetic() -> None:
    require(4 * 6 * 30 < 5 * 5 * 29, "larger short corner")
    require(4 * 30 * 32 < 5 * 29 * 31, "both large short corner")
    require(48 * 18 <= 85 * 17, "seventeen")
    require(8 * 30 <= 15 * 29, "three with even short order")
    require(66 * 30 <= 115 * 29, "twenty-three half partner")
    require(3 * 30 * 34 < 5 * 31 * 33, "large half times half")
    require(3 * 30 * 32 < 5 * 29 * 31, "inert half with gcd at least 2")
    require(12 * 12 > 5 * 21 and 12 * 6 <= 5 * 35, "seven times three and five")
    require(12 * 84 > 5 * 195, "three-prime example is not short")
    pairs = {
        (3, 5): (12, False),
        (3, 11): (12, True),
        (3, 13): (28, False),
        (3, 17): (8, True),
        (3, 19): (20, True),
        (5, 11): (12, True),
        (5, 13): (42, False),
        (5, 17): (24, True),
        (11, 17): (24, True),
        (13, 17): (56, True),
        (7, 17): (24, True),
        (7, 23): (33, True),
        (7, 13): (42, False),
        (7, 19): (60, False),
    }
    for (p, q), (order, short) in pairs.items():
        got = ORDERS[p] * ORDERS[q] // gcd(ORDERS[p], ORDERS[q])
        require(got == order, f"lcm {p},{q}")
        require((12 * got <= 5 * p * q) == short, f"short flag {p},{q}")


def ceiling(alpha: Fraction, gamma: Fraction, beta: Fraction, unit: Fraction, square: int) -> Fraction:
    return ru(alpha) + beta + ru(gamma) / square + unit


def check_bounds() -> None:
    five = Fraction(5, 7)
    three = Fraction(3, 4)
    kick = Fraction(82, 105)
    require(three + Fraction(13, 420) == kick, "kick threshold")
    corners = [
        ("15", Fraction(8, 5), Fraction(4, 5), Fraction(3, 40), Fraction(1, 30), 9),
        ("39", Fraction(56, 39), Fraction(28, 39), Fraction(3, 104), Fraction(1, 78), 9),
        ("65", Fraction(84, 65), Fraction(28, 65), Fraction(5, 156), Fraction(1, 130), 25),
        ("p3", Fraction(88, 69), Fraction(22, 69), Fraction(3, 184), Fraction(1, 138), 9),
        ("p5", Fraction(96, 85), Fraction(16, 85), Fraction(5, 204), Fraction(1, 170), 25),
        ("p11", Fraction(144, 143), Fraction(12, 143), Fraction(11, 312), Fraction(1, 286), 121),
        ("p13", Fraction(224, 221), Fraction(16, 221), Fraction(13, 476), Fraction(1, 442), 169),
        ("p19", Fraction(440, 437), Fraction(22, 437), Fraction(19, 920), Fraction(1, 874), 361),
        ("p23", Fraction(660, 713), Fraction(60, 713), Fraction(23, 682), Fraction(1, 1426), 529),
    ]
    for name, alpha, gamma, beta, unit, square in corners:
        require(ceiling(alpha, gamma, beta, unit, square) < five, name)
    split = ru(Fraction(960, 1023)) + Fraction(31, 990) + Fraction(33, 1984) + Fraction(1, 2046)
    nonsplit = ru(Fraction(840, 899)) + Fraction(29, 1736) + Fraction(31, 870) + Fraction(1, 1798)
    require(split < five, "split tail")
    require(nonsplit < five, "non-split tail")

    a21 = Fraction(8, 9) * Fraction(48, 49)
    b21 = Fraction(8, 9) / 49
    c21 = Fraction(48, 49) / 9
    d21 = Fraction(1, 441)
    low21 = (
        a21 * rl(Fraction(8, 7))
        + b21 * rl(Fraction(8, 21))
        + c21 * rl(Fraction(2, 7))
        + d21 * rl(Fraction(2, 21))
    )
    require(low21 == Fraction(1485928284770040951, 1861068320411356730), "N=21 fraction")
    require(low21 > kick, "N=21 clears the kick margin")

    a3 = Fraction(8, 9) * Fraction(840, 841)
    c3 = Fraction(840, 841) / 9
    low3 = a3 * rl(Fraction(80, 87)) + c3 * rl(Fraction(20, 87))
    require(low3 == Fraction(5704517734146, 5603750430307), "three-short fraction")
    require(low3 > kick, "three-short clears the kick margin")

    e6 = series_upper(Fraction(6, 7), 4)
    e2 = series_upper(Fraction(2, 7), 4)
    require(e6 == Fraction(23441, 9947) and e2 == Fraction(45187, 33957), "majorants")
    seven = Fraction(48, 49) / (e6 - 1) + Fraction(1, 49) / (e2 - 1)
    require(seven == Fraction(19796077, 25256270), "seven value")
    require(seven - Fraction(13, 420) > three, "seven kick margin")


def check_phi() -> None:
    e6 = Fraction(23441, 9947)
    e2 = Fraction(45187, 33957)
    q = Poly([0, 1])
    one = Poly([1])
    q2 = q * q
    num_m = Poly([Fraction(-18), 0, 49])
    den_m = Poly([0, Fraction(-42), 49])  # 49q^2 - 42q
    # E6*M - 1 = (23441 num_m - 9947 den_m) / (9947 den_m)
    em_num = Poly([23441]) * num_m - Poly([9947]) * den_m
    # Term A = 48*9947*(q^2-1)*(7q-6) / (7 q * em_num)
    a_num = Poly([48 * 9947]) * (q2 - one) * Poly([-6, 7])
    a_den = Poly([7]) * q * em_num
    # Term B = 8(7q-6)/(49 q^2)
    b_num = Poly([8]) * Poly([-6, 7])
    b_den = Poly([49]) * q2
    num_m3 = Poly([Fraction(-2), 0, 49])
    den_m3 = Poly([0, Fraction(-14), 49])
    em3_num = Poly([45187]) * num_m3 - Poly([33957]) * den_m3
    # Term C = 33957 (q^2-1) (7q-2) / (7 q * em3_num)
    c_num = Poly([33957]) * (q2 - one) * Poly([-2, 7])
    c_den = Poly([7]) * q * em3_num
    phi = RF(a_num, a_den) + RF(b_num, b_den) + RF(c_num, c_den)
    target = RF(Poly([3]), Poly([4]))
    diff = phi - target
    num = monic_integer(diff.n)
    den = monic_integer(diff.d)
    # Addition of the three terms leaves a common positive power of q.
    shift = 0
    while shift < len(num) and shift < len(den) and num[shift] == 0 and den[shift] == 0:
        shift += 1
    num = num[shift:]
    den = den[shift:]
    expect_n = (
        -610115596992,
        3854354403900,
        759755266431,
        -7015097338690,
        -3360079183489,
        281046183404,
        200914962101,
    )
    quart = (
        3177685401,
        -19862032400,
        -7777227521,
        45352042414,
        30320152135,
    )
    quad_a = (-70323, 69629, 110201)
    quad_b = (-45187, 237699, 275135)
    product = [0] * 5
    for i, a in enumerate(quad_a):
        for j, b in enumerate(quad_b):
            product[i + j] += a * b
    require(tuple(product) == quart, "denominator factorization")
    expect_d = (0, 0) + quart
    # monic_integer drops the content 196 and keeps the positive leading term.
    require(num == expect_n, "phi numerator")
    require(den == expect_d, "phi denominator")
    require(e6 == Fraction(23441, 9947) and e2 == Fraction(45187, 33957), "constants used")

    def eval_poly(coeffs: tuple[int, ...], x: int) -> int:
        total = 0
        for coeff in reversed(coeffs):
            total = total * x + coeff
        return total

    np = (
        3854354403900,
        1519510532862,
        -21045292016070,
        -13440316733956,
        1405230917020,
        1205489772606,
    )
    npp = (
        1519510532862,
        -42090584032140,
        -40320950201868,
        5620923668080,
        6027448863030,
    )
    qpoly = (
        15505209519,
        -429495755430,
        -411438267366,
        57356363960,
        61504580235,
    )
    scaled = tuple(98 * coeff for coeff in qpoly)
    require(scaled == npp, "second derivative factor")
    for index, coeff in enumerate(expect_n):
        if index + 1 < len(expect_n):
            require(np[index] == (index + 1) * expect_n[index + 1], f"derivative {index}")
    for index, coeff in enumerate(np):
        if index + 1 < len(np):
            require(npp[index] == (index + 1) * np[index + 1], f"second derivative {index}")
    gap = 61504580235 * 169 - 411438267366
    require(gap == 9982835792349, "quartic gap")
    require(13 * gap - 429495755430 == 129347369545107, "linear gap")
    require(eval_poly(expect_n, 13) == 962927132597336369, "N(13)")
    require(eval_poly(np, 13) == 454663292137321722, "N'(13)")
    require(eval_poly(npp, 13) == 177139237609770940, "N''(13)")
    require(110201 * 169 - 70323 == 18553646, "first quadratic")
    require(275135 * 169 - 45187 == 46452628, "second quadratic")


def order_of(p: int) -> int:
    u, v = 1, 0
    for m in range(1, p + 2):
        u, v = u + 2 * v, u + v
        if (m % 2 == 1 and u % p == 0) or (m % 2 == 0 and v % p == 0):
            return m
    raise SystemExit(f"no order {p}")


def kind_of(p: int, t: int) -> str:
    eps = legendre(p)
    modulus = p - eps
    if 3 * t <= modulus:
        return "short"
    if t == modulus or (eps == -1 and 2 * t == p + 1):
        return "long"
    if eps == 1 and 2 * t == p - 1:
        return "half"
    raise SystemExit(f"unclassified {p}")


def check_sandwich() -> None:
    primes = [p for p in range(3, 100) if is_prime(p)]
    orders = {p: order_of(p) for p in primes}
    kinds = {p: kind_of(p, orders[p]) for p in primes}
    for p, t in ORDERS.items():
        require(orders[p] == t, f"audit order {p}")
    five = Fraction(5, 7)
    three = Fraction(3, 4)
    for i, p in enumerate(primes):
        for q in primes[i + 1 :]:
            t, s = orders[p], orders[q]
            order = t * s // gcd(t, s)
            modulus = p * q
            short = 12 * order <= 5 * modulus
            seven = (p == 7 or q == 7) and not short
            three_short = p == 3 and kinds[q] == "short" and not short
            alpha = Fraction(2 * order, modulus)
            beta = Fraction(2 * t, modulus)
            gamma = Fraction(2 * s, modulus)
            ups = Fraction(2, modulus)
            a = (1 - Fraction(1, p * p)) * (1 - Fraction(1, q * q))
            b = (1 - Fraction(1, p * p)) / (q * q)
            c = (1 - Fraction(1, q * q)) / (p * p)
            d = Fraction(1, modulus * modulus)
            upper = a * ru(alpha) + b * ru(beta) + c * ru(gamma) + d * ru(ups)
            lower = a * rl(alpha) + b * rl(beta) + c * rl(gamma)
            if short or seven or three_short:
                require(lower > three, f"sandwich low {p}*{q}")
            else:
                require(upper < five, f"sandwich high {p}*{q}")


def check_tails() -> None:
    require(15 * 5 > 12 * 6, "three, gcd 4")
    require(25 * 29 > 24 * 30, "five, gcd 3")
    require(25 * 7 > 18 * 8, "five, half partner")
    require(144 < 21 * 7, "eleven, gcd 3")
    require(144 <= 76 * 2, "eleven, gcd 4")
    require(55 * 13 > 36 * 14, "eleven, half partner")
    require(65 * 13 > 24 * 14, "thirteen, gcd 7")
    require(65 * 17 > 42 * 18, "thirteen, half partner")
    require(240 < 140 * 2, "nineteen, gcd 4")
    require(95 * 23 > 60 * 24, "nineteen, half partner")
    require(115 * 3 > 66 * 4, "twenty-three, half partner")
    require(5 * 29 * 31 > 3 * 30 * 32, "inert corner")
    identity = 5 * 31 * 33 - 3 * 30 * 34
    require(identity == 2 * 31 * 31 + 4 * 31 + 9 and identity > 0, "split-half identity")
    require(Fraction(456, 481) > Fraction(840, 899), "full alpha corner")
    require(Fraction(37, 2808) < Fraction(29, 1736), "full beta corner")
    require(Fraction(39, 1406) < Fraction(31, 870), "full gamma corner")
    require(Fraction(1, 2 * 37 * 39) < Fraction(1, 2 * 29 * 31), "full unit corner")
    require(3 * 37 * 37 + 5 * 37 + 5 == 4297, "inert numerator")
    require(2 * 37 * 38 * 39 == 109668, "inert denominator")
    inert = Fraction(4297, 109668)
    envelope = Fraction(29, 1736) + Fraction(31, 870) + Fraction(1, 1798)
    require(inert < envelope, "inert extras fit the majorant")


def check_defect() -> None:
    numerator = 184981 * 10**104 * 420
    denominator = 26 * (10**26 - 2) * (160000 * 10**80 - 184981 * 10**26)
    require(numerator < denominator, "defect endpoint")


def main() -> None:
    check_orders()
    check_arithmetic()
    check_bounds()
    check_phi()
    check_tails()
    check_sandwich()
    check_defect()
    print("crt-composite-abel: pass")


if __name__ == "__main__":
    main()
