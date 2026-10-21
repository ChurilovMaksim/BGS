#!/usr/bin/env python3
"""Independent exact finite checks for the two round-7 countermodel notes.

No previous author or auditor checker is imported. Character sums are checked
in Q[zeta_p] by exact integer coefficient vectors. These checks supplement the
analytic proof; they neither construct the generic H nor numerically test LW.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__file__).with_suffix(".md")
counts = Counter()


def check(value, category):
    if not value:
        raise AssertionError(category)
    counts[category] += 1


def dot(left, right, p):
    return sum(a * b for a, b in zip(left, right)) % p


def mv(matrix, vector, p):
    return tuple(dot(row, vector, p) for row in matrix)


def transpose(matrix):
    return tuple(zip(*matrix))


def mm(left, right, p):
    columns = transpose(right)
    return tuple(tuple(dot(row, column, p) for column in columns) for row in left)


def sub(left, right, p):
    return tuple((a - b) % p for a, b in zip(left, right))


def bil(left, matrix, right, p):
    return dot(left, mv(matrix, right, p), p)


def root_sum_equals(histogram, expected, p):
    # Phi_p(z)=1+z+...+z^(p-1). A polynomial of degree at most p-1
    # vanishes at zeta_p iff its coefficient vector is constant.
    coefficients = [histogram.get(j, 0) for j in range(p)]
    coefficients[0] -= expected
    return len(set(coefficients)) == 1


def squared_root_sum_equals(histogram, expected, p):
    square = Counter()
    for a, multiplicity_a in histogram.items():
        for b, multiplicity_b in histogram.items():
            square[(a - b) % p] += multiplicity_a * multiplicity_b
    return root_sum_equals(square, expected, p)


for p in (5, 7, 11):
    inv2, inv3, inv6 = (pow(v, -1, p) for v in (2, 3, 6))
    points = list(product(range(p), repeat=2))
    identity = ((1, 0), (0, 1))

    def action(t, k, l):
        return (t * l * l * inv2
                + t * t * k * l * inv2
                + t * t * t * k * k * inv6) % p

    for t, s, k, l in product(range(p), repeat=4):
        check((action(t, k, l) + action(s, k, l + t * k)
               - action((t + s) % p, k, l)) % p == 0,
              "raw finite-field group law")

    multiplicities = [p - 1] * p
    for l in range(p):
        multiplicities[(l * l * inv2) % p] += 1
    check(sum(multiplicities) == p * p, "spectral multiplicity total")
    check(min(multiplicities) >= p - 1 and max(multiplicities) <= p + 1,
          "spectral multiplicity range")
    for k in range(1, p):
        check(sum(action(1, k, l) for l in range(p)) % p == 0,
              "weighted-cycle product")

    for t in range(1, p):
        ti = pow(t, -1, p)
        H = ((t**3 * inv3 % p, t*t * inv2 % p),
             (t*t * inv2 % p, t % p))
        G = ((12 * ti**3 % p, -6 * ti**2 % p),
             (-6 * ti**2 % p, 4 * ti % p))
        Y = ((1, t), (0, 1))
        D = mm(G, Y, p)
        alternating = tuple(tuple((D[i][j] - D[j][i]) % p
                                  for j in range(2)) for i in range(2))
        expected_alt = ((0, 12 * ti**2 % p), (-12 * ti**2 % p, 0))
        check(mm(H, G, p) == identity, "Hessian inverse")
        check(alternating == expected_alt, "alternating reverse-edge coefficient")
        check((alternating[0][0]*alternating[1][1]
               - alternating[0][1]*alternating[1][0]) % p != 0,
              "reverse-edge nonsingularity")

        for v in points:
            histogram = Counter((action(t, k, l) + k*v[0] + l*v[1]) % p
                                for k, l in points)
            check(squared_root_sum_equals(histogram, p*p, p),
                  "complete two-dimensional Gauss norm")
            for z in points:
                shift = sub(z, mv(G, v, p), p)
                check((inv2 * bil(shift, H, shift, p)
                       + dot(shift, v, p)
                       - inv2 * bil(z, H, z, p)
                       + inv2 * bil(v, G, v, p)) % p == 0,
                      "completed-square identity")

        YtGY = mm(transpose(Y), mm(G, Y, p), p)
        A_matrix = tuple(tuple((YtGY[i][j] - G[i][j]) % p
                               for j in range(2)) for i in range(2))

        def phase(x, y):
            difference = sub(mv(Y, y, p), x, p)
            return -inv2 * bil(difference, G, difference, p) % p

        def endpoint(x):
            return inv2 * bil(x, A_matrix, x, p) % p

        for x, y in product(points, repeat=2):
            check((phase(x, y) - phase(y, x)
                   - endpoint(x) + endpoint(y)
                   - bil(x, alternating, y, p)) % p == 0,
                  "full reverse-edge phase")

        for difference in points:
            histogram = Counter(bil(difference, alternating, y, p) for y in points)
            expected = p*p if difference == (0, 0) else 0
            check(root_sum_equals(histogram, expected, p),
                  "reverse-edge row orthogonality")

        trace_histogram = Counter(t * l*l * inv2 % p for l in range(p))
        check(squared_root_sum_equals(trace_histogram, p, p),
              "direct nontrivial trace modulus")
        spectral_histogram = Counter()
        for a, multiplicity in enumerate(multiplicities):
            spectral_histogram[t * a % p] += multiplicity
        check(squared_root_sum_equals(spectral_histogram, p, p),
              "multiplicity trace cross-check")

    # Read the formal first-return series independently from R=I+R F.
    returns = [(1, 1)]
    first = [(0, 0)]
    for n in range(1, 4*p + 1):
        returns.append((1, int(n % p == 0)))
        f = tuple(returns[n][axis]
                  - sum(returns[n-r][axis] * first[r][axis] for r in range(1, n))
                  for axis in range(2))
        first.append(f)
        expected = (1, 0) if n == 1 else ((0, 1) if n == p else (0, 0))
        check(f == expected, "exact formal base first returns")


# Binary injectivity is proved generally in the report; these exact finite
# checks catch indexing, zero-power, sign, and subset conventions.
differences = {}
for j, k in product(range(64), repeat=2):
    if j == k:
        continue
    value = 2**j - 2**k
    check(value not in differences, "nontrivial ordered binary differences")
    differences[value] = (j, k)
for q in (-7, -1, 1, 13):
    exponents = []
    for mask in range(1 << 14):
        subtotal = sum(2**j for j in range(14) if mask & (1 << j))
        exponents.append(q * subtotal)
    check(len(set(exponents)) == len(exponents), "all-subset binary exponents")

for p in (5, 7, 11, 13, 17, 19, 23, 29, 31):
    n = p*p
    delta_bound = F(3, n**12)
    outside_bound = 4*p*delta_bound
    check((2*p*delta_bound)**2 < 1-F(1, n), "positive return-probability bracket")
    check(outside_bound == F(12, p**23), "outside probability exponent")
    truncated_bound = F(p, n) + F(n**12, n)*outside_bound
    check(truncated_bound == F(13, p), "N^12 normalized moment bound")


sources = (
    "research_round7_2026_10_21/root_unipotent_flat_clock.md",
    "research_round7_2026_10_21/r7_return_generic_microperturbation.md",
)
hashes = {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in sources}
lines = [
    "# Independent exact countermodel checks",
    "",
    "**All checks passed.** No earlier checker was imported or executed.",
    "",
    "These finite checks supplement the analytic proof in r7_audit_countermodel.md. They do not construct the generic algebraic eigenbasis, numerically test transcendence, or approximate the long return tail.",
    "",
    "| Check | Assertions |",
    "| --- | ---: |",
]
lines += [f"| {name} | {amount} |" for name, amount in sorted(counts.items())]
lines += [
    "",
    "The raw finite-field calculations use primes 5, 7, and 11, including every field parameter in each stated finite loop. Cyclotomic checks use exact integer coefficient vectors modulo the prime cyclotomic polynomial.",
    "",
    "Binary ordered differences were checked on indices 0 through 63. All subset exponents on 14 indices were checked at powers -7, -1, 1, and 13. Their universal injectivity and applicability to every nonzero integer power are proved analytically in the audit.",
    "",
    "| Source | SHA-256 |",
    "| --- | --- |",
]
lines += [f"| {name} | {digest} |" for name, digest in hashes.items()]
lines += [
    "",
    "Reproduce with:",
    "",
    "    python research_round7_2026_10_21/r7_audit_countermodel_checks.py",
    "",
]
OUT.write_text("\n".join(lines))
print(json.dumps({"status": "passed", "assertions": sum(counts.values()),
                  "output": str(OUT),
                  "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
                 indent=2))
