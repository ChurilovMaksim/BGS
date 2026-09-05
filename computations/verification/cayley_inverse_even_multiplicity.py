#!/usr/bin/env python3
"""Exact regression for cayley_inverse_even_multiplicity_localization.md.

Finite controls only.  The universal statements are proved in the mathematics
note.

Checks:
  * inverse zero edges form a matching and I_-1=2*d on split anchors;
  * all odd elementary symmetric functions vanish on 2d opposite endpoints;
  * deg gcd(E,O)=d for F(X)=E(X^2)+X O(X^2);
  * direct translated-resultant order equals d for K=29 and K=43;
  * exhaustive six-subset equivalence at K=29,p=59.
"""
from __future__ import annotations

from itertools import combinations
import sympy as sp

X, Y, Z = sp.symbols("X Y Z")


def primitive_k_root(K: int, p: int) -> int:
    assert sp.isprime(K) and sp.isprime(p) and p % K == 1
    g = int(sp.primitive_root(p))
    h = pow(g, (p - 1) // K, p)
    assert h != 1 and pow(h, K, p) == 1
    return h


def centered_values(K: int, p: int, h: int) -> dict[int, int]:
    m = (K - 1) // 2
    powers = [1] * K
    for a in range(1, K):
        powers[a] = powers[a - 1] * h % p

    trace = [0] * (m + 1)
    trace[0] = 2 % p
    for a in range(1, m + 1):
        trace[a] = (powers[a] + powers[K - a]) % p

    assert len(set(trace)) == len(trace)
    tau = trace[1]
    values = {
        a: (trace[a] - tau) % p
        for a in range(m + 1)
        if a != 1
    }
    assert 0 not in values.values()
    assert len(set(values.values())) == len(values)
    return values


def zero_edges(values: dict[int, int], p: int) -> list[tuple[int, int]]:
    inverse = {x: a for a, x in values.items()}
    out: list[tuple[int, int]] = []
    for a, x in values.items():
        b = inverse.get((-x) % p)
        if b is not None and a < b:
            out.append((a, b))
    return sorted(out)


def maximal_embedding(
    K: int, p: int
) -> tuple[int, int, dict[int, int], list[tuple[int, int]]]:
    h0 = primitive_k_root(K, p)
    m = (K - 1) // 2
    best: tuple[int, int, dict[int, int], list[tuple[int, int]]] | None = None
    for j in range(1, m + 1):
        values = centered_values(K, p, pow(h0, j, p))
        edges = zero_edges(values, p)
        candidate = (len(edges), j, values, edges)
        if best is None or candidate[0] > best[0]:
            best = candidate
    assert best is not None
    return best


def elementary_symmetric(values: list[int], p: int) -> list[int]:
    """Return [e_0,...,e_n] modulo p."""
    e = [1]
    for x in values:
        new = [0] * (len(e) + 1)
        for j, value in enumerate(e):
            new[j] = (new[j] + value) % p
            new[j + 1] = (new[j + 1] + value * x) % p
        e = new
    return e


def endpoint_values(
    values: dict[int, int], edges: list[tuple[int, int]]
) -> list[int]:
    vertices: list[int] = []
    seen: set[int] = set()
    for a, b in edges:
        assert a not in seen and b not in seen
        seen.add(a)
        seen.add(b)
        vertices.extend([values[a], values[b]])
    return vertices


def centered_polynomial(values: dict[int, int], p: int) -> sp.Poly:
    F = sp.Poly(1, X, modulus=p)
    for x in values.values():
        F *= sp.Poly(X - x, X, modulus=p)
    assert F.degree() == len(values)
    return F


def parity_gcd_degree(values: dict[int, int], p: int) -> int:
    F = centered_polynomial(values, p)
    E_expr = sp.Integer(0)
    O_expr = sp.Integer(0)
    for (degree,), coefficient in F.terms():
        c = int(coefficient) % p
        if degree % 2 == 0:
            E_expr += c * Y ** (degree // 2)
        else:
            O_expr += c * Y ** ((degree - 1) // 2)
    E = sp.Poly(E_expr, Y, modulus=p)
    O = sp.Poly(O_expr, Y, modulus=p)
    return sp.gcd(E, O).degree()


def translated_resultant_order(values: dict[int, int], p: int) -> int:
    """Compute ord_(Z=0) Res_Y(E_Z,O_Z) directly over F_p."""
    F = centered_polynomial(values, p)
    inv2 = pow(2, -1, p)
    shifted = sp.Poly(
        sp.expand(F.as_expr().subs(X, X + inv2 * Z)),
        X,
        Z,
        modulus=p,
    )

    E_expr = sp.Integer(0)
    O_expr = sp.Integer(0)
    for (x_degree, z_degree), coefficient in shifted.terms():
        c = int(coefficient) % p
        term = c * Z**z_degree
        if x_degree % 2 == 0:
            E_expr += term * Y ** (x_degree // 2)
        else:
            O_expr += term * Y ** ((x_degree - 1) // 2)

    resultant = sp.Poly(
        sp.resultant(E_expr, O_expr, Y),
        Z,
        modulus=p,
    )
    for degree in range(resultant.degree() + 1):
        if int(resultant.nth(degree)) % p != 0:
            return degree
    raise RuntimeError("translated resultant vanished identically")


def check_anchor(K: int, p: int, expected_d: int, check_rho: bool) -> None:
    d, embedding, values, edges = maximal_embedding(K, p)
    assert d == expected_d, (K, p, d, expected_d)

    endpoints = endpoint_values(values, edges)
    assert len(endpoints) == 2 * d
    odd = elementary_symmetric(endpoints, p)
    assert all(odd[j] % p == 0 for j in range(1, 2 * d, 2))

    gcd_degree = parity_gcd_degree(values, p)
    assert gcd_degree == d, (K, p, gcd_degree, d)

    rho_order: int | None = None
    if check_rho:
        rho_order = translated_resultant_order(values, p)
        assert rho_order == d, (K, p, rho_order, d)

    rho_text = f" rho_order={rho_order}" if rho_order is not None else ""
    print(
        f"K={K:3d} p={p:<12d} emb={embedding:2d} "
        f"zero_edges={d} I_inverse={2*d} gcd_degree={gcd_degree}"
        f"{rho_text}: OK"
    )


def exhaustive_k29_six_subsets() -> None:
    K, p = 29, 59
    d, _embedding, values, edges = maximal_embedding(K, p)
    assert d == 3
    items = sorted(values.items())

    good = 0
    for subset in combinations(items, 6):
        xs = [x for _a, x in subset]
        e = elementary_symmetric(xs, p)
        symmetric_certificate = all(e[j] % p == 0 for j in (1, 3, 5))

        xset = set(xs)
        opposite_pairs = sum(1 for x in xs if (-x) % p in xset) // 2
        matching_certificate = opposite_pairs == 3

        assert symmetric_certificate == matching_certificate
        good += int(symmetric_certificate)

    assert good == 1
    expected_vertices = {a for edge in edges for a in edge}
    assert len(expected_vertices) == 6
    print("K=29 p=59 exhaustive 3003 six-subsets: unique e1=e3=e5=0 subset: OK")


def main() -> None:
    check_anchor(29, 59, 3, check_rho=True)
    check_anchor(43, 173, 4, check_rho=True)
    check_anchor(83, 167, 7, check_rho=False)
    check_anchor(89, 179, 8, check_rho=False)
    exhaustive_k29_six_subsets()
    print("cayley inverse even-multiplicity localization regression: OK")


if __name__ == "__main__":
    main()
