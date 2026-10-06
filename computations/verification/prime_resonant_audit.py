#!/usr/bin/env python3
"""Exact prime-orbit arithmetic and finite resonant-block controls.

Inputs: unchanged symbol via the prior audited Laurent reconstruction;
all odd primes <=2000; complex128 matrices p=19,23,29,31 at control
kick time t=0.137, NOT physical 1e-80*p. No random samples.
Spectral comb controls use abstract powers d=3,7,10, not cat orders.
Exact Gaussian rationals and numerical diagnostics are kept separate.
No asymptotic block cancellation, priority or BGS certification.
"""

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import argparse
import hashlib
import json
import platform
from pathlib import Path
import numpy as np
import sympy as sp
from heisenberg_note_audit import symbol_check

ROOT = Path(__file__).resolve().parents[2]
S = (3, 4, 2, 3)
I = (1, 0, 0, 1)


def mul(a, b, modulus=None):
    out = (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
           a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3])
    return tuple(x % modulus for x in out) if modulus else out


def power(a, exponent, modulus=None):
    ans = I
    while exponent:
        if exponent & 1:
            ans = mul(ans, a, modulus)
        a = mul(a, a, modulus)
        exponent //= 2
    return ans


def order(p):
    chi = 1 if pow(2, (p-1)//2, p) == 1 else -1
    d = p-chi
    for divisor in map(int, sp.factorint(d)):
        while d % divisor == 0 and power(S, d//divisor, p) == I:
            d //= divisor
    assert power(S, d, p) == I
    return d, chi


def orbit(p, start):
    out, seen, v = [], set(), start
    while v not in seen:
        seen.add(v)
        out.append(v)
        a, b = v
        v = ((3*a+4*b) % p, (2*a+3*b) % p)
    assert v == start
    return out


def arithmetic_checks(raw):
    a, b = sp.symbols('a b')
    Q = lambda v: v[0]**2-2*v[1]**2
    assert sp.expand(Q((3*a+4*b, 2*a+3*b))-Q((a, b))) == 0
    assert sp.expand(a*(2*a+3*b)-b*(3*a+4*b)) == 2*Q((a, b))
    assert sp.expand(a*(-2*a+3*b)-b*(3*a-4*b)) == -2*Q((a, b))
    assert sp.det(sp.Matrix([[4, 4], [2, 4]])) == 8
    differences = {v: v+98 for v in sorted(set(Q(v) for v in raw)) if v != -98}
    candidates = set()
    for value in differences.values():
        candidates.update(map(int, sp.factorint(abs(value))))
    assert candidates == {2, 3, 5, 11, 13, 29, 97}
    negative_mass = sum(-sp.re(c) for c in raw.values() if sp.re(c) < 0)
    assert negative_mass == sp.Rational(14, 125)
    assert sum(abs(c) for c in raw.values()) == sp.Rational(19, 20)+sp.sqrt(101)/50
    rows, primes = [], list(map(int, sp.primerange(3, 2001)))
    for p in primes:
        d, chi = order(p)
        q = (p-chi)//d
        assert (p-chi) % d == 0
        assert (chi == 1 and q % 2 == 0) or (chi == -1 and q % 2 == 1)
        integral = power(S, d)
        determinant_abs = integral[0]+integral[3]-2
        assert determinant_abs >= p*p and determinant_abs % (p*p) == 0
        if p >= 19:
            orb = orbit(p, (0, 7))
            assert len(orb) == d
            orbit_set = set(orb)
            supported = sorted(v for v in raw if (v[0] % p, v[1] % p) in orbit_set)
            total = sp.simplify(sum(raw[v] for v in supported))
            assert sp.re(total) >= sp.Rational(169, 500)
            if p not in (29, 97):
                assert supported in ([(0, 7)], [(0, -7), (0, 7)])
                assert total in (sp.Rational(9, 20), sp.Rational(9, 10))
            if p == 29:
                assert total == sp.Rational(903, 1000)
            if p == 97:
                assert total == sp.Rational(9, 10)
            rows.append({'p': p, 'd': d, 'chi': chi, 'q': q,
                         'orbit_sum': str(total), 'support': [list(v) for v in supported]})
    assert pow(31, 48, 97) == 1
    assert all(pow(31, 48//int(v), 97) != 1 for v in sp.factorint(48))
    assert pow(13, 48, 97) == pow(15, 48, 97) == 96
    assert pow(31, 24, 97) == 96
    return {'order_primes_checked': len(primes), 'prime_cap': 2000,
            'candidate_primes': sorted(candidates), 'selected_invariant': -98,
            'differences': differences, 'negative_real_mass': str(negative_mass),
            'orbit_rows': rows}


def direct_matrices(p):
    j = np.arange(p)
    q = j/p
    r = lambda x: (1-np.cos(14*np.pi*x))*(1+np.cos(2*np.pi*x))
    v = np.cos(14*np.pi*q)+r(q)/10+r(q)*np.sin(2*np.pi*q)/100-.1
    edge = (-3-4j)/5*r((j+pow(2, -1, p))/p)/200
    A = np.diag(v).astype(complex)
    A[j, (j+1) % p] = edge
    A[(j+1) % p, j] = edge.conjugate()
    xx, yy = np.meshgrid(j, j, indexing='ij')
    residue = (-pow(8, -1, p)*(3*xx*xx-2*xx*yy+3*yy*yy)) % p
    M = np.exp(2j*np.pi*residue/p)/np.sqrt(p)
    return A, M


def matrix_checks():
    rows = []
    for p in (19, 23, 29, 31):
        d, _ = order(p)
        A, M = direct_matrices(p)
        values, vectors = np.linalg.eigh(A)
        t = .137
        B = (vectors*np.exp(1j*t*values))@vectors.conj().T
        U = B@M
        C = np.eye(p, dtype=complex)
        inverse_C, J = C.copy(), C.copy()
        for _ in range(d):
            C = C@(J@B@J.conj().T)
            inverse_C = inverse_C@(J.conj().T@B@J)
            J = J@M
        zeta = np.trace(J)/p
        scalar_error = float(np.linalg.norm(J-zeta*np.eye(p), 2))
        exact_error = max(float(np.linalg.norm(np.linalg.matrix_power(U, d*r)
                          -zeta**r*np.linalg.matrix_power(C, r), 2)) for r in (1, 2, 3))
        covariance_error = float(np.linalg.norm(M@C@M.conj().T-B.conj().T@C@B, 2))
        wrong_error = float(np.linalg.norm(C-inverse_C, 2))
        assert scalar_error < 3e-12 and exact_error < 3e-11 and covariance_error < 3e-12
        assert wrong_error > .01
        reverse_U = B@M.conj().T
        inverse_error = float(np.linalg.norm(np.linalg.matrix_power(reverse_U, d)
                             -zeta.conjugate()*inverse_C, 2))
        assert inverse_error < 3e-11
        trace_difference = abs(abs(np.trace(C))**2-abs(np.trace(inverse_C))**2)
        small_t = .005
        small_U = ((vectors*np.exp(1j*small_t*values))@vectors.conj().T)@M
        actual_mass = abs(np.trace(np.linalg.matrix_power(small_U, d)))**2/p**2
        x = d*small_t*(.95+np.sqrt(101)/50)
        floor = (1-x*x/2)**2
        assert actual_mass >= floor-1e-12
        rows.append({'p': p, 'd': d, 'control_t': t, 'scalar_error': scalar_error,
                     'powers_1_2_3_error': exact_error, 'cyclic_covariance_error': covariance_error,
                     'opposite_orientation_distance': wrong_error,
                     'opposite_orientation_trace_square_difference': float(trace_difference),
                     'inverse_map_block_error': inverse_error, 'small_control_t': small_t,
                     'small_t_trace_mass': float(actual_mass), 'small_t_coherent_floor': float(floor)})
    return rows


def fejer(L, x):
    return abs(sum(np.exp(2j*np.pi*s*x) for s in range(L)))**2/L


def spectral_checks():
    rows = []
    for p, d, L in ((19, 3, 4), (23, 7, 3), (31, 10, 2)):
        j = np.arange(p)
        for label, theta in (('clock', j/p), ('cluster', j/p**3),
                             ('deterministic_control', (j*j/(p*p)+.031*np.sin(j)) % 1)):
            phi = (d*theta) % 1
            delta = phi[:, None]-phi[None, :]
            G = float(np.sum(fejer(L, delta))/p**2)
            weighted = 1+2*sum((1-r/L)*abs(np.exp(2j*np.pi*r*phi).sum())**2/p**2
                              for r in range(1, L))
            original_delta = theta[:, None]-theta[None, :]
            comb = sum(np.sum(fejer(d*L, original_delta-h/d)) for h in range(d))/(d*p**2)
            error = max(abs(G-weighted), abs(G-comb))
            assert error < 2e-12
            R = L-1
            energy = sum(abs(np.exp(2j*np.pi*r*phi).sum())**2 for r in range(1, R+1))/p**2
            upper = float(np.sum(fejer(2*R+1, delta))/p**2)-1
            assert (G-1)/2 <= energy+2e-12 and energy <= upper+2e-12
            if label == 'clock':
                assert abs(energy) < 1e-25 and abs(G-1) < 1e-12
            if label == 'cluster':
                assert energy > .9*R
            rows.append({'p': p, 'd': d, 'L': L, 'spectrum': label, 'G': G,
                         'E_initial': float(energy), 'Fejer_upper': upper,
                         'trace_kernel_comb_error': float(error)})
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    ordinary, _ = symbol_check()
    # Python (-1)**negative_integer introduces a float; sp.Integer avoids it.
    raw = {(m, n): sp.Integer(-1)**(m*n)*c for (n, m), c in ordinary.items()}
    assert not any(c.has(sp.Float) for c in raw.values())
    data = {'status': 'PASS', 'date': '2026-09-30',
            'arithmetic': 'integer modular matrices and Gaussian rationals; complex128 controls separately',
            'python': platform.python_version(), 'sympy': sp.__version__, 'numpy': np.__version__,
            'arithmetic_checks': arithmetic_checks(raw), 'matrix_controls': matrix_checks(),
            'spectral_controls': spectral_checks(),
            'non_claims': ['frozen-coupling asymptotics', 'sector cancellation for the actual map',
                           'BGS solution', 'priority', 'external independent referee', 'Lean compilation']}
    sources = ['mathematics/prime_resonant_sector.md',
               'computations/verification/prime_resonant_audit.py',
               'computations/verification/heisenberg_note_audit.py']
    data['source_sha256'] = {s: hashlib.sha256((ROOT/s).read_bytes()).hexdigest() for s in sources}
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(data, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'odd_primes': data['arithmetic_checks']['order_primes_checked'],
                      'orbit_primes': len(data['arithmetic_checks']['orbit_rows']),
                      'matrix_controls': len(data['matrix_controls']),
                      'spectral_controls': len(data['spectral_controls'])}))


if __name__ == '__main__':
    main()
