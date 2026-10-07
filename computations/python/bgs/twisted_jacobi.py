"""Reusable arithmetic for the active twisted-Jacobi finite regressions."""
from __future__ import annotations

import numpy as np

from .finite_field import (multiplicative_order, primitive_root, require_integer,
                           require_odd_prime)
from .jacobi import dlog_table, require_supported_prime

TRACE = 3


def square_roots_mod_prime(value: int, prime: int) -> list[int]:
    """Return all square roots of ``value`` modulo an odd prime."""
    prime = require_integer(prime, "prime")
    value = require_integer(value, "value")
    require_odd_prime(prime)
    value %= prime
    if value == 0:
        return [0]
    if pow(value, (prime - 1) // 2, prime) != 1:
        return []
    if prime % 4 == 3:
        root = pow(value, (prime + 1) // 4, prime)
        return sorted({root, (-root) % prime})

    odd_part = prime - 1
    two_adic_order = 0
    while odd_part % 2 == 0:
        odd_part //= 2
        two_adic_order += 1

    non_residue = 2
    while pow(non_residue, (prime - 1) // 2, prime) != prime - 1:
        non_residue += 1

    m = two_adic_order
    c = pow(non_residue, odd_part, prime)
    t = pow(value, odd_part, prime)
    root = pow(value, (odd_part + 1) // 2, prime)

    while t != 1:
        i = 0
        t_power = t
        while t_power != 1:
            t_power = t_power * t_power % prime
            i += 1
            if i >= m:
                raise RuntimeError("Tonelli-Shanks iteration failed")
        b = pow(c, 1 << (m - i - 1), prime)
        m = i
        c = b * b % prime
        t = t * c % prime
        root = root * b % prime

    return sorted({root, (-root) % prime})


def find_design_eigenvalue(
    prime: int,
    subgroup_order: int,
    trace: int = TRACE,
) -> int:
    """Find a root of ``x^2-trace*x+1`` of exactly the requested order."""
    prime = require_integer(prime, "prime")
    subgroup_order = require_integer(subgroup_order, "subgroup_order")
    trace = require_integer(trace, "trace")
    require_odd_prime(prime)
    if subgroup_order <= 0 or (prime - 1) % subgroup_order:
        raise ValueError("subgroup_order must divide prime-1")

    roots = square_roots_mod_prime(trace * trace - 4, prime)
    if not roots:
        raise ValueError(f"N={prime} is not split for trace={trace}")

    inverse_two = pow(2, prime - 2, prime)
    for root in roots:
        candidate = (trace + root) * inverse_two % prime
        if multiplicative_order(candidate, prime) == subgroup_order:
            return candidate
    raise ValueError(
        f"no eigenvalue of order K={subgroup_order} at N={prime}"
    )


def build_closed_form(
    prime: int,
    subgroup_order: int,
    eigenvalue: int,
    residue_class: int,
    odd_parity: bool,
    q_values,
):
    """Compute finite standardized moments in the recorded character sector.

    ``eigenvalue`` is a checked design parameter: it must have exact order
    ``subgroup_order``.  This routine is a numerical/finite-regression helper,
    not a theorem about an asymptotic ensemble. All discrete inputs must be
    exact integers (NumPy integer scalars are accepted); booleans are valid
    for ``odd_parity`` only. Residue representatives are reduced before
    vectorized arithmetic.
    """
    prime = require_supported_prime(prime)
    subgroup_order = require_integer(subgroup_order, "subgroup_order")
    eigenvalue = require_integer(eigenvalue, "eigenvalue") % prime
    residue_class = require_integer(residue_class, "residue_class")
    if not isinstance(odd_parity, (bool, np.bool_)):
        raise ValueError("odd_parity must be a boolean")
    odd_parity = bool(odd_parity)
    if subgroup_order <= 0 or (prime - 1) % subgroup_order:
        raise ValueError("subgroup_order must divide prime-1")
    actual_order = multiplicative_order(eigenvalue, prime)
    if actual_order != subgroup_order:
        raise ValueError(
            f"eigenvalue has order {actual_order}, expected {subgroup_order}"
        )

    generator = primitive_root(prime)
    dlog = dlog_table(prime, generator)

    character_indices = np.array(
        [
            k
            for k in range(prime - 1)
            if k % subgroup_order == residue_class % subgroup_order
            and (k % 2 == 1) == odd_parity
        ],
        dtype=np.int64,
    )
    dimension = len(character_indices)
    if dimension == 0:
        raise ValueError("requested character/parity sector is empty")

    x_values = np.arange(2, prime, dtype=np.int64)
    log_x = dlog[x_values]
    log_x_minus_one = dlog[(x_values - 1) % prime]
    left = np.exp(
        -2j * np.pi * np.outer(character_indices, log_x) / (prime - 1)
    )
    right = np.exp(
        2j * np.pi * np.outer(character_indices, log_x_minus_one) / (prime - 1)
    )

    inverse_two = pow(2, prime - 2, prime)
    output: dict[int, dict[str, float | int]] = {}
    for q_value in q_values:
        q = require_integer(q_value, "q") % prime
        additive_phase = np.exp(2j * np.pi * (q * x_values % prime) / prime)
        jacobi = (left * additive_phase) @ right.T
        normalized = (
            np.exp(-2j * np.pi * (inverse_two * q % prime) / prime)
            * jacobi
            / (prime - 1)
        )
        hermitian = normalized + normalized.conj().T
        eigenvalues = np.linalg.eigvalsh(hermitian)
        centered = eigenvalues - eigenvalues.mean()
        variance = float((centered**2).mean())
        if not variance > 0.0:
            raise ValueError(f"zero spectral variance at q={q}")
        standardized = centered / np.sqrt(variance)
        output[q] = {
            "m": int(dimension),
            "s2": variance,
            "mu4": float((standardized**4).mean()),
            "mu6": float((standardized**6).mean()),
            "tr2": float((eigenvalues**2).sum()),
        }

    return output, dimension


sqrt_mod = square_roots_mod_prime
