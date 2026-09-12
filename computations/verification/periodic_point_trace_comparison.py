#!/usr/bin/env python3
"""Exact first-order lattice/Weyl controls and a small physical trace check."""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as Q
import json
from math import gcd
from pathlib import Path
import random

import numpy as np

from even_period_spin_resonance import recurrence

A = ((3, 4), (2, 3))
AINV = ((3, -4), (-2, 3))


def act(a, v):
    return tuple(sum(x*y for x, y in zip(row, v)) for row in a)


def matmul(a, b):
    return tuple(tuple(sum(a[i][ell]*b[ell][j] for ell in range(2))
                       for j in range(2)) for i in range(2))


def matrix_power(k):
    value = ((1, 0), (0, 1))
    for _ in range(k):
        value = matmul(value, A)
    return value


def omega(v, w):
    return v[0]*w[1]-v[1]*w[0]


def first_order(p):
    return [tuple(x-y for x, y in zip(p[j], act(A, p[(j+1) % len(p)])))
            for j in range(len(p))]


def norm(values):
    return sum(abs(x) for row in values for x in row)


def lattice_phase_checks():
    rng = random.Random(110935)
    result = []
    for k in (6, 10, 14, 18, 22, 34):
        n = recurrence(k)[k//2]
        ak = matrix_power(k)
        d = tuple(tuple(int(i == j)-ak[i][j] for j in range(2)) for i in range(2))
        determinant = d[0][0]*d[1][1]-d[0][1]*d[1][0]
        assert abs(determinant) == 32*n*n
        assert gcd(*[abs(value) for row in d for value in row]) == 4*n
        assert all(value % (2*n) == 0 for row in d for value in row)
        classes = set()
        for z in ((u, v) for u in range(32) for v in range(32)):
            p0 = (Q(n*(d[1][1]*z[0]-d[0][1]*z[1]), determinant),
                  Q(n*(-d[1][0]*z[0]+d[0][0]*z[1]), determinant))
            classes.add(tuple(x-x//1 for x in p0))
        assert len(classes) == 32
        class_checks = 0
        for initial in sorted(classes):
            for _ in range(5):
                fractional, value = [], initial
                for _ in range(k):
                    value = tuple(x-x//1 for x in value)
                    fractional.append(value)
                    value = act(AINV, value)
                assert tuple(x-x//1 for x in value) == initial
                p = [tuple(x+rng.randrange(-2, 3) for x in row) for row in fractional]
                c = first_order(p)
                assert all(x.denominator == 1 for row in c for x in row)
                assert all((32*x).denominator == 1 for row in p for x in row)
                assert norm(p) <= 2*norm(c)
                if initial != (0, 0):
                    assert all(any(x.denominator != 1 for x in row) for row in p)
                    assert norm(c) >= Q(k, 64)
                total = [0, 0]
                orbit_matrix = ((1, 0), (0, 1))
                for row in c:
                    w = act(orbit_matrix, row)
                    total = [x+y for x, y in zip(total, w)]
                    orbit_matrix = matmul(orbit_matrix, A)
                assert all(x % n == 0 for x in total)
                class_checks += 1
        parity_count = Counter()
        for trial in range(201):
            p = [(rng.randrange(-3, 4), rng.randrange(-3, 4)) for _ in range(k)]
            if trial == 0:
                p = [(1, 0), (0, 1)]+[(0, 0)]*(k-2)
            c = first_order(p)
            total, ordered_area, parity = (0, 0), 0, 0
            orbit_matrix = ((1, 0), (0, 1))
            for row in c:
                w = act(orbit_matrix, row)
                ordered_area += omega(total, w)
                total = tuple(x+y for x, y in zip(total, w))
                parity += row[0]*row[1]
                orbit_matrix = matmul(orbit_matrix, A)
            assert all(x % (2*n) == 0 for x in total)
            local_area = sum(omega(p[j], act(A, p[(j+1) % k])) for j in range(k))
            assert (ordered_area-local_area) % (2*n) == 0
            centered_phase = pow(2, -1, n)*ordered_area % n
            balanced_phase = (2*centered_phase+n*parity) % (2*n)
            assert balanced_phase == local_area % (2*n)
            assert abs(local_area) <= 2*norm(c)**2
            parity_count[local_area % 2] += 1
        assert parity_count[1] > 0
        result.append({"K": k, "N": n, "fractional_classes": len(classes),
                       "seeded_class_checks": class_checks, "integer_phase_checks": 201,
                       "even_and_odd_local_areas": dict(parity_count)})
    return {"seed": 110935, "cases": result}


def balanced_weyl(v, n):
    x = np.arange(n)
    out = np.zeros((n, n), dtype=complex)
    out[x, (x-v[1]) % n] = np.exp(2j*np.pi*v[0]*x/n-1j*np.pi*v[0]*v[1]/n)
    return out


def physical_check():
    """Floating diagnostic on the full physical space, not a proof certificate."""
    k, n = 6, 35
    x = np.arange(n, dtype=np.int64)
    exponent = ((3*x[:, None]**2-2*x[:, None]*x[None, :]+3*x[None, :]**2)
                *pow(4, -1, n)) % n
    u0 = np.exp(2j*np.pi*exponent/n)/np.sqrt(n)
    phase = np.trace(np.linalg.matrix_power(u0, k))/n
    u0 *= np.exp(-1j*np.angle(phase)/k)
    assert np.linalg.norm(np.linalg.matrix_power(u0, k)-np.eye(n), 2) < 2e-12
    positive = {(1, 0): 1.0, (0, 1): .4, (1, 1): .3}
    hamiltonian = sum(coefficient*(balanced_weyl(v, n)+balanced_weyl(tuple(-a for a in v), n))
                      for v, coefficient in positive.items())
    assert np.linalg.norm(hamiltonian-hamiltonian.conj().T, 2) < 2e-12
    egorov_errors = []
    for v in positive:
        residual = u0@balanced_weyl(v, n)@u0.conj().T-balanced_weyl(act(A, v), n)
        egorov_errors.append(float(np.linalg.norm(residual, 2)))
    assert max(egorov_errors) < 2e-12
    energies, basis = np.linalg.eigh(hamiltonian)
    grid_u, grid_v = np.meshgrid(np.arange(8*n), np.arange(4*n), indexing="ij")
    u, v = grid_u.ravel().copy(), grid_v.ravel().copy()
    action = np.zeros_like(u, dtype=float)
    for _ in range(k):
        action += sum(2*c*np.cos(2*np.pi*(mode[0]*u/(8*n)+mode[1]*v/(4*n)))
                      for mode, c in positive.items())
        u, v = (3*u+4*v) % (8*n), (2*u+3*v) % (4*n)
    assert np.array_equal(u, grid_u.ravel()) and np.array_equal(v, grid_v.ravel())
    rows = []
    for epsilon in (.08, .04, .02, .01):
        kick = (basis*np.exp(1j*epsilon*energies))@basis.conj().T
        quantum = np.trace(np.linalg.matrix_power(kick@u0, k))/n
        classical = np.mean(np.exp(1j*epsilon*action))
        rows.append({"epsilon": epsilon, "quantum_trace": [quantum.real, quantum.imag],
                     "periodic_point_average": [classical.real, classical.imag],
                     "absolute_difference": float(abs(quantum-classical))})
    return {"K": k, "N": n, "periodic_points": int(action.size),
            "Egorov_operator_norm_residuals": egorov_errors, "comparisons": rows,
            "scope": "Double-precision finite diagnostics only; no interval enclosure or asymptotic proof."}


def repeated_period_obstruction():
    """Exact quadratic characters: quantum repeats versus longer classical orbits."""
    cases = []
    k = 10
    n = recurrence(k)[k//2]
    for r in range(1, 9):
        length = r*k
        classical_modulus = recurrence(length)[length//2]
        quantum_atoms, classical_atoms = [], []
        quantum_v = classical_v = (1, 0)
        for _ in range(length):
            quantum_atoms.extend(tuple(sign*x % n for x in quantum_v) for sign in (-1, 1))
            classical_atoms.extend((sign*classical_v[0] % (8*classical_modulus),
                                    sign*classical_v[1] % (4*classical_modulus))
                                   for sign in (-1, 1))
            quantum_v = tuple(x % n for x in act(A, quantum_v))
            cv = act(A, classical_v)
            classical_v = cv[0] % (8*classical_modulus), cv[1] % (4*classical_modulus)
        quantum_count = classical_count = 0
        for v in quantum_atoms:
            for w in quantum_atoms:
                if all((x+y) % n == 0 for x, y in zip(v, w)):
                    assert omega(v, w) % n == 0
                    quantum_count += 1
        for v in classical_atoms:
            for w in classical_atoms:
                if ((v[0]+w[0]) % (8*classical_modulus) == 0
                        and (v[1]+w[1]) % (4*classical_modulus) == 0):
                    classical_count += 1
        assert quantum_count == 2*k*r*r
        assert classical_count == 2*k*r
        cases.append({"K": k, "replicas": r, "quantum_dimension": n,
                      "classical_orbit_length": length,
                      "quantum_quadratic_coefficient": -quantum_count//2,
                      "classical_quadratic_coefficient": -classical_count//2})
    return cases


def centered_coupling_bound():
    """Exact geometric upper bound; this is not a sampled CLT."""
    cases = []
    for k in (6, 10, 14, 34, 66, 130, 262):
        n = recurrence(k)[k//2]
        # ||(A^T)^j||_infinity = ||A^j||_1, also for negative j.
        powers = {0: ((1, 0), (0, 1))}
        for j in range(1, k//2+1):
            powers[j] = matmul(powers[j-1], A)
            powers[-j] = matmul(powers[1-j], AINV)
        numerator = sum(max(sum(abs(powers[j][i][ell]) for i in range(2))
                            for ell in range(2))
                        for j in range(-k//2, k//2))
        bound = Q(numerator, 8*n)
        assert bound < 3
        # The count and cell sizes are exact, not floating nearest neighbors.
        assert Q(1, 8*n)*Q(1, 4*n)*(32*n*n) == 1
        cases.append({"K": k, "N": n, "exact_distance_bound": str(bound),
                      "distance_bound_decimal": float(bound)})
    return cases


def pair_multiplicity_check():
    """Exhaust ordered pairs, including equal times and one theorem-range case."""
    support = ((1, 0), (-1, 0), (0, 1), (0, -1))
    cases = []
    for k in (6, 10, 14, 34, 262):
        n = recurrence(k)[k//2]
        orbits, orbit_matrix = [], ((1, 0), (0, 1))
        for _ in range(k):
            orbits.append([tuple(x % n for x in act(orbit_matrix, v)) for v in support])
            orbit_matrix = tuple(tuple(x % n for x in row) for row in matmul(orbit_matrix, A))
        counts = Counter()
        zero_keys = 0
        for i in range(k):
            for j in range(i+1, k):
                for v in orbits[i]:
                    for w in orbits[j]:
                        key = ((v[0]+w[0]) % n, (v[1]+w[1]) % n)
                        if key == (0, 0):
                            assert omega(v, w) % n == 0
                            zero_keys += 2
                        else:
                            counts[key] += 2  # Both time orders, with frequencies exchanged.
        for modes in orbits:
            for v in modes:
                for w in modes:
                    key = ((v[0]+w[0]) % n, (v[1]+w[1]) % n)
                    if key == (0, 0):
                        assert omega(v, w) % n == 0
                        zero_keys += 1
                    else:
                        counts[key] += 1
        histogram = Counter(counts.values())
        representations = k*k*len(support)**2
        assert sum(size*number for size, number in histogram.items())+zero_keys == representations
        bound = (2*(2*(8+1)+1)*len(support))**2
        if k > 256:
            assert max(counts.values(), default=0) <= bound
        cases.append({"K": k, "N": n, "support": support, "representations": representations,
                      "zero_output_representations": zero_keys,
                      "multiplicity_histogram": dict(sorted(histogram.items())),
                      "maximum_multiplicity": max(counts.values(), default=0),
                      "proved_bound": bound, "inside_theorem_range": k > 256})
    return cases


def normal_form_diagnostic():
    """Floating physical controls on the full space, distinct from exact proofs."""
    k, n = 6, 35
    x = np.arange(n, dtype=np.int64)
    exponent = ((3*x[:, None]**2-2*x[:, None]*x[None, :]+3*x[None, :]**2)
                *pow(4, -1, n)) % n
    u0 = np.exp(2j*np.pi*exponent/n)/np.sqrt(n)
    phase = np.trace(np.linalg.matrix_power(u0, k))/n
    u0 *= np.exp(-1j*np.angle(phase)/k)
    positive = {(1, 0): 1.0, (0, 1): .4, (1, 1): .3, (3, 2): .25}
    h = sum(coef*(balanced_weyl(v, n)+balanced_weyl(tuple(-a for a in v), n))
            for v, coef in positive.items())
    orbit = [h]
    for _ in range(1, k):
        orbit.append(u0@orbit[-1]@u0.conj().T)
    hbar = sum(orbit)/k
    g = sum((k-1-2*j)/(2*k)*hj for j, hj in enumerate(orbit))
    identity_error = np.linalg.norm(g-u0@g@u0.conj().T-h+hbar, 2)
    assert identity_error < 1e-11

    def hs(value):
        return float(np.linalg.norm(value, "fro")/np.sqrt(n))

    def comm(left, right):
        return left@right-right@left

    def spectral_exp(matrix):
        eigenvalues, basis = np.linalg.eigh(matrix)
        return lambda t: (basis*np.exp(1j*t*eigenvalues))@basis.conj().T

    eh, eg, ebar = map(spectral_exp, (h, g, hbar))
    duh_constant = .5*(hs(comm(g, h))+hs(comm(h, hbar))+hs(comm(g, hbar)))
    rows = []
    for epsilon in (.16, .08, .04, .02, .01):
        residual = eg(-epsilon)@(eh(epsilon)@u0)@eg(epsilon)-ebar(epsilon)@u0
        error = hs(residual)
        bound = epsilon**2*duh_constant
        assert error <= bound+2e-12
        rows.append({"epsilon": epsilon, "normalized_HS_error": error,
                     "Duhamel_HS_bound": bound})
    replicas = []
    for t in (.3, .8):
        reference = np.trace(ebar(t*np.sqrt(k)))/n
        for r in (1, 2, 3, 7, 16):
            epsilon = t/(r*np.sqrt(k))
            physical_return = np.linalg.matrix_power(eh(epsilon)@u0, r*k)
            actual = np.trace(physical_return)/n
            error = abs(actual-reference)
            bound = t*t*duh_constant/r
            assert error <= bound+2e-11
            ungauged_error = hs(physical_return-ebar(t*np.sqrt(k)))
            ungauged_bound = t*t*(duh_constant+hs(comm(g, hbar)))/r
            assert ungauged_error <= ungauged_bound+2e-11
            replicas.append({"t": t, "replicas": r,
                             "trace": [float(actual.real), float(actual.imag)],
                             "averaged_reference": [float(reference.real), float(reference.imag)],
                             "absolute_error": float(error), "trace_error_bound": bound,
                             "ungauged_HS_error": ungauged_error, "ungauged_HS_bound": ungauged_bound})
    second_positive = {(1, 0): .3, (0, 1): 1.0, (1, 1): -.2, (4, 3): .1}
    h2 = sum(coef*(balanced_weyl(v, n)+balanced_weyl(tuple(-a for a in v), n))
             for v, coef in second_positive.items())
    orbit2 = [h2]
    for _ in range(1, k):
        orbit2.append(u0@orbit2[-1]@u0.conj().T)
    hbar2 = sum(orbit2)/k
    g2 = sum((k-1-2*j)/(2*k)*hj for j, hj in enumerate(orbit2))
    eh2, ebar2 = map(spectral_exp, (h2, hbar2))
    normal2 = .5*(hs(comm(g2, h2))+hs(comm(h2, hbar2))+hs(comm(g2, hbar2)))
    commutator_constant = k*hs(comm(hbar, hbar2))
    joint = []
    for t1, t2 in ((.3, -.2), (.8, .5)):
        sum_exp = spectral_exp(np.sqrt(k)*(t1*hbar+t2*hbar2))(1)
        product_exp = ebar(t1*np.sqrt(k))@ebar2(t2*np.sqrt(k))
        product_error = hs(product_exp-sum_exp)
        product_bound = .5*abs(t1*t2)*commutator_constant
        assert product_error <= product_bound+2e-11
        for r1, r2 in ((1, 1), (2, 7), (16, 3)):
            physical1 = np.linalg.matrix_power(eh(t1/(r1*np.sqrt(k)))@u0, r1*k)
            physical2 = np.linalg.matrix_power(eh2(t2/(r2*np.sqrt(k)))@u0, r2*k)
            joint_error = hs(physical1@physical2-sum_exp)
            bound = (product_bound+t1*t1*(duh_constant+hs(comm(g, hbar)))/r1
                     +t2*t2*(normal2+hs(comm(g2, hbar2)))/r2)
            assert joint_error <= bound+4e-11
            joint.append({"parameters": [t1, t2], "replicas": [r1, r2],
                          "exponential_product_HS_error": product_error,
                          "exponential_product_HS_bound": product_bound,
                          "physical_product_HS_error": joint_error, "physical_product_HS_bound": bound})
    return {"K": k, "N": n, "cohomological_identity_residual": float(identity_error),
            "Duhamel_constant": duh_constant, "conjugacy_checks": rows, "replica_checks": replicas,
            "joint_physical_return_checks": joint,
            "scope": "Double precision, no interval enclosure. K=6 is outside the asymptotic pair-bound range."}


def coboundary_second_order_diagnostic():
    """Exact generated Fourier symbol, then floating unitary-loop controls."""
    k, n = 6, 35
    v, av = (1, 0), act(A, (1, 0))
    g_coefficients = {v: 1, tuple(-x for x in v): 1}
    cg_coefficients = {av: 1, tuple(-x for x in av): 1}
    h_over_pi = Counter()
    for a, ca in g_coefficients.items():
        for b, cb in cg_coefficients.items():
            h_over_pi[tuple(x+y for x, y in zip(a, b))] -= omega(a, b)*ca*cb
    assert dict(h_over_pi) == {(4, 2): -2, (-2, -2): 2, (2, 2): 2, (-4, -2): -2}
    invariants = [omega(w, act(A, w)) for w in ((-2, -2), (4, 2))]
    assert invariants == [-8, 16]
    gamma_over_pi_squared = sum(c*c for c in h_over_pi.values())
    assert gamma_over_pi_squared == 16

    grid = np.arange(n, dtype=np.int64)
    exponent = ((3*grid[:, None]**2-2*grid[:, None]*grid[None, :]+3*grid[None, :]**2)
                *pow(4, -1, n)) % n
    u0 = np.exp(2j*np.pi*exponent/n)/np.sqrt(n)
    phase = np.trace(np.linalg.matrix_power(u0, k))/n
    u0 *= np.exp(-1j*np.angle(phase)/k)
    x = sum(c*balanced_weyl(a, n) for a, c in g_coefficients.items())
    y = sum(c*balanced_weyl(a, n) for a, c in cg_coefficients.items())
    h = np.pi*sum(c*balanced_weyl(a, n) for a, c in h_over_pi.items())
    assert np.linalg.norm(u0@x@u0.conj().T-y, 2) < 1e-11

    def comm(a, b):
        return a@b-b@a

    def spectral_exp(matrix):
        assert np.linalg.norm(matrix-matrix.conj().T, 2) < 1e-11
        energies, basis = np.linalg.eigh(matrix)
        return lambda t: (basis*np.exp(1j*t*energies))@basis.conj().T

    q = comm(x, y)
    ex, ey, ef, eh, eq = map(spectral_exp, (x, y, x-y, h, -1j*q))
    loop_constant = .5*np.linalg.norm(comm(x, q), 2)+np.linalg.norm(comm(y, q), 2)/6
    sine_residual = np.linalg.norm(q+2j*h/n, 2)
    assert sine_residual <= 32*np.pi**3/(3*n**3)+1e-11
    rows = []
    for epsilon in (-1.28, -.16, -.08, .08, .16, .32, .64, 1.28, 2.56):
        loop = ex(-epsilon)@ef(epsilon)@ey(epsilon)
        error = np.linalg.norm(loop-eq(-epsilon*epsilon/2), 2)
        bound = abs(epsilon)**3*loop_constant
        effective_error = np.linalg.norm(loop-eh(epsilon*epsilon/n), 2)
        effective_bound = bound+epsilon*epsilon*sine_residual/2
        assert error <= bound+2e-11
        assert effective_error <= effective_bound+2e-11
        rows.append({"epsilon": epsilon, "loop_operator_error": float(error),
                     "loop_operator_bound": float(bound), "effective_kick_error": float(effective_error),
                     "effective_kick_bound": float(effective_bound)})
    replicas = []
    for t in (.01, .05):
        for r in (1, 2, 5, 17):
            epsilon = np.sqrt(t*n/(r*np.sqrt(k)))
            actual = np.trace(np.linalg.matrix_power(ef(epsilon)@u0, r*k))/n
            effective = np.trace(np.linalg.matrix_power(eh(epsilon**2/n)@u0, r*k))/n
            bound = r*k*(epsilon**3*loop_constant+epsilon**2*sine_residual/2)
            assert abs(actual-effective) <= bound+2e-10
            replicas.append({"t": t, "replicas": r, "epsilon": float(epsilon),
                             "trace": [float(actual.real), float(actual.imag)],
                             "effective_trace": [float(effective.real), float(effective.imag)],
                             "trace_error": float(abs(actual-effective)), "trace_bound": float(bound)})
    return {"K": k, "N": n, "exact_h_over_pi": [[list(a), c] for a, c in sorted(h_over_pi.items())],
            "exact_orbit_invariants": invariants, "exact_Gamma_over_pi_squared": gamma_over_pi_squared,
            "floating_sine_residual": float(sine_residual), "loop_checks": rows,
            "replica_checks": replicas,
            "scope": "Fourier coefficients and orbit invariants exact; matrix errors are double-precision diagnostics."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = {"exact_algebra": lattice_phase_checks(), "physical_diagnostic": physical_check(),
              "repeated_period_obstruction": repeated_period_obstruction(),
              "centered_coupling_exact_bounds": centered_coupling_bound(),
              "pair_multiplicity_exact_checks": pair_multiplicity_check(),
              "normal_form_floating_diagnostic": normal_form_diagnostic(),
              "coboundary_second_order_diagnostic": coboundary_second_order_diagnostic()}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
