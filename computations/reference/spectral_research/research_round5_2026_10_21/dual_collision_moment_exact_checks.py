"""Finite exact checks for the collision-moment phase-cancellation probe."""

from fractions import Fraction as F
from itertools import product
from math import comb, prod


def rank_checks():
    checked = 0
    for n in range(3, 61):
        for k in range(1, (n-1)//2 + 1):
            for d in range(1, n):
                parent = list(range(n))
                def find(a):
                    while a != parent[a]:
                        parent[a] = parent[parent[a]]
                        a = parent[a]
                    return a
                for u in range(k):
                    a, b = find(u), find((u+d) % n)
                    parent[a] = b
                rank = n-len({find(a) for a in range(n)})
                assert rank == k, (n, k, d, rank)
                checked += 1
    return checked


def multiply(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def matrix_power(a, n):
    out = [[F(i == j) for j in range(len(a))] for i in range(len(a))]
    for _ in range(n):
        out = multiply(out, a)
    return out


def constrained_contraction_check():
    # Rational nonflat orthogonal U, with exact C=32/25 and op(P-J)=7/25.
    u = [[F(3, 5), F(-4, 5)], [F(-4, 5), F(-3, 5)]]
    assert multiply(u, u) == [[1, 0], [0, 1]]
    p = [[x*x for x in row] for row in u]
    p3, p4 = matrix_power(p, 3), matrix_power(p, 4)
    r = 4
    sigma = (3, 0, 1, 2)
    full = centered = F(0)
    checked = 0
    # Each arc has four internal edges. Its first internal vertex is
    # constrained to agree between arcs 0 and 2, so s=2 and h=1.
    for starts in product(range(2), repeat=r):
        if not all(starts[sigma[i]] != starts[(i+1) % r] for i in range(r)):
            continue
        for shared in range(2):
            for ends in product(range(2), repeat=r):
                term_full = term_centered = F(1)
                for i, a in enumerate(ends):
                    connector = u[a][starts[(i+1) % r]] * u[a][starts[sigma[i]]]
                    if i in (0, 2):
                        internal = p[starts[i]][shared] * p3[shared][a]
                        term_full *= internal * connector
                        term_centered *= internal * connector
                    else:
                        term_full *= p4[starts[i]][a] * connector
                        term_centered *= (p4[starts[i]][a]-F(1, 2)) * connector
                full += term_full
                centered += term_centered
                checked += 1
    assert full == centered and full != 0
    c = F(32, 25)
    delta = (c-1)/4
    bound = c**2 * (c/2) * delta**2
    assert abs(full) <= bound
    return checked, str(full), str(bound)


def signed_measure_checks():
    checked = 0
    for h in range(1, 31):
        for degree in range(h):
            total = sum((-1)**q * comb(h, q) * q**degree
                        for q in range(h+1))
            assert total == 0
            checked += 1
        assert sum(comb(h, q) for q in range(h+1)) == 2**h
        assert (-1)**0 * comb(h, 0) == 1
    return checked


if __name__ == "__main__":
    print("Exact rank-K repeated-block constraints:", rank_checks())
    print("Constrained contraction: terms / nonzero value / bound:",
          constrained_contraction_check())
    print("Vanishing signed moments with unit zero-atom:", signed_measure_checks())
    print("All exact finite collision-probe checks passed.")
