#!/usr/bin/env python3
"""Exact vector-phase/gap controls; a separate finite matrix diagnostic.

Finite checks support, but do not replace, the growing-parameter proofs
in mathematics/returns/phase_space_return_gas.md. No dense matrix is built at the
large moduli used for the regularity counterexample.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import argparse
from collections import defaultdict
from fractions import Fraction
import json
from math import gcd
from pathlib import Path
import random

import numpy as np

from periodic_point_trace_comparison import (
    A, act, balanced_weyl, first_order, matrix_power, norm, omega,
)
from even_period_spin_resonance import recurrence


def add(v, w):
    return v[0]+w[0], v[1]+w[1]


def quadratic_unit_power(h):
    """Exact (a,b) such that (1+sqrt(2))**h = a+b*sqrt(2)."""
    a, b = 1, 0
    for _ in range(h):
        a, b = a+2*b, a+b
    return a, b


def assert_ge_quadratic(x, pair):
    """Certify x >= a+b sqrt(2), using rational/integer arithmetic."""
    a, b = pair
    assert b >= 0
    difference = x-a
    assert difference >= 0 and difference*difference >= 2*b*b


def ordered_area(word):
    total, area = (0, 0), 0
    for v in word:
        area += omega(total, v)
        total = add(total, v)
    return total, area


def replica_phase_controls():
    rng = random.Random(221909)
    rows = []
    for k in (6, 10, 14, 34):
        n = recurrence(k//2)[k//2]
        powers = [matrix_power(j) for j in range(k)]
        full_powers = [matrix_power(j) for j in range(5*k)]
        counts = 0
        for r in (1, 2, 3, 5):
            for trial in range(20):
                profiles = [[(rng.randrange(-2, 3), rng.randrange(-2, 3))
                             for _ in range(k)] for _ in range(r)]
                if trial % 2 == 0:
                    for j in range(k):
                        profiles[-1][j] = tuple(
                            -sum(profiles[nu][j][d] for nu in range(r-1))
                            for d in range(2))
                transformed = [[act(powers[j], profiles[nu][j])
                                for j in range(k)] for nu in range(r)]
                original = ordered_area([v for replica in transformed for v in replica])
                grouped = ordered_area([transformed[nu][j]
                                        for j in range(k) for nu in range(r)])
                crossing = -2*sum(
                    omega(transformed[mu][i], transformed[nu][j])
                    for i in range(k) for j in range(i+1, k)
                    for nu in range(r) for mu in range(nu+1, r))
                aggregate = [tuple(sum(profiles[nu][j][d] for nu in range(r))
                                   for d in range(2)) for j in range(k)]
                aggregate_total, aggregate_area = ordered_area(
                    [act(powers[j], aggregate[j]) for j in range(k)])
                onsite = sum(omega(profiles[nu][j], profiles[mu][j])
                             for j in range(k) for nu in range(r)
                             for mu in range(nu+1, r))
                assert original[0] == grouped[0] == aggregate_total
                assert original[1] == grouped[1]+crossing
                assert grouped[1] == aggregate_area+onsite
                # Repeated Egorov periods may be reduced modulo 2N.
                actual = ordered_area([
                    act(full_powers[nu*k+j], profiles[nu][j])
                    for nu in range(r) for j in range(k)])
                assert all((x-y) % (2*n) == 0
                           for x, y in zip(actual[0], original[0]))
                assert (actual[1]-original[1]) % (2*n) == 0
                counts += 1
        m = k//2
        alpha = matrix_power(m)[0][0]
        e1, e2 = (1, 0), (0, 1)
        antipodal_word = [e1, act(powers[m], e2), (-1, 0),
                          act(powers[m], (0, -1))]
        total, area = ordered_area(antipodal_word)
        assert total == (0, 0) and area == 2*alpha
        assert area % (2*n) != 0 and gcd(alpha, n) == 1
        assert ordered_area([e1, e2, (-1, -1)]) == ((0, 0), 1)
        rows.append({"K": k, "N": n, "integer_word_checks": counts,
                     "antipodal_area_mod_2N": area % (2*n),
                     "onsite_area": 1})
    return {"seed": 221909, "cases": rows}


def gap_controls():
    endpoint_checks = 0
    powers = [matrix_power(h) for h in range(25)]
    for a in range(-5, 6):
        for b in range(-5, 6):
            if not (a or b):
                continue
            p = (Fraction(a, 32), Fraction(b, 32))
            assert omega(p, act(A, p)) != 0
            for h, power in enumerate(powers):
                endpoint_norm = norm([p, act(power, p)])
                assert_ge_quadratic(32*endpoint_norm, quadratic_unit_power(h))
                endpoint_checks += 1
    run_checks = 0
    for length in range(1, 31):
        for v in ((1, 0), (0, 1), (1, -1), (-2, 3)):
            p = [(0, 0)]+[act(matrix_power(length-j), v)
                           for j in range(1, length+1)]+[(0, 0)]
            c = first_order(p)
            forcing = [j for j, x in enumerate(c) if x != (0, 0)]
            assert forcing == [0, length]
            assert c[0] == tuple(-x for x in act(matrix_power(length), v))
            assert c[length] == v
            assert_ge_quadratic(128*norm(c), quadratic_unit_power(length-1))
            run_checks += 1
    return {"rational_endpoint_checks": endpoint_checks,
            "finite_two_force_run_checks": run_checks,
            "arithmetic": "Fractions and integer comparisons in Q(sqrt(2)); no floats."}


def atom_controls():
    representatives = ((1, 0), (0, 1), (1, 1))
    invariants = [omega(v, act(A, v)) for v in representatives]
    assert invariants == [2, -4, -2]
    support = representatives+tuple(tuple(-x for x in v) for v in representatives)
    checks = 0
    for d in range(1, 35):
        power = matrix_power(d)
        for v in support:
            for w in support:
                assert add(v, act(power, w)) != (0, 0)
                checks += 1
    # A nonzero finite component can have TWO sites and THREE original atoms.
    c0, c1 = (1, 1), (1, -1)
    assert add(c0, act(A, c1)) == (0, 0)
    assert c0 in support and add((1, 0), (0, -1)) == c1
    return {"orbit_quadratic_invariants": invariants,
            "finite_two_atom_exclusions": checks,
            "three_atom_two_site_witness": [list(c0), list(c1)]}


def convolution(a, b):
    result = defaultdict(complex)
    for v, coefficient in a.items():
        for w, other in b.items():
            result[add(v, w)] += coefficient*other
    return dict(result)


def onsite_matrix_diagnostic():
    """Finite Taylor polynomial, not an infinite-kick truncation certificate."""
    n, degree = 35, 4
    support = ((1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1))
    symbol = dict.fromkeys(support, 1.0)
    rows = []
    for epsilon in (.03, .09):
        coefficients, term = {(0, 0): 1.0}, {(0, 0): 1.0}
        for d in range(1, degree+1):
            term = {v: z*1j*epsilon/d for v, z in convolution(term, symbol).items()}
            for v, z in term.items():
                coefficients[v] = coefficients.get(v, 0)+z
        operator = sum(z*balanced_weyl(v, n) for v, z in coefficients.items())
        f0 = sum(abs(z) for z in coefficients.values())
        f1 = sum(norm([v])*abs(z) for v, z in coefficients.items())
        classical = {(0, 0): 1.0}
        for r in (1, 2, 3):
            classical = convolution(classical, coefficients)
            assert max(norm([v]) for v in classical) < n
            actual = np.trace(np.linalg.matrix_power(operator, r))/n
            reference = classical.get((0, 0), 0)
            error = abs(actual-reference)
            bound = np.pi/n*(r*(r-1)/2)*f1*f1*f0**(r-2)
            assert error <= bound+2e-12
            rows.append({"epsilon": epsilon, "replicas": r,
                         "matrix_classical_difference": float(error),
                         "phase_bound": float(bound)})
    return {"N": n, "Taylor_degree": degree, "cases": rows,
            "scope": "Double precision diagnostic of onsite Weyl-phase bound only."}


def orbit_period(v, n, k):
    target = tuple(x % n for x in v)
    value = target
    for d in range(1, k+1):
        value = tuple(x % n for x in act(A, value))
        if value == target:
            return d
    raise AssertionError("No modular return at K")


def early_return_controls():
    rows = []
    for k in (6, 10, 14, 34, 262):
        n = recurrence(k//2)[k//2]
        alpha = matrix_power(k//2)[0][0]
        vectors = ((1, 0), (0, 1), (1, 1),
                   (n//gcd(n, alpha-1), 0), (n, 0))
        for v in vectors:
            d = orbit_period(v, n, k)
            if d < k:
                x, y = quadratic_unit_power(d-1), quadratic_unit_power(k-d-1)
                assert_ge_quadratic(256*norm([v]), add(x, y))
            else:
                assert k == d
            rows.append({"K": k, "vector_norm_bits": norm([v]).bit_length(),
                         "orbit_period": d, "early": d < k})
        # Exact Egorov preserves the identity character Wcal_N(N,0).
        value = (1, 0)
        for _ in range(k):
            assert (value[0]*value[1]) % 2 == 0
            value = act(A, value)
    return {"cases": rows}


def regularity_counterexample_controls():
    ks = [4*2**(2**j)+2 for j in range(1, 13)]
    for j, (k, following) in enumerate(zip(ks, ks[1:]), start=1):
        assert k % 4 == 2
        assert following == (k-2)**2//4+2
        assert 5*following >= k*k
        if j >= 2:
            assert 4*(j+1)**2*k <= j*j*following
    ns = [recurrence(k//2)[k//2] for k in ks[:3]]
    rows = []
    for j, (k, n) in enumerate(zip(ks[:3], ns), start=1):
        assert orbit_period((n, 0), n, k) == 1
        older_periods = [orbit_period((old, 0), n, k) for old in ns[:j-1]]
        assert all(d == k for d in older_periods)
        rows.append({"j": j, "K": k, "N_bits": n.bit_length(),
                     "older_mode_periods": older_periods,
                     "own_mode_coefficient_in_X": 2*j})
    return {"exact_recurrence_and_tail_ratio_checks": len(ks)-1,
            "K_bit_lengths": [k.bit_length() for k in ks], "modular_cases": rows,
            "scope": "Finite arithmetic controls; summability and escape are proved in the note."}


def centered_counterexample_controls():
    assert recurrence(15)[15] % 25 == 0
    orbit, value = [], (1, 0)
    for _ in range(6):
        assert value[0]*value[1] % 2 == 0
        orbit.append(tuple(x % 5 for x in value))
        value = act(A, value)
    assert orbit == [(1, 0), (3, 2), (2, 2), (4, 0), (2, 3), (3, 3)]
    assert tuple(x % 5 for x in value) == (1, 0)
    # Coefficient counting in the exact group algebra of (Z/5Z)^2.
    counts = [sum((a*x+b*y) % 5 == 0 for a, b in orbit)
              for x in range(5) for y in range(5)]
    assert counts[0] == 6 and all(c < 6 for c in counts[1:])
    assert all(((5-a) % 5, (5-b) % 5) in orbit for a, b in orbit)
    assert (0, 0) not in orbit  # Zero normalized trace of the orbit sum.
    ks = [15*(4*2**(2**j)+2) for j in range(1, 4)]
    ns = [recurrence(k//2)[k//2] for k in ks]
    modular_rows = []
    for j, (k, n) in enumerate(zip(ks, ns), start=1):
        assert n % 25 == 0 and n % 2 == 1 and k % 6 == 0
        d = n//5
        assert orbit_period((d, 0), n, k) == 6
        older = [orbit_period((old//5, 0), n, k) for old in ns[:j-1]]
        assert all(period == k for period in older)
        modular_rows.append({"j": j, "K": k, "N_bits": n.bit_length(),
                             "own_mode_period": 6, "older_mode_periods": older,
                             "full_H_equals_one_rank": "N/25",
                             "odd_H_equals_one_rank": "(N/25-1)/2"})

    # Independent dense checks at modest M=25t: no cat-map propagator needed.
    matrix_rows = []
    for n in (25, 75, 125):
        d, t = n//5, n//25
        clock, shift = balanced_weyl((d, 0), n), balanced_weyl((0, d), n)
        projector = sum(np.linalg.matrix_power(clock, a)@np.linalg.matrix_power(shift, b)
                        for a in range(5) for b in range(5))/25
        parity = np.eye(n)[(-np.arange(n)) % n]
        h = sum(np.linalg.matrix_power(clock, a)@np.linalg.matrix_power(shift, b)
                for a, b in orbit)/6
        residuals = [np.linalg.norm(clock@shift-shift@clock, 2),
                     np.linalg.norm(projector@projector-projector, 2),
                     np.linalg.norm(h@projector-projector, 2),
                     np.linalg.norm(h-h.conj().T, 2)]
        assert max(residuals) < 2e-11
        assert abs(np.trace(h)) < 2e-11
        assert abs(np.trace(projector)-t) < 2e-11
        assert abs(np.trace(parity@projector)-1) < 2e-11
        eigs = np.linalg.eigvalsh(h)
        assert np.count_nonzero(abs(eigs-1) < 1e-10) == t
        odd_rank = np.trace((np.eye(n)-parity)@projector)/2
        assert abs(odd_rank-(t-1)/2) < 2e-11
        matrix_rows.append({"M": n, "joint_vacuum_rank": t,
                            "joint_vacuum_odd_rank": (t-1)//2,
                            "largest_matrix_residual": float(max(residuals))})
    return {"exact_orbit_mod_5": orbit, "exact_modular_cases": modular_rows,
            "floating_commuting_matrix_checks": matrix_rows,
            "scope": "Divisibility and orbit periods exact; physical projector checks floating."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = {
        "exact_replica_phases": replica_phase_controls(),
        "exact_vector_gaps": gap_controls(),
        "exact_atomic_degree": atom_controls(),
        "onsite_matrix_diagnostic": onsite_matrix_diagnostic(),
        "exact_early_return_checks": early_return_controls(),
        "exact_regularity_counterexample": regularity_counterexample_controls(),
        "centered_counterexample": centered_counterexample_controls(),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
