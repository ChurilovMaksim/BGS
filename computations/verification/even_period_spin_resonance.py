#!/usr/bin/env python3
"""Finite controls and sparse Monte Carlo for the even-period return theorem.

The exact checks are bounded. Monte Carlo estimates the analytically isolated
zero-aggregate term, with an explicit error bound for all omitted aggregates.
It does not diagonalize the enormous matrices in the sparse experiment.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from itertools import product
import json
import math
from pathlib import Path
import platform
import time

import mpmath as mp
import numpy as np
from pell_resonance_lattice import determinant


def recurrence(k):
    b = [0, 1]
    for _ in range(2, k+1):
        b.append(6*b[-1]-b[-2])
    return b


def g_bound(k, z):
    return math.expm1(5*k*z**8)+2*0.26**k+31*0.6**k


def exact_controls():
    rows, phase_checks = [], 0
    classes, pairs = set(), set()
    for r in range(16):
        for s in range(2):
            even, odd = (-3*r-s) % 16, (-r-3*s) % 16
            classes.add((even, odd))
            pairs.add(tuple(sorted((min(even, 16-even), min(odd, 16-odd)))))
    assert len(classes) == 32
    pairs.remove((0, 0))
    assert min(i+j for i, j in pairs) == 4
    x = Q(3, 4)
    h = lambda j: (x**j+x**(16-j))/(1-x**16)
    largest = max(h(i)*h(j) for i, j in pairs)
    assert largest == Q(10040323357589760, 28926125721773329)
    assert largest < Q(9, 25)
    z = Q(3, 10)
    activity_ratio = 4*(1+3*z**4)/((1-z**4)*(1-9*z**4))
    assert activity_ratio < 5
    assert 8*z**4/(1-z**4) < Q(13, 50)**2

    for k in (6, 10, 14, 18, 22):
        b = recurrence(k)
        n, a = b[k//2], (b[k//2]+1)//2
        assert n % 2 and 2*a*a % n == pow(2, -1, n)
        lap = [[-6*int(i == j)+int(i == (j-1) % k)+int(i == (j+1) % k)
                for j in range(k)] for i in range(k)]
        assert abs(determinant(lap)) == 32*n*n
        orbit, v = [], (1, 0)
        for _ in range(k):
            orbit.append(v)
            v = ((3*v[0]+4*v[1]) % n, (2*v[0]+3*v[1]) % n)
        assert v == (1, 0)
        for color in (0, 1):
            assert all(sum(orbit[j][c] for j in range(color, k, 2)) % n == 0
                       for c in (0, 1))
        for d in range(1, k):
            assert (b[d]+b[k-d]) % n == 0
            assert b[d] % 2 == d % 2
        if k == 6:
            for indices in product((-1, 0, 1), repeat=k):
                total, phase = [0, 0], 0
                for sign in (1, -1):
                    for index, vector in zip(indices, orbit):
                        w = [sign*index*a*q for q in vector]
                        phase += (total[0]*w[1]-total[1]*w[0])*pow(2, -1, n)
                        total = [(p+q) % n for p, q in zip(total, w)]
                assert total == [0, 0]
                expected = 2*a*a*sum(indices[i]*indices[j]*b[j-i]
                                    for i in range(k) for j in range(i+1, k))
                assert (phase-expected) % n == 0
                e, o = sum(indices[::2]), sum(indices[1::2])
                parity_phase = sum(indices[i]*indices[j]*(j-i)
                                   for i in range(k) for j in range(i+1, k))
                assert (parity_phase-e*o) % 2 == 0
                assert (-1)**(sum(indices)+parity_phase) == (
                    1 if e % 2 == o % 2 == 0 else -1)
                phase_checks += 1
        rows.append({"K": k, "N": n, "a": a, "central_quotient_order": 32})

    # This verifies the parity average for arbitrary one-site parity biases,
    # using exact rational probabilities, independently of the Bessel series.
    for bias in (Q(0), Q(1, 3), Q(4, 5), Q(1)):
        p0, p1 = (1+bias)/2, (1-bias)/2
        average = p0*p0-2*p0*p1-p1*p1
        assert average == -Q(1, 2)+bias+bias*bias/2
    rng = np.random.default_rng(611033)
    pauli = (np.array([[0, 1], [1, 0]], dtype=int),
             np.array([[1, 0], [0, -1]], dtype=int))
    multiple_block_checks = 0
    for k in (6, 10):
        b = recurrence(k)
        n, a = b[k//2], (b[k//2]+1)//2
        orbit, v = [], (1, 0)
        for _ in range(k):
            orbit.append(v)
            v = ((3*v[0]+4*v[1]) % n, (2*v[0]+3*v[1]) % n)
        for r in range(2, 7):
            for _ in range(100):
                indices = rng.integers(-1, 2, size=(r, k))
                indices[-1] = -indices[:-1].sum(axis=0)
                total, phase, spin = [0, 0], 0, np.eye(2, dtype=int)
                for row in indices:
                    for j, (value, vector) in enumerate(zip(row, orbit)):
                        w = [int(value)*a*q for q in vector]
                        phase += (total[0]*w[1]-total[1]*w[0])*pow(2, -1, n)
                        total = [(p+q) % n for p, q in zip(total, w)]
                        if value % 2:
                            spin = spin @ pauli[j % 2]
                predicted, parity = 0, 0
                for i in range(k):
                    for j in range(i+1, k):
                        qij = sum(int(indices[nu, i])*int(indices[mu, j])
                                  for nu in range(r) for mu in range(nu, r))
                        predicted += qij*2*a*a*b[j-i]
                        parity += qij*(j-i)
                assert total == [0, 0] and (phase-predicted) % n == 0
                assert np.array_equal(spin, (-1)**parity*np.eye(2, dtype=int))
                multiple_block_checks += 1
    return {"rows": rows, "ordered_two-block_Weyl_checks": phase_checks,
            "ordered_multiblock_Weyl_Pauli_checks": multiple_block_checks,
            "noninteger_fraction_pairs": sorted(pairs),
            "largest_rational_coset_majorant": str(largest),
            "activity_ratio_at_z_0_3": str(activity_ratio)}


def character_moment(r, t):
    def h(two_j):
        if two_j < 0:
            return 0.
        j = two_j/2
        return sum(math.exp(-t*(j*(j+1)-ell*ell))
                   for ell in np.arange(-j, j+1, 1))
    return (h(r)-h(r-2))/2


def aggregate_phase_controls():
    """Exhaust all {-1,0,1}^6 words in each of the 32 aggregate classes.

    The inputs include nonzero aggregates. Thus this is a check of the new
    reduction needed for summing all resonances, not just the earlier x=-y case.
    """
    k, n = 6, 35
    a, half = (n+1)//2, pow(2, -1, n)
    b = recurrence(k)
    orbit, v = [], (1, 0)
    for _ in range(k):
        orbit.append(v)
        v = ((3*v[0]+4*v[1]) % n, (2*v[0]+3*v[1]) % n)
    checks = 0
    for r in range(16):
        for s in range(2):
            c = [r if j % 2 == 0 else s for j in range(k)]
            assert all(sum(c[j]*orbit[j][d] for j in range(k)) % n == 0
                       for d in (0, 1))
            for x in product((-1, 0, 1), repeat=k):
                total, phase = [0, 0], 0
                for row in (x, [c[j]-x[j] for j in range(k)]):
                    for value, vector in zip(row, orbit):
                        w = [value*a*q for q in vector]
                        phase += half*(total[0]*w[1]-total[1]*w[0])
                        total = [(p+q) % n for p, q in zip(total, w)]
                reduced = a*a*sum(
                    (2*x[i]*x[j]-c[i]*x[j]-x[i]*c[j]+c[i]*c[j])*b[j-i]
                    for i in range(k) for j in range(i+1, k))
                assert total == [0, 0] and (phase-reduced) % n == 0
                checks += 1
    return {"K": k, "N": n, "classes": 32,
            "exhaustive_nonzero_aggregate_Weyl_checks": checks}


def sign_average(size, edge_i, edge_j, angles):
    """Exact conditional sign average, up to floating arithmetic.

    Edge signs are independent on a forest. Cyclic components are enumerated
    completely after fixing the common sign. A large component fails loudly.
    """
    parent = list(range(size))

    def root(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    cyclic = False
    for i, j in zip(edge_i, edge_j):
        ri, rj = root(int(i)), root(int(j))
        if ri == rj:
            cyclic = True
        else:
            parent[ri] = rj
    if not cyclic:
        return complex(np.prod(np.cos(angles))), False
    components = {}
    for e, (i, j) in enumerate(zip(edge_i, edge_j)):
        components.setdefault(root(int(i)), []).append(e)
    average = 1.+0j
    for edges in components.values():
        vertices = sorted(set(int(v) for e in edges for v in (edge_i[e], edge_j[e])))
        if len(edges) == len(vertices)-1:
            average *= np.prod(np.cos(angles[edges]))
            continue
        if len(vertices) > 20:
            raise RuntimeError("Cyclic component exceeds the exhaustive sign budget")
        index = {v: i for i, v in enumerate(vertices)}
        labels = np.arange(2**(len(vertices)-1), dtype=np.uint32)
        signs = np.ones((len(labels), len(vertices)), dtype=np.int8)
        for i in range(1, len(vertices)):
            signs[:, i] = 1-2*((labels >> (i-1)) & 1).astype(np.int8)
        phase = np.zeros(len(labels))
        for e in edges:
            phase += angles[e]*signs[:, index[int(edge_i[e])]]*signs[:, index[int(edge_j[e])]]
        average *= np.exp(1j*phase).mean()
    return complex(average), True


def conditional_average_controls():
    """Independent complete sign sums check both branches of the fast average."""
    rng = np.random.default_rng(918432)
    checks = 0
    for size in range(2, 9):
        for dense in (False, True):
            ei, ej = np.triu_indices(size, 1)
            keep = rng.random(len(ei)) < (0.7 if dense else 0.15)
            ei, ej = ei[keep], ej[keep]
            angles = rng.uniform(-math.pi, math.pi, len(ei))
            actual, _ = sign_average(size, ei, ej, angles)
            expected = 0j
            for signs in product((-1, 1), repeat=size):
                phase = sum(angle*signs[i]*signs[j] for i, j, angle in zip(ei, ej, angles))
                expected += complex(np.exp(1j*phase))/2**size
            assert abs(actual-expected) < 2e-14
            checks += 1
    # The four-corner identity is the source of the field-uniform contraction.
    for h, g in rng.uniform(-math.pi, math.pi, (100, 2)):
        corners = 1+np.exp(1j*h)+np.exp(1j*g)-np.exp(1j*(h+g))
        assert abs(abs(corners)**2-(4+4*math.sin(h)*math.sin(g))) < 1e-14
    return {"complete_sign_average_cases": checks, "four_corner_identity_cases": 100}


def sharp_aggregate_bound(k, delta):
    z = mp.mpf(3)*delta
    v = 2*z**4/(1-z**4)
    activity = (2*mp.besseli(1, 4*delta)**2*mp.besseli(6, 4*delta)
                +2*z**16/(1-z**8)+12*z**4*v**2/(1-4*v))
    return float(mp.expm1(k*activity)+2*mp.mpf('0.26')**k+31*mp.mpf('0.6')**k)


def critical_experiments(samples, seed=91345):
    """Rao--Blackwell estimates of the actual zero-aggregate expectation.

    Small Bessel charges and short antipodal offsets are retained with stated
    analytic tail bounds. Conditional sign sums include all cycles exactly.
    """
    rng = np.random.default_rng(seed)
    k, cutoff, offset_cutoff = 10002, 4, 12
    lam = 3+2*mp.sqrt(2)
    kappa_terms = 50
    kappa = 4*(1+sum(1-mp.cos(mp.pi*lam**(-ell)) for ell in range(1, kappa_terms+1)))
    kappa_tail = 2*mp.pi**2*lam**(-2*(kappa_terms+1))/(1-lam**(-2))
    cases, alpha = 3, 1e-6
    log_confidence = math.log(4*cases/alpha)
    rows = []
    for u in (0.02, 0.1, 0.3):
        delta = (u/k)**0.25
        probabilities = np.array([2*float(mp.besselj(j, 2*delta)**2)
                                  for j in range(1, cutoff+1)])
        p = float(sum(probabilities))
        bias = float(mp.besselj(0, 4*delta))
        ideal = -0.5+bias**(k//2)+0.5*bias**k
        differences = np.zeros(samples, dtype=complex)
        cycles = 0
        for sample, count in enumerate(rng.binomial(k, p, size=samples)):
            if count < 2:
                continue
            sites = np.sort(rng.choice(k, size=count, replace=False))
            amplitudes = rng.choice(np.arange(1, cutoff+1), size=count, p=probabilities/p)
            even = int(sum(amplitudes[sites % 2 == 0])) % 2
            odd = int(sum(amplitudes[sites % 2 == 1])) % 2
            parity = 1 if even == odd == 0 else -1
            ei, ej = np.triu_indices(count, 1)
            offsets = sites[ej]-sites[ei]-k//2
            keep = abs(offsets) <= offset_cutoff
            ei, ej, offsets = ei[keep], ej[keep], offsets[keep]
            angles = (np.where(offsets <= 0, 1., -1.)*math.pi
                      *float(lam)**(-abs(offsets))*amplitudes[ei]*amplitudes[ej])
            average, cyclic = sign_average(count, ei, ej, angles)
            cycles += int(cyclic)
            differences[sample] = parity*(average-1)
        mean = complex(differences.mean())
        phase_bound = 2*math.sqrt(2)*math.pi*u
        # Conditional averaging cannot increase the second moment. The limiting
        # Binet angles obey the same absolute row bound as the exact angles.
        radius = math.sqrt(2)*(math.sqrt(4*phase_bound*log_confidence/samples)
                               +(8/3)*log_confidence/samples)
        tail_mass = (2*mp.exp(2*delta**2)*mp.mpf(delta)**(2*(cutoff+1))
                     /math.factorial(cutoff+1)**2/(1-delta**2/(cutoff+2)**2))
        binet_error = (4*mp.pi*u*offset_cutoff*lam**(-k+offset_cutoff)
                       /(1-lam**(-k)))
        log_n = (k//2)*mp.log(lam)+mp.log1p(-lam**(-k))-mp.log(4*mp.sqrt(2))
        rows.append({
            "K": k, "u": u, "t": 2*k*delta**2, "epsilon": delta,
            "samples": samples, "spin_cutoff": cutoff, "offset_cutoff": offset_cutoff,
            "zero_aggregate_estimate": [ideal+mean.real, mean.imag],
            "asymptotic_prediction": float(-mp.exp(-kappa*u)/2),
            "empirical_standard_error_not_confidence_bound": float(np.std(differences, ddof=1)/math.sqrt(samples)),
            "Monte_Carlo_complex_radius": radius,
            "global_failure_probability_bound": alpha,
            "cyclic_sample_graphs": cycles,
            "capped_tail_expectation_error_bound": float(4*k*tail_mass),
            "offset_tail_expectation_error_bound": float(4*mp.pi*u*lam**(-offset_cutoff)/(lam-1)),
            "Binet_angle_expectation_error_bound": mp.nstr(binet_error, 18),
            "all_nonzero_aggregate_error_bound": sharp_aggregate_bound(k, delta),
            "odd_projection_error_bound": mp.nstr(mp.exp(4*k*delta-log_n)/(1-mp.exp(-log_n)), 18),
        })
    return {"seed": seed, "kappa": mp.nstr(kappa, 55),
            "kappa_series_tail_bound": mp.nstr(kappa_tail, 12),
            "scope": "Numerical evidence with analytic truncation and sampling bounds; floating arithmetic is not interval-certified. No physical matrix was constructed.",
            "rows": rows}


def spin_representation_controls():
    """Direct finite spin-matrix powers versus the finite exponential formula."""
    rows = []
    for two_j in range(1, 7):
        j = two_j/2
        labels = np.arange(-j, j+1)
        raising = np.zeros((two_j+1, two_j+1))
        for i, ell in enumerate(labels[:-1]):
            raising[i+1, i] = math.sqrt((j-ell)*(j+ell+1))
        jx, jz = (raising+raising.T)/2, np.diag(labels)
        jy = (raising-raising.T)/(2j)
        assert np.max(abs(jx@jx+jy@jy+jz@jz-j*(j+1)*np.eye(two_j+1))) < 1e-12
        errors = []
        for k in (200, 800):
            t = 2.
            eps = math.sqrt(t/(2*k))
            def averaged(axis):
                eigenvalues, eigenvectors = np.linalg.eigh(axis)
                factors = np.array([float(mp.besselj(0, 4*eps*x)) for x in eigenvalues])
                return (eigenvectors*factors[None, :]) @ eigenvectors.conj().T
            actual = np.trace(np.linalg.matrix_power(averaged(jx)@averaged(jz), k//2))
            target = sum(math.exp(-t*(j*(j+1)-ell*ell)) for ell in labels)
            error = float(abs(actual-target))
            errors.append(error)
            rows.append({"spin": str(Q(two_j, 2)), "K": k, "t": t,
                         "character_error": error})
        assert errors[1] < 0.3*errors[0]
    return rows


def physical_controls():
    rows = []
    for k in (6, 10):
        n = recurrence(k)[k//2]
        d, a = (n-1)//2, (n+1)//2
        x = np.arange(1, d+1)
        inv4 = pow(4, -1, n)
        plus = ((3*x[:, None]**2-2*x[:, None]*x[None, :]+3*x[None, :]**2)*inv4) % n
        minus = ((3*x[:, None]**2+2*x[:, None]*x[None, :]+3*x[None, :]**2)*inv4) % n
        u = (np.exp(2j*np.pi*plus/n)-np.exp(2j*np.pi*minus/n))/math.sqrt(n)
        unitarity = float(np.max(abs(u@u.conj().T-np.eye(d))))
        assert unitarity < 2e-12
        stochastic = 2/n*(1-np.cos(2*np.pi*((x[:, None]*x[None, :]) % n)/n))
        assert np.max(abs(abs(u)**2-stochastic)) < 2e-12
        mixing_error = float(np.max(abs(stochastic@stochastic
                                        -(np.eye(d)+2*np.ones((d, d)))/n)))
        assert mixing_error < 2e-12
        uk = np.linalg.matrix_power(u, k)
        scalar = np.trace(uk)/d
        scalar_error = float(np.max(abs(uk-scalar*np.eye(d))))
        assert scalar_error < 2e-12
        u *= np.exp(-1j*np.angle(scalar)/k)
        for epsilon in (0.03, 0.1):
            phase = np.exp(2j*epsilon*np.cos(2*np.pi*((a*x) % n)/n))
            kicked = phase[:, None]*u
            returned = np.linalg.matrix_power(kicked, k)
            first = np.trace(returned)/d
            second = np.trace(returned@returned)/d
            b = float(mp.besselj(0, 4*epsilon))
            target = -0.5+b**(k//2)+0.5*b**k
            bound = (2*math.sqrt(2)*math.pi*k*epsilon**4+g_bound(k, 3*epsilon)
                     +math.exp(4*k*epsilon)/(n-1))
            assert abs(second-target) <= bound+1e-12
            rows.append({"K": k, "N": n, "epsilon": epsilon,
                         "unitarity_error": unitarity, "period_scalar_error": scalar_error,
                         "stochastic_square_error": mixing_error,
                         "first_return": [float(first.real), float(first.imag)],
                         "second_return": [float(second.real), float(second.imag)],
                         "two_parity_prediction": target, "theorem_error_bound": bound})
    return rows


def sparse_experiments(samples, seed):
    rng = np.random.default_rng(seed)
    alpha, cases, cutoff = 1e-6, 8, 4
    log_confidence = math.log(4*cases/alpha)
    rows = []
    for k in (1002, 10002):
        b = recurrence(k//2)
        n = b[-1]
        eta = np.zeros(k)
        for distance in range(1, k//2+1):
            angle = math.pi*(b[distance]/n)
            eta[distance] = angle
            if distance != k//2:
                eta[k-distance] = -angle
        for t in (1., 2., 4., 8.):
            epsilon = math.sqrt(t/(2*k))
            probabilities = np.array([2*float(mp.besselj(j, 2*epsilon)**2)
                                      for j in range(1, cutoff+1)])
            occupied_probability = float(sum(probabilities))
            magnitude_probabilities = probabilities/occupied_probability
            parity_bias = float(mp.besselj(0, 4*epsilon))
            ideal = -0.5+parity_bias**(k//2)+0.5*parity_bias**k
            differences = np.zeros(samples, dtype=complex)
            counts = rng.binomial(k, occupied_probability, size=samples)
            for sample, count in enumerate(counts):
                if count < 2:
                    continue
                sites = np.sort(rng.choice(k, size=count, replace=False))
                values = rng.choice(np.arange(1, cutoff+1), size=count,
                                    p=magnitude_probabilities)
                values *= rng.choice(np.array([-1, 1]), size=count)
                even = int(sum(values[sites % 2 == 0])) % 2
                odd = int(sum(values[sites % 2 == 1])) % 2
                sign = 1 if even == odd == 0 else -1
                angle = sum(int(values[i]*values[j])*eta[sites[j]-sites[i]]
                            for i in range(count) for j in range(i+1, count))
                differences[sample] = sign*np.expm1(1j*angle)
            mean = complex(differences.mean())
            phase_bound = 2*math.sqrt(2)*math.pi*k*epsilon**4
            # Bernstein, union bound for real/imaginary parts and all cases:
            # |Y|<=2, |Y-EY|<=4, Var(component)<=E|Y|^2<=2*phase_bound.
            component_radius = (math.sqrt(4*phase_bound*log_confidence/samples)
                                +(8/3)*log_confidence/samples)
            radius = math.sqrt(2)*component_radius
            tail_mass = (2*math.exp(2*epsilon**2)*epsilon**(2*(cutoff+1))
                         /math.factorial(cutoff+1)**2
                         /(1-epsilon**2/(cutoff+2)**2))
            omitted_aggregate_bound = g_bound(k, 3*epsilon)
            log_odd_error = 4*k*epsilon-float(mp.log(n-1))
            odd_error = math.exp(log_odd_error) if log_odd_error > -745 else 0.
            rows.append({
                "K": k, "log10_N": float(mp.log10(n)), "t": t, "epsilon": epsilon,
                "samples": samples, "spin_cutoff": cutoff,
                "known_two_parity_expectation": ideal,
                "zero_aggregate_estimate": [ideal+mean.real, mean.imag],
                "paired_correction_mean": [mean.real, mean.imag],
                "Monte_Carlo_complex_radius": radius,
                "global_failure_probability_bound": alpha,
                "capped_tail_expectation_error_bound": 4*k*tail_mass,
                "all_nonzero_aggregate_error_bound": omitted_aggregate_bound,
                "odd_projection_error_bound": odd_error,
                "deterministic_phase_comparison_bound": phase_bound,
            })
    return {"seed": seed,
            "scope": "Sparse zero-aggregate expectation with a known parity control variate. No large matrix diagonalization. Bernstein probabilities exclude unvalidated floating rounding.",
            "rows": rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--samples", type=int, default=20000)
    parser.add_argument("--seed", type=int, default=20260910)
    parser.add_argument("--critical-samples", type=int, default=0,
                        help="Also run the second-scale experiment (0 disables it)")
    args = parser.parse_args()
    if args.samples < 2:
        parser.error("--samples must be at least 2")
    if args.critical_samples < 0 or args.critical_samples == 1:
        parser.error("--critical-samples must be 0 or at least 2")
    mp.mp.dps = 80
    start = time.monotonic()
    result = {"scope": "Bounded exact controls, finite matrix checks, and probabilistic sparse experiments; not a BGS or priority certificate.",
              "python": platform.python_version(), "numpy": np.__version__,
              "mpmath": mp.__version__, "exact": exact_controls(),
              "aggregate_phase_controls": aggregate_phase_controls(),
              "conditional_average_controls": conditional_average_controls(),
              "spin_representations": spin_representation_controls(),
              "physical_controls": physical_controls(),
              "sparse_experiments": sparse_experiments(args.samples, args.seed)}
    if args.critical_samples:
        result["critical_experiments"] = critical_experiments(args.critical_samples)
    result["elapsed_seconds"] = time.monotonic()-start
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"output": str(args.output), "elapsed_seconds": result["elapsed_seconds"],
                      "exact_Weyl_checks": result["exact"]["ordered_two-block_Weyl_checks"],
                      "sparse_experiments": len(result["sparse_experiments"]["rows"])}))


if __name__ == "__main__":
    main()
