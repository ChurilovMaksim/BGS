#!/usr/bin/env python3
"""Exact finite check supplementing the uniform affine-symmetry proof.

All coefficients are pairs of integers representing 4000 times a Gaussian
rational coefficient. No floating point or probabilistic sampling is used.
Run: python3 research_continuation_2026_10_20/verify_affine_symmetry.py
"""

from collections import defaultdict
from fractions import Fraction
import json


def original_coefficients():
    r = {
        0: Fraction(1),
        1: Fraction(1, 2), -1: Fraction(1, 2),
        7: Fraction(-1, 2), -7: Fraction(-1, 2),
        6: Fraction(-1, 4), -6: Fraction(-1, 4),
        8: Fraction(-1, 4), -8: Fraction(-1, 4),
    }
    coefficients = defaultdict(lambda: [0, 0])

    def add(index, real=0, imag=0):
        real, imag = Fraction(real), Fraction(imag)
        assert real.denominator == imag.denominator == 1
        coefficients[index][0] += real.numerator
        coefficients[index][1] += imag.numerator

    for k in (7, -7):
        add((k, 0), 2000)
    for k, value in r.items():
        add((k, 0), 400 * value)
        add((k + 1, 0), imag=-20 * value)
        add((k - 1, 0), imag=20 * value)
        add((k, 1), -12 * value, -16 * value)
        add((k, -1), -12 * value, 16 * value)
    add((0, 0), -400)
    result = {
        index: tuple(value)
        for index, value in coefficients.items()
        if value != [0, 0]
    }
    for (k, l), (real, imag) in result.items():
        assert result.get((-k, -l)) == (real, -imag)
    assert len(result) == 32
    return result


def alias(original, n):
    coefficients = defaultdict(lambda: [0, 0])
    for (k, l), (real, imag) in original.items():
        coefficients[k % n, l % n][0] += real
        coefficients[k % n, l % n][1] += imag
    return {
        index: tuple(value)
        for index, value in coefficients.items()
        if value != [0, 0]
    }


def check_dimension(original, n):
    full = alias(original, n)
    mean = full.get((0, 0), (0, 0))
    coefficients = {v: c for v, c in full.items() if v != (0, 0)}
    e1, e2 = (1, 0), (0, 1)
    c1, c2 = coefficients[e1], coefficients[e2]
    assert c1 != (0, 0) and c2 != (0, 0)

    def positions(value):
        return sorted(v for v, c in coefficients.items() if c == value)

    assert positions(c1) == [e1]
    assert positions((c1[0], -c1[1])) == [(n - 1, 0)]
    assert positions((-c1[0], -c1[1])) == []
    assert positions((-c1[0], c1[1])) == []
    assert positions(c2) == [e2]
    assert positions((c2[0], -c2[1])) == [(0, n - 1)]
    for (k, l), (real, imag) in coefficients.items():
        assert coefficients.get((-k % n, -l % n)) == (real, -imag)

    support = sorted(coefficients)
    candidates = 0
    matches = []
    for first in support:
        for second in support:
            determinant = (
                first[0] * second[1] - second[0] * first[1]
            ) % n
            if determinant not in (1, n - 1):
                continue
            candidates += 1
            antiunitary = determinant == n - 1
            for sign in (1, -1):
                for (k, l), (real, imag) in coefficients.items():
                    target = (
                        (first[0] * k + second[0] * l) % n,
                        (first[1] * k + second[1] * l) % n,
                    )
                    expected = (
                        sign * real,
                        sign * (-imag if antiunitary else imag),
                    )
                    if coefficients.get(target) != expected:
                        break
                else:
                    matches.append({
                        "columns": [list(first), list(second)],
                        "antiunitary": antiunitary,
                        "sign": sign,
                    })
    assert matches == [{
        "columns": [[1, 0], [0, 1]],
        "antiunitary": False,
        "sign": 1,
    }]
    result = {
        "N": n,
        "support_size": len(support),
        "candidate_linear_maps": candidates,
        "mean_scaled4000": list(mean),
        "q_basis_scaled4000": list(c1),
        "p_basis_scaled4000": list(c2),
        "matches": matches,
    }
    if n in (3, 5, 9):
        result["pure_q_scaled4000"] = [
            [k, list(coefficients.get((k, 0), (0, 0)))]
            for k in range(1, n)
        ]
    return result


def main():
    original = original_coefficients()
    n7 = alias(original, 7)
    assert n7 == {(0, 0): (3600, 0)}
    dimensions = [n for n in range(3, 101, 2) if n != 7]
    results = [check_dimension(original, n) for n in dimensions]
    assert len(results) == 48
    assert sum(item["candidate_linear_maps"] for item in results) == 5600
    print(json.dumps({
        "arithmetic": "exact Gaussian integers; coefficient scale 4000",
        "assertion_tested": (
            "Coefficient uniqueness and complete signed Weyl-index symmetry "
            "classification with trivial character for odd 3 <= N <= 99, N != 7."
        ),
        "character_reduction": (
            "Proved separately using Q(i) intersect mu_N = {1} for odd N."
        ),
        "dimension_count": len(results),
        "candidate_linear_maps": 5600,
        "N7_mean_scaled4000": [3600, 0],
        "non_claims": [
            "No numerical inference of a universal theorem.",
            "No claim about arbitrary non-Clifford antiunitaries.",
            "No spectral-statistics or Hdiag conclusion.",
        ],
        "dimensions": results,
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
