#!/usr/bin/env python3
"""Pell Floquet normal form: exact arithmetic and independent matrix/FFT tests.

The proof is mathematics/pell_floquet_normal_form.md. Dense floating-point
checks and seeded trace estimates are diagnostics, not a proof of the limit.
No SciPy dependency is needed: Hermitian exponentials use numpy.linalg.eigh.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from pathlib import Path
import subprocess
import mpmath as mp
import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]


def design(k: int) -> tuple[int, int, int]:
    if k < 3 or not sp.isprime(k) or k % 2 == 0:
        raise ValueError('K must be an odd prime')
    n, f = 1, 0
    for _ in range(k):
        n, f = n + 2*f, n + f
    assert n*n - 2*f*f == -1
    h = (3 + 2*pow(f, -1, n)) % n
    assert pow(h, k, n) == 1
    assert all(math.gcd(pow(h, j, n)-1, n) == 1 for j in range(1, k))
    assert all(math.gcd(pow(h, j, n)+1, n) == 1 for j in range(k))
    assert (n-1) % (2*k) == 0
    return n, f, h


def arithmetic(k: int) -> dict:
    n, f, h = design(k)
    # Signed pairs with distinct time labels, modulo the simultaneous inverse
    # pair of congruences. This is independent of dense matrix construction.
    vectors = [(pow(h, j, n), pow(h, -j, n)) for j in range(k)]
    keys = set()
    for t in range(k):
        for s in range(t+1, k):
            for e in (-1, 1):
                for d in (-1, 1):
                    key = ((e*vectors[t][0]+d*vectors[s][0]) % n,
                           (e*vectors[t][1]+d*vectors[s][1]) % n)
                    assert key != (0, 0) and key not in keys
                    keys.add(key)
    assert len(keys) == 2*k*(k-1)
    # Integer numerators of the centered discrete cohomological inverse.
    b = [k-1-2*j for j in range(k)]
    assert sum(b) == 0
    assert [b[j]-b[(j-1) % k] for j in range(k)] == [2*(k-1)]+[-2]*(k-1)
    mp.mp.dps = 70
    lam = 3+2*mp.sqrt(2)
    aa = [mp.mpf(0)]*k
    for j in range(1, (k+1)//2):
        qq, pp = 1, 0
        for _ in range(2*j):
            qq, pp = qq+2*pp, qq+pp
        assert (-f*(pow(h, j, n)-pow(h, -j, n))+2*pp) % n == 0
        aa[j] = aa[k-j] = abs(mp.exp(4j*mp.pi*pp/n)-1)
    l1 = sum(aa)
    weighted = sum(abs(b[j])*aa[j]/2 for j in range(k))
    assert l1 < 9 and weighted <= 2*mp.pi/(1-lam**(-k))
    gram = 4*sum((k-j)*j*j*aa[j]**2 for j in range(1,k))/mp.mpf(k)**4
    assert gram <= 9/mp.mpf(k)
    if k >= 11:
        # Exact rational version of four-letter quadratic-norm lifting.
        L = k-(k+3)//4
        Q, P = 1, 0
        for _ in range(2*L):
            Q, P = Q+2*P, Q+P
        assert 16*(2*Q+3*P) < 2*n*n
    return {'K':k, 'N':str(n), 'signed_pair_keys':len(keys),
            'phase_l1':float(l1), 'K_weighted_phase_l1':float(weighted),
            'commutator_full_HS_squared':float(gram),
            'K_times_commutator_HS_squared':float(k*gram)}


def weyl(n: int, a: int, b: int) -> np.ndarray:
    x = np.arange(n, dtype=np.int64)
    mat = np.zeros((n,n), dtype=complex)
    phase = (a*(x-b*pow(2,-1,n))) % n
    mat[x,(x-b) % n] = np.exp(2j*np.pi*phase/n)
    return mat


def hermitian_exponential(a: np.ndarray, t: float) -> np.ndarray:
    if np.max(abs(a-a.conj().T)) > 1e-10:
        raise ValueError('Hermitian exponential received a non-Hermitian matrix')
    values, vectors = np.linalg.eigh(a)
    return (vectors*np.exp(1j*t*values))@vectors.conj().T


def fft_step(z: np.ndarray, k: int, eps: float) -> np.ndarray:
    """Apply exp(i eps B_q) S_h^(-1) to columns of odd or full vectors."""
    n, f, h = design(k)
    if z.ndim != 2 or z.shape[0] != n:
        raise ValueError('expected an N by R matrix')
    x = np.arange(n, dtype=np.int64)
    q = -f % n
    phase = (((q*((x*x) % n)) % n)*pow(2,-1,n)) % n
    chirp = np.exp(2j*np.pi*phase/n)
    diagonal = np.exp(2j*eps*np.cos(2*np.pi*x/n))
    y = chirp.conj()[:,None]*z[(h*x) % n]
    y = np.fft.ifft(diagonal[:,None]*np.fft.fft(y, axis=0), axis=0)
    return chirp[:,None]*y


def dense(k: int) -> list[dict]:
    if k > 7:
        raise ValueError('dense reference tests are limited to K <= 7')
    n, f, h = design(k)
    q = -f % n
    bs = []
    for j in range(k):
        w = weyl(n, q*pow(h,j,n) % n, pow(h,-j,n))
        bs.append(w+w.conj().T)
    c = (k-1-2*np.arange(k))/(2*k)
    g, av, b = sum(ct*bt for ct,bt in zip(c,bs)), sum(bs)/k, bs[0]
    u = np.eye(n, dtype=complex)[(h*np.arange(n)) % n]
    assert np.max(abs(g-u@g@u.conj().T-b+av)) < 2e-11
    gram = np.linalg.norm(g@av-av@g,'fro')**2/n
    assert abs(gram-arithmetic(k)['commutator_full_HS_squared']) < 1e-10
    d = (n-1)//2
    projection = np.zeros((n,d))
    j = np.arange(1,d+1)
    projection[j,j-1] = 1/math.sqrt(2)
    projection[n-j,j-1] = -1/math.sqrt(2)
    gr, ar, br, ur = [projection.T@a@projection for a in (g,av,b,u)]
    # Independent comparison with the existing signed orbit block assembler.
    from pell_gaussian_regression import block
    block_values = np.sort(np.concatenate([np.linalg.eigvalsh(block(k,j)) for j in range(k)]))
    assert np.max(abs(block_values-np.linalg.eigvalsh(math.sqrt(k/2)*ar))) < 1e-10
    out = []
    for tau in (.5,1.,2.):
        eps = tau/math.sqrt(2*k)
        uk = hermitian_exponential(br,eps)@ur
        normal = hermitian_exponential(ar,eps)@ur
        v = hermitian_exponential(gr,-eps)
        error = np.linalg.norm(v@uk@v.conj().T-normal,'fro')/math.sqrt(d)
        assert error <= 12*eps*eps/math.sqrt(k)+1e-10
        assert np.max(abs(projection.T@fft_step(projection,k,eps)-uk)) < 2e-11
        for m in (1,2):
            actual = np.trace(np.linalg.matrix_power(uk,m*k))/d
            model = np.trace(hermitian_exponential(ar,m*eps*k))/d
            assert abs(actual-model) <= m*k*error+1e-9
            out.append({'K':k, 'N':n, 'dimension':d, 'tau':tau, 'm':m,
                        'one_step_HS_error':float(error),
                        'one_step_proved_bound':12*eps*eps/math.sqrt(k),
                        'trace_real':float(actual.real), 'trace_imag':float(actual.imag),
                        'effective_trace_real':float(model.real),
                        'wrapped_Gaussian_limit':math.exp(-m*m*tau*tau/2),
                        'method':'complete dense odd spectrum; floating-point diagnostic'})
    return out


def sampled_trace(k: int, tau: float, probes: int, seed: int) -> list[dict]:
    if probes < 2:
        raise ValueError('at least two independent probes required')
    n, _, _ = design(k)
    if n > 50000:
        raise ValueError('standard FFT experiment limited to N <= 50000')
    d = (n-1)//2
    rng = np.random.default_rng(seed)
    coefficients = (1j)**rng.integers(0,4,size=(d,probes))
    z = np.zeros((n,probes), dtype=complex)
    z[1:d+1] = coefficients/math.sqrt(2)
    z[n-np.arange(1,d+1)] = -coefficients/math.sqrt(2)
    initial = z.copy()
    eps = tau/math.sqrt(2*k)
    out = []
    for t in range(1,2*k+1):
        z = fft_step(z,k,eps)
        if t % k == 0:
            estimates = np.sum(initial.conj()*z,axis=0)/d
            value = np.mean(estimates)
            assert np.max(abs(np.sum(abs(z)**2,axis=0)/d-1)) < 1e-10
            m = t//k
            out.append({'K':k, 'N':n, 'dimension':d, 'tau':tau, 'm':m,
                        'trace_real':float(value.real), 'trace_imag':float(value.imag),
                        'wrapped_Gaussian_limit':math.exp(-m*m*tau*tau/2),
                        'probes':probes, 'seed':seed,
                        'complex_RMS_error_upper_bound':1/math.sqrt(probes*d),
                        'complex_sample_standard_error':float(np.std(estimates,ddof=1)/math.sqrt(probes)),
                        'method':'seeded unbiased random-phase trace estimate; RMS bound is not a deterministic error bar'})
    return out


def report(cpp: Path | None, extended: bool, probes: int) -> dict:
    ks = (3,5,7,11,13,17,23,31,47,101)
    rows = [arithmetic(k) for k in ks]
    if cpp:
        text = subprocess.check_output([str(cpp.resolve())],text=True,timeout=60)
        got = json.loads(text)
        assert [(r['K'],r['N'],r['signed_pair_keys']) for r in rows] == [
            (r['K'],r['N'],r['signed_pair_keys']) for r in got['checks']]
    # A nonprime period is an explicit negative domain control.
    try:
        design(9)
    except ValueError:
        pass
    else:
        raise AssertionError('composite period silently accepted')
    r = (3+2*sp.sqrt(2))**-1
    A = 4*sp.pi/(sp.sqrt(2)*(1+sp.sqrt(2)))
    assert sp.simplify(A*(1+r)/(1-r)**2-2*sp.pi) == 0
    out = {'producer':'computations/verification/pell_floquet_regression.py',
           'scope':'Exact finite Pell/cohomological/pair-key checks; floating-point matrix and FFT diagnostics; no proof of BGS, priority, or general Lean formalization.',
           'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'arithmetic_checks':rows, 'dense_checks':sum((dense(k) for k in (3,5,7)),[]),
           'cpp_cross_check':bool(cpp), 'sampled_checks':[], 'status':'PASS'}
    if extended:
        for k in (11,13):
            for tau in (.5,1.,2.):
                out['sampled_checks'].extend(sampled_trace(k,tau,probes,20260905+k))
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cpp',type=Path)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--extended',action='store_true')
    parser.add_argument('--probes',type=int,default=32)
    args = parser.parse_args()
    data = report(args.cpp,args.extended,args.probes)
    text = json.dumps(data,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text,encoding='utf-8')
    else:
        print(text,end='')

if __name__ == '__main__':
    main()
