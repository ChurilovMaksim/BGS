#!/usr/bin/env python3
"""Exact finite regression for bandlimited_correlation_extension.md."""

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
from fractions import Fraction as F
from itertools import permutations, product
from math import prod, factorial
import json
import random


def lifts(delta, low, high, period, closed=False):
    """All lifts in a bounded rational interval; exact endpoint decisions."""
    start = (low - delta) // period - 1
    stop = (high - delta) // period + 2
    return [delta + m * period for m in range(start, stop)
            if low <= delta + m * period
            and (delta + m * period <= high if closed
                 else delta + m * period < high)]


def cube_mass(points, k, lows, width=F(1), closed=False):
    n = len(points)
    count = 0
    for labels in permutations(range(n), k):
        anchor = points[labels[-1]]
        count += prod(len(lifts(points[j]-anchor, a, a+width, n, closed))
                      for j, a in zip(labels[:-1], lows))
    return F(count, n)


def overlap_mass(points, k):
    n = len(points)
    total = F(0)
    for labels in permutations(range(n), k):
        anchor = points[labels[-1]]
        choices = [lifts(points[j]-anchor, F(-2), F(2), n, True)
                   for j in labels[:-1]]
        for z in product(*choices):
            span = max((F(0),) + z) - min((F(0),) + z)
            total += max(F(0), F(2)-span)
    return total / n


def occupation(points, t):
    n = len(points)
    return sum((x-t) % n < 2 for x in points)


def integrate_occupation(points, shifts, integrand):
    """Integrate constant values on exact window-entry/exit intervals."""
    n = len(points)
    breaks = sorted({F(0), F(n)} |
                    {(x-a-b) % n for x in points for a in shifts
                     for b in (F(0), F(2))})
    return sum((right-left)*integrand([
        occupation(points, (left+right)/2+a) for a in shifts])
        for left, right in zip(breaks, breaks[1:])) / n


def falling(r, k):
    return factorial(r)//factorial(r-k) if r >= k else 0


def main():
    rng = random.Random(73019)
    cases = []
    for n in (3, 4, 6):
        cases.extend([
            ("clock", [F(j) for j in range(n)]),
            ("cluster", [F(0)]*n),
            ("repeated", [F(j//2) for j in range(n)]),
            ("seeded", [F(rng.randrange(8*n), 8) for _ in range(n)]),
        ])
    configurations = inequalities = identities = 0
    for name, points in cases:
        for k in range(2, 6):
            configurations += 1
            mean = integrate_occupation(points, [F(0)], lambda r: r[0])
            fact = integrate_occupation(points, [F(0)], lambda r: falling(r[0], k))
            power = integrate_occupation(points, [F(0)], lambda r: r[0]**k)
            local = cube_mass(points, k, [F(-2)]*(k-1), F(4), True)
            assert mean == 2, (name, k, "mean")
            assert fact == overlap_mass(points, k), (name, k, "overlap")
            identities += 2
            assert fact <= 2*local
            assert power <= 2*k**k*(1+local)
            inequalities += 2
            translations = [[F(0)]*(k-1), [F(-1, 2)]*(k-1),
                            [F(3*i-7, 2) for i in range(k-1)],
                            [F(100*len(points)+i, 3) for i in range(k-1)]]
            for a in translations:
                mass = cube_mass(points, k, a)
                mixed = integrate_occupation(points, a+[F(0)], prod)
                assert mass <= mixed <= power, (name, k, a, mass, mixed, power)
                inequalities += 2
    # Signed normalization does not ensure the positivity needed in (3).
    n, k = 12, 2
    clock, cluster = list(map(F, range(n))), [F(0)]*n
    signed_local = (2*cube_mass(clock, k, [F(-2)], F(4), True)
                    - cube_mass(cluster, k, [F(-2)], F(4), True))
    signed_cube = 2*cube_mass(clock, k, [F(6)])-cube_mass(cluster, k, [F(6)])
    signed_rhs = 2*k**k*(1+signed_local)
    assert (signed_local, signed_cube, signed_rhs) == (-3, 2, -16)
    assert signed_cube > signed_rhs
    print(json.dumps({"status": "pass", "arithmetic": "exact rational",
                      "configuration_order_cases": configurations,
                      "identities": identities, "inequalities": inequalities,
                      "signed_average_counterexample": {
                          "cube_mass": str(signed_cube), "bound_rhs": str(signed_rhs)}},
                     sort_keys=True))


if __name__ == "__main__":
    main()
