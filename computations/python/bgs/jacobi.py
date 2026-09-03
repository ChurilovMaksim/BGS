"""Core character-coset and twisted-Jacobi matrix primitives.

These routines are implementation primitives, not theorem statements. They
validate the finite-field design metadata aggressively so that a wrong
eigenvalue order or non-primitive logarithm generator cannot silently produce
a plausible-looking matrix.
"""
from __future__ import annotations

import math

import numpy as np

from .finite_field import multiplicative_order, require_odd_prime


def dlog_table(prime: int, generator: int) -> np.ndarray:
    """Return the discrete-log table for a primitive root modulo ``prime``."""
    require_odd_prime(prime)
    generator %= prime
    if generator == 0:
        raise ValueError("discrete-log generator must be nonzero")

    table = np.full(prime, -1, dtype=np.int64)
    value = 1
    for exponent in range(prime - 1):
        if table[value] != -1:
            raise ValueError(f"generator {generator} is not primitive modulo {prime}")
        table[value] = exponent
        value = value * generator % prime

    if value != 1 or np.any(table[1:] < 0):
        raise ValueError(f"generator {generator} does not generate F_{prime}^*")
    return table


def annihilator_indices(
    prime: int,
    subgroup_order: int,
    eigenvalue: int,
    dlog: np.ndarray,
) -> np.ndarray:
    """Return character indices ``k`` satisfying ``chi_k(eigenvalue)=1``.

    The supplied eigenvalue is required to have *exactly* ``subgroup_order``.
    This turns the design metadata into a checked contract instead of an
    ignored annotation.
    """
    require_odd_prime(prime)
    if subgroup_order <= 0 or (prime - 1) % subgroup_order:
        raise ValueError("subgroup_order must be a positive divisor of prime-1")
    if len(dlog) != prime:
        raise ValueError("discrete-log table has the wrong length")
    eigenvalue %= prime
    if eigenvalue == 0:
        raise ValueError("eigenvalue must lie in F_p^*")
    actual_order = multiplicative_order(eigenvalue, prime)
    if actual_order != subgroup_order:
        raise ValueError(
            f"eigenvalue has order {actual_order}, expected {subgroup_order}"
        )

    exponent = int(dlog[eigenvalue])
    if exponent < 0:
        raise ValueError("eigenvalue is absent from the discrete-log table")
    step = (prime - 1) // math.gcd(exponent, prime - 1)
    indices = np.arange(0, prime - 1, step, dtype=np.int64)
    expected_dimension = (prime - 1) // subgroup_order
    if len(indices) != expected_dimension:
        raise AssertionError(
            "annihilator dimension disagrees with (prime-1)/subgroup_order"
        )
    return indices


def jacobi_matrix(
    prime: int,
    subgroup_order: int,
    eigenvalue: int,
    dlog: np.ndarray,
    character_indices: np.ndarray,
    q: int,
) -> np.ndarray:
    """Return the twisted-Jacobi matrix in the active character convention."""
    expected = annihilator_indices(prime, subgroup_order, eigenvalue, dlog)
    supplied = np.asarray(character_indices, dtype=np.int64)
    if not np.array_equal(supplied, expected):
        raise ValueError(
            "character_indices do not equal the annihilator of the supplied eigenvalue"
        )

    x_values = np.arange(2, prime, dtype=np.int64)
    log_x = dlog[x_values]
    log_x_minus_one = dlog[(x_values - 1) % prime]

    left = np.exp(
        -2j * np.pi * np.outer(supplied, log_x) / (prime - 1)
    )
    right = np.exp(
        2j * np.pi * np.outer(supplied, log_x_minus_one) / (prime - 1)
    )
    additive_phase = np.exp(2j * np.pi * (q * x_values % prime) / prime)
    return (left * additive_phase) @ right.T
