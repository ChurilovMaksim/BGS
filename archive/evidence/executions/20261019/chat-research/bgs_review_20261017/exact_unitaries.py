#!/usr/bin/env python3
"""Exact Q(i) matrix helpers copied from the 16 October external checkpoint."""
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

