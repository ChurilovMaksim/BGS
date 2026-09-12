#!/usr/bin/env python3
"""Exact finite Fourier/mark controls and separate Gaussian diagnostics.
No finite check proves ergodicity, weak limits, or cat-map asymptotics.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import platform
import subprocess
import numpy as np

COS, SIN = (1, 0, -1, 0), (0, 1, 0, -1)


def exact_controls():
    identities = marked = 0
    negative_control = None
    for d in range(1, 11):
        for a in range(d+1):
            for b in range(d-a+1):
                for c in range(d-a-b+1):
                    counts = (a, b, c, d-a-b-c)
                    window = (3, 1, 0, 1)
                    z = [sum(counts[j]*window[(j-x) % 4] for j in range(4)) for x in range(4)]
                    for q in (1, 2, 3):
                        tr = (sum(counts[j]*COS[q*j % 4] for j in range(4)),
                              sum(counts[j]*SIN[q*j % 4] for j in range(4)))
                        w = (sum(window[j]*COS[q*j % 4] for j in range(4)),
                             -sum(window[j]*SIN[q*j % 4] for j in range(4)))
                        assert sum(z[x]*COS[q*x % 4] for x in range(4)) == tr[0]*w[0]-tr[1]*w[1]
                        assert sum(z[x]*SIN[q*x % 4] for x in range(4)) == tr[0]*w[1]+tr[1]*w[0]
                        marked += 1
                    for cap in (1, 3, 7):
                        w = {m: F(1, 1+m*m) for m in range(-cap, cap+1)}
                        kernel = [sum(w[m]*COS[m*j % 4] for m in w)/d for j in range(4)]
                        direct = sum((counts[i]*counts[j]-(counts[i] if i == j else 0))
                                     *kernel[(i-j) % 4] for i in range(4) for j in range(4))/d
                        energy = {m: F(sum(counts[j]*COS[m*j % 4] for j in range(4))**2
                                       +sum(counts[j]*SIN[m*j % 4] for j in range(4))**2, d*d) for m in w}
                        diagonal = sum(w.values())/d
                        assert direct == sum(w[m]*energy[m] for m in w)-diagonal
                        assert direct >= w[0]+2*w[1]*energy[1]-diagonal
                        if negative_control is None and direct < w[0]+2*w[1]*energy[1]:
                            negative_control = {'D': d, 'counts': counts, 'pair': str(direct)}
                        identities += 1
    assert negative_control is not None
    return {'rational_pair_identities_and_bounds': identities, 'integer_mark_identities': marked,
            'domain': 'all multiplicity vectors on four quarter-circle sites, D=1..10; caps 1,3,7',
            'omitted_diagonal_counterexample': negative_control}


def winding_cap(d, length):
    return math.ceil(length/d*math.sqrt(math.log(1e15*d)/math.pi))+2


def diagonal_sum(d, length):
    return 1+2*sum(math.exp(-math.pi*(d*j/length)**2) for j in range(1, winding_cap(d, length)+1))


def gaussian_pair(phases, length):
    d = len(phases)
    delta = (phases[:, None]-phases[None, :]+0.5) % 1-0.5
    np.fill_diagonal(delta, np.inf)
    cap = winding_cap(d, length)
    return float(sum(np.exp(-math.pi*(d*(delta+z)/length)**2).sum()/d for z in range(-cap, cap+1)))


def gaussian_trace(phases, length):
    d = len(phases)
    cap = math.ceil(d/length*math.sqrt(math.log(1e15*d)/math.pi))+2
    m = np.arange(1, cap+1)
    tr = np.exp(2j*math.pi*m[:, None]*phases).mean(axis=1)
    return float(length+2*length*np.sum(np.exp(-math.pi*(length*m/d)**2)*abs(tr)**2)-diagonal_sum(d, length))


def cue_gaussian(length):
    return length-math.erf(math.sqrt(math.pi)*length)-math.expm1(-math.pi*length*length)/(math.pi*length)


def numerical_controls():
    rng = np.random.default_rng(20260912)
    rows = []
    for d in (1, 4, 11, 37, 101):
        families = {'clock': np.arange(d)/d, 'coincident': np.zeros(d), 'random': rng.random(d),
                    'two_bands': (rng.integers(0, 2, d)/2+0.015*rng.random(d)) % 1}
        for name, phases in families.items():
            for length in (0.5, 1.0, 3.0, 8.0):
                pair, spectral = gaussian_pair(phases, length), gaussian_trace(phases, length)
                residual = abs(pair-spectral)
                assert residual < 2e-10
                q = max(1, math.isqrt(d))
                energy = abs(np.exp(2j*math.pi*q*phases).mean())**2
                lower = length+2*length*math.exp(-math.pi*(length*q/d)**2)*energy-diagonal_sum(d, length)
                assert pair+2e-10 >= lower
                rows.append({'D': d, 'family': name, 'L': length, 'pair': pair, 'residual': residual, 'lower_bound': lower})
    quadrature = []
    for length in (0.5, 1.0, 3.0, 8.0):
        x = np.linspace(-12*length, 12*length, 100001)
        y = np.exp(-math.pi*(x/length)**2)*(1-np.sinc(x)**2)
        quad = (x[1]-x[0])*(y.sum()-(y[0]+y[-1])/2)
        assert abs(quad-cue_gaussian(length)) < 1e-9
        assert 0 <= cue_gaussian(length)-length+1 <= 1/(math.pi*length)+1e-14
        quadrature.append(float(abs(quad-cue_gaussian(length))))
    density_rows = []
    for n in (16, 32, 64):
        k = 8
        phases = ((np.arange(k)[:, None]+np.arange(n)[None, :]/(2*n))/k).ravel()
        moment = np.exp(2j*math.pi*k*phases).mean()
        assert abs(moment-2/(n*(1-np.exp(1j*math.pi/n)))) < 1e-13
        pair = gaussian_pair(phases, 1.0)
        mixture = 2*sum(math.exp(-math.pi*(j/2)**2) for j in range(1, 30))
        assert abs(pair-mixture) <= 4/n
        density_rows.append({'D': n*k, 'n': n, 'K': k, 'return_modulus': float(abs(moment)),
                             'pair': pair, 'mixture_limit': mixture})
    clock = np.arange(101)/101
    assert len(set((10*np.arange(101) % 101).tolist())) == 101
    assert abs(gaussian_pair(clock, 1)-cue_gaussian(1)) > 0.1
    return {'cases': rows, 'maximum_pair_trace_residual': max(r['residual'] for r in rows),
            'maximum_quadrature_error': max(quadrature), 'half_filled_cells': density_rows,
            'clock_pair': gaussian_pair(clock, 1), 'sine_pair': cue_gaussian(1),
            'scope': 'float64/complex128, analytic Gaussian tail cutoffs; not interval-certified'}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output', type=Path, default=Path('build/return-trace-obstruction.json'))
    args = p.parse_args()
    result = {'producer': 'computations/verification/return_trace_obstruction.py',
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'input_commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
              'python': platform.python_version(), 'numpy': np.__version__,
              'exact': exact_controls(), 'numerical': numerical_controls()}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'exact_pair_checks': result['exact']['rational_pair_identities_and_bounds'],
                      'exact_mark_checks': result['exact']['integer_mark_identities'],
                      'numerical_cases': len(result['numerical']['cases']),
                      'max_residual': result['numerical']['maximum_pair_trace_residual']}))

if __name__ == '__main__':
    main()
