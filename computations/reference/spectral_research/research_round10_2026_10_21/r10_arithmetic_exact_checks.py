#!/usr/bin/env python3
"""Exact finite checks and input provenance, not a spectral experiment."""
from __future__ import annotations

import hashlib
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__file__).with_suffix(".json")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def falling(n: int, k: int) -> int:
    return math.prod(n - j for j in range(k)) if n >= k else 0


ZERO = (Fraction(0), Fraction(0))
ONE = (Fraction(1), Fraction(0))


def cadd(a, b):
    return a[0] + b[0], a[1] + b[1]


def cmul(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def cscale(a, s):
    return a[0] * s, a[1] * s


def csum(values):
    ans = ZERO
    for value in values:
        ans = cadd(ans, value)
    return ans


def ipow(n):
    return (ONE, (Fraction(0), Fraction(1)),
            (Fraction(-1), Fraction(0)), (Fraction(0), Fraction(-1)))[n % 4]


def minor_det(matrix, indices):
    ans = ZERO
    for perm in itertools.permutations(range(len(indices))):
        inversions = sum(perm[i] > perm[j] for i in range(len(perm))
                         for j in range(i + 1, len(perm)))
        term = ONE
        for i, j in enumerate(perm):
            term = cmul(term, matrix[indices[i]][indices[j]])
        ans = cadd(ans, cscale(term, (-1) ** inversions))
    return ans


def grid_image(point: tuple[int, int]) -> tuple[int, int]:
    a, b = point
    q, p = Fraction(a, 2), Fraction(b, 8)
    q1, p1 = (3 * q - 4 * p) % 1, (-2 * q + 3 * p) % 1
    assert (2 * q1).denominator == 1 and (8 * p1).denominator == 1
    ans = int(2 * q1), int(8 * p1)
    assert ans == ((a - b) % 2, (3 * b) % 8)
    return ans


remaining = set(itertools.product(range(2), range(8)))
cycles = []
while remaining:
    first = min(remaining)
    cycle, point = [], first
    while not cycle or point != first:
        assert point in remaining
        cycle.append(point)
        remaining.remove(point)
        point = grid_image(point)
    cycles.append(cycle)
assert sum(len(c) == 1 for c in cycles) == 4
assert sum(len(c) == 2 for c in cycles) == 6
assert sum(map(len, cycles)) == 16


# The partition inequality is an integer statement. Multiplying by M^(k-1)
# avoids every floating-point evaluation, including negative powers.
partition_cases = 0
nonvacuous_partition_cases = 0
for k in range(2, 7):
    for cells in range(1, 5):
        for counts in itertools.product(range(13), repeat=cells):
            total = sum(counts)
            lhs = total**k if total > 2 * k * cells else 0
            rhs = 2**k * cells ** (k - 1) * sum(falling(n, k) for n in counts)
            assert lhs <= rhs
            partition_cases += 1
            nonvacuous_partition_cases += total > 2 * k * cells


# Finite measure version of the Gram/Cauchy--Binet identity, with nodes
# x_a=N*a/4. Labels a=0,4 and a=1,5 differ by one full period. Uncentered
# kernels suffice because centering only conjugates each Gram matrix.
gram_cases = []
labels = [0, 1, 2, 4, 5]
weights = [Fraction(1, 2), Fraction(2, 3), Fraction(3, 5),
           Fraction(5, 7), Fraction(7, 11)]
for dim in (3, 5, 7):
    T = [[cscale(csum(cscale(ipow((s - r) * a), weights[j])
                      for j, a in enumerate(labels)), Fraction(1, dim))
          for s in range(dim)] for r in range(dim)]
    K = [[cscale(csum(ipow(r * (labels[a] - labels[b]))
                      for r in range(dim)), Fraction(1, dim))
          for b in range(len(labels))] for a in range(len(labels))]
    for k in range(1, min(dim, 4) + 1):
        ek = csum(minor_det(T, E) for E in itertools.combinations(range(dim), k))
        # Summing subsets equals the ordered integral divided by k!, since
        # repeated nodes have zero determinant and all reorderings agree.
        rhs = csum(cscale(minor_det(K, E), math.prod(weights[j] for j in E))
                   for E in itertools.combinations(range(len(labels)), k))
        assert ek == rhs and ek[1] == 0
        gram_cases.append({"N": dim, "k": k, "value": str(ek[0])})
    for a, b in ((0, 3), (1, 4)):
        assert minor_det(K, (a, b)) == ZERO


map_count_cases = 0
convexity_cases = 0
exclusion_polynomial_cases = 0
for k in range(2, 13):
    for n in range(41):
        assert n**k <= k**k * falling(n, k) + k ** (k - 1) * n
        assert 0 <= n**k - falling(n, k) <= math.comb(k, 2) * n ** (k - 1)
        map_count_cases += 1
    for denominator in range(1, 21):
        for numerator in range(4 * denominator + 1):
            y = Fraction(numerator, denominator)
            assert abs(y - 1)**k <= y**k - 1 - k * (y - 1)
            convexity_cases += 1
    for j in range(1, k):
        r = k - j
        for y in range(51):
            for d in range(min(j, y) + 1):
                assert abs(falling(y - d, r) - y**r) <= r * k * (y + k) ** (r - 1)
                exclusion_polynomial_cases += 1


# Count exclusion must use the number d of the selected local labels lying
# in the large window, not j when some selected points lie outside it.
positions = [-2, 0, 0, 1, 3]
h_at = {-2: Fraction(1, 2), 0: Fraction(2, 3),
        1: Fraction(3, 5), 3: Fraction(5, 7)}
h_weights = [h_at[x] for x in positions]
inside = [Fraction(-1, 2) <= x <= Fraction(3, 2) for x in positions]
window_count = sum(inside)
selected_label_exclusion_cases = []
for k in range(2, 6):
    for j in range(1, k):
        r = k - j
        direct = sum(math.prod(h_weights[label] for label in E[:j])
                     * math.prod(inside[label] for label in E[j:])
                     for E in itertools.permutations(range(len(positions)), k))
        grouped = sum(math.prod(h_weights[label] for label in E)
                      * falling(window_count - sum(inside[label] for label in E), r)
                      for E in itertools.permutations(range(len(positions)), j))
        assert direct == grouped
        selected_label_exclusion_cases.append({"k": k, "j": j, "value": str(direct)})


inputs = {
    "research_history_frozen/master_before_round10.md": "base hash only; not reread as a whole",
    "research_round10_2026_10_21/round10_target_checkpoint.md": "full",
    "research_round9_2026_10_21/round9_continuation_ledger.md": "full",
    "research_round9_2026_10_21/r9_arithmetic_galois_obstruction.md": "full",
    "research_round2_2026_10_20/root_all_odd_no_algebraic_eigenvectors.md": "full",
    "research_round4_2026_10_21/counter_subpolynomial_comb_quantitative.md": "full",
    "research_round2_2026_10_20/arithmetic_iterated_all_oldspaces.md": "full (272 lines)",
    "research_round3_2026_10_21/arithmetic_comb_rescaled_gap.md": "lines 1-250 only",
    "research_round3_2026_10_21/arithmetic_seven_chain_cut_stability.md": "full, across sequential reads",
    "research_round7_2026_10_21/r7_original_full_cyclicity_laurent_unit.md": "lines 1-240 only",
    "research_round8_2026_10_21/r8_original_uniform_antiunitary_clifford_gap.md": "lines 430-520 only",
    "research_round4_2026_10_21/root_character_collision_and_routing_audit.md": "full",
    "research_round4_2026_10_21/counter_growing_routing_families.md": "lines 260-460 only, including full Sections 4-6 after definitions",
    "research_round9_2026_10_21/r9_sector_continuous_symbol_stability.md": "lines 335-410 only; phase matching passage",
    "research_round10_2026_10_21/r10_weyl_orderwise_repulsion_stability.md": "full candidate for independent audit",
    "research_round10_2026_10_21/r10_weyl_downward_moment_heredity.md": "full initial and intermediate mathematical text, then exact raw-byte reconstruction of both cosmetic repairs to final ba5e5fb7...",
}

manifest = {
    "scope": "Exact residue cycles and finite counting/Gram identities only; no original spectral statistic computed",
    "base_expected_sha256": "e338400f1f360b680ea74c739283b296c9c67eb4e598c2067b136f9f29773777",
    "cycles_residue_coordinates": cycles,
    "partition_inequality_exact_cases": partition_cases,
    "partition_inequality_nonvacuous_cases": nonvacuous_partition_cases,
    "gram_copy_identity_cases": gram_cases,
    "gram_copy_zero_determinant_checks": 6,
    "map_count_bound_cases": map_count_cases,
    "rational_convexity_cases": convexity_cases,
    "exclusion_polynomial_bound_cases": exclusion_polynomial_cases,
    "selected_label_exclusion_cases": selected_label_exclusion_cases,
    "script_sha256": sha(Path(__file__).resolve()),
    "inputs": {rel: {"sha256": sha(ROOT / rel), "read_scope": scope}
               for rel, scope in inputs.items()},
}
assert manifest["inputs"]["research_history_frozen/master_before_round10.md"]["sha256"] == manifest["base_expected_sha256"]
OUT.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"written": str(OUT),
                  "grid_cycles": len(cycles),
                  "partition_cases": partition_cases,
                  "gram_cases": len(gram_cases),
                  "map_count_cases": map_count_cases,
                  "convexity_cases": convexity_cases,
                  "exclusion_polynomial_cases": exclusion_polynomial_cases,
                  "selected_label_exclusion_cases": len(selected_label_exclusion_cases),
                  "status": "all exact assertions passed"}, ensure_ascii=False))
