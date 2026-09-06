#!/usr/bin/env python3
"""Finite checks for holomorphic_shell_rigidity.tex; not an analytic proof.

Determinants and jet coefficients use exact rational arithmetic. A separate
mpmath diagnostic checks the punctured-domain theta example numerically.
No files are changed unless --output is given. Do not execute with python -O.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from itertools import permutations
from math import factorial
from pathlib import Path
import hashlib
import json
import random
import sympy as sp


def falling(n: int, k: int) -> int:
    if k > n:
        return 0
    return factorial(n) // factorial(n-k)


def det_fraction(matrix: list[list[F]]) -> F:
    """Gaussian elimination with exact rational pivots."""
    n = len(matrix)
    a = [[F(x) for x in row] for row in matrix]
    result = F(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return F(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            result = -result
        result *= a[j][j]
        for i in range(j+1, n):
            scale = a[i][j] / a[j][j]
            for k in range(j+1, n):
                a[i][k] -= scale*a[j][k]
    return result


def confluent(nodes: list[F], multiplicities: list[int], orders: list[int]):
    return [[F(falling(n, k))*c**(n-k) for n in orders]
            for c, m in zip(nodes, multiplicities) for k in range(m)]


def multiply(a: list[F], b: list[F], cutoff: int) -> list[F]:
    out = [F(0)]*(cutoff+1)
    for j, x in enumerate(a):
        if not x:
            continue
        for k, y in enumerate(b[:cutoff-j+1]):
            if y:
                out[j+k] += x*y
    return out


def det_series(a: list[list[list[F]]], cutoff: int) -> list[F]:
    """Leibniz determinant over a truncated exact power-series ring."""
    n = len(a)
    out = [F(0)]*(cutoff+1)
    for p in permutations(range(n)):
        inv = sum(p[i] > p[j] for i in range(n) for j in range(i+1, n))
        term = [F((-1)**inv)]+[F(0)]*cutoff
        for i in range(n):
            term = multiply(term, a[i][p[i]], cutoff)
        out = [x+y for x, y in zip(out, term)]
    return out


def partition(r: int, rng: random.Random) -> list[int]:
    blocks = []
    while r:
        m = rng.randint(1, r)
        blocks.append(m)
        r -= m
    return blocks


def exact_checks(seed: int, cases: int) -> dict:
    rng = random.Random(seed)
    checked = 0
    jet_checked = 0
    for _ in range(cases):
        r = rng.randint(1, 8)
        mult = partition(r, rng)
        nodes = [F(n, 7) for n in sorted(rng.sample(range(1, 41), len(mult)))]
        orders = sorted(rng.sample(range(0, 31), r))
        matrix = confluent(nodes, mult, orders)
        d1 = det_fraction(matrix)
        d2 = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row]
                        for row in matrix]).det(method='domain-ge')
        assert d1 != 0 and d1 == F(int(sp.numer(d2)), int(sp.denom(d2)))
        checked += 1
    # Full determinants of jets of f_j(w)=a_j*w^n_j*exp(beta_j*w).
    # The determinant implementation here is distinct from pivot elimination.
    for _ in range(max(12, cases//12)):
        r = rng.randint(1, 4)
        mult = partition(r, rng)
        nodes = [F(n, 5) for n in sorted(rng.sample(range(1, 11), len(mult)))]
        orders = sorted(rng.sample(range(0, 7), r))
        amplitudes = [F(rng.choice([-3, -2, -1, 1, 2, 3])) for _ in orders]
        beta = [F(rng.randint(-3, 3)) for _ in orders]
        total = sum(orders)
        cutoff = total+1
        matrix = []
        for c, m in zip(nodes, mult):
            for k in range(m):
                row = []
                for n0, amp, b in zip(orders, amplitudes, beta):
                    coeff = [F(0)]*(cutoff+1)
                    for n in range(max(n0, k), cutoff+1):
                        coeff[n] = amp*b**(n-n0)/factorial(n-n0)*falling(n, k)*c**(n-k)
                    row.append(coeff)
                matrix.append(row)
        series = det_series(matrix, cutoff)
        leading = det_fraction(confluent(nodes, mult, orders))
        for amp in amplitudes:
            leading *= amp
        assert all(x == 0 for x in series[:total])
        assert series[total] == leading != 0
        jet_checked += 1
    x, t = sp.symbols('x t')
    sharp = 0
    for d in range(1, 9):
        for _ in range(8):
            mult = partition(2*d-1, rng)
            radii = sorted(rng.sample(range(1, 33), len(mult)))
            b = sp.Poly(sp.prod((x-rho*rho)**m for rho, m in zip(radii, mult)), x)
            coeffs = [b.nth(j) for j in range(2*d)]
            assert sum(bool(v > 0) for v in coeffs) == d
            assert sum(bool(v < 0) for v in coeffs) == d
            radial = b.as_expr().subs(x, t*t)
            for rho, m in zip(radii, mult):
                assert all(sp.diff(radial, t, k).subs(t, rho) == 0 for k in range(m))
                assert sp.diff(radial, t, m).subs(t, rho) != 0
            sharp += 1
    # Inadmissible nodes and uncounted centre: these must not pass as positive,
    # distinct radial conditions of the theorem.
    assert det_fraction(confluent([F(1), F(1)], [1, 1], [0, 1])) == 0
    assert det_fraction(confluent([F(-1), F(1)], [1, 1], [0, 2])) == 0
    assert det_fraction(confluent([F(0)], [1], [1])) == 0
    assert det_fraction(confluent([F(1), F(2)], [1, 1], [0, 0])) == 0
    return {'confluent_determinants': checked, 'two_exact_determinant_algorithms': True,
            'nonpolynomial_leading_jet_determinants': jet_checked,
            'sharp_mixed_shell_multiplicity_examples': sharp, 'negative_controls': 4}


def theta_checks() -> dict:
    import mpmath as mp
    mp.mp.dps = 85
    q = mp.mpf(1)/4
    def theta(z):
        value = mp.mpc(1)
        for j in range(190):
            value *= (1-q**j*z)*(1-q**(j+1)/z)
        return value
    a, b, c, d = mp.mpf(2), mp.mpf(3), mp.mpf(5), mp.mpf(6)/5
    def p(z):
        return theta(a*z)*theta(b*z)*theta(c/z)*theta(d/z)
    def qq(z):
        return p(1/z)
    errors = []
    recurrence_errors = []
    for n in range(-6, 7):
        for j in range(1, 10):
            z = q**(mp.mpf(n)/2)*mp.exp(2j*mp.pi*j/11)
            pz, qz = p(z), qq(z)
            lhs, rhs = abs(pz)**2, abs(qz)**2
            errors.append(abs(lhs-rhs)/max(mp.mpf(1), lhs, rhs))
            target = q**(-2)*z**(-4)*pz
            recurrence_errors.append(abs(p(q*z)-target)/max(mp.mpf(1), abs(target)))
    assert max(errors) < mp.mpf('1e-65')
    assert max(recurrence_errors) < mp.mpf('1e-65')
    # One zero of P that is not a zero of Q, checked independently of the ratio.
    z0 = mp.mpf(1)/3
    assert abs(p(z0)) < mp.mpf('1e-65') and abs(qq(z0)) > mp.mpf('1e-10')
    return {'scope': 'high-precision numerical diagnostic, not an exact certificate',
            'decimal_precision': 85, 'product_terms': 190, 'shell_angle_pairs': len(errors),
            'max_relative_intensity_residual': mp.nstr(max(errors), 12),
            'max_relative_functional_equation_residual': mp.nstr(max(recurrence_errors), 12),
            'nonproportionality_control_abs_Q_at_one_third': mp.nstr(abs(qq(z0)), 15)}


def main() -> None:
    if not __debug__:
        raise RuntimeError('Verification requires assertions; do not use python -O')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cases', type=int, default=120)
    parser.add_argument('--seed', type=int, default=20260906)
    parser.add_argument('--skip-theta', action='store_true')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.cases < 1:
        parser.error('--cases must be positive')
    data = {'status': 'PASS', 'scope': 'finite regression; universal proof is in the manuscript',
            'seed': args.seed, 'exact': exact_checks(args.seed, args.cases),
            'numerical': None if args.skip_theta else theta_checks(),
            'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(data, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(data, indent=2))


if __name__ == '__main__':
    main()
