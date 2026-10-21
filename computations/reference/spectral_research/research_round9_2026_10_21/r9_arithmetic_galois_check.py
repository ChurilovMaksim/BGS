#!/usr/bin/env python3
"""Exact certificate for the original/galois-2 cubic Hamiltonian moments.

Only rational arithmetic is used. This is a finite coefficient identity,
not a numerical experiment on the requested spectral-statistics limit.
"""

from collections import defaultdict
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mul(a, b):
    return (a[0] * b[0] - a[1] * b[1],
            a[0] * b[1] + a[1] * b[0])


def scale(a, b):
    return (b * a[0], b * a[1])


Z = (F(0), F(0))
c = defaultdict(lambda: Z)


def put(index, value):
    c[index] = add(c[index], value)


# Build directly from r, the cosine, and the two prescribed mixed terms.
r = {0: F(1), 1: F(1, 2), -1: F(1, 2),
     7: F(-1, 2), -7: F(-1, 2),
     6: F(-1, 4), -6: F(-1, 4),
     8: F(-1, 4), -8: F(-1, 4)}
put((7, 0), (F(1, 2), F(0)))
put((-7, 0), (F(1, 2), F(0)))
put((0, 0), (F(-1, 10), F(0)))
for k, v in r.items():
    put((k, 0), (v / 10, F(0)))
    put((k + 1, 0), (F(0), -v / 200))
    put((k - 1, 0), (F(0), v / 200))
    put((k, 1), (F(-3, 1000) * v, F(-4, 1000) * v))
    put((k, -1), (F(-3, 1000) * v, F(4, 1000) * v))
c = {p: v for p, v in c.items() if v != Z}
assert len(c) == 32
assert (0, 0) not in c
for (k, l), v in c.items():
    assert c[-k, -l] == (v[0], -v[1])

# Every triple has total q-frequency <=27 and p-frequency <=3.
# For N>=29, vanishing modulo N is therefore vanishing in Z^2.
areas = defaultdict(lambda: Z)
triples = 0
for u, cu in c.items():
    for v, cv in c.items():
        w = (-u[0] - v[0], -u[1] - v[1])
        if w not in c:
            continue
        triples += 1
        area = u[1] * v[0] - u[0] * v[1]
        areas[area] = add(areas[area], mul(mul(cu, cv), c[w]))
areas = {k: v for k, v in sorted(areas.items()) if v != Z}
expected = {0: (F(-273, 20000), F(0))}
for k, value in [(1, F(9, 800000)), (6, F(3, 800000)),
                 (7, F(-81, 800000)), (8, F(3, 800000))]:
    expected[k] = expected[-k] = (value, F(0))
assert areas == dict(sorted(expected.items())), (areas, expected)

# Rational lower bound used in the uniform Galois-2 cubic gap.
# pi^2<10 and N>=75 imply cos(7x)+cos(14x)>=2-1225/N^2.
# The two remaining cosine differences are nonnegative.
bound_num = 81 * (F(2) - F(1225, 75**2)) - 18
assert bound_num > 120
assert bound_num / 400000 > F(3, 10000)

root = Path(__file__).resolve().parents[1]
inputs = [
    "Spectral_research_master.md",
    "research_round8_2026_10_21/r8_original_obstruction_audit.md",
    "research_round2_2026_10_20/arithmetic_banded_time_reversal.md",
    "research_round2_2026_10_20/arithmetic_padic_jacobi_simplicity.md",
    "research_round2_2026_10_20/arithmetic_seven_chain_discriminant_checkpoint.md",
    "research_continuation_2026_10_20/affine_reversal_and_crt_obstructions.md",
    "research_continuation_2026_10_20/quantitative_transcendence_limits.md",
    "research_round3_2026_10_21/arithmetic_flat_packet_obstruction_test.md",
    "research_round3_2026_10_21/arithmetic_comb_rescaled_gap.md",
    "research_round4_2026_10_21/counter_subpolynomial_comb_quantitative.md",
]
output = {
    "status": "PASS exact coefficient identity and rational gap constant",
    "scope": "No H_diag estimate and no microscopic countersequence",
    "coefficient_count": len(c),
    "zero_sum_triples": triples,
    "cubic_area_coefficients": {str(k): [str(x) for x in v]
                                 for k, v in areas.items()},
    "uniform_gap_numerator_lower_bound": str(bound_num),
    "input_sha256": {name: hashlib.sha256((root / name).read_bytes()).hexdigest()
                     for name in inputs},
}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
print(json.dumps(output, indent=2))
