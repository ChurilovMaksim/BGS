#!/usr/bin/env python3
"""Finite controls for FLOW-010, not a stochastic/asymptotic certificate.

Deterministic seed; complex128; full real Hermitian basis for Frechet
gradients; all 16 words and three Wick pairings for the fourth mean.
No Monte Carlo, large-step-count simulation, or semigroup bound test.
"""
import argparse
import hashlib
import itertools
import json
import platform
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import expm_frechet


def basis(n):
    out = []
    for j in range(n):
        e = np.zeros((n, n), complex)
        e[j, j] = 1
        out.append(e)
    for j in range(n):
        for k in range(j + 1, n):
            e = np.zeros((n, n), complex)
            e[j, k] = e[k, j] = 1 / np.sqrt(2)
            out.append(e)
            e = np.zeros((n, n), complex)
            e[j, k] = 1j / np.sqrt(2)
            e[k, j] = -1j / np.sqrt(2)
            out.append(e)
    return np.array(out)


def fourth_mean(u):
    n = len(u)
    powers = {j: np.linalg.matrix_power(u, j) for j in range(-2, 3)}
    total = np.zeros_like(u)
    for word in itertools.product((0, 1), repeat=4):
        b0, b1, b2, b3 = word
        a, b, c = (powers[b1 - b0], powers[b2 - b1], powers[b3 - b2])
        contraction = (np.trace(a) * np.trace(c) * b + c @ b @ a
                       + np.trace(b) * np.trace(a @ c) * np.eye(n)) / n**2
        total += (-1)**sum(word) * powers[b0] @ contraction @ powers[-b3]
    return np.trace(total @ u) / (24 * n)


def exact_fourth_mean():
    # Monomial key contains nonzero normalized-trace exponents; m_0=1.
    out = defaultdict(Fraction)
    nonplanar = Fraction(0)
    for a, b, c, d in itertools.product((0, 1), repeat=4):
        coefficient = Fraction((-1)**(a+b+c+d), 24)
        for exponents in ((b-a, d-c, a+c-b-d+1),
                          (c-b, b-a+d-c, a-d+1)):
            key = tuple(sorted(j for j in exponents if j))
            out[key] += coefficient
        nonplanar += coefficient  # The common m_1/N^2 term cancels.
    out = {k: v for k, v in out.items() if v}
    expected = {(1,): Fraction(1, 8), (-1, 2): Fraction(-1, 6),
                (-2, 1, 2): Fraction(1, 24), (-1, 1, 1): Fraction(-1, 24),
                (-1, -1, 3): Fraction(1, 24)}
    assert out == expected and nonplanar == 0
    return {str(k): str(v) for k, v in sorted(out.items())}


def formula(u):
    n = len(u)
    x, q, r = (np.trace(np.linalg.matrix_power(u, j)) / n for j in (1, 2, 3))
    return x / 8 - q * x.conjugate() / 6 + (
        abs(q)**2 * x - abs(x)**2 * x + x.conjugate()**2 * r) / 24


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    seed = 20260930
    rng = np.random.default_rng(seed)
    cases = []
    for n in (3, 4, 5, 7, 9):
        bs = basis(n)
        fourier = np.exp(2j * np.pi * np.outer(np.arange(n), np.arange(n)) / n) / np.sqrt(n)
        for kind in ('clock', 'perturbed'):
            theta = 2 * np.pi * np.arange(n) / n
            if kind == 'perturbed':
                theta = theta + .19 * np.cos(theta) + .07 * np.sin(2 * theta)
            u = fourier @ np.diag(np.exp(1j * theta)) @ fourier.conj().T
            error = float(abs(fourth_mean(u) - formula(u)))
            assert error < 2e-14
            g = np.einsum('a,ajk->jk', rng.normal(size=n*n) / np.sqrt(n), bs)
            d = g - u @ g @ u.conj().T
            gradient = []
            for eps in (.01, .08, .25):
                coeff = np.array([
                    np.trace(expm_frechet(1j * eps * d,
                        1j * eps * (e - u @ e @ u.conj().T),
                        compute_expm=False) @ u) / n for e in bs])
                norm = float(np.linalg.norm(coeff))
                bound = float(8 * eps**2 * np.linalg.norm(g, 2) / np.sqrt(n))
                assert norm <= bound + 1e-13
                gradient.append({'epsilon': eps, 'gradient_norm': norm,
                                 'bound': bound, 'ratio': norm / bound})
            cases.append({'N': n, 'spectrum': kind,
                          'fourth_mean_error': error, 'gradient': gradient})
    report = {
        'status': 'PASS', 'date': '2026-09-30', 'seed': seed,
        'arithmetic': 'numpy complex128; scipy matrix-exponential Frechet derivative',
        'python': platform.python_version(), 'numpy': np.__version__,
        'scipy': scipy.__version__, 'cases': cases,
        'exact_fourth_coefficient': exact_fourth_mean(),
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'coverage': {'N': [3, 4, 5, 7, 9], 'spectra': ['clock', 'perturbed'],
                     'Wick_words': 16, 'pairings_per_word': 3,
                     'gradient_directions': 'full N^2 real Hermitian basis'},
        'exclusions': ['No joint-limit simulation', 'No numerical semigroup certificate',
                       'No independent proof review', 'No Lean compilation',
                       'No deterministic BGS theorem']}
    data = json.dumps(report, indent=2) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(data)
    print(data, end='')


if __name__ == '__main__':
    main()
