#!/usr/bin/env python3
"""Wave 41, task 3 (part 2): E_alt distribution by nu, and reduction data.

For each kernel point: minimal period p, nu from the half-period defect
y_{i+p/2} - y_i = (Q/2) * nu_{i mod 2} (nu in (Z/2)^2), E_alt = 8A/Q,
splitness (fiber orbit count > 1). Also: v2(gcd of entries of M^p - I)
and the exact 2-adic divisibility of period-p points (reduction scale).
"""
import sys
from math import gcd
from collections import Counter
from wave41_reversal_census import kernel_seeds, build_seq, min_period, orbit_count


def nu_of(seq, p, Q):
    half = Q // 2
    nu = []
    for r in (0, 1):
        d = (seq[r + p // 2] - seq[r]) % Q
        if d == 0:
            nu.append(0)
        elif d == half:
            nu.append(1)
        else:
            return None
    return tuple(nu)


def mat_int_pow(M, n):
    a, b, c, d = 1, 0, 0, 1
    x, y, z, w = M
    while n:
        if n & 1:
            a, b, c, d = a * x + b * z, a * y + b * w, c * x + d * z, c * y + d * w
        x, y, z, w = x * x + y * z, x * y + y * w, z * x + w * z, z * y + w * w
        n >>= 1
    return (a, b, c, d)


def v2(n):
    n = abs(n)
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def analyze(j):
    m = 2 ** j
    N = m
    Q = 2 ** (2 * j + 3)
    seeds = kernel_seeds(N, Q)
    fibers = {}
    for (y0, y1) in seeds:
        s = build_seq(y0, y1, N, Q)
        fibers.setdefault(tuple(sorted(s)), []).append(s)
    dist = {}   # (p, nu) -> Counter of E_alt
    split_by_nu = Counter()
    div_by_p = {}  # p -> min v2 over all y_i over points of period p
    for key, members in fibers.items():
        n_orb = orbit_count(members)
        split = n_orb > 1
        for s in members:
            p = min_period(s, N)
            if p < 8:
                continue
            nu = nu_of(s, p, Q)
            A = sum((-1) ** i * s[i] for i in range(p))
            assert (8 * A) % Q == 0
            e = 8 * A // Q
            dist.setdefault((p, nu), Counter())[e] += 1
            if split:
                split_by_nu[(p, nu)] += 1
            dv = min(v2(v) if v != 0 else 99 for v in s)
            div_by_p[p] = min(div_by_p.get(p, 99), dv)
    print(f"=== m={m} ===")
    for (p, nu) in sorted(dist, key=lambda t: (t[0], str(t[1]))):
        c = dist[(p, nu)]
        print(f"  p={p} nu={nu} E_alt values: {dict(sorted(c.items()))} "
              f"split_pts={split_by_nu.get((p, nu), 0)} total={sum(c.values())}")
    print(f"  min v2 of entries by period p: {div_by_p}  (2j+3={2*j+3})")


if __name__ == "__main__":
    for p in (8, 16, 32, 64, 128):
        a, b, c, d = mat_int_pow((6, -1, 1, 0), p)
        a1, b1, c1, d1 = a - 1, b, c, d - 1
        g = gcd(gcd(a1, b1), gcd(c1, d1))
        det = a1 * d1 - b1 * c1
        print(f"p={p}: v2(gcd entries of M^p-I)={v2(g)}  v2(det)={v2(det)}  "
              f"K_p = v2(det)-v2(gcd)={v2(det)-v2(g)}")
    levels = [int(x) for x in sys.argv[1:]] or [5, 6, 7]
    for j in levels:
        analyze(j)
