#!/usr/bin/env python3
"""Current finite regression gate for the active mathematical surface.

This script deliberately checks exact finite identities and preserved anchors.
It does not assert an asymptotic BGS law.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "computations" / "python"))

from bgs.key_geometry import (  # noqa: E402
    explicit_key_table,
    fast_difference_distribution,
    original_pair_key_table,
    records_as_map,
    subgroup_elements,
    variety_count_formula,
)


def prime_divisors(n: int) -> list[int]:
    out: list[int] = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def element_of_order(prime: int, order: int) -> int:
    factors = prime_divisors(order)
    for a in range(2, prime):
        if pow(a, order, prime) != 1:
            continue
        if all(pow(a, order // q, prime) != 1 for q in factors):
            return a
    raise RuntimeError(f"no element of order {order} mod {prime}")


def check_small_pair_map() -> None:
    p = 23
    left = records_as_map(original_pair_key_table(p))
    right = records_as_map(explicit_key_table(p))
    assert left == right
    assert len(left) == (p - 2) * (p - 3) + 1
    assert left[(1, 1)].multiplicity == p - 2


def check_fourth_moment_anchors() -> None:
    anchors = {
        (23, 11): (48621, 2609, 103156981),
        (53, 13): (423879, 12063, 3410502105),
    }
    for (p, k), (expected_total, expected_zero, expected_energy) in anchors.items():
        a = element_of_order(p, k)
        H = subgroup_elements(p, a, k)
        B, classes = fast_difference_distribution(p, H)
        assert int(B.sum()) == expected_total == variety_count_formula(p, k)
        assert int(B[0]) == expected_zero
        assert int(np.dot(B.astype(object), B.astype(object))) == expected_energy
        assert sum(classes.values()) == expected_total


def cayley_energy(prime: int, order: int) -> int:
    a = element_of_order(prime, order)
    H = [int(x) for x in subgroup_elements(prime, a, order).tolist() if int(x) != 1]
    cayley = {
        h: (h + 1) * pow((h - 1) % prime, prime - 2, prime) % prime for h in H
    }
    counts: Counter[int] = Counter()
    for u in H:
        for v in H:
            if u == v:
                continue
            delta = (cayley[u] - cayley[v]) % prime
            counts[(2 * pow(delta, prime - 2, prime)) % prime] += 1
    return sum(c * c for c in counts.values())


def check_exceptional_k23() -> None:
    observed = cayley_energy(461, 23)
    forced = (23 - 1) * (2 * 23 - 5)
    assert observed == 1190
    assert forced == 902
    assert observed != forced


def check_certificate_corpus() -> None:
    root = ROOT / "evidence" / "certificates"
    required = {
        "fourth_moment_factorization.json",
        "second_moment_reduction.json",
        "twisted_jacobi_moments.json",
        "twisted_jacobi_scalar_formula.json",
        "cayley_exception_k23.json",
    }
    present = {p.name for p in root.glob("*.json")}
    assert required <= present
    for path in root.glob("*.json"):
        json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    check_small_pair_map()
    check_fourth_moment_anchors()
    check_exceptional_k23()
    check_certificate_corpus()
    print("current finite regression: PASS")


if __name__ == "__main__":
    main()
