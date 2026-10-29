#!/usr/bin/env python3
"""Exact integer certificate for BGS-TRACE-124.

Recomputes the orders used in the finite partner list, the Bernoulli tower
majorant on each ceiling class, the degree-four lower bounds on the
above-side towers, the inert table from 13 through 39, and the defect
endpoint at 2*10^26. No floating comparison is used. A pass does not prove
BGS-TRACE-005.
"""
from __future__ import annotations

from fractions import Fraction
from math import gcd


def series_upper(z: Fraction, n: int = 4) -> Fraction:
    term = Fraction(1)
    total = Fraction(0)
    for j in range(n):
        total += term
        term *= z / (j + 1)
    return total + term / (1 - z / (n + 1))


def rl(z: Fraction) -> Fraction:
    return 1 / (series_upper(z) - 1)


def require(cond: bool, message: str) -> None:
    if not cond:
        raise SystemExit("odd-modulus-abel: " + message)


def K(r: int) -> Fraction:
    return Fraction(r * (r + 1), r * r + r + 1)


def tower_majorant(p: int, q: int, alpha: Fraction) -> Fraction:
    gamma = (1 + Fraction(1, p)) * (1 + Fraction(1, q))
    return gamma / alpha - Fraction(1, 2) + (alpha / 12) * K(p) * K(q)


def envelope_majorant(p: int, q: int, coef: int) -> Fraction:
    alpha = Fraction(coef * (q - 1), p * q)
    gamma = (1 + Fraction(1, p)) * (1 + Fraction(1, q))
    return gamma / alpha - Fraction(1, 2) + (alpha / 12) * K(p)


def legendre(p: int) -> int:
    return 1 if p % 8 in (1, 7) else -1


def order_and_witness(p: int) -> tuple[int, int]:
    modulus = p - legendre(p)
    u, v = 1, 0
    found = None
    witness = None
    for m in range(1, modulus + 1):
        u, v = u + 2 * v, u + v
        value = u if m % 2 else v
        if modulus % m == 0 and value % p == 0:
            found = m
            witness = value
            break
    require(found is not None and witness is not None, f"order {p}")
    return found, witness


def prefix_clear(p: int, t: int) -> None:
    u, v = 1, 0
    for m in range(1, t):
        u, v = u + 2 * v, u + v
        value = u if m % 2 else v
        require(value % p != 0, f"smaller index {p},{m}")


ORDERS = {
    3: 4,
    5: 6,
    7: 3,
    11: 12,
    13: 14,
    17: 8,
    19: 20,
    23: 11,
    29: 10,
    31: 15,
    37: 38,
    41: 5,
    43: 44,
    47: 23,
}
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
    31: 275807,
    37: 124145519261542,
    41: 41,
    43: 24580185800219268,
    47: 318281039,
}


def lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b


def check_orders() -> None:
    for p, t in ORDERS.items():
        got, witness = order_and_witness(p)
        require(got == t, f"order {p}")
        require(witness == WITNESSES[p], f"witness {p}")
        require(witness % p == 0, f"divisible {p}")
        prefix_clear(p, t)
        require((p - legendre(p)) % t == 0, f"splitting {p}")


def check_partners_of_23() -> None:
    # Every odd prime strictly between 23 and 50. Only 37 is non-short.
    short = {29: 10, 31: 15, 41: 5, 43: 44, 47: 23}
    for q, t in short.items():
        order = lcm(11, t)
        require(12 * order <= 5 * 23 * q, f"23 times {q} short")
    order = lcm(11, 38)
    require(order == 418, "23 times 37 order")
    require(12 * 418 > 5 * 851, "23 times 37 non-short")
    require(Fraction(2 * 418, 851) == Fraction(836, 851), "23 times 37 ratio")


def check_explicit_ceilings() -> None:
    five = Fraction(5, 7)
    rows = [
        (3, 5, Fraction(8, 5), Fraction(499, 806)),
        (3, 13, Fraction(56, 39), Fraction(8705, 14274)),
        (5, 13, Fraction(84, 65), Fraction(2283, 3782)),
        (11, 13, Fraction(168, 143), Fraction(1383, 2318)),
        (23, 37, Fraction(836, 851), Fraction(11512715, 17117562)),
    ]
    for p, q, alpha, expect in rows:
        got = tower_majorant(p, q, alpha)
        require(got == expect, f"majorant {p} {q}")
        require(got < five, f"majorant below 5/7 {p} {q}")
    corner = tower_majorant(3, 23, Fraction(88, 69))
    require(corner == Fraction(108945, 158158), "3 times 23 majorant")
    gap = five - corner
    require(gap == Fraction(575, 22594), "3 times 23 gap")
    require(gap < Fraction(13, 420), "3 times 23 gap does not absorb the defect")


TAILS = [
    # p, coefficient of (q-1)/(p q), q0, N(q), first difference, second difference, denominator factor
    (3, 4, 23, lambda q: 61 * q * q - 1097 * q - 56, lambda q: 2 * (61 * q - 518), 122, 546),
    (5, 6, 19, lambda q: 51 * q * q - 877 * q - 42, lambda q: 2 * (51 * q - 413), 102, 434),
    (11, 12, 17, lambda q: 33 * q * q - 541 * q - 24, lambda q: 2 * (33 * q - 254), 66, 266),
    (13, 14, 17, lambda q: 961 * q * q - 15647 * q - 686, lambda q: 2 * (961 * q - 7343), 1922, 7686),
    (19, 20, 23, lambda q: 2029 * q * q - 32633 * q - 1400, lambda q: 2 * (2029 * q - 15302), 4058, 16002),
    (23, 22, 50, lambda q: 533 * q * q - 26109 * q - 968, lambda q: 2 * (533 * q - 12788), 1066, 12166),
]


def check_tails() -> None:
    five = Fraction(5, 7)
    for p, coef, q0, num, diff, second, den_factor in TAILS:
        n0 = num(q0)
        d0 = den_factor * q0 * (q0 - 1)
        n1 = num(q0 + 1)
        d1 = den_factor * (q0 + 1) * q0
        n2 = num(q0 + 2)
        require(n0 > 0, f"tail numerator {p}")
        require(n1 - n0 == diff(q0) and diff(q0) > 0, f"tail first difference {p}")
        require(n2 - 2 * n1 + n0 == second and second > 0, f"tail second difference {p}")
        for q, n, d in ((q0, n0, d0), (q0 + 1, n1, d1), (q0 + 10, num(q0 + 10), den_factor * (q0 + 10) * (q0 + 9))):
            got = five - envelope_majorant(p, q, coef)
            require(got == Fraction(n, d), f"tail identity {p} at {q}")
            require(got > 0, f"tail positive {p} at {q}")


def check_large_primes() -> None:
    five = Fraction(5, 7)

    def U1(p: int, q: int) -> Fraction:
        alpha = (1 - Fraction(1, p)) * (1 - Fraction(1, q))
        gamma = (1 + Fraction(1, p)) * (1 + Fraction(1, q))
        return gamma / alpha - Fraction(1, 2) + alpha / 12

    def num(p: int) -> int:
        return 11 * p**3 - 311 * p * p - 701 * p - 7

    def den(p: int) -> int:
        return 84 * p * (p - 1) * (p + 2)

    for p in (31, 37, 100):
        q = p + 2
        require(five - U1(p, q) == Fraction(num(p), den(p)), f"large identity {p}")
    require(num(31) == 7092 and num(31) > 0, "large numerator")
    diff = lambda p: 33 * p * p - 589 * p - 1001
    require(num(32) - num(31) == diff(31) == 12453, "large first difference")
    require(diff(32) - diff(31) == 66 * 31 - 556 == 1490, "large second difference")
    require(1490 > 0, "large second difference positive")


def check_drop_and_radical() -> None:
    require(5 * 5**3 - 12 * 5**2 - 24 * 5 - 12 == 193, "drop base")
    require(15 * 5**2 - 9 * 5 - 31 == 299, "drop step")
    require(21 * 5 - 24 == 81, "raise three")
    require(15 * 5**2 - 48 * 5 - 48 == 87, "raise the partner of three")
    require(12 * 84 < 5 * 195 * 3, "195 drop")
    require(12 * 84 > 5 * 195, "195 itself is not short")
    require(12 * 12 <= 5 * 105, "radical 105 is short")
    require(8 * 12 <= 3 * 105, "radical 105 is strongly short")
    require(8 * 12 <= 3 * 315, "315 inherits strong shortness")
    require(Fraction(4, 5) + Fraction(1, 10**24) < Fraction(81, 100), "return threshold")
    require(Fraction(4, 5 * 10**24) < Fraction(1, 10**24), "large fifteen ratio")
    require(10**26 // 15 > 10**24, "fifteen partner past 10^26")
    require(81 < 5 * 100, "81/100 lies below five")


def lower_terms(terms: list[tuple[Fraction, Fraction]]) -> Fraction:
    total = Fraction(0)
    for coeff, arg in terms:
        require(0 < arg < 5, "degree-four domain")
        total += coeff * rl(arg)
    return total


def check_lower_bounds() -> None:
    kick = Fraction(82, 105)
    three = Fraction(3, 4)
    rows = {
        "21": (
            [
                (Fraction(383, 441), Fraction(8, 7)),
                (Fraction(1, 49), Fraction(8, 49)),
                (Fraction(1, 9), Fraction(2, 7)),
            ],
            Fraction(265028515609711, 309078510309860),
        ),
        "195": (
            [
                (Fraction(24, 25), Fraction(56, 65)),
                (Fraction(1, 25), Fraction(56, 325)),
            ],
            Fraction(50134551873841695, 54792051773384968),
        ),
        "inert-a2": (
            [
                (Fraction(48, 49), Fraction(12, 13)),
                (Fraction(1, 49), Fraction(12, 91)),
            ],
            Fraction(26832108548323, 33947639168772),
        ),
        "three-short-a1": (
            [
                (Fraction(8, 9), Fraction(80, 87)),
                (Fraction(1, 9), Fraction(20, 87)),
            ],
            Fraction(114226176533733, 112075008606140),
        ),
        "three-short-a2": (
            [
                (Fraction(8, 9), Fraction(80, 87)),
                (Fraction(1, 9), Fraction(80, 261)),
            ],
            Fraction(2228970493853307, 2479202684534320),
        ),
    }
    for name, (terms, expect) in rows.items():
        got = lower_terms(terms)
        require(got == expect, name)
        require(got > kick, name + " kick margin")
    scaled = Fraction(1599, 1600) * lower_terms(
        [
            (Fraction(48, 49), Fraction(123, 140)),
            (Fraction(1, 49), Fraction(41, 140)),
        ]
    )
    require(scaled == Fraction(13146189928817400, 17402756940259603), "inert tail scale")
    require(scaled > three, "inert tail above 3/4")
    require(scaled < kick, "inert tail does not clear the kick")


def inert_subsum(q: int) -> Fraction:
    alpha = Fraction(6 * (q + 1), 7 * q)
    gamma = Fraction(2 * (q + 1), 7 * q)
    require(alpha < 5 and gamma < 5, f"inert domain {q}")
    top = Fraction(48, 49) * rl(alpha) + Fraction(1, 49) * rl(gamma)
    low = Fraction(48, 49) * rl(alpha / q) + Fraction(1, 49) * rl(gamma / q)
    return (1 - Fraction(1, q * q)) * top + Fraction(1, q * q) * low


def check_inert_table() -> None:
    kick = Fraction(82, 105)
    corner = inert_subsum(13)
    require(
        corner == Fraction(16323101582366123785899971, 20875800430500088687646340),
        "inert q=13 fraction",
    )
    for q in range(13, 40):
        require(inert_subsum(q) > kick, f"inert kick {q}")


def check_defect_endpoint() -> None:
    low = rl(Fraction(81, 100))
    require(low == Fraction(3352000000, 4183386507), "81/100 fraction")
    margin = low - Fraction(3, 4)
    require(margin == Fraction(857840479, 16733546028), "return margin")
    B = Fraction(184981, 160000)
    N = 2 * 10**26
    require(B * N < 10**80, "defect formula applies at 2e26")
    defect = B * N**4 / (2 * (N - 2) * (10**80 - B * N))
    require(defect < margin, "defect at 2e26 stays under the return margin")
    # The same majorant exceeds 1 at every 79-digit dimension.
    huge = 10**78
    require(B * huge**4 > 2 * huge * 10**80, "majorant exceeds 1 at 10^78")
    require(B * 10**79 < 10**80, "majorant still defined at 10^79")


def main() -> None:
    check_orders()
    check_partners_of_23()
    check_explicit_ceilings()
    check_tails()
    check_large_primes()
    check_drop_and_radical()
    check_lower_bounds()
    check_inert_table()
    check_defect_endpoint()
    print("odd-modulus-abel: pass")


if __name__ == "__main__":
    main()
