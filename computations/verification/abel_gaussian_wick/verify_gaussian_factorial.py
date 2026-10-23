#!/usr/bin/env python3
"""Exact finite checks of the flat equal-edge / Ginibre comparison.

Arithmetic: integers and fractions.Fraction only. Coverage is printed as JSON.
No assertions are used; checks remain active with python -O. These finite
tests do not establish the asymptotic theorem proved in the accompanying note.
"""

from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from math import comb, factorial, prod
import hashlib
import json
from pathlib import Path


def check(ok, message):
    if not ok:
        raise RuntimeError(message)


def cycles(sigma):
    remaining = set(range(len(sigma)))
    result = []
    while remaining:
        start = min(remaining)
        cycle = []
        j = start
        while j in remaining:
            remaining.remove(j)
            cycle.append(j)
            j = sigma[j]
        result.append(cycle)
    return result


def cycle_partition_count_after_join(sigma, blocks):
    parent = list(range(len(sigma)))

    def root(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def join(a, b):
        parent[root(a)] = root(b)

    for i, j in enumerate(sigma):
        join(i, j)
    for block in blocks:
        for i in block[1:]:
            join(block[0], i)
    return len({root(i) for i in range(len(sigma))})


def edge_table(x):
    return tuple(sorted(Counter(zip(x, x[1:] + x[:1])).items()))


def gaussian_integer(n, m):
    return factorial(m) * (comb(n + m, m + 1) - (comb(n, m + 1) if n > m else 0))


def a(n, m):
    return Fraction(prod(n + j for j in range(m)), n ** m)


def q(n, m):
    if m >= n:
        return Fraction(0)
    return prod(Fraction(n - j, n + j) for j in range(m + 1))


def r(n, m):
    q3 = Fraction(6, (n + 1) * (n + 2))
    q22 = Fraction(4 * (n + 5), (n + 1) * (n + 2) * (n + 3))
    return 3 * q3 if m == 3 else m * q3 + (comb(m, 2) - m) * q22


def main():
    word_count = type_count = cases = one_circuit_cases = permutation_checks = 0
    samples = []
    for n in range(1, 6):
        for m in range(1, 9):
            if n ** m > 70000:
                continue
            tables = Counter()
            weighted_collision = 0
            for x in product(range(n), repeat=m):
                nu = edge_table(x)
                tables[nu] += 1
                f = prod(factorial(v) for v in Counter(x).values())
                cedge = sum(k * (k - 1) // 2 for _, k in nu)
                weighted_collision += f * cedge
                word_count += 1
            bi = gi = 0
            for nu, c in tables.items():
                rows = Counter()
                for (u, v), k in nu:
                    rows[u] += k
                f = prod(factorial(v) for v in rows.values())
                d = prod(factorial(k) for _, k in nu)
                ce = sum(k * (k - 1) // 2 for _, k in nu)
                check(c * d <= m * f, ('factorial domination', n, m, nu))
                check(2 * (d - 1) <= d * ce, ('factorial deficit', n, m, nu))
                if ce:
                    check(2 * c * d <= m * f, ('repeat domination', n, m, nu))
                bi += c * c
                gi += c * c * d
            check(gi == gaussian_integer(n, m), ('Gaussian formula', n, m))
            type_count += len(tables)
            if m >= 3:
                aa, rr = a(n, m), r(n, m)
                check(Fraction(weighted_collision, n ** m) == aa * rr,
                      ('weighted collision identity', n, m))
                upper = m * aa * rr / 4
                check(0 <= Fraction(gi - bi, n ** m) <= upper,
                      ('absolute finite comparison', n, m))
                error = Fraction(m * (m + 1), 4 * (n + m)) * rr / (1 - q(n, m))
                check(Fraction(gi - bi, gi) <= error,
                      ('relative finite comparison', n, m))
                convenient = Fraction(5 * m * m, 2 * n * n) * (1 + Fraction(m * (m + 1), n))
                check(error <= convenient, ('convenient finite bound', n, m))
            elif m == 2:
                check(gi == 2 * n ** 2 and bi == 2 * n ** 2 - n,
                      ('length two exception', n))
            else:
                check(bi == gi == n, ('length one', n))
            if n in (3, 5) and m in (4, 6, 8):
                samples.append({'N': n, 'm': m, 'B_over_G': str(Fraction(bi, gi))})
            cases += 1

    # Independent direct join enumerations check the two exact rational
    # probabilities and deletion consistency on up to seven marked/unmarked slots.
    for n in (1, 2, 7):
        for k, blocks, expected in (
            (3, ((0, 1, 2),), Fraction(6, (n + 1) * (n + 2))),
            (4, ((0, 2), (1, 3)), Fraction(4 * (n + 5), (n + 1) * (n + 2) * (n + 3))),
        ):
            for m in range(k, 8):
                numerator = sum(n ** cycle_partition_count_after_join(s, blocks)
                                for s in permutations(range(m)))
                denominator = prod(n + j for j in range(m))
                check(Fraction(numerator, denominator) == expected,
                      ('Ewens constraint consistency', n, k, m))
                permutation_checks += factorial(m)

    # Exact one-circuit reconnection count with repeated edges and periodic words.
    for n in (1, 2, 3):
        for m in range(1, 6):
            tables = Counter(edge_table(x) for x in product(range(n), repeat=m))
            perms = list(permutations(range(m)))
            for x in product(range(n), repeat=m):
                count = 0
                for sigma in perms:
                    if all(x[i] == x[sigma[i]] for i in range(m)):
                        gs = tuple((sigma[i] + 1) % m for i in range(m))
                        if len(cycles(gs)) == 1:
                            count += 1
                nu = edge_table(x)
                d = prod(factorial(k) for _, k in nu)
                check(m * count == tables[nu] * d,
                      ('one circuit marginal', n, m, x))
                one_circuit_cases += 1

    # Larger exact certificates do not enumerate words.
    large = []
    for n, m in ((100003, 316), (100003, 2000), (1000000007, 100000), (1000000007, 1000000)):
        rr = r(n, m)
        # exp bound avoided: 1-Q >= x/(1+x), x=m(m+1)/N.
        x = Fraction(m * (m + 1), n)
        certified = Fraction(m * (m + 1), 4 * (n + m)) * rr * (1 + x) / x
        large.append({'N': n, 'm': m, 'relative_deficit_upper_rational': str(certified),
                      'relative_deficit_upper_decimal': float(certified)})
    receipt = {
        'status': 'PASS', 'arithmetic': 'exact integers and rational fractions',
        'rooted_words': word_count, 'edge_tables': type_count,
        'word_enumeration_cases': cases, 'permutation_join_checks': permutation_checks,
        'one_circuit_word_checks': one_circuit_cases,
        'samples': samples, 'large_exact_upper_bounds': large,
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'nonclaims': ['No finite check proves an asymptotic theorem.',
                      'No physical fixed-unitary signed statistic is evaluated.',
                      'No extension beyond m=o(N^(3/4)) is certified.'],
    }
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
