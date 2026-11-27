#!/usr/bin/env python3
"""Exact finite Fejér lower bounds at the original BGS coupling."""

from fractions import Fraction
from math import isqrt


def require(condition: bool, label: str) -> None:
    if not condition:
        raise RuntimeError(f"Pell Fejér certificate failed: {label}")


def main() -> None:
    sigma = Fraction(1650797, 4000000)
    fourier = {0: 4, 1: 2, -1: 2, 6: -1, -6: -1, 7: -2, -7: -2, 8: -1, -8: -1}
    support = []
    for k in range(-9, 10):
        value = fourier.get(k, 0)
        real_part = 2000 * (abs(k) == 7) + 100 * value - 400 * (k == 0)
        imaginary_part = 5 * (fourier.get(k - 1, 0) - fourier.get(k + 1, 0))
        weight = abs(real_part) + abs(imaginary_part)
        if weight:
            support.append((0, k, weight))
        if value:
            support.extend((sign, k, 7 * abs(value)) for sign in (-1, 1))
    require(len(support) == 32, "literal Weyl support")
    thresholds = {197: 26202, 199: 4452, 201: 740, 203: 109, 205: 9}
    dimension, pell = 1, 0
    for order in range(1, 208):
        dimension, pell = dimension + 2 * pell, dimension + pell
        if order not in thresholds and order != 207:
            continue
        time = Fraction(dimension, 10**80)
        shifted = support[:]
        mass = 0
        for _ in range((order - 1) // 2):
            shifted = [
                ((3*a + 4*b) % dimension, (2*a + 3*b) % dimension, weight)
                for a, b, weight in shifted
            ]
            for x, y, in_weight in support:
                for a, b, out_weight in shifted:
                    determinant = (x*b - y*a) % dimension
                    distance = min(determinant, dimension - determinant)
                    mass += in_weight * out_weight * min(7*dimension, 22*distance)

        commutator = Fraction(order * mass, 7 * dimension * 4000**2)
        squared_hs = order * sigma
        scale = 10**9
        upper_hs = Fraction(isqrt(squared_hs.numerator * scale**2 // squared_hs.denominator) + 1, scale)
        require(upper_hs**2 >= squared_hs, "upward square-root enclosure")
        eta = time * upper_hs + commutator * time**2
        window = dimension // 4
        last = min((window - 1)//order, isqrt(2 * eta.denominator**2 // eta.numerator**2))
        lower = Fraction(dimension, window) * sum(
            (1 - Fraction(order * j, window))**2 * max(0, 1 - Fraction(j*j, 2) * eta**2)**2
            for j in range(1, last + 1)
        )
        if order in thresholds:
            require(lower > thresholds[order], f"order {order}")
            print(order, "active terms", last, "floor(1000*lower bound)", int(1000*lower))
        else:
            # Section 3 of pell_microscopic_window.md supplies the older one-term bound.
            older = Fraction(dimension, window) * (1 - Fraction(order, window))**2 * Fraction(31, 50)**2
            require(older > Fraction(3, 2), "order 207 via the older Weyl certificate")
            print("207: existing one-term lower bound for Fejer energy > 3/2")


if __name__ == "__main__":
    main()
