#!/usr/bin/env python3
"""Exact author-level certificate for the one-step frozen trace-square extension.

Run: python3 -S verify_trace_variance.py --output-dir evidence
All arithmetic is integer or finite-field arithmetic. No float, eigenvalue,
asymptotic extrapolation, independent audit, or formal verification is claimed.
The all-order implication uses the separate proof in candidate_proof.md.
"""
from __future__ import annotations

if not __debug__:
    raise RuntimeError('Run without -O/-OO or PYTHONOPTIMIZE.')

import argparse
from collections import defaultdict
import hashlib
import importlib.util
import json
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'source_snapshot' / 'frozen_antireversor.py'
SOURCE_SHA256 = '2bd246b21def724ef07c849cb507d4a18e904039307322164d095f40c5424e0f'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA256
spec = importlib.util.spec_from_file_location('pinned_antireversor', SOURCE)
f = importlib.util.module_from_spec(spec)
spec.loader.exec_module(f)


def Q(v):
    return 2*v[1]*v[1] - v[0]*v[0]


def build():
    """Build the integer Laurent polynomial from all 32^2 ordered pairs."""
    coeff = f.coefficients()
    poly = defaultdict(lambda: (0, 0))
    for v, c in coeff.items():
        for w, d in coeff.items():
            term = f.multiply(c, d)
            for e, s in [(Q(f.add(v, w)) + 2*f.omega(v, w), 1),
                         (Q(v) + Q(w), -1)]:
                poly[e] = f.gaussian_add(poly[e], (s*term[0], s*term[1]))
    assert all(c[1] == 0 for c in poly.values())
    return {e: c[0] for e, c in poly.items() if c[0]}


def verify_raw_symbol():
    """Own exact expansion of the original raw trigonometric symbol.

    This is a second assembly check in the same author-level run, not an
    independently audited implementation or a new quantization convention.
    """
    raw = defaultdict(lambda: (Fraction(0), Fraction(0)))
    def put(v, re=0, im=0):
        x, y = raw[v]
        raw[v] = (x+re, y+im)
    r = {0: Fraction(1), 1: Fraction(1, 2), -1: Fraction(1, 2),
         6: Fraction(-1, 4), -6: Fraction(-1, 4),
         7: Fraction(-1, 2), -7: Fraction(-1, 2),
         8: Fraction(-1, 4), -8: Fraction(-1, 4)}
    # cos(14*pi*q) + r(q)/10 + r(q)sin(2*pi*q)/100 - 1/10.
    put((0, 7), Fraction(1, 2))
    put((0, -7), Fraction(1, 2))
    put((0, 0), Fraction(-1, 10))
    for k, value in r.items():
        put((0, k), value/10)
        put((0, k+1), im=-value/200)
        put((0, k-1), im=value/200)
        # r(q)cos(2*pi*p-alpha)/100; cos alpha=-3/5, sin alpha=4/5.
        put((1, k), -3*value/1000, -4*value/1000)
        put((-1, k), -3*value/1000, 4*value/1000)
    scaled = {v: (4000*re, 4000*im) for v, (re, im) in raw.items()
              if re or im}
    assert scaled == f.coefficients()


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def monic_divmod(a, b):
    """Ascending coefficient arrays; exact division over Z by monic b."""
    a, b = trim(a), trim(b)
    assert b[-1] == 1
    q = [0] * max(1, len(a)-len(b)+1)
    while a != [0] and len(a) >= len(b):
        k, c = len(a)-len(b), a[-1]
        q[k] += c
        for j, d in enumerate(b):
            a[j+k] -= c*d
        a = trim(a)
    return trim(q), a


def convolution(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, c in enumerate(a):
        for j, d in enumerate(b):
            out[i+j] += c*d
    return trim(out)


def multiplicity_certificate(poly, factor):
    quotients = []
    while True:
        quotient, remainder = monic_divmod(poly, factor)
        if any(remainder):
            return {'multiplicity': len(quotients),
                    'quotients_ascending': quotients,
                    'first_nonzero_remainder_ascending': remainder}
        assert convolution(quotient, factor) == poly
        quotients.append(quotient)
        poly = quotient


def isprime(n):
    return n >= 2 and all(n % p for p in range(2, isqrt(n)+1))


def prime_factors(n):
    ps = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            ps.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        ps.append(n)
    return ps


def finite_field_control(N, poly):
    """Direct actual sparse B=4000A and dense-kernel trace contractions.

    The chosen p=1 mod 4N embeds both i and a primitive Nth root. This is
    a bounded exact control, not the proof that all complex N pass.
    """
    p = next(4*N*k+1 for k in range(1, 1000) if isprime(4*N*k+1))
    factors = prime_factors(p-1)
    generator = next(g for g in range(2, p)
                     if all(pow(g, (p-1)//q, p) != 1 for q in factors))
    imaginary = pow(generator, (p-1)//4, p)
    root = pow(generator, (p-1)//N, p)
    assert imaginary*imaginary % p == p-1
    assert pow(root, N, p) == 1
    assert all(pow(root, N//q, p) != 1 for q in prime_factors(N))
    powers = [pow(root, e, p) for e in range(N)]
    eN = lambda e: powers[e % N]
    h, inv4, inv8 = (pow(d, -1, N) for d in [2, 4, 8])
    K = lambda x, y: eN(-inv8*(3*x*x - 2*x*y + 3*y*y))
    G = sum(K(x, x) for x in range(N)) % p
    assert G != 0
    coeff = f.coefficients()
    B = []
    for x in range(N):
        row = defaultdict(int)
        for (a, b), (re, im) in coeff.items():
            row[(x+a) % N] += (re+imaginary*im)*eN(b*(x+h*a))
        B.append({y: c % p for y, c in row.items() if c % p})
    t1 = sum(c*K(y, x) for x, row in enumerate(B)
             for y, c in row.items()) % p
    t2 = sum(c*d*K(z, x) for x, row in enumerate(B)
             for y, c in row.items() for z, d in B[y].items()) % p
    target = sum(c*eN(inv4*e) for e, c in poly.items()) % p
    left = (G*t2-t1*t1) % p
    right = G*G*target % p
    assert left == right
    # Direct kernel trace character, with aliases retained for every mode.
    for a, b in coeff:
        direct = sum(eN(b*(x+h*a))*K((x+a) % N, x)
                     for x in range(N)) % p
        assert direct == G*eN(inv4*Q((a, b))) % p
    # Weyl product cocycle, checked at x=0; the x coefficients agree.
    for a, b in coeff:
        for c, d in coeff:
            lhs = b*h*a + d*(a+h*c)
            rhs = (b+d)*h*(a+c) + h*(a*d-b*c)
            assert (lhs-rhs) % N == 0
    if N == 7:
        assert all(row == {x: 3600 % p} for x, row in enumerate(B))
        assert left == 0
    return {'N': N, 'prime': p, 'generator': generator,
            'root': root, 'imaginary': imaginary,
            'G': G, 'trace_BK': t1, 'trace_B2K': t2,
            'G_trace_B2K_minus_trace_BK_squared': left,
            'G_squared_times_polynomial': right,
            'polynomial_value': target}


def raw_alias_control():
    """Exact Gaussian-integer aggregation; proves B_7=3600 I."""
    alias = defaultdict(lambda: (0, 0))
    for (a, b), c in f.coefficients().items():
        v = (a % 7, b % 7)
        alias[v] = f.gaussian_add(alias[v], c)
    alias = {v: c for v, c in alias.items() if c != (0, 0)}
    assert alias == {(0, 0): (3600, 0)}
    return [{'mode': list(v), 'coefficient': list(c)}
            for v, c in sorted(alias.items())]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=ROOT/'evidence')
    args = parser.parse_args()
    verify_raw_symbol()
    poly = build()
    assert len(poly) == 143 and min(poly) == -36 and max(poly) == 648
    assert poly[-36] == -14 and poly[648] == -50
    assert gcd(*(abs(c) for c in poly.values())) == 2
    primitive = [poly.get(i-36, 0)//2 for i in range(685)]
    screens = [f.root_of_unity_screen(poly, flag) for flag in (False, True)]
    assert screens[0]['possible_cyclotomic_orders_mod_2'] == [1]
    assert screens[1]['possible_cyclotomic_orders_mod_2'] == [7]
    assert screens[0]['number_of_orders_tested'] == 373
    assert screens[1]['number_of_orders_tested'] == 73
    assert all(s['finite_upper_n'] == 1894 for s in screens)
    primitive_mod2 = sum(1 << j for j, c in enumerate(primitive) if c % 2)
    order_tests = []
    for n in range(1, 1895, 2):
        degree = f.euler_phi(n)
        if degree <= 684:
            residue = f.f2_remainder(primitive_mod2, f.phi_f2(n))
            order_tests.append({'order': n, 'totient': degree,
                                'remainder_F2_hex': hex(residue)})
    assert len(order_tests) == 446
    assert [r['order'] for r in order_tests
            if r['remainder_F2_hex'] == '0x0'] == [1, 7]
    division = {'1': multiplicity_certificate(primitive, [-1, 1]),
                '7': multiplicity_certificate(primitive, [1]*7)}
    assert all(v['multiplicity'] == 2 for v in division.values())
    factor = [1] + [0]*6 + [-2] + [0]*6 + [1]
    quotient, remainder = monic_divmod(primitive, factor)
    assert remainder == [0] and len(quotient) == 671
    assert convolution(quotient, factor) == primitive
    assert sum(quotient) == 2067702784
    dimensions = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 25, 35,
                  49, 63, 105, 147, 175, 245, 343, 1225]
    controls = [finite_field_control(N, poly) for N in dimensions]
    # A negative control ensures that the actual polynomial identity is used.
    altered = dict(poly)
    altered[0] = altered.get(0, 0)+1
    rejected = False
    try:
        finite_field_control(21, altered)
    except AssertionError:
        rejected = True
    assert rejected
    out = args.output_dir
    out.mkdir(parents=True, exist_ok=True)
    payloads = {
        'raw_coefficients.json': [
            {'mode': list(v), 'scaled_coefficient': list(c)}
            for v, c in sorted(f.coefficients().items())],
        'polynomial_sparse.json': sorted(poly.items()),
        'primitive_polynomial_ascending.json': primitive,
        'integer_cyclotomic_division.json': division,
        'quotient_by_z7_minus1_squared_ascending.json': quotient,
        'exact_finite_field_controls.json': controls,
        'all_odd_order_F2_remainders.json': order_tests,
    }
    for name, value in payloads.items():
        (out/name).write_text(json.dumps(value, indent=2)+'\n')
    (out/'polynomial_sparse.csv').write_text(
        'exponent,coefficient\n'+f.csv_body(poly))
    summary = {
        'arithmetic': 'Integer/Gaussian-integer exact assembly; F2 polynomial '
                      'divisions; monic Z divisions; bounded prime-field controls.',
        'non_claims': 'No independent audit, formalization, spectral simplicity, '
                      'quantitative trace or gap estimate, or BGS conclusion.',
        'ordered_pair_count': 1024,
        'original_raw_trigonometric_symbol_check': True,
        'nonzero_polynomial_terms': len(poly),
        'coefficient_l1': sum(abs(c) for c in poly.values()),
        'screens': screens,
        'exact_odd_cyclotomic_orders': [1, 7],
        'exact_multiplicities': {'1': 2, '7': 2},
        'N7_raw_alias': raw_alias_control(),
        'finite_field_dimensions': dimensions,
        'negative_polynomial_control_rejected': rejected,
        'source_sha256': SOURCE_SHA256,
        'generated_file_hashes': {
            name: hashlib.sha256((out/name).read_bytes()).hexdigest()
            for name in sorted(list(payloads)+['polynomial_sparse.csv'])},
    }
    (out/'certificate_summary.json').write_text(json.dumps(summary, indent=2)+'\n')
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
