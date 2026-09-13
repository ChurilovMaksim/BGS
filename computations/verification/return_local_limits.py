#!/usr/bin/env python3
"""Exact finite cloud/void controls and floating unfolding diagnostics.

These checks audit constructions and normalizations. They do not certify
weak process limits, ergodicity, or the analytic cat-map return theorem.
"""
from collections import defaultdict
from fractions import Fraction as F
import argparse
import hashlib
import json
import math
from pathlib import Path
import platform
import subprocess

import numpy as np
import sympy as sp


def count_distribution(phases, width):
    """Exact origin-averaged forward-window count law, via an event sweep."""
    assert F(0) < width <= 1
    events = defaultdict(int)
    for p in phases:
        events[(p-width) % 1] += 1
        events[p % 1] -= 1
    cuts = sorted(set(events) | {F(0), F(1)})
    midpoint = (cuts[0]+cuts[1])/2
    count = sum((p-midpoint) % 1 < width for p in phases)
    law = defaultdict(F)
    for i, (left, right) in enumerate(zip(cuts, cuts[1:])):
        if i:
            count += events[left]
        assert 0 <= count <= len(phases)
        law[count] += right-left
    assert sum(law.values()) == 1
    return dict(law)


def brute_count_distribution(phases, width):
    cuts = sorted({F(0), F(1)} | {p % 1 for p in phases}
                  | {(p-width) % 1 for p in phases})
    law = defaultdict(F)
    for left, right in zip(cuts, cuts[1:]):
        midpoint = (left+right)/2
        count = sum((p-midpoint) % 1 < width for p in phases)
        law[count] += right-left
    return dict(law)


def cloud_spectrum(d, k, alpha):
    """Return profile alpha*Haar+(1-alpha)*delta_0, with simple levels."""
    n = int(alpha*d)
    clock = [F(j, n) for j in range(n)]
    clouds = []
    for j in range(d-n):
        # Positive offsets cannot collide with the rational clock for these
        # finite ranges; the explicit distinctness assertion verifies this.
        clouds.append((F(j % k, k)+F(j+1, d**3*(d-n+1))) % 1)
    assert len(set(clock+clouds)) == d
    return clock, clouds


def exact_cloud_controls():
    cases, brute_cases, rows = 0, 0, []
    for d in (24, 60, 180, 480):
        for k in (1, 3, 7):
            for alpha in (F(0), F(1, 3), F(2, 3), F(1)):
                clock, clouds = cloud_spectrum(d, k, alpha)
                for length in (F(1, 2), F(1), F(2)):
                    law = count_distribution(clock+clouds, length/d)
                    assert sum(n*p for n, p in law.items()) == length
                    if d == 24:
                        assert law == brute_count_distribution(clock+clouds, length/d)
                        brute_cases += 1
                    bg_void = max(F(0), 1-F(len(clock), d)*length)
                    cloud_hit_bound = min(F(1), k*(length/d+F(2, d**3))) if clouds else F(0)
                    void = law.get(0, F(0))
                    assert 0 <= bg_void-void <= cloud_hit_bound
                    cases += 1
                    if k == 3 and alpha == F(1, 3) and length == 1:
                        rows.append({'D': d, 'mean_count': str(length),
                                     'void_probability': str(void),
                                     'background_void': str(bg_void),
                                     'cloud_hit_bound': str(cloud_hit_bound)})
    return {'rational_window_cases': cases, 'independent_brute_cases': brute_cases,
            'scope': 'D=24,60,180,480; K=1,3,7; alpha=0,1/3,2/3,1; L=1/2,1,2',
            'intensity_loss_examples': rows}


def cdf(y, amplitude=0.6):
    return y+amplitude*np.sin(2*np.pi*y)/(2*np.pi)


def inverse_cdf(v, amplitude=0.6):
    lo, hi = np.zeros_like(v), np.ones_like(v)
    for _ in range(55):
        mid = (lo+hi)/2
        below = cdf(mid, amplitude) < v
        lo, hi = np.where(below, mid, lo), np.where(below, hi, mid)
    return (lo+hi)/2


def inverse_unfold(phases, k):
    v = k*phases
    return (np.floor(v)+inverse_cdf(v % 1))/k


def unfolding_controls():
    rows = []
    for d, k in ((256, 5), (1024, 11), (4096, 17)):
        original = np.arange(d)/d
        theta = inverse_unfold(original, k)
        recovered = (np.floor(k*theta)+cdf((k*theta) % 1))/k
        residual = float(np.max(abs(recovered-original)))
        assert residual < 3e-14
        moments = []
        for r in range(1, 5):
            moment = np.exp(2j*np.pi*r*k*theta).mean()
            target = 0.3 if r == 1 else 0.
            # Lipschitz Riemann-sum error; this is not an interval certificate.
            bound = 2*np.pi*r*k/(0.4*d)
            assert abs(moment-target) < bound+1e-12
            moments.append({'r': r, 'error': float(abs(moment-target)), 'bound': bound})
        rows.append({'D': d, 'K': k, 'inverse_residual': residual, 'moments': moments})

    # Independent test of the origin Jacobian in (S25): after unfolding a
    # constant-density background alpha, the mean must remain alpha.
    y = np.arange(65536)/65536
    rho = 1+0.6*np.cos(2*np.pi*y)
    correct = float(np.mean(rho*(1/3)/rho))
    omitted_weight = float(np.mean((1/3)/rho))
    assert abs(correct-1/3) < 1e-14
    assert abs(omitted_weight-5/12) < 1e-14
    assert abs(omitted_weight-correct) > 0.08

    # Determinantal kernel normalization of the CUE example, independent of
    # eigenvalue sampling: sinc(s)/sinc(s/D) tends locally to sinc(s).
    kernel_errors = []
    s = np.linspace(-4, 4, 16001)
    for d in (32, 64, 128):
        kernel = np.sinc(s)/np.sinc(s/d)
        error = float(np.max(abs(kernel-np.sinc(s))))
        assert error < 40/d**2
        kernel_errors.append({'D': d, 'sup_error': error})
    return {'clock_transport': rows, 'jacobian_correct_mean': correct,
            'jacobian_omitted_mean': omitted_weight, 'cue_kernel': kernel_errors,
            'arithmetic': 'float64/complex128; tolerances and Riemann bounds, not intervals'}


def gap_controls():
    u = sp.symbols('u', positive=True)
    t = sp.symbols('t', positive=True)
    b = sp.sqrt(t*(4-t))/2+sp.acos(1-t/2)
    # Multiply by sqrt(t*(4-t)) to eliminate branch ambiguity on 0<t<4.
    derivative = sp.simplify(sp.diff(b, t)*sp.sqrt(t*(4-t))-(4-t)/2)
    assert derivative == 0
    # Independent endpoint derivation: g(4-s)=integral_0^s sqrt(u/(4-u))/(2*pi) du.
    leading = sp.limit((sp.sqrt(u/(4-u))/(2*sp.pi))/sp.sqrt(u), u, 0)
    assert sp.simplify(leading*sp.Rational(2, 3)-1/(6*sp.pi)) == 0
    values = []
    for v, reference in ((1, .39100221895577064), (2, .18169011381620933),
                         (3, .05766888562243731)):
        gap = 1-(math.sqrt(v*(4-v))/2+math.acos(1-v/2))/math.pi
        assert abs(gap-reference) < 2e-15
        values.append({'t': v, 'gap_lower_bound': gap})
    return {'symbolic_derivative_zero': True, 'endpoint_coefficient': '1/(6*pi)',
            'wolfram_compared_values': values}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('build/return-local-limits.json'))
    args = parser.parse_args()
    result = {'producer': 'computations/verification/return_local_limits.py',
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'input_commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
              'dirty': bool(subprocess.check_output(['git', 'status', '--porcelain'], text=True)),
              'versions': {'python': platform.python_version(), 'numpy': np.__version__, 'sympy': sp.__version__},
              'exact': exact_cloud_controls(), 'unfolding': unfolding_controls(),
              'free_brownian_gap': gap_controls()}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'exact_cases': result['exact']['rational_window_cases'],
                      'independent_brute_cases': result['exact']['independent_brute_cases'],
                      'scope': 'finite construction controls and separate floating/symbolic diagnostics'}))


if __name__ == '__main__':
    main()
