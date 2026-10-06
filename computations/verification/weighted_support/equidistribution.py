"""Exact finite checks supporting (not proving) the weighted-periodic audit.

Scope: reconstruct the literal symbol's finite Fourier coefficients with
rational complex arithmetic; verify the derivative-budget coefficient.
No orbit sampling, pressure approximation or asymptotic claim is made.
"""
from fractions import Fraction as F
import json
ZERO = (F(0), F(0))

def addc(a, b):
    return (a[0] + b[0], a[1] + b[1])

def mulc(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])

def add(*args):
    out = {}
    for a in args:
        for k, v in a.items():
            out[k] = addc(out.get(k, ZERO), v)
    return {k: v for k, v in out.items() if v != ZERO}

def scale(a, s):
    return {k: (v[0] * s, v[1] * s) for k, v in a.items()}

def product(a, b):
    out = {}
    for (k, l), v in a.items():
        for (j, h), w in b.items():
            key = (k + j, l + h)
            out[key] = addc(out.get(key, ZERO), mulc(v, w))
    return {k: v for k, v in out.items() if v != ZERO}

def cosq(k):
    return {(k, 0): (F(1, 2), F(0)), (-k, 0): (F(1, 2), F(0))}

def run():
    one = {(0, 0): (F(1), F(0))}
    r = product(add(one, scale(cosq(7), -1)), add(one, cosq(1)))
    rs = {k: (v[0] * (-1 if k[0] % 2 else 1), v[1] * (-1 if k[0] % 2 else 1)) for k, v in r.items()}
    sinq = {(1, 0): (F(0), F(-1, 2)), (-1, 0): (F(0), F(1, 2))}
    cospalpha = {(0, 1): (F(-3, 10), F(-2, 5)), (0, -1): (F(-3, 10), F(2, 5))}
    g = add(cosq(7), scale(r, F(1, 10)), scale(product(r, sinq), F(1, 100)), scale(product(rs, cospalpha), F(1, 100)), scale(one, F(-1, 10)))
    budget = sum(((abs(v[0]) + abs(v[1])) * (k * k + l * l) for (k, l), v in g.items()))
    if not budget == F(51451, 1000):
        raise RuntimeError('Exact check failed at original line 38')
    if not (len(g) == 32 and (0, 0) not in g):
        raise RuntimeError('Exact check failed at original line 39')
    if not all((k * k + l * l < 100 for k, l in g)):
        raise RuntimeError('Exact check failed at original line 40')
    if not all((g[-k, -l] == (v[0], -v[1]) for (k, l), v in g.items())):
        raise RuntimeError('Exact check failed at original line 41')
    pi_upper = F(22, 7)
    checks = {'vector_field': 2 * pi_upper * 52 < 400, 'first_derivative': (2 * pi_upper) ** 2 * 52 < 3000, 'second_derivative': (2 * pi_upper) ** 3 * 10 * 52 < 200000}
    if not all(checks.values()):
        raise RuntimeError('Exact check failed at original line 47')
    return {'status': 'PASS', 'arithmetic': 'exact rational complex coefficients', 'modes': len(g), 'weighted_coefficient_sum': str(budget), 'derivative_budget_checks': checks, 'scope': 'Finite literal-symbol assembly only; no asymptotic theorem verified by computation.'}
