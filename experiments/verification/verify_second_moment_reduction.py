#!/usr/bin/env python3
"""Verify the exact k=2 reduction and its Cayley/additive-energy form.

This finite verifier checks four layers of the same object:

1. the original k=2 Jacobi-energy reduction;
2. the Cayley identity d(u,v)=2/(c(u)-c(v));
3. the equality between C_H collision energy and additive energy of
   A=c(H\\{1});
4. for odd prime K, an exact cyclotomic audit of the rational primes where
   non-forced collisions can appear after reduction.

It is a finite certificate/regression tool, not an asymptotic BGS theorem.
"""
from __future__ import annotations

import itertools
import json
import math
import sys
from collections import Counter
from pathlib import Path

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src" / "python"))

from bgs.key_geometry import key_difference, subgroup_elements  # noqa: E402

OUTPUT = ROOT / "results" / "verified" / "second_moment_reduction.json"


def prime_divisors(value: int) -> list[int]:
    factors: list[int] = []
    candidate = 2
    while candidate * candidate <= value:
        if value % candidate == 0:
            factors.append(candidate)
            while value % candidate == 0:
                value //= candidate
        candidate += 1
    if value > 1:
        factors.append(value)
    return factors


def primitive_root(prime: int) -> int:
    factors = prime_divisors(prime - 1)
    for generator in range(2, prime):
        if all(
            pow(generator, (prime - 1) // factor, prime) != 1
            for factor in factors
        ):
            return generator
    raise RuntimeError(f"primitive root not found modulo {prime}")


def dlog_table(prime: int, generator: int) -> np.ndarray:
    table = np.full(prime, -1, dtype=np.int64)
    value = 1
    for exponent in range(prime - 1):
        table[value] = exponent
        value = value * generator % prime
    if value != 1 or np.any(table[1:] < 0):
        raise AssertionError("discrete-log table construction failed")
    return table


def cayley(prime: int, value: int) -> int:
    """Return c(h)=(h+1)/(h-1), defined for h != 1."""
    if value % prime == 1:
        raise ValueError("Cayley transform is singular at h=1")
    return (value + 1) * pow((value - 1) % prime, prime - 2, prime) % prime


def constraint_pairs(
    prime: int, subgroup_values: np.ndarray
) -> list[tuple[int, int]]:
    """Original off-diagonal pairs used in the exact k=2 reduction."""
    subgroup_set = {int(value) for value in subgroup_values.tolist()}
    pairs: list[tuple[int, int]] = []
    for x in range(2, prime):
        for y in range(2, prime):
            if x == y:
                continue
            if x * pow(y, prime - 2, prime) % prime not in subgroup_set:
                continue
            shifted = (x - 1) * pow(y - 1, prime - 2, prime) % prime
            if shifted in subgroup_set:
                pairs.append((x, y))
    return pairs


def cayley_energy_audit(
    prime: int, subgroup_values: np.ndarray
) -> dict[str, object]:
    """Check the exact additive-energy model for C_H(t)."""
    subgroup_nonidentity = [
        int(value) for value in subgroup_values.tolist() if int(value) != 1
    ]
    transformed = [cayley(prime, value) for value in subgroup_nonidentity]
    transformed_set = set(transformed)
    if len(transformed_set) != len(transformed):
        raise AssertionError("Cayley transform is not injective on H\\{1}")

    central_symmetry = all((-value) % prime in transformed_set for value in transformed)
    if not central_symmetry:
        raise AssertionError("c(h^-1)=-c(h) symmetry failed")

    difference_counts = np.zeros(prime, dtype=np.int64)
    for first in transformed:
        for second in transformed:
            difference_counts[(first - second) % prime] += 1

    collision_counts = np.zeros(prime, dtype=np.int64)
    cayley_identity_ok = True
    for u in subgroup_nonidentity:
        for v in subgroup_nonidentity:
            if u == v:
                continue
            delta = (cayley(prime, u) - cayley(prime, v)) % prime
            expected_d = 2 * pow(delta, prime - 2, prime) % prime
            actual_d = key_difference(prime, u, v)
            cayley_identity_ok &= expected_d == actual_d
            collision_counts[actual_d] += 1

    nonzero_additive_energy = int(
        np.dot(difference_counts[1:], difference_counts[1:])
    )
    collision_energy = int(np.dot(collision_counts, collision_counts))
    if collision_energy != nonzero_additive_energy:
        raise AssertionError("C_H energy and Cayley additive energy disagree")

    size = len(transformed)
    zero_present = int(0 in transformed_set)
    forced_energy = 2 * size * (size - 1) - (size - zero_present)
    excess_energy = collision_energy - forced_energy
    if excess_energy < 0:
        raise AssertionError("energy fell below the forced symmetry baseline")

    # c(k)=c(h)-x is conjugate to a one-parameter unipotent PGL2 action.
    mobius_intersections_match = True
    subgroup_nonidentity_set = set(subgroup_nonidentity)
    for shift in range(1, prime):
        intersection = 0
        for h in subgroup_nonidentity:
            denominator = (2 + shift - h * shift) % prime
            if denominator == 0:
                continue
            image = (
                ((2 - shift) * h + shift)
                * pow(denominator, prime - 2, prime)
                % prime
            )
            if image in subgroup_nonidentity_set:
                intersection += 1
        mobius_intersections_match &= intersection == int(difference_counts[shift])

    return {
        "cayley_set_size": size,
        "central_symmetry_A_equals_minus_A": bool(central_symmetry),
        "zero_in_cayley_set": bool(zero_present),
        "cayley_difference_identity": bool(cayley_identity_ok),
        "mobius_intersection_identity": bool(mobius_intersections_match),
        "additive_energy_E_plus_A": int(np.dot(difference_counts, difference_counts)),
        "C_H_collision_energy": collision_energy,
        "forced_central_symmetry_baseline": forced_energy,
        "excess_collision_energy": excess_energy,
        "max_nonzero_difference_multiplicity": int(difference_counts[1:].max()),
        "pass": bool(cayley_identity_ok and mobius_intersections_match),
    }


def matching_rank_audit() -> dict[str, object]:
    """Classify all 6! cyclotomic multiset matchings as integer systems.

    The matching equations are homogeneous in (i,j,r,s). Maximal minors show
    that rank can drop only in characteristic two. Rank-two and rank-three
    kernels are both classified, so no one-dimensional family is silently
    omitted.
    """
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
                    positive[row][column] - negative[permutation[row]][column]
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
            bad_rank_drop_primes.update(sp.factorint(minor_gcd).keys())

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

    rank_two = kernel_types[2]
    rank_three = kernel_types[3]
    passed = bool(
        bad_rank_drop_primes == {2}
        and rank_counts == Counter({4: 450, 3: 240, 2: 30})
        and rank_two
        == Counter(
            {
                "invalid_zero_or_diagonal": 26,
                "identity_r_i_s_j": 2,
                "inversion_swap_r_minus_j_s_minus_i": 2,
            }
        )
        and rank_three
        == Counter(
            {
                "invalid_zero_or_diagonal": 236,
                "identity_r_i_s_j": 4,
            }
        )
    )
    return {
        "matching_count": math.factorial(6),
        "rank_counts_over_Q": dict(sorted(rank_counts.items())),
        "bad_rank_drop_primes": sorted(int(value) for value in bad_rank_drop_primes),
        "rank_two_kernel_types": dict(sorted(rank_two.items())),
        "rank_three_kernel_types": dict(sorted(rank_three.items())),
        "conclusion": (
            "For odd prime K, every characteristic-zero Cayley difference "
            "collision is forced by identity or inversion-swap symmetry."
        ),
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
    """Compute the exact reduction-prime set for one odd prime K."""
    if not sp.isprime(order) or order == 2:
        raise ValueError("exception audit currently requires odd prime K")

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
                    raise AssertionError("non-forced characteristic-zero collision found")
                distinct_norms.add(norm)
                for prime_factor in sp.factorint(norm):
                    if prime_factor % order == 1:
                        possible_primes.add(int(prime_factor))
                quadruples_checked += 1

    return {
        "K": order,
        "normalized_nonforced_quadruples_checked": quadruples_checked,
        "distinct_nonzero_norms": len(distinct_norms),
        "exact_exception_primes_N_congruent_1_mod_K": sorted(possible_primes),
        "pass": True,
    }


def verify_design(
    prime: int,
    subgroup_generator: int,
    subgroup_order: int,
    exceptional_primes: set[int],
) -> dict[str, object]:
    generator = primitive_root(prime)
    dlog = dlog_table(prime, generator)
    subgroup_values = subgroup_elements(prime, subgroup_generator, subgroup_order)
    pairs = constraint_pairs(prime, subgroup_values)

    expected_count = (subgroup_order - 1) * (subgroup_order - 2)
    if len(pairs) != expected_count:
        raise AssertionError(
            f"constraint count mismatch at N={prime}: {len(pairs)} != {expected_count}"
        )

    pair_x = np.array([x for x, _ in pairs], dtype=np.int64)
    pair_y = np.array([y for _, y in pairs], dtype=np.int64)
    differences = (pair_x - pair_y) % prime

    eigen_exponent = int(dlog[subgroup_generator])
    annihilator_step = (prime - 1) // math.gcd(eigen_exponent, prime - 1)
    character_indices = np.array(
        [k for k in range(prime - 1) if k % annihilator_step == 0],
        dtype=np.int64,
    )
    dimension = len(character_indices)

    x_values = np.arange(2, prime, dtype=np.int64)
    left = np.exp(
        -2j * np.pi * np.outer(character_indices, dlog[x_values]) / (prime - 1)
    )
    right = np.exp(
        2j
        * np.pi
        * np.outer(character_indices, dlog[(x_values - 1) % prime])
        / (prime - 1)
    )
    off_diagonal_sums = np.array(
        [
            np.exp(2j * np.pi * (q * differences % prime) / prime).sum()
            for q in range(1, prime)
        ]
    )

    maximum_deviation = 0.0
    for q in (1, 2, 3):
        phase = np.exp(2j * np.pi * (q * x_values % prime) / prime)
        jacobi = (left * phase) @ right.T
        measured = float((np.abs(jacobi) ** 2).sum())
        predicted = dimension**2 * (
            (prime - 2) + off_diagonal_sums[q - 1].real
        )
        maximum_deviation = max(maximum_deviation, abs(measured - predicted))

    energy = cayley_energy_audit(prime, subgroup_values)
    is_exceptional = prime in exceptional_primes
    prediction_matches = bool(is_exceptional or energy["excess_collision_energy"] == 0)
    return {
        "N": prime,
        "a": subgroup_generator,
        "K": subgroup_order,
        "m": int(dimension),
        "constraint_pair_count": len(pairs),
        "expected_pair_count": expected_count,
        "identity_max_abs_deviation": float(maximum_deviation),
        "cayley_energy": energy,
        "cyclotomic_exception_status": {
            "N_in_exact_exception_set": is_exceptional,
            "prediction": (
                "non-forced collisions occur"
                if is_exceptional
                else "only forced central-symmetry collisions occur"
            ),
            "prediction_matches_finite_energy": prediction_matches,
        },
        "pass": bool(maximum_deviation < 1e-8 and energy["pass"] and prediction_matches),
    }


def main() -> None:
    matching = matching_rank_audit()
    audits = [cyclotomic_exceptional_primes(11), cyclotomic_exceptional_primes(13)]
    exception_sets = {
        audit["K"]: set(audit["exact_exception_primes_N_congruent_1_mod_K"])
        for audit in audits
    }
    rows = [
        verify_design(53, 10, 13, exception_sets[13]),
        verify_design(67, 64, 11, exception_sets[11]),
        verify_design(199, 139, 11, exception_sets[11]),
        verify_design(521, 101, 13, exception_sets[13]),
    ]
    result = {
        "producer": "experiments/verification/verify_second_moment_reduction.py",
        "scope": (
            "Finite exact k=2 reduction plus Cayley/additive-energy and "
            "cyclotomic reduction-prime audit; not an asymptotic theorem."
        ),
        "exact_identities": [
            "d(u,v)=2/(c(u)-c(v)), c(h)=(h+1)/(h-1)",
            "sum_t C_H(t)^2 = E_plus(c(H\\{1})) - (K-1)^2",
            "c(h^-1)=-c(h)",
            "r_{A-A}(x)=#{h in H\\{1}: g_x(h) in H\\{1}} with g_x(h)=((2-x)h+x)/(2+x-xh)",
        ],
        "matching_rank_audit": matching,
        "cyclotomic_exception_audits": audits,
        "results": rows,
        "verdict": (
            "PASS"
            if matching["pass"]
            and all(audit["pass"] for audit in audits)
            and all(row["pass"] for row in rows)
            else "FAIL"
        ),
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
