#!/usr/bin/env python3
"""
Finite regression for Frobenius amplification of non-forced Cayley collisions.

Two independent exact implementations are compared:
  1. direct arithmetic in F_{p^f}, f = ord_K(p);
  2. collision-polynomial divisibility by one irreducible factor of Phi_K mod p.

This is a finite regression only. The growing-parameter theorem is proved in
mathematics/cayley_frobenius_amplification.md.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from collections import Counter
from itertools import product
from math import gcd
import warnings

import sympy as sp
from sympy.polys.domains import ZZ
from sympy.polys.galoistools import gf_irreducible
from sympy.utilities.exceptions import SymPyDeprecationWarning

warnings.filterwarnings("ignore", category=SymPyDeprecationWarning)

X = sp.symbols("X")


def ord_mod(a: int, n: int) -> int:
    assert gcd(a, n) == 1
    x = 1
    for f in range(1, n + 1):
        x = x * a % n
        if x == 1:
            return f
    raise AssertionError("multiplicative order not found")


class Fq:
    """Tiny exact polynomial-basis finite field, only for regression sizes."""

    def __init__(self, p: int, coeffs, modpoly):
        self.p = p
        self.mod = tuple(int(c) % p for c in modpoly)  # high-to-low, monic
        self.f = len(self.mod) - 1
        cc = list(coeffs) + [0] * self.f
        self.c = tuple(int(x) % p for x in cc[: self.f])  # low-to-high

    def __hash__(self):
        return hash((self.p, self.mod, self.c))

    def __eq__(self, other):
        return (
            isinstance(other, Fq)
            and (self.p, self.mod, self.c) == (other.p, other.mod, other.c)
        )

    def from_int(self, n: int) -> "Fq":
        return Fq(self.p, [n], self.mod)

    def __add__(self, other):
        if isinstance(other, int):
            other = self.from_int(other)
        return Fq(
            self.p, [(a + b) % self.p for a, b in zip(self.c, other.c)], self.mod
        )

    __radd__ = __add__

    def __neg__(self):
        return Fq(self.p, [(-a) % self.p for a in self.c], self.mod)

    def __sub__(self, other):
        if isinstance(other, int):
            other = self.from_int(other)
        return self + (-other)

    def __rsub__(self, other):
        return self.from_int(other) - self

    def __mul__(self, other):
        if isinstance(other, int):
            other = self.from_int(other)
        f, p = self.f, self.p
        tmp = [0] * (2 * f - 1)
        for i, a in enumerate(self.c):
            for j, b in enumerate(other.c):
                tmp[i + j] = (tmp[i + j] + a * b) % p
        ml = list(reversed(self.mod))
        for deg in range(2 * f - 2, f - 1, -1):
            coef = tmp[deg] % p
            if coef:
                for j in range(f):
                    tmp[deg - f + j] = (tmp[deg - f + j] - coef * ml[j]) % p
        return Fq(p, tmp[:f], self.mod)

    __rmul__ = __mul__

    def __pow__(self, n: int):
        assert n >= 0
        r = self.from_int(1)
        a = self
        while n:
            if n & 1:
                r = r * a
            a = a * a
            n //= 2
        return r

    def inv(self):
        if all(x == 0 for x in self.c):
            raise ZeroDivisionError
        return self ** (self.p**self.f - 2)

    def __truediv__(self, other):
        if isinstance(other, int):
            other = self.from_int(other)
        return self * other.inv()


def find_order_k_root(p: int, K: int):
    f = ord_mod(p, K)
    modpoly = list(gf_irreducible(f, p, ZZ))
    zero = Fq(p, [0], modpoly)
    one = zero.from_int(1)
    exponent = (p**f - 1) // K
    for idx in range(1, p**f):
        t, coeffs = idx, []
        for _ in range(f):
            coeffs.append(t % p)
            t //= p
        h = Fq(p, coeffs, modpoly) ** exponent
        if h != one and h**K == one:
            return h, f
    raise AssertionError("failed to find K-th root")


def direct_extension_delta(K: int, p: int):
    h, f = find_order_k_root(p, K)
    zero = h.from_int(0)
    cayley = {}
    for i in range(1, K):
        z = h**i
        cayley[i] = (z + 1) / (z - 1)

    bins = {}
    counts = Counter()
    for i, j in product(range(1, K), repeat=2):
        d = cayley[i] - cayley[j]
        counts[d] += 1
        if i != j:
            bins.setdefault(d, []).append((i, j))

    e_nonzero = sum(v * v for d, v in counts.items() if d != zero)
    baseline = (K - 1) * (2 * K - 5)
    delta = e_nonzero - baseline

    nonforced = []
    for pairs in bins.values():
        for (i, j), (r, s) in product(pairs, repeat=2):
            forced = (r == i and s == j) or ((r + j) % K == 0 and (s + i) % K == 0)
            if not forced:
                nonforced.append((i, j, r, s))

    assert len(nonforced) == delta

    # Frobenius scaling q -> p q modulo K. Every non-forced orbit must have f terms.
    unseen = set(nonforced)
    orbit_sizes = []
    while unseen:
        q = next(iter(unseen))
        orbit = []
        cur = q
        while cur not in orbit:
            orbit.append(cur)
            cur = tuple((p * x) % K for x in cur)
        for item in orbit:
            unseen.remove(item)
        orbit_sizes.append(len(orbit))

    assert all(size == f for size in orbit_sizes)
    assert delta % f == 0
    return f, delta, tuple(sorted(orbit_sizes))


def factor_delta(K: int, p: int):
    """Independent collision-polynomial test, using sparse modular remainders."""
    phi = sp.cyclotomic_poly(K, X, polys=True)
    _, factors = sp.factor_list(phi, modulus=p)
    g = factors[0][0]
    f = g.degree()
    assert f == ord_mod(p, K)
    assert all(poly.degree() == f and mult == 1 for poly, mult in factors)

    # Precompute X^e mod g as coefficient vectors, low degree first.
    gc = [int(c) % p for c in reversed(g.all_coeffs())][:-1]
    powers = []
    v = [0] * f
    v[0] = 1
    powers.append(tuple(v))
    for _ in range(3 * K + 1):
        top = v[-1]
        w = [0] + v[:-1]
        if top:
            for j in range(f):
                w[j] = (w[j] - top * gc[j]) % p
        v = w
        powers.append(tuple(v))

    def is_collision(i, j, r, s):
        terms = (
            (1, r + s + i),
            (-1, r + s + j),
            (-1, r + i + j),
            (2, r + j),
            (-1, r),
            (1, s + i + j),
            (-2, s + i),
            (1, s),
            (1, i),
            (-1, j),
        )
        rem = [0] * f
        for coeff, exponent in terms:
            pw = powers[exponent]
            for a in range(f):
                rem[a] = (rem[a] + coeff * pw[a]) % p
        return not any(rem)

    delta = 0
    for i, j, r, s in product(range(1, K), repeat=4):
        if i == j or r == s:
            continue
        forced = (r == i and s == j) or ((r + j) % K == 0 and (s + i) % K == 0)
        if not forced and is_collision(i, j, r, s):
            delta += 1
    return f, delta


CASES = {
    (7, 13): (2, 32),
    (11, 43): (2, 128),
    (13, 3): (3, 432),
    (13, 5): (4, 496),
}


def main():
    for (K, p), expected in CASES.items():
        f1, d1, orbit_sizes = direct_extension_delta(K, p)
        f2, d2 = factor_delta(K, p)
        assert (f1, d1) == expected
        assert (f2, d2) == expected
        print(
            f"K={K:2d} p={p:2d} f={f1} delta={d1:3d} "
            f"orbits={len(orbit_sizes):3d} all_orbit_size={f1}"
        )

    # For K=7, the universal resultant cutoff is < 94.
    # Exhaust all odd p != 7 below 94 with the independent factor method.
    bad = []
    for p in sp.primerange(3, 94):
        if p == 7:
            continue
        f, delta = factor_delta(7, int(p))
        if delta:
            bad.append((int(p), f, delta))
    assert bad == [(13, 2, 32)]
    print("K=7 complete p<94 bad list:", bad)


if __name__ == "__main__":
    main()
