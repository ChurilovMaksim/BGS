#!/usr/bin/env python3
"""Wave 41, task 3: census of E_alt for split points at m = 32, 64, 128.

Setup (waves 38/39): level j >= 3, m = 2^j, Q = 2^(2j+3), N = 2^j.
y kernel sequence mod Q (N-periodic, y_{i+1} = 6 y_i - y_{i-1}),
minimal period p (8 <= p | N). Fiber = sequences sharing the same
multiset; split = fiber contains > 1 Gamma-orbit (Gamma = dihedral:
shifts + reversal). A = sum_{i<p} (-1)^i y_i (canonical reps);
E_alt := 8*A/Q (claimed integer). Reversal exclusion needs, for split
points, E_alt != p; |E_alt| < 8 suffices since p >= 8.
"""
import sys
from math import gcd


def mat_pow_mod(M, n, Q):
    # 2x2 matrix power mod Q
    a, b, c, d = 1, 0, 0, 1
    x, y, z, w = M
    while n:
        if n & 1:
            a, b, c, d = (a * x + b * z) % Q, (a * y + b * w) % Q, \
                         (c * x + d * z) % Q, (c * y + d * w) % Q
        x, y, z, w = (x * x + y * z) % Q, (x * y + y * w) % Q, \
                     (z * x + w * z) % Q, (z * y + w * w) % Q
        n >>= 1
    return (a, b, c, d)


def kernel_seeds(N, Q):
    """All (y0, y1) mod Q with (M^N - I) s = 0, via linear congruences."""
    a, b, c, d = mat_pow_mod((6, Q - 1, 1, 0), N, Q)
    A11, A12 = (a - 1) % Q, b
    A21, A22 = c, (d - 1) % Q
    seeds = []
    g = gcd(A11, Q)
    step = Q // g
    for y0 in range(Q):
        rhs = (-A12 * y0) % Q
        if rhs % g:
            continue
        # solve A11 * y1 = rhs mod Q
        gg = g
        a_red, rhs_red, mod_red = A11 // gg, rhs // gg, Q // gg
        inv = pow(a_red, -1, mod_red)
        y1_0 = (inv * rhs_red) % mod_red
        for t in range(gg):
            y1 = y1_0 + t * mod_red
            if (A21 * y1 + A22 * y0) % Q == 0:
                seeds.append((y0, y1))
    return seeds


def build_seq(y0, y1, N, Q):
    seq = [0] * N
    seq[0] = y0
    if N > 1:
        seq[1] = y1
    for i in range(1, N - 1):
        seq[i + 1] = (6 * seq[i] - seq[i - 1]) % Q
    return tuple(seq)


def min_period(seq, N):
    p = N
    k = 1
    while k <= N:
        if N % k == 0:
            ok = True
            for i in range(N):
                if seq[i] != seq[i % k]:
                    ok = False
                    break
            if ok:
                return k
        k *= 2
    return N


def orbit_count(members):
    """Number of dihedral orbits among tuples in members (same length N)."""
    rem = set(members)
    n_orb = 0
    while rem:
        s = rem.pop()
        N = len(s)
        rev = s[:1] + s[:0:-1]
        orb = set()
        for k in range(N):
            orb.add(s[k:] + s[:k])
            orb.add(rev[k:] + rev[:k])
        rem -= orb
        n_orb += 1
    return n_orb


def analyze(j):
    m = 2 ** j
    N = m
    Q = 2 ** (2 * j + 3)
    seeds = kernel_seeds(N, Q)
    print(f"m={m} Q={Q} N={N} kernel points={len(seeds)}", flush=True)
    fibers = {}
    for (y0, y1) in seeds:
        s = build_seq(y0, y1, N, Q)
        fibers.setdefault(tuple(sorted(s)), []).append(s)
    print(f"m={m} fibers={len(fibers)}", flush=True)
    split_max = {}   # p -> max |E_alt| over split points
    split_count = {}
    nonsplit_max = {}
    bad = []         # split points with |E_alt| >= 8
    nonint = []      # points where 8A not divisible by Q
    n_split_fibers = 0
    for key, members in fibers.items():
        n_orb = orbit_count(members)
        if n_orb <= 1:
            for s in members:
                p = min_period(s, N)
                A = sum((-1) ** i * s[i] for i in range(p))
                if (8 * A) % Q:
                    nonint.append((s[:4], p))
                else:
                    e = 8 * A // Q
                    nonsplit_max[p] = max(nonsplit_max.get(p, 0), abs(e))
            continue
        n_split_fibers += 1
        for s in members:
            p = min_period(s, N)
            A = sum((-1) ** i * s[i] for i in range(p))
            if (8 * A) % Q:
                nonint.append((s[:4], p))
                continue
            e = 8 * A // Q
            split_max[p] = max(split_max.get(p, 0), abs(e))
            split_count[p] = split_count.get(p, 0) + 1
            if abs(e) >= 8:
                bad.append((p, e, s[:8]))
    print(f"m={m} split fibers={n_split_fibers}")
    print(f"m={m} split |E_alt| max by p: {dict(sorted(split_max.items()))}")
    print(f"m={m} split point counts by p: {dict(sorted(split_count.items()))}")
    print(f"m={m} nonsplit |E_alt| max by p: {dict(sorted(nonsplit_max.items()))}")
    print(f"m={m} split points with |E_alt|>=8: {len(bad)}")
    for b in bad[:20]:
        print("  BAD", b)
    print(f"m={m} points with 8A not divisible by Q: {len(nonint)}")
    for b in nonint[:10]:
        print("  NONINT", b)
    return bad


if __name__ == "__main__":
    levels = [int(x) for x in sys.argv[1:]] or [5, 6, 7]
    all_bad = []
    for j in levels:
        all_bad += analyze(j)
    print("TOTAL split violations:", len(all_bad))
