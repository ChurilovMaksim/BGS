"""Small dependency-free finite-field helpers shared by active Python code."""
from __future__ import annotations

from numbers import Integral


def require_integer(value: int, name: str) -> int:
    """Return an exact Python integer; reject booleans and coercible floats.

    NumPy integer scalars implement Integral; NumPy booleans do not.
    """
    if isinstance(value, bool) or not isinstance(value, Integral):
        raise ValueError(f"{name} must be an integer (not a boolean)")
    return int(value)


def is_prime(n: int) -> bool:
    """Return whether integer ``n`` is prime by deterministic trial division.

    Non-integral inputs and booleans raise ValueError, rather than silently
    coercing them or reporting them as composite. NumPy integers are accepted.

    Active computations use modest finite-field characteristics, so this
    deliberately simple check is preferable to silently accepting a composite
    modulus and then applying Fermat inverses.
    """
    n = require_integer(n, "n")
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def require_odd_prime(prime: int) -> None:
    """Fail fast unless ``prime`` is an odd prime."""
    prime = require_integer(prime, "prime")
    if prime < 3 or not is_prime(prime):
        raise ValueError(f"expected an odd prime modulus, got {prime}")


def distinct_prime_factors(n: int) -> list[int]:
    """Return the distinct prime factors of a positive integer."""
    n = require_integer(n, "n")
    if n < 1:
        raise ValueError("n must be positive")
    factors: list[int] = []
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            while n % divisor == 0:
                n //= divisor
        divisor += 1 if divisor == 2 else 2
    if n > 1:
        factors.append(n)
    return factors


def primitive_root(prime: int) -> int:
    """Return the least primitive root modulo an odd prime."""
    prime = require_integer(prime, "prime")
    require_odd_prime(prime)
    factors = distinct_prime_factors(prime - 1)
    for generator in range(2, prime):
        if all(pow(generator, (prime - 1) // q, prime) != 1 for q in factors):
            return generator
    raise RuntimeError(f"primitive root not found modulo prime {prime}")


def multiplicative_order(value: int, prime: int) -> int:
    """Return the multiplicative order of a nonzero residue modulo an odd prime."""
    prime = require_integer(prime, "prime")
    value = require_integer(value, "value")
    require_odd_prime(prime)
    value %= prime
    if value == 0:
        raise ValueError("zero has no multiplicative order")
    order = prime - 1
    for q in distinct_prime_factors(order):
        while order % q == 0 and pow(value, order // q, prime) == 1:
            order //= q
    return order
