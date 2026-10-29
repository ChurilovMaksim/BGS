#!/usr/bin/env python3
"""Exact integer certificate for BGS-TRACE-123.

Recomputes the orders used in the finite list, the corner comparisons, the
degree-four lower bounds at 88/115 and 152/185, and the eight-term lower
bound at N=195. No floating comparison is used. A pass does not prove
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
        raise SystemExit("squarefree-product-abel: " + message)


def legendre(p: int) -> int:
    return 1 if p % 8 in (1, 7) else -1


def order_and_witness(p: int) -> tuple[int, int]:
    eps = legendre(p)
    modulus = p - eps
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
}


def lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b


def lcm_all(values: list[int]) -> int:
    out = 1
    for value in values:
        out = lcm(out, value)
    return out


def check_orders() -> None:
    for p, t in ORDERS.items():
        got, witness = order_and_witness(p)
        require(got == t, f"order {p}")
        require(witness == WITNESSES[p], f"witness {p}")
        require(witness % p == 0, f"divisible {p}")
        prefix_clear(p, t)
        eps = legendre(p)
        require((p - eps) % t == 0, f"splitting {p}")


def check_corners() -> None:
    require(4 * 6 * 8 * 12 <= 3 * 3 * 5 * 7 * 11, "four primes")
    require(4 * 6 * 8 * 12 * 14 <= 6 * 3 * 5 * 7 * 11 * 13, "five primes")
    require(2 * 6 * 8 * 12 <= 3 * 5 * 7 * 11, "primes at least five")
    require(4 * 8 * 12 <= 5 * 7 * 11, "three times a prime at least seven")
    require(72 * 30 <= 75 * 29, "three times five, tail")
    require(3 * 29 - 72 == 15, "three times five, slope")
    require(48 * 12 <= 63 * 11, "three times seven, tail")
    require(15 * 11 - 48 == 117, "three times seven, slope")
    require(8 * 12 * 38 <= 9 * 11 * 37, "eleven tail")
    require(9 * 11 - 8 * 12 == 3, "eleven slope")
    require(8 * 14 * 24 <= 9 * 13 * 23, "thirteen tail")
    require(9 * 13 - 8 * 14 == 5, "thirteen slope")
    require(8 * 18 * 20 <= 9 * 17 * 19, "seventeen tail")
    require(17 - 8 == 9, "seventeen slope")
    require(4 * 38 * 185 == 152 * 5 * 37, "return corner")
    require(20 * 37 == 740, "return slope")
    require(152 < 5 * 185, "wide ratio below five")
    require(88 < 5 * 115, "narrow ratio below five")
    require(168 < 5 * 195, "subset ratios below five")


def check_explicit_products() -> None:
    pure = [
        ((3, 5, 7), 12, True),
        ((3, 5, 11), 12, True),
        ((3, 5, 13), 84, False),
        ((3, 5, 17), 24, True),
        ((3, 5, 19), 60, True),
        ((3, 5, 23), 132, True),
    ]
    for primes, expect, short in pure:
        order = lcm_all([ORDERS[p] for p in primes])
        modulus = primes[0] * primes[1] * primes[2]
        require(order == expect, f"pure lcm {primes}")
        require((12 * order <= 5 * modulus) == short, f"pure flag {primes}")
    kicked = [
        ((3, 5, 7), 12),
        ((3, 5, 11), 12),
        ((3, 5, 17), 24),
        ((3, 5, 19), 60),
        ((3, 5, 29), 60),
        ((3, 5, 31), 60),
        ((3, 11, 13), 84),
        ((3, 11, 17), 24),
        ((3, 11, 19), 60),
        ((3, 11, 23), 132),
        ((3, 11, 29), 60),
        ((3, 11, 31), 60),
        ((3, 13, 17), 56),
        ((3, 13, 19), 140),
    ]
    for primes, expect in kicked:
        order = lcm_all([ORDERS[p] for p in primes])
        modulus = primes[0] * primes[1] * primes[2]
        require(order == expect, f"kick lcm {primes}")
        require(8 * order <= 3 * modulus, f"kick flag {primes}")
    require(8 * 132 > 3 * 345, "345 misses the strong shortness")
    require(8 * 84 > 3 * 195, "195 misses the strong shortness")


def lower_at_195() -> Fraction:
    primes = [3, 5, 13]
    orders = [ORDERS[p] for p in primes]
    modulus = 195
    total = Fraction(0)
    for mask in range(8):
        coeff = Fraction(1)
        step = 1
        for k in range(3):
            if mask & (1 << k):
                coeff *= 1 - Fraction(1, primes[k] * primes[k])
                step = lcm(step, orders[k])
            else:
                coeff *= Fraction(1, primes[k] * primes[k])
        total += coeff * rl(Fraction(2 * step, modulus))
    return total


def main() -> None:
    check_orders()
    check_corners()
    check_explicit_products()
    kick = Fraction(82, 105)
    require(Fraction(3, 4) + Fraction(13, 420) == kick, "kick threshold")
    wide = rl(Fraction(152, 185))
    narrow = rl(Fraction(88, 115))
    require(wide == Fraction(4894346125, 6236939544), "152/185 fraction")
    require(narrow == Fraction(740666125, 851428424), "88/115 fraction")
    require(wide > kick and narrow > kick, "return bounds clear the kick margin")
    low = lower_at_195()
    require(
        low
        == Fraction(
            54421025909829591004375115797555753149956840906272969117235,
            53966707446709005093212565207656544939196850800058844271758,
        ),
        "N=195 fraction",
    )
    require(low > kick, "N=195 clears the kick margin")
    print("squarefree-product-abel: pass")


if __name__ == "__main__":
    main()
