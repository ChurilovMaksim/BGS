#!/usr/bin/env python3
"""Verify the exact k=2 reduction and its Cayley/additive-energy form.

Besides the original finite Jacobi identity, this verifier checks the exact
change of variables

    c(h) = (h+1)/(h-1),
    d(u,v) = 2/(c(u)-c(v)),

which identifies the k=2 collision energy with the nonzero additive energy of
A=c(H\{1}).  For odd prime subgroup orders it also performs a small exact
cyclotomic audit explaining which rational primes can acquire non-forced
collisions after reduction.
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

from bgs.jacobi import dlog_table  # noqa: E402
from bgs.key_geometry import key_difference, subgroup_elements  # noqa: E402
from bgs.twisted_jacobi import primitive_root  # noqa: E402

OUTPUT = ROOT / "results" / "verified" / "second_moment_reduction.json"


def cayley(prime: int, value: int) -> int:
    """Cayley transform c(h)=(h+1)/(h-1), defined away from h=1."""
    if value % prime == 1:
        raise ValueError("Cayley transform is singular at h=1")
    return (value + 1) * pow((value - 1) % prime, prime - 2, prime) % prime


def constraint_pairs(
    prime: int, subgroup_values: np.ndarray
) -> list[tuple[int, int]]:
    """Build the original off-diagonal pair set of the exact k=2 reduction."""
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
    prime: int,
    subgroup_values: np.ndarray,
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
            if delta == 0:
                raise AssertionError("non-diagonal Cayley difference vanished")
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
        raise AssertionError("energy fell below the forced central-symmetry baseline")

    # The translation c(k)=c(h)-x conjugates to a one-parameter PGL2 action.
    mobius_intersections_match = True
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
            if image in subgroup_nonidentity:
                intersection += 1
        mobius_intersections_match &= intersection == int(difference_counts[shift])

    return {
        "cayley_set_size": size,
        "central_symmetry_A_equals_minus_A": bool(central_symmetry),
        "zero_in_cayley_set": bool(zero_present),
        "cayley_difference_identity": bool(cayley_identity_ok),
        "mobius_intersection_identity": bool(mobius_intersections_match),
        "additive_energy_E_plus_A": int(
            np.dot(difference_counts, difference_counts)
        ),
        "C_H_collision_energy": collision_energy,
        "forced_central_symmetry_baseline": forced_energy,
        "excess_collision_energy": excess_energy,
        "max_nonzero_difference_multiplicity": int(difference_counts[1:].max()),
        "pass": bool(
            cayley_identity_ok
            and mobius_intersections_match
            and collision_energy == nonzero_additive_energy
        ),
    }


def matching_rank_audit() -> dict[str, object]:
    """Classify the characteristic-zero six-term matching systems exactly.

    For prime K, a cyclotomic collision first reduces to equality of two
    six-element exponent multisets.  Each of the 6! matchings is a homogeneous
    integer linear system in (i,j,r,s).  This audit proves that rank can change
    only in characteristic 2 and that the only admissible rank-two families in
    odd characteristic are identity and inversion-swap.
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
    rank_two_types: Counter[str] = Counter()

    coordinate_forms = [
        sp.Matrix([[1, 0, 0, 0]]),
        sp.Matrix([[0, 1, 0, 0]]),
        sp.Matrix([[0, 0, 1, 0]]),
        sp.Matrix([[0, 0, 0, 1]]),
    ]
    same_pair_forms = [
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

        if rank != 2:
            continue
        nullspace = matrix.nullspace()
        invalid = any(
            annihilates(form, nullspace)
            for form in coordinate_forms + same_pair_forms
        )
        if invalid:
            rank_two_types["invalid_zero_or_diagonal"] += 1
        elif all(annihilates(form, nullspace) for form in identity_forms):
            rank_two_types["identity_r_i_s_j"] += 1
        elif all(annihilates(form, nullspace) for form in inversion_forms):
            rank_two_types["inversion_swap_r_minus_j_s_minus_i"] += 1
        else:
            raise AssertionError("unexpected admissible rank-two matching family")

    return {
        "matching_count": math.factorial(6),
        "rank_counts_over_Q": dict(sorted(rank_counts.items())),
        "bad_rank_drop_primes": sorted(int(value) for value in bad_rank_drop_primes),
        "rank_two_matching_types": dict(sorted(rank_two_types.items())),
        "conclusion": (
            "For odd prime K, the characteristic-zero Cayley difference set "
            "has only identity and inversion-swap collisions."
        ),
        "pass": bool(
            bad_rank_drop_primes == {2}
            and rank_two_types["identity_r_i_s_j"] == 2
            and rank_two_types["inversion_swap_r_minus_j_s_minus_i"] == 2
            and rank_two_types["invalid_zero_or_diagonal"] == 26
        ),
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
    """Compute the exact possible reduction primes for an odd prime K.

    Galois scaling normalizes the first exponent to i=1. Every non-forced
    collision gives a nonzero algebraic integer P(zeta_K). A rational prime N
    supporting that collision must divide its norm, i.e. the resultant with
    Phi_K. We retain only N == 1 (mod K), the primes where F_N contains an
    order-K subgroup.
    """
    if not sp.isprime(order) or order == 2:
        raise ValueError("cyclotomic exception audit currently requires odd prime K")

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
        "possible_reduction_primes_N_congruent_1_mod_K": sorted(possible_primes),
        "pass": True,
    }


def verify_design(
    prime: int,
    subgroup_generator: int,
    subgroup_order: int,
    exceptional_primes: set[int] | None,
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
    row_pass = maximum_deviation < 1e-8 and energy["pass"]

    row: dict[str, object] = {
        "N": prime,
        "a": subgroup_generator,
        "K": subgroup_order,
        "m": int(dimension),
        "constraint_pair_count": len(pairs),
        "expected_pair_count": expected_count,
        "identity_max_abs_deviation": float(maximum_deviation),
        "cayley_energy": energy,
        "pass": bool(row_pass),
    }
    if exceptional_primes is not None:
        row["cyclotomic_exception_status"] = {
            "N_in_possible_exception_set": prime in exceptional_primes,
            "prediction": (
                "excess collisions allowed"
                if prime in exceptional_primes
                else "only forced central-symmetry collisions possible"
            ),
            "prediction_matches_finite_energy": bool(
                (prime in exceptional_primes)
                or energy["excess_collision_energy"] == 0
            ),
        }
        row["pass"] = bool(
            row["pass"]
            and row["cyclotomic_exception_status"]["prediction_matches_finite_energy"]
        )
    return row


def main() -> None:
    matching = matching_rank_audit()
    exceptions_11 = cyclotomic_exceptional_primes(11)
    exceptions_13 = cyclotomic_exceptional_primes(13)
    exception_sets = {
        11: set(exceptions_11["possible_reduction_primes_N_congruent_1_mod_K"]),
        13: set(exceptions_13["possible_reduction_primes_N_congruent_1_mod_K"]),
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
            "small-prime-order cyclotomic collision audit; not an asymptotic theorem."
        ),
        "exact_identities": [
            "d(u,v)=2/(c(u)-c(v)), c(h)=(h+1)/(h-1)",
            "sum_t C_H(t)^2 = E_plus(c(H\\{1})) - (K-1)^2",
            "c(h^-1)=-c(h)",
            "r_{A-A}(x)=#{h in H\\{1}: g_x(h) in H\\{1}} with g_x(h)=((2-x)h+x)/(2+x-xh)",
        ],
        "matching_rank_audit": matching,
        "cyclotomic_exception_audits": [exceptions_11, exceptions_13],
        "results": rows,
        "verdict": (
            "PASS"
            if matching["pass"]
            and all(audit["pass"] for audit in (exceptions_11, exceptions_13))
            and all(row["pass"] for row in rows)
            else "FAIL"
        ),
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
