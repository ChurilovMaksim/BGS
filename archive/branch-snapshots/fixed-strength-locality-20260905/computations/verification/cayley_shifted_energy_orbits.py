#!/usr/bin/env python3
"""Finite regression for cayley_shifted_energy_orbits.md.

Checks the exact shifted-product/Cayley orbit identities on generic and
exceptional split designs.  The large exceptional cases are deliberate negative
controls against a false pointwise exact-baseline claim from p>K^4.

No finite run is a proof of the universal theorems.
"""
from __future__ import annotations

import sys
from collections import Counter
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
    assert h != 1 and pow(h, order, prime) == 1
    return H


def cayley_set(prime: int, H: list[int]) -> list[int]:
    return [
        (h + 1) * pow((h - 1) % prime, -1, prime) % prime
        for h in H
        if h != 1
    ]


def additive_reps(prime: int, A: list[int]) -> Counter[int]:
    return Counter((a + b) % prime for a in A for b in A)


def additive_energy(prime: int, A: list[int]) -> int:
    reps = additive_reps(prime, A)
    return sum(value * value for value in reps.values())


def shifted_product_reps(
    prime: int, H: list[int], lam: int
) -> tuple[Counter[int], int]:
    shifted = [(h + lam) % prime for h in H]
    reps = Counter((x * y) % prime for x in shifted for y in shifted)
    return reps, sum(value * value for value in reps.values())


def cayley_parameter(prime: int, mu: int) -> int:
    assert mu % prime != prime - 1
    return 2 * mu * pow((1 + mu) % prime, -1, prime) % prime


def choose_lambda(prime: int, H: list[int], reps: Counter[int]) -> int:
    # Prefer a genuinely exceptional Cayley bin when present.  Invert
    # t=2mu/(1+mu) by mu=t/(2-t), then take g=1 so lambda=mu.
    candidates = [
        t for t, multiplicity in reps.items()
        if t not in {0, 2 % prime} and multiplicity > 2
    ]
    if not candidates:
        candidates = [t for t in reps if t not in {0, 2 % prime}]
    t = min(candidates)
    mu = t * pow((2 - t) % prime, -1, prime) % prime
    assert mu != 0 and mu != prime - 1
    return mu


def check_orbit(prime: int, order: int) -> None:
    H = subgroup(prime, order)
    A = cayley_set(prime, H)
    r = additive_reps(prime, A)
    lam = choose_lambda(prime, H, r)
    product_reps, energy = shifted_product_reps(prime, H, lam)

    D = 2 * order * order - order
    lhs = 0
    seen_t: set[int] = set()

    for g in H:
        if (g + lam) % prime == 0:
            # mu=-1, corresponding to the missing Cayley parameter t=2.
            continue
        mu = lam * pow(g, -1, prime) % prime
        assert mu != prime - 1
        t = cayley_parameter(prime, mu)
        assert t not in {0, 2 % prime}
        assert t not in seen_t
        seen_t.add(t)

        selected_bin = ((g + lam) * (g + lam)) % prime
        R = product_reps[selected_bin]

        # Scaling by g sends the selected diagonal product bin to
        # (x+mu)(y+mu)=(1+mu)^2.  The enlarged H^2 fiber contains exactly
        # one denominator point (1,1) beyond the Cayley domain.
        scaled_reps, _ = shifted_product_reps(prime, H, mu)
        assert R == scaled_reps[((1 + mu) * (1 + mu)) % prime]
        assert R == r[t] + 1
        lhs += (R - 1) ** 2

    assert lhs == sum(r[t] * r[t] for t in seen_t)
    assert lhs <= 2 * (energy - D)

    # Shift energy is constant on multiplicative H-cosets.
    sample = H[min(3, order - 1)]
    _, scaled_energy = shifted_product_reps(prime, H, lam * sample % prime)
    assert scaled_energy == energy

    # The two large designs are explicit negative controls.
    if (order, prime) in {(29, 728017), (31, 1042903)}:
        assert prime > order**4
        total = additive_energy(prime, A)
        forced_total = 3 * (order - 1) * (order - 2)
        assert total == forced_total + 48
        assert max(r.values()) >= 4


def check_global_shift_identity(prime: int, order: int) -> None:
    H = subgroup(prime, order)
    D = 2 * order * order - order
    left = 0
    for lam in range(prime):
        _, energy = shifted_product_reps(prime, H, lam)
        left += energy - D
    right = order**4 - additive_energy(prime, H)
    assert left == right

    # At zero shift a subgroup has exactly K representations of each product.
    _, zero_energy = shifted_product_reps(prime, H, 0)
    assert zero_energy == order**3


def main() -> None:
    for prime, order in (
        (199, 11),
        (461, 23),
        (728017, 29),
        (1042903, 31),
    ):
        check_orbit(prime, order)

    # Full lambda-sums are intentionally restricted to small designs.
    check_global_shift_identity(199, 11)
    check_global_shift_identity(461, 23)

    print("cayley shifted-energy orbit regression: OK")


if __name__ == "__main__":
    main()
