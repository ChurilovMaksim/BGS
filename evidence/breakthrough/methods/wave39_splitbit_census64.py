"""Wave 39, task 3: Split Bit census at m=64 (q=32768), vectorized periods.
Checks: split => nu=(1,1); nonsplit p>=8 => nu in {(1,0),(0,1)};
nu=(1,0) odd sub-multiset never Q/2-symmetric; nu=(0,1) even never.
"""
import sys
sys.path.insert(0, ".")
import numpy as np
from collections import Counter, defaultdict
from wave16_d1a_targeted import group_ids
from wave36_2part import snf_kernel_i32, orbit_canon

m, q = 64, 32768
pts = snf_kernel_i32(m, q)
print("points:", len(pts))
fib = group_ids(np.sort(pts, axis=1))
ba, bb = orbit_canon(pts[:, :2].astype(np.int64), m, q)
gam = group_ids(np.stack([ba, bb], axis=1))
fib_orbits = defaultdict(set)
for i in range(len(pts)):
    fib_orbits[int(fib[i])].add(int(gam[i]))
split_ids = {f for f in fib_orbits if len(fib_orbits[f]) > 1}
print("fibers:", len(fib_orbits), "split:", len(split_ids),
      "orbit-count dist:", Counter(len(fib_orbits[f]) for f in split_ids))

# vectorized minimal period (divisors of 64)
divs = [1, 2, 4, 8, 16, 32, 64]
per = np.full(len(pts), 64, dtype=np.int64)
for p in divs[:-1]:
    # p-periodic iff pts[:, i] == pts[:, i%p] for all i; check via reshape
    ok = np.ones(len(pts), dtype=bool)
    arr = pts.astype(np.int64)
    for r in range(p):
        ok &= (arr[:, r::p] == arr[:, r:r + 1]).all(axis=1)
    per = np.where(ok & (per == 64), p, per)
half = q // 2
arr = pts.astype(np.int64)
viol_split = 0
viol_nonsplit = 0
sym10 = 0
sym01 = 0
tot10 = tot01 = 0
nu_counter = Counter()
for i in range(len(pts)):
    p = int(per[i])
    if p < 8 or p % 2:
        continue
    y = arr[i]
    d0 = int(y[p // 2] - y[0]) % q
    d1 = int(y[p // 2 + 1] - y[1]) % q
    if d0 % half or d1 % half:
        nu_counter["BAD"] += 1
        continue
    nu = ((d0 // half) % 2, (d1 // half) % 2)
    nu_counter[nu] += 1
    f = int(fib[i])
    if f in split_ids and nu != (1, 1):
        viol_split += 1
    if f not in split_ids and nu not in ((1, 0), (0, 1)):
        viol_nonsplit += 1
    if nu == (1, 0):
        tot10 += 1
        odd = [int(v) for v in y[:p:2 + 1] if False]
        odd = [int(y[t]) for t in range(p) if t % 2 == 1]
        c = Counter(odd)
        if all(c[v] == c[(v + half) % q] for v in c):
            sym10 += 1
    elif nu == (0, 1):
        tot01 += 1
        even = [int(y[t]) for t in range(p) if t % 2 == 0]
        c = Counter(even)
        if all(c[v] == c[(v + half) % q] for v in c):
            sym01 += 1
print("nu dist (p>=8):", dict(nu_counter))
print("split-fiber points with nu!=(1,1):", viol_split)
print("nonsplit p>=8 points with nu not in {(1,0),(0,1)}:", viol_nonsplit)
print(f"nu=(1,0): {tot10} points, odd sub-multiset symmetric: {sym10}")
print(f"nu=(0,1): {tot01} points, even sub-multiset symmetric: {sym01}")
