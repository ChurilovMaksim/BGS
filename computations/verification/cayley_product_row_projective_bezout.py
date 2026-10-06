#!/usr/bin/env python3
"""Regression for cayley_product_row_projective_bezout.md.

Default mode is deliberately fast enough for CI.  It checks

* the universal trace polynomial and its differential equation,
* reconstruction of finite-field row polynomials from the universal formula,
* the first two row symmetric sums,
* equality between ambient Bezout nullity and direct projective row
  intersection counts on both false-positive and genuine high-intersection
  designs.

``--extended`` adds the K=23 geometric anchors.  ``--ideal-norm-small``
computes exact HNF norms of the projective determinantal ideals for K=7 and
all unordered ratio classes at K=11.  The HNF mode is exact but intentionally
not part of default CI because it is much slower.

Finite computation is regression evidence, not a proof of the universal
statements in the mathematics note.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import argparse
import itertools
import math
import sys
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "computations" / "python"))

from bgs.finite_field import primitive_root  # noqa: E402
from cayley_product_row_subresultants import (  # noqa: E402
    reduce_cyclotomic,
    row_polynomial,
)

X, U = sp.symbols("X U")


def multiplicative_order(x: int, p: int) -> int:
    x %= p
    if x == 0:
        raise ValueError("order requires a nonzero residue")
    value = 1
    for order in range(1, p):
        value = value * x % p
        if value == 1:
            return order
    raise AssertionError("multiplicative order search failed")


def subgroup(p: int, K: int) -> list[int]:
    assert (p - 1) % K == 0
    g = primitive_root(p)
    h = pow(g, (p - 1) // K, p)
    H = [pow(h, j, p) for j in range(K)]
    assert len(set(H)) == K
    return H


def cayley(x: int, p: int) -> int:
    assert x % p != 1
    return (x + 1) * pow((x - 1) % p, -1, p) % p


def polynomial_eval(coeffs: list[int], x: int, p: int) -> int:
    """Evaluate ascending coefficients modulo p."""
    value = 0
    for coeff in reversed(coeffs):
        value = (value * x + coeff) % p
    return value


def derivative_coeffs(coeffs: list[int], order: int, p: int) -> list[int]:
    out = [value % p for value in coeffs]
    for _ in range(order):
        out = [(j * out[j]) % p for j in range(1, len(out))]
    return out


def universal_coeffs(K: int) -> list[int]:
    m = (K - 1) // 2
    return [math.comb(K, 2 * j) for j in range(m + 1)]


def check_universal_ode(K: int) -> None:
    """Check the exact coefficient form of the universal ODE over Z."""
    b = universal_coeffs(K)
    m = (K - 1) // 2
    for j in range(m):
        lhs = (
            2 * j * j + (1 - 2 * K) * j + K * (K - 1) // 2
        ) * b[j]
        rhs = (j + 1) * (2 * j + 1) * b[j + 1]
        assert lhs == rhs, (K, j, lhs, rhs)


def universal_row_polynomial(p: int, K: int, w: int) -> list[int]:
    """Return the monic row polynomial W_C(T) modulo p, ascending."""
    m = (K - 1) // 2
    C = cayley(w, p)
    a = C * C % p
    P = universal_coeffs(K)

    assert polynomial_eval(P, a, p) == 0
    Pprime = derivative_coeffs(P, 1, p)
    Pprime_a = polynomial_eval(Pprime, a, p)
    assert Pprime_a != 0
    inv_Pprime = pow(Pprime_a, -1, p)

    # F_a(Z)=sum_{k=1}^m d_k(a)(1-a)^(k-1)/k! Z^(m+1-k).
    F = [0] * (m + 1)
    factorial = 1
    for k in range(1, m + 1):
        factorial = factorial * k % p
        derivative = derivative_coeffs(P, k, p)
        d_k = polynomial_eval(derivative, a, p) * inv_Pprime % p
        coefficient = (
            d_k
            * pow((1 - a) % p, k - 1, p)
            * pow(factorial, -1, p)
        ) % p
        F[m + 1 - k] = coefficient

    assert F[0] == 0
    assert F[m] == 1

    # W_C(T)=(-2C)^m F_a(1-T/(2C)).
    q = pow((2 * C) % p, -1, p)
    scale = pow((-2 * C) % p, m, p)
    W = [0] * (m + 1)
    for j, coefficient in enumerate(F):
        for ell in range(j + 1):
            W[ell] = (
                W[ell]
                + scale
                * coefficient
                * math.comb(j, ell)
                * pow((-q) % p, ell, p)
            ) % p
    assert W[m] == 1
    return W


def direct_row_parameters(p: int, K: int, w: int) -> set[int]:
    H = subgroup(p, K)
    inverses = {x: pow(x, -1, p) for x in H}
    u = w * w % p
    params: set[int] = set()
    for x in H:
        if x == 1:
            continue
        y = u * inverses[x] % p
        if y == 1:
            continue
        params.add((cayley(x, p) + cayley(y, p)) % p)
    assert len(params) == (K - 1) // 2
    return params


def check_universal_rows(p: int, K: int) -> None:
    H = subgroup(p, K)
    inv2 = pow(2, -1, p)
    inv6 = pow(6, -1, p)

    # Several Galois-conjugate rows, not a single hand-picked one.
    for w in H[1 : min(5, K)]:
        W = universal_row_polynomial(p, K, w)
        roots = {t for t in range(p) if polynomial_eval(W, t, p) == 0}
        direct = direct_row_parameters(p, K, w)
        assert roots == direct, (p, K, w)

        C = cayley(w, p)
        e1 = sum(direct) % p
        e2 = sum((a * b) % p for a, b in itertools.combinations(direct, 2)) % p
        expected_e1 = (C - pow(C, -1, p)) * inv2 % p
        expected_e2 = (
            (K * K - 1) * inv6
            - (C * C - pow(C, -2, p)) * inv2
        ) % p
        assert e1 == expected_e1, (p, K, w, e1, expected_e1)
        assert e2 == expected_e2, (p, K, w, e2, expected_e2)


def projective_row_roots(p: int, K: int, h: int, i: int) -> set[tuple[int, int]]:
    """Roots [U:V] of the normalized projective row form after zeta->h."""
    i %= K
    assert i != 0
    m = (K - 1) // 2
    N = (1 - pow(h, 2 * i, p)) % p
    assert N != 0

    roots: set[tuple[int, int]] = set()
    for a in range(m + 1):
        if a == i or (-a) % K == i:
            continue
        trace = 2 if a == 0 else (pow(h, a, p) + pow(h, (-a) % K, p)) % p
        D = (pow(h, i, p) * trace - 2) % p
        root = (1, 0) if D == 0 else (N * pow(D, -1, p) % p, 1)
        roots.add(root)

    assert len(roots) == m
    return roots


def row_affine_coeffs(p: int, K: int, h: int, i: int) -> list[int]:
    """Ascending coefficients of R_i(U,1), padded through ambient degree m."""
    i %= K
    m = (K - 1) // 2
    N = (1 - pow(h, 2 * i, p)) % p
    coeffs = [1]

    for a in range(m + 1):
        if a == i or (-a) % K == i:
            continue
        trace = 2 if a == 0 else (pow(h, a, p) + pow(h, (-a) % K, p)) % p
        D = (pow(h, i, p) * trace - 2) % p
        nxt = [0] * (len(coeffs) + 1)
        for j, value in enumerate(coeffs):
            nxt[j] = (nxt[j] - N * value) % p
            nxt[j + 1] = (nxt[j + 1] + D * value) % p
        coeffs = nxt

    assert len(coeffs) == m + 1
    return coeffs


def bezout_matrix_mod(
    f: list[int], g: list[int], p: int, m: int
) -> list[list[int]]:
    """Ambient m x m Bezout matrix from ascending coefficients."""
    B = [[0] * m for _ in range(m)]
    for i in range(m + 1):
        for j in range(i):
            coefficient = (f[i] * g[j] - f[j] * g[i]) % p
            for k in range(i - j):
                row = i - 1 - k
                col = j + k
                B[row][col] = (B[row][col] + coefficient) % p
    return B


def rank_mod(matrix: list[list[int]], p: int) -> int:
    A = [row[:] for row in matrix]
    nrows = len(A)
    ncols = len(A[0]) if A else 0
    rank = 0

    for col in range(ncols):
        pivot = next((r for r in range(rank, nrows) if A[r][col] % p), None)
        if pivot is None:
            continue
        A[rank], A[pivot] = A[pivot], A[rank]
        inv = pow(A[rank][col] % p, -1, p)
        A[rank] = [(value * inv) % p for value in A[rank]]
        for r in range(nrows):
            if r == rank or A[r][col] % p == 0:
                continue
            factor = A[r][col] % p
            A[r] = [
                (A[r][c] - factor * A[rank][c]) % p
                for c in range(ncols)
            ]
        rank += 1
        if rank == nrows:
            break
    return rank


def check_projective_design(p: int, K: int, r: int, expected_max: int) -> None:
    m = (K - 1) // 2
    g = primitive_root(p)
    h0 = pow(g, (p - 1) // K, p)
    assert multiplicative_order(h0, p) == K

    histogram: dict[int, int] = {}
    maximum = 0
    for exponent in range(1, K):
        h = pow(h0, exponent, p)
        roots_1 = projective_row_roots(p, K, h, 1)
        roots_r = projective_row_roots(p, K, h, r)
        intersection = len(roots_1 & roots_r)

        f = row_affine_coeffs(p, K, h, 1)
        q = row_affine_coeffs(p, K, h, r)
        bezout = bezout_matrix_mod(f, q, p, m)
        nullity = m - rank_mod(bezout, p)
        assert nullity == intersection, (p, K, r, h, nullity, intersection)

        histogram[intersection] = histogram.get(intersection, 0) + 1
        maximum = max(maximum, intersection)

    assert maximum == expected_max, (p, K, r, maximum, expected_max)
    print(
        f"projective Bezout (K,p,r)=({K},{p},{r}) "
        f"max={maximum} histogram={dict(sorted(histogram.items()))}"
    )


def exact_bezout_matrix(K: int, A: sp.Poly, B: sp.Poly) -> sp.Matrix:
    m = (K - 1) // 2
    left = [A.nth(i) for i in range(m + 1)]
    right = [B.nth(i) for i in range(m + 1)]
    matrix = [[sp.Integer(0) for _ in range(m)] for _ in range(m)]

    for i in range(m + 1):
        for j in range(i):
            coefficient = reduce_cyclotomic(
                left[i] * right[j] - left[j] * right[i], K
            )
            if coefficient == 0:
                continue
            for k in range(i - j):
                row = i - 1 - k
                col = j + k
                matrix[row][col] = reduce_cyclotomic(
                    matrix[row][col] + coefficient, K
                )
    return sp.Matrix(matrix)


def projective_ideal_norm(K: int, r: int) -> int:
    """Exact norm of the (m-2)-minor determinantal ideal via an HNF lattice."""
    m = (K - 1) // 2
    if m < 3:
        return 1

    A = row_polynomial(K, 1)
    B = row_polynomial(K, r)
    bezout = exact_bezout_matrix(K, A, B)
    size = m - 2
    generators: list[sp.Expr] = []

    for rows in itertools.combinations(range(m), size):
        for cols in itertools.combinations(range(m), size):
            minor = reduce_cyclotomic(bezout.extract(rows, cols).det(), K)
            if minor != 0:
                generators.append(minor)
    assert generators

    # O_L=Z[zeta_K] has basis 1,zeta,...,zeta^(K-2) for prime K.
    degree = K - 1
    lattice_columns: list[list[int]] = []
    for generator in generators:
        for power in range(degree):
            value = reduce_cyclotomic(generator * X**power, K)
            poly = sp.Poly(value, X, domain=sp.ZZ)
            lattice_columns.append([int(poly.nth(j)) for j in range(degree)])

    lattice = sp.Matrix(
        degree,
        len(lattice_columns),
        lambda row, col: lattice_columns[col][row],
    )
    hnf = hermite_normal_form(lattice)
    assert hnf.shape == (degree, degree)
    return abs(int(hnf.det()))


def unordered_ratio_classes(K: int) -> list[int]:
    seen: set[int] = set()
    reps: list[int] = []
    for r in range(2, K):
        if r in seen:
            continue
        inverse = pow(r, -1, K)
        seen.add(r)
        seen.add(inverse)
        reps.append(min(r, inverse))
    return reps


def check_small_ideal_norms() -> None:
    expected = {
        (7, 2): 7**7,
        (11, 2): 11**39,
        (11, 3): 11**39,
        (11, 5): 11**39,
        (11, 7): 11**41,
        (11, 10): 2**30 * 11**39,
    }
    for key, target in expected.items():
        observed = projective_ideal_norm(*key)
        assert observed == target, (key, observed, target)
        print(f"projective ideal norm {key}: {observed}")

    assert unordered_ratio_classes(11) == [2, 3, 5, 7, 10]
    print("exact K=11 projective order-three split support: empty")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--extended", action="store_true")
    parser.add_argument("--ideal-norm-small", action="store_true")
    args = parser.parse_args()

    for K in (7, 11, 13, 17, 23):
        check_universal_ode(K)

    check_universal_rows(199, 11)
    check_universal_rows(461, 23)

    # Negative control: coarse fixed-degree subresultants retain 23 for r=7,
    # but projectively the true order-three intersection support is absent.
    check_projective_design(23, 11, 7, 1)

    # Positive control: a genuine three-intersection split reduction.
    check_projective_design(103, 17, 10, 3)

    if args.extended:
        check_projective_design(47, 23, 18, 5)
        check_projective_design(139, 23, 18, 3)

    if args.ideal_norm_small:
        check_small_ideal_norms()

    print("cayley projective Bezout row regression: OK")


if __name__ == "__main__":
    main()
