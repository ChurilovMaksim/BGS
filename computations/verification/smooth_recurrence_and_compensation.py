#!/usr/bin/env python3
"""Independent finite tests for smooth_recurrence_and_compensation.md.

Rational Fourier-tail equalities are exact. Matrix exponentials and phases
are floating-point falsification tests, not interval certificates or proofs
of an asymptotic theorem. No finite spectrum is forced to a Gaussian fit.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
from typing import Iterable

import numpy as np

Vec = tuple[int, int]
ROOT = Path(__file__).resolve().parents[2]


def pell(k: int) -> tuple[int, int]:
    if k < 0:
        raise ValueError('Pell index must be nonnegative')
    n, f = 1, 0
    for _ in range(k):
        n, f = n + 2*f, n + f
    return n, f


def step(v: Vec, n: int | None = None) -> Vec:
    a, b = 3*v[0] + 2*v[1], 4*v[0] + 3*v[1]
    return (a, b) if n is None else (a % n, b % n)


def det(v: Vec, w: Vec) -> int:
    return v[0]*w[1] - v[1]*w[0]


def positive(v: Vec) -> Vec:
    return v if v[0] > 0 or (v[0] == 0 and v[1] > 0) else (-v[0], -v[1])


def physical_sign(v: Vec) -> int:
    # Never use (-1)**negative_integer in exact rational calculations.
    return -1 if (v[0]*v[1]) % 2 else 1


def rational_tail(k: int, radius: int, low: int) -> dict:
    """Check the exact scaled-average second moment, with alias controls."""
    n, _ = pell(k)
    modes = [(a, b) for a in range(-radius, radius+1)
             for b in range(-radius, radius+1)
             if 0 < a*a+b*b <= radius*radius and positive((a, b)) == (a, b)]
    parent = {v: v for v in modes}

    def find(v: Vec) -> Vec:
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    for v in modes:
        w = positive(step(v))
        if w in parent:
            parent[find(v)] = find(w)
    # Include all modes in the ball as vertices, even where the tail's
    # coefficient is zero: the intermediate orbit path may cross that region.
    groups = defaultdict(Fraction)
    modular = defaultdict(Fraction)
    norm1 = Fraction(0)
    for v in modes:
        square = v[0]*v[0] + v[1]*v[1]
        c = Fraction(1, (1+square)**4) if square > low*low else Fraction(0)
        groups[find(v)] += c
        norm1 += 2*abs(c)
        x = (v[0] % n, v[1] % n)
        for _ in range(k):
            for e in (-1, 1):
                modular[(e*x[0] % n, e*x[1] % n)] += c*physical_sign(v)
            x = step(x, n)
    second = sum((c*c for c in modular.values()), Fraction(0))/k
    variance = 2*sum((c*c for c in groups.values()), Fraction(0))
    assert isinstance(second, Fraction) and isinstance(variance, Fraction)
    # M=2R. lambda>5 and (1-lambda^-K)^2>81/100.
    cutoff = 81*5**((k+1)//2) > 6400*radius*radius
    if cutoff:
        assert second == variance
        assert variance <= norm1*norm1
    return {'K': k, 'N': str(n), 'radius': radius, 'low_cutoff': low,
            'sufficient_lifting_cutoff': cutoff,
            'exact_quantum_second': str(second), 'exact_orbit_variance': str(variance),
            'alias_difference': str(second-variance),
            'exact_equality': second == variance}


def pair_and_third(k: int) -> dict:
    """Original T-coordinate pairs and a genuinely nonzero mixed third moment."""
    n, _ = pell(k)
    orbits = []
    for seed in ((1, 0), (2, 4), (4, 4)):
        v = seed
        orbit = []
        for _ in range(k):
            orbit.append(v)
            v = step(v, n)
        assert v == seed
        orbits.append(orbit)
    bins = Counter()
    for t in range(k):
        for s in range(t+1, k):
            for a in range(3):
                for b in range(3):
                    v, w = orbits[a][t], orbits[b][s]
                    for e in (-1, 1):
                        for f in (-1, 1):
                            bins[(e*v[0]+f*w[0]) % n, (e*v[1]+f*w[1]) % n] += 1
    hist = Counter(bins.values())
    if k >= 23:
        assert (0, 0) not in bins
        assert max(hist) <= 34596
    half = pow(2, -1, n)
    norm = math.sqrt(2*k)
    atoms0 = [(e*v[0] % n, e*v[1] % n) for v in orbits[0] for e in (-1, 1)]
    convolution = defaultdict(complex)
    for v in atoms0:
        for w in atoms0:
            phase_index = det(v, w)*half % n
            if phase_index > n//2:
                phase_index -= n
            phase = np.exp(2j*np.pi*(phase_index/n))
            convolution[(v[0]+w[0]) % n, (v[1]+w[1]) % n] += phase/(2*k)
    thirds = []
    for species in (1, 2):
        value = sum(convolution[(-e*v[0] % n, -e*v[1] % n)]/norm
                    for v in orbits[species] for e in (-1, 1))
        reference = math.sqrt(2/k)*math.cos(4*math.pi/n)
        if k >= 23:
            assert abs(value-reference) < 2e-11
        thirds.append({'species': species, 'real': float(value.real),
                       'imaginary': float(value.imag), 'reference': reference,
                       'scaled_real': float(math.sqrt(k)*value.real)})
    return {'K': k, 'N': str(n), 'pair_count': 18*k*(k-1),
            'distinct_keys': len(bins), 'multiplicity_histogram': dict(sorted(hist.items())),
            'mixed_third_moments': thirds}


def expi(a: np.ndarray, x: float) -> np.ndarray:
    if np.linalg.norm(a-a.conj().T, 'fro') > 1e-9:
        raise AssertionError('Non-Hermitian generator')
    values, vectors = np.linalg.eigh(a)
    return (vectors*np.exp(1j*x*values)) @ vectors.conj().T


def moment(symbol: dict[Vec, Fraction | float], j: int) -> float:
    return sum(math.hypot(*v)**j*abs(float(c)) for v, c in symbol.items())


def symbol_data() -> tuple[dict, dict, dict]:
    g = {}
    for v, c in (((1, 0), Fraction(1)), ((0, 1), Fraction(1, 3)),
                 ((1, 1), Fraction(1, 5))):
        g[v] = g[(-v[0], -v[1])] = c
    d = {step(v): c for v, c in g.items()}
    r_over_pi = defaultdict(Fraction)
    for v, cv in g.items():
        for w, cw in d.items():
            r_over_pi[v[0]+w[0], v[1]+w[1]] -= det(v, w)*cv*cw
    r_over_pi = {v: c for v, c in r_over_pi.items() if c}
    assert r_over_pi.get((0, 0), Fraction(0)) == 0
    assert all(r_over_pi.get((-v[0], -v[1])) == c for v, c in r_over_pi.items())
    return g, d, r_over_pi


def operator_checks(k: int) -> dict:
    if k not in (3, 5, 7):
        raise ValueError('Dense reference restricted to K=3,5,7')
    n, f = pell(k)
    s = pow(f, -1, n)
    h = (3+2*s) % n
    half = pow(2, -1, n)
    x = np.arange(n)
    dimension = (n-1)//2
    basis = np.zeros((n, dimension))
    for j in range(1, dimension+1):
        basis[j, j-1] = 1/math.sqrt(2)
        basis[-j, j-1] = -1/math.sqrt(2)
    u_full = np.eye(n, dtype=complex)[(h*x) % n]
    u = basis.T @ u_full @ basis
    assert np.linalg.norm(np.linalg.matrix_power(u, k)-np.eye(dimension)) < 1e-10

    def quantize(symbol: dict) -> np.ndarray:
        result = np.zeros((n, n), dtype=complex)
        for (a, b), c in symbol.items():
            # Exact original-to-diagonal symplectic transformation.
            aa, bb = (-f*a-half*b) % n, (a-f*b) % n
            powers = aa*(x-bb*half) % n
            result[x, (x-bb) % n] += float(c)*physical_sign((a, b))*np.exp(2j*np.pi*powers/n)
        return basis.T @ result @ basis

    g, d, rational_r = symbol_data()
    r = {v: math.pi*float(c) for v, c in rational_r.items()}
    a, dd, rr = quantize(g), quantize(d), quantize(r)
    assert np.linalg.norm(dd-u@a@u.conj().T) < 1e-9
    q = a@dd-dd@a
    bracket_error = float(np.linalg.norm(q+2j*rr/n, 2))
    bracket_bound = math.pi**3*moment(g, 3)*moment(d, 3)/(3*n**3)
    assert bracket_error <= bracket_bound+1e-9
    hstar = moment(g, 2)*moment(d, 1)+moment(g, 1)*moment(d, 2)
    la, ld = 4*math.pi**2*moment(g, 1)*hstar, 4*math.pi**2*moment(d, 1)*hstar
    assert np.linalg.norm(a@q-q@a, 2) <= la/n**2+1e-9
    assert np.linalg.norm(dd@q-q@dd, 2) <= ld/n**2+1e-9
    c3 = la/2+ld/6
    c2 = math.pi**3*moment(g, 3)*moment(d, 3)/6
    cross = math.pi*moment(r, 1)*(3*moment(g, 1)+moment(d, 1))
    rows = []
    parameters = [(0., .25, 1), (.4, .25, 1), (-.25, .25, 1),
                  (-.25, .25, -1), (0., 1., 1)]
    for epsilon in (.025, .05, .1):
        t = epsilon*epsilon*math.sqrt(k)/n
        parameters.extend([(0., t, 1), (-t, t, 1), (-t, t, -1)])
    for ordinary, t, sign in parameters:
        epsilon = sign*math.sqrt(t*n/math.sqrt(k))
        eta = ordinary/math.sqrt(k)
        actual = expi(epsilon*(a-dd)+eta*rr, 1) @ u
        gauge = expi(a, -epsilon)
        target = expi(rr, eta+epsilon*epsilon/n) @ u
        error = float(np.linalg.norm(gauge@actual@gauge.conj().T-target, 2))
        # F=R, so the final effective exponentials commute exactly.
        bound = c3*abs(epsilon)**3/n**2+c2*epsilon**2/n**3+cross*abs(epsilon*eta)/n
        assert error <= bound+1e-8
        recurrence = np.trace(np.linalg.matrix_power(actual, k))/dimension
        rows.append({'a': ordinary, 't': t, 'epsilon': epsilon,
                     'operator_error': error, 'analytic_bound': bound,
                     'bound_below_one_tenth': bound < .1,
                     'is_compensated': ordinary == -t,
                     'actual_recurrence_real': float(recurrence.real),
                     'actual_recurrence_imaginary': float(recurrence.imag)})
    assert sum(row['bound_below_one_tenth'] for row in rows) >= 3
    return {'K': k, 'N': n, 'dimension': dimension,
            'bracket_error': bracket_error, 'bracket_bound': bracket_bound,
            'operator_checks': rows}


def report() -> dict:
    tails = [rational_tail(k, radius, low)
             for k in (3, 5, 11, 23, 47) for radius in (2, 4, 8) for low in (0, 1)]
    assert any(not r['exact_equality'] for r in tails if not r['sufficient_lifting_cutoff'])
    return {'producer': 'computations/verification/smooth_recurrence_and_compensation.py',
            'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'status': 'PASS',
            'scope': 'Exact rational finite Fourier tails and integer pair classes; numerical phases and matrix exponentials are separate finite falsifiers, not interval or asymptotic proofs.',
            'rational_tail_checks': tails,
            'pair_and_third_checks': [pair_and_third(k) for k in (3, 11, 23, 47)],
            'matrix_checks': [operator_checks(k) for k in (3, 5, 7)]}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    data = report()  # no PASS file is written before all assertions finish
    text = json.dumps(data, indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding='utf-8')
    else:
        print(text, end='')


if __name__ == '__main__':
    main()
