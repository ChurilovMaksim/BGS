#!/usr/bin/env python3
"""Independent finite checks for coherent/heterodyne aperture minimax proofs.

Exact: Chebyshev recurrences, factorial bias inequalities, endpoint bounds,
central-binomial inequalities, coefficient transformations. Numerical (mpmath):
probability/Hellinger inequalities and high-precision reconstruction. Neither
category is a proof of a growing-parameter minimax theorem; that proof is TeX.
No output file is created unless --output or --replay is supplied.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib
import importlib.util
import json
import random
import sys
import time
import mpmath as mp
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
MODULE = ROOT/'computations/analysis/coherent_reconstruction.py'
spec = importlib.util.spec_from_file_location('coherent_reconstruction', MODULE)
assert spec and spec.loader
cr = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = cr
spec.loader.exec_module(cr)


def exact_checks(max_k: int, rng: random.Random):
    counts = {'chebyshev_l1': 0, 'factorial_bias': 0,
              'logconvex_endpoints': 0, 'tail_ratio': 0,
              'central_binomial': 0, 'complex_coordinate_identities': 0}
    for j in range(257):
        coeff = cr.chebyshev_coefficients(j)
        assert sum(abs(x) for x in coeff) <= 3**j
        counts['chebyshev_l1'] += 1
    cases = []
    for s in [1, 2, 3, 5]:
        for K in range(1, max_k+1):
            for S in sorted(set([F(K), F(K, 2), F(K, 17), F(1, 4),
                                 F(1, 100), F(rng.randint(1, 100)*K, 100)])):
                if S > K:
                    continue
                L = 128*s*K
                A = max(F(1), factorial(K)*(F(2*s)/S)**K)
                # The squared analytic-bias inequality after cancelling the
                # common 16*binomial(L+2s,2s-1) factor on both sides.
                left = 9**L*A*A*(2*S)**(L+1)/factorial(L+1)
                right = F(1, 2**(2*(64*s-1)*K))
                assert left <= right, (s, K, S)
                counts['factorial_bias'] += 1
                cases.append([s, K, S.numerator, S.denominator])
                for j in range(K+1):
                    assert factorial(j)*(F(2*s)/S)**j <= A
                    counts['logconvex_endpoints'] += 1
                for j in [L, L+1, 2*L, 5*L]:
                    assert 8*S*(j+2*s) <= (j+1)**2
                    counts['tail_ratio'] += 1
    for k in range(1, 2049):
        assert comb(2*k, k)*(2*k+1) >= 2**(2*k)
        counts['central_binomial'] += 1
    z, w = sp.symbols('z w')
    for p in range(9):
        for q in range(9-p):
            polynomial = sp.Poly(((z+w)/2)**p*((z-w)/(2*sp.I))**q, w, z)
            for j in range(p+q+1):
                signed = sum(comb(p, ell)*comb(q, j-ell)*(-1)**(j-ell)
                             for ell in range(max(0, j-q), min(p, j)+1))
                expected = sp.Rational(signed, 2**(p+q))*sp.I**(-q)
                assert polynomial.coeff_monomial(w**j*z**(p+q-j)) == expected
                counts['complex_coordinate_identities'] += 1
    return counts, cases


def pair_probabilities(n, u, radial, cosine):
    a = mp.sqrt(1-u)*mp.exp(-radial/2)
    b = mp.sqrt(u)*mp.exp(-radial/2)*mp.power(radial, mp.mpf(n)/2)/mp.sqrt(factorial(n))
    plus = (a-b)**2+2*a*b*(1+cosine)
    minus = (a-b)**2+2*a*b*(1-cosine)
    difference = 4*a*b*cosine
    if difference == 0:
        return plus, minus, mp.mpf(0), a, b
    h = difference**2/(mp.sqrt(plus)+mp.sqrt(minus))**2
    h += difference**2/(mp.sqrt(1-plus)+mp.sqrt(1-minus))**2
    return plus, minus, h, a, b


def numerical_checks(rng: random.Random, dps: int):
    count = 0
    largest_h_ratio = mp.mpf(0)
    largest_forward_ratio = mp.mpf(0)
    anchors = []
    with mp.workdps(dps):
        tolerance = 1+mp.mpf(10)**(-dps//2)
        for E in [mp.mpf('0.25'), mp.mpf(1), mp.mpf(3)]:
            for beta in [mp.mpf('0.5'), mp.mpf(1), mp.mpf(2), mp.mpf(3)]:
                for n in [16, 32, 64, 128, 256, 512]:
                    u = E/mp.power(n, beta)
                    if u > mp.mpf('0.5') or 2**(-mp.mpf(n)/2) > mp.sqrt(u)/8:
                        continue
                    radii2 = [mp.mpf(0), u/10, mp.mpf('0.1'), mp.mpf(1),
                              n/(4*mp.e), mp.mpf(n)/4, n/mp.e,
                              mp.mpf(n)/2, mp.mpf(n), mp.mpf(2*n)]
                    radii2 += [mp.mpf(rng.randint(1, 100))*n/50]
                    for radial in radii2:
                        for cosine in [-1, mp.mpf('-0.5'), 0, mp.mpf('0.5'), 1]:
                            plus, minus, h, a, b = pair_probabilities(n, u, radial, cosine)
                            assert 0 <= plus <= 1-u/4
                            assert 0 <= minus <= 1-u/4
                            assert b*b <= u/2*tolerance
                            assert a*b <= mp.sqrt(u)*mp.power(2, -mp.mpf(n)/2)*tolerance
                            hb = 68*min(mp.power(2, -mp.mpf(n)/2),
                                        mp.power(radial, n)/factorial(n))
                            fb = 4*mp.sqrt(u)*min(mp.power(2, -mp.mpf(n)/2),
                                                mp.power(radial, mp.mpf(n)/2)/mp.sqrt(factorial(n)))
                            assert h <= hb*tolerance
                            # Avoid subtracting almost equal probabilities.
                            diff = abs(4*a*b*cosine)
                            assert diff <= fb*tolerance
                            if hb:
                                largest_h_ratio = max(largest_h_ratio, h/hb)
                            if fb:
                                largest_forward_ratio = max(largest_forward_ratio, diff/fb)
                            count += 1
        # Check the exact inverse-scale identity across aperture regimes.
        inverse_count = 0
        for T in [10, 100, 1000, 1000000]:
            for R2 in [mp.mpf('0.001'), 1, 100, mp.mpf(T)/100,
                       mp.mpf(T), mp.mpf(T)*100, mp.inf]:
                logplus = max(mp.mpf(0), mp.log(T/R2)) if R2 != mp.inf else mp.mpf(0)
                K = T/(1+logplus)
                phi = K*(1+max(mp.mpf(0), mp.log(K/R2))) if R2 != mp.inf else K
                assert (1-1/mp.e)*T <= phi*tolerance and phi <= T*tolerance
                inverse_count += 1
        for n in [8, 16, 32, 64, 128, 256]:
            u = mp.mpf(1)/n
            global_h = 4*mp.sqrt(u*(1-u))*mp.gamma(n/2+1)/mp.sqrt(factorial(n))
            assert global_h <= 4*mp.sqrt(u*(n+1))*mp.power(2, -mp.mpf(n)/2)*tolerance
            anchors.append({'n': n, 'mean_energy': 1,
                            'trace_distance': mp.nstr(2*mp.sqrt(u*(1-u)), 24),
                            'full_heterodyne_h2_upper': mp.nstr(global_h, 24),
                            'unit_aperture_h2_upper': mp.nstr(4*u/factorial(n+1), 24)})
    return {'probability_hellinger_cases': count, 'inverse_scale_cases': inverse_count,
            'decimal_precision': dps,
            'largest_ratio_to_hellinger_bound': mp.nstr(largest_h_ratio, 20),
            'largest_ratio_to_forward_bound': mp.nstr(largest_forward_ratio, 20),
            'anchors': anchors}


def reconstruction_checks(rng: random.Random, dps: int, expanded: bool):
    records = []
    with mp.workdps(dps):
        # Polynomial probabilities admit exact recovery up to working precision.
        for dim in ([2, 3, 4, 5, 6] if expanded else [2, 3, 4]):
            vectors = mp.matrix(dim, dim)
            for j in range(dim):
                for k in range(dim):
                    vectors[j, k] = mp.mpc(rng.randint(-4, 4), rng.randint(-4, 4))
            rho = vectors*vectors.H
            rho /= mp.fsum(rho[j, j] for j in range(dim))
            degree = 2*(dim-1)+3
            result = cr.reconstruct(lambda z: cr.fock_probability(rho, z), dim-1,
                                    degree, mp.mpf('0.7'), decimal_precision=dps)
            error = max(abs(result.raw[j, k]-rho[j, k])
                        for j in range(dim) for k in range(dim))
            assert error < mp.power(10, -dps+18), error
            state_error = cr.trace_norm_hermitian(result.density-rho)/2
            assert state_error < mp.power(10, -dps+20)
            records.append({'kind': 'finite_exact_polynomial', 'cutoff': dim-1,
                            'degree': degree, 'max_entry_error': mp.nstr(error, 12),
                            'trace_distance': mp.nstr(state_error, 12)})
        # A coherent input is truly infinite-dimensional: use its closed-form
        # probability, never a truncated probability model.
        alpha = mp.mpc('0.37', '-0.19')
        beta = mp.mpc('-0.25', '0.31')
        K = 2
        for L in ([32, 48, 64] if expanded else [32, 48]):
            prob = lambda z: (mp.exp(-abs(z-alpha)**2)+mp.exp(-abs(z-beta)**2))/2
            result = cr.reconstruct(prob, K, L, mp.mpf('0.2'), decimal_precision=dps)
            rho = mp.matrix(K+1)
            for j in range(K+1):
                for k in range(K+1):
                    rho[j, k] = mp.fsum(mp.exp(-abs(c)**2)*c**j*mp.conj(c)**k
                                       for c in [alpha, beta])/(2*mp.sqrt(factorial(j)*factorial(k)))
            error = max(abs(result.raw[j, k]-rho[j, k])
                        for j in range(K+1) for k in range(K+1))
            bound = cr.coefficient_bound(K, L, mp.mpf('0.2'), 0)
            assert error <= bound, (L, error, bound)
            records.append({'kind': 'infinite_coherent_mixture', 'cutoff': K,
                            'degree': L, 'max_entry_error': mp.nstr(error, 15),
                            'proved_entry_bound': mp.nstr(bound, 15)})
        # Deterministic bounded noise: check the theorem's multiplier rather
        # than fitting a condition number from the observed error.
        L, K, S = 32, 2, mp.mpf('0.2')
        a = mp.sqrt(S/2)
        nodes = [a*mp.cos(mp.pi*(j+mp.mpf('0.5'))/(L+1)) for j in range(L+1)]
        eta = mp.mpf('1e-24')
        prob = lambda z: mp.exp(-abs(z-alpha)**2)
        observed = [[prob(mp.mpc(x, y))+eta*mp.mpf(rng.randint(-10, 10))/10
                     for y in nodes] for x in nodes]
        result = cr.reconstruct(prob, K, L, S, observations=observed, decimal_precision=dps)
        true = mp.matrix([[mp.exp(-abs(alpha)**2)*alpha**j*mp.conj(alpha)**k/
                          mp.sqrt(factorial(j)*factorial(k)) for k in range(K+1)]
                          for j in range(K+1)])
        error = max(abs(result.raw[j, k]-true[j, k]) for j in range(K+1) for k in range(K+1))
        bound = cr.coefficient_bound(K, L, S, eta)
        assert error <= bound
        records.append({'kind': 'bounded_noise_infinite_input', 'cutoff': K,
                        'degree': L, 'noise': str(eta), 'max_entry_error': mp.nstr(error, 15),
                        'proved_entry_bound': mp.nstr(bound, 15)})
    rejected = 0
    for arguments in [(-1, 2, 1), (3, 2, 1), (1, 4, -1)]:
        try:
            cr.reconstruct(lambda z: 1, *arguments)
        except ValueError:
            rejected += 1
        else:
            raise AssertionError('invalid reconstruction inputs accepted')
    return {'cases': records, 'negative_controls': rejected}


def main():
    if not __debug__:
        raise RuntimeError('Verification must not run with python -O')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seed', type=int, default=20260906)
    parser.add_argument('--max-k', type=int, default=4)
    parser.add_argument('--dps', type=int, default=90)
    parser.add_argument('--expanded', action='store_true')
    parser.add_argument('--output', type=Path)
    parser.add_argument('--replay', type=Path)
    args = parser.parse_args()
    if args.max_k < 1 or args.max_k > 64 or args.dps < 60:
        parser.error('Require 1<=max-k<=64 and dps>=60')
    start = time.monotonic()
    rng = random.Random(args.seed)
    exact, cases = exact_checks(args.max_k, rng)
    numeric = numerical_checks(rng, args.dps)
    reconstruction = reconstruction_checks(rng, args.dps, args.expanded)
    result = {'status': 'PASS', 'scope': 'finite checks, not a proof by enumeration',
              'seed': args.seed, 'exact': exact, 'high_precision': numeric,
              'reconstruction': reconstruction,
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'implementation_sha256': hashlib.sha256(MODULE.read_bytes()).hexdigest(),
              'seconds': round(time.monotonic()-start, 3)}
    if args.replay:
        args.replay.parent.mkdir(parents=True, exist_ok=True)
        args.replay.write_text(str(len(cases))+'\n'+'\n'.join(' '.join(map(str, c)) for c in cases)+'\n')
        result['replay_sha256'] = hashlib.sha256(args.replay.read_bytes()).hexdigest()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
