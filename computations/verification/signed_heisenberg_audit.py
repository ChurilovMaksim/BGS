#!/usr/bin/env python3
"""Independent finite controls for TRACE-010; no frozen-map or BGS theorem.

Exact integer/Fraction CUE cycles, cumulants and density constant terms;
SymPy exact Toeplitz determinant; complex128 finite spectral/table checks.
Caps: factorial order <=6, explicit box dimension <=2048, unitary dimension
<=127, density integration N=4; sparse large-index algebra uses N=2^56
and at most 63 moment entries per tuple. No Monte Carlo calibration is substituted
for a CUE law; seeded phases are adversarial finite algebra controls only.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import importlib.util
import itertools
import json
import math
from pathlib import Path
import platform

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]


def module(path, name):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    out = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(out)
    return out


def mobius(partition):
    return math.prod((-1)**(len(b)-1)*math.factorial(len(b)-1)
                     for b in partition)


def polynomial(traces, modes, partitions):
    return sum(mobius(p)*math.prod(traces[sum(modes[j] for j in b)]
                                 for b in p)
               for p in partitions(len(modes)))


def stable_moment(n, modes):
    positive = Counter(j for j in modes if j > 0)
    negative = Counter(-j for j in modes if j < 0)
    degree = max(sum(positive.elements()), sum(negative.elements()))
    if degree > n or 0 in modes:
        raise ValueError('Outside the stated stable nonzero-mode range')
    if positive != negative:
        return 0
    return math.prod(j**v*math.factorial(v) for j, v in positive.items())


def cue_checks(old, support):
    cycles = 0
    for k in range(2, 7):
        for n in (3, 7, 19):
            for positive in itertools.product((1, 2), repeat=k-1):
                modes = positive + (-sum(positive),)
                expected = (-1)**(k-1)*math.factorial(k-1)*max(n-sum(positive), 0)
                assert support.cycle_benchmark(n, modes) == expected
                cycles += 1
    kernels = []
    for n, times in ((8, (1, 2)), (16, (1, 2, 3))):
        for m, j, r, s in itertools.product(times, repeat=4):
            modes = (m, j, -m-j, -r, -s, r+s)
            expected = m*j*(m+j)*(int(m == r and j == s)+int(m == s and j == r))
            actual = old.cue_moment(n, modes)
            assert actual == expected == stable_moment(n, modes)
            kernels.append([n, m, j, r, s, int(actual)])
        for m, j in itertools.product(times, repeat=2):
            assert old.cue_moment(n, (m, j, -m-j)) == 0
            for h in range(1, 2*max(times)+1):
                assert old.cue_moment(n, (m, j, -m-j, h, -h)) == 0
    # Independent determinant-density integration, not a Gaussian sampler.
    density = old.vandermonde_moment(4, (1, 1, -2, -1, -1, 2))
    assert density == 4
    delta_variance = (4*(old.vandermonde_moment(4, (1, -1, 1, -1))-1)
                      +old.vandermonde_moment(4, (2, -2, 2, -2))-4)
    delta_cross = old.vandermonde_moment(4, (1, -1, 2, -2))-2
    assert delta_variance == 8 and delta_cross == 0
    assert old.vandermonde_moment(4, (1, 1, -2, 1, -1)) == 0
    assert old.vandermonde_moment(4, (1, 1, -2, 2, -2)) == 0
    assert density+delta_variance == 12
    # A nonfactorized complex weight checks conjugation and diagonal factors.
    weights = {(1, 1):sp.Integer(1), (1, 2):sp.I,
               (2, 1):2-sp.I, (2, 2):-sp.Rational(1, 2)+sp.I/3}
    n = 8
    c = Counter()
    for (m, j), w in weights.items():
        for h in (m, j, m+j):
            c[h] += w
    kernel_sum = sum(w*sp.conjugate(v)*old.cue_moment(n, (m, j, -m-j, -r, -s, r+s))
                     for (m, j), w in weights.items() for (r, s), v in weights.items())
    formula_sum = sum(m*j*(m+j)*(abs(w)**2+w*sp.conjugate(weights[j, m]))
                      for (m, j), w in weights.items())
    pair_sum = sum(h*h*abs(v)**2 for h, v in c.items())
    assert sp.simplify(kernel_sum-formula_sum) == 0
    exact_variance = sp.simplify((formula_sum+pair_sum)/n**6)
    assert exact_variance > 0
    try:
        stable_moment(3, (1, 1, -2, -1, -1, 2))
    except ValueError:
        pass
    else:
        raise AssertionError('Stable-range gate failed')
    outside = old.cue_moment(3, (1, 1, -2, -1, -1, 2))
    assert outside != 4
    return {'cycle_cases':cycles, 'covariance_cases':len(kernels),
            'covariance_table':kernels, 'density_unscaled_variance_N4':12,
            'complex_weight_variance_N8':str(exact_variance),
            'outside_range_sixth_moment_N3':str(outside)}


def cubic_bound(n, positive):
    a, b, eta = 1/8, 1/4, 1/32
    times = np.arange(math.ceil(a*n), math.floor(b*n)+1)
    window = np.arange(math.ceil(a*n), math.floor(2*b*n)+1)
    delta = np.abs(positive)**2-np.arange(n+1)
    a2 = float(np.sum(np.abs(delta[window]))/n**2)
    m, j = times[:, None], times[None, :]
    cubic = positive[m]*positive[j]*positive[m+j].conjugate()
    error = cubic-delta[m]-delta[j]-delta[m+j]
    a3 = float(np.sum(np.abs(error))/n**3)
    ell = len(times)/n
    rhs = math.sqrt(n)*(a-eta)*math.sqrt(2*a-eta)*ell*max(ell-3*a2/eta, 0)-3*ell*a2
    bad = set(window[np.abs(delta[window]) > eta*n].tolist())
    good = sum(m not in bad and j not in bad and m+j not in bad
               for m, j in itertools.product(times, repeat=2))
    assert good >= max(len(times)**2-3*len(times)*len(bad), 0)
    assert a3 >= rhs-2e-11
    return {'N':n, 'A2':a2, 'A3':a3, 'finite_lower_bound':rhs,
            'good_pairs':good, 'bad_times':len(bad)}


def finite_bounds(old):
    rng = np.random.default_rng(20260930)
    rows = []
    for n in (32, 64, 128):
        times = np.arange(n+1)
        trace = np.sqrt(times)*np.exp(2j*np.pi*rng.random(n+1))
        trace[0] = n
        rows.append({'role':'formal table with exact pair amplitudes', **cubic_bound(n, trace)})
        trace = trace.copy()
        trace[::11] *= 1.2
        trace[0] = n
        rows.append({'role':'formal table with sparse amplitude defects', **cubic_bound(n, trace)})
    for n in (29, 61, 127):
        for phases, name in ((np.arange(n)/n, 'unitary clock'),
                             (rng.random(n), 'unitary seeded spectral control')):
            trace = np.exp(2j*np.pi*np.outer(np.arange(n+1), phases)).sum(axis=1)
            rows.append({'role':name, **cubic_bound(n, trace)})
    direct_cases = 0
    for n in (7, 11, 17):
        phases = rng.random(n)
        traces = {h:np.exp(2j*np.pi*h*phases).sum() for h in range(-4, 5)}
        for m, j in itertools.product((1, 2), repeat=2):
            direct = sum(np.exp(2j*np.pi*(m*phases[x]+j*phases[y]-(m+j)*phases[z]))
                         for x,y,z in itertools.permutations(range(n), 3))
            formula = polynomial(traces, (m,j,-m-j), old.partitions)
            assert abs(direct-formula) < 2e-10
            direct_cases += 1
    # All-order finite triangle budget on a formal table, not a realized spectrum.
    general = []
    for k in range(3, 7):
        n, a, b, eta = 64, 1/32, 1/16, 1/64
        q = k-1
        I = tuple(range(math.ceil(a*n), math.floor(b*n)+1))
        traces = {0:complex(n)}
        for h in range(1, n+1):
            traces[h] = math.sqrt(h)*np.exp(2j*np.pi*((h*h)%n)/n)
            traces[-h] = traces[h].conjugate()
        total = 0.
        for positive in itertools.product(I, repeat=q):
            s = sum(positive)
            value = polynomial(traces, positive+(-s,), old.partitions)
            total += abs(value-(-1)**q*math.factorial(q)*(n-s))
        leading = (a-eta)**(q/2)*math.sqrt(q*a-eta)
        constant = 2*math.factorial(q)+sum(
            abs(mobius(p))*(q*b+eta)**(len(p)/2)
            for p in old.partitions(k) if 2 <= len(p) <= k-1)
        finite_rhs = (len(I)/n)**q*max(leading-constant/math.sqrt(n), 0)*n**(k/2-1)
        assert total/n**k >= finite_rhs-2e-11
        general.append({'k':k, 'tuples':len(I)**q, 'absolute_discrepancy':total/n**k,
                        'finite_lower_bound':finite_rhs})
    # The conservative box bound above may be zero at small N. Check a
    # strictly positive pointwise budget at large indices without allocating
    # a large spectrum/table. These are algebra controls, not unitary spectra.
    large = []
    for k in range(3, 7):
        n, a, b, eta = 2**56, 1/32, 1/16, 1/64
        q = k-1
        for positive in ((int(a*n),)*q, (int(b*n),)*q,
                         tuple(int((a+(b-a)*j/max(q-1,1))*n) for j in range(q))):
            modes = positive+(-sum(positive),)
            needed = {sum(modes[j] for j in block)
                      for p in old.partitions(k) for block in p}
            traces = {h:(complex(n) if h == 0 else math.sqrt(abs(h))*np.exp(
                (1 if h > 0 else -1)*2j*np.pi*((h*h)%n)/n)) for h in needed}
            value = polynomial(traces, modes, old.partitions)
            reference = (-1)**q*math.factorial(q)*(n-sum(positive))
            leading = (a-eta)**(q/2)*math.sqrt(q*a-eta)
            constant = 2*math.factorial(q)+sum(
                abs(mobius(p))*(q*b+eta)**(len(p)/2)
                for p in old.partitions(k) if 2 <= len(p) <= k-1)
            rhs = leading-constant/math.sqrt(n)
            assert rhs > 0
            actual = abs(value-reference)/n**(k/2)
            assert actual >= rhs-2e-10
            large.append({'k':k,'N':n,'positive_modes':list(positive),
                          'scaled_error':actual,'strictly_positive_bound':rhs,
                          'moment_entries':len(needed)})
    return {'cubic_cases':rows, 'direct_distinct_label_cases':direct_cases,
            'higher_order_cases':general,'large_index_atomic_cases':large}


def phase_checks():
    coefficient = []
    for q in range(1, 11):
        total = sum(math.comb(q-1,h-1)*math.factorial(h-1)*math.factorial(q-h)
                    for h in range(1, q+1))
        assert total == math.factorial(q)
        coefficient.append([q, total])
    z = -sp.Rational(1, 2)+sp.I*sp.sqrt(3)/2
    t = [sp.Integer(3), z, sp.sqrt(2)*z, sp.sqrt(3)]
    moment = sp.Matrix(4, 4, lambda j,k:t[j-k] if j >= k else sp.conjugate(t[k-j]))
    determinant = sp.simplify(sp.expand_complex(moment.det()))
    assert sp.simplify(determinant+5+6*sp.sqrt(2)+6*sp.sqrt(6)) == 0
    assert float(determinant) < 0
    rows = []
    for n in (64, 128, 256, 512, 1024, 2048):
        I = np.arange((n+7)//8, n//4+1)
        m, j = I[:, None], I[None, :]
        amplitude = np.sqrt((m*j*(m+j)).astype(float))
        phase = np.exp(-4j*np.pi*((m*j)%n)/n)
        x = (I/n-3/16)/(1/16)
        bump = np.zeros(len(I))
        interior = np.abs(x) < 1
        bump[interior] = np.exp(-1/(1-x[interior]**2))
        smooth = np.sum(bump[:, None]*bump[None, :]*amplitude*phase)/n**3
        hard = np.sum(amplitude*phase)/n**3
        absolute = float(np.sum(amplitude)/n**3)
        assert absolute/math.sqrt(n) >= 1/1024-1e-12
        rows.append({'N':n, 'absolute_over_sqrt_N':absolute/math.sqrt(n),
                     'hard_signed_real_imag':[float(hard.real),float(hard.imag)],
                     'smooth_signed_real_imag':[float(smooth.real),float(smooth.imag)]})
    return {'two_block_coefficients':coefficient, 'toeplitz_N3_determinant':str(determinant),
            'quadratic_phase_controls':rows,
            'scope':'Formal table; negative N=3 moment determinant forbids claiming a unitary construction.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    old = module('supplement/fixed_map/report-audit/verify.py', 'bgs_cue_reference')
    support = module('computations/verification/heisenberg_note_audit.py', 'bgs_cycle_reference')
    sources = ['mathematics/trace-bridge/signed_heisenberg_comparison.md',
               'computations/verification/signed_heisenberg_audit.py',
               'supplement/fixed_map/report-audit/verify.py',
               'computations/verification/heisenberg_note_audit.py']
    data = {'schema':'bgs-signed-heisenberg-audit-v1', 'status':'PASS',
            'arithmetic':['integer/Fraction CUE algebra','exact SymPy radical determinant','complex128'],
            'runtime':{'python':platform.python_version(),'numpy':np.__version__,'sympy':sp.__version__},
            'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources},
            'cue':cue_checks(old, support), 'bounds':finite_bounds(old), 'phase':phase_checks(),
            'non_claims':['asymptotic proof by computation','frozen-map signed cancellation',
                          'unitary realization of the formal table','BGS solution','external priority']}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, indent=2)+'\n')
    print('PASS signed Heisenberg audit:',data['cue']['cycle_cases'],'cycle cases,',
          data['cue']['covariance_cases'],'exact covariance cases; bounds and failed-realization control')


if __name__ == '__main__':
    main()
