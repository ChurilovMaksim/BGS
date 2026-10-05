#!/usr/bin/env python3
"""Exact mixed-trace generator and finite FLOW-015 controls.

Fraction Laurent polynomials are compared with a separately implemented
radial generator. NumPy quadrature and finite differences are diagnostics,
not asymptotic proofs or simulated Brownian endpoints.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
from fractions import Fraction as Q
import hashlib
from itertools import combinations, combinations_with_replacement
import json
from pathlib import Path
import platform

import numpy as np
from numpy.polynomial.legendre import leggauss

from quadratic_noise_clock import alias_kernel


def clean(pol):
    return {key: value for key, value in pol.items() if value}


def add(left, right, coefficient=Q(1)):
    out = defaultdict(Q, left)
    for key, value in right.items():
        out[key] += coefficient*value
    return clean(out)


def multiply(left, right):
    out = defaultdict(Q)
    for a, ca in left.items():
        for b, cb in right.items():
            out[tuple(x+y for x, y in zip(a, b))] += ca*cb
    return clean(out)


def power_trace(n, m):
    if not m:
        return {(0,)*n: Q(n)}
    out = {}
    for j in range(n):
        key = [0]*n
        key[j] = m
        out[tuple(key)] = Q(1)
    return out


def expand_word(n, word):
    out = {(0,)*n: Q(1)}
    for m in word:
        out = multiply(out, power_trace(n, m))
    return out


def trace_generator(n, word):
    """D5 in trace symbols; zero powers explicitly contribute N."""
    out = defaultdict(Q)

    def term(w, c):
        zeros = w.count(0)
        out[tuple(sorted(m for m in w if m))] += c*n**zeros

    term(list(word), -Q(sum(abs(m) for m in word), 2))
    for i, m in enumerate(word):
        assert m != 0
        sign = 1 if m > 0 else -1
        for b in range(1, abs(m)):
            term(list(word[:i]+word[i+1:]) + [sign*b, m-sign*b],
                 -Q(abs(m), 2*n))
    for i, j in combinations(range(len(word)), 2):
        w = [m for a, m in enumerate(word) if a not in (i, j)]
        term(w+[word[i]+word[j]], -Q(word[i]*word[j], n))
    return clean(out)


def expand_symbolic(n, symbolic):
    out = {}
    for word, coefficient in symbolic.items():
        out = add(out, expand_word(n, word), coefficient)
    return out


def radial_generator(n, pol):
    """D2 directly on symmetric Laurent polynomials, without traces.

    D_j=z_j*d/dz_j; angular diffusion is -sum(D_j^2)/(2N).
    For each antisymmetric pair, divide (D_j-D_k)F by z_j-z_k
    using the exact finite geometric sum, then multiply z_j+z_k.
    """
    out = {a: -Q(sum(x*x for x in a), 2*n)*c for a, c in pol.items()}
    out = defaultdict(Q, out)
    for j, k in combinations(range(n), 2):
        for exponents, c in pol.items():
            a, b = exponents[j], exponents[k]
            swapped = list(exponents)
            swapped[j], swapped[k] = b, a
            assert pol.get(tuple(swapped), Q(0)) == c
            if a <= b:
                continue
            d = a-b
            coefficient = -Q(d, 2*n)*c
            for r in range(d):
                for shift_j, shift_k in ((1, 0), (0, 1)):
                    key = list(exponents)
                    key[j] = a-1-r+shift_j
                    key[k] = b+r+shift_k
                    out[tuple(key)] += coefficient
    return clean(out)


def partitions(q, largest=None):
    if q == 0:
        yield ()
        return
    for a in range(min(q, largest or q), 0, -1):
        for tail in partitions(q-a, a):
            yield (a,)+tail


def neutral_words(qmax):
    for q in range(qmax+1):
        for a in partitions(q):
            for b in partitions(q):
                yield tuple(sorted(a+tuple(-m for m in b)))


def homogeneous(n, r, sign=1):
    pol = {}
    for indices in combinations_with_replacement(range(n), r):
        key = [0]*n
        for i in indices:
            key[i] += sign
        pol[tuple(key)] = Q(1)
    return pol


def entropy_geometry_checks():
    """Finite rational cyclic-gap and independently intersected-window checks.

    A finite event volume is checked; Poisson nullity and infinite entropy
    are analytic statements, not conclusions of this enumeration.
    """
    cases = 0
    minimum_probability = Q(1)
    for n in (3, 5, 7, 9):
        designs = [[Q(1)]*n, [Q(n)]+[Q(0)]*(n-1)]
        for phase in range(8):
            raw = [((i+phase)**2+3*i) % 13 for i in range(n)]
            assert sum(raw) > 0
            designs.append([Q(n*a, sum(raw)) for a in raw])
        for gaps in designs:
            assert sum(gaps) == n
            d = min(gaps)
            assert 0 <= d <= 1
            expected_probability = (2-d)/n
            for offset in (Q(0), Q(n, 4), Q(3*n, 4), Q(6*n, 7)):
                intervals = []
                for lift in range(-2, 2):
                    a = offset+lift*n
                    lower = max(Q(0), -a, -a-d)
                    upper = min(Q(n), 2-a, 2-a-d)
                    if lower < upper:
                        intervals.append((lower, upper))
                # Distinct period copies cannot fit in this length-two window.
                assert all(left[1] <= right[0] for left, right in
                           zip(sorted(intervals), sorted(intervals)[1:]))
                probability = sum((b-a for a, b in intervals), Q(0))/n
                assert probability == expected_probability
                assert probability >= Q(1, n)
                minimum_probability = min(minimum_probability, probability)
                cases += 1
    low, high = Q(7807, 10000), Q(7808, 10000)
    assert 2*low*low+low-2 < 0 < 2*high*high+high-2
    # The monotone quadratic brackets (sqrt(17)-1)/4 exactly.
    return {"rational_cyclic_designs": 40, "window_volume_cases": cases,
        "dimensions": [3, 5, 7, 9], "window_length": 2,
        "min_positive_event_probability": str(minimum_probability),
        "D17_constant_rational_bracket": [str(low), str(high)],
        "non_claim": "No enumeration proves the zero Poisson probability or entropy theorem"}


def exact_checks():
    signed = set()
    for k in range(1, 4):
        signed.update(combinations_with_replacement((-3, -2, -1, 1, 2, 3), k))
    neutral = set(neutral_words(4))
    words = sorted(signed | neutral)
    cases, max_monomials = 0, 0
    for n in (2, 3, 4):
        for word in words:
            pol = expand_word(n, word)
            direct = radial_generator(n, pol)
            symbolic = expand_symbolic(n, trace_generator(n, word))
            assert direct == symbolic, (n, word)
            cases += 1
            max_monomials = max(max_monomials, len(pol), len(direct))
    closure_cases = 0
    closure_words = set(neutral_words(6))
    for n in (3, 5, 7):
        for word in sorted(closure_words):
            q = sum(m for m in word if m > 0)
            for target in trace_generator(n, word):
                assert sum(target) == 0
                assert sum(m for m in target if m > 0) <= q
                assert target in closure_words
            closure_cases += 1
    # D7 coefficients are checked against literal independently supplied rows.
    d7_cases = 0
    for n in (2, 3, 5, 7):
        x, y, z, zbar, w = (-1, 1), (-2, 2), (-1, -1, 2), (-2, 1, 1), (-1, -1, 1, 1)
        expected = {
            x: {(): Q(1), x: Q(-1)},
            y: {(): Q(4), y: Q(-2), z: -Q(1, n), zbar: -Q(1, n)},
            z: {z: Q(-2), w: -Q(1, n), y: -Q(1, n), x: Q(4, n)},
            w: {w: Q(-2), z: -Q(1, n), zbar: -Q(1, n), x: Q(4)},
        }
        for word, row in expected.items():
            assert trace_generator(n, word) == row
            d7_cases += 1
    # Independent character eigenmode controls; the all-r formula is analytic.
    character_cases = 0
    for n in (2, 3, 4):
        for r in range(1, 5):
            chi = add(multiply(homogeneous(n, r), homogeneous(n, r, -1)),
                      multiply(homogeneous(n, r-1), homogeneous(n, r-1, -1)), Q(-1))
            gamma = Q(r*(r+n-1), n)
            assert radial_generator(n, chi) == {a: -gamma*c for a, c in chi.items()}
            character_cases += 1
    return {"coefficient_domain": "Fraction Laurent coefficients over Q",
            "dimensions": [2, 3, 4], "distinct_words": len(words),
            "signed_words": len(signed), "neutral_words_q_le_4": len(neutral),
            "direct_radial_vs_trace_cases": cases, "max_laurent_monomials": max_monomials,
            "closure_q_max": 6, "closure_words": len(closure_words),
            "closure_dimensions": [3, 5, 7], "closure_cases": closure_cases,
            "literal_D7_cases": d7_cases, "character_cases": character_cases,
            "trace_relations": "Not assumed independent when q>=N",
            "entropy_and_stationarity_geometry": entropy_geometry_checks()}


def bump(x, width, amplitude, derivatives=False):
    u = 2*np.asarray(x)/width
    mask = abs(u) < 1
    f = np.zeros_like(u)
    fp, fpp = np.zeros_like(u), np.zeros_like(u)
    v = u[mask]
    den = 1-v*v
    f[mask] = amplitude*np.exp(1-1/den)
    if derivatives:
        first = -4*v/(width*den**2)
        second = -8*(1+3*v*v)/(width**2*den**3)
        fp[mask] = f[mask]*first
        fpp[mask] = f[mask]*(first**2+second)
        return f, fp, fpp
    return f


def laplace_integral(angles, width, amplitude, origin_nodes_per_unit=512):
    n = len(angles)
    origin = np.arange(n*origin_nodes_per_unit)/origin_nodes_per_unit
    x = n*np.asarray(angles)/(2*np.pi)
    difference = (x[:, None]-origin[None, :]+n/2) % n-n/2
    f = bump(difference, width, amplitude)
    return float(np.mean(np.exp(-f.sum(axis=0))))


def generator_integral(angles, width, amplitude, origin_nodes_per_unit=4096):
    n = len(angles)
    origin = np.arange(n*origin_nodes_per_unit)/origin_nodes_per_unit
    x = n*np.asarray(angles)/(2*np.pi)
    difference = (x[:, None]-origin[None, :]+n/2) % n-n/2
    f, fp, fpp = bump(difference, width, amplitude, True)
    z = np.exp(-f.sum(axis=0))
    diffusion = n/(8*np.pi**2)*np.sum(fp**2-fpp, axis=0)
    drift = np.zeros_like(origin)
    for j, k in combinations(range(n), 2):
        drift -= (fp[j]-fp[k])/(4*np.pi*np.tan((angles[j]-angles[k])/2))
    return float(np.mean(z*(diffusion+drift)))


def finite_difference_generator(angles, width, amplitude, step):
    n = len(angles)
    base = laplace_integral(angles, width, amplitude)
    value = 0.
    for j in range(n):
        plus, minus = np.array(angles), np.array(angles)
        plus[j] += step
        minus[j] -= step
        fp = laplace_integral(plus, width, amplitude)
        fm = laplace_integral(minus, width, amplitude)
        first = (fp-fm)/(2*step)
        second = (fp+fm-2*base)/step**2
        force = sum(1/np.tan((angles[j]-angles[k])/2) for k in range(n) if k != j)
        value += (second+force*first)/(2*n)
    return value


def quadrature_checks():
    nodes, weights = leggauss(128)
    flat_cases, worst_flat, worst_flat_generator = 0, 0., 0.
    for n in (3, 5, 9):
        base = 2*np.pi*np.arange(n)/n
        perturbed = base.copy()
        perturbed[0] += n**-4
        warped = base+2*np.pi/n*.1*np.sin(base)
        for angles in (base, perturbed, warped):
            gaps = np.diff(np.r_[np.sort(angles), np.sort(angles)[0]+2*np.pi])*n/(2*np.pi)
            for width in (.4, .7):
                assert min(gaps) > width
                for amplitude in (.25, 1.2):
                    h = -np.expm1(-bump(width*nodes/2, width, amplitude))
                    a = float(np.dot(weights*width/2, h))
                    value = laplace_integral(angles, width, amplitude)
                    generator = generator_integral(angles, width, amplitude)
                    error = abs(value-(1-a))
                    assert error < 3e-12
                    assert abs(generator) < 2e-9
                    worst_flat = max(worst_flat, error)
                    worst_flat_generator = max(worst_flat_generator, abs(generator))
                    flat_cases += 1
    derivative_rows = []
    for n in (3, 5, 9):
        angles = 2*np.pi*np.arange(n)/n
        for warped in (False, True):
            if warped:
                angles = angles+2*np.pi/n*.1*np.sin(angles)
            exact_integral = generator_integral(angles, 1.6, .8)
            coarse = finite_difference_generator(angles, 1.6, .8, 2e-4)
            fine = finite_difference_generator(angles, 1.6, .8, 1e-4)
            extrapolated = (4*fine-coarse)/3
            error = abs(extrapolated-exact_integral)
            assert error < 2e-7
            derivative_rows.append({"N": n, "warped": warped,
                "D3_integral": exact_integral, "finite_difference_radial": extrapolated,
                "absolute_error": error})
    convergence = []
    clock9 = 2*np.pi*np.arange(9)/9
    for count in (512, 1024, 2048, 4096):
        convergence.append({"nodes_per_unit": count,
            "narrow_clock9_generator_residual": generator_integral(clock9, .4, 1.2, count)})
    return {"flat_cases": flat_cases, "laplace_origin_nodes_per_unit": 512,
        "generator_origin_nodes_per_unit": 4096,
        "generator_quadrature_convergence": convergence,
        "bump_integral_Gauss_nodes": 128,
        "max_flat_laplace_error": worst_flat,
        "max_flat_generator_residual": worst_flat_generator,
        "wide_support_generator_cases": derivative_rows,
        "tolerances": {"flat_laplace": 3e-12, "flat_generator": 2e-9, "D3": 2e-7}}


def fredholm_checks():
    width, amplitude = .7, 1.2
    sine_rows = []
    for q in (32, 48, 96):
        nodes, weights = leggauss(q)
        nodes, weights = width*nodes/2, width*weights/2
        h = -np.expm1(-bump(nodes, width, amplitude))
        root = np.sqrt(weights*h)
        op = root[:, None]*np.sinc(nodes[:, None]-nodes[None, :])*root[None, :]
        eig = np.linalg.eigvalsh(op)
        assert min(eig) > -1e-13 and max(eig) < 1
        a = float(np.trace(op))
        e2 = float((a*a-np.trace(op@op))/2)
        value = float(np.linalg.det(np.eye(q)-op))
        defect = value-1+a
        lower = (1-a/3)*e2
        assert e2 > 0 and defect >= lower-3e-14
        sine_rows.append({"quadrature_nodes": q, "a_f": a, "Laplace": value,
            "defect": defect, "D16_lower_bound": lower})
    assert abs(sine_rows[-1]["defect"]-sine_rows[-2]["defect"]) < 2e-11
    # Actual finite clock heat kernels: not sampling, not a limiting certificate.
    n, q, origin_count, aliases = 31, 48, 32, 20
    nodes, weights = leggauss(q)
    nodes, weights = width*nodes/2, width*weights/2
    h = -np.expm1(-bump(nodes, width, amplitude))
    root = np.sqrt(weights*h)
    initial = 1-float(np.dot(weights, h))
    clock_rows = []
    for nt in (.25, 1., 4., 16.):
        values = []
        for u in np.arange(origin_count)/origin_count:
            angles = 2*np.pi*(nodes+u)/n
            kernel = 2*np.pi/n*alias_kernel(n, nt/n, angles, angles, rmax=aliases)
            value = np.linalg.det(np.eye(q)-root[:, None]*kernel*root[None, :])
            assert abs(value.imag) < 2e-11
            assert -1e-11 < value.real <= 1+1e-11
            values.append(value.real)
        average = float(np.mean(values))
        assert average >= initial-1e-11
        # The analytic bound is strictly positive. Do not report an
        # underflowed binary64 zero as a rigorous zero tail.
        log_tail = float(np.log(2)-nt*(aliases+1)*aliases/2
                         -np.log1p(-np.exp(-nt*(aliases+1))))
        tail = float(np.exp(log_tail))
        clock_rows.append({"N": n, "Nt": nt, "origin_average_Laplace": average,
            "initial_flat_Laplace": initial, "defect": average-initial,
            "normalized_kernel_omitted_alias_bound": tail if tail > 0 else None,
            "omitted_alias_log_bound_binary64": log_tail,
            "alias_bound_underflows_binary64": tail == 0})
    return {"width": width, "amplitude": amplitude,
        "sine_quadratures": sine_rows, "finite_clock_heat": clock_rows,
        "finite_clock_quadrature_nodes": q, "finite_clock_origin_nodes": origin_count,
        "clock_alias_range": [-aliases, aliases],
        "scope": "Finite determinant quadrature; no all-N certificate or endpoint sampling"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    data = {"claim_id": "BGS-FLOW-015", "status": "PASS",
        "versions": {"Python": platform.python_version(), "NumPy": np.__version__},
        "exact": exact_checks(), "quadrature": quadrature_checks(),
        "fredholm": fredholm_checks(),
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "non_claims": ["No finite computation establishes the all-order flatness theorem",
            "No actual frozen-map noise removal or Heisenberg cancellation",
            "No all-N analytic, priority or Lean certificate",
            "No simulation of the original enormous-step chain",
            "Character tests have bounded r and N, not all highest weights"]}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, indent=2)+"\n")
    print(json.dumps({"status": data["status"], "exact_cases": data["exact"]["direct_radial_vs_trace_cases"],
        "flat_cases": data["quadrature"]["flat_cases"], "output": str(args.output)}))


if __name__ == "__main__":
    main()
