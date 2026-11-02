import numpy as np
ALPHA = (3, 2)
def mul(a, b, M): return ((a[0]*b[0]+2*a[1]*b[1]) % M, (a[0]*b[1]+a[1]*b[0]) % M)
def pw(a, n, M):
    r = (1, 0)
    while n:
        if n & 1: r = mul(r, a, M)
        a = mul(a, a, M); n >>= 1
    return r
ap = [pw(ALPHA, i, 8192) for i in range(32)]
Re = np.array([a[0] for a in ap], dtype=np.int64)
Im = np.array([a[1] for a in ap], dtype=np.int64)
cols = [np.arange(r, 32, 4) for r in range(4)]
pairs = [(r1, r2) for r1 in range(4) for r2 in range(r1+1, 4)]
bad = []  # (x, y) with cross-class p-collision
for x in range(8192):
    y = np.arange(8192, dtype=np.int64)[:, None]
    P = (2*x*Re[None, :] + 4*y*Im[None, :]) % 8192  # (8192, 32)
    mixed = np.zeros(8192, dtype=bool)
    for (r1, r2) in pairs:
        A = P[:, cols[r1]][:, :, None]  # (8192, 8, 1)
        B = P[:, cols[r2]][:, None, :]  # (8192, 1, 8)
        mixed |= (A == B).any(axis=(1, 2))
    for yy in np.nonzero(mixed)[0]:
        bad.append((x, int(yy)))
    if x % 2048 == 0: print(f"  x={x} bad={len(bad)}", flush=True)
print("TOTAL B2 with cross-class p-collision:", len(bad))
print("first 30:", bad[:30])
# valuation structure: min 2-adic valuation of (x,y)
from collections import Counter
def v2(n):
    if n == 0: return 99
    c = 0
    while n % 2 == 0: n //= 2; c += 1
    return c
cnt = Counter(min(v2(x), v2(y)) for (x, y) in bad)
print("by min v2(x,y):", dict(sorted(cnt.items())))
import json
json.dump(bad, open("wave46_rho_badB2.json", "w"))
print("saved wave46_rho_badB2.json")
