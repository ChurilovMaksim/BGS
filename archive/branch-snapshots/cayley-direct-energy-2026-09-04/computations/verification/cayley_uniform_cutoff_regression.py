#!/usr/bin/env python3
"""Independent exact regression for the prime-order Cayley cutoff theorem.

Mathematical theorem (proved in mathematics/cayley_additive_energy.md):
for odd prime K and p == 1 (mod K), p > 12^(K-1), every Cayley-difference
collision is forced by identity or central inversion, so the mixed collision
energy is (K-1)(2K-5).

This script does NOT prove the theorem. It independently checks the cleared
polynomial identity, the coefficient norm, exhaustive small-K nonvanishing and
resultant bounds, and representative finite fields above the cutoff.
"""
from __future__ import annotations

import itertools
import json
from collections import Counter

import sympy as sp


def coefficient_dict(order: int, i: int, j: int, r: int, s: int) -> dict[int, int]:
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
    out: Counter[int] = Counter()
    for coefficient, exponent in terms:
        out[exponent % order] += coefficient
    return {exponent: coefficient for exponent, coefficient in out.items() if coefficient}


def forced(order: int, i: int, j: int, r: int, s: int) -> bool:
    return (r % order == i % order and s % order == j % order) or (
        r % order == (-j) % order and s % order == (-i) % order
    )


def symbolic_identity() -> dict[str, object]:
    R, S, I, J = sp.symbols("R S I J")
    cayley = lambda z: (z + 1) / (z - 1)
    cleared = sp.cancel(
        (cayley(R) - cayley(S) - cayley(I) + cayley(J))
        * (R - 1)
        * (S - 1)
        * (I - 1)
        * (J - 1)
    )
    polynomial = sp.expand(
        R * S * I
        - R * S * J
        - R * I * J
        + 2 * R * J
        - R
        + S * I * J
        - 2 * S * I
        + S
        + I
        - J
    )
    identity = sp.expand(cleared - 2 * polynomial) == 0
    l1 = sum(abs(int(value)) for value in sp.Poly(polynomial, R, S, I, J).coeffs())
    return {"cleared_identity": bool(identity), "coefficient_l1": l1, "pass": identity and l1 == 12}


def small_resultant_audit(order: int) -> dict[str, object]:
    X = sp.Symbol("X")
    cyclotomic = sp.cyclotomic_poly(order, X)
    count = 0
    maximum = 0
    all_nonzero = True
    all_bounded = True
    bound = 12 ** (order - 1)

    for i, j, r, s in itertools.product(range(1, order), repeat=4):
        if i == j or r == s or forced(order, i, j, r, s):
            continue
        coeffs = coefficient_dict(order, i, j, r, s)
        polynomial = sum(coefficient * X**exponent for exponent, coefficient in coeffs.items())
        resultant = abs(int(sp.resultant(cyclotomic, polynomial, X)))
        count += 1
        maximum = max(maximum, resultant)
        all_nonzero &= resultant != 0
        all_bounded &= resultant <= bound

    return {
        "K": order,
        "nonforced_quadruples": count,
        "max_abs_resultant": maximum,
        "universal_bound": bound,
        "all_nonzero": bool(all_nonzero),
        "all_within_bound": bool(all_bounded),
        "pass": bool(all_nonzero and all_bounded),
    }


def primitive_element_of_order(prime: int, order: int) -> int:
    generator = int(sp.primitive_root(prime))
    value = pow(generator, (prime - 1) // order, prime)
    if value == 1 or pow(value, order, prime) != 1:
        raise AssertionError("failed to construct exact-order subgroup generator")
    return value


def cayley(prime: int, value: int) -> int:
    return (value + 1) * pow((value - 1) % prime, prime - 2, prime) % prime


def finite_field_energy(prime: int, order: int) -> dict[str, object]:
    if not sp.isprime(prime) or (prime - 1) % order:
        raise ValueError("design must have prime p and K | p-1")
    threshold = 12 ** (order - 1)
    if prime <= threshold:
        raise ValueError("design must lie strictly above the proved cutoff")

    generator = primitive_element_of_order(prime, order)
    transformed = [cayley(prime, pow(generator, exponent, prime)) for exponent in range(1, order)]
    counts: Counter[int] = Counter()
    for left in transformed:
        for right in transformed:
            if left != right:
                counts[(left - right) % prime] += 1

    energy = sum(value * value for value in counts.values())
    baseline = (order - 1) * (2 * order - 5)
    return {
        "K": order,
        "p": prime,
        "threshold": threshold,
        "energy": energy,
        "forced_baseline": baseline,
        "multiplicities": sorted(set(counts.values())),
        "pass": energy == baseline,
    }


def main() -> None:
    symbolic = symbolic_identity()
    resultants = [small_resultant_audit(order) for order in (3, 5, 7)]
    finite_fields = [
        finite_field_energy(151, 3),
        finite_field_energy(20771, 5),
        finite_field_energy(2985991, 7),
    ]
    passed = symbolic["pass"] and all(row["pass"] for row in resultants + finite_fields)
    result = {
        "producer": "computations/verification/cayley_uniform_cutoff_regression.py",
        "scope": (
            "Independent finite/symbolic regression for the theorem proof; "
            "bounded checks are not the source of the universal theorem."
        ),
        "symbolic": symbolic,
        "small_resultants": resultants,
        "finite_fields_above_cutoff": finite_fields,
        "verdict": "PASS" if passed else "FAIL",
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
