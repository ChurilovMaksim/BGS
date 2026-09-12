#!/usr/bin/env python3
"""Exact arithmetic for general hyperbolic cat maps; separate matrix checks."""
from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import product
import json
from math import isqrt
from pathlib import Path

import numpy as np

from periodic_point_trace_comparison import act, balanced_weyl, matmul, omega


IDENTITY = ((1, 0), (0, 1))


def power(a, exponent):
    result = IDENTITY
    while exponent:
        if exponent % 2:
            result = matmul(result, a)
        a = matmul(a, a)
        exponent //= 2
    return result


def lucas(t, m):
    return power(((t, -1), (1, 0)), m)[1][0]


def removed_power(t):
    if t % 2 == 0:
        return 1
    value, result = t*t-1, 1
    while value % 2 == 0:
        value //= 2
        result *= 2
    return result


def refinement(v):
    return (v[0]*v[1]+v[0]+v[1]) % 2


def det(a):
    return a[0][0]*a[1][1]-a[0][1]*a[1][0]


def arithmetic_controls():
    matrices = [((a, b), (c, d)) for a, b, c, d in product(range(-4, 5), repeat=4)
                if a*d-b*c == 1 and abs(a+d) > 2]
    cases = preimages = phase_checks = excluded = 0
    traces, mod_two = set(), set()
    frequencies = ((1, 0), (0, 1), (1, 1), (-2, 1))
    for a in matrices:
        t = a[0][0]+a[1][1]
        delta, q = t*t-4, removed_power(t)
        traces.add(t)
        mod_two.add(tuple(x % 2 for row in a for x in row))
        ainv = ((a[1][1], -a[0][1]), (-a[1][0], a[0][0]))
        for m in ((3, 5, 7) if t % 2 == 0 else (3, 9, 15)):
            b = lucas(t, m)
            assert b > 0 and b % q == 0
            n, k = b//q, 2*m
            assert n % 2 == 1
            if n == 1:
                excluded += 1
                continue
            ak = power(a, k)
            defect = tuple(tuple(IDENTITY[i][j]-ak[i][j] for j in range(2))
                           for i in range(2))
            determinant = det(defect)
            assert all(x % (2*n) == 0 for row in defect for x in row)
            assert abs(determinant) == delta*q*q*n*n
            for v in frequencies:
                assert refinement(act(a, v)) == refinement(v)
                for w in frequencies:
                    polar = refinement(v)+refinement(w)-refinement(
                        (v[0]+w[0], v[1]+w[1]))
                    phase_exponent = n*polar+(n+1)*omega(v, w)
                    assert (phase_exponent-omega(v, w)) % (2*n) == 0
                    phase_checks += 1
            for z in frequencies:
                initial = (
                    Fraction(n*(defect[1][1]*z[0]-defect[0][1]*z[1]), determinant),
                    Fraction(n*(-defect[1][0]*z[0]+defect[0][0]*z[1]), determinant))
                value = initial
                for j in range(k):
                    assert all((delta*q*q*x).denominator == 1 for x in value)
                    forcing = (n*z[0], n*z[1]) if j == 0 else (0, 0)
                    value = act(ainv, (value[0]-forcing[0], value[1]-forcing[1]))
                assert value == initial
                preimages += 1
            cases += 1
    assert len(mod_two) == 6
    return {"matrices": len(matrices), "admissible_dimension_cases": cases,
            "excluded_N_equals_one": excluded, "traces": sorted(traces),
            "distinct_mod_two_matrices": len(mod_two),
            "exact_cyclic_preimages": preimages, "exact_Weyl_phase_checks": phase_checks}


def prime_divisor_other_than_five(value):
    for p in range(3, value+1, 2):
        if value % p == 0 and p != 5:
            # The first divisor other than five is prime after removing fives.
            assert all(p % d for d in range(2, isqrt(p)+1))
            return p
    raise AssertionError("No eligible prime")


def orbit_period(a, v, n, maximum):
    start = tuple(x % n for x in v)
    value = start
    for d in range(1, maximum+1):
        value = tuple(x % n for x in act(a, value))
        if value == start:
            return d
    raise AssertionError("Expected modular period missing")


def centered_construction_controls():
    trace_cases = []
    for t in range(-16, 17):
        if abs(t) <= 2:
            continue
        b5 = lucas(t, 5)
        assert b5 == t**4-3*t*t+1 and b5 % 2 == 1 and b5 > 5
        p = prime_divisor_other_than_five(b5)
        assert (t*t-4) % p != 0
        assert lucas(t, 5*p) % (p*p) == 0
        a = ((t, -1), (1, 0))
        h = orbit_period(a, (1, 0), p, 10)
        assert h in (5, 10)
        trace_cases.append({"trace": t, "prime": p, "orbit_period_mod_prime": h})
    rows = []
    for t in (-3, 3, 4, 6):
        a = ((t, -1), (1, 0))
        p, q = prime_divisor_other_than_five(lucas(t, 5)), removed_power(t)
        factor = (15 if t % 2 else 5)*p
        periods = [factor*(4*2**(2**j)+2) for j in (1, 2)]
        moduli = [lucas(t, k//2)//q for k in periods]
        for j, (k, n) in enumerate(zip(periods, moduli), start=1):
            assert n % (p*p) == 0 and n % 2 == 1
            h = orbit_period(a, (n//p, 0), n, k)
            assert h in (5, 10) and k % h == 0
            older = [orbit_period(a, (old//p, 0), n, k) for old in moduli[:j-1]]
            assert all(d == k for d in older)
            rows.append({"trace": t, "j": j, "K": k, "N_bits": n.bit_length(),
                         "p": p, "own_mode_period": h, "older_mode_periods": older})
    return {"prime_lifting_exact_cases": trace_cases,
            "centered_alias_exact_cases": rows,
            "scope": "Exact divisibility and finite orbit checks; no dense large-N matrices."}


def universal_weyl(v, n):
    # Reduction modulo 2N avoids avoidable floating argument growth.
    v = tuple(x % (2*n) for x in v)
    return (-1)**(v[0]+v[1])*balanced_weyl(v, n)


def central_weyl(v, n):
    v = tuple(x % n for x in v)
    return (-1)**(v[0]*v[1])*balanced_weyl(v, n)


def capped_kernel_controls():
    """Exact dyadic envelope for the logarithmic phase-kernel estimate."""
    masses = (1, 2, 3, 17, 2**20, 2**200)
    checks = 0
    for constant, x, y in product((1, 17), masses, masses):
        height = constant*x*y
        cutoff = (height-1).bit_length()
        one_sided = sum(min(2, Fraction(height, 2**d))
                        for d in range(cutoff+1))+Fraction(height, 2**cutoff)
        bilateral = 2*one_sided-min(2, height)
        assert bilateral <= 4*cutoff+6
        assert bilateral <= ((4*constant.bit_length()+10)
                             *(1+x.bit_length())*(1+y.bit_length()))
        checks += 1
    return {"exact_infinite_dyadic_sum_checks": checks,
            "maximum_particle_mass_bits": max(masses).bit_length(),
            "scope": "Exact envelope checks; the Gevrey tree and quasi-norm arguments are analytic proofs."}


def physical_quantization_checks():
    """Construct the intertwiner from images of clock and shift."""
    rows = []
    for a, m in ((((3, 2), (1, 1)), 3),
                 (((6, 5), (1, 1)), 3),
                 (((3, 4), (2, 3)), 3),
                 (((3, -1), (1, 0)), 9)):
        t, k = a[0][0]+a[1][1], 2*m
        n = lucas(t, m)//removed_power(t)
        image_clock = central_weyl(act(a, (1, 0)), n)
        image_shift = central_weyl(act(a, (0, 1)), n)
        values, vectors = np.linalg.eig(image_clock)
        index = np.argmin(abs(values-1))
        assert abs(values[index]-1) < 1e-10
        vacuum = vectors[:, index]
        vacuum /= np.linalg.norm(vacuum)
        columns, value = [], vacuum
        for _ in range(n):
            columns.append(value)
            value = image_shift@value
        u = np.column_stack(columns)
        kth = np.linalg.matrix_power(u, k)
        phase = np.trace(kth)/n
        u *= np.exp(-1j*np.angle(phase)/k)
        parity = np.eye(n)[(-np.arange(n)) % n]
        errors = [np.linalg.norm(u.conj().T@u-np.eye(n), 2),
                  np.linalg.norm(np.linalg.matrix_power(u, k)-np.eye(n), 2),
                  np.linalg.norm(u@parity-parity@u, 2)]
        for v in ((1, 0), (0, 1), (1, 1), (-2, 1)):
            errors.append(np.linalg.norm(
                u@universal_weyl(v, n)@u.conj().T-universal_weyl(act(a, v), n), 2))
        assert max(errors) < 2e-9
        assert np.linalg.norm(universal_weyl((n, 0), n)+np.eye(n), 2) < 1e-10
        rows.append({"A": a, "K": k, "N": n, "maximum_matrix_residual": float(max(errors))})
    return {"cases": rows, "scope": "Double precision, not interval-certified unitary identities."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = {"exact_general_arithmetic": arithmetic_controls(),
              "exact_centered_counterexamples": centered_construction_controls(),
              "exact_capped_phase_kernel": capped_kernel_controls(),
              "physical_quantization_diagnostics": physical_quantization_checks()}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
