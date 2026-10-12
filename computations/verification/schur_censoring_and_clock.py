#!/usr/bin/env python3
"""Exact finite energy/clock-word controls and separate floating feedback checks.

No finite calculation proves the stopped asymptotic theorems or BGS.
Runs are deterministic; the seed fixes diagnostic examples, not a probability law.
"""
from __future__ import annotations

if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from fractions import Fraction
from itertools import product
from math import comb, factorial
import argparse
import json
from pathlib import Path

import numpy as np
import sympy as sp


def rational_mix(n: int, trial: int) -> sp.Matrix:
    """Positive doubly stochastic matrices, including nonreversible examples."""
    p = sp.ones(n) / n
    for shift in range(n):
        perm = list(range(n))
        if (trial + shift) % 2:
            perm.reverse()
        perm = perm[shift:] + perm[:shift]
        weight = 1 + ((trial + 2) * (shift + 3)) % 7
        p += weight * sp.Matrix(n, n, lambda i, j: int(j == perm[i]))
    return p / sum(p[0, j] for j in range(n))


def exact_energy_controls() -> tuple[int, int]:
    cases = identities = 0
    for n in range(2, 9):
        for trial in range(5):
            p = rational_mix(n, trial)
            assert p * sp.ones(n, 1) == sp.ones(n, 1)
            assert p.T * sp.ones(n, 1) == sp.ones(n, 1)
            for a in range(1, n):
                deleted = n - a
                inverse = (sp.eye(deleted) - p[a:, a:]).inv()
                pc = p[:a, :a] + p[:a, a:] * inverse * p[a:, :a]
                assert pc * sp.ones(a, 1) == sp.ones(a, 1)
                assert pc.T * sp.ones(a, 1) == sp.ones(a, 1)
                x = sp.Matrix([((i + 1) * (trial + 2)) % 11 - 5 for i in range(a)])
                x -= sp.ones(a, 1) * sum(x) / a
                t = inverse * p[a:, :a] * x
                lift = x.col_join(t)
                lift -= sp.ones(n, 1) * sum(lift) / n
                q = p - sp.ones(n) / n
                for s2 in [sp.Rational(0), sp.Rational(1, 9), sp.Rational(1, 4),
                           sp.Rational(9, 16), sp.Rational(1)]:
                    left = (q * lift).dot(q * lift) - s2 * lift.dot(lift)
                    extra = t.dot(t) - sum(t) ** 2 / n
                    right = (pc * x).dot(pc * x) - s2 * x.dot(x) + (1 - s2) * extra
                    assert left == right
                    assert extra >= 0
                    identities += 1
                # The numerical singular-value comparison is explicitly diagnostic.
                sv = np.linalg.svd(np.array(q, dtype=float), compute_uv=False)
                svc = np.linalg.svd(np.array(pc - sp.ones(a) / a, dtype=float),
                                    compute_uv=False)
                assert np.all(svc[:a - 1] <= sv[:a - 1] + 2e-13)
                cases += 1
    return cases, identities


def compositions(n: int, parts: int):
    if parts == 1:
        yield (n,)
    else:
        for first in range(1, n - parts + 2):
            for tail in compositions(n - first, parts - 1):
                yield (first, *tail)


def fraction(value) -> Fraction:
    return Fraction(int(sp.numer(value)), int(sp.denom(value)))


def exact_clock_words() -> tuple[int, int]:
    """Every positive composition/orientation for k=2..7 in nine exact examples."""
    words = cases = 0
    for n in [2, 3, 4]:
        skew = sp.Matrix(n, n, lambda i, j: sp.Rational(i - j, n + 2))
        s = (sp.eye(n) - skew).inv() * (sp.eye(n) + skew)
        x = sp.Matrix(n, n, lambda i, j: (2 * i + 3 * j + i * j) % 5 - 2)
        t = sp.eye(n) + x.T * x
        assert s.T * s == sp.eye(n)
        assert s * t != t * s
        powers = [sp.eye(n)]
        for _ in range(7):
            powers.append(powers[-1] * t)
        for label in range(n):
            e = sp.eye(n)[:, label]
            v = s.T * e
            vec = [e, v]
            moments = {(degree, left, right):
                       fraction((vec[left].T * powers[degree] * vec[right])[0])
                       for degree in range(1, 8) for left in range(2) for right in range(2)}
            cap = max(moments[1, 0, 0], moments[1, 1, 1])
            for k in range(2, 8):
                for r in range(2, k + 1):
                    high = k - r + 1
                    for gaps in compositions(k, r):
                        for orientation in product(range(2), repeat=r):
                            value = Fraction(1)
                            eweight = Fraction(0)
                            for i in range(r):
                                # rank-one term i is |orientation_i><1-orientation_i|.
                                left = 1 - orientation[i - 1]
                                right = orientation[i]
                                degree = gaps[i]
                                value *= moments[degree, left, right]
                                count_e = int(left == 0) + int(right == 0)
                                eweight += (Fraction((degree - 1) * count_e, 2 * (high - 1))
                                            if high > 1 else Fraction(count_e, 2 * r))
                            assert 0 <= eweight <= 1
                            bound = cap ** (r - 1) * (
                                eweight * moments[high, 0, 0]
                                + (1 - eweight) * moments[high, 1, 1])
                            assert value * value <= bound * bound
                            words += 1
            cases += 1
    return cases, words


def canonical(matrix):
    return matrix.applyfunc(sp.expand)


def polynomial_multiply(left, right):
    result = {}
    for (r, s), a in left.items():
        for (t, v), b in right.items():
            key = (r + t, s + v)
            value = canonical(a * b)
            result[key] = canonical(result[key] + value) if key in result else value
    return result


def phase_moment(r, s, a):
    """Exact residue of w^(r-1)/((1-aw)^r(w-conj(a))^s)."""
    if r == s == 0:
        return sp.Integer(1)
    if not r or not s:
        return sp.Integer(0)
    abar = sp.conjugate(a)
    d = sp.expand(1 - a * abar)
    value = 0
    for j in range(min(r - 1, s - 1) + 1):
        degree = s - 1 - j
        rising = factorial(r + degree - 1) // factorial(r - 1)
        value += (sp.Rational(comb(r - 1, j) * rising, factorial(degree))
                  * abar ** (r - 1 - j) * a ** degree / d ** (r + degree))
    return sp.expand(value)


def phase_mean(polynomial, a):
    first = next(iter(polynomial.values()))
    result = sp.zeros(first.rows, first.cols)
    for (r, s), matrix in polynomial.items():
        result += matrix * phase_moment(r, s, a)
    return canonical(result)


def unitary_fixture(n, seed):
    s = sp.eye(n)
    for start in [range(n - 1), reversed(range(n - 1))]:
        for j in start:
            rotation = sp.eye(n)
            rotation[j, j] = rotation[j + 1, j + 1] = sp.Rational(3, 5)
            if (j + seed) % 2:
                rotation[j, j + 1] = rotation[j + 1, j] = 4 * sp.I / 5
            else:
                rotation[j, j + 1] = sp.Rational(4, 5)
                rotation[j + 1, j] = -sp.Rational(4, 5)
            s = canonical(rotation * s)
    phases = sp.diag(*[sp.I ** ((j + seed) % 4) for j in range(n)])
    return canonical(phases * s)


def exact_feedback_power_controls():
    cases = nonzero = gamma_checks = square_checks = quartic_checks = 0
    for n in [2, 3, 4]:
        for seed in [0, 1]:
            s = unitary_fixture(n, seed)
            assert canonical(s * s.H) == sp.eye(n)
            x = sp.Matrix(n, n, lambda i, j:
                          ((i + 2 * j + seed) % 5 - 2)
                          + sp.I * ((2 * i + j + seed) % 3 - 1))
            t = canonical(sp.eye(n) + x.H * x)
            assert canonical(s * t - t * s) != sp.zeros(n)
            for e in range(n):
                indices = [j for j in range(n) if j != e]
                b, c = s.extract([e], indices), s.extract(indices, [e])
                a, d = s[e, e], sp.expand(1 - abs(s[e, e]) ** 2)
                assert d > 0
                # K has retained coordinate columns; both factors are rectangular.
                selection = sp.eye(n).extract(range(n), indices)
                coordinate = sp.eye(n)[:, e]
                k = {(0, 0): selection, (1, 0): canonical(coordinate * b)}
                kh = {(v, r): matrix.H for (r, v), matrix in k.items()}
                tp = polynomial_multiply(polynomial_multiply(kh, {(0, 0): t}), k)
                powers = [None, tp]
                for _ in range(3):
                    powers.append(polynomial_multiply(powers[-1], tp))
                qmat = canonical(s * t * s.H)
                t2, t3, t4 = [canonical(t ** degree) for degree in [2, 3, 4]]
                q2, q3 = [canonical(qmat ** degree) for degree in [2, 3]]
                gamma, beta = canonical(s * t), canonical(s * t2)
                spoly = {(0, 0): s.extract(indices, indices),
                         (1, 0): canonical(c * b)}
                mean_gamma = phase_mean(polynomial_multiply(spoly, tp), a)
                assert mean_gamma == gamma.extract(indices, indices)
                gamma_checks += (n - 1) ** 2
                mean_square = phase_mean(powers[2], a)
                tt, ss, gg = t[e, e], qmat[e, e], gamma[e, e]
                for retained, j in enumerate(indices):
                    expected = (t2[j, j]
                                + (abs(s[e, j]) ** 2 * t2[e, e]
                                   + 2 * tt * sp.re(sp.conjugate(s[e, j]) * gamma[e, j])) / d
                                + 2 * abs(s[e, j]) ** 2 * tt
                                * sp.re(sp.conjugate(a) * gg) / d ** 2)
                    assert sp.expand(mean_square[retained, retained] - expected) == 0
                    square_checks += 1
                expected4 = (sp.trace(t4)
                             + 4 * (tt * q3[e, e] + t2[e, e] * q2[e, e]
                                    + ss * t3[e, e]) / d
                             + 8 * sp.re(sp.conjugate(a) *
                                         (gg * (ss * t2[e, e] + tt * q2[e, e])
                                          + tt * ss * beta[e, e])) / d ** 2
                             + (1 + abs(a) ** 2) *
                             (2 * tt ** 2 * ss ** 2 + 4 * tt * ss * abs(gg) ** 2) / d ** 3
                             + 8 * tt * ss * sp.re(sp.conjugate(a) ** 2 * gg ** 2) / d ** 3)
                assert sp.expand(sp.trace(phase_mean(powers[4], a)) - expected4) == 0
                quartic_checks += 1
                cases += 1
                nonzero += int(a != 0)
    return {"arithmetic": "exact Gaussian rationals via SymPy; phase integrals by residues",
            "dimensions": [2, 3, 4], "fixture_seeds": [0, 1],
            "cases": cases, "nonzero_deleted_diagonal_cases": nonzero,
            "mixed_clock_entries": gamma_checks, "diagonal_square_identities": square_checks,
            "fourth_trace_identities": quartic_checks}


def feedback_controls() -> dict:
    rng = np.random.default_rng(20261011)
    samples = phase_points = 0
    mean_error = 0.0
    for n in [3, 5, 8, 12]:
        for _ in range(6):
            z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
            s, r = np.linalg.qr(z)
            s = s @ np.diag(np.diag(r) / np.abs(np.diag(r)))
            a, c, b, aa = s[-1, -1], s[:-1, -1], s[-1, :-1], s[:-1, :-1]
            d = 1 - abs(a) ** 2
            delta = float(np.max(abs(s) ** 2))
            classical = abs(aa) ** 2 + np.outer(abs(c) ** 2, abs(b) ** 2) / d
            cc = np.diag(c) @ aa.conjugate() @ np.diag(b)
            rr = np.outer(abs(c) ** 2, abs(b) ** 2)
            phases = np.exp(2j * np.pi * np.arange(4096) / 4096)
            qs = phases / (1 - a * phases)
            feedback = aa[None, :, :] + qs[:, None, None] * np.outer(c, b)
            error = float(np.max(abs(np.mean(abs(feedback) ** 2, axis=0) - classical)))
            mean_error = max(mean_error, error)
            assert error < 2e-13
            for index in range(0, 4096, 128):
                q = qs[index]
                noise = abs(feedback[index]) ** 2 - classical
                expansion = q * cc + q.conjugate() * cc.conjugate() + (abs(q) ** 2 - 1 / d) * rr
                assert np.max(abs(noise - expansion)) < 2e-14
                assert np.linalg.norm(noise, 2) <= 4 * delta / (1 - np.sqrt(delta)) + 2e-13
                phase_points += 1
            samples += 1
    h = sp.Matrix([[1, 1, 1, 1], [1, -1, 1, -1],
                   [1, 1, -1, -1], [1, -1, -1, 1]]) / 2
    s1 = h[1:, 1:] + 2 * h[1:, :1] * h[:1, 1:]
    assert s1 == sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    return {'floating_unitaries': samples, 'floating_phase_points': phase_points,
            'maximum_quadrature_mean_error': mean_error, 'exact_walsh_mean_gap_falsifier': True}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='New result file; existing files are rejected.')
    args = parser.parse_args()
    cases, identities = exact_energy_controls()
    clock_cases, words = exact_clock_words()
    result = {'status': 'PASS', 'arithmetic': 'exact SymPy rationals and Python Fraction; separately float64',
              'exact_censoring_cases': cases, 'exact_lift_energy_identities': identities,
              'exact_noncommuting_clock_examples': clock_cases,
              'exact_clock_words': words, 'clock_orders': [2, 3, 4, 5, 6, 7],
              'exact_feedback_power_controls': exact_feedback_power_controls(),
              'diagnostics': feedback_controls(),
              'non_claims': ['asymptotic proof by finite computation', 'flatness probability',
                             'equality clock laws', 'BGS universality', 'worldwide priority']}
    serialized = json.dumps(result, indent=2) + '\n'
    if args.output:
        with args.output.open('x', encoding='utf-8') as stream:
            stream.write(serialized)
    print(serialized, end='')


if __name__ == '__main__':
    main()
