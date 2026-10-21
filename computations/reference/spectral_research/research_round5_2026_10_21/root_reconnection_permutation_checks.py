"""Finite exact cross-check of Hamiltonian reconnection cycle counts.

This script checks only finite combinatorics. It is not an asymptotic
spectral test and is not needed to assume any universality statement.
"""

from collections import Counter
from itertools import permutations
from math import comb, factorial


def cycle_count(mapping):
    seen = set()
    total = 0
    for v in range(len(mapping)):
        if v in seen:
            continue
        total += 1
        cur = v
        while cur not in seen:
            seen.add(cur)
            cur = mapping[cur]
    return total


def counts(r):
    gamma = [(i + 1) % r for i in range(r)]
    out = Counter()
    for tail in permutations(range(1, r)):
        order = (0,) + tail
        sigma = [None] * r
        for i, v in enumerate(order):
            sigma[v] = order[(i + 1) % r]
        if any(sigma[i] == gamma[i] for i in range(r)):
            continue
        inv = [None] * r
        for i, v in enumerate(sigma):
            inv[v] = i
        pi = [inv[gamma[i]] for i in range(r)]
        assert all(pi[i] != i for i in range(r))
        c = cycle_count(pi)
        assert (r - c) % 2 == 0
        out[c] += 1
    expected = sum((-1)**j * comb(r, j) * factorial(r - j - 1)
                   for j in range(r)) + (-1)**r
    assert sum(out.values()) == expected
    return dict(sorted(out.items()))


if __name__ == "__main__":
    wolfram_checked = {
        3: {1: 1},
        4: {2: 1},
        5: {1: 8},
        6: {2: 36},
        7: {1: 180, 3: 49},
        8: {2: 1604, 4: 21},
        9: {1: 8064, 3: 5144},
    }
    for r, expected in wolfram_checked.items():
        actual = counts(r)
        assert actual == expected, (r, actual, expected)
        print(r, actual, "total", sum(actual.values()))
    print("All exact Python counts agree with corrected Wolfram enumeration.")
