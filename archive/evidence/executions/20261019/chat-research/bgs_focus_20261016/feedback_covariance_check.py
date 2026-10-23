#!/usr/bin/env python3
"""Exact finite controls. No asymptotic or physical-BGS certification."""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import permutations
from math import factorial
import json
import platform
import sys


@dataclass(frozen=True)
class Q:
    x: F = F(0)
    y: F = F(0)

    def __add__(self, other):
        other = coerce(other)
        return Q(self.x + other.x, self.y + other.y)

    __radd__ = __add__

    def __neg__(self):
        return Q(-self.x, -self.y)

    def __sub__(self, other):
        return self + (-coerce(other))

    def __rsub__(self, other):
        return coerce(other) - self

    def __mul__(self, other):
        other = coerce(other)
        return Q(self.x * other.x - self.y * other.y,
                 self.x * other.y + self.y * other.x)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = coerce(other)
        return self * other.conj() * Q(1 / other.abs2())

    def conj(self):
        return Q(self.x, -self.y)

    def abs2(self):
        return self.x * self.x + self.y * self.y


def coerce(z):
    return z if isinstance(z, Q) else Q(F(z))


def eye(n):
    return [[Q(F(i == j)) for j in range(n)] for i in range(n)]


def adj(a):
    return [[z.conj() for z in col] for col in zip(*a)]


def mul(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)]
            for row in a]


def rational_unitary(n):
    s = eye(n)
    phases = (Q(F(3, 5), F(4, 5)), Q(F(5, 13), F(12, 13)),
              Q(F(-8, 17), F(15, 17)))
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            z = phases[count % len(phases)]
            g = eye(n)
            g[i][i] = g[j][j] = Q(F(3, 5))
            g[i][j] = F(4, 5) * z
            g[j][i] = -F(4, 5) * z.conj()
            s = mul(g, s)
            count += 1
    return s


def kernel(s):
    n = len(s)
    return [[sum(s[i][e] * s[e][j] * (s[k][e] * s[e][l]).conj()
                 for e in range(n))
             for k in range(n) for l in range(n)]
            for i in range(n) for j in range(n)]


def check_matrix(n):
    s = rational_unitary(n)
    assert mul(s, adj(s)) == eye(n)
    assert mul(adj(s), s) == eye(n)
    c = kernel(s)
    assert adj(c) == c
    assert mul(c, c) == c
    assert sum(c[i][i] for i in range(n * n)) == Q(F(n))
    assert sum(z.abs2() for row in c for z in row) == F(n)
    p = [[z.abs2() for z in row] for row in s]
    p2 = [[sum(p[i][e] * p[e][j] for e in range(n))
           for j in range(n)] for i in range(n)]
    b = [[s[i][j] * s[j][i].conj() for j in range(n)] for i in range(n)]
    h = [[s[i][j] * s[j][i] for j in range(n)] for i in range(n)]
    b2, hh = mul(b, b), mul(h, adj(h))
    for i in range(n):
        for j in range(n):
            assert c[i * n + j][i * n + j] == Q(p2[i][j])
            assert c[i * n + j][j * n + i] == b2[i][j]
            assert c[i * n + i][j * n + j] == hh[i][j]
    # Independent construction from orthonormal tensor-column vectors.
    a = [[s[i][e] * s[e][j] for e in range(n)]
         for i in range(n) for j in range(n)]
    assert mul(adj(a), a) == eye(n)
    assert mul(a, adj(a)) == c
    phases = (Q(F(1)), Q(F(-1)), Q(F(0), F(1)), Q(F(0), F(-1)),
              Q(F(3, 5), F(4, 5)), Q(F(3, 5), F(-4, 5)))
    count = 0
    for e in range(n):
        keep = [i for i in range(n) if i != e]
        for w in phases:
            q = w / (1 - s[e][e] * w)
            t = [[s[i][j] + q * s[i][e] * s[e][j]
                  for j in keep] for i in keep]
            assert mul(t, adj(t)) == eye(n - 1)
            count += 1
    # Mutation control: replacing coherent covariance by intensity products fails.
    intensity_fake = [[Q(sum(p[i][e] * p[e][j] * p[k][e] * p[e][l]
                            for e in range(n)))
                       for k in range(n) for l in range(n)]
                      for i in range(n) for j in range(n)]
    assert intensity_fake != c
    return {"n": n, "unitary_cases": 1, "feedback_cases": count,
            "projector_rank": n, "arithmetic": "Q(i), exact Fractions",
            "intensity_replacement_rejected": True}


def falling(n, k):
    return factorial(n) // factorial(n - k)


def mark_checks():
    cases, prefixes, compatible_tuples = 0, 0, 0
    for n in range(3, 8):
        for u in range(2, n + 1):
            for marks in range(1, min(4, u) + 1):
                target = F(1, falling(n, n - u))
                joint_weight = F(1, falling(n, marks) * falling(n - marks, n - u))
                prefix_count = 0
                for deleted in permutations(range(n), n - u):
                    survivors = tuple(i for i in range(n) if i not in deleted)
                    tuples = tuple(permutations(survivors, marks))
                    assert len(tuples) == falling(u, marks)
                    assert len(set(tuples)) == len(tuples)
                    assert joint_weight * len(tuples) == target
                    for labels in tuples:
                        assert not set(labels).intersection(deleted)
                    compatible_tuples += len(tuples)
                    prefix_count += 1
                assert prefix_count == falling(n, n - u)
                assert prefix_count * target == 1
                prefixes += prefix_count
                cases += 1
    return {"cases": cases, "prefixes": prefixes,
            "compatible_ordered_mark_tuples": compatible_tuples,
            "n_range": [3, 7], "mark_range": [1, 4],
            "u_range": "2..N, marks<=u", "arithmetic": "Q, exact Fractions"}


def main():
    result = {"status": "passed", "python": platform.python_version(),
              "matrices": [check_matrix(n) for n in range(2, 6)],
              "marks": mark_checks(),
              "non_claims": ["Not an asymptotic Gaussian theorem certificate.",
                             "Not a check of upstream trajectory inequalities.",
                             "No fixed-operator BGS conclusion."]}
    out = sys.argv[1]
    with open(out, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
        f.write("\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
