#!/usr/bin/env python3
"""Exact finite gap and cubic-resonance controls for analytic position kicks."""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import argparse
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations_with_replacement, product
import json
from pathlib import Path
import random
from math import gcd

from even_period_spin_resonance import recurrence
from pell_resonance_lattice import inverse


def alpha_power(n):
    """(1+sqrt(2))**n as an exact pair of integers."""
    a, b = 1, 0
    for _ in range(n):
        a, b = a+2*b, a+b
    return a, b


def rational_dominates_surd(x, a, b):
    assert b >= 0
    residual = x-a
    return residual >= 0 and residual*residual >= 2*b*b


def gap_controls():
    checks = 0
    for left, right in product(range(-3, 4), repeat=2):
        if left == right == 0:
            continue
        start = (Q(left, 16), Q(right, 16))
        current = start
        invariant = start[1]**2-6*start[0]*start[1]+start[0]**2
        assert abs(invariant) >= Q(1, 256)
        for gap in range(1, 25):
            assert current[1]**2-6*current[0]*current[1]+current[0]**2 == invariant
            endpoint_sum = sum(map(abs, start))+sum(map(abs, current))
            a, b = alpha_power(gap-1)
            assert rational_dominates_surd(100*endpoint_sum, a, b)
            current = current[1], 6*current[1]-current[0]
            checks += 1
    return {"exact_rational_homogeneous_gaps": checks,
            "initial_numerators": [-3, 3], "denominator": 16, "max_gap": 24}


def finite_component_controls():
    checked = 0
    for length in range(1, 8):
        for values in product((-1, 0, 1), repeat=length):
            if not values[0] or not values[-1]:
                continue
            if any(values[j] == values[j+1] == 0 for j in range(length-1)):
                continue
            p = (0, 0)+values+(0, 0)
            c = [p[j-1]-6*p[j]+p[j+1] for j in range(1, len(p)-1)]
            support = [j for j, value in enumerate(c) if value]
            assert len(support) >= 3
            rhs_a = rhs_b = 0
            for i, j in zip(support, support[1:]):
                a, b = alpha_power(j-i-1)
                rhs_a += a
                rhs_b += b
            assert rational_dominates_surd(100*sum(map(abs, c)), rhs_a, rhs_b)
            checked += 1
    return {"exhaustive_finite_components": checked,
            "alphabet": [-1, 0, 1], "maximum_hull_length": 7}


def winding_controls():
    rng = random.Random(110934)
    checked = 0
    for k in (6, 10, 14, 18, 22):
        for r in range(16):
            for s in range(2):
                for _ in range(10):
                    p = [Q(-3*r-s if j % 2 == 0 else -r-3*s, 16)
                         +rng.randrange(-2, 3) for j in range(k)]
                    if any(p[j] == p[(j+1) % k] == 0 for j in range(k)):
                        continue
                    c = [p[(j-1) % k]-6*p[j]+p[(j+1) % k] for j in range(k)]
                    assert all(value.denominator == 1 for value in c)
                    support = [j for j, value in enumerate(c) if value]
                    assert support
                    rhs_a = rhs_b = 0
                    for i, j in zip(support, support[1:]+[support[0]+k]):
                        a, b = alpha_power(j-i-1)
                        rhs_a += a
                        rhs_b += b
                    assert rational_dominates_surd(100*sum(map(abs, c)), rhs_a, rhs_b)
                    checked += 1
    return {"seed": 110934, "seeded_cyclic_gap_checks": checked,
            "fractional_classes": 32}


def cubic_resonance_controls(k):
    """Every ordered cubic atom word for f=2cos(q)+(2/5)cos(6q).

    A scalar 1/3! converts the atom orders into the exponential coefficients.
    Atoms are sorted by physical kick site before their Weyl multiplication.
    The central phase histogram is exact, including repeated sites.
    """
    a = 1
    n = recurrence(k)[k//2]
    orbit, v = [], (1, 0)
    for _ in range(k):
        orbit.append(v)
        v = ((3*v[0]+4*v[1]) % n, (2*v[0]+3*v[1]) % n)
    atoms = [(j, mode, Q(1) if abs(mode) == 1 else Q(1, 5))
             for j in range(k) for mode in (-6, -1, 1, 6)]
    half = pow(2, -1, n)
    histogram = Counter()
    central_words = 0
    for word in product(atoms, repeat=3):
        total, phase, coefficient = [0, 0], 0, Q(1, 6)
        for site, mode, amplitude in sorted(word):
            w = [a*mode*x for x in orbit[site]]
            phase += half*(total[0]*w[1]-total[1]*w[0])
            total = [(x+y) % n for x, y in zip(total, w)]
            coefficient *= amplitude
        if total == [0, 0]:
            histogram[phase % n] += coefficient
            central_words += 1
    expected = {(-6*a*a) % n: 2*k*Q(1, 5)}
    winding = None
    if k == 10:
        # 6*v_0+6*v_4+v_7 = v_9+v_1+v_3+v_5+v_7 = 0 mod N.
        # This noninteger class was missed by the initial cubic prediction.
        expected[210] = Q(4, 5)
        c = [6, 0, 0, 0, 6, 0, 0, 1, 0, 0]
        lap = [[-6*int(i == j)+int(i == (j-1) % k)+int(i == (j+1) % k)
                for j in range(k)] for i in range(k)]
        p = [sum(value*coefficient for value, coefficient in zip(row, c))
             for row in inverse(lap)]
        fractions = [value-value//1 for value in p]
        assert fractions == [Q(15, 16) if j % 2 == 0 else Q(13, 16) for j in range(k)]
        winding = {"aggregate": c, "fractional_preimage": [str(v) for v in fractions],
                   "Weyl_phase": 210,
                   "mechanism": "Pair adjacent terms in the length-five parity-orbit sum."}
    assert histogram == expected, (k, dict(histogram))
    return {"K": k, "N": n, "ordered_atom_words": len(atoms)**3,
            "central_atom_words": central_words,
            "exact_phase_histogram_before_factor_minus_i":
                {str(phase): str(coefficient) for phase, coefficient in histogram.items()},
            "winding_cubic_alias": winding,
            "scope": "Exact finite full-space cubic coefficient; no odd-projector correction is omitted."}


def replica_cubic_histogram(k, replicas, coefficients):
    """Independent unordered-atom expansion, with exact multiplicity factors."""
    n = recurrence(k)[k//2]
    orbit, v = [], (1, 0)
    for _ in range(k):
        orbit.append(v)
        v = ((3*v[0]+4*v[1]) % n, (2*v[0]+3*v[1]) % n)
    atoms = [(mode*orbit[j][0] % n, mode*orbit[j][1] % n, coefficient)
             for _ in range(replicas) for j in range(k)
             for mode, coefficient in sorted(coefficients.items())]
    half = pow(2, -1, n)
    histogram = Counter()
    checked = central = 0
    for i, j, ell in combinations_with_replacement(range(len(atoms)), 3):
        checked += 1
        x, y, z = atoms[i], atoms[j], atoms[ell]
        if (x[0]+y[0]+z[0]) % n or (x[1]+y[1]+z[1]) % n:
            continue
        central += 1
        phase = half*(x[0]*y[1]-x[1]*y[0]
                      +x[0]*z[1]-x[1]*z[0]+y[0]*z[1]-y[1]*z[0]) % n
        divisor = 6 if i == ell else (2 if i == j or j == ell else 1)
        histogram[phase] += x[2]*y[2]*z[2]/divisor
    return histogram, checked, central


def replica_cubic_controls():
    """Test the cubic orientation law against complete physical-time words."""
    cases = []
    for positive_modes, replicas in (
            ({1: Q(1), 6: Q(1, 5)}, (1, 2, 3, 5)),
            ({1: Q(1), 2: Q(1, 3), 6: Q(1, 5), 35: Q(1, 7)}, (1, 2))):
        coefficients = {sign*n: c for n, c in positive_modes.items() for sign in (-1, 1)}
        k = 10
        n = recurrence(k)[k//2]
        base = None
        for r in replicas:
            actual, checked, central = replica_cubic_histogram(k, r, coefficients)
            if r == 1:
                base = actual
            predicted = Counter()
            for phase, coefficient in base.items():
                predicted[phase] += r*r*(r+1)//2*coefficient
                predicted[-phase % n] += r*r*(r-1)//2*coefficient
            assert +actual == +predicted, (positive_modes, r, actual, predicted)
            cases.append({"K": k, "replicas": r,
                          "positive_modes": {str(m): str(c) for m, c in positive_modes.items()},
                          "unordered_atom_multisets": checked, "central_multisets": central,
                          "phase_histogram_before_minus_i":
                              {str(p): str(c) for p, c in sorted(actual.items())}})
    return cases


def classical_cubic_controls():
    """Exhaust all possible finite temporal triples for one finite alphabet.

    The stopping rule follows from (A7), not a guessed time cutoff.
    """
    positive = {1: Q(1), 2: Q(1, 3), 6: Q(1, 5), 35: Q(1, 7)}
    coefficients = {sign*n: c for n, c in positive.items() for sign in (-1, 1)}
    max_gap = 0
    while rational_dominates_surd(Q(300*max(positive)), *alpha_power(max_gap)):
        max_gap += 1
    b = recurrence(2*max_gap+2)
    correlations = []
    for d in range(1, max_gap+1):
        for gap in range(1, max_gap+1):
            e = d+gap
            divisor = gcd(gcd(b[d], b[e]), b[gap])
            primitive = (b[gap]//divisor, -b[e]//divisor, b[d]//divisor)
            value = Q(0)
            for first in coefficients:
                if first % primitive[0]:
                    continue
                multiplier = first//primitive[0]
                charges = [multiplier*t for t in primitive]
                value += coefficients[first]*coefficients.get(charges[1], 0)*coefficients.get(charges[2], 0)
            if value:
                correlations.append({"d": d, "e": e, "value": str(value),
                                     "primitive_relation": list(primitive)})
    onsite = sum((c*d*coefficients.get(-m-n, 0)
                  for m, c in coefficients.items() for n, d in coefficients.items()), Q(0))
    temporal = sum((Q(row["value"]) for row in correlations), Q(0))
    assert correlations == [
        {"d": 1, "e": 2, "value": "2/5", "primitive_relation": [1, -6, 1]},
        {"d": 1, "e": 3, "value": "2/35", "primitive_relation": [6, -35, 1]},
        {"d": 2, "e": 3, "value": "2/35", "primitive_relation": [1, -35, 6]}]
    assert onsite == 2 and onsite+6*temporal == Q(178, 35)
    return {"positive_modes": {str(m): str(c) for m, c in positive.items()},
            "proved_maximum_gap": max_gap,
            "onsite_third_moment": str(onsite),
            "temporal_triples": correlations, "classical_third_cumulant": str(onsite+6*temporal)}


def classified_cubic_controls(k):
    """Classify complete central cubic words by the exact rational preimage."""
    n = recurrence(k)[k//2]
    positive = {1: Q(1), 2: Q(1, 3), 6: Q(1, 5), 35: Q(1, 7)}
    modes = {sign*m: c for m, c in positive.items() for sign in (-1, 1)}
    lap = [[-6*int(i == j)+int(i == (j-1) % k)+int(i == (j+1) % k)
            for j in range(k)] for i in range(k)]
    inv = inverse(lap)
    orbit, v = [], (1, 0)
    for _ in range(k):
        orbit.append(v)
        v = ((3*v[0]+4*v[1]) % n, (2*v[0]+3*v[1]) % n)
    atoms = [(j, m, c, m*orbit[j][0] % n, m*orbit[j][1] % n)
             for j in range(k) for m, c in sorted(modes.items())]
    histograms = {name: Counter() for name in ("zero_aggregate", "finite_component", "winding")}
    half = pow(2, -1, n)
    checked = central = 0
    for i, j, ell in combinations_with_replacement(range(len(atoms)), 3):
        checked += 1
        x, y, z = atoms[i], atoms[j], atoms[ell]
        if (x[3]+y[3]+z[3]) % n or (x[4]+y[4]+z[4]) % n:
            continue
        central += 1
        phase = half*(x[3]*y[4]-x[4]*y[3]
                      +x[3]*z[4]-x[4]*z[3]+y[3]*z[4]-y[4]*z[3]) % n
        divisor = 6 if i == ell else (2 if i == j or j == ell else 1)
        coefficient = x[2]*y[2]*z[2]/divisor
        c = Counter()
        for atom in (x, y, z):
            c[atom[0]] += atom[1]
        if all(value == 0 for value in c.values()):
            category = "zero_aggregate"
        else:
            p = [sum((row[site]*value for site, value in c.items()), Q(0)) for row in inv]
            integer = all(value.denominator == 1 for value in p)
            has_cut = any(p[site] == p[(site+1) % k] == 0 for site in range(k))
            category = "finite_component" if integer and has_cut else "winding"
        histograms[category][phase] += coefficient
    expected_finite = Counter({-6 % n: 2*k*Q(1, 5), -210 % n: 4*k*Q(1, 35)})
    assert histograms["finite_component"] == expected_finite, (k, histograms)
    assert histograms["zero_aggregate"] == {0: Q(k, 3)}, (k, histograms)
    if k >= 34:
        # (A7) bounds each of the three winding gaps by 11 for |mode| <= 35.
        assert not histograms["winding"], (k, histograms)
    return {"K": k, "N": n, "unordered_atom_multisets": checked,
            "central_multisets": central,
            "classified_phase_histograms_before_minus_i":
                {name: {str(p): str(c) for p, c in sorted(hist.items())}
                 for name, hist in histograms.items()}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = {"scope": "Bounded exact checks; the analytic theorem is a separate proof, with independent review outstanding.",
              "homogeneous_gaps": gap_controls(),
              "finite_components": finite_component_controls(),
              "winding": winding_controls(),
              "cubic_resonance": [cubic_resonance_controls(k) for k in (10, 14, 18)],
              "replica_cubic": replica_cubic_controls(),
              "classical_cubic": classical_cubic_controls(),
              "classified_cubic": [classified_cubic_controls(k) for k in (10, 14, 18, 22, 34)]}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
