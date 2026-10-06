#!/usr/bin/env python3
"""Exact finite controls for husimi_shell_tomography.tex.

Ranks, normalization, Laguerre identities and positive root counts use exact
rational arithmetic. State differences are checked as algebraic 2x2 matrices.
No finite enumeration establishes the infinite-dimensional injectivity theorem.
No output files are written unless --output is explicitly supplied.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import argparse
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import sympy as sp


def laguerre_controls(max_rank: int) -> list[dict]:
    x = sp.Symbol('x')
    rows = []
    for m in range(1, 2*max_rank+1):
        even = [F(comb(m, j), 2**(m-1)) if j % 2 == 0 else F(0) for j in range(m+1)]
        odd = [F(comb(m, j), 2**(m-1)) if j % 2 else F(0) for j in range(m+1)]
        assert sum(even) == sum(odd) == 1
        assert all(a*b == 0 for a, b in zip(even, odd))
        assert sum(abs(a-b) for a, b in zip(even, odd))/2 == 1
        poly = sp.Poly(sum(sp.Rational((a-b).numerator, (a-b).denominator)*x**j/factorial(j)
                           for j, (a, b) in enumerate(zip(even, odd))), x)
        target = sp.Poly(sp.laguerre(m, x)/2**(m-1), x)
        assert poly == target
        assert sp.gcd(poly, poly.diff()).degree() == 0
        assert poly.count_roots(0, sp.oo) == m
        # Integration against exp(-x) equals the trace difference, exactly zero.
        assert sum(poly.nth(j)*factorial(j) for j in range(m+1)) == 0
        positive_rank = sum(a > 0 for a in even)
        negative_rank = sum(a > 0 for a in odd)
        assert positive_rank == m//2+1 and negative_rank == (m+1)//2
        rows.append({'laguerre_degree': m, 'ranks': [positive_rank, negative_rank],
                     'exact_positive_simple_roots': m, 'trace_distance': 1})
    return rows


def energy_controls() -> list[dict]:
    rows = []
    for energy in (F(1, 2), F(1), F(3)):
        for n in (10, 20, 60, 120):
            t = sp.Rational(energy.numerator, energy.denominator*n)
            assert 0 < t < sp.Rational(1, 2)
            c = sp.sqrt(t*(1-t))
            plus = sp.Matrix([[1-t, c], [c, t]])
            minus = sp.Matrix([[1-t, -c], [-c, t]])
            assert plus.trace() == minus.trace() == 1
            assert plus.det() == minus.det() == 0
            assert plus.rank() == minus.rank() == 1
            assert n*plus[1, 1] == sp.Rational(energy.numerator, energy.denominator)
            difference = plus-minus
            assert difference*difference == 4*t*(1-t)*sp.eye(2)
            z, w = sp.symbols('z w')
            vector = sp.Matrix([1, z**n/sp.sqrt(sp.factorial(n))])
            dual = sp.Matrix([[1, w**n/sp.sqrt(sp.factorial(n))]])
            intensity = (dual*difference*vector)[0]
            assert sp.simplify(intensity-2*c*(z**n+w**n)/sp.sqrt(sp.factorial(n))) == 0
            bounds = []
            for radius in (F(1, 2), F(1), F(2)):
                weight = energy/n
                # pi^2 times the square of the uniform data bound.
                error2 = 16*weight*(1-weight)*radius**(2*n)/factorial(n)
                # Exact sufficient conditions for the positive intensity floor.
                floor_verified = 1-weight >= F(9, 16) and weight*radius**(2*n)/factorial(n) <= F(1, 16)
                if n >= 60:
                    assert floor_verified
                bounds.append({'radius': str(radius), 'pi_squared_error_bound_squared': str(error2),
                               'positive_intensity_floor_verified': floor_verified})
            rows.append({'mean_energy': str(energy), 'n': n,
                         'trace_distance_squared': str(F(4)*energy/n*(1-energy/n)),
                         'ranks': [1, 1], 'bounds': bounds})
    return rows


def finite_probe_control() -> dict:
    z = sp.Symbol('z')
    points = (0, 1, sp.I, -1+sp.I)
    f = sp.Poly(sp.prod(z-a for a in points), z)
    g = sp.Poly(z*f.as_expr(), z)
    def inner(a, b):
        return sp.expand(sum(sp.conjugate(a.nth(n))*b.nth(n)*sp.factorial(n)
                             for n in range(max(a.degree(), b.degree())+1)))
    g = sp.Poly(g.as_expr()-inner(f, g)/inner(f, f)*f.as_expr(), z)
    assert inner(f, g) == 0
    assert inner(f, f) > 0 and inner(g, g) > 0
    assert all(f.eval(a) == 0 and sp.simplify(g.eval(a)) == 0 for a in points)
    # Removing a root must destroy the zero-probability conclusion there.
    bad = sp.Poly(sp.prod(z-a for a in points[1:]), z)
    assert bad.eval(0) != 0
    return {'probe_count': len(points), 'orthogonal_states_constructed': 2,
            'largest_fock_occupation': int(max(f.degree(), g.degree())), 'negative_controls': 1}


def main() -> None:
    if not __debug__:
        raise RuntimeError('Do not disable verification assertions')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-rank', type=int, default=12)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if not 1 <= args.max_rank <= 40:
        parser.error('--max-rank must be between 1 and 40')
    laguerre = laguerre_controls(args.max_rank)
    energy = energy_controls()
    data = {'status': 'PASS', 'scope': 'finite exact controls, not proof by enumeration',
            'maximum_rank_parameter': args.max_rank, 'laguerre_families': len(laguerre),
            'positive_root_count_method': 'exact Sturm count and polynomial gcd',
            'energy_state_pairs': len(energy), 'uniform_disk_bound_cases': 3*len(energy),
            'finite_probe_control': finite_probe_control(),
            'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'laguerre_anchors': [laguerre[0], laguerre[-2], laguerre[-1]],
            'energy_anchors': [energy[0], energy[-1]]}
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(data, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(data, indent=2))


if __name__ == '__main__':
    main()
