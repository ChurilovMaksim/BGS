"""Check resolvent/loop/Brownian identities, not BGS or fixed-tau asymptotics.

Run: OPENBLAS_NUM_THREADS=1 python3 build/resolvent-flow/checks.py
"""
from fractions import Fraction
from pathlib import Path
import importlib.util
import json
import math

import numpy as np
from scipy.linalg import expm

HERE = Path(__file__).resolve().parent


def energies(theta, s):
    n = len(theta)
    q = np.exp(-2*s/n)
    x = q*np.exp(1j*(theta[:, None]-theta[None, :]))
    aa = np.sum(x/(1-x), axis=1)
    bb = np.sum(x/(1-x)**2, axis=1)
    ll = np.sum(aa).real/n**2
    cc0 = np.sum(aa**2)/n**3
    derivative = -2*np.sum(bb).real/n**3
    cc1 = 2*np.sum(aa*bb).real/n**4
    source = q*(1+q)/(n**3*(1-q)**3)
    return dict(L=float(ll), C0_real=float(cc0.real), C0_imag=float(cc0.imag),
                derivative=float(derivative), C1=float(cc1), source=float(source),
                Brownian_W=float(source+derivative/2-cc1),
                mixed_bracket_real=float(ll+cc0.real-1/(4*s*s)),
                mixed_bracket_imag=float(cc0.imag))


def cot_values(theta, alpha, w):
    n = len(theta)
    t = (theta[None, :]-alpha[:, None])/2-w/n
    c = 1/np.tan(t)
    return (np.mean(c, axis=1), np.sum(1+c*c, axis=1)/n**2,
            np.sum(2*c*(1+c*c), axis=1)/n**3)


def loop_quadrature(theta, ws, grid=8192, beta=2):
    alpha = np.arange(grid)*2*np.pi/grid
    ss = [cot_values(theta, alpha, w) for w in ws]
    product = np.prod([t[0] for t in ss[1:]], axis=0) if len(ws)>1 else 1
    value = (((2-beta)/beta)*ss[0][1]+ss[0][0]**2+1)*product
    for j in range(1, len(ws)):
        d = ws[0]-ws[j]
        quotient = (ss[0][2]/2 if d == 0 else
                    -ss[j][1]/d+(ss[0][0]-ss[j][0])/d**2)
        rest = np.ones(grid, dtype=complex)
        for k in range(1, len(ws)):
            if k != j:
                rest *= ss[k][0]
        value += (2/beta)*quotient*rest
    return np.mean(value)


def frozen_unitary(n, epsilon):
    path = HERE.parent/'secular-route/exact_structure_checks.py'
    spec = importlib.util.spec_from_file_location('exact_structure', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    a, m = module.frozen_matrices(n)
    return expm(1j*epsilon*a)@m


def hermitian_basis(n):
    for j in range(n):
        h = np.zeros((n, n), complex)
        h[j, j] = 1
        yield h
    for j in range(n):
        for k in range(j):
            h = np.zeros((n, n), complex)
            h[j, k] = h[k, j] = 1/np.sqrt(2)
            yield h
            h = np.zeros((n, n), complex)
            h[j, k] = 1j/np.sqrt(2)
            h[k, j] = -1j/np.sqrt(2)
            yield h


def trace_square_generator(u, m):
    n = len(u)
    traces = [complex(n)]+[np.trace(np.linalg.matrix_power(u, k)) for k in range(1, m+1)]
    return m*m-m*abs(traces[m])**2-m/n*np.real(
        traces[m].conjugate()*sum(traces[k]*traces[m-k] for k in range(1, m)))


def laplacian(u, f, h):
    n = len(u)
    f0 = f(u)
    value = 0.
    for hh in hermitian_basis(n):
        ep = expm(1j*h*hh)
        value += (f(ep@u)-2*f0+f(ep.conj().T@u))/h**2
    return value/(2*n)


def check_brownian():
    rows = []
    for n in (3, 5):
        u = frozen_unitary(n, 0.17)
        for m in (1, 2, 4):
            f = lambda v: abs(np.trace(np.linalg.matrix_power(v, m)))**2
            direct = (4*laplacian(u, f, 0.005)-laplacian(u, f, 0.01))/3
            exact = trace_square_generator(u, m)
            error = abs(direct-exact)
            assert error < 2e-7
            rows.append(dict(N=n, m=m, generator=float(exact), error=float(error)))
        s = 1.3
        f = lambda v: energies(np.angle(np.linalg.eigvals(v)), s)['L']
        direct = (4*laplacian(u, f, 0.0025)-laplacian(u, f, 0.005))/(3*n)
        data = energies(np.angle(np.linalg.eigvals(u)), s)
        error = abs(direct-data['Brownian_W'])
        assert error < 2e-7
        rows.append(dict(N=n, observable='L', W=data['Brownian_W'], error=float(error)))
    return rows


def exact_cue():
    # Check every coefficient of the infinite cubic generating function:
    # sum_{a+b=m} E[p_-a p_-b p_m] = N*(m-N)_+.
    count = 0
    for n in range(1, 14):
        for m in range(2, 8*n+5):
            coefficient = sum(n-max(n-a, 0)-max(n-(m-a), 0)+max(n-m, 0)
                              for a in range(1, m))
            assert coefficient == n*max(m-n, 0)
            count += 1
        for q in (Fraction(1, 3), Fraction(2, 3), Fraction(7, 8)):
            l = q*(1-q**n)/(n*n*(1-q)**2)
            c0 = q**(n+1)/(n*n*(1-q)**2)
            assert l+c0 == q/(n*n*(1-q)**2)
            # Derivatives are with q'=-2q/N.
            dl = -2*q/n**3*((1-(n+1)*q**n)/(1-q)**2
                            +2*(q-q**(n+1))/(1-q)**3)
            c1 = q**(n+1)/n**3*((n+1)/(1-q)**2+2*q/(1-q)**3)
            source = q*(1+q)/(n**3*(1-q)**3)
            assert source+dl/2-c1 == 0
    return dict(integer_coefficients_checked=count, rational_CUE_stationarity=True,
                warning='CUE expectations are references, not the deterministic model.')


def check_loops():
    rows = []
    rng = np.random.default_rng(20260920)
    for n in (3, 5, 9, 15):
        cases = [('clock', 2*np.pi*np.arange(n)/n),
                 ('nonuniform_control', rng.uniform(-np.pi, np.pi, n)),
                 ('frozen_auxiliary_epsilon_0.17', np.angle(np.linalg.eigvals(frozen_unitary(n, .17))))]
        for name, theta in cases:
            s = 1.1
            ee = energies(theta, s)
            predicted = 8j*complex(ee['mixed_bracket_real'], ee['mixed_bracket_imag'])
            residual = loop_quadrature(theta, [1j*s/2, -1j*s/2])
            mixed_error = abs(residual-predicted)
            # Distinct and diagonal arguments, in both half-planes, all beta.
            same = max(abs(loop_quadrature(theta, ws, beta=beta))
                       for beta in (1, 2, 4)
                       for ws in ([.7j], [.7j, .3+1.1j], [.7j, .7j, -.2+.9j],
                                  [-.7j, -.7j, .2-.9j]))
            assert mixed_error < 2e-10 and same < 2e-10
            # A direct finite Fourier evaluation is independent of cot quadrature.
            cutoff = math.ceil(100*n/(2*s))
            ms = np.arange(1, cutoff+1)
            traces = np.exp(1j*ms[:, None]*theta).sum(axis=1)
            weights = np.exp(-2*s*ms/n)
            ld = np.sum(weights*abs(traces)**2)/n**2
            cubic = 0j
            for m in range(2, cutoff+1):
                cubic += weights[m-1]*traces[m-1]*np.sum(
                    np.conj(traces[:m-1])*np.conj(traces[m-2::-1]))/n**3
            fourier_error = max(abs(ld-ee['L']), abs(cubic-complex(ee['C0_real'], ee['C0_imag'])))
            assert fourier_error < 2e-10
            step = 1e-5
            def finite_defect(v):
                data = energies(theta, v)
                q = np.exp(-2*v/n)
                return data['L']+data['C0_real']-q/(n*n*(1-q)**2)
            derivative = (finite_defect(s+step)-finite_defect(s-step))/(4*step)
            assert abs(derivative-ee['Brownian_W']) < 2e-8
            if name == 'clock':
                assert abs(ee['L']+ee['C0_real']-1/(4*np.sinh(s)**2)) < 2e-12
            rows.append(dict(N=n, case=name, mixed_formula_error=float(mixed_error),
                             same_half_plane_max_error=float(same),
                             Fourier_sum_error=float(fourier_error), data=ee))
    return rows


if __name__ == '__main__':
    result = dict(status='finite identity checks passed; full mixed hierarchy UNPROVED',
                  CUE=exact_cue(), loops=check_loops(), Brownian=check_brownian(),
                  scope='Auxiliary exponents check formulas only. Original tau=1e-80 is not resolved.')
    (HERE/'checks.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(status=result['status'], CUE=result['CUE'],
        max_loop_error=max(r['mixed_formula_error'] for r in result['loops']),
        max_same_half_error=max(r['same_half_plane_max_error'] for r in result['loops']),
        max_laplacian_error=max(r['error'] for r in result['Brownian'])), indent=2))
