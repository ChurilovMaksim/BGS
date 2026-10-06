"""Exact finite certificates; generators are checked by a separate replay.

No floating eigenvalues are used. A certificate proves a squarefree
characteristic polynomial of G+E modulo p. The theorem in the accompanying
note then proves simplicity at EVERY nonzero algebraic real exponent
epsilon, including tau*N for the frozen tau=10^-80, at the certified N.
"""

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import argparse
import hashlib
import json
from pathlib import Path
import time

import numpy as np

from exact_coefficients import average_coefficients, check_coefficients


def prime(n):
    if n < 2:
        return False
    d = 2
    while d*d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def factors(n):
    out = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def primitive_root(p):
    ff = factors(p-1)
    return next(g for g in range(2, p) if all(pow(g, (p-1)//q, p) != 1 for q in ff))


def construct(n, ordinary=False, p=None, weight=1):
    r, coeff = average_coefficients(n, ordinary)
    if p is None:
        p = 4*n+1
        while not prime(p) or (4000*r*n) % p == 0:
            p += 4*n
    assert prime(p) and (p-1) % (4*n) == 0 and (4000*r*n) % p != 0
    assert n*(p-1)**2 < 2**63-1, 'int64 matrix-vector sum could overflow'
    g = primitive_root(p)
    gamma = pow(g, (p-1)//(4*n), p)
    zeta, imag = pow(gamma, 4, p), pow(gamma, n, p)
    assert pow(imag, 2, p) == p-1
    assert pow(zeta, n, p) == 1
    assert all(pow(zeta, n//q, p) != 1 for q in factors(n))
    table = np.array([pow(zeta, j, p) for j in range(n)], dtype=np.int64)
    x = np.arange(n, dtype=np.int64)
    phase = (-pow(8, -1, n)*(3*x[:, None]**2 - 2*x[:, None]*x[None, :]
                            + 3*x[None, :]**2)) % n
    G = table[phase]
    E = np.zeros((n, n), dtype=np.int64)
    def residue(q):
        return (q.numerator*pow(q.denominator, -1, p)) % p
    for (a, b), (re, im) in coeff.items():
        c = (residue(re)+imag*residue(im)) % p
        E[x, (x+a) % n] = (E[x, (x+a) % n]
                          + c*table[(b*(x+a*pow(2, -1, n))) % n]) % p
    return (G+weight*E) % p, {'N': n, 'ordinary_midpoint': ordinary,
                            'p': p, 'period': r, 'weight': weight,
                            'primitive_root': g, 'zeta_N': zeta, 'image_of_i': imag}


def trim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return a


def remainder(a, b, p):
    a, b = trim(a), trim(b)
    assert b
    inv = pow(int(b[-1]), -1, p)
    while len(a) >= len(b):
        factor = int(a[-1])*inv % p
        shift = len(a)-len(b)
        for j, c in enumerate(b):
            a[j+shift] = (int(a[j+shift])-factor*int(c)) % p
        a = trim(a)
    return a


def gcd(a, b, p):
    a, b = trim(a), trim(b)
    while b:
        a, b = b, remainder(a, b, p)
    if not a:
        return []
    inv = pow(int(a[-1]), -1, p)
    return [int(c)*inv % p for c in a]


def berlekamp_massey(s, p):
    """Candidate generator only; replay does not trust this algorithm."""
    C, B, L, distance, last = [1], [1], 0, 1, 1
    for n in range(len(s)):
        discrepancy = (s[n]+sum(C[i]*s[n-i] for i in range(1, L+1))) % p
        if discrepancy == 0:
            distance += 1
            continue
        old = C.copy()
        factor = discrepancy*pow(last, -1, p) % p
        C += [0]*max(0, len(B)+distance-len(C))
        for j, c in enumerate(B):
            C[j+distance] = (C[j+distance]-factor*c) % p
        if 2*L <= n:
            L, B, last, distance = n+1-L, old, discrepancy, 1
        else:
            distance += 1
    return C[:L+1]


def replay(certificate):
    n, p = certificate['N'], certificate['p']
    matrix, metadata = construct(n, certificate['ordinary_midpoint'], p, certificate['weight'])
    assert all(certificate[k] == value for k, value in metadata.items())
    C = certificate['recurrence_descending']
    assert len(C) == n+1 and C[0] == 1 and all(0 <= c < p for c in C)
    u = np.array(certificate['u'], dtype=np.int64)
    v = np.array(certificate['v'], dtype=np.int64)
    assert u.shape == v.shape == (n,) and np.all((0 <= u) & (u < p))
    assert np.all((0 <= v) & (v < p))
    total = np.zeros(n, dtype=np.int64)
    moments = []
    # q(B)v=0, verified directly and exactly, without trusting the generator.
    for k in range(n+1):
        total = (total+C[n-k]*v) % p
        if k < n:
            moments.append(int(u@v) % p)
            v = (matrix@v) % p
    assert not np.any(total), 'annihilator residual is nonzero'
    numerator_desc = [sum(C[i]*moments[k-i] for i in range(k+1)) % p
                      for k in range(n)]
    q = list(reversed(C))
    numerator = list(reversed(numerator_desc))
    # q(B)v=0 implies u^T(tI-B)^(-1)v=numerator(t)/q(t).
    # Coprimality forces q to divide chi_B; equal degree makes them equal.
    assert gcd(q, numerator, p) == [1], 'the scalar resolvent was not cyclic'
    derivative = [j*q[j] % p for j in range(1, len(q))]
    assert gcd(q, derivative, p) == [1], 'characteristic polynomial not squarefree'
    return {'N': n, 'ordinary_midpoint': certificate['ordinary_midpoint'],
            'p': p, 'period': certificate['period'],
            'characteristic_degree': n, 'annihilator_residual_zero': True,
            'resolvent_coprime': True, 'squarefree': True}


def generate(n, ordinary=False, p=None, weight=1):
    matrix, metadata = construct(n, ordinary, p, weight)
    p = metadata['p']
    rng = np.random.default_rng(72000+n+int(ordinary)+p+weight)
    u = rng.integers(0, p, n, dtype=np.int64)
    v0 = rng.integers(0, p, n, dtype=np.int64)
    v, moments = v0.copy(), []
    for k in range(2*n):
        moments.append(int(u@v) % p)
        v = (matrix@v) % p
    C = berlekamp_massey(moments, p)
    return {**metadata, 'u': u.tolist(), 'v': v0.tolist(),
            'recurrence_descending': C}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--largest', type=int, default=1393)
    parser.add_argument('--replay', action='store_true')
    args = parser.parse_args()
    folder = Path(__file__).resolve().parent
    start = time.monotonic()
    if args.replay:
        certs = json.loads((folder/'certificates.json').read_text())['certificates']
        for c in certs:
            print(json.dumps(replay(c)), flush=True)
        return
    exact = check_coefficients()
    (folder/'coefficient_checks.json').write_text(json.dumps(exact, indent=2)+'\n')
    certs, results, failed_candidates = [], [], []
    cases = [(n, False) for n in (3, 5, 9, 15, 21, 41, 239, 1393) if n <= args.largest]
    cases += [(7, True), (41, True)]
    for n, ordinary in cases:
        print(json.dumps({'stage': 'generating', 'N': n, 'ordinary_midpoint': ordinary}), flush=True)
        p = 4*n+1
        success = False
        for attempt in range(4):
            r = average_coefficients(n, ordinary)[0]
            while not prime(p) or (4000*r*n) % p == 0:
                p += 4*n
            for weight in (1, 2):
                c = generate(n, ordinary, p, weight)
                try:
                    result = replay(c)
                except AssertionError as error:
                    failed_candidates.append({'N': n, 'ordinary_midpoint': ordinary,
                                              'p': p, 'weight': weight,
                                              'candidate_degree': len(c['recurrence_descending'])-1,
                                              'reason': str(error) or 'candidate degree was not N'})
                else:
                    success = True
                    break
            if success:
                break
            p += 4*n
        assert success, f'No certificate found at N={n}; no simplicity conclusion follows'
        certs.append(c)
        results.append(result)
        (folder/'certificates.json').write_text(json.dumps({'certificates': certs}, indent=2)+'\n')
        print(json.dumps(result), flush=True)
    bad = generate(7, False)
    assert len(bad['recurrence_descending']) < 8, 'the true N=7 exception was missed'
    try:
        replay(bad)
    except AssertionError:
        rejected_exception = True
    else:
        raise AssertionError('false simplicity certificate was accepted')
    bad = dict(certs[0])
    bad['recurrence_descending'] = bad['recurrence_descending'].copy()
    bad['recurrence_descending'][-1] = (bad['recurrence_descending'][-1]+1) % bad['p']
    try:
        replay(bad)
    except AssertionError:
        rejected_corruption = True
    else:
        raise AssertionError('corrupt certificate was accepted')
    output = {'status': 'completed', 'results': results, 'failed_candidates': failed_candidates,
              'raw_N7_rejected': rejected_exception, 'corrupt_polynomial_rejected': rejected_corruption,
              'elapsed_seconds': time.monotonic()-start,
              'certificate_sha256': hashlib.sha256((folder/'certificates.json').read_bytes()).hexdigest(),
              'scope': 'Exact finite simplicity certificates, not an all-N simplicity or BGS theorem'}
    (folder/'simple_spectrum.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(output), flush=True)


if __name__ == '__main__':
    main()
