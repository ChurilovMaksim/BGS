#!/usr/bin/env python3
"""Exact Gaussian-integer trace-word certificate for the specified family.

This is a finite symbolic Fourier identity valid uniformly for every odd
N >= 75; it does not inspect numerical spectra or substitute for tau.
"""

from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json

SCALE = 4000


def original_coefficients():
    r = {0: Fraction(1), 1: Fraction(1, 2), -1: Fraction(1, 2),
         7: Fraction(-1, 2), -7: Fraction(-1, 2),
         6: Fraction(-1, 4), -6: Fraction(-1, 4),
         8: Fraction(-1, 4), -8: Fraction(-1, 4)}
    out = defaultdict(lambda: [0, 0])

    def add(w, re=0, im=0):
        re, im = Fraction(re), Fraction(im)
        assert re.denominator == im.denominator == 1
        out[w][0] += re.numerator
        out[w][1] += im.numerator

    for k in (7, -7):
        add((k, 0), 2000)
    for k, value in r.items():
        add((k, 0), 400 * value)
        add((k + 1, 0), im=-20 * value)
        add((k - 1, 0), im=20 * value)
        add((k, 1), -12 * value, -16 * value)
        add((k, -1), -12 * value, 16 * value)
    add((0, 0), -400)
    return {w: tuple(z) for w, z in out.items() if z != [0, 0]}


def mul(z, w):
    return z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0]


def triple_trace_polynomial(a, b, c):
    """Coefficients of exp(pi*i*e/N); total Fourier index is exactly zero."""
    result = defaultdict(lambda: [0, 0])
    count = 0
    for u, z in a.items():
        for v, w in b.items():
            t = -u[0] - v[0], -u[1] - v[1]
            if t not in c:
                continue
            value = mul(mul(z, w), c[t])
            exponent = u[1] * v[0] - u[0] * v[1]
            result[exponent][0] += value[0]
            result[exponent][1] += value[1]
            count += 1
    return {e: tuple(z) for e, z in result.items() if z != [0, 0]}, count


def as_rational(poly):
    assert all(im == 0 for re, im in poly.values())
    return {e: Fraction(z[0], SCALE ** 3) for e, z in poly.items()}


def product(p, q):
    out = defaultdict(Fraction)
    for e, a in p.items():
        for f, b in q.items():
            out[e + f] += a * b
    return {e: a for e, a in out.items() if a}


def main():
    original = original_coefficients()
    assert len(original) == 32
    a = {w: tuple((-1 if w[0] * w[1] % 2 else 1) * z for z in value)
         for w, value in original.items()}
    assert all(a[-k, -l] == (re, -im) for (k, l), (re, im) in a.items())
    b = {(3 * k + 2 * l, 4 * k + 3 * l): z for (k, l), z in a.items()}
    assert all(((3 * k + 2 * l) * (4 * k + 3 * l) - k * l) % 2 == 0
               for k, l in a)
    bounds_a = tuple(max(abs(w[i]) for w in a) for i in (0, 1))
    bounds_b = tuple(max(abs(w[i]) for w in b) for i in (0, 1))
    assert bounds_a == (9, 1) and bounds_b == (27, 36)
    assert tuple(bounds_a[i] + 2 * bounds_b[i] for i in (0, 1)) == (63, 73)
    assert tuple(2 * bounds_a[i] + bounds_b[i] for i in (0, 1)) == (45, 38)
    abb, count_abb = triple_trace_polynomial(a, b, b)
    aab, count_aab = triple_trace_polynomial(a, a, b)
    diff = {e: tuple(abb.get(e, (0, 0))[i] - aab.get(e, (0, 0))[i]
                     for i in (0, 1)) for e in abb.keys() | aab.keys()}
    diff = {e: z for e, z in diff.items() if z != (0, 0)}
    rational = as_rational(diff)
    factor = product({0: Fraction(2), 7: Fraction(-1, 2), -7: Fraction(-1, 2)},
                     {1: Fraction(2), -1: Fraction(2),
                      2: Fraction(-1, 2), -2: Fraction(-1, 2)})
    factor = {e: Fraction(3, 50_000_000) * z for e, z in factor.items()}
    assert rational == factor
    assert count_abb == count_aab == 32
    aaa, count_aaa = triple_trace_polynomial(a, a, a)
    third = as_rational(aaa)
    expected_third = {0: Fraction(-273, 20000)}
    for e, num in ((1, -9), (6, 3), (7, 81), (8, 3)):
        expected_third[e] = expected_third[-e] = Fraction(num, 800000)
    assert third == expected_third
    upper_third = third[0] + sum(abs(value) for e, value in third.items() if e)
    assert upper_third == Fraction(-1341, 100000)
    rbound = Fraction(59, 50)
    lipschitz = 3 * rbound ** 2 + 2 * rbound ** 3
    invariant_lower_bound = Fraction(3, 20_000_000)
    approximate_error_lower_bound = invariant_lower_bound / lipschitz
    assert approximate_error_lower_bound > Fraction(2, 100_000_000)
    root = Path(__file__).resolve().parent
    inputs = [root.parent / 'research_continuation_2026_10_20' /
              'verify_affine_symmetry.py',
              root.parent / 'research_continuation_2026_10_20' /
              'affine_reversal_and_crt_obstructions.md',
              root / 'arithmetic_second_order_proof.md']
    result = {
        'scope': 'Every odd N >= 75, exact symbolic identity; no tau proxy.',
        'arithmetic': 'Gaussian integers at coefficient scale 4000; rational Laurent polynomials.',
        'input_sha256': {str(path): sha256(path.read_bytes()).hexdigest() for path in inputs},
        'symbol_support_size': len(a),
        'symbol_support_bounds': bounds_a,
        'cat_transformed_support_bounds': bounds_b,
        'maximum_total_support_bounds': [63, 73],
        'zero_frequency_triple_counts': {'abb': count_abb, 'aab': count_aab, 'aaa': count_aaa},
        'invariant_laurent_coefficients': {str(e): str(q) for e, q in sorted(rational.items())},
        'invariant_factorization': '3/50000000 * (2-cos(7*x)) * (4*cos(x)-cos(2*x)), x=pi/N',
        'invariant_lower_bound': str(invariant_lower_bound),
        'third_moment_laurent_coefficients': {str(e): str(q) for e, q in sorted(third.items())},
        'third_moment_upper_bound': str(upper_third),
        'lipschitz_coefficient': str(lipschitz),
        'approximate_common_reversal_error_lower_bound': str(approximate_error_lower_bound),
        'non_claims': [
            'No estimate of spectral correlation functions.',
            'No denial of transcendental spectral-dependent antiunitary reversers.',
            'No signed trace cancellation at times proportional to N.'
        ]
    }
    target = root / 'arithmetic_banded_time_reversal.json'
    target.write_text(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + '\n')
    print(json.dumps({'certificate': str(target), 'sha256': sha256(target.read_bytes()).hexdigest(),
                      'verified': True, 'invariant_lower_bound': str(invariant_lower_bound),
                      'approximate_error_lower_bound': str(approximate_error_lower_bound)}, indent=2))


if __name__ == '__main__':
    main()
