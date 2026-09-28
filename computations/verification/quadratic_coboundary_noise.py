#!/usr/bin/env python3
"""Finite controls for BGS-FLOW-003; no asymptotic or universality test.

Deterministic complex128 full Hermitian-basis contractions, N<=7; radial
generator checks, N<=65; exact Fraction Laurent integration for Haar U(4).
No Monte Carlo, eigengap cutoff, actual frozen coupling, or Lean certificate.
The analytic theorem is in mathematics/quadratic_coboundary_noise.md.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import platform

import numpy as np
import scipy
from scipy.linalg import expm


def hermitian_basis(n, traceless=False):
    out = []
    if traceless:
        for k in range(1, n):
            d = np.zeros(n)
            d[:k], d[k] = 1, -k
            out.append(np.diag(d).astype(complex)/np.sqrt(k*(k+1)))
    else:
        for j in range(n):
            d = np.zeros(n)
            d[j] = 1
            out.append(np.diag(d).astype(complex))
    for j in range(n):
        for k in range(j):
            t = np.zeros((n, n), complex)
            t[j, k] = t[k, j] = 1/np.sqrt(2)
            out.append(t)
            t = np.zeros((n, n), complex)
            t[j, k], t[k, j] = 1j/np.sqrt(2), -1j/np.sqrt(2)
            out.append(t)
    return np.array(out)


def comm(a, b):
    return a @ b - b @ a


def coefficients(u, basis):
    b = u @ basis @ u.conj().T
    return np.array([[1j/(2*np.sqrt(2))*(comm(tj, bk)+comm(tk, bj))
                      for tk, bk in zip(basis, b)]
                     for tj, bj in zip(basis, b)])


def parameters(theta):
    n = len(theta)
    z = np.exp(1j*theta)
    q = np.mean(z*z)
    delta = theta[:, None]-theta[None, :]
    v = (1-np.real(q/(z[:, None]*z[None, :])))/n
    sigma = np.diag(np.diag(v))-2*np.sin(delta)**2/n**2
    return z, q, delta, v, sigma


def covariance_check(theta):
    n = len(theta)
    z, q, delta, v, sigma = parameters(theta)
    u = np.diag(z)
    aa = coefficients(u, hermitian_basis(n)/np.sqrt(n))
    mu = np.einsum('aajk->jk', aa)
    # E[(xi_a xi_b-delta_ab)(xi_c xi_d-delta_cd)] gives 2 for symmetric aa.
    tensor = 2*np.einsum('rsjk,rsab->jkab', aa, aa)
    pred = np.zeros_like(tensor)
    for j in range(n):
        for k in range(n):
            pred[j, k, k, j] += v[j, k]
            pred[j, j, k, k] -= 2*np.sin(delta[j, k])**2/n**2
    mean_error = float(np.max(abs(mu-np.diag(np.sqrt(2)*np.imag(z*np.conj(np.mean(z)))))))
    tensor_error = float(np.max(abs(tensor-pred)))
    assert max(mean_error, tensor_error) < 2e-13
    assert np.linalg.norm(sigma @ np.ones(n)) < 2e-13
    basis = hermitian_basis(n, traceless=True)
    coord = np.einsum('rsjk,akj->rsa', aa, basis)
    assert np.max(abs(coord.imag)) < 2e-13
    cov = 2*np.einsum('rsa,rsb->ab', coord.real, coord.real)
    # Independent invariant covariance operator, then scalar products.
    tr2 = np.einsum('jk,akj->a', u @ u, basis)
    applied = (basis/n-(q*(u.conj().T @ basis @ u.conj().T)
                        +np.conj(q)*(u @ basis @ u))/(2*n)
               +(tr2[:, None, None]*(u.conj().T @ u.conj().T)
                 +tr2.conj()[:, None, None]*(u @ u))/(2*n*n))
    invariant = np.einsum('ajk,bkj->ab', basis, applied).real
    assert np.max(abs(cov-invariant)) < 2e-13
    eig, vec = np.linalg.eigh(cov)
    assert eig[0] >= (1-abs(q))/n-2e-13
    assert eig[-1] <= (2+abs(q))/n+2e-13
    whitening_error = None
    if abs(q) < 1-1e-8:
        w = (vec/np.sqrt(n*eig)) @ vec.T
        whitening_error = float(np.max(abs(w @ cov @ w-np.eye(n*n-1)/n)))
        assert whitening_error < 2e-12
    else:
        assert np.linalg.norm(sigma) < 2e-13
        assert eig[0] < 2e-13
    return {'N': n, 'abs_m2': float(abs(q)), 'tensor_error': tensor_error,
            'mean_error': mean_error, 'min_cov_eigenvalue': float(eig[0]),
            'whitening_error': whitening_error}


def generator_checks():
    rows = []
    for n in (3, 4, 7, 13):
        theta = np.linspace(.1, 5., n)**1.13
        z, q, delta, v, sigma = parameters(theta)
        cot = np.zeros_like(delta)
        mask = ~np.eye(n, dtype=bool)
        cot[mask] = 1/np.tan(delta[mask]/2)
        drift = .5*np.sum(v*cot, axis=1)
        p = {r: sum(z**r) for r in (1, 2, 3, 4)}
        lp2 = np.dot(drift, 2j*z*z)-2*np.dot(np.diag(sigma), z*z)
        pred = (-p[2]/2-p[1]**2/n
                +(p[2]*abs(p[1])**2+np.conj(p[2])*(p[1]*p[3]+p[2]**2))/(2*n*n))
        gamma = 4*np.einsum('jk,j,k', sigma, z*z, np.conj(z*z))
        gamma_pred = 6-8*abs(p[2])**2/n**2+2*abs(p[4])**2/n**2
        # Direct real gradient/Hessian of |p2|^2 also checks the product rule.
        grad = -4*np.imag(z*z*np.conj(p[2]))
        hess = 8*np.real(z[:, None]**2*np.conj(z[None, :]**2))
        hess -= np.diag(8*np.real(z*z*np.conj(p[2])))
        direct = np.dot(drift, grad)+.5*np.sum(sigma*hess)
        product = 2*np.real(np.conj(p[2])*pred)+gamma_pred
        err = float(max(abs(lp2-pred), abs(gamma-gamma_pred), abs(direct-product)))
        assert err < 2e-12
        rows.append({'N': n, 'moment_generator_error': err})
    clocks = []
    for n in (5, 9, 17, 33, 65):
        theta = 2*np.pi*np.arange(n)/n
        z, q, delta, v, sigma = parameters(theta)
        x = ((delta+np.pi) % (2*np.pi)-np.pi)*n/(2*np.pi)
        radius = 1.4
        dd = np.where(abs(x) < radius,
                      8/radius**2*(1-(x/radius)**2)**2*(7*(x/radius)**2-1), 0)
        np.fill_diagonal(dd, 0)
        hess = 2*(n/(2*np.pi))**2/n*(np.diag(dd.sum(axis=1))-dd)
        # Pair gradient vanishes at the clock by cyclic and reflection symmetry.
        ld = .5*np.trace(hess)/n
        lx = .5*np.sum(sigma*hess)
        prediction = np.sum((1-np.cos(2*delta))*dd)/(4*np.pi**2*n)
        assert abs(lx-ld-prediction) < 2e-12
        # A conservative analytic supremum bound on |x^2 phi''(x)| is 48.
        assert abs(prediction) <= 96*(n-1)/n**2
        clocks.append({'N': n, 'pair_generator_difference': float(lx-ld),
                       'Dyson_pair_generator_over_N': float(ld/n)})
    deformed = []
    for n in (17, 33, 65):
        base = 2*np.pi*np.arange(n)/n
        theta = base+.15*np.sin(2*base)
        z, q, delta, v, sigma = parameters(theta)
        x = ((delta+np.pi) % (2*np.pi)-np.pi)*n/(2*np.pi)
        radius = 1.4
        dp = np.where(abs(x) < radius, -8*x/radius**2*(1-(x/radius)**2)**3, 0)
        dd = np.where(abs(x) < radius,
                      8/radius**2*(1-(x/radius)**2)**2*(7*(x/radius)**2-1), 0)
        np.fill_diagonal(dd, 0)
        grad = dp.sum(axis=1)/np.pi
        hess = n/(2*np.pi**2)*(np.diag(dd.sum(axis=1))-dd)
        cot = np.zeros_like(delta)
        mask = ~np.eye(n, dtype=bool)
        cot[mask] = 1/np.tan(delta[mask]/2)
        direct = (.5*np.sum((sigma-np.eye(n)/n)*hess)
                  +.5*np.dot(np.sum((v-1/n)*cot, axis=1), grad))
        a = np.real(q/(z[:, None]*z[None, :]))
        rank2 = np.sum((1-np.cos(2*delta))*dd)/(4*np.pi**2*n)
        drift = -np.sum(a*cot*(grad[:, None]-grad[None, :]))/(4*n)
        diagonal = -np.dot(np.diag(a), np.diag(hess))/(2*n)
        assert abs(direct-rank2-drift-diagonal) < 2e-12
        forward = (theta[:, None]-theta[None, :]) % (2*np.pi)
        occupancy = int(np.max(np.sum(forward <= 2*np.pi/n+1e-12, axis=0)))
        assert occupancy == 2
        deformed.append({'N': n, 'abs_m2': float(abs(q)), 'occupancy_bound': occupancy,
                         'microscopic_pair_generator_difference': float(direct/n),
                         'symmetrized_identity_error': float(abs(direct-rank2-drift-diagonal))})
    return {'moment_identities': rows, 'clock_pairs': clocks,
            'nonzero_m2_pairs': deformed}


def exact_haar_check():
    """Weyl integral as a Laurent constant coefficient / 4!, all rational."""
    n = 4
    zero = (0,)*n
    one = {zero: F(1)}

    def add(*polys):
        out = {}
        for poly in polys:
            for k, v in poly.items():
                out[k] = out.get(k, F(0))+v
        return {k: v for k, v in out.items() if v}

    def scale(poly, c):
        return {k: c*v for k, v in poly.items() if c*v}

    def mul(a, b):
        out = {}
        for k, v in a.items():
            for l, w in b.items():
                key = tuple(x+y for x, y in zip(k, l))
                out[key] = out.get(key, F(0))+v*w
        return {k: v for k, v in out.items() if v}

    def conj(a):
        return {tuple(-x for x in k): v for k, v in a.items()}

    def p(r):
        return {tuple(r if j == k else 0 for j in range(n)): F(1) for k in range(n)}

    def abs2(a):
        return mul(a, conj(a))

    p1, p2, p3, p4 = (p(r) for r in (1, 2, 3, 4))
    lp2 = add(scale(p2, F(-1, 2)), scale(mul(p1, p1), F(-1, n)),
              scale(add(mul(p2, abs2(p1)),
                        mul(conj(p2), add(mul(p1, p3), mul(p2, p2)))), F(1, 2*n*n)))
    cross = mul(conj(p2), lp2)
    observable = add(cross, conj(cross), scale(one, F(6)),
                     scale(abs2(p2), F(-8, n*n)), scale(abs2(p4), F(2, n*n)))
    density = one
    for j in range(n):
        for k in range(j):
            ex = tuple(int(a == j)-int(a == k) for a in range(n))
            density = mul(density, {zero: F(2), ex: F(-1),
                                   tuple(-x for x in ex): F(-1)})
    assert density[zero] == math.factorial(n)
    integral = sum(v*density.get(tuple(-x for x in k), 0)
                   for k, v in observable.items())/math.factorial(n)
    assert integral == F(4)+F(2, n*n) == F(33, 8)
    return {'N': n, 'arithmetic': 'Fraction Laurent constant coefficient',
            'density_monomials': len(density), 'stationarity_defect': str(integral)}


def normal_form_and_rank():
    n = 7
    theta = np.linspace(.1, 5., n)**1.13
    u = np.diag(np.exp(1j*theta))
    basis = hermitian_basis(n)
    g = np.einsum('a,ajk->jk', np.sin(np.arange(n*n)+.2)/n, basis)
    b = u @ g @ u.conj().T
    h = 1j/np.sqrt(2)*comm(g, b)
    errors = []
    for t in (.02, .01, .005):
        w = expm(-1j*t*g) @ expm(1j*t*(g-b)) @ expm(1j*t*b)
        error = float(np.linalg.norm((w-np.eye(n))/t**2-1j*h/np.sqrt(2)))
        errors.append(error)
    assert errors[1] < .6*errors[0] and errors[2] < .6*errors[1]
    short = basis[:3]
    aa = coefficients(u, short)
    coord = np.einsum('rsjk,akj->rsa', aa, hermitian_basis(n, True)).real
    rank = int(np.linalg.matrix_rank(coord.reshape(9, -1), tol=1e-12))
    assert rank <= 3*4//2
    # These diagonal generators commute with diagonal U: rank is actually zero.
    # Use a mixed basis as well, to avoid a vacuous rank-only test.
    short = np.array([basis[0]+basis[n], basis[1]+basis[n+2], basis[n+4]])
    aa = coefficients(u, short)
    coord = np.einsum('rsjk,akj->rsa', aa, hermitian_basis(n, True)).real
    mixed_rank = int(np.linalg.matrix_rank(coord.reshape(9, -1), tol=1e-12))
    assert 0 < mixed_rank <= 6
    translate_errors = []
    for r in (1, 2, 9):
        ur = np.linalg.matrix_power(u, r)
        gr = ur.conj().T @ g @ ur
        hr = 1j/np.sqrt(2)*comm(gr, u @ gr @ u.conj().T)
        err = float(np.max(abs(np.diag(hr)-np.diag(h))))
        assert err < 2e-13
        translate_errors.append(err)
    return {'normal_form_scaled_errors': errors, 'd3_mixed_rank': mixed_rank,
            'translated_radial_errors': translate_errors}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    cases = []
    for n in (2, 3, 4, 5, 7):
        cases.append(covariance_check(2*np.pi*np.arange(n)/n))
        cases.append(covariance_check(np.linspace(.1, 5., n)**1.13))
    cases.append(covariance_check(np.array([0., 0., np.pi, np.pi])))
    cases.append(covariance_check(np.zeros(3)))
    report = {'claim': 'BGS-FLOW-003', 'status': 'PASS finite controls only',
              'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__,
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'covariance_cases': cases, 'generators': generator_checks(),
              'exact_haar': exact_haar_check(), 'normal_form_rank': normal_form_and_rank(),
              'exclusions': ['no deterministic BGS transfer', 'no large-N limit',
                             'no full original fourth-order generator',
                             'no novelty or formal-proof certificate']}
    payload = json.dumps(report, indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload)
    print(payload)


if __name__ == '__main__':
    main()
