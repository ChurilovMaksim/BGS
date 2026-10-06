#!/usr/bin/env python3
"""Exact regression for cayley_principal_subresultant_support.md.

The fixed-degree maximal-real row polynomials are imported from the existing
real-trace verifier.  From their subresultant sequence we keep only

    psc_0, psc_1, psc_2,

where psc_j is the coefficient of T^j in the j-th subresultant polynomial.
The three-scalar ideal is contracted to Z by Smith normal form.

Finite anchors verify split prime support only; equality with the older
Lambda/Omega integers is deliberately not asserted.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

from cayley_product_row_real_trace_ideal import (
    TAU,
    T,
    reduce_T_polynomial,
    reduce_real,
    strip_2K,
    trace_cofactor_pair,
)


def principal_subresultant_scalars(
    K: int, r: int
) -> tuple[sp.Poly, list[sp.Expr]]:
    modulus, P, Q = trace_cofactor_pair(K, r)
    raw = sp.subresultants(P.as_expr(), Q.as_expr(), T)
    reduced = [reduce_T_polynomial(expr, modulus) for expr in raw]

    # Characteristic zero is coprime after removing the forced invalid root,
    # so the standard sequence ends at degrees 2,1,0.
    selected = reduced[-3:]
    degrees = [poly.degree() for poly in selected]
    assert degrees == [2, 1, 0], (K, r, degrees)

    # Store in increasing principal-subresultant index order.
    pi_2 = reduce_real(selected[0].nth(2), modulus)
    pi_1 = reduce_real(selected[1].nth(1), modulus)
    pi_0 = reduce_real(selected[2].nth(0), modulus)
    assert pi_0 != 0 and pi_1 != 0 and pi_2 != 0
    return modulus, [pi_0, pi_1, pi_2]


def contract_scalar_ideal(
    modulus: sp.Poly, generators: list[sp.Expr]
) -> tuple[int, list[int]]:
    degree = modulus.degree()
    columns: list[sp.Matrix] = []
    for generator in generators:
        for j in range(degree):
            reduced = sp.Poly(
                reduce_real(generator * TAU**j, modulus),
                TAU,
                domain=sp.ZZ,
            )
            columns.append(
                sp.Matrix([int(reduced.nth(k)) for k in range(degree)])
            )

    lattice = sp.Matrix.hstack(*columns)
    smith = smith_normal_form(lattice, domain=sp.ZZ)
    invariants = [
        abs(int(smith[j, j]))
        for j in range(min(smith.rows, smith.cols))
        if smith[j, j] != 0
    ]
    assert len(invariants) == degree
    assert all(
        invariants[j + 1] % invariants[j] == 0
        for j in range(len(invariants) - 1)
    )
    return invariants[-1], invariants


def check_anchor(
    K: int,
    r: int,
    expected_full: int,
    expected_stripped: int,
) -> None:
    modulus, generators = principal_subresultant_scalars(K, r)
    full, invariants = contract_scalar_ideal(modulus, generators)
    stripped = strip_2K(full, K)
    assert full == expected_full, (K, r, full, expected_full)
    assert stripped == expected_stripped, (
        K,
        r,
        stripped,
        expected_stripped,
    )
    print(
        f"K={K:2d} r={r:2d} Pi3={full} Pi3'={stripped} "
        f"smith_rank={len(invariants)}"
    )


def main() -> None:
    for K, r, full, stripped in (
        (7, 2, 7, 1),
        (11, 7, 11**2, 1),
        (13, 3, 13**3, 1),
        (13, 12, 2**4 * 5**3 * 13**3, 5**3),
        (17, 10, 2**2 * 17**5 * 103, 103),
    ):
        check_anchor(K, r, full, stripped)

    print("cayley principal-subresultant scalar support regression: OK")


if __name__ == "__main__":
    main()
