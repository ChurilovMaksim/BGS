#!/usr/bin/env python3
"""Exact finite checks of weighted Cayley moment and norm identities.

The asymptotic theorems are proved in mathematics/cayley_trace_gaussian_limit.md.
This checks stated finite tuple domains, not the infinite Chowla/BV inputs.
Run from any directory; --output writes a reproducible JSON certificate.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from functools import lru_cache
import hashlib
from itertools import product
import json
from math import factorial
from pathlib import Path

import sympy as sp


def balanced(K, exponents, weights):
    totals = [0] * ((K - 1) // 2)
    for a, w in zip(exponents, weights):
        if a <= (K - 1) // 2:
            totals[a - 1] += w
        else:
            totals[K - a - 1] -= w
    return not any(totals)


def scalar_baseline(K, r):
    if r % 2:
        return 0
    s = r // 2
    coeff = [Fraction(1)] + [Fraction(0)] * s
    for _ in range((K - 1) // 2):
        coeff = [sum((coeff[i-j] / factorial(j)**2 for j in range(i+1)),
                     Fraction(0)) for i in range(s+1)]
    value = factorial(r) * coeff[s]
    assert value.denominator == 1
    return value.numerator


def cayley_design(K, p):
    if not (sp.isprime(K) and K % 2 == 1 and sp.isprime(p)
            and (p - 1) % K == 0):
        raise ValueError('requires odd prime K and prime p == 1 (mod K)')
    h = pow(int(sp.primitive_root(p)), (p - 1) // K, p)
    values = {a: ((pow(h, a, p) + 1) *
                  pow(pow(h, a, p) - 1, -1, p)) % p for a in range(1, K)}
    assert len(set(values.values())) == K - 1
    assert all((values[a] + values[K-a]) % p == 0 for a in values)
    return h, values


def zero_count(K, p, weights):
    _, values = cayley_design(K, p)
    current = Counter({0: 1})
    for w in weights:
        following = Counter()
        for x, count in current.items():
            for a in values.values():
                following[(x + w*a) % p] += count
        current = following
    assert sum(current.values()) == (K-1)**len(weights)
    return current[0]


def numerator(K, exponents, weights):
    """Expand the cleared numerator in Z[T]/(T^K-1), with integer coefficients."""
    total = [0] * K
    for i, w in enumerate(weights):
        coeff = [0] * K
        coeff[0] = w
        for j, a in enumerate(exponents):
            sign = 1 if j == i else -1
            updated = [sign*c for c in coeff]
            for k, c in enumerate(coeff):
                updated[(k+a) % K] += c
            coeff = updated
        total = [a+b for a, b in zip(total, coeff)]
    return tuple(total)


@lru_cache(None)
def norm(K, coefficients):
    T = sp.Symbol('T')
    phi = sum(T**i for i in range(K))
    # Subtract the last coefficient times Phi_K to lower the degree.
    reduced = sum((coefficients[i] - coefficients[-1])*T**i
                  for i in range(K-1))
    return int(sp.resultant(phi, reduced, T))


def eval_poly(coeff, x, p):
    value = 0
    for c in reversed(coeff):
        value = (value*x+c) % p
    return value


def valuation(integer, p):
    integer = abs(integer)
    assert integer
    count = 0
    while integer % p == 0:
        count += 1
        integer //= p
    return count


def check_word(K, weights):
    n, r = K-1, len(weights)
    split_primes = [int(p) for p in sp.primerange(3, 258) if (p-1) % K == 0]
    designs = {p: cayley_design(K, p) for p in split_primes}
    excess = Counter()
    forced_orbits = 0
    tested = 0
    nonzero_norms = 0
    valuation_checks = 0
    for tail in product(range(1, K), repeat=r-1):
        exponents = (1,) + tail
        is_balanced = balanced(K, exponents, weights)
        coeff = numerator(K, exponents, weights)
        R = norm(K, coeff)
        assert (R == 0) == is_balanced, (K, weights, exponents, R)
        assert sum(abs(c) for c in coeff) <= sum(weights)*2**r
        orbit = [tuple((u*a) % K for a in exponents) for u in range(1, K)]
        assert len(set(orbit)) == n
        assert all(balanced(K, a, weights) == is_balanced for a in orbit)
        tested += 1
        if is_balanced:
            forced_orbits += 1
            continue
        nonzero_norms += 1
        assert R % K**(r-1) == 0
        assert abs(R) <= (sum(weights)*2**r)**n
        consumed = 1
        for p, (h, values) in designs.items():
            s = 0
            for u, a in enumerate(orbit, start=1):
                vanishes = sum(w*values[b] for w, b in zip(weights, a)) % p == 0
                assert vanishes == (eval_poly(coeff, pow(h, u, p), p) == 0)
                s += vanishes
            assert s <= valuation(R, p), (K, weights, exponents, p)
            consumed *= p**s
            excess[p] += s
            valuation_checks += 1
        # An exact integer version of the tested part of the logarithmic budget.
        assert (abs(R) // K**(r-1)) % consumed == 0
    B = n*forced_orbits
    if len(set(weights)) == 1 and weights[0] == 1:
        assert B == scalar_baseline(K, r)
    if weights == (1, 1, 2):
        assert B == n
    for p in split_primes:
        Z = zero_count(K, p, weights)
        assert Z == B+excess[p], (K, weights, p, Z, B, excess[p])
    return {'K': K, 'weights': weights, 'ordered_tuples': n**r,
            'normalized_orbits': tested, 'nonzero_resultants': nonzero_norms,
            'balanced_tuples': B, 'split_primes': split_primes,
            'orbit_valuation_checks': valuation_checks}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    configs = [(K, (1,)*r) for K, maximum in [(3, 7), (5, 5), (7, 4), (11, 3)]
               for r in range(1, maximum+1)]
    configs += [(K, word) for K in [3, 5, 7]
                for word in [(1, 1, 2), (1, 2, 3), (1, 1, 2, 2), (3,)]]
    configs += [(3, (7,))]  # The split prime p=7 divides the fixed weight.
    cases = [check_word(K, word) for K, word in configs]
    controls = []
    for K, p, expected in [(11, 199, [6, 270, 12250]),
                            (13, 521, [6, 396, 22650])]:
        actual = [zero_count(K, p, (1,)*r) for r in [3, 4, 6]]
        B = [scalar_baseline(K, r) for r in [3, 4, 6]]
        assert actual == expected and actual[1] == B[1] and actual[2] > B[2]
        controls.append({'K': K, 'p': p, 'orders': [3, 4, 6],
                         'zero_counts': actual, 'balanced_counts': B})
    # Reject a superficially plausible pair outside the theorem's domain.
    try:
        cayley_design(11, 521)
    except ValueError:
        pass
    else:
        raise AssertionError('nonsplit design accepted')
    result = {'schema': 1, 'status': 'FINITE-REGRESSION',
              'base_commit': 'd6086cfa9ce9be37aa3d936875e8ec1da3edf811',
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'associated_proof_sha256': {
                  name: hashlib.sha256((Path(__file__).resolve().parents[2]/name)
                                       .read_bytes()).hexdigest()
                  for name in ['mathematics/cayley_trace_gaussian_limit.md',
                               'manuscript/unified_sections/cayley_trace_gaussian.tex']},
              'scope': 'All ordered tuples represented by every normalized scaling orbit '
                       'in each listed (K,word); all split primes up to 257 for valuation tests. '
                       'Not an asymptotic proof or enumeration of all exceptional primes.',
              'cases': cases, 'counterexamples': controls,
              'totals': {key: sum(c[key] for c in cases) for key in
                         ['ordered_tuples', 'normalized_orbits', 'nonzero_resultants',
                          'orbit_valuation_checks']}}
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'cases': len(cases), **result['totals'],
                      'counterexamples': controls}, indent=2))


if __name__ == '__main__':
    main()
