#!/usr/bin/env python3
"""Finite controls for TRACE-011; no actual-map density or BGS estimate.

Exact integer/Fraction clock moments, SymPy interpolation, complex128
Fourier identities/Holder/counterterms and simple-spectrum perturbations.
Caps: explicit spectra <=194481 phases for occupancy counts, <=81 for
direct moment/positivity checks; Fourier controls <=127 phases, >=8N
FFT cells; resonant Riemann grids <=1160^2. No Monte Carlo calibration.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import platform
from collections import Counter
from itertools import product

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
A, B = 1/8, 1/4


def bump(x):
    u = (2*np.asarray(x)-A-B)/(B-A)
    z = np.maximum(1-u*u, 0)
    out = np.zeros_like(z, dtype=float)
    np.exp(-1/np.maximum(z, 1e-300), out=out, where=z > 0)
    return out


def interpolation():
    s = sp.Symbol('s')
    theta = 2*(s-3)/(s-2)
    assert sp.simplify(1-2/s-theta/2-(1-theta)/s) == 0
    assert sp.simplify((3-theta)/s-1/(s-2)) == 0
    k = sp.Symbol('k')
    th = 2*(s-k)/(s-2)
    assert sp.simplify(1-(k-1)/s-th/2-(1-th)/s) == 0
    assert sp.simplify((k-th)/s-(k-2)/(s-2)) == 0
    return {'cubic_theta':str(theta),
            'exponents':[[str(t),str((t-3)/(t-2)),str(1/(t-2))]
                         for t in map(sp.Rational, ['10/3','7/2','4'])],
            'general_raw_order_interpolation_checked':True}


def cue_background_controls():
    path = ROOT/'supplement/fixed_map/report-audit/verify.py'
    spec = importlib.util.spec_from_file_location('bgs_density_cue',path)
    old = importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
    cumulant_cases = 0
    max_ratio = Fraction(0)
    for h in (2,3,4,7):
        for m,j in product(range(1,2*h+1),repeat=2):
            cumulant = old.cue_cumulant(h,(m,-m,j,-j))
            covariance = old.cue_moment(h,(m,-m,j,-j))-min(m,h)*min(j,h)
            assert covariance == int(m == j)*min(m,h)**2+cumulant
            assert abs(cumulant) <= 26*h
            max_ratio = max(max_ratio,abs(cumulant)/h)
            cumulant_cases += 1
    assert sum(math.factorial(j-1)*int(sp.functions.combinatorial.numbers.stirling(4,j,
                        kind=2)) for j in range(1,5)) == 26
    assert int(sp.bell(3)) == 5 and int(sp.bell(6)) == 203

    # Independent CUE determinant-density constant term: H=4, arbitrary
    # one-point cluster h_m=1, modes (1,1,-2). This verifies all seven
    # V-containing expansion pieces without a Gaussian sampler.
    terms = [((1,1,-2),1),((1,-2),2),((-2,),1),((1,1),1),((1,),2)]
    variance = sum(c*d*old.vandermonde_moment(4,tuple(sorted(a+tuple(-v for v in b))))
                   for a,c in terms for b,d in terms)
    assert variance == 20
    stable_cases = 0
    mixed_rows = []
    for n,h,d,K,I in ((16,12,2,4,(2,3)),(24,18,3,6,(3,4)),
                      (81,72,3,9,(11,12,13,14))):
        assert 4*max(I) <= h
        # Generic rational weights, including asymmetry and signs.
        W = {(m,j):Fraction(2*m-j,7) for m,j in product(I,repeat=2)}
        one = []
        for position in range(3):
            pieces = []
            for (m,j),w in W.items():
                modes = (m,j,-m-j)
                if modes[position]%d == 0:
                    pieces.append((tuple(v for k,v in enumerate(modes) if k != position),K*w))
            actual = Fraction(0)
            gaussian = Fraction(0)
            for (a,c),(b,e) in product(pieces,repeat=2):
                modes = tuple(sorted(a+tuple(-v for v in b)))
                positive = Counter(v for v in modes if v > 0)
                negative = Counter(-v for v in modes if v < 0)
                expected = (math.prod(v**t*math.factorial(t) for v,t in positive.items())
                            if positive == negative else 0)
                found = old.cue_moment(h,modes)
                assert found == expected
                actual += c*e*found;gaussian += c*e*expected;stable_cases += 1
            assert actual == gaussian >= 0
            one.append(str(actual/Fraction(n**6)))
        # Group the two-cluster pieces into a linear Fourier sum; account
        # for the two positive-frequency pieces before taking the square.
        groups = Counter()
        for (m,j),w in W.items():
            modes = (m,j,-m-j)
            for remaining in range(3):
                others = [v for k,v in enumerate(modes) if k != remaining]
                if all(v%d == 0 for v in others):
                    groups[modes[remaining]] += K*K*w
        linear_variance = sum(c*c*min(abs(v),h) for v,c in groups.items())/n**6
        exact_linear = sum(c*e*old.cue_moment(h,(v,-u))
                           for v,c in groups.items() for u,e in groups.items())/n**6
        assert linear_variance == exact_linear >= 0
        mixed_rows.append({'N':n,'H':h,'d':d,'one_cluster_variances':one,
                           'two_cluster_combined_variance':str(linear_variance)})
    return {'all_band_pair_covariance_cases':cumulant_cases,
            'max_abs_kappa4_over_H':str(max_ratio),'safe_kappa4_constant':26,
            'Bell_third_sixth':[5,203],'independent_density_shifted_cubic_variance_H4':20,
            'stable_mixed_moment_cases':stable_cases,'mixed_variances':mixed_rows,
            'scope':'Exact CUE reference algebra, not Monte Carlo and not actual-map estimates.'}


def exact_occupancy(q, d):
    n, coherent = d*q**3, d*q
    clock = n-coherent
    occ = np.zeros(n, dtype=np.int64)
    # Rational phase positions and integer division avoid bin-edge roundoff.
    np.add.at(occ, np.arange(clock, dtype=np.int64)*n//clock, 1)
    np.add.at(occ, np.arange(d, dtype=np.int64)*n//d, q)
    assert int(occ.sum()) == n
    assert int(occ.max()) <= q+2
    third = sum(int(v)**3 for v in occ)
    fourth = sum(int(v)**4 for v in occ)
    tail = sum(int(v)**3 for v in occ if v > q/2)
    return occ, Fraction(third,n), Fraction(fourth,n), Fraction(tail,n)


def cluster_controls():
    rows = []
    fine = np.linspace(A, B, 32769)
    integral = float(np.trapezoid(bump(fine),fine))**2
    for q in (3,5,9,13,21):
        d, n, coherent = q, q**4, q*q
        lo, hi = math.ceil(A*n), math.floor(2*B*n)
        count = hi//d-(lo-1)//d
        energy = Fraction(count*coherent**2,n*n)
        _, m3, m4, tail = exact_occupancy(q,d)
        resonant = np.arange(math.ceil(A*n/d),math.floor(B*n/d)+1)*d
        mesh = d/n
        raw = float((mesh*bump(resonant/n).sum())**2)
        assert coherent**3 == n*d*d
        assert Fraction(coherent**2,n*d) == Fraction(1,q)
        assert m3 < 8 and m4 >= q and energy <= Fraction(1,q)
        rows.append({'q':q,'d':d,'N':n,'E':str(energy),'M3':str(m3),
                     'M4':str(m4),'third_tail_above_q_over_2':str(tail),
                     'signed_smooth_cluster':raw,'smooth_integral':integral})
    assert abs(rows[-1]['signed_smooth_cluster']-integral) < 1e-10
    return rows


def trace(phases, top):
    return np.exp(2j*np.pi*np.outer(np.arange(top+1),phases)).sum(axis=1)


def realized_moments():
    rows = []
    for q,d in ((2,2),(2,3),(3,3)):
        n, coherent = d*q**3, d*q
        clock = n-coherent
        phases = np.r_[np.arange(clock)/clock,np.repeat(np.arange(d)/d,q)]
        top = math.floor(n/2)
        t = trace(phases,top)
        expected = coherent*(np.arange(top+1)%d == 0)
        expected[0] = n
        assert np.max(np.abs(t-expected)) < 5e-11
        # Moment positivity independent of the integer roots-of-unity sum.
        order = min(9,top+1)
        ix = np.arange(order)
        dif = ix[:,None]-ix[None,:]
        toeplitz = t[np.abs(dif)].copy()
        toeplitz[dif < 0] = toeplitz[dif < 0].conjugate()
        minimum = float(np.linalg.eigvalsh(toeplitz)[0])
        assert minimum >= -2e-10
        perturbed = (phases+np.arange(1,n+1)/n**6)%1
        assert len(np.unique(perturbed)) == n
        tp = trace(perturbed,top)
        trace_error = float(np.max(np.abs(tp-t)))
        rigorous_trace_budget = 2*np.pi*top*n*(n+1)/(2*n**6)
        assert trace_error <= rigorous_trace_budget+5e-11
        rows.append({'N':n,'Toeplitz_min_eigenvalue':minimum,
                     'simple_perturbation_trace_error':trace_error,
                     'trace_error_budget':rigorous_trace_budget})
    return rows


def factor_controls():
    rng = np.random.default_rng(20261001)
    rows = []
    for n in (17,31,81,127):
        spectra = [('clock',np.arange(n)/n),('seeded_adversarial',rng.random(n))]
        if n == 81:
            spectra.append(('critical_cluster',np.r_[np.arange(72)/72,
                                  np.repeat(np.arange(3)/3,3)]))
        for name,phases in spectra:
            t = trace(phases,n)
            I = np.arange(math.ceil(A*n),math.floor(B*n)+1)
            J = np.arange(math.ceil(A*n),math.floor(2*B*n)+1)
            m,j = I[:,None],I[None,:]
            w1 = bump(I/n)*np.exp(2j*np.pi*I/n)
            w2 = bump(I/n)*(1+.3j*I/n)
            w3 = np.zeros(n+1,dtype=complex)
            w3[J] = np.exp(-J/n)*(1-.2j*J/n)
            weight = w1[:,None]*w2[None,:]*w3[m+j].conjugate()
            cubic = t[m]*t[j]*t[m+j].conjugate()
            # Grid has no alias for the integral of these three polynomials.
            grid = 1 << math.ceil(math.log2(8*n))
            coeff = []
            for mode,weights in ((I,w1),(I,w2),(J,w3[J])):
                c = np.zeros(grid,dtype=complex)
                c[mode] = weights*t[mode]/n
                coeff.append(c)
            for d in (1,2,3,7):
                projected = []
                ordinary = []
                for c in coeff:
                    cp = c.copy();cp[np.arange(grid)%d != 0] = 0
                    ordinary.append(np.fft.ifft(c)*grid)
                    projected.append(np.fft.ifft(cp)*grid)
                masks = [np.broadcast_to(m%d == 0,cubic.shape),
                         np.broadcast_to(j%d == 0,cubic.shape),(m+j)%d == 0]
                union = masks[0]|masks[1]|masks[2]
                both = masks[0]&masks[1]
                exact_union = (masks[0].astype(int)+masks[1].astype(int)
                               +masks[2].astype(int)-2*both.astype(int))
                assert np.array_equal(exact_union,union.astype(int))
                integrals = []
                bounds = []
                for h in range(3):
                    f = [projected[k] if k == h else ordinary[k] for k in range(3)]
                    integral = np.mean(f[0]*f[1]*f[2].conjugate())
                    direct = np.sum(weight*cubic*masks[h])/n**3
                    assert abs(integral-direct) < 3e-12
                    norms = [float(np.mean(abs(z)**(2 if k == h else 4))**
                                   (1/(2 if k == h else 4))) for k,z in enumerate(f)]
                    holder = math.prod(norms)
                    assert abs(integral) <= holder+3e-12
                    for s in (10/3,3.5,4):
                        theta = 2*(s-3)/(s-2)
                        rr = s/(s-2)
                        left = np.mean(abs(f[h])**rr)**(1/rr)
                        right = (np.mean(abs(f[h])**2)**(theta/2)
                                 *np.mean(abs(f[h])**s)**((1-theta)/s))
                        assert left <= right+2e-12
                    integrals.append(integral);bounds.append(holder)
                intersection = np.mean(projected[0]*projected[1]*ordinary[2].conjugate())
                z = np.sum(weight*cubic*union)/n**3
                assert abs(z-(sum(integrals)-2*intersection)) < 3e-12
                E = float(np.sum(abs(t[J[J%d == 0]])**2)/n**2)
                Q = float(np.sum(abs(t[J])**2)/n**2)
                ell = len(I)/n
                counter = -abs(t[m])**2-abs(t[j])**2-abs(t[m+j])**2+2*(m+j)
                delta = np.sum(weight*(cubic+counter)*union)/n**3
                budget = (np.max(abs(weight))*(3*ell*E+6*(ell/d+1/n)*Q
                                              +12*B*ell*(ell/d+1/n)))
                assert abs(delta-z) <= budget+3e-12
                rows.append({'N':n,'spectrum':name,'d':d,'E':E,'Q':Q,
                             'union_real_imag':[float(z.real),float(z.imag)],
                             'strip_Holder_bounds':bounds,
                             'counterterm_size':float(abs(delta-z)),
                             'counterterm_budget':float(budget)})
    return rows


def critical_family_exact_boxes():
    # The hard box gives a separate exact rational representation. Smoothness
    # is not used here to infer the theorem for arbitrary weights.
    rows = []
    for q in (3,5,9,13,21):
        d,n,K = q,q**4,q*q
        I = range(math.ceil(A*n),math.floor(B*n)+1)
        l = len(I)
        nr = sum(m%d == 0 for m in I)
        both = nr*nr
        # O(N^2) enumeration is deliberately capped at q=5; thereafter use
        # only exact cluster contribution and energy, not a full box scan.
        raw = Fraction(both*K**3,n**3)
        row = {'N':n,'hard_raw':str(raw),'limit':str(Fraction(1,64))}
        if q <= 5:
            pair = 0;ref = 0;size = 0
            for m in I:
                for j in I:
                    if m%d == 0 or j%d == 0 or (m+j)%d == 0:
                        pair += K*K*((m%d == 0)+(j%d == 0)+((m+j)%d == 0))
                        ref += 2*(m+j);size += 1
            row.update({'factorial_discrepancy':str(raw+Fraction(ref-pair,n**3)),
                        'union_size':size})
        rows.append(row)
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    sources = ['mathematics/trace-bridge/resonant_cubic_density_control.md',
               'computations/verification/resonant_density_audit.py',
               'supplement/fixed_map/report-audit/verify.py']
    data = {'schema':'bgs-resonant-density-audit-v1','status':'PASS',
            'arithmetic':['integer/Fraction','SymPy exact rational algebra','complex128 FFT'],
            'runtime':{'python':platform.python_version(),'numpy':np.__version__,'sympy':sp.__version__},
            'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources},
            'interpolation':interpolation(),'cue_background':cue_background_controls(),
            'clusters':cluster_controls(),
            'realized_moments':realized_moments(),'factor_controls':factor_controls(),
            'exact_boxes':critical_family_exact_boxes(),
            'non_claims':['asymptotic theorem by finite computation',
                          'actual frozen-map E or local occupancy control','BGS solution',
                          'explicit clock background satisfies CUE pairs',
                          'numerical generation of the asymptotic CUE-background sequence',
                          'external referee or priority']}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS resonant density:',len(data['factor_controls']),
          'signed Fourier/Holder/counterterm cases; exact clusters and realizability')


if __name__ == '__main__':
    main()
