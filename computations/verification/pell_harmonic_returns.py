#!/usr/bin/env python3
"""Exact diagram/arithmetic controls and independent finite return matrices.

This finite computation does not prove asymptotic phase averaging or BGS.
Run with OPENBLAS_NUM_THREADS=1; output JSON separates exact and floating checks.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
import itertools
import json
import math
from pathlib import Path
import platform
import time

import numpy as np
from pell_harmonic_transition import design, pell, pell_phase


def crossing_edges(types):
    endpoints = sorted((cycle, i) for i, pair in enumerate(types) for cycle in pair)
    slots = [[j for j, (_, label) in enumerate(endpoints) if label == i]
             for i in range(len(types))]
    return [(i, j) for i in range(len(types)) for j in range(i+1, len(types))
            if ((slots[i][0] < slots[j][0] < slots[i][1] < slots[j][1])
                or (slots[j][0] < slots[i][0] < slots[j][1] < slots[i][1]))]


def exact_diagrams():
    rows = []
    word_count = 0
    n, f, _, h = design(11)
    inv2 = pow(2, -1, n)
    for m in range(1, 6):
        choices = tuple(itertools.combinations(range(m), 2))
        for ell in range(0, min(m, 4)+1):
            count = 0
            for types in itertools.product(choices, repeat=ell):
                cross = crossing_edges(types)
                count += not cross
                # A genuinely ordered word: label order is NOT first-endpoint order.
                # The phase formula must orient crossing edges by first endpoint.
                if ell == 0:
                    continue
                endpoints = sorted((cycle, i) for i, pair in enumerate(types)
                                   for cycle in pair)
                first = {i: endpoints.index((types[i][0], i)) for i in range(ell)}
                labels = [j*j % 11 for j in range(ell)]
                for signs in itertools.product((-1, 1), repeat=ell):
                    x = y = phase = 0
                    for cycle, i in endpoints:
                        sign = signs[i] if cycle == types[i][0] else -signs[i]
                        vx = -4*f*sign*pow(h, labels[i], n) % n
                        vy = sign*pow(h, -labels[i], n) % n
                        phase = (phase+(x*vy-y*vx)*inv2) % n
                        x, y = (x+vx) % n, (y+vy) % n
                    assert x == y == 0
                    predicted = 0
                    for i, j in cross:
                        if first[i] > first[j]:
                            i, j = j, i
                        predicted -= 4*signs[i]*signs[j]*pell_phase(labels[j]-labels[i], 11)
                    assert (phase-predicted) % n == 0
                    word_count += 1
            expected = (1 if ell == 0 else
                        m**(ell-1)*math.comb(m, ell+1) if ell < m else 0)
            assert count == expected
            rows.append({"m": m, "ell": ell, "noncrossing": count})
    # Independent recurrence using exact rational arithmetic; no diagram calls.
    counts = {(m, 0): Fraction(1) for m in range(1, 13)}
    for m in range(1, 13):
        for ell in range(1, 13):
            value = Fraction(m, 2)*sum(
                math.comb(ell-1, p)*counts.get((j, p), 0)
                *counts.get((m-j, ell-1-p), 0)
                for j in range(1, m) for p in range(ell))
            counts[m, ell] = value
            expected = m**(ell-1)*math.comb(m, ell+1) if ell < m else 0
            assert value == expected
    return {"enumerated_counts": rows, "exact_ordered_Weyl_words": word_count,
            "rational_recurrence_checks": 144}


def exact_lattice():
    count = 0
    for k in (3, 5, 7):
        n, _, _, h = design(k)
        for q in itertools.product((-1, 0, 1), repeat=k):
            c = [q[(j-2) % k]-6*q[(j-1) % k]+q[j] for j in range(k)]
            assert sum(map(abs, c)) >= 4*sum(map(abs, q))
            assert sum(c[j]*pow(h, j, n) for j in range(k)) % n == 0
            assert sum(c[j]*pow(h, -j, n) for j in range(k)) % n == 0
            count += 1
    cutoffs = []
    for k in (19, 31, 61, 127):
        n, _ = pell(k)
        r = 0
        while (r+1)**3 <= k*k:
            r += 1
        degree = k-(k+r-1)//r
        q, p = pell(2*degree)
        # sqrt(2)<99/70 (9800<9801); 3/2 is too coarse at K=19.
        assert r*r*(70*q+99*p) < 70*n*n
        cutoffs.append({"K": k, "R0": r, "degree": degree})
    return {"cyclic_integer_vectors": count, "rational_lifting_cutoffs": cutoffs}


def bessel(n, x):
    """J_n(2*x), via an absolutely convergent scalar series in this finite range."""
    sign = -1 if n < 0 and (-n) % 2 else 1
    n = abs(n)
    term = x**n/math.factorial(n)
    total = term
    for j in range(1, 100):
        term *= -x*x/(j*(n+j))
        total += term
        if abs(term) < 1e-20:
            break
    return sign*total


def odd_operators(k, a):
    n, f, _, h = design(k)
    d = (n-1)//2
    basis = np.zeros((n, d))
    for x in range(1, d+1):
        basis[x, x-1] = 1/math.sqrt(2)
        basis[-x, x-1] = -1/math.sqrt(2)
    w = np.zeros((n, n), complex)
    q = -a*a*f % n
    for x in range(n):
        w[x, (x-1) % n] = np.exp(2j*np.pi*(q*(x-pow(2, -1, n)) % n)/n)
    b = basis.T @ (w+w.conj().T) @ basis
    # S_h^-1 f(x)=f(h*x).
    u = basis.T @ basis[(h*np.arange(n)) % n]
    assert np.max(np.abs(u.conj().T @ u-np.eye(d))) < 1e-12
    return b, u


def bessel_word_trace(k, a, epsilon, m, cutoff):
    """Independent full Weyl-algebra dynamic expansion; no matrix multiplications."""
    n, f, _, h = design(k)
    inv2 = pow(2, -1, n)
    state = {(0, 0, 0): 1+0j}
    coeff = {z: (1j)**z*bessel(z, epsilon) for z in range(-cutoff, cutoff+1)}
    for j in list(range(k))*m:
        vx, vy = -a*a*f*pow(h, j, n) % n, pow(h, -j, n)
        nxt = defaultdict(complex)
        for (x, y, phase), value in state.items():
            for z, c in coeff.items():
                key = ((x+z*vx) % n, (y+z*vy) % n,
                       (phase+z*(x*vy-y*vx)*inv2) % n)
                nxt[key] += value*c
        state = nxt
    result = sum(value*np.exp(2j*np.pi*phase/n)*((n if x == y == 0 else 0)-1)/(n-1)
                 for (x, y, phase), value in state.items())
    # Simple certified analytic upper bound on omitted absolute coefficient mass.
    delta = abs(epsilon)
    first = delta**(cutoff+1)/math.factorial(cutoff+1)
    scalar_tail = 2*math.exp(delta*delta)*first/(1-delta/(cutoff+2))
    error_bound = m*k*scalar_tail*math.exp(2*delta*(m*k-1))
    return result, error_bound


def matrix_checks():
    rows = []
    for k, m, cutoff in ((3, 1, 7), (3, 2, 7), (5, 1, 5)):
        for a in (1, 2):
            epsilon = 0.23
            b, u0 = odd_operators(k, a)
            eig, vectors = np.linalg.eigh(b)
            kick = (vectors*np.exp(1j*epsilon*eig)) @ vectors.conj().T
            actual = np.trace(np.linalg.matrix_power(kick @ u0, m*k))/len(b)
            expanded, bound = bessel_word_trace(k, a, epsilon, m, cutoff)
            error = abs(actual-expanded)
            assert error <= bound+3e-12
            rows.append({"K": k, "m": m, "a": a, "coefficient_cutoff": cutoff,
                         "matrix_real": float(actual.real),
                         "matrix_imag": float(actual.imag),
                         "absolute_error": float(error),
                         "analytic_truncation_bound": bound})
    return rows


def clique_checks():
    count = 0
    for size in (7, 11, 17):
        for radius in range(1, (size-1)//3+1):
            for ell in (2, 3, 4):
                for pts in itertools.combinations(range(size), ell):
                    close = all(min((x-y) % size, (y-x) % size) <= radius
                                for x, y in itertools.combinations(pts, 2))
                    covers = sum(all((x-start) % size <= radius for x in pts)
                                 for start in pts)
                    assert covers == int(close)
                    count += 1
    return {"exact_distinct_circle_subsets": count}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    start = time.monotonic()
    result = {"scope": "Finite exact diagram/lattice checks and floating return-matrix controls; not an asymptotic proof.",
              "python": platform.python_version(), "numpy": np.__version__,
              "exact_diagrams": exact_diagrams(), "exact_lattice": exact_lattice(),
              "exact_cliques": clique_checks(), "floating_matrices": matrix_checks()}
    result["elapsed_seconds"] = time.monotonic()-start
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")


if __name__ == "__main__":
    main()
