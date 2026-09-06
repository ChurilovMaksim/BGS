#!/usr/bin/env python3
"""Finite regression for cayley_product_row_intersections.md.

Checks the exact decomposition of non-forced Cayley additive energy into
cross-terms between fixed-product rows.  Includes large split-prime negative
controls.  Finite checks do not prove the open uniform row-intersection bound.
"""
from __future__ import annotations

import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "computations" / "python"))

from bgs.finite_field import primitive_root  # noqa: E402


def subgroup(prime: int, order: int) -> list[int]:
    assert (prime - 1) % order == 0
    g = primitive_root(prime)
    h = pow(g, (prime - 1) // order, prime)
    H = [pow(h, j, prime) for j in range(order)]
    assert len(set(H)) == order
    return H


def cayley(prime: int, x: int) -> int:
    assert x % prime != 1
    return (x + 1) * pow((x - 1) % prime, -1, prime) % prime


def row_data(
    prime: int, H: list[int]
) -> tuple[dict[int, dict[int, int]], Counter[int]]:
    """Return row -> (nonzero t -> ordered weight) and total sum reps."""
    valid = [x for x in H if x != 1]
    rows: dict[int, dict[int, int]] = defaultdict(dict)
    total: Counter[int] = Counter()

    for i, x in enumerate(valid):
        for y in valid[i:]:
            u = x * y % prime
            t = (cayley(prime, x) + cayley(prime, y)) % prime
            weight = 1 if x == y else 2
            total[t] += weight

            if t == 0:
                # The central product row u=1 contains all zero-sum pairs.
                assert u == 1
                continue

            assert u != 1
            # Lemma 1: fixed product and nonzero Cayley sum determine the
            # unordered pair uniquely.
            assert t not in rows[u], (prime, u, t)
            rows[u][t] = weight

    return rows, total


def check_design(prime: int, order: int) -> tuple[int, int]:
    H = subgroup(prime, order)
    rows, reps = row_data(prime, H)

    energy = sum(value * value for value in reps.values())
    forced = 3 * (order - 1) * (order - 2)
    delta = energy - forced
    assert delta >= 0

    keys = sorted(rows)
    cross = 0
    intersection_count = 0
    max_intersection = 0

    for i, u in enumerate(keys):
        for v in keys[i + 1 :]:
            common = set(rows[u]).intersection(rows[v])
            max_intersection = max(max_intersection, len(common))
            intersection_count += len(common)
            cross += sum(
                2 * rows[u][t] * rows[v][t]
                for t in common
            )

    # Theorem 2: every non-forced nonzero-sum collision is a cross-row term.
    assert cross == delta, (prime, order, cross, delta)
    assert 2 * intersection_count <= delta
    assert delta <= 8 * intersection_count
    assert delta <= 4 * max_intersection * (order - 1) * (order - 2)

    # The zero bin is exactly the centrally symmetric class.
    assert reps[0] == order - 1

    return delta, max_intersection


def main() -> None:
    promoted = {
        (199, 11): (0, 0),
        (461, 23): (288, None),
        (728017, 29): (48, 1),
        (2908049, 41): (192, 2),
    }

    for (prime, order), (expected_delta, expected_max) in promoted.items():
        delta, maximum = check_design(prime, order)
        assert delta == expected_delta, (prime, order, delta)
        if expected_max is not None:
            assert maximum == expected_max, (prime, order, maximum)
        if (prime, order) in {(728017, 29), (2908049, 41)}:
            assert prime > order**4

    print("cayley product-row intersection regression: OK")


if __name__ == "__main__":
    main()
