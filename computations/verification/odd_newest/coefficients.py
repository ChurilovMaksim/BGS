"""Exact unchanged 32-mode dictionary extracted from the pinned source.
Assertions are explicit exceptions and survive Python optimization.
"""
from __future__ import annotations
from fractions import Fraction
Vec = tuple[int, int]
Gauss = tuple[int, int]

def coefficients() -> dict[Vec, Gauss]:
    """The exact coefficients d_v = 4000 c_v of 4000 A_N."""
    result: dict[Vec, Gauss] = {}
    diagonal = {1: (200, -20), 2: (0, -10), 5: (0, -5), 6: (-100, -10), 7: (1800, 0), 8: (-100, 10), 9: (0, 5)}
    for k, c in diagonal.items():
        result[0, k] = c
        result[0, -k] = (c[0], -c[1])
    r = {0: Fraction(1), 1: Fraction(1, 2), -1: Fraction(1, 2), 6: Fraction(-1, 4), -6: Fraction(-1, 4), 7: Fraction(-1, 2), -7: Fraction(-1, 2), 8: Fraction(-1, 4), -8: Fraction(-1, 4)}
    for k, value in r.items():
        if not (4 * value).denominator == 1:
            raise AssertionError('Verification failed: (4 * value).denominator == 1')
        d = int(4 * value)
        result[1, k] = (-3 * d, -4 * d)
        result[-1, k] = (-3 * d, 4 * d)
    if not len(result) == 32:
        raise AssertionError('Verification failed: len(result) == 32')
    if not all((result[-a, -b] == (c[0], -c[1]) for (a, b), c in result.items())):
        raise AssertionError('Verification failed: all((result[-a, -b] == (c[0], -c[1]) for (a, b), c in result.items()))')
    return result
