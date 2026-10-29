#!/usr/bin/env python3
"""Occupation checks for BGS-TRACE-132.

Floating point. The distance from the dihedral main term 2m P(N,m)/N^m,
and from the rotational main term m P(p,m)/p^m after row inversion.
A pass checks the inequalities in
mathematics/fixed-map/hyperbolic_short_time_limit.md.
It does not prove BGS-TRACE-005 or BGS-BGS-001.

Coverage. Matrices [[3,4],[2,3]], [[2,1],[1,1]] and [[5,2],[2,1]],
times 3 and 4, odd moduli 5 through 15. Inversion on the primes 5, 7 and 11.
Times one and two are compared with the flat-matrix formulae at N=5 and N=7.
"""
from __future__ import annotations

import math
from itertools import product
from math import gcd

import numpy as np

ABS_TOL = 1e-8
PI = float.fromhex("0x1.921fb54442d18p+1")


def quant(s, n, invert=False):
    alpha, beta, _gamma, delta = s
    kappa = (-pow((2 * beta) % n, -1, n)) % n
    pi = {0: 0}
    if invert:
        for x in range(1, n):
            pi[x] = pow(x, -1, n)
    else:
        pi = {x: x for x in range(n)}
    mat = np.zeros((n, n), dtype=np.complex128)
    scale = n**-0.5
    for x in range(n):
        xx = pi[x]
        for y in range(n):
            phase = (kappa * (delta * xx * xx - 2 * xx * y + alpha * y * y)) % n
            mat[x, y] = scale * np.exp(2j * PI * phase / n)
    return mat


def occupation(mat, m):
    n = mat.shape[0]
    buckets = {}
    for word in product(range(n), repeat=m):
        amp = 1 + 0j
        for t in range(m):
            amp *= mat[word[t], word[(t + 1) % m]]
        key = tuple(sorted(word))
        buckets[key] = buckets.get(key, 0j) + amp
    return float(np.real(sum(abs(v) ** 2 for v in buckets.values())))


def falling(n, m):
    out = 1
    for k in range(m):
        out *= n - k
    return out


def main() -> None:
    matrices = [(3, 4, 2, 3), (2, 1, 1, 1), (5, 2, 2, 1)]
    rows = 0
    for s in matrices:
        beta = s[1]
        for n in (5, 7, 9, 11, 15):
            if gcd(beta, n) != 1:
                continue
            mat = quant(s, n)
            for m, closed in ((1, 1.0), (2, (2 * n - 1) / n)):
                if n > 7:
                    continue
                got = occupation(mat, m)
                if abs(got - closed) > 1e-6:
                    raise SystemExit(f"flat {s} {n} {m} {got}")
            for m in (3, 4):
                got = occupation(mat, m)
                main_term = 2 * m * falling(n, m) / n**m
                bound = math.factorial(m) * (1 + m * (m - 1)) / n
                if abs(got - main_term) > bound + ABS_TOL:
                    raise SystemExit(f"haar {s} {n} {m} {got} {main_term} {bound}")
                rows += 1
        for p in (5, 7, 11):
            if gcd(beta, p) != 1:
                continue
            mat = quant(s, p, invert=True)
            if p == 3:
                continue
            for m in (3, 4):
                got = occupation(mat, m)
                main_term = m * falling(p, m) / p**m
                bound = math.factorial(m) * (
                    3**0.25 * p ** (-0.25) + (m * (m - 1) + 2) / p
                )
                if abs(got - main_term) > bound + 1e-6:
                    raise SystemExit(f"inv {s} {p} {m} {got} {bound}")
                rows += 1
    # At p=3 the inversion is the identity for every matrix.
    model = (3, 4, 2, 3)
    plain = occupation(quant(model, 3), 3)
    inv = occupation(quant(model, 3, invert=True), 3)
    if abs(plain - inv) > 1e-8:
        raise SystemExit(f"p=3 inversion {plain} {inv}")
    # Majorant obstruction: N^2 * 11/18 > 6 at N=11.
    if 121 * 11 <= 6 * 18:
        raise SystemExit("majorant")
    print("BGS-TRACE-132 ok")
    print(f"inequality_rows {rows}")
    print(f"p3_time3 {plain:.12f}")


if __name__ == "__main__":
    main()
