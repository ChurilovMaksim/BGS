#!/usr/bin/env python3
"""Exact finite controls for multiradius_polynomial_rigidity.md.

The arbitrary-degree theorem is proved in the mathematics note. These tests
check identities and the sharp construction, not a finite enumeration proof.
"""
from __future__ import annotations
import argparse
import itertools
import json
from pathlib import Path
import sympy as sp

def dot(a, b):
    return sum(x*y for x, y in zip(a, b))

def is_flat(coefficients, radius_squared):
    for lag in range(1, len(coefficients)):
        value = sum(dot(coefficients[j], coefficients[j+lag])
                    * radius_squared**j
                    for j in range(len(coefficients)-lag))
        if value != 0:
            return False
    return True

def exhaustive_two_component(max_degree):
    alphabet = list(itertools.product((-1, 0, 1), repeat=2))
    checked = 0
    accepted = 0
    for degree in range(1, max_degree+1):
        for middle in itertools.product(alphabet, repeat=degree-1):
            coefficients = ((1, 0),) + middle + ((0, 1),)
            checked += 1
            if is_flat(coefficients, 1) and is_flat(coefficients, 4):
                accepted += 1
                assert all(v == (0, 0) for v in middle)
    counterexample = ((1, 1), (2, 0), (-1, 1))
    assert is_flat(counterexample, 1)
    assert not is_flat(counterexample, 4)
    return {'coefficient_arrays': checked, 'flat_at_both_radii': accepted,
            'one_radius_counterexample': True}

def sharp_examples():
    x = sp.Symbol('x')
    rows = []
    for dimension in range(2, 8):
        squares = [j*j for j in range(1, dimension)]
        polynomial = sp.Poly(sp.prod(x-a for a in squares), x)
        coefficients = list(reversed(polynomial.all_coeffs()))
        assert len(coefficients) == dimension and all(coefficients)
        # Use an exact positive diagonal metric rather than square roots.
        metric = sp.diag(*[abs(a) for a in coefficients])
        columns = []
        for k in range(dimension+1):
            column = sp.zeros(dimension, 1)
            if k < dimension:
                column[k] = 1
            if k > 0:
                column[k-1] = sp.sign(coefficients[k-1])
            columns.append(column)
        gram = sp.Matrix(dimension+1, dimension+1,
                         lambda i,j:(columns[i].T*metric*columns[j])[0])
        assert gram.rank() == dimension
        for lag in range(2, dimension+1):
            assert all(gram[j,j+lag] == 0
                       for j in range(dimension+1-lag))
        angular = sp.Poly(sum(gram[j,j+1]*x**j
                             for j in range(dimension)), x)
        assert angular == polynomial
        for square in squares:
            assert angular.eval(square) == 0
        assert angular.eval(dimension*dimension) != 0
        rows.append({'coefficient_rank': dimension,
                     'prescribed_radius_squares': squares,
                     'angular_polynomial': str(angular.as_expr()),
                     'exact_cross_gram_rank': int(gram.rank())})
    return rows

def triangular_rank_controls():
    # Deterministic coefficient vectors; no numerical rank threshold.
    checked = 0
    for d in range(1, 5):
        for n in range(1, 10):
            vectors = [sp.Matrix([((i+1)*(j+3)+i*i-j) % 7-3
                                  for i in range(d)]) for j in range(n+1)]
            rank = sp.Matrix.hstack(*vectors).rank()
            last_lag = 0
            for lag in range(1, n+1):
                if any((vectors[j].T*vectors[j+lag])[0]
                       for j in range(n+1-lag)):
                    last_lag = lag
            if not last_lag:
                continue
            positions = [j for j in range(n+1-last_lag)
                         if (vectors[j].T*vectors[j+last_lag])[0] != 0]
            cross = sp.Matrix(len(positions), len(positions),
                              lambda a,b:(vectors[positions[a]].T
                              *vectors[positions[b]+last_lag])[0])
            assert cross.det() != 0
            assert cross.rank() == len(positions) <= rank
            checked += 1
    return checked

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-degree', type=int, default=6)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if not 1 <= args.max_degree <= 7:
        parser.error('--max-degree must be between one and seven')
    result = {'scope':'exact finite controls, not the general theorem',
              'two_component':exhaustive_two_component(args.max_degree),
              'sharp_examples':sharp_examples(),
              'triangular_rank_cases':triangular_rank_controls()}
    text = json.dumps(result, indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding='utf-8')
    print(text, end='')

if __name__ == '__main__':
    main()
