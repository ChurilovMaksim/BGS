"""Core character-coset and twisted-Jacobi matrix primitives."""
from __future__ import annotations

import math

import numpy as np


def dlog_table(prime: int, generator: int) -> np.ndarray:
    """Return the discrete-log table for a primitive root modulo ``prime``."""
    table = np.zeros(prime, dtype=np.int64)
    value = 1
    for exponent in range(prime - 1):
        table[value] = exponent
        value = value * generator % prime
    return table


def annihilator_indices(
    prime: int,
    subgroup_order: int,
    eigenvalue: int,
    dlog: np.ndarray,
) -> np.ndarray:
    """Return character indices ``k`` satisfying ``chi_k(eigenvalue)=1``.

    ``subgroup_order`` is kept in the signature as design metadata.  The
    annihilator itself is determined from the discrete logarithm of the
    supplied eigenvalue.
    """
    del subgroup_order
    exponent = int(dlog[eigenvalue])
    step = (prime - 1) // math.gcd(exponent, prime - 1)
    return np.array(
        [k for k in range(prime - 1) if k % step == 0],
        dtype=np.int64,
    )


def jacobi_matrix(
    prime: int,
    subgroup_order: int,
    eigenvalue: int,
    dlog: np.ndarray,
    character_indices: np.ndarray,
    q: int,
) -> np.ndarray:
    """Return the twisted-Jacobi matrix in the active character convention."""
    del subgroup_order, eigenvalue

    x_values = np.arange(2, prime, dtype=np.int64)
    log_x = dlog[x_values]
    log_x_minus_one = dlog[(x_values - 1) % prime]

    left = np.exp(
        -2j
        * np.pi
        * np.outer(character_indices, log_x)
        / (prime - 1)
    )
    right = np.exp(
        2j
        * np.pi
        * np.outer(character_indices, log_x_minus_one)
        / (prime - 1)
    )
    additive_phase = np.exp(2j * np.pi * (q * x_values % prime) / prime)
    return (left * additive_phase) @ right.T
