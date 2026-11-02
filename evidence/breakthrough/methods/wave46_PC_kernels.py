#!/usr/bin/env python3
"""Wave 46, task 7, step 1: kernels at m=24 other components.

Fix vectors mod q: sequences y with y_{n+2} = 6*y_{n+1} - y_n (mod q)
and y_24 = y_0, y_25 = y_1. Enumerated from (y_0, y_1).
Class profile: 4 sorted multisets of values at i = r (mod 4), i < 24.
D4 class maps: r -> r+b and r -> -r+b (mod 4), 8 maps.
Pi_q(y, y') = {pi : prof'[r] == prof[pi(r)] for all r}.
"""
from collections import Counter

M = 24
T = 4

def kernel(q):
    out = []
    for y0 in range(q):
        for y1 in range(q):
            y = [0] * 26
            y[0], y[1] = y0, y1
            for n in range(24):
                y[n + 2] = (6 * y[n + 1] - y[n]) % q
            if y[24] == y0 and y[25] == y1:
                out.append(tuple(y[:24]))
    return out

def prof(y):
    return tuple(tuple(sorted(y[i] for i in range(24) if i % 4 == r))
                  for r in range(4))

D4 = []
for b in range(4):
    D4.append(tuple((r + b) % 4 for r in range(4)))
    D4.append(tuple((-r + b) % 4 for r in range(4)))
D4 = sorted(set(D4))
assert len(D4) == 8

def pi_set(p, pp):
    # pi with prof'[r] == prof[pi(r)]
    return [pi for pi in D4 if all(pp[r] == p[pi[r]] for r in range(4))]

def orbit_size(B, q):
    # B = (a, b) in R/q, alpha = 3 + 2*sqrt(2); smallest d>0 with B*alpha^d = B
    a, b = B
    # alpha^d via recurrence on (a,b): multiply by (3,2): (3a+4b, 2a+3b)
    ca, cb = a, b
    for d in range(1, 25):
        ca, cb = (3 * ca + 4 * cb) % q, (2 * ca + 3 * cb) % q
        if (ca, cb) == (a, b):
            return d
    return None

def B_of(y, q):
    # odd q only: y0 = 2a, y1 = 6a + 8b
    inv2 = pow(2, -1, q)
    inv8 = pow(8, -1, q)
    a = (y[0] * inv2) % q
    b = ((y[1] - 3 * y[0]) * inv8) % q
    return (a, b)

for q in [25, 49, 81, 121, 289, 512]:
    K = kernel(q)
    profs = [prof(y) for y in K]
    full = sum(1 for p in profs if p[0] == p[1] == p[2] == p[3])
    print(f"q={q}: |ker|={len(K)} full={full} frac={full}/{len(K)}")
    if q % 2 == 1:
        by_d = Counter()
        full_by_d = Counter()
        for y in K:
            d = orbit_size(B_of(y, q), q)
            by_d[d] += 1
            p = prof(y)
            if p[0] == p[1] == p[2] == p[3]:
                full_by_d[d] += 1
        print(f"   orbit sizes: {dict(sorted(by_d.items()))}")
        print(f"   full by d:   {dict(sorted(full_by_d.items()))}")
    # single-component pair Pi statistics
    by_mult = {}
    for idx, y in enumerate(K):
        by_mult.setdefault(tuple(sorted(y)), []).append(idx)
    npairs = 0
    pi_empty = 0
    pi_dist = Counter()
    for idxs in by_mult.values():
        for ii in range(len(idxs)):
            for jj in range(ii + 1, len(idxs)):
                ps = pi_set(profs[idxs[ii]], profs[idxs[jj]])
                npairs += 1
                pi_dist[len(ps)] += 1
                if not ps:
                    pi_empty += 1
    print(f"   pairs with equal multiset: {npairs}, Pi empty: {pi_empty}, "
          f"|Pi| dist: {dict(sorted(pi_dist.items()))}")
