#!/usr/bin/env python3
"""Exact polynomial diagnostics for the fixed-word/echo extension.

This does not evaluate the transcendental kick strength numerically and
does not infer any asymptotic result from finite-dimensional experiments.
"""
import hashlib
import json
from pathlib import Path
import random
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
x = sp.symbols('x')
S = sp.Matrix([[3, 4], [2, 3]])
E = sp.Matrix([[0, 0], [1, 0]])
T = sp.eye(2) + x*E
assert E**2 == sp.zeros(2)

polynomial_tests = []
for a in range(-12, 13):
    if a:
        A = S**a
        assert A[0, 1] != 0
        assert E*A*E == A[0, 1]*E
for b in range(-8, 9):
    assert T**b == sp.eye(2)+b*x*E

rng = random.Random(9803)
for k in range(1, 7):
    for sample in range(7):
        aa = [rng.choice([-3, -2, -1, 1, 2, 3]) for _ in range(k)]
        bb = [rng.choice([-4, -2, -1, 1, 2, 4]) for _ in range(k)]
        C = sp.eye(2)
        expected = sp.Integer(1)
        for a, b in zip(aa, bb):
            C = (C*(S**a)*(sp.eye(2)+b*x*E)).applyfunc(sp.expand)
            expected *= b*(S**a)[0, 1]
        poly = sp.Poly(sp.trace(C), x)
        assert poly.degree() == k
        assert poly.LC() == expected != 0
        assert all(t.is_Integer for t in poly.all_coeffs())
        polynomial_tests.append({'a': aa, 'b': bb,
                                 'degree': k, 'leading': str(expected)})

echo_tests = []
for m in range(1, 11):
    C = (S**(-m) * (S*T)**m).applyfunc(sp.expand)
    poly = sp.Poly(sp.trace(C), x)
    if m == 1:
        assert C == T and poly.as_expr() == 2
    else:
        expected = 4**(m-1)*(S**(1-m))[0, 1]
        assert poly.degree() == m
        assert poly.LC() == expected != 0
    echo_tests.append({'m': m, 'trace': str(poly.as_expr())})

result = {
    'result': 'PASS: exact finite polynomial diagnostics only',
    'candidate_sha256': hashlib.sha256((ROOT/'fixed_word_freeness.md').read_bytes()).hexdigest(),
    'alternating_words_checked': len(polynomial_tests),
    'degree_range': [1, 6],
    'negative_exponents_included': True,
    'echo_trace_polynomials': echo_tests,
    'caveat': 'All-word nonvanishing and asymptotic claims are proved in the separate audit, not established by finite tests.'
}
print(json.dumps(result, indent=2))
