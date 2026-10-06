#!/usr/bin/env python3
"""Finite exact controls for the sharp single-orbit resonance constant.

No optional dependencies. Checks rational candidate autocorrelations, the
positive Fejer decomposition, and the attained quadratic lower bound. The
universal real spectral-factor existence is proved in the companion note,
not inferred from the checks. Only a successfully emitted report establishes
that this source was executed.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import random


def determinant_ratios(count: int) -> list[int]:
    """Return D_0,...,D_count with D_r=det(v,T^r v)/det(v,Tv)."""
    if count < 0:
        raise ValueError('count must be nonnegative')
    values = [0, 1]
    for _ in range(1, count):
        values.append(6*values[-1]-values[-2])
    return values[:count+1]


def candidate(span: int) -> dict:
    if span < 0:
        raise ValueError('span must be nonnegative')
    m = span//2
    ratios = determinant_ratios(2*m+1)
    weights = [Q(1, ratios[2*k+1]**2) for k in range(m+1)]
    total = sum(weights, Q(0))
    correlations = [sum(weights[k:], Q(0))/total for k in range(m+1)]
    extended = weights+[Q(0)]
    fejer = [Q(k+1)*(extended[k]-extended[k+1])/total for k in range(m+1)]
    assert all(a > 0 for a in fejer)
    assert sum(fejer, Q(0)) == 1
    for k in range(m+1):
        recovered = sum((fejer[j]*Q(j+1-k, j+1) for j in range(k, m+1)), Q(0))
        assert recovered == correlations[k]
    zero_extended = correlations+[Q(0)]
    energy = sum((ratios[2*k+1]**2*(zero_extended[k]-zero_extended[k+1])**2
                  for k in range(m+1)), Q(0))
    assert energy == 1/total
    return {'span': span, 'M': m, 'sharp_dimensionless_ratio': str(energy),
            'even_autocorrelations_C0_equals_one': list(map(str, correlations)),
            'positive_Fejer_coefficients': list(map(str, fejer))}


def autocorrelation_energy(coefficients: list[Q]) -> Q:
    span = len(coefficients)-1
    ratios = determinant_ratios(span+1)
    correlations = [sum((coefficients[j]*coefficients[j+r]
                        for j in range(len(coefficients)-r)), Q(0))
                    for r in range(span+1)]+[Q(0), Q(0)]
    return sum((ratios[r]**2*(correlations[r-1]-correlations[r+1])**2
                for r in range(1, span+2)), Q(0))


def beta_enclosure(m: int) -> dict:
    if m < 0:
        raise ValueError('nonnegative truncation index required')
    ratios = determinant_ratios(2*m+1)
    partial = sum((Q(1, ratios[2*k+1]**2) for k in range(m+1)), Q(0))
    # lambda>5 and D_(2k+1)>=lambda^(2k) bound the positive tail.
    tail = Q(1, 5**(4*(m+1)))/(1-Q(1, 5**4))
    lower, upper = 1/(partial+tail), 1/partial
    assert Q(0) < lower < upper <= 1
    return {'M': m, 'lower_rational': str(lower), 'upper_rational': str(upper),
            'width_rational': str(upper-lower), 'tail_bound_rational': str(tail),
            'arithmetic': 'exact rational; no floating-point enclosure claims'}


def report() -> dict:
    rows = [candidate(span) for span in range(25)]
    assert rows[0]['sharp_dimensionless_ratio'] == '1'
    assert rows[1]['sharp_dimensionless_ratio'] == '1'
    assert rows[2]['sharp_dimensionless_ratio'] == '1225/1226'
    assert rows[3]['sharp_dimensionless_ratio'] == '1225/1226'
    for m in range(12):
        assert rows[2*m]['sharp_dimensionless_ratio'] == rows[2*m+1]['sharp_dimensionless_ratio']
    rng = random.Random(20260905)
    random_checks = 0
    for span in range(25):
        sharp = Q(rows[span]['sharp_dimensionless_ratio'])
        for _ in range(20):
            coefficients = [Q(rng.randint(-4, 4), rng.randint(1, 5)) for _ in range(span+1)]
            if not any(coefficients):
                coefficients[0] = Q(1)
            c0 = sum((c*c for c in coefficients), Q(0))
            energy = autocorrelation_energy(coefficients)
            assert energy >= sharp*c0*c0
            random_checks += 1
    # The simple two-lag minimization is an exact algebraic check.
    a = Q(1, 1226)
    assert (1-a)**2+1225*a*a == Q(1225, 1226)
    enclosures = [beta_enclosure(m) for m in (0, 1, 2, 4, 8, 12)]
    for left, right in zip(enclosures, enclosures[1:]):
        assert Q(left['lower_rational']) < Q(right['lower_rational'])
        assert Q(right['upper_rational']) < Q(left['upper_rational'])
    return {'producer': str(Path(__file__).name), 'status': 'PASS',
            'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'seed': 20260905, 'finite_span_candidates': rows,
            'rational_random_inequality_checks': random_checks,
            'beta_enclosures': enclosures,
            'scope': ('Exact finite rational checks of candidate autocorrelations, Fejer positivity '
                      'coefficients and energy minima. The real factorization and all-span theorem '
                      'are analytic arguments, not conclusions of a finite search. No BGS claim.')}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    text = json.dumps(report(), indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding='utf-8')
    else:
        print(text, end='')


if __name__ == '__main__':
    main()
