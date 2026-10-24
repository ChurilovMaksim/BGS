#!/usr/bin/env python3
"""Exact regression for the polynomial-scale Cayley energy route.

This script checks the algebraic surrogate used in
``mathematics/cayley-arithmetic/cayley_energy_curve_bound.md`` and several finite designs.  It
is deliberately not a proof of the Makarychev--Vyugin point bound.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass

import sympy as sp


@dataclass(frozen=True)
class Design:
    p: int
    generator: int
    k: int
    direct_energy: int
    enlarged_curve_total: int
    max_offdiag_curve: int


def symbolic_audit() -> None:
    U, V, x, y, rho, sigma = sp.symbols("U V x y rho sigma")

    F = (
        (1 - sigma) * y * (rho * x - 1) * (x - 1)
        - (1 - rho) * x * (sigma * y - 1) * (y - 1)
    )
    G = sp.expand(
        sigma * (rho - 1) * U**2 * V**2
        + rho * (1 - sigma) * U**2
        + 2 * (sigma - rho) * U * V
        + (1 - sigma) * V**2
        + (rho - 1)
    )

    transformed = sp.cancel((V / U) * F.subs({x: U / V, y: U * V}))
    if sp.simplify(transformed - G) != 0:
        raise AssertionError("toric transform identity failed")

    discriminant = sp.factor(sp.discriminant(G, U))
    expected_discriminant = sp.factor(
        -4
        * (rho - 1)
        * (sigma - 1)
        * (rho - sigma * V**2)
        * (V**2 - 1)
    )
    if sp.expand(discriminant - expected_discriminant) != 0:
        raise AssertionError("quadratic discriminant identity failed")

    diagonal = sp.factor(G.subs(sigma, rho))
    expected_diagonal = (rho - 1) * (V**2 - 1) * (rho * U**2 - 1)
    if sp.expand(diagonal - expected_diagonal) != 0:
        raise AssertionError("parameter-diagonal factorization failed")

    print("symbolic curve identities: PASS")


def prime_divisors(n: int) -> list[int]:
    out: list[int] = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def has_exact_order(a: int, order: int, p: int) -> bool:
    if pow(a, order, p) != 1:
        return False
    return all(pow(a, order // q, p) != 1 for q in prime_divisors(order))


def subgroup(p: int, generator: int, k: int) -> list[int]:
    if not has_exact_order(generator, k, p):
        raise AssertionError(f"{generator=} does not have order {k} modulo {p}")
    return [pow(generator, j, p) for j in range(k)]


def inv(x: int, p: int) -> int:
    if x % p == 0:
        raise ZeroDivisionError("finite-field inverse of zero")
    return pow(x, p - 2, p)


def cayley(h: int, p: int) -> int:
    return (h + 1) * inv(h - 1, p) % p


def d_value(u: int, v: int, p: int) -> int:
    return (u - 1) * (v - 1) * inv(v - u, p) % p


def ratio_value(rho: int, x: int, p: int) -> int:
    return (
        (rho * x + inv(x, p) - rho - 1) * inv(1 - rho, p)
    ) % p


def transformed_curve_value(rho: int, sigma: int, U: int, V: int, p: int) -> int:
    U2 = U * U % p
    V2 = V * V % p
    return (
        sigma * (rho - 1) * U2 * V2
        + rho * (1 - sigma) * U2
        + 2 * (sigma - rho) * U * V
        + (1 - sigma) * V2
        + (rho - 1)
    ) % p


def audit_design(design: Design) -> None:
    p, k = design.p, design.k
    H = subgroup(p, design.generator, k)

    direct = Counter()
    for u in H:
        if u == 1:
            continue
        for v in H:
            if v == 1 or u == v:
                continue
            direct[d_value(u, v, p)] += 1
    direct_energy = sum(value * value for value in direct.values())
    if direct_energy != design.direct_energy:
        raise AssertionError((p, k, direct_energy, design.direct_energy))

    parameters = [rho for rho in H if rho != 1]
    enlarged_total = 0
    max_offdiag = 0
    for rho in parameters:
        diagonal_count = 0
        for sigma in parameters:
            ratio_count = 0
            transformed_count = 0
            for x in H:
                rx = ratio_value(rho, x, p)
                for y in H:
                    ratio_equal = rx == ratio_value(sigma, y, p)
                    ratio_count += ratio_equal

            # The monomial map (U,V)->(U/V,UV) is a bijection on H^2 for
            # odd K.  Count the transformed polynomial independently.
            for U in H:
                for V in H:
                    transformed_count += transformed_curve_value(
                        rho, sigma, U, V, p
                    ) == 0

            if ratio_count != transformed_count:
                raise AssertionError(
                    f"curve transform mismatch at {(p, k, rho, sigma)}: "
                    f"{ratio_count} != {transformed_count}"
                )
            enlarged_total += ratio_count
            if rho == sigma:
                diagonal_count = ratio_count
            else:
                max_offdiag = max(max_offdiag, ratio_count)

        if diagonal_count != 2 * k - 1:
            raise AssertionError(
                f"diagonal fibre count at {(p, k, rho)} is {diagonal_count}, "
                f"expected {2*k-1}"
            )

    if enlarged_total != design.enlarged_curve_total:
        raise AssertionError(
            (p, k, "curve_total", enlarged_total, design.enlarged_curve_total)
        )
    if max_offdiag != design.max_offdiag_curve:
        raise AssertionError(
            (p, k, "max_offdiag", max_offdiag, design.max_offdiag_curve)
        )
    if direct_energy > enlarged_total:
        raise AssertionError("domain enlargement decreased the energy count")

    print(
        f"finite curve audit: PASS p={p} K={k} "
        f"direct={direct_energy} enlarged={enlarged_total} "
        f"max_offdiag={max_offdiag}"
    )


def main() -> None:
    symbolic_audit()
    designs = [
        Design(199, 139, 11, 170, 570, 4),
        Design(67, 64, 11, 218, 618, 8),
        Design(521, 101, 13, 252, 828, 4),
        Design(53, 10, 13, 460, 1036, 12),
        Design(461, 23, 23, 1190, 3126, 12),
    ]
    for design in designs:
        audit_design(design)
    print("cayley energy curve regression: PASS")


if __name__ == "__main__":
    main()
