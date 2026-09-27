#!/usr/bin/env python3
"""Audit controls for the 27 September CUE upload; no universality test.

Default: exact integer/rational arithmetic controls plus deterministic small
complex128 diagnostics. --proxy recomputes the N=1001, tau_eff=.05 example;
it changes the physical coupling and is never evidence for tau=1e-80.
No input scripts from the submission are imported. Requires numpy/scipy.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import platform

import numpy as np
import scipy
from scipy.linalg import expm
from frozen_full_lag_gap import ONE, cosine, plus, product, scale, sine


def mm(a, b):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))
                 for i in range(2) for j in range(2))


def symbol(physical=True):
    r = product(plus({(0, 0): ONE}, scale(cosine(7), (F(-1), F(0)))),
                plus({(0, 0): ONE}, cosine(1)))
    shifted = {k: tuple((-1 if physical and k[0] % 2 else 1)*v for v in c)
               for k, c in r.items()}
    pc = {(0, 1): (F(-3, 10), F(-2, 5)),
          (0, -1): (F(-3, 10), F(2, 5))}
    return plus(cosine(7), scale(r, (F(1, 10), F(0))),
                scale(product(r, sine(1)), (F(1, 100), F(0))),
                scale(product(shifted, pc), (F(1, 100), F(0))),
                {(0, 0): (F(-1, 10), F(0))})


def exact_lattice_checks():
    c = (1, 2, 1, 1)
    cm = (1, 0, 0, 1)
    samples = []
    for m in range(1, 101):
        cm = mm(cm, c)
        x, y = cm[0], cm[2]
        sm = mm(cm, cm)
        b = (sm[0]-1, sm[1], sm[2], sm[3]-1)
        bt = (b[0], b[2], b[1], b[3])
        det = b[0]*b[3]-b[1]*b[2]
        assert x*x-2*y*y == (-1)**m
        if m % 2:
            assert b == tuple(2*x*v for v in cm)
            d1 = d2 = 2*x
        else:
            assert b == tuple(2*y*v for v in mm(cm, (0, 2, 1, 0)))
            d1, d2 = 2*y, 4*y
        assert -det == d1*d2
        for k in range(-9, 10):
            for l in range(-9, 10):
                inverse_integer = ((bt[3]*k-bt[1]*l) % det == 0
                                   and (-bt[2]*k+bt[0]*l) % det == 0)
                assert inverse_integer == (k % d1 == 0 and l % d2 == 0)
        for g in (symbol(False), symbol(True)):
            assert len(g) == 32 and max(abs(k) for k, l in g) == 9
            avg = tuple(sum((v[j] for (k, l), v in g.items()
                             if k % d1 == 0 and l % d2 == 0), F(0))
                        for j in range(2))
            assert avg == ({1: F(-1, 10), 2: F(-1, 20)}.get(m, F(0)), F(0))
        if m <= 3:
            # Independent enumeration in the universal denominator |det B|.
            d = -det
            pts = {(j, k) for j in range(d) for k in range(d)
                   if (b[0]*j+b[1]*k) % d == 0
                   and (b[2]*j+b[3]*k) % d == 0}
            grid = {(j*(d//d1), k*(d//d2)) for j in range(d1) for k in range(d2)}
            assert pts == grid and len(pts) == d
        if m <= 6:
            samples.append({'m': m, 'grid': [d1, d2], 'points': -det})
    return {'times': [1, 100], 'membership_box': 9,
            'brute_enumerated_times': [1, 2, 3], 'first_grids': samples}


def r(q):
    return (1-np.cos(14*np.pi*q))*(1+np.cos(2*np.pi*q))


def v(q):
    return np.cos(14*np.pi*q)+r(q)/10+r(q)*np.sin(2*np.pi*q)/100-.1


def model(n):
    x = np.arange(n, dtype=np.int64)
    q = 3*x[:, None]**2-2*x[:, None]*x[None, :]+3*x[None, :]**2
    m = np.exp(2j*np.pi*((-pow(8, -1, n)*q) % n)/n)/np.sqrt(n)
    a = np.diag(v(x/n).astype(complex))
    b = (-3-4j)/1000*r((x+(n+1)//2)/n)
    a[x, (x+1) % n] += b
    a[(x+1) % n, x] += b.conj()
    return a, m


def convention_checks():
    norms = []
    for n in (19, 31, 101):
        a, _ = model(n)
        x = np.arange(n)
        wrong = np.diag(v(x/n).astype(complex))
        b = (-3-4j)/1000*r((x+.5)/n)
        wrong[x, (x+1) % n] += b
        wrong[(x+1) % n, x] += b.conj()
        err = float(np.linalg.norm(a-wrong, 'fro')**2/n)
        assert abs(err-1/5000) < 1e-15
        norms.append([n, err])
    rows = []
    for n in (1001, 1003, 1005, 1007, 8001, 8003, 8005, 8007):
        # Sparse trace contraction, without constructing dense matrices.
        x = np.arange(n, dtype=np.int64)
        y = (x+1) % n
        u = pow(8, -1, n)
        diag = np.exp(2j*np.pi*((-u*4*x*x) % n)/n)/np.sqrt(n)
        off = np.exp(2j*np.pi*((-u*(3*x*x-2*x*y+3*y*y)) % n)/n)/np.sqrt(n)
        b = (-3-4j)/1000*r((x+(n+1)//2)/n)
        tm = diag.sum()
        ta = (v(x/n)*diag+2*b.real*off).sum()
        expected = {1: 1, 3: 1j, 5: -1, 7: -1j}[n % 8]
        assert abs(tm-expected) < 1e-10
        rows.append({'N': n, 'raw_error': float(abs(ta+1.1)),
                     'phase_normalized_error': float(abs(ta/tm+1.1))})
    assert rows[6]['raw_error'] > 2
    return {'wrong_symbol_HS_squared_over_N': norms, 'phase_rows': rows}


def homometry_check():
    aa, bb = {0, 1, 4}, {0, 10, 22}
    x = {a+b for a in aa for b in bb}
    y = {a+22-b for a in aa for b in bb}
    pair = lambda z: Counter((a-b) % 101 for a in z for b in z)
    triple = lambda z: Counter(((a-c) % 101, (b-c) % 101)
                               for a in z for b in z for c in z
                               if len({a, b, c}) == 3)
    assert len(x) == len(y) == 9 and pair(x) == pair(y)
    assert triple(x)[6, 18] == 1 and triple(y)[6, 18] == 0
    return {'phase_numerators_X': sorted(x), 'phase_numerators_Y': sorted(y),
            'denominator': 101, 'distinct_triple_offsets': [6, 18], 'counts': [1, 0]}


def bispectrum_check():
    # The upload uses positive trace powers and a positive inverse Fourier
    # exponential: this reflects both offsets. Compare to real-space kernels.
    theta = np.array([0., .1, .35])
    n, sigma, s1, s2 = 3, .08, .3, 1.05
    xx = n*theta
    direct = 0.
    for anchor in xx:
        d = (xx-anchor) % n
        def kernel(s):
            return sum(np.exp(-.5*((d+j*n-s)/sigma)**2)
                       for j in (-1, 0, 1))/(sigma*np.sqrt(2*np.pi))
        direct += kernel(s1).sum()*kernel(s2).sum()/n
    ns = np.arange(-80, 81)
    ps = np.array([np.exp(2j*np.pi*k*theta).sum() for k in range(-160, 161)])
    p = ps[ns+160]
    coef = p[:, None]*p[None, :]*ps[ns[:, None]+ns[None, :]+160].conj()/n**3
    damp = np.exp(-2*np.pi**2*sigma**2*(ns/n)**2)
    def reconstruct(sign):
        e1 = damp*np.exp(sign*2j*np.pi*ns*s1/n)
        e2 = damp*np.exp(sign*2j*np.pi*ns*s2/n)
        return float(np.real(e1@coef@e2))
    wrong, corrected = reconstruct(1), reconstruct(-1)
    assert abs(corrected-direct) < 1e-12 and abs(wrong-direct) > 8
    for a, b in ((0, 0), (1, 2), (1, -1)):
        pn = lambda k: np.exp(2j*np.pi*k*theta).sum()
        formula = pn(a)*pn(b)*pn(-a-b)-abs(pn(a))**2-abs(pn(b))**2-abs(pn(a+b))**2+2*n
        brute = sum(np.exp(2j*np.pi*(a*(theta[j]-theta[l])+b*(theta[k]-theta[l])))
                    for j in range(n) for k in range(n) for l in range(n)
                    if len({j, k, l}) == 3)
        assert abs(formula-brute) < 1e-12
    return {'N': n, 'theta': theta.tolist(), 'sigma': sigma, 'nmax': 80,
            'offsets': [s1, s2], 'real_space': float(direct),
            'submitted_sign': wrong, 'corrected_sign': corrected,
            'distinct_index_modes': [[0, 0], [1, 2], [1, -1]]}


def taylor_checks():
    count = 0
    for n in (11, 19):
        a, mat = model(n)
        anorm = np.linalg.norm(a, 2)
        for m in (1, 2, 4):
            mp = np.linalg.matrix_power(mat, m)
            c1 = 1j*m*np.trace(a@mp)
            c2 = -m*np.trace(a@a@mp)/2
            c2 -= sum((m-d)*np.trace(a@np.linalg.matrix_power(mat, d)
                      @a@np.linalg.matrix_power(mat, m-d)) for d in range(1, m))
            # Independent truncated-polynomial multiplication of (exp(itA)M)^m.
            coeff = [np.eye(n, dtype=complex), np.zeros((n, n), complex),
                     np.zeros((n, n), complex)]
            factor = [mat, 1j*a@mat, -a@a@mat/2]
            for _ in range(m):
                coeff = [sum((coeff[j]@factor[k-j] for j in range(k+1)),
                             np.zeros((n, n), complex)) for k in range(3)]
            assert abs(np.trace(coeff[1])-c1) < 1e-10
            assert abs(np.trace(coeff[2])-c2) < 1e-10
            t = .02
            exact = np.trace(np.linalg.matrix_power(expm(1j*t*a)@mat, m))
            error = abs(exact-np.trace(mp)-t*c1-t*t*c2)
            assert error <= n*(m*anorm*t)**3/math.factorial(3)+1e-12
            count += 1
    return {'finite_cases': count, 'lambda': .02, 'orders': [1, 2]}


def full_abel(theta, s):
    n = len(theta)
    rr = np.exp(-2*s/n)
    one_minus = -np.expm1(-2*s/n)
    delta = np.pi*(theta[:, None]-theta[None, :])
    poisson = -np.expm1(-4*s/n)/(one_minus**2+4*rr*np.sin(delta)**2)
    return float((poisson.sum()/n**2-1)/2)


def proxy():
    n = 1001
    a, m = model(n)
    theta = np.angle(np.linalg.eigvals(expm(1j*.05*n*a)@m))/(2*np.pi) % 1
    ms = np.arange(1, 8*n+1)
    p2 = np.array([abs(np.exp(2j*np.pi*j*theta).sum())**2 for j in ms])
    rows = []
    for s in (.5, 1., 2.):
        short = float(np.sum(np.exp(-2*s*ms/n)*p2)/n**2)
        full = full_abel(theta, s)
        bound = float(np.exp(-2*s*(8*n+1)/n)/(-np.expm1(-2*s/n)))
        assert -1e-12 <= full-short <= bound+1e-12
        rows.append({'s': s, 'truncated': short, 'infinite_poisson': full,
                     'tail': full-short, 'universal_tail_bound': bound})
    assert abs(rows[0]['truncated']-.633090539674316) < 1e-9
    assert rows[0]['tail'] > 3e-4
    return {'N': n, 'tau_eff': .05, 'cutoff': 8*n, 'rows': rows,
            'nonclaim': 'Proxy coupling, not the prescribed tau=1e-80 limit.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--proxy', action='store_true')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    for n in (3, 9):
        for s in (.5, 2.):
            assert abs(full_abel(np.zeros(n), s)-1/np.expm1(2*s/n)) < 1e-12
    result = {'status': 'passed', 'arithmetic': 'exact integers/fractions; complex128 diagnostics',
              'lattice': exact_lattice_checks(), 'conventions': convention_checks(),
              'homometry': homometry_check(), 'bispectrum': bispectrum_check(),
              'taylor': taylor_checks(),
              'environment': {'python': platform.python_version(),
                              'numpy': np.__version__, 'scipy': scipy.__version__},
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'nonclaim': 'Finite regression; no BGS, high-time remainder or novelty certification.'}
    if args.proxy:
        result['proxy'] = proxy()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
