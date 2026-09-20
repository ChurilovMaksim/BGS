"""Independent exact review of the cubic CUE sixth-cumulant certificate.

Run from the repository root:
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/workspace/scratch/75a15b7b1123/dependencies/python python build/report-audit-20260919/independent_variance_review.py

The symbolic certificate below does not use the author's partition generator
or cumulant evaluator. Only the separately labeled existing moment checks are
imported. Output is written beside this script.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import combinations, permutations, product
import json
from pathlib import Path


FORMS = (
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (-1, -1, 0, 0),
    (0, 0, -1, 0),
    (0, 0, 0, -1),
    (0, 0, 1, 1),
)


def cyclic_paths():
    """Generate cyclic ordered partitions through onto maps, anchoring label 0.

    Each ordered partition with k blocks has k rotations. Their equal spans
    let us cancel the 1/k in the cumulant formula. Requiring label 0 in block
    0 selects exactly one representative of each orbit.
    """
    paths = []
    for k in range(1, 7):
        for tail in product(range(k), repeat=5):
            labels = (0,) + tail
            if set(labels) != set(range(k)):
                continue
            positions = [(0,) * 4]
            for block in range(k):
                step = tuple(
                    sum(FORMS[j][i] for j in range(6) if labels[j] == block)
                    for i in range(4)
                )
                positions.append(tuple(x + y for x, y in zip(positions[-1], step)))
            paths.append(((-1) ** (k - 1), tuple(positions)))
    assert len(paths) == 1082
    return paths


def coefficient_vector(paths, dimension, point):
    """Accumulate exact affine coefficients, using a point to select branches."""
    result = [0] * 5
    for sign, positions in paths:
        values = [sum(x * y for x, y in zip(v, point)) for v in positions]
        low = values.index(min(values))
        high = values.index(max(values))
        if values[high] - values[low] < dimension:
            result[0] += sign
            for i in range(4):
                result[i + 1] -= sign * (positions[high][i] - positions[low][i])
    return tuple(result)


def check_domain_coverage():
    """Verify the possible comparison forms and threshold bounds over the band.

    A difference of visited partial sums is a subset sum, or its negative;
    taking the complementary subset supplies that negative because total=0.
    Linear bounds over the closed band follow from its 16 corners. With zero
    coefficient sum, nonzero comparisons are variable differences or pair
    differences. Ordering four variables fixes every such pair comparison
    except x1+x4 versus x2+x3. The two witness templates cover its two sides.
    """
    vectors = {
        tuple(sum(FORMS[j][i] for j in subset) for i in range(4))
        for size in range(7)
        for subset in combinations(range(6), size)
    }
    assert len(vectors) == 49
    assert all(set(v) <= {-1, 0, 1} for v in vectors)
    assert all(tuple(-x for x in v) in vectors for v in vectors)
    corners = tuple(product((F(2, 3), F(4, 5)), repeat=4))
    for v in vectors:
        total = sum(v)
        values = [sum(a * b for a, b in zip(v, corner)) for corner in corners]
        if total == 1:
            assert 0 < min(values) <= max(values) < 1
        elif total >= 2:
            assert min(values) > 1
        elif total == -1:
            assert -1 < min(values) <= max(values) < 0
        elif total <= -2:
            assert max(values) < -1
        else:
            assert max(abs(value) for value in values) < 1
            assert v == (0, 0, 0, 0) or (v.count(1), v.count(-1)) in ((1, 1), (2, 2))
    return {
        "subset_coefficient_vectors": len(vectors),
        "band_corner_checks_per_vector": len(corners),
        "all_sign_and_threshold_bounds_passed": True,
        "remaining_walls": "variable equality or equality of two disjoint pair sums",
    }


def check_chambers(paths):
    seen = set()
    coefficient_counts = Counter()
    for template in ((72, 73, 76, 78), (72, 74, 76, 77)):
        for point in permutations(template):
            assert all(F(2, 3) * 100 < x < F(4, 5) * 100 for x in point)
            order = tuple(sorted(range(4), key=lambda i: point[i]))
            x = sorted(point)
            assert x[0] + x[3] != x[1] + x[2]
            side = 1 if x[0] + x[3] > x[1] + x[2] else -1
            assert (order, side) not in seen
            seen.add((order, side))
            a, b, c, d = point
            assert a + b != c + d
            expected = (3, -2, -2, 0, 0) if a + b < c + d else (3, 0, 0, -2, -2)
            actual = coefficient_vector(paths, 100, point)
            assert actual == expected, (point, actual, expected)
            coefficient_counts[actual] += 1
    assert seen == {(order, side) for order in permutations(range(4)) for side in (-1, 1)}
    return {
        "distinct_chambers": len(seen),
        "all_24_orders_and_both_pair_sum_sides": True,
        "exact_coefficient_counts": [
            {"coefficients_N_a_b_c_d": list(vector), "chambers": count}
            for vector, count in sorted(coefficient_counts.items())
        ],
    }


def check_equality_walls(paths):
    points = (
        (75, 75, 75, 75),
        (72, 73, 73, 72),
        (72, 74, 76, 78),
        (67, 68, 79, 79),
        (79, 67, 67, 79),
    )
    results = []
    for point in points:
        assert all(F(2, 3) * 100 < x < F(4, 5) * 100 for x in point)
        vector = coefficient_vector(paths, 100, point)
        actual = sum(c * t for c, t in zip(vector, (100,) + point))
        expected = 300 - 2 * min(point[0] + point[1], point[2] + point[3])
        assert actual == expected, (point, actual, expected)
        results.append({"N": 100, "a_b_c_d": list(point), "sixth_cumulant": actual})
    return results


def main():
    paths = cyclic_paths()
    # These two checks are reruns of the author's separate moment checks;
    # they are not part of the independently constructed chamber evaluator.
    from cubic_variance import independent_checks

    result = {
        "status": "passed",
        "construction": "onto maps with label 0 anchored; cyclic rotations cancel 1/k",
        "cyclic_ordered_partitions": len(paths),
        "domain_coverage": check_domain_coverage(),
        "symbolic_chambers": check_chambers(paths),
        "equality_wall_checks": check_equality_walls(paths),
        "existing_moment_checks_rerun": independent_checks(),
        "limitations": [
            "The determinant-to-cumulant identity and variance partition decomposition are checked analytically in the accompanying review, not proved by this script.",
            "Continuity extends the chamber identity to every equality wall; the five wall evaluations are additional finite checks.",
            "No deterministic-map universality claim or experiment calibration is checked.",
        ],
    }
    output = json.dumps(result, indent=2) + "\n"
    Path(__file__).with_suffix('.json').write_text(output)
    print(output, end="")


if __name__ == "__main__":
    main()
