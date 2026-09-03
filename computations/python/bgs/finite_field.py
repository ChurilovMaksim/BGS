"""Small dependency-free finite-field helpers shared by active Python code."""
from __future__ import annotations


def distinct_prime_factors(n: int) -> list[int]:
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
    if prime < 3:
        raise ValueError("prime must be an odd prime")
    factors = distinct_prime_factors(prime - 1)
    for generator in range(2, prime):
        if all(pow(generator, (prime - 1) // q, prime) != 1 for q in factors):
            return generator
    raise ValueError(f"no primitive root modulo {prime}")


def multiplicative_order(value: int, prime: int) -> int:
    """Return the order of a nonzero residue using divisor reduction."""
    value %= prime
    if value == 0:
        raise ValueError("zero has no multiplicative order")
    order = prime - 1
    for q in distinct_prime_factors(order):
        while order % q == 0 and pow(value, order // q, prime) == 1:
            order //= q
    return order
