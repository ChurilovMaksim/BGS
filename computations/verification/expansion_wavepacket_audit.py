#!/usr/bin/env python3
"""Finite convention controls for TRACE-013 and FM-013/016.

Exact integer/rational arithmetic; finite Weil characters at p=5,13;
complex128 group multiplication at p=5, even channels p=41,61,
and odd-N Gaussian frames at N=5,13,19. No asymptotic theorem is
certified by these computations; in particular no fixed-tau eigenvalue
experiment, factorial flat kick, Monte Carlo or Heisenberg extrapolation.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
R = (4, 9, 19, 43)
S = (3, 2, 1, 1)
V = (-5, 19, -24, 91)
IDENTITY = (1, 0, 0, 1)


def mul(a, b, p=None):
    out = (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
           a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3])
    return tuple(x % p for x in out) if p else out


def power(a, k, p):
    out = IDENTITY
    while k:
        if k & 1:
            out = mul(out, a, p)
        a = mul(a, a, p)
        k //= 2
    return out


def matrix(g):
    return sp.Matrix(2, 2, g)


def arithmetic():
    r, s, v = map(matrix, (R, S, V))
    assert v*s == r
    assert all(a.det() == 1 for a in (r, s, v))
    assert ((r+8*sp.eye(2))/21)**4 == r
    assert (r+sp.eye(2))[0, 0] % 7 != 0
    x, t, z = sp.symbols('x t z', integer=True)
    c = sp.Matrix([[x, 3*x+9*t], [-2*x-19*t, -x]])
    assert c*r == r.inv()*c
    form = 5*x*x+75*x*t+171*t*t
    assert sp.expand(c.det()-form) == 0
    assert sp.expand((10*x+75*t)**2-5*(21*t)**2-20*form) == 0
    a = [2, 3]
    for _ in range(16):
        a.append(3*a[-1]-a[-2])
    assert [n % 3 for n in a[:4]] == [2, 0, 1, 0]
    assert [n % 7 for n in a[:8]] == [2, 3, 0, 4, 5, 4, 0, 3]
    assert (a[8] % 7, a[9] % 7) == (2, 3)
    assert not any(n % 21 == 0 for n in a)
    assert sp.resultant(z*z-2*z-2, 19*z*z+39*z-9, z) == -6551
    assert sp.trace(s*v*s.inv()*v.inv()) == -6549
    rows = []
    for p in map(int, sp.primerange(2, 1000)):
        if p % 20 != 1:
            continue
        d = (p-1)//4
        assert power(R, d, p) == IDENTITY
        for q in map(int, sp.factorint(d)):
            while d % q == 0 and power(R, d//q, p) == IDENTITY:
                d //= q
        assert power(R, d, p) == IDENTITY
        rows.append({'p': p, 'order': d, 'even_dimension': (p+1)//2,
                     'clock_pitch': str(Fraction(p+1, 2*d))})
    return {'resultant': -6551, 'commutator_trace': -6549,
            'prime_progression_rows': rows}


def legendre(a, p):
    a %= p
    return 0 if a == 0 else (1 if pow(a, (p-1)//2, p) == 1 else -1)


def group(p):
    return [(a, b, c, d) for a in range(p) for b in range(p)
            for c in range(p) for d in range(p) if (a*d-b*c) % p == 1]


def weil(g, p):
    a, b, c, d = (v % p for v in g)
    x = np.arange(p)
    if b:
        exponent = ((d*x[:, None]**2-2*x[:, None]*x[None, :]+a*x[None, :]**2)
                    * pow(2*b, -1, p)) % p
        return legendre(-2*b, p)*np.exp(2j*np.pi*exponent/p)/np.sqrt(p)
    out = np.zeros((p, p), complex)
    out[x, (pow(a, -1, p)*x) % p] = legendre(a, p)*np.exp(
        2j*np.pi*((c*pow(2*a, -1, p)*x*x) % p)/p)
    return out


def even_basis(p):
    basis = np.zeros((p, (p+1)//2))
    basis[0, 0] = 1
    for j in range(1, (p+1)//2):
        basis[j, j] = basis[-j, j] = 1/np.sqrt(2)
    return basis


def characters():
    rows = []
    p_symbol = sp.symbols('p', positive=True)
    formulas = {}
    for k in range(1, 6):
        unipotent_sum = sp.Rational(2, 2**(2*k))*sum(
            sp.binomial(2*k, 2*l)*p_symbol**l for l in range(k+1))
        expr = sp.cancel((2*((p_symbol+1)/2)**(2*k)
                          +(p_symbol-3)*p_symbol*(p_symbol+1)/2
                          +(p_symbol**2-1)*unipotent_sum)
                         /(p_symbol*(p_symbol**2-1)))
        formulas[k] = expr
    assert formulas[1] == 1
    assert sp.simplify(formulas[2]-(p_symbol+7)/4) == 0
    assert sp.simplify(formulas[3]-(p_symbol+3)*(p_symbol**2+4*p_symbol+19)/32) == 0
    for p in (5, 13):
        basis = even_basis(p)
        values, counts = [], Counter()
        for g in group(p):
            q = basis.T@weil(g, p)@basis
            tr = np.trace(q)
            values.append(tr)
            trace = (g[0]+g[3]) % p
            if g in ((1, 0, 0, 1), (p-1, 0, 0, p-1)):
                counts['center'] += 1
            elif trace not in (2, p-2):
                label = 'split' if legendre(trace*trace-4, p) == 1 else 'nonsplit'
                counts[label] += 1
                assert abs(abs(tr)**2-(label == 'split')) < 3e-12
            else:
                counts['unipotent'] += 1
        assert len(values) == p*(p*p-1)
        assert counts['center'] == 2
        assert counts['split'] == (p-3)*p*(p+1)//2
        assert counts['unipotent'] == 2*(p*p-1)
        moments = {}
        for k in range(1, 6):
            expected = int(formulas[k].subs(p_symbol, p))
            actual = float(np.mean(np.abs(values)**(2*k)))
            assert abs(actual-expected) < 3e-10*(1+expected)
            moments[k] = {'exact_rank': expected, 'character_average': actual}
        rows.append({'p': p, 'elements': len(values), 'classes': dict(counts),
                     'moments': moments})
    p = 5
    matrices = {g: weil(g, p) for g in group(p)}
    err = max(float(np.max(abs(a@b-matrices[mul(g, h, p)])))
              for g, a in matrices.items() for h, b in matrices.items())
    assert err < 3e-12
    return {'formulas': {k: str(v) for k, v in formulas.items()},
            'enumerated': rows, 'p5_all_group_products': len(matrices)**2,
            'multiplication_max_error': err}


def compression():
    p = 5
    gs = group(p)
    pairs = {(a, b, c, d) for a in range(p) for b in range(p)
             for c in range(p) for d in range(p)}
    rows = []
    while pairs:
        v = next(iter(pairs))
        orbit = {((g[0]*v[0]+g[1]*v[1]) % p,
                  (g[2]*v[0]+g[3]*v[1]) % p,
                  (g[0]*v[2]+g[1]*v[3]) % p,
                  (g[2]*v[2]+g[3]*v[3]) % p) for g in gs}
        pairs -= orbit
        phases = Counter((w[1]+w[3]) % p for w in orbit)
        zero_sum = all((w[0]+w[2]) % p == 0 and
                       (w[1]+w[3]) % p == 0 for w in orbit)
        expected = 1 if zero_sum else -1/(p*p-1)
        average = sum(count*np.exp(2j*np.pi*phase/p)
                      for phase, count in phases.items())/len(orbit)
        assert abs(average-expected) < 2e-15
        rows.append({'orbit_size': len(orbit), 'zero_sum': zero_sum,
                     'phase_counts': dict(sorted(phases.items())),
                     'compressed_real_part': float(average.real)})
    assert len(rows) == 2*p+1
    assert sum(row['zero_sum'] for row in rows) == 2
    return sorted(rows, key=lambda row: (row['orbit_size'], row['zero_sum']))


def channels():
    rows = []
    for p in (41, 61):
        basis = even_basis(p)
        n = basis.shape[1]
        qs, qv, qr = (basis.T@weil(g, p)@basis for g in (S, V, R))
        op = np.eye(n*n, dtype=complex)/2
        for q in (qs, qv):
            adj = np.kron(q.conj(), q)
            op += (adj+adj.conj().T)/8
        eigen = np.linalg.eigvalsh(op)
        assert -3e-12 <= eigen[0] and abs(eigen[-1]-1) < 3e-12
        gap = float(1-eigen[-2])
        assert gap > .01
        d = next(k for k in range(1, (p-1)//4+1) if power(R, k, p) == IDENTITY)
        scalar_error = float(np.max(abs(np.linalg.matrix_power(qr, d)-np.eye(n))))
        assert scalar_error < 1e-11
        rows.append({'p': p, 'N': n, 'finite_one_copy_gap': gap,
                     'word_order': d, 'scalar_word_error': scalar_error})
    return rows


def frames():
    rows = []
    for n in (5, 13, 19):
        x = np.arange(n)
        pgrid = np.arange(8*n)/(8*n)
        qgrid = np.arange(8*n)/(8*n)
        frame = np.zeros((n, n), complex)
        norm_error = 0.
        for q in qgrid:
            dist = x[None, :, None]/n-q-np.arange(-2, 3)[None, None, :]
            psi = (2/n)**.25*np.sum(np.exp(-np.pi*n*dist**2)
                        *np.exp(2j*np.pi*n*pgrid[:, None, None]*dist), axis=2)
            frame += psi.T@psi.conj()/len(pgrid)
            norm_error = max(norm_error, float(np.max(abs(np.sum(abs(psi)**2, axis=1)-1))))
        frame *= n/len(qgrid)
        err = float(np.max(abs(frame-np.eye(n))))
        assert err < 5e-13
        raw_err = 0.
        for a, b in ((1, 1), (-2, 3), (3, -1)):
            raw = np.eye(n)[(x+a) % n]*np.exp(
                2j*np.pi*b*((x+pow(2, -1, n)*a) % n)/n)[:, None]
            mid = np.eye(n)[(x+a) % n]*np.exp(2j*np.pi*b*(x+a/2)/n)[:, None]
            raw_err = max(raw_err, float(np.max(abs((-1)**(a*b)*raw-mid))))
        assert raw_err < 2e-14
        rows.append({'N': n, 'q_cells': len(qgrid), 'p_cells': len(pgrid),
                     'images': [-2, 2], 'frame_max_error': err,
                     'norm_max_error': norm_error, 'midpoint_dictionary_max_error': raw_err})
    q, p = sp.symbols('q p', real=True)
    r = lambda a: (1-sp.cos(14*sp.pi*a))*(1+sp.cos(2*sp.pi*a))
    g = sp.cos(14*sp.pi*q)+r(q)/10+r(q)*sp.sin(2*sp.pi*q)/100-sp.Rational(1, 10)
    g += r(q+sp.Rational(1, 2))*(-3*sp.cos(2*sp.pi*p)+4*sp.sin(2*sp.pi*p))/500
    hessians = []
    for a in (0, sp.Rational(1, 2)):
        for b in (0, sp.Rational(1, 2)):
            sub = {q: a, p: b}
            assert all(sp.diff(g, v).subs(sub).simplify() == 0 for v in (q, p))
            mat = sp.hessian(g, (q, p)).subs(sub).applyfunc(sp.simplify)
            assert mat[0, 1] == mat[1, 0] == mat[1, 1] == 0
            hessians.append(str(sp.simplify(mat[0, 0]/sp.pi**2)))
    assert sorted(hessians) == sorted(['-19606/125', '-19594/125', '24306/125', '24894/125'])
    return {'finite_frames': rows, 'exact_q_hessians_over_pi_squared': hessians}


def gaussian_trace_bounds():
    """Exact normalization/algebra controls for the fixed-time bound only."""
    a, b, c, d = sp.symbols('a b c d', real=True)
    mat = sp.Matrix([[a, b], [c, d]])
    sigma = sp.eye(2)+mat*mat.T
    frobenius_square = sum(value**2 for value in mat)
    assert sp.expand(sigma.det()-1-frobenius_square-mat.det()**2) == 0
    cat = sp.Matrix([[3, -4], [-2, 3]])
    rows = []
    for j, points, square, sigma_upper, ratio, bound in (
            (1, 4, 38, 41, sp.Rational(40, 39), 4),
            (2, 32, 1298, 1301, sp.Rational(320, 319), 9)):
        jac = cat**j
        assert jac.det() == 1 and abs((jac-sp.eye(2)).det()) == points
        assert sum(value**2 for value in jac) == square
        covariance = sp.eye(2)+jac*jac.T
        displacement = jac-sp.eye(2)
        quadratic = displacement.T*covariance.inv()*displacement
        assert quadratic.det() == sp.Rational(points**2, square+2)
        # Fourth powers remove every radical from the strict upper bounds.
        fourth_power = ratio**4*4*sigma_upper
        assert fourth_power < bound**4
        rows.append({'j': j, 'cat_fixed_points': points,
                     'cat_frobenius_square': square,
                     'displacement_gaussian_determinant': str(quadratic.det()),
                     'conservative_bound_fourth_power': str(fourth_power),
                     'strict_limsup_bound': bound})
    # Identity propagation: the Gaussian overlap amplitude must be one.
    assert sp.sqrt(2)*(sp.eye(2)*2).det()**(-sp.Rational(1, 4)) == 1
    return {'general_covariance_determinant_identity': True,
            'vacuum_overlap_normalization': True, 'first_two_times': rows,
            'scope': 'Exact Gaussian/matrix algebra; not a numerical test of the nonlinear trace limit, threshold or Heisenberg estimates.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    data = {'status': 'PASS', 'date': '2026-10-04',
            'python': platform.python_version(), 'numpy': np.__version__, 'sympy': sp.__version__,
            'arithmetic': arithmetic(), 'characters': characters(),
            'translation_compression': compression(), 'finite_channels': channels(),
            'coherent_frames': frames(), 'gaussian_trace_bounds': gaussian_trace_bounds(),
            'non_claims': ['asymptotic proof certification', 'actual flat-kick numerical spectra',
                          'Heisenberg trace cancellation', 'BGS', 'priority',
                          'independent referee', 'Lean compilation']}
    sources = ['mathematics/arithmetic_word_expansion_obstruction.md',
               'mathematics/egorov_overlap_rigidity.md',
               'mathematics/fixed_time_wavepacket_trace_bound.md',
               'computations/verification/expansion_wavepacket_audit.py']
    data['source_sha256'] = {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
                             for name in sources}
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(data, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'prime_orders': len(data['arithmetic']['prime_progression_rows']),
                      'group_products': data['characters']['p5_all_group_products'],
                      'two_copy_orbits': len(data['translation_compression']),
                      'finite_channels': len(data['finite_channels']), 'odd_frames': 3}))


if __name__ == '__main__':
    main()
