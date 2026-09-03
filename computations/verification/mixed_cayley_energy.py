#!/usr/bin/env python3
"""Exact finite certificate for the mixed Cayley-energy term.

The script recomputes the 6! integer matching classification, exact
cyclotomic exceptional-prime sets for K=11,13, and representative finite-field
Cayley/additive-energy checks.  It is a finite exact certificate, not a
uniform-in-K theorem and not a BGS theorem.
"""
from __future__ import annotations

import itertools
import json
import math
import sys
from collections import Counter
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "computations" / "python"))

from bgs.key_geometry import key_difference, subgroup_elements  # noqa: E402

EXPECTED_EXCEPTION_SETS = {
    11: [23, 67, 89],
    13: [53, 79, 131, 157, 313],
}


def cayley(prime: int, value: int) -> int:
    """Return c(h)=(h+1)/(h-1) in F_p, for h != 1."""
    value %= prime
    if value == 1:
        raise ValueError("Cayley transform is singular at h=1")
    return (value + 1) * pow((value - 1) % prime, prime - 2, prime) % prime


def cayley_energy_audit(
    prime: int, subgroup_generator: int, subgroup_order: int
) -> dict[str, object]:
    """Recompute C_H collision energy and its Cayley additive-energy model."""
    subgroup = subgroup_elements(prime, subgroup_generator, subgroup_order)
    nonidentity = [int(h) for h in subgroup.tolist() if int(h) != 1]
    transformed = [cayley(prime, h) for h in nonidentity]
    transformed_set = set(transformed)
    if len(transformed_set) != len(transformed):
        raise AssertionError("Cayley transform is not injective on H\\{1}")

    central_symmetry = all((-x) % prime in transformed_set for x in transformed)
    if not central_symmetry:
        raise AssertionError("c(h^-1)=-c(h) failed")

    difference_counts = [0] * prime
    for x in transformed:
        for y in transformed:
            difference_counts[(x - y) % prime] += 1

    collision_counts = [0] * prime
    cayley_identity_ok = True
    for u in nonidentity:
        for v in nonidentity:
            if u == v:
                continue
            delta = (cayley(prime, u) - cayley(prime, v)) % prime
            expected = 2 * pow(delta, prime - 2, prime) % prime
            actual = key_difference(prime, u, v)
            cayley_identity_ok &= actual == expected
            collision_counts[actual] += 1

    collision_energy = sum(c * c for c in collision_counts)
    nonzero_additive_energy = sum(c * c for c in difference_counts[1:])
    if collision_energy != nonzero_additive_energy:
        raise AssertionError("mixed collision energy != nonzero Cayley additive energy")

    size = len(transformed)
    zero_present = int(0 in transformed_set)
    forced = 2 * size * (size - 1) - (size - zero_present)
    excess = collision_energy - forced
    if excess < 0:
        raise AssertionError("energy fell below forced central-symmetry baseline")

    nonidentity_set = set(nonidentity)
    mobius_ok = True
    for shift in range(1, prime):
        intersection = 0
        for h in nonidentity:
            denominator = (2 + shift - h * shift) % prime
            if denominator == 0:
                continue
            image = (
                ((2 - shift) * h + shift)
                * pow(denominator, prime - 2, prime)
                % prime
            )
            if image in nonidentity_set:
                intersection += 1
        mobius_ok &= intersection == difference_counts[shift]

    return {
        "N": prime,
        "K": subgroup_order,
        "a": subgroup_generator,
        "cayley_set_size": size,
        "central_symmetry_A_equals_minus_A": central_symmetry,
        "zero_in_cayley_set": bool(zero_present),
        "cayley_difference_identity": cayley_identity_ok,
        "mobius_intersection_identity": mobius_ok,
        "additive_energy_E_plus_A": sum(c * c for c in difference_counts),
        "C_H_collision_energy": collision_energy,
        "forced_central_symmetry_baseline": forced,
        "excess_collision_energy": excess,
        "max_nonzero_difference_multiplicity": max(difference_counts[1:]),
        "pass": bool(cayley_identity_ok and mobius_ok),
    }


def matching_rank_audit() -> dict[str, object]:
    """Classify all 6! multiset matchings as integer linear systems."""
    positive = [
        (0, 0, 0, 1),
        (1, 0, 0, 0),
        (1, 0, 1, 1),
        (0, 1, 1, 0),
        (0, 1, 1, 0),
        (1, 1, 0, 1),
    ]
    negative = [
        (0, 0, 1, 0),
        (1, 0, 0, 1),
        (1, 0, 0, 1),
        (0, 1, 0, 0),
        (0, 1, 1, 1),
        (1, 1, 1, 0),
    ]

    rank_counts: Counter[int] = Counter()
    bad_rank_drop_primes: set[int] = set()
    kernel_types: dict[int, Counter[str]] = {2: Counter(), 3: Counter()}

    invalid_forms = [
        sp.Matrix([[1, 0, 0, 0]]),
        sp.Matrix([[0, 1, 0, 0]]),
        sp.Matrix([[0, 0, 1, 0]]),
        sp.Matrix([[0, 0, 0, 1]]),
        sp.Matrix([[1, -1, 0, 0]]),
        sp.Matrix([[0, 0, 1, -1]]),
    ]
    identity_forms = [
        sp.Matrix([[1, 0, -1, 0]]),
        sp.Matrix([[0, 1, 0, -1]]),
    ]
    inversion_forms = [
        sp.Matrix([[1, 0, 0, 1]]),
        sp.Matrix([[0, 1, 1, 0]]),
    ]

    def annihilates(form: sp.Matrix, nullspace: list[sp.Matrix]) -> bool:
        return all((form * vector)[0] == 0 for vector in nullspace)

    for permutation in itertools.permutations(range(6)):
        matrix = sp.Matrix(
            [
                [
                    positive[row][column]
                    - negative[permutation[row]][column]
                    for column in range(4)
                ]
                for row in range(6)
            ]
        )
        rank = matrix.rank()
        rank_counts[rank] += 1

        nonzero_minors: list[int] = []
        for rows in itertools.combinations(range(6), rank):
            for columns in itertools.combinations(range(4), rank):
                determinant = int(matrix.extract(rows, columns).det())
                if determinant:
                    nonzero_minors.append(abs(determinant))
        minor_gcd = 0
        for determinant in nonzero_minors:
            minor_gcd = math.gcd(minor_gcd, determinant)
        if minor_gcd > 1:
            bad_rank_drop_primes.update(int(p) for p in sp.factorint(minor_gcd))

        if rank not in kernel_types:
            continue
        nullspace = matrix.nullspace()
        if any(annihilates(form, nullspace) for form in invalid_forms):
            kernel_types[rank]["invalid_zero_or_diagonal"] += 1
        elif all(annihilates(form, nullspace) for form in identity_forms):
            kernel_types[rank]["identity_r_i_s_j"] += 1
        elif all(annihilates(form, nullspace) for form in inversion_forms):
            kernel_types[rank]["inversion_swap_r_minus_j_s_minus_i"] += 1
        else:
            kernel_types[rank]["unclassified"] += 1

    expected_ranks = Counter({4: 450, 3: 240, 2: 30})
    expected_rank2 = Counter(
        {
            "invalid_zero_or_diagonal": 26,
            "identity_r_i_s_j": 2,
            "inversion_swap_r_minus_j_s_minus_i": 2,
        }
    )
    expected_rank3 = Counter(
        {"invalid_zero_or_diagonal": 236, "identity_r_i_s_j": 4}
    )
    passed = (
        rank_counts == expected_ranks
        and bad_rank_drop_primes == {2}
        and kernel_types[2] == expected_rank2
        and kernel_types[3] == expected_rank3
    )
    return {
        "matching_count": math.factorial(6),
        "rank_counts_over_Q": dict(sorted(rank_counts.items())),
        "bad_rank_drop_primes": sorted(bad_rank_drop_primes),
        "rank_two_kernel_types": dict(sorted(kernel_types[2].items())),
        "rank_three_kernel_types": dict(sorted(kernel_types[3].items())),
        "pass": passed,
    }


def collision_polynomial(
    symbol: sp.Symbol,
    order: int,
    i: int,
    j: int,
    r: int,
    s: int,
) -> sp.Expr:
    """Cleared Cayley-difference collision numerator, exponents mod K."""
    coefficients: Counter[int] = Counter()
    terms = [
        (-1, r),
        (1, s),
        (1, i),
        (-2, s + i),
        (1, r + s + i),
        (-1, j),
        (2, r + j),
        (-1, r + s + j),
        (-1, r + i + j),
        (1, s + i + j),
    ]
    for coefficient, exponent in terms:
        coefficients[exponent % order] += coefficient
    return sp.Add(
        *[
            coefficient * symbol**exponent
            for exponent, coefficient in coefficients.items()
            if coefficient
        ]
    )


def cyclotomic_exceptional_primes(order: int) -> dict[str, object]:
    """Compute exact bad reduction primes for one odd prime K."""
    if not sp.isprime(order) or order == 2:
        raise ValueError("K must be an odd prime")

    symbol = sp.Symbol("X")
    cyclotomic = sp.cyclotomic_poly(order, symbol)
    possible_primes: set[int] = set()
    distinct_norms: set[int] = set()
    quadruples_checked = 0
    i = 1

    for j in range(1, order):
        if j == i:
            continue
        for r in range(1, order):
            for s in range(1, order):
                if r == s:
                    continue
                if (r == i and s == j) or (
                    r % order == (-j) % order
                    and s % order == (-i) % order
                ):
                    continue
                polynomial = collision_polynomial(symbol, order, i, j, r, s)
                norm = abs(int(sp.resultant(cyclotomic, polynomial, symbol)))
                if norm == 0:
                    raise AssertionError(
                        "non-forced characteristic-zero collision found"
                    )
                distinct_norms.add(norm)
                for prime_factor in sp.factorint(norm):
                    if prime_factor % order == 1:
                        possible_primes.add(int(prime_factor))
                quadruples_checked += 1

    result = sorted(possible_primes)
    return {
        "K": order,
        "normalized_nonforced_quadruples_checked": quadruples_checked,
        "distinct_nonzero_norms": len(distinct_norms),
        "exact_exception_primes_N_congruent_1_mod_K": result,
        "pass": result == EXPECTED_EXCEPTION_SETS[order],
    }


def verify_design(
    prime: int, subgroup_generator: int, subgroup_order: int
) -> dict[str, object]:
    """Check exact bad-prime status against observed finite collision excess."""
    if pow(subgroup_generator, subgroup_order, prime) != 1:
        raise ValueError("a^K != 1")
    if subgroup_generator % prime == 1:
        raise ValueError("non-trivial subgroup generator required")
    if (prime - 1) % subgroup_order:
        raise ValueError("K must divide N-1")

    energy = cayley_energy_audit(prime, subgroup_generator, subgroup_order)
    exceptional = prime in set(EXPECTED_EXCEPTION_SETS.get(subgroup_order, []))
    observed_nonforced = int(energy["excess_collision_energy"]) > 0
    prediction_matches = observed_nonforced == exceptional
    return {
        **energy,
        "cyclotomic_exception_status": {
            "N_in_exact_exception_set": exceptional,
            "observed_nonforced_collisions": observed_nonforced,
            "prediction_matches_finite_energy": prediction_matches,
        },
        "pass": bool(energy["pass"] and prediction_matches),
    }


def main() -> None:
    matching = matching_rank_audit()
    audits = [
        cyclotomic_exceptional_primes(11),
        cyclotomic_exceptional_primes(13),
    ]
    designs = [
        verify_design(53, 10, 13),
        verify_design(67, 64, 11),
        verify_design(199, 139, 11),
        verify_design(521, 101, 13),
        cayley_energy_audit(461, 23, 23),
    ]
    if int(designs[-1]["excess_collision_energy"]) <= 0:
        raise AssertionError(
            "(N,K)=(461,23) must remain an explicit non-uniformity witness"
        )

    passed = (
        bool(matching["pass"])
        and all(bool(row["pass"]) for row in audits)
        and all(bool(row["pass"]) for row in designs)
    )
    result = {
        "producer": "computations/verification/mixed_cayley_energy.py",
        "scope": (
            "Exact finite certificate for the fixed-K Cayley mixed term; "
            "not a uniform-in-K theorem and not a BGS theorem."
        ),
        "matching_rank_audit": matching,
        "cyclotomic_exception_audits": audits,
        "finite_field_designs": designs,
        "verdict": "PASS" if passed else "FAIL",
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
