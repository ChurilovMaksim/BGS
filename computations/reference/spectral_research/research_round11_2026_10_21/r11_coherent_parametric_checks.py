#!/usr/bin/env python3
"""Exact arithmetic audit; no fixed-kick spectral simulation is performed."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json


ZERO = (F(0), F(0))


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def mul(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def conj(a):
    return a[0], -a[1]


def norm2(a):
    return a[0] * a[0] + a[1] * a[1]


def original_coefficients():
    # Independent construction from r's one-dimensional coefficients.
    r = {0: F(1)}
    for k, value in [(1, F(1, 2)), (6, F(-1, 4)),
                     (7, F(-1, 2)), (8, F(-1, 4))]:
        r[k] = r[-k] = value
    coeff = {}
    for k in range(-9, 10):
        re = ((F(1, 2) if abs(k) == 7 else F(0))
              + r.get(k, F(0))/10
              - (F(1, 10) if k == 0 else F(0)))
        im = (r.get(k+1, F(0)) - r.get(k-1, F(0)))/200
        if (re, im) != ZERO:
            coeff[(k, 0)] = re, im
    for k, value in r.items():
        coeff[(k, 1)] = F(-3, 1000)*value, F(-4, 1000)*value
        coeff[(k, -1)] = F(-3, 1000)*value, F(4, 1000)*value
    return coeff


def S(v):
    return 3*v[0] + 2*v[1], 4*v[0] + 3*v[1]


def Q(v):
    return 2*v[0]*v[0] - v[1]*v[1]


def modular_matrix_product(a, b, modulus):
    return tuple(tuple(sum(a[j][r]*b[r][k] for r in range(2)) % modulus
                       for k in range(2)) for j in range(2))


def return_check(modulus, coeff):
    identity = ((1, 0), (0, 1))
    step = ((3, 2), (4, 3))
    power = identity
    period = 0
    while True:
        period += 1
        power = modular_matrix_product(power, step, modulus)
        if power == identity:
            break
        assert period < 100000, "Only a finite check budget, not an order theorem"
    accumulated = {}
    transported = {(k % modulus, l % modulus): c for (k, l), c in coeff.items()}
    for _ in range(period):
        for v, c in transported.items():
            accumulated[v] = add(accumulated.get(v, ZERO), c)
        transported = {(S(v)[0] % modulus, S(v)[1] % modulus): c
                       for v, c in transported.items()}
    variance = sum((norm2(c) for c in accumulated.values()), F(0))
    orbit = []
    v = (7, 0)
    while v not in orbit:
        orbit.append(v)
        v = S(v)
        v = v[0] % modulus, v[1] % modulus
    assert v == (7, 0)
    length = len(orbit)
    assert period % length == 0
    same_orbit = ((-7) % modulus, 0) in orbit
    orbit_bound = (F(81, 100) if same_orbit else F(81, 200)) * period**2 / length
    assert variance >= orbit_bound >= F(81, 200)*period
    return {
        "N": modulus,
        "order_S_mod_N": period,
        "orbit_length_of_7_0": length,
        "negative_label_in_same_orbit": same_orbit,
        "trace_B2_div_N": str(variance),
        "isolated_orbit_lower_bound": str(orbit_bound),
        "uniform_lower_bound": str(F(81, 200)*period),
    }


def main():
    coeff = original_coefficients()
    assert len(coeff) == 32
    assert all(coeff[(-k, -l)] == conj(c) for (k, l), c in coeff.items())
    assert all(Q(S(v)) == Q(v) for v in coeff)
    selected = {v: c for v, c in coeff.items() if Q(v) == 98}
    assert selected == {(-7, 0): (F(9, 20), F(0)),
                        (7, 0): (F(9, 20), F(0))}
    assert max(abs(Q(v)-98) for v in coeff) == 99
    energy = sum((norm2(c) for c in coeff.values()), F(0))
    cross = ZERO
    overlap_pairs = []
    for v, c in coeff.items():
        if S(v) in coeff:
            overlap_pairs.append([v, S(v)])
            cross = add(cross, mul(c, conj(coeff[S(v)])))
    assert energy == F(66033, 160000)
    assert cross == (F(-7, 2000000), F(0))
    charge = 2*energy - 2*cross[0]
    assert charge == F(1650839, 2000000)
    alias_radius = max(max(abs(v[0]+S(u)[0]), abs(v[1]+S(u)[1]))
                       for u in coeff for v in coeff)
    assert alias_radius == 37
    small_traces = {}
    for modulus in [3, 5, 7, 9, 11]:
        trace = ZERO
        for (k, l), c in coeff.items():
            if k % modulus == 0 and l % modulus == 0:
                trace = add(trace, c)
        assert trace[1] == 0
        small_traces[str(modulus)] = str(modulus*trace[0])
    base = Path(__file__).parent
    root_results_path = base / "root_parametric_exact_results.json"
    root_results = json.loads(root_results_path.read_text())
    root_coeff = {(c["k"], c["l"]): (F(c["real"]), F(c["imag"]))
                  for c in root_results["coefficients"]}
    assert root_coeff == coeff
    result = {
        "status": "exact_finite_algebra_and_orbit_checks_only",
        "no_original_fixed_kick_spectrum_computed": True,
        "coefficient_count": len(coeff),
        "root_coefficient_list_agrees": True,
        "root_results_sha256": hashlib.sha256(root_results_path.read_bytes()).hexdigest(),
        "Q_values": sorted(set(map(Q, coeff))),
        "max_Q_distance_to_98": 99,
        "Q98_coefficients": [{"k": k, "l": l, "re": str(c[0]), "im": str(c[1])}
                             for (k, l), c in sorted(selected.items())],
        "trace_A2_div_N": str(energy),
        "neighbor_overlap_div_N": str(cross[0]),
        "trace_D2_div_N": str(charge),
        "alias_exclusion_radius": alias_radius,
        "overlap_pairs": overlap_pairs,
        "small_dimension_trace_A": small_traces,
        "finite_modular_return_checks": [return_check(n, coeff) for n in [101, 105, 121, 143]],
    }
    output = base / "r11_coherent_parametric_checks.json"
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
