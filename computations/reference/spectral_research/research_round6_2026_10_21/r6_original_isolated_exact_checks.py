#!/usr/bin/env python3
"""Exact checks for r6_original_isolated_cross_occupation.md.

Only Python integer and Fraction arithmetic is used.  The original large-N
theorems are proved in the companion note; these finite tests check the
literal pair definitions, cyclic counts, phases, and coefficient extraction.
"""

from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, product
from math import comb
import json


def legal_sets(n, gap):
    for r in range(1, n // gap + 1):
        for positions in combinations(range(n), r):
            gaps = tuple(
                (positions[(i + 1) % r] - positions[i]) % n
                if r > 1 else n
                for i in range(r)
            )
            if min(gaps) >= gap:
                yield positions, gaps


def count_formula(n, r, gap):
    if r < 1 or n < gap * r:
        return 0
    numerator = n * comb(n - (gap - 1) * r - 1, r - 1)
    assert numerator % r == 0
    return numerator // r


def scalar_eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def scalar_matmul(a, b):
    n = len(a)
    return [
        [sum((a[i][k] * b[k][j] for k in range(n)), F(0))
         for j in range(n)] for i in range(n)
    ]


def scalar_power(a, exponent):
    answer = scalar_eye(len(a))
    for _ in range(exponent):
        answer = scalar_matmul(answer, a)
    return answer


def trace_scalar(a):
    return sum((a[i][i] for i in range(len(a))), F(0))


def clean(poly):
    return {key: value for key, value in poly.items() if value}


def p_add(a, b):
    out = defaultdict(F, a)
    for key, value in b.items():
        out[key] += value
    return clean(out)


def p_mul(a, b):
    out = defaultdict(F)
    for ka, va in a.items():
        for kb, vb in b.items():
            out[tuple(x + y for x, y in zip(ka, kb))] += va * vb
    return clean(out)


def p_scale(a, c):
    if not c:
        return {}
    return clean({key: value * c for key, value in a.items()})


def pmat_eye(n):
    zero = (0,) * n
    return [
        [{zero: F(1)} if i == j else {} for j in range(n)]
        for i in range(n)
    ]


def pmat_mul(a, b):
    n = len(a)
    out = [[{} for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                out[i][j] = p_add(out[i][j], p_mul(a[i][k], b[k][j]))
    return out


def pmat_scalar_right(a, b):
    n = len(a)
    out = [[{} for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                out[i][j] = p_add(out[i][j], p_scale(a[i][k], b[k][j]))
    return out


def trace_poly(a):
    out = {}
    for i in range(len(a)):
        out = p_add(out, a[i][i])
    return out


def charge(n, u, v):
    result = [0] * n
    result[u] += 1
    result[v] -= 1
    return tuple(result)


def defect_matrix(h, denominator_squared, ab=None):
    n = len(h)
    d = [[defaultdict(F) for _ in range(n)] for _ in range(n)]
    if ab is None:
        pairs = [(u, v) for u in range(n) for v in range(n) if u != v]
    else:
        pairs = list(product(*ab))
        assert set(ab[0]).isdisjoint(ab[1])
    for a in range(n):
        for b in range(n):
            for u, v in pairs:
                d[a][b][charge(n, u, v)] += F(
                    h[a][u] * h[u][b] * h[a][v] * h[v][b],
                    denominator_squared ** 2,
                )
            d[a][b] = clean(d[a][b])
    return d


def direct_poly(h, denominator_squared, n, positions, ab=None, seen=None):
    """Enumerate actual ordered pairs once; return their Laurent polynomial."""
    size = len(h)
    fixed = set(positions)
    common = [j for j in range(n) if j not in fixed]
    if ab is None:
        defects = [(u, v) for u in range(size) for v in range(size) if u != v]
    else:
        defects = list(product(*ab))
    out = defaultdict(int)
    count = 0
    for shared_labels in product(range(size), repeat=len(common)):
        x = [0] * n
        y = [0] * n
        for pos, value in zip(common, shared_labels):
            x[pos] = value
            y[pos] = value
        for changes in product(defects, repeat=len(positions)):
            occupation_difference = [0] * size
            for pos, (u, v) in zip(positions, changes):
                x[pos], y[pos] = u, v
                occupation_difference[u] += 1
                occupation_difference[v] -= 1
            assert tuple(j for j in range(n) if x[j] != y[j]) == positions
            if ab is not None:
                assert sum(occupation_difference[v] for v in ab[0]) == len(positions)
            if seen is not None:
                key = (tuple(x), tuple(y))
                assert key not in seen, "An actual rooted pair was counted twice."
                seen.add(key)
            numerator = 1
            for j in range(n):
                numerator *= h[x[j]][x[(j + 1) % n]]
                numerator *= h[y[j]][y[(j + 1) % n]]
            out[tuple(occupation_difference)] += numerator
            count += 1
    expected = size ** len(common) * len(defects) ** len(positions)
    assert count == expected
    denominator = denominator_squared ** n
    return clean({key: F(value, denominator) for key, value in out.items()}), count


def contraction_poly(d, p_powers, gaps):
    out = pmat_eye(len(d))
    for g in gaps:
        out = pmat_mul(out, d)
        out = pmat_scalar_right(out, p_powers[g - 2])
    return trace_poly(out)


def cyclic_count_checks():
    tests = 0
    for gap, activity in ((2, 2), (3, 17), (4, 4), (5, 8)):
        t = [[F(0) for _ in range(gap)] for _ in range(gap)]
        t[0][0] = 1
        t[0][gap - 1] = activity
        for j in range(1, gap):
            t[j][j - 1] = 1
        power = scalar_eye(gap)
        for n in range(1, 81):
            power = scalar_matmul(power, t)
            counts = {
                r: count_formula(n, r, gap)
                for r in range(1, n // gap + 1)
            }
            weighted = 1 + sum(counts[r] * activity ** r for r in counts)
            assert trace_scalar(power) == weighted
            if n <= 18:
                actual = defaultdict(int)
                for positions, gaps in legal_sets(n, gap):
                    assert sum(gaps) == n
                    actual[len(positions)] += 1
                assert dict(actual) == counts
            tests += 1
    q, d = F(1, 4), F(1, 2)
    t = [[q, d], [F(1), F(0)]]
    power = scalar_eye(2)
    for n in range(1, 81):
        power = scalar_matmul(power, t)
        z = sum(
            F(count_formula(n, r, 2)) * d ** r * q ** (n - 2 * r)
            for r in range(1, n // 2 + 1)
        )
        assert z == trace_scalar(power) - q ** n
        tests += 1
    total = d * (2 - q) / ((1 - q - d) * (1 - q))
    assert total == F(14, 3)
    assert F(3) ** 3 - F(3) ** 2 > 17
    assert 96 * F(3, 4) ** 4 / (1 - F(3, 4)) == F(243, 2)
    assert 12 * 9 + F(243, 2) * 8 == 1080
    return tests


def unitary_checks(h, denominator_squared):
    size = len(h)
    for a in range(size):
        for b in range(size):
            assert sum(h[a][u] * h[b][u] for u in range(size)) == (
                denominator_squared if a == b else 0
            )
            assert sum(h[u][a] * h[u][b] for u in range(size)) == (
                denominator_squared if a == b else 0
            )


def run_model(name, h, denominator_squared, max_n, prove_bound=False, c=None):
    size = len(h)
    unitary_checks(h, denominator_squared)
    p = [[F(h[a][b] ** 2, denominator_squared) for b in range(size)]
         for a in range(size)]
    p_powers = [scalar_power(p, ell) for ell in range(max_n + 1)]
    pair_count = 0
    identity_count = 0
    summaries = []
    ab = ((0,), tuple(range(1, size)))
    for gap, colored in ((3, False), (2, True)):
        selection = ab if colored else None
        d = defect_matrix(h, denominator_squared, selection)
        for a in range(size):
            row, column = {}, {}
            for b in range(size):
                row = p_add(row, d[a][b])
                column = p_add(column, d[b][a])
            assert row == {}
            assert column == {}
        polarized_absolute_sum = F(0)
        for n in range(1, max_n + 1):
            complete = {}
            seen = set() if n <= 4 else None
            for positions, gaps in legal_sets(n, gap):
                empirical, count = direct_poly(
                    h, denominator_squared, n, positions, selection, seen
                )
                contracted = contraction_poly(d, p_powers, gaps)
                assert empirical == contracted, (name, n, positions, colored)
                complete = p_add(complete, empirical)
                pair_count += count
                identity_count += 1
            zero = (0,) * size
            at_one = sum(complete.values(), F(0))
            constant = complete.get(zero, F(0))
            unequal = sum(
                (value for key, value in complete.items() if key != zero), F(0)
            )
            assert unequal == at_one - constant
            if colored:
                assert constant == 0
                for key in complete:
                    assert sum(key[v] for v in ab[0]) > 0
                # The opposite orientation has conjugate, here real, value.
                polarized_absolute_sum += 2 * abs(at_one)
            elif prove_bound:
                if n < 3:
                    assert unequal == 0
                elif n == 3:
                    assert abs(unequal) <= 12 * c
                else:
                    assert abs(unequal) <= 96 * (c - 1) * F(3, 4) ** n
            if n in (3, max_n):
                summaries.append({
                    "mode": "polarized_gap2" if colored else "arbitrary_gap3",
                    "n": n,
                    "phase_polynomial_terms": len(complete),
                    "original_signed_sum": str(at_one),
                    "same_occupation_sum": str(constant),
                    "unequal_occupation_sum": str(unequal),
                })
        if colored and prove_bound:
            assert polarized_absolute_sum <= F(28, 3) * size
    return {
        "model": name,
        "size": size,
        "max_n": max_n,
        "exact_pair_enumerations": pair_count,
        "full_laurent_polynomial_identities": identity_count,
        "selected_totals": summaries,
    }


def main():
    results = {"cyclic_count_identities": cyclic_count_checks(), "models": []}
    # Nonflat, rational, genuinely mixed example:
    # P-J has eigenvalues 0 and -41/841, so ||P-J|| < 1/4.
    assert F(41, 841) < F(1, 4)
    results["models"].append(run_model(
        "rational_rotation_20_21_29",
        [[20, 21], [-21, 20]], 841, 10,
        prove_bound=True, c=F(882, 841),
    ))
    # The identities are universal, even when q=1/3 exceeds the theorem's
    # convenient threshold; this model checks repeated labels in odd size.
    results["models"].append(run_model(
        "three_dimensional_householder",
        [[-1, 2, 2], [2, -1, 2], [2, 2, -1]], 9, 7,
    ))
    # Flat P=J: all gap3 contractions vanish identically as Laurent
    # polynomials, although their individual path-pair amplitudes do not.
    results["models"].append(run_model(
        "four_dimensional_hadamard",
        [[1, 1, 1, 1], [1, -1, 1, -1],
         [1, 1, -1, -1], [1, -1, -1, 1]],
        4, 6, prove_bound=True, c=F(1),
    ))
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
