"""Wave 39, task 3: valuation structure by nu type at m=32.
- SNF invariant factors of M^m - I.
- min 2-adic valuation of sequence values, by nu type.
- is y/4 (mod Q/4) (N/2)-periodic mod Q/4 for nu!=(1,1) points?
- split fibers: are even-flip and odd-flip in the same orbit as each other?
"""
import sys
sys.path.insert(0, ".")
import numpy as np, math, sympy as sp
from collections import Counter, defaultdict
from wave16_d1a_targeted import Dm, torsion_data, group_ids, smith_normal_decomp
from wave36_2part import snf_kernel_i32, orbit_canon


def period_of_row(y):
    m = len(y)
    for p in range(1, m + 1):
        if m % p == 0 and all(y[i] == y[i % p] for i in range(m)):
            return p
    return m


def v2(n):
    if n == 0:
        return 99
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


m, q = 32, 8192
M = sp.Matrix([[6, -1], [1, 0]])
A = M**m - sp.eye(2)
S, U, V = smith_normal_decomp(A, domain=sp.ZZ)
d1, d2 = abs(int(S[0, 0])), abs(int(S[1, 1]))
print("SNF d1,d2:", d1, d2, "v2:", v2(d1), v2(d2),
      "gcd(d1,q),gcd(d2,q):", math.gcd(d1, q), math.gcd(d2, q))

pts = snf_kernel_i32(m, q)
fib = group_ids(np.sort(pts, axis=1))
ba, bb = orbit_canon(pts[:, :2].astype(np.int64), m, q)
gam = group_ids(np.stack([ba, bb], axis=1))
fib_orbits = defaultdict(set)
for i in range(len(pts)):
    fib_orbits[int(fib[i])].add(int(gam[i]))
split_ids = {f for f in fib_orbits if len(fib_orbits[f]) > 1}

half = q // 2
minval_by_nu = defaultdict(Counter)
allval_mod4 = Counter()
for i in range(len(pts)):
    y = pts[i].astype(np.int64)
    p = period_of_row(y)
    if p < 8 or p % 2:
        continue
    d0 = int(y[p // 2] - y[0]) % q
    d1 = int(y[p // 2 + 1] - y[1]) % q
    nu = ((d0 // half) % 2, (d1 // half) % 2) if d0 % half == 0 and d1 % half == 0 else None
    mv = min(v2(int(v)) for v in y[:p])
    minval_by_nu[nu][mv] += 1
    allval_mod4[(nu, int(y[0]) % 4)] += 1
for nu in sorted(minval_by_nu, key=str):
    print("nu", nu, "min-valuation dist:", dict(sorted(minval_by_nu[nu].items())))

# y/4 periodicity mod Q/4 for nu!=(1,1)
print("\ny/4 (N/2)-periodic mod Q/4? (nu!=(1,1), p>=8)")
cnt = Counter()
for i in range(len(pts)):
    y = pts[i].astype(np.int64)
    p = period_of_row(y)
    if p < 8 or p % 2:
        continue
    d0 = int(y[p // 2] - y[0]) % q
    d1 = int(y[p // 2 + 1] - y[1]) % q
    nu = ((d0 // half) % 2, (d1 // half) % 2) if d0 % half == 0 and d1 % half == 0 else None
    if nu in ((1, 0), (0, 1)):
        yp = (y // 4) % (q // 4)
        per = all(int(yp[t + m // 2]) == int(yp[t]) for t in range(m // 2))
        cnt[per] += 1
print("  (N/2)-periodic:", cnt)

# split fibers: even-flip orbit vs odd-flip orbit
print("\nsplit fibers: even-flip orbit == odd-flip orbit?")
seed_to_idx = {(int(pts[i, 0]), int(pts[i, 1])): i for i in range(len(pts))}
for f in sorted(split_ids):
    members = [i for i in range(len(pts)) if fib[i] == f]
    y = pts[members[0]].astype(np.int64)
    idx = np.arange(m)
    ev = y.copy(); ev[idx % 2 == 0] = (ev[idx % 2 == 0] + half) % q
    od = y.copy(); od[idx % 2 == 1] = (od[idx % 2 == 1] + half) % q
    je = seed_to_idx.get((int(ev[0]), int(ev[1])))
    jo = seed_to_idx.get((int(od[0]), int(od[1])))
    same = (je is not None and jo is not None and int(gam[je]) == int(gam[jo]))
    print(f"  fiber {f} orbits={len(fib_orbits[f])} even==odd orbit: {same}")
