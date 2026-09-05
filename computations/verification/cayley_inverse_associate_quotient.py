#!/usr/bin/env python3
"""Exact regression for cayley_inverse_associate_quotient.md.

Finite controls:
  * a noncanonical K=31 nonunit associate class;
  * exact K=59 cross-class ideal contraction;
  * small-p multiplicity countercontrols K=83,89;
  * a large-p K=139 structural multiplicity-four control.

The universal quotient reduction is proved in the mathematics note.
"""
from __future__ import annotations

import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form

from cayley_inverse_structural_associates import (
    T,
    real_cyclotomic_polynomial,
    v_polynomial,
    zero_edges,
)


def w_polynomial(a: int, b: int) -> sp.Poly:
    return sp.Poly(2, T, domain=sp.ZZ) - v_polynomial(a) - v_polynomial(b)


def edge_norm(K: int, e: tuple[int, int]) -> int:
    C = real_cyclotomic_polynomial(K)
    return abs(int(sp.resultant(C.as_expr(), w_polynomial(*e).as_expr(), T)))


def quotient_unit(K: int, e: tuple[int, int], f: tuple[int, int]) -> sp.Poly:
    C = real_cyclotomic_polynomial(K)
    we = w_polynomial(*e)
    wf = w_polynomial(*f)
    inv = sp.invert(wf.as_expr(), C.as_expr(), domain=sp.QQ)
    q_expr = sp.rem(we.as_expr() * inv, C.as_expr(), domain=sp.QQ)
    q = sp.Poly(sp.expand(q_expr), T, domain=sp.QQ)
    assert all(c.q == 1 for c in q.all_coeffs())
    qz = sp.Poly(q.as_expr(), T, domain=sp.ZZ)
    unit_norm = int(sp.resultant(C.as_expr(), qz.as_expr(), T))
    assert abs(unit_norm) == 1
    return qz


def coefficient_vector(poly: sp.Poly, m: int) -> sp.Matrix:
    return sp.Matrix([int(poly.nth(j)) for j in range(m)])


def multiplication_columns(C: sp.Poly, w: sp.Poly) -> list[sp.Matrix]:
    m = C.degree()
    out: list[sp.Matrix] = []
    for i in range(m):
        rem = sp.Poly(
            sp.rem(T**i * w.as_expr(), C.as_expr(), domain=sp.ZZ),
            T,
            domain=sp.ZZ,
        )
        out.append(coefficient_vector(rem, m))
    return out


def ideal_contraction_generator(
    K: int,
    e: tuple[int, int],
    f: tuple[int, int],
) -> tuple[int, int]:
    C = real_cyclotomic_polynomial(K)
    m = C.degree()
    M = sp.Matrix.hstack(
        *(
            multiplication_columns(C, w_polynomial(*e))
            + multiplication_columns(C, w_polynomial(*f))
        )
    )
    H = hermite_normal_form(M)
    assert H.shape == (m, m) and H.det() != 0
    e0 = sp.Matrix([1] + [0] * (m - 1))
    coordinates = H.inv() * e0
    d = 1
    for value in coordinates:
        d = sp.ilcm(d, sp.denom(value))
    assert all((d * value).q == 1 for value in coordinates)
    return int(d), abs(int(H.det()))


def primitive_K_root(K: int, p: int) -> int:
    assert p % K == 1
    g = int(sp.primitive_root(p))
    h = pow(g, (p - 1) // K, p)
    assert h != 1 and pow(h, K, p) == 1
    return h


def maximum_zero_edges(K: int, p: int):
    h0 = primitive_K_root(K, p)
    m = (K - 1) // 2
    best: tuple[int, int, list[tuple[int, int]]] = (0, 0, [])
    for j in range(1, m + 1):
        edges = zero_edges(K, p, pow(h0, j, p))
        candidate = (len(edges), j, edges)
        if candidate[0] > best[0]:
            best = candidate
    return best


def check_unit_skeleton_anchor() -> None:
    # Exact polynomial checks of the two universal formulas at one conductor.
    K = 31
    C = real_cyclotomic_polynomial(K)
    tau = sp.Poly(T, T, domain=sp.ZZ)

    for a in (2, 5, 10, 13):
        left = w_polynomial(a, a + 2)
        right = -tau * v_polynomial(a + 1)
        rem = sp.rem(left.as_expr() - right.as_expr(), C.as_expr(), domain=sp.ZZ)
        assert sp.Poly(rem, T, domain=sp.ZZ).is_zero

    m = (K - 1) // 2
    left = w_polynomial(0, m - 1)
    right = -(tau - sp.Poly(1, T, domain=sp.ZZ)) * v_polynomial(m)
    rem = sp.rem(left.as_expr() - right.as_expr(), C.as_expr(), domain=sp.ZZ)
    assert sp.Poly(rem, T, domain=sp.ZZ).is_zero
    assert edge_norm(K, (0, m - 1)) == 1
    print("canonical unit-edge skeleton K=31 anchor: OK")


def check_k31_extra_associate() -> None:
    K = 31
    e = (2, 11)
    f = (5, 12)
    assert edge_norm(K, e) == 1303
    assert edge_norm(K, f) == 1303
    q = quotient_unit(K, e, f)
    print(
        "K=31 additional nonunit associate class "
        f"{e}~{f}, quotient degree={q.degree()}, norm=+-1: OK"
    )


def check_k59_cross_class_contraction() -> None:
    K = 59
    e = (8, 26)
    f = (9, 10)
    n_e = edge_norm(K, e)
    n_f = edge_norm(K, f)
    assert n_e != n_f  # associates would have equal absolute norm
    d, index = ideal_contraction_generator(K, e, f)
    assert d == 21713
    assert index == 21713
    print(
        "K=59 cross-class contraction "
        f"({e},{f}) cap Z = 21713 Z, quotient index=21713: OK"
    )


def check_scale_controls() -> None:
    n83, j83, _ = maximum_zero_edges(83, 167)
    assert n83 == 7 and 2 * n83 == 14
    n89, j89, _ = maximum_zero_edges(89, 179)
    assert n89 == 8 and 2 * n89 == 16
    print(f"K=83 p=167: max zero edges=7 at emb={j83}, I_inverse=14: OK")
    print(f"K=89 p=179: max zero edges=8 at emb={j89}, I_inverse=16: OK")

    K = 139
    p = 3_596_704_231
    assert sp.isprime(p) and p % K == 1 and p > K**4
    n, j, edges = maximum_zero_edges(K, p)
    expected = [(26, 55), (30, 53)]
    assert n == 2 and edges == expected
    print(
        f"K=139 p={p}: p/K^4={p / K**4:.12f}, "
        f"emb={j}, zero_edges={edges}, I_inverse=4: OK"
    )


def main() -> None:
    check_unit_skeleton_anchor()
    check_k31_extra_associate()
    check_k59_cross_class_contraction()
    check_scale_controls()
    print("cayley inverse associate-quotient regression: OK")


if __name__ == "__main__":
    main()
