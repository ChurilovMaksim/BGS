#!/usr/bin/env python3
"""Direct signed Heisenberg-band diagnostics for the specified BGS matrices.

This is NOT a proof of BGS. All numerical couplings are explicit proxies,
not the literal 10**(-80). It does not assert that these proxy maps satisfy
the small-coupling classical hypotheses of the research project.
Dependencies: Python 3.10+, numpy, scipy. No network or repository writes.

Example:
    OPENBLAS_NUM_THREADS=1 python -O pair_probe.py --output results.json
"""
from __future__ import annotations
import argparse
import json
import math
import time
from pathlib import Path
from typing import Any
import numpy as np
import scipy
import scipy.linalg as la
from scipy.signal import fftconvolve

BANDS = {'stable': (0.08, 0.40), 'transition': (0.75, 1.25),
         'plateau': (1.20, 1.80), 'broad': (0.08, 1.80)}


def require(ok: bool, why: str) -> None:
    if not ok:
        raise RuntimeError(why)


def profile(q: np.ndarray) -> np.ndarray:
    return (1-np.cos(14*np.pi*q))*(1+np.cos(2*np.pi*q))


def physical_generator(n: int) -> np.ndarray:
    require(n >= 3 and n % 2 == 1, 'N must be odd and at least 3')
    x = np.arange(n, dtype=np.int64)
    q = x/n
    r = profile(q)
    diagonal = np.cos(14*np.pi*q)+r/10+r*np.sin(2*np.pi*q)/100-0.1
    a = np.diag(diagonal.astype(complex))
    shifted_q = ((x+pow(2, -1, n)) % n)/n
    upper = ((-3-4j)/5)*profile(shifted_q)/200
    a[x, (x+1) % n] += upper
    a[(x+1) % n, x] += upper.conjugate()
    return a


def metaplectic(n: int) -> np.ndarray:
    x = np.arange(n, dtype=np.int64)[:, None]
    y = x.T
    e = (pow(8, -1, n)*(3*x*x-2*x*y+3*y*y)) % n
    return np.exp(-2j*np.pi*e/n)/np.sqrt(n)


def weights(t: np.ndarray, a: float, b: float) -> np.ndarray:
    x = (2*t-a-b)/(b-a)
    y = np.zeros_like(t, dtype=float)
    inside = np.abs(x) < 1
    y[inside] = np.exp(1-1/(1-x[inside]**2))
    return y


def order_mod(n: int) -> int:
    a, b, c, d = 1, 0, 0, 1
    for k in range(1, 16*n*n+1):
        a, b, c, d = ((3*a+2*b) % n, (4*a+3*b) % n,
                      (3*c+2*d) % n, (4*c+3*d) % n)
        if (a, b, c, d) == (1, 0, 0, 1):
            return k
    raise RuntimeError('cat order search budget exceeded')


def cue_covariance(n: int, m: np.ndarray, k: np.ndarray) -> np.ndarray:
    """Exact covariance of |Tr V**m|^2 and |Tr V**k|^2 for Haar U(n)."""
    return ((m == k)*np.minimum(m, n)**2
            + 2*np.maximum(n-np.maximum(m, k), 0)
            - np.maximum(n-m-k, 0)-np.maximum(n-np.abs(m-k), 0))


def cue_variance(n: int, w: np.ndarray) -> float:
    """O(M log M) exact-formula evaluation, w[r-1] is the rth weight."""
    z = np.concatenate(([0.0], w))
    r = np.arange(len(z))
    diagonal = np.dot(z*z, np.minimum(r, n)**2)
    prefix_before = np.cumsum(z)-z
    maximum = 2*np.dot(np.maximum(n-r, 0), z*z+2*z*prefix_before)
    convolution = fftconvolve(z, z, mode='full')
    sums = np.dot(np.maximum(n-np.arange(len(convolution)), 0), convolution)
    ac = fftconvolve(z, z[::-1], mode='full')[len(z)-1:]
    differences = n*ac[0]+2*np.dot(np.maximum(n-r[1:], 0), ac[1:])
    v = float((diagonal+maximum-sums-differences)/n**4)
    require(v > -1e-11, 'negative CUE variance beyond roundoff')
    return max(v, 0.0)


def spectral_traces(u: np.ndarray, max_m: int) -> tuple[np.ndarray, dict[str, float]]:
    n = len(u)
    t, z = la.schur(u, output='complex', check_finite=False)
    ev = np.diag(t)
    residual = float(la.norm(u@z-z@t, ord='fro')/np.sqrt(n))
    modulus = float(np.max(np.abs(np.abs(ev)-1)))
    require(residual < 2e-11 and modulus < 2e-11, 'Schur residual too large')
    theta = np.angle(ev)
    traces = np.empty(max_m, dtype=complex)
    for lo in range(0, max_m, 128):
        hi = min(max_m, lo+128)
        m = np.arange(lo+1, hi+1)
        traces[lo:hi] = np.exp(1j*m[:, None]*theta[None, :]).sum(axis=1)
    return traces, {'schur_relative_residual': residual,
                    'unit_circle_residual': modulus}


def measure(u: np.ndarray, d: int) -> dict[str, Any]:
    n = len(u)
    max_m = math.floor(max(b for _, b in BANDS.values())*n)
    traces, checks = spectral_traces(u, max_m)
    m = np.arange(1, max_m+1)
    energy = np.abs(traces)**2
    records: dict[str, Any] = {}
    for name, (a, b) in BANDS.items():
        w = weights(m/n, a, b)
        main = float(np.dot(w, energy)/n**2)
        ref = float(np.dot(w, np.minimum(m, n))/n**2)
        variance = cue_variance(n, w)
        require(variance > 0, 'empty or degenerate weight')
        resonance = m % d == 0
        records[name] = {
            'band': [a, b], 'actual': main, 'reference_CUE': ref,
            'defect': main-ref, 'CUE_standard_deviation': math.sqrt(variance),
            'standardized_defect_not_a_pvalue': (main-ref)/math.sqrt(variance),
            'resonant_actual': float(np.dot(w[resonance], energy[resonance])/n**2),
            'resonant_reference': float(np.dot(w[resonance], np.minimum(m[resonance], n))/n**2),
            'number_active_modes': int(np.count_nonzero(w))}
    return {'bands': records, **checks}


def regressions() -> dict[str, Any]:
    rng = np.random.default_rng(20261015)
    max_var_error = 0.0
    max_trace_error = 0.0
    max_derivative_error = 0.0
    for n in [7, 19, 31]:
        r = np.arange(1, 2*n+1)
        cov = cue_covariance(n, r[:, None], r[None, :])
        for _ in range(5):
            w = rng.normal(size=len(r))
            exact = float(w@cov@w/n**4)
            fast = cue_variance(n, w)
            err = abs(exact-fast)
            max_var_error = max(max_var_error, err)
            require(err < 1e-11, 'CUE variance convolution error')
    for n in [19, 31, 63]:
        a = physical_generator(n)
        mcat = metaplectic(n)
        tau = 0.03
        u = la.expm(1j*tau*n*a)@mcat
        t, _ = spectral_traces(u, 2*n)
        power = np.eye(n, dtype=complex)
        direct = []
        inserted = []
        for j in range(1, 2*n+1):
            power = power@u
            direct.append(np.trace(power))
            inserted.append(np.trace(a@power))
        err = float(np.max(np.abs(t-np.array(direct))))
        max_trace_error = max(max_trace_error, err)
        require(err < 2e-10, 'trace eigenvalue/direct-power mismatch')
        inds = np.arange(1, 2*n+1)
        w = weights(inds/n, *BANDS['broad'])
        analytic = float(-2/n*np.sum(w*inds*np.imag(np.array(inserted)*np.conjugate(direct))))
        step = 1e-7
        values = []
        for sign in [-1, 1]:
            us = la.expm(1j*(tau+sign*step)*n*a)@mcat
            ts, _ = spectral_traces(us, 2*n)
            values.append(float(np.dot(w, np.abs(ts)**2)/n**2))
        finite = (values[1]-values[0])/(2*step)
        err = abs(analytic-finite)
        max_derivative_error = max(max_derivative_error, err)
        require(err < 2e-5, 'parameter derivative mismatch')
    return {'seed': 20261015, 'CUE_variance_comparisons': 15,
            'max_variance_error': max_var_error,
            'direct_power_dimensions': [19, 31, 63],
            'max_direct_power_trace_error': max_trace_error,
            'max_parameter_derivative_error': max_derivative_error,
            'tests_active_under_python_O': True}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sizes', type=int, nargs='+', default=[127, 251, 509, 777, 1009])
    parser.add_argument('--couplings', type=float, nargs='+', default=[0.03, 0.30])
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('pair_probe_extended.json'))
    args = parser.parse_args()
    for n in args.sizes:
        require(n >= 19 and n % 2 == 1, 'probe sizes must be odd and at least 19')
    require(all(math.isfinite(t) and abs(t) >= 1e-12 for t in args.couplings),
            'use explicitly finite, numerically resolvable proxy couplings')
    report: dict[str, Any] = {
        'status': 'finite proxy diagnostics; NOT a proof or literal-coupling asymptotic',
        'couplings_proxy_only': args.couplings, 'bands': BANDS,
        'weight': 'exp(1-1/(1-x^2)), x=(2t-a-b)/(b-a), supported on (a,b)',
        'CUE_covariance': 'delta_mn min(m,N)^2 + 2(N-max(m,n))_+ - (N-m-n)_+ - (N-|m-n|)_+',
        'CUE_reference_is_not_an_assumption_about_the_input': True,
        'numpy_version': np.__version__, 'scipy_version': scipy.__version__,
        'regressions': regressions(), 'records': []}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    for n in args.sizes:
        start = time.perf_counter()
        a = physical_generator(n)
        mcat = metaplectic(n)
        herror = float(la.norm(a-a.conj().T, ord='fro'))
        norm2 = float(np.vdot(a, a).real/n)
        require(herror < 1e-11, 'generator is not Hermitian')
        require(abs(norm2-66033/160000) < 1e-11, 'wrong generator norm')
        ae, av = la.eigh(a, check_finite=False)
        d = order_mod(n)
        for tau in args.couplings:
            q = (av*np.exp(1j*tau*n*ae))@av.conj().T
            u = q@mcat
            result = measure(u, d)
            result.update(N=n, tau_proxy=tau, cat_order=d,
                          norm2_generator=norm2)
            report['records'].append(result)
            print(json.dumps(result), flush=True)
            args.output.write_text(json.dumps(report, indent=2), encoding='utf-8')
        print('SECONDS', n, time.perf_counter()-start, flush=True)

if __name__ == '__main__':
    main()
