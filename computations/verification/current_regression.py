#!/usr/bin/env python3
"""Current exact finite regression gate for the active mathematical surface.

Every assertion here is a finite identity, API invariant, or preserved exact
anchor. Passing this script is evidence for those finite statements only; it
is not an asymptotic theorem and does not imply the microscopic BGS law.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "computations" / "python"))

from bgs.finite_field import multiplicative_order, primitive_root  # noqa: E402
from bgs.jacobi import annihilator_indices, dlog_table, jacobi_matrix  # noqa: E402
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


def check_finite_field_contracts() -> None:
    p = 199
    g = primitive_root(p)
    assert multiplicative_order(g, p) == p - 1
    log = dlog_table(p, g)
    a = element_of_order(p, 11)
    indices = annihilator_indices(p, 11, a, log)
    assert len(indices) == (p - 1) // 11

    # A parity sector is a legitimate sub-sector of the annihilator.
    odd_sector = indices[indices % 2 == 1]
    sector_matrix = jacobi_matrix(p, 11, a, log, odd_sector, 1)
    assert sector_matrix.shape == (len(odd_sector), len(odd_sector))

    try:
        jacobi_matrix(p, 11, a, log, np.array([1], dtype=np.int64), 1)
    except ValueError:
        pass
    else:
        raise AssertionError("character outside the annihilator was silently accepted")

    try:
        annihilator_indices(p, 9, a, log)
    except ValueError:
        pass
    else:
        raise AssertionError("wrong subgroup_order was silently accepted")

    try:
        dlog_table(p, a)
    except ValueError:
        pass
    else:
        raise AssertionError("non-primitive dlog generator was silently accepted")


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
        subgroup = subgroup_elements(p, a, k)
        distribution, classes = fast_difference_distribution(p, subgroup)
        assert int(distribution.sum()) == expected_total == variety_count_formula(p, k)
        assert int(distribution[0]) == expected_zero
        assert int(np.dot(distribution.astype(object), distribution.astype(object))) == expected_energy
        assert sum(classes.values()) == expected_total


def cayley_energy(prime: int, order: int) -> int:
    a = element_of_order(prime, order)
    subgroup = [
        int(x) for x in subgroup_elements(prime, a, order).tolist() if int(x) != 1
    ]
    cayley = {
        h: (h + 1) * pow((h - 1) % prime, prime - 2, prime) % prime
        for h in subgroup
    }
    counts: Counter[int] = Counter()
    for u in subgroup:
        for v in subgroup:
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
    assert observed > forced


def check_certificate_corpus() -> None:
    root = ROOT / "evidence" / "certificates"
    required = {
        "fourth_moment_factorization.json",
        "second_moment_reduction.json",
        "twisted_jacobi_moments.json",
        "twisted_jacobi_scalar_formula.json",
        "cayley_exception_k23.json",
    }
    present = {path.name for path in root.glob("*.json")}
    assert required <= present
    for path in root.glob("*.json"):
        json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    check_finite_field_contracts()
    check_small_pair_map()
    check_fourth_moment_anchors()
    check_exceptional_k23()
    check_certificate_corpus()
    print("current exact finite regression: PASS")


if __name__ == "__main__":
    main()
