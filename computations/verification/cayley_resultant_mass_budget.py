#!/usr/bin/env python3
"""Exact finite regression for the normalized resultant collision-mass budget.

The universal theorem is proved in mathematics/cayley_resultant_mass_budget.md.
This script checks only the complete promoted finite exceptional sets K=11,13:

* normalized orbit count;
* nonzero resultant, |R| <= 12^(K-1), and R/K^3 a perfect square;
* number of common primitive K-th roots modulo p is <= v_p(R);
* summing common-root counts reproduces the directly computed non-forced
  Cayley energy excess;
* on these finite designs the stronger equality sum v_p(R)=excess happens to
  hold;
* the sharpened weighted budget with the inert K^3 factor removed is checked
  by exact integer arithmetic, with no floating-point logarithms.
"""
from __future__ import annotations

import json
import math
from collections import Counter

import sympy as sp

X = sp.Symbol("X")


def collision_polynomial(k: int, i: int, j: int, r: int, s: int) -> sp.Poly:
    terms = [
        (1, r + s + i),
        (-1, r + s + j),
        (-1, r + i + j),
        (2, r + j),
        (-1, r),
        (1, s + i + j),
        (-2, s + i),
        (1, s),
        (1, i),
        (-1, j),
    ]
    coefficients: Counter[int] = Counter()
    for coefficient, exponent in terms:
        coefficients[exponent % k] += coefficient
    return sp.Poly(
        sum(c * X**e for e, c in coefficients.items() if c),
        X,
        domain=sp.ZZ,
    )


def forced(k: int, i: int, j: int, r: int, s: int) -> bool:
    return (r % k == i % k and s % k == j % k) or (
        r % k == (-j) % k and s % k == (-i) % k
    )


def valuation(n: int, p: int) -> int:
    n = abs(n)
    if n == 0:
        raise ValueError("valuation of zero is not used in this regression")
    result = 0
    while n % p == 0:
        n //= p
        result += 1
    return result


def subgroup_generator(p: int, k: int) -> int:
    primitive = int(sp.primitive_root(p))
    h = pow(primitive, (p - 1) // k, p)
    if pow(h, k, p) != 1 or h == 1:
        raise AssertionError("failed to construct exact-order subgroup generator")
    return h


def cayley_energy_excess(p: int, k: int, h: int) -> int:
    subgroup = [pow(h, exponent, p) for exponent in range(k)]
    values = [
        (z + 1) * pow((z - 1) % p, -1, p) % p
        for z in subgroup
        if z != 1
    ]
    counts: Counter[int] = Counter()
    for a in values:
        for b in values:
            if a != b:
                counts[(a - b) % p] += 1
    energy = sum(multiplicity * multiplicity for multiplicity in counts.values())
    baseline = (k - 1) * (2 * k - 5)
    excess = energy - baseline
    if excess < 0:
        raise AssertionError("energy fell below the forced baseline")
    return excess


def audit(k: int, exceptional_primes: tuple[int, ...]) -> dict[str, object]:
    if not sp.isprime(k) or k % 2 == 0:
        raise AssertionError("regression expects an odd prime K")
    if not all(sp.isprime(p) and (p - 1) % k == 0 for p in exceptional_primes):
        raise AssertionError("every test prime must be split: p == 1 mod K")

    phi = sp.Poly(sp.cyclotomic_poly(k, X), X, domain=sp.ZZ)
    generators = {p: subgroup_generator(p, k) for p in exceptional_primes}
    root_totals = {p: 0 for p in exceptional_primes}
    valuation_totals = {p: 0 for p in exceptional_primes}

    normalized = 0
    max_resultant = 0
    max_square_factor = 0
    resultant_cap = 12 ** (k - 1)

    i = 1
    for j in range(1, k):
        if j == i:
            continue
        for r in range(1, k):
            for s in range(1, k):
                if r == s or forced(k, i, j, r, s):
                    continue

                polynomial = collision_polynomial(k, i, j, r, s)
                resultant = abs(
                    int(sp.resultant(phi.as_expr(), polynomial.as_expr(), X))
                )
                if resultant == 0:
                    raise AssertionError(
                        f"zero non-forced resultant at K={k}, {(i,j,r,s)}"
                    )
                if resultant > resultant_cap:
                    raise AssertionError(
                        f"resultant norm bound failed at K={k}, {(i,j,r,s)}"
                    )

                k3 = k**3
                if resultant % k3:
                    raise AssertionError("resultant lost its universal K^3 factor")
                quotient = resultant // k3
                square_factor = math.isqrt(quotient)
                if square_factor * square_factor != quotient:
                    raise AssertionError("R/K^3 lost its perfect-square structure")

                normalized += 1
                max_resultant = max(max_resultant, resultant)
                max_square_factor = max(max_square_factor, square_factor)

                for p in exceptional_primes:
                    h = generators[p]
                    common_roots = 0
                    for a in range(1, k):
                        root = pow(h, a, p)
                        if int(polynomial.eval(root)) % p == 0:
                            common_roots += 1
                    vp = valuation(resultant, p)
                    if common_roots > vp:
                        raise AssertionError(
                            "common-root count exceeds resultant valuation: "
                            f"K={k}, p={p}, q={(i,j,r,s)}, roots={common_roots}, v={vp}"
                        )
                    if vp % 2:
                        raise AssertionError(
                            f"split-prime valuation should be even by R=K^3 M^2: K={k}, p={p}"
                        )
                    root_totals[p] += common_roots
                    valuation_totals[p] += vp

    expected_orbits = (k - 1) * (k - 2) ** 2 - (2 * k - 5)
    if normalized != expected_orbits:
        raise AssertionError(
            f"normalized orbit count mismatch: {normalized} != {expected_orbits}"
        )

    prime_rows: list[dict[str, int | bool]] = []
    exact_weighted_product = 1
    for p in exceptional_primes:
        direct_excess = cayley_energy_excess(p, k, generators[p])
        if root_totals[p] != direct_excess:
            raise AssertionError(
                f"orbit/root count does not reproduce energy excess at K={k}, p={p}: "
                f"{root_totals[p]} != {direct_excess}"
            )
        # Equality is a finite observation, stronger than the universal proof needs.
        if valuation_totals[p] != direct_excess:
            raise AssertionError(
                f"finite valuation equality changed at K={k}, p={p}: "
                f"{valuation_totals[p]} != {direct_excess}"
            )
        exact_weighted_product *= p**direct_excess
        prime_rows.append(
            {
                "p": p,
                "direct_nonforced_excess": direct_excess,
                "normalized_common_root_count": root_totals[p],
                "sum_resultant_p_adic_valuations": valuation_totals[p],
                "finite_equality": True,
            }
        )

    # Equivalent to
    #   sum Delta(p) log p <= N_K ((K-1)log 12 - 3log K),
    # checked entirely in exact integer arithmetic.
    exact_budget_lhs = exact_weighted_product * k ** (3 * normalized)
    exact_budget_rhs = 12 ** (normalized * (k - 1))
    if exact_budget_lhs > exact_budget_rhs:
        raise AssertionError("sharpened weighted prime-budget product inequality failed")

    return {
        "K": k,
        "normalized_nonforced_scaling_orbits": normalized,
        "formula_orbit_count": expected_orbits,
        "resultant_absolute_cap": resultant_cap,
        "max_resultant_seen": max_resultant,
        "max_square_factor_M_seen": max_square_factor,
        "exceptional_prime_rows": prime_rows,
        "sharpened_weighted_budget_product_inequality": True,
    }


def main() -> None:
    result = {
        "producer": "computations/verification/cayley_resultant_mass_budget.py",
        "scope": (
            "Exact finite regression of the Galois-orbit/common-root/resultant-valuation "
            "mechanism and sharpened K^3-square prime budget on the complete promoted "
            "K=11,13 exceptional sets. The universal weighted-prime theorem is proved "
            "separately in mathematics/cayley_resultant_mass_budget.md."
        ),
        "audits": [
            audit(11, (23, 67, 89)),
            audit(13, (53, 79, 131, 157, 313)),
        ],
        "verdict": "PASS",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
