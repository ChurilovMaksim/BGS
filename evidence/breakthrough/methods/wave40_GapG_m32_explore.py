"""Wave 40, task 1: explore nu=(1,0) points at m=32 to find the invariant
behind Gap G (odd sub-multiset O never Q/2-symmetric)."""
import math
import sys
from collections import Counter

import numpy as np
import sympy as sp
from wave36_2part import snf_kernel_i32

m, q = 32, 8192
half = q // 2
pts = snf_kernel_i32(m, q)
print("points:", len(pts))


def period_of_row(y):
    for p in range(1, m + 1):
        if m % p == 0 and all(y[i] == y[i % p] for i in range(m)):
            return p
    return m


nu10 = []
for i in range(len(pts)):
    y = pts[i].astype(np.int64)
    p = period_of_row(y)
    if p < 8:
        continue
    d0 = int(y[p // 2] - y[0]) % q
    d1 = int(y[p // 2 + 1] - y[1]) % q
    if d0 % half or d1 % half:
        continue
    nu = ((d0 // half) % 2, (d1 // half) % 2)
    if nu == (1, 0):
        nu10.append((y, p))

print("nu=(1,0) points:", len(nu10))
print("by period:", Counter(p for _, p in nu10))

# For each nu=(1,0) point: odd subsequence over one period, its cycle,
# top-bit count, and whether O is Q/2-symmetric.
sym = 0
feat = Counter()
examples = []
for y, p in nu10:
    odd = [int(y[i]) for i in range(1, p, 2)]  # p/2 entries
    O = Counter(odd)
    Osym = all(O[(v + half) % q] == O[v] for v in O)
    if Osym:
        sym += 1
    # w-cycle: odd subsequence as a cycle under step 2 in i (k-index)
    w = [int(y[2 * k + 1]) for k in range(p // 2)]
    # minimal period of w-cycle
    L = p // 2
    for d in range(1, p // 2 + 1):
        if (p // 2) % d == 0 and all(w[k] == w[k % d] for k in range(p // 2)):
            L = d
            break
    wcycle = w[:L]
    ntop = sum(1 for v in wcycle if v >= half)
    feat[("L", L, "ntop", ntop)] += 1
    feat[("w0mod2", wcycle[0] % 2)] += 1
    # residues of w-cycle mod 8, mod 16: is the set closed under +half?
    for mod in (8, 16, 32, 64, 128, 256, 512, 1024, 2048):
        s = set(v % mod for v in wcycle)
        # +half mod mod: half % mod
        closed = all((v + half) % mod in s for v in s)
        feat[("mod", mod, "closed", closed)] += 1
    if len(examples) < 8:
        examples.append((p, L, wcycle, ntop))
print("symmetric O count:", sym)
print("features (L, ntop):", sorted((k, v) for k, v in feat.items() if k[0] == "L"))
for mod in (8, 16, 32, 64, 128, 256, 512, 1024, 2048):
    print("mod", mod, "closed=True count:",
          feat[("mod", mod, "closed", True)], "closed=False count:",
          feat[("mod", mod, "closed", False)])
print("w0 parity:", feat[("w0mod2", 0)], feat[("w0mod2", 1)])
for e in examples:
    print("ex p,L,wcycle,ntop:", e)
