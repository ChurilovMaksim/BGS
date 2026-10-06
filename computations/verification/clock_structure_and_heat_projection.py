#!/usr/bin/env python3
"""Finite exact controls of FLOW-018/019; no asymptotic certificate.

Fractions control Fourier selection, clock heat jets and stable Gram matrices.
Complex128 kernels and binary64 quadratures are finite diagnostics.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import argparse
from collections import defaultdict
from fractions import Fraction as Q
import hashlib
from math import factorial
from itertools import permutations
from pathlib import Path
import platform
import json

import numpy as np
from numpy.polynomial.legendre import leggauss

from microscopic_noise_removal import (
    add, expand_word, neutral_words, radial_generator, trace_generator,
)
from quadratic_noise_clock import alias_kernel


def clock_value(n, word):
    return n**len(word) if all(m % n == 0 for m in word) else 0


def profile(n, m, z):
    """S3 at z=exp(-t), entirely rational for its squared mean."""
    mean = Q(0)
    if m % n == 0:
        q = m//n
        mean = sum(z**(n*q*q+q*(l+k))
                   for l in range(-(n-1)//2, (n-1)//2+1)
                   for k in range(-(n-1)//2, (n-1)//2+1))
    r0 = m//n
    cross = sum(Q(n-abs(m-r*n))*z**(r*m)
                for r in (r0, r0+1) if abs(m-r*n)<n)
    return mean+n-cross


def angular_selection(n, m, z):
    """Independent l,k enumeration of both angular Fourier constraints."""
    ell = range(-(n-1)//2, (n-1)//2+1)
    mean = Q(0)
    if m % n == 0:
        q = m//n
        for l in ell:
            for k in ell:
                mean += z**(n*q*q+q*(l+k))
    cross = Q(0)
    for l in ell:
        for k in ell:
            difference = m-(l-k)
            if difference % n == 0:
                r = difference//n
                exponent = n*r*r+r*(l-k)
                assert exponent == r*m and exponent >= 0
                cross += z**exponent
    return mean+n-cross


def profile_jet(n, m, order):
    mean = 0
    if m % n == 0:
        q = m//n
        mean = sum((-(n*q*q+q*(l+k)))**order
                   for l in range(-(n-1)//2, (n-1)//2+1)
                   for k in range(-(n-1)//2, (n-1)//2+1))
    r0 = m//n
    cross = sum((n-abs(m-r*n))*(-r*m)**order
                for r in (r0, r0+1) if abs(m-r*n)<n)
    return mean+(n if order == 0 else 0)-cross


def gram(left, right):
    powers = defaultdict(lambda: [0, 0])
    for m in left+tuple(-k for k in right):
        powers[abs(m)][m < 0] += 1
    if any(a != b for a, b in powers.values()):
        return Q(0)
    result = Q(1)
    for m, (a, _) in powers.items():
        result *= m**a*factorial(a)
    return result


def positive_ldl(matrix):
    """Exact unpivoted LDL pivots; used only for positive definite matrices."""
    size = len(matrix)
    lower = [[Q(0) for _ in range(size)] for _ in range(size)]
    diag = []
    for i in range(size):
        pivot = matrix[i][i]-sum(lower[i][k]**2*diag[k] for k in range(i))
        assert pivot > 0
        diag.append(pivot)
        lower[i][i] = Q(1)
        for j in range(i+1, size):
            lower[j][i] = (matrix[j][i]-sum(
                lower[j][k]*lower[i][k]*diag[k] for k in range(i)))/pivot
    return diag


def critical_kernel(tau, u, v, phase, rmax=12):
    difference = v[None, :]-u[:, None]
    result = np.sinc(difference).astype(complex)
    for r in range(-rmax, rmax+1):
        if r == 0:
            continue
        integral = (
            np.exp(-tau*r*(r-1)/2-1j*np.pi*difference)
            -np.exp(-tau*r*(r+1)/2+1j*np.pi*difference)
        )/(tau*r-2j*np.pi*difference)
        result += np.exp(2j*np.pi*r*(v[None, :]+phase))*integral
    return result


def block_determinant_coefficients(matrix, split):
    """Determinant after multiplying the two off-diagonal blocks by z."""
    size = len(matrix)
    coefficients = defaultdict(Q)
    for perm in permutations(range(size)):
        inversions = sum(perm[i]>perm[j] for i in range(size) for j in range(i+1, size))
        coefficient = Q((-1)**inversions)
        degree = 0
        for i, j in enumerate(perm):
            coefficient *= matrix[i][j]
            degree += (i<split) != (j<split)
        coefficients[degree] += coefficient
    return {degree: c for degree, c in coefficients.items() if c}


def run():
    exact = 0
    for n in (3, 5, 7, 11):
        for m in range(1, 2*n+2):
            for z in (Q(1, 4), Q(2, 3), Q(9, 10)):
                value = profile(n, m, z)
                assert value == angular_selection(n, m, z)
                assert 0 <= value <= n*n
                exact += 1

    masses = 0
    abel_signs = 0
    for n in (3, 5, 7):
        for q in range(1, 5):
            for z in (Q(1, 4), Q(2, 3), Q(9, 10)):
                mesh = sum(Q(n-abs(m-q*n), n*n)*z**(q*m)
                           for m in range((q-1)*n+1, (q+1)*n))
                ell = range(-(n-1)//2, (n-1)//2+1)
                square = sum(z**(n*q*q+q*(l+k)) for l in ell for k in ell)/(n*n)
                assert mesh == square
                masses += 1
                for w in (Q(1, 2), Q(4, 5)):
                    weighted = sum(Q(n-abs(m-q*n), n*n)*z**(q*m)*w**m
                        for m in range((q-1)*n+1, (q+1)*n))
                    assert square*w**(q*n)-weighted < 0
                    abel_signs += 1

    jets = 0
    for n in (3, 5, 7):
        for m in range(1, n+3):
            symbolic = {tuple(sorted((m, -m))): Q(1)}
            for order in range(5):
                value = sum(c*clock_value(n, word) for word, c in symbolic.items())
                assert value == profile_jet(n, m, order)
                updated = {}
                for word, c in symbolic.items():
                    updated = add(updated, trace_generator(n, word), c)
                symbolic = updated
                jets += 1

    radial = 0
    for m in range(1, 6):
        pol = expand_word(3, (m, -m))
        symbolic = {tuple(sorted((m, -m))): Q(1)}
        for order in range(4):
            direct = {}
            for word, c in symbolic.items():
                direct = add(direct, expand_word(3, word), c)
            assert pol == direct
            pol = radial_generator(3, pol)
            updated = {}
            for word, c in symbolic.items():
                updated = add(updated, trace_generator(3, word), c)
            symbolic = updated
            radial += 1

    stable = []
    for degree in range(5):
        words = list(neutral_words(degree))
        h = [[gram(a, b) for b in words] for a in words]
        pivots = positive_ldl(h)
        index = {word: i for i, word in enumerate(words)}
        for n in sorted({max(3, 2*degree), max(3, 2*degree+1), 2*degree+3}):
            actions = [trace_generator(n, word) for word in words]
            assert all(word in index for action in actions for word in action)
            mh = [[sum(c*h[index[word]][j] for word, c in action.items())
                   for j in range(len(words))] for action in actions]
            assert mh == [list(row) for row in zip(*mh)]
            assert all(value == 0 for value in mh[0])
            drift_pivots = positive_ldl([
                [-mh[i][j] for j in range(1, len(words))]
                for i in range(1, len(words))])
            stable.append({'Q': degree, 'N': n, 'dimension': len(words),
                           'gram_min_pivot': str(min(pivots)),
                           'negative_generator_min_pivot':
                           str(min(drift_pivots)) if drift_pivots else None})

    kernel_rows = []
    u = np.array([-.7, .11, .9])
    v = np.array([-.3, .45, 1.1])
    for tau in (.5, 2., 8.):
        for phase in (.17, .43):
            limiting = critical_kernel(tau, u, v, phase)
            for n in (31, 63, 127):
                finite = (2*np.pi/n)*alias_kernel(n, tau/n,
                    2*np.pi*(phase+u)/n, 2*np.pi*(phase+v)/n)
                error = float(np.max(abs(finite-limiting)))
                max_x = float(np.max(abs(v[None, :]-u[:, None])))
                mid = sum(np.exp(-tau*abs(r)*(abs(r)-1)/2)
                    *((tau*r)**2+(2*np.pi*max_x)**2)
                    for r in range(-12, 13))/(24*n*n)
                tail = 2*np.exp(-tau*13*12/2)/(1-np.exp(-tau*13))
                assert error <= mid+2*tail+2e-12
                kernel_rows.append({'N': n, 'tau': tau, 'phase': phase,
                                    'error': error, 'midpoint_bound': float(mid),
                                    'alias_tail_bound': float(tail)})

    nodes, weights = leggauss(96)
    xi = .5+.25*nodes
    weights = .25*weights
    bump = lambda x: np.where(abs(x-.5)<.25,
        np.exp(-1/np.maximum(1-16*(x-.5)**2, 1e-300)), 0.)
    band = []
    for tau in (.5, 2., 8.):
        target = float(np.sum(weights*bump(xi)**2*xi*(-np.expm1(-tau*xi))))
        for n in (31, 101, 301):
            x = np.arange(1, n)/n
            finite = float(np.sum(bump(x)**2*x*(-np.expm1(-tau*x)))/n)
            assert abs(finite-target) < 2e-4/n
            band.append({'N': n, 'tau': tau, 'variance': finite,
                         'quadrature': target, 'error': abs(finite-target)})

    sharp = []
    for tau, n in ((4., 1001), (8., 2001), (16., 4001), (32., 8001)):
        a1 = (-np.expm1(-tau))/(2*n*np.sinh(tau/(2*n)))
        # W is supported in [0.8,1.2], equals one at 1, and vanishes at 0.
        x = np.arange(1, 2*n)/n
        w = np.where(abs(x-1)<.2,
             np.exp(1-1/np.maximum(1-25*(x-1)**2, 1e-300)), 0.)
        negative = float(np.sum(w*(1-abs(x-1))*np.exp(-tau*x))/n)
        # W's support meets q=1 and q=2 profiles; include both.
        negative += float(np.sum(w*np.maximum(1-abs(x-2), 0.)*np.exp(-2*tau*x))/n)
        coefficient = tau*tau*(a1*a1-negative)
        assert 0 < coefficient <= 1.000001
        sharp.append({'N': n, 'tau': tau, 'rescaled_pair_defect': float(coefficient)})
    assert abs(sharp[-1]['rescaled_pair_defect']-1) < 1e-5

    blocks = 0
    for size in range(2, 7):
        for split in range(1, size):
            for pattern in range(2):
                matrix = [[Q((3*i+5*j+i*j)%5-2, 3) if pattern == 0
                           else Q((i+j)%3-1, 2)
                           for j in range(size)] for i in range(size)]
                coefficients = block_determinant_coefficients(matrix, split)
                assert all(degree % 2 == 0 for degree in coefficients)
                cross = max(abs(matrix[i][j]) for i in range(size) for j in range(size)
                            if (i<split) != (j<split))
                error = abs(sum(c for degree, c in coefficients.items() if degree>0))
                # Squared Taylor/Hadamard bound, entirely rational.
                assert error**2 <= Q(size**8, 4)*cross**4*(size-2)**(size-2)
                blocks += 1

    return {'status': 'PASS', 'exact_angular_selection_cases': exact,
            'exact_mesh_mass_cases': masses, 'exact_clock_generator_jets': jets,
            'exact_abel_summand_sign_cases': abel_signs,
            'exact_radial_polynomial_cases': radial,
            'stable_gram_cases': stable, 'critical_kernel_diagnostics': kernel_rows,
            'exact_cross_block_taylor_surrogates': blocks,
            'band_variance_diagnostics': band, 'sharp_rate_diagnostics': sharp,
            'randomness': {'used': False, 'generator': '', 'seed': None},
            'numerical_tolerances': {'kernel_roundoff_margin': 2e-12,
                'band_error_bound': '2e-4/N', 'sharp_last_error': 1e-5},
            'non_claims': ['No stochastic trajectory simulated',
                'No all-N/degree or asymptotic proof certificate',
                'No analytic Lean, actual-map noise removal, full BGS or novelty certification']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = run()
    result.update({'python': platform.python_version(), 'numpy': np.__version__,
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})
    data = json.dumps(result, indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(data)
    print(data, end='')


if __name__ == '__main__':
    main()
