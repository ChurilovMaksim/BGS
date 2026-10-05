#!/usr/bin/env python3
"""Exact finite controls for FLOW-021, not an asymptotic BGS certificate.

Rational sparse trace polynomials versus D5 and radial Laurent derivatives;
determinant coefficients are also evaluated on genuine diagonal unitaries.
No simulated Brownian paths or large-N frozen operator are used.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction as R
from math import factorial
import hashlib
import json
from pathlib import Path
import platform

from microscopic_noise_removal import partitions, expand_symbolic, radial_generator
from growing_degree_trace_projection import (
    wick_word, permutation_cut_join, polynomial_generator,
)


def clean(p):
    return {w: c for w, c in p.items() if c}


def add(target, source, coefficient=R(1)):
    for word, value in source.items():
        target[word] += coefficient*value


def hook_modes(m):
    modes = [defaultdict(R) for _ in range(m)]
    for word in partitions(m):
        word = tuple(sorted(word))
        z = 1
        for j, count in Counter(word).items():
            z *= j**count*factorial(count)
        coefficients = [1]+[0]*m
        for j in word:
            previous = coefficients[:]
            for k in range(j, m+1):
                coefficients[k] -= previous[k-j]
        running = 0
        for r in range(m):
            running += coefficients[r]
            modes[r][word] += R(running, z)
        assert sum(coefficients) == 0
    return [clean(p) for p in modes]


def holo_gram(left, right):
    result = R(0)
    for word, c in left.items():
        z = 1
        for j, count in Counter(word).items():
            z *= j**count*factorial(count)
        result += c*right.get(word, R(0))*z
    return result


def cut_join(p):
    out = defaultdict(R)
    for word, c in p.items():
        add(out, permutation_cut_join(word), c)
    return clean(out)


def mixed_wick(left, right):
    out = defaultdict(R)
    for a, ca in left.items():
        for b, cb in right.items():
            raw = tuple(sorted(a+tuple(-j for j in b)))
            add(out, wick_word(raw)[0], ca*cb)
    return clean(out)


def cmul(z, u):
    return z[0]*u[0]-z[1]*u[1], z[0]*u[1]+z[1]*u[0]


def cadd(z, u):
    return z[0]+u[0], z[1]+u[1]


def cscale(z, a):
    return z[0]*a, z[1]*a


def cpow(z, k):
    out = (R(1), R(0))
    for _ in range(k):
        out = cmul(out, z)
    return out


def traces(nodes, maximum):
    out = {}
    for j in range(1, maximum+1):
        value = (R(0), R(0))
        for node in nodes:
            value = cadd(value, cpow(node, j))
        out[j] = value
        out[-j] = value[0], -value[1]
    return out


def evaluate(polynomial, values):
    result = (R(0), R(0))
    for word, c in polynomial.items():
        value = (R(1), R(0))
        for j in word:
            value = cmul(value, values[j])
        result = cadd(result, cscale(value, c))
    return result


def determinant_coefficients(nodes, scale):
    out = [(R(1), R(0))]
    for node in nodes:
        previous = out
        out = [(R(0), R(0)) for _ in range(len(previous)+1)]
        for k, coefficient in enumerate(previous):
            out[k] = cadd(out[k], coefficient)
            out[k+1] = cadd(out[k+1], cscale(cmul(coefficient, node), -scale))
    return out


def determinant_hooks(nodes, y, maximum):
    if y == 1:
        return [None]+[traces(nodes, maximum)[j] for j in range(1, maximum+1)]
    numerator = determinant_coefficients(nodes, y)
    denominator = determinant_coefficients(nodes, R(1))
    quotient = [(R(1), R(0))]
    for k in range(1, maximum+1):
        value = numerator[k] if k < len(numerator) else (R(0), R(0))
        for j in range(1, min(k, len(denominator)-1)+1):
            value = cadd(value, cscale(cmul(denominator[j], quotient[k-j]), -1))
        quotient.append(value)
    return [None]+[cscale(value, 1/(1-y)) for value in quotient[1:]]


def squared(z):
    return z[0]**2+z[1]**2


def run():
    counts = Counter()
    all_modes = {}
    for m in range(1, 9):
        modes = hook_modes(m)
        all_modes[m] = modes
        raw_sum = defaultdict(R)
        for r, mode in enumerate(modes):
            eigenvalue = R(m*(m-1-2*r), 2)
            assert cut_join(mode) == clean({w: eigenvalue*c for w, c in mode.items()})
            counts['holomorphic_cut_join_modes'] += 1
            add(raw_sum, mode)
            for s, other in enumerate(modes):
                assert holo_gram(mode, other) == (1 if r == s else 0)
                counts['holomorphic_gram_entries'] += 1
        assert clean(raw_sum) == {(m,): R(1)}
        counts['power_sum_reconstructions'] += 1

    for m in range(1, 6):
        modes = all_modes[m]
        for r, left in enumerate(modes):
            for s, right in enumerate(modes):
                wick = mixed_wick(left, right)
                for n in sorted({2*m, 2*m+1}):
                    rate = R(m)+R(m*(m-1-r-s), n)
                    assert polynomial_generator(n, wick) == clean({w: -rate*c for w, c in wick.items()})
                    counts['mixed_wick_d5_eigenvectors'] += 1
                if m <= 3:
                    for n in sorted({2*m, max(3, 2*m)}):
                        expanded = expand_symbolic(n, wick)
                        rate = R(m)+R(m*(m-1-r-s), n)
                        assert radial_generator(n, expanded) == clean({w: -rate*c for w, c in expanded.items()})
                        counts['radial_laurent_eigenvectors'] += 1

    y_nodes = (R(-1), R(0), R(1, 2), R(1), R(3, 2), R(2))
    imaginary = (R(0), R(1))
    for m in range(1, 7):
        n = max(3, 2*m)
        designs = [[(R(1), R(0))]*n,
                   [(R((-1)**j), R(0)) for j in range(n)],
                   [cpow(imaginary, j) for j in range(n)]]
        modes = all_modes[m]
        for nodes in designs:
            values = traces(nodes, m)
            for y in y_nodes:
                hooks = determinant_hooks(nodes, y, m)
                symbolic = defaultdict(R)
                for r, mode in enumerate(modes):
                    add(symbolic, mode, y**r)
                assert evaluate(clean(symbolic), values) == hooks[m]
                counts['determinant_hook_evaluations'] += 1
                left = evaluate(mixed_wick(clean(symbolic), clean(symbolic)), values)
                right = squared(hooks[m])-m*y**(m-1)
                right -= (1-y)**2*sum((m-k)*y**(m-k-1)*squared(hooks[k]) for k in range(1, m))
                assert left == (right, R(0))
                counts['complete_contraction_evaluations'] += 1

    for m in range(1, 13):
        for y in y_nodes:
            # The geometric sum representation is exact before substituting
            # y=exp(mt/N); this checks both tensor multiplicities and endpoints.
            coefficient_sum = sum(y**(r+s) for r in range(m) for s in range(m))
            assert coefficient_sum == sum(y**r for r in range(m))**2
            assert Counter(r+s for r in range(m) for s in range(m)) == Counter({k: min(k+1, 2*m-1-k) for k in range(2*m-1)})
            counts['finite_spectral_multiplicity_cases'] += 1

    for n in range(5, 66):
        for m in range(1, n//2+1):
            xi = R(m, n)
            # Exact affine exponents before the 4 N Delta error: the
            # uncontracted square has the extra finite-N term xi*t.
            leading = -(R(m)+R(m*(m-1), n))+2*(R(n)*xi/4+R(3*m)*xi/4)
            assert leading == -R(n)*xi*(1-xi)/2+xi
            counts['uncontracted_contour_exponents'] += 1
            for k in range(1, m):
                eta = R(k, n)
                contracted = -(R(m)+R(m*(m-1), n))+xi*(m-k-1)+2*(R(n)*xi/4+R(3*k)*xi/4)
                assert contracted == -R(n)*xi*(1-eta)/2
                assert contracted <= -R(n)*xi*(1-xi)/2
                counts['contracted_contour_exponents'] += 1

    return {
        'schema': 'bgs-pair-heat-formula-check-v1', 'claim_id': 'BGS-FLOW-021',
        'status': 'passed', 'arithmetic': 'exact fractions and rational real/imaginary pairs',
        'python': platform.python_version(), 'randomness_used': False,
        'counts': dict(sorted(counts.items())),
        'bounds': {'hook_degree_max': 8, 'mixed_degree_max': 5,
                   'independent_radial_degree_max': 3, 'point_degree_max': 6,
                   'spectral_multiplicity_degree_max': 12, 'contour_dimension_max': 65},
        'non_claims': ['No asymptotic BGS proof', 'No actual frozen-map Heisenberg trace computation',
                       'No large-N spectral experiment', 'No analytic Lean certificate',
                       'Finite cases do not prove H4 or the limiting spectral measure'],
        'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = run()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS exact Heisenberg pair heat formula controls')
    print(json.dumps(result['counts'], sort_keys=True))


if __name__ == '__main__':
    main()
