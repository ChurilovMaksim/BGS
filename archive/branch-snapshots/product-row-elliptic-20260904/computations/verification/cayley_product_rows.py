#!/usr/bin/env python3
"""Exact finite regression for cayley_product_row_elliptic.md.

The script independently reconstructs the odd-order subgroup, Cayley product
rows, their self/cross energies, the trace-set parametrization, and the branch
loci of the degree-two row maps.  Finite runs are regression evidence only;
the universal statements are proved algebraically in the mathematics note.
"""

from __future__ import annotations

from collections import Counter
from math import isqrt


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d <= isqrt(n):
        if n % d == 0:
            return False
        d += 2
    return True


def multiplicative_order(x: int, p: int) -> int:
    if x % p == 0:
        raise ValueError("order is defined only for nonzero residues")
    y = 1
    for k in range(1, p):
        y = y * x % p
        if y == 1:
            return k
    raise AssertionError("F_p^* order search failed")


def subgroup(p: int, K: int) -> list[int]:
    if not is_prime(p):
        raise ValueError(f"p={p} is not prime")
    if K <= 1 or K % 2 == 0 or (p - 1) % K:
        raise ValueError("K must be an odd divisor of p-1")

    exponent = (p - 1) // K
    for seed in range(2, p):
        h = pow(seed, exponent, p)
        if h != 1 and multiplicative_order(h, p) == K:
            values = [1]
            x = 1
            for _ in range(1, K):
                x = x * h % p
                values.append(x)
            if x * h % p != 1 or len(set(values)) != K:
                raise AssertionError("subgroup generation failed")
            return values
    raise AssertionError(f"failed to find an element of order {K} modulo {p}")


def cayley(x: int, p: int) -> int:
    if x % p == 1:
        raise ValueError("Cayley map has a pole at 1")
    return (x + 1) * pow((x - 1) % p, -1, p) % p


def product_rows(p: int, K: int) -> tuple[list[int], dict[int, int], dict[int, Counter[int]]]:
    H = subgroup(p, K)
    inv = {x: pow(x, -1, p) for x in H}
    B = [x for x in H if x != 1]
    c = {x: cayley(x, p) for x in B}

    rows: dict[int, Counter[int]] = {}
    for u in H:
        row: Counter[int] = Counter()
        for x in B:
            y = u * inv[x] % p
            if y == 1:
                continue
            row[(c[x] + c[y]) % p] += 1
        rows[u] = row
    return H, inv, rows


def verify_design(p: int, K: int, expected_delta: int, expected_max_intersection: int) -> None:
    H, inv, rows = product_rows(p, K)

    # The central product row is the entire t=0 forced spike.
    assert rows[1] == Counter({0: K - 1})

    self_energy = 0
    for u, row in rows.items():
        row_mass = sum(row.values())
        row_energy = sum(value * value for value in row.values())
        self_energy += row_energy

        if u == 1:
            assert row_mass == K - 1
            assert row_energy == (K - 1) ** 2
            continue

        # K-2 admissible ordered pairs, one diagonal and all other values swaps.
        assert row_mass == K - 2
        assert 0 not in row
        multiplicities = list(row.values())
        assert multiplicities.count(1) == 1
        assert all(value in (1, 2) for value in multiplicities)
        assert row_energy == 2 * K - 5

    baseline = 3 * (K - 1) * (K - 2)
    assert self_energy == baseline

    total: Counter[int] = Counter()
    for row in rows.values():
        total.update(row)
    energy = sum(value * value for value in total.values())
    delta = energy - baseline

    # Recompute the cross-row mass independently from the expanded square.
    noncentral = [u for u in H if u != 1]
    cross = 0
    max_finite_intersection = 0
    for i, u in enumerate(noncentral):
        left = rows[u]
        for v in noncentral[i + 1 :]:
            right = rows[v]
            common = set(left) & set(right)
            cross += 2 * sum(left[t] * right[t] for t in common)
            finite_common = {t for t in common if t != 2}
            max_finite_intersection = max(max_finite_intersection, len(finite_common))

    assert cross == delta == expected_delta
    assert max_finite_intersection == expected_max_intersection

    # Squaring is a bijection on an odd-order group: recover the unique row root w.
    square_root = {w * w % p: w for w in H}
    assert len(square_root) == K

    trace_set = {(z + inv[z]) % p for z in H}
    assert len(trace_set) == (K + 1) // 2

    # Check the exact trace/Mobius parametrization row by row.
    for u in noncentral:
        w = square_root[u]
        invalid_trace = (w + inv[w]) % p

        trace_mu: set[int] = set()
        for X in trace_set:
            if X == invalid_trace:
                continue
            denominator = (w * X - 2) % p
            if denominator == 0:  # t=2 -> mu=infinity
                continue
            mu = (1 - w * w) % p * pow(denominator, -1, p) % p
            assert mu != p - 1  # mu=-1 is exactly the excluded coordinate-1 trace
            trace_mu.add(mu)

        row_mu = {
            t * pow((2 - t) % p, -1, p) % p
            for t in rows[u]
            if t != 2
        }
        assert trace_mu == row_mu

    # Distinct noncentral row maps have disjoint branch loci.
    inv2 = pow(2, -1, p)
    roots = [square_root[u] for u in noncentral]
    for i, w in enumerate(roots):
        branch_w = {
            (-(w + 1) * inv2) % p,
            ((w - 1) * inv2) % p,
        }
        assert len(branch_w) == 2
        for q in roots[i + 1 :]:
            branch_q = {
                (-(q + 1) * inv2) % p,
                ((q - 1) * inv2) % p,
            }
            assert branch_w.isdisjoint(branch_q)

    print(
        f"(p,K)=({p},{K}) energy={energy} baseline={baseline} "
        f"Delta={delta} max_finite_row_intersection={max_finite_intersection}"
    )


def main() -> None:
    designs = [
        # Generic baseline anchor.
        (199, 11, 0, 0),
        # Known exceptional reduction.
        (461, 23, 288, 2),
        # Dense negative control: disproves an unconditional <=3 intersection claim.
        (47, 23, 3856, 5),
        # p>K^3 negative control: <=2 still fails.
        (680453, 67, 624, 4),
        # p>K^4 negative control against the stronger exploratory <=1 claim.
        (2908049, 41, 192, 2),
        # Large p>K^4 exceptional design with small but nonzero cross-row mass.
        (728017, 29, 48, 1),
    ]

    for design in designs:
        verify_design(*design)

    print("cayley product-row / elliptic reduction regression: OK")


if __name__ == "__main__":
    main()
