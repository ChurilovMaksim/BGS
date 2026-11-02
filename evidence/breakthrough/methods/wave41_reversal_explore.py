#!/usr/bin/env python3
"""Wave 41, task 3 (part 3): structure of reduced nu=(1,1) sequences.

Reduced setting: modulus R = 2^(k+3), period p = 2^k. A period-p point
y at level j is y = 2^(2j+3-k-3) * z with z mod R. Print examples of
nu=(1,1) reduced sequences and their entry valuations, plus the
alternating sum and its descent (half/quarter defects).
"""
from math import gcd
from wave41_reversal_census import kernel_seeds, build_seq, min_period


def nu_of(seq, p, Q):
    half = Q // 2
    nu = []
    for r in (0, 1):
        d = (seq[r + p // 2] - seq[r]) % Q
        nu.append(0 if d == 0 else 1 if d == half else -1)
    return tuple(nu)


def v2(n):
    n = abs(n)
    if n == 0:
        return 99
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def reduced_points(j, p_target):
    m = 2 ** j
    N = m
    Q = 2 ** (2 * j + 3)
    k = p_target.bit_length() - 1
    R = 2 ** (k + 3)
    scale = Q // R
    out = []
    for (y0, y1) in kernel_seeds(N, Q):
        s = build_seq(y0, y1, N, Q)
        if min_period(s, N) != p_target:
            continue
        if nu_of(s, p_target, Q) != (1, 1):
            continue
        assert all(v % scale == 0 for v in s)
        z = tuple(v // scale for v in s[:p_target])
        out.append(z)
    return out, R


for p_target, j in ((16, 6), (32, 7)):
    pts, R = reduced_points(j, p_target)
    print(f"p={p_target} R={R} reduced nu=(1,1) points: {len(pts)}")
    for z in pts[:3]:
        print("  z =", z)
        print("  v2 =", [v2(v) for v in z])
        print("  z mod 8 =", [v % 8 for v in z])
        A = sum((-1) ** i * z[i] for i in range(p_target))
        print(f"  A_z={A}  A_z/2^k={A // (p_target)}")
    # valuation profile across all points
    from collections import Counter
    minv = Counter()
    allv = Counter()
    for z in pts:
        minv[min(v2(v) for v in z)] += 1
        for v in z:
            allv[v2(v)] += 1
    print("  min-v2 distribution:", dict(sorted(minv.items())))
    print("  entry-v2 distribution:", dict(sorted(allv.items())))
