"""Wave 35, task 3: 2-part census at m=128 (q2 = 131072).
Direct kernel rows + sorted-multiset fibers + seed-space Gamma orbits
(S: (a,b)->(b,6b-a), R: (a,b)->(a,6a-b)) + wave16 support criterion.
Reports on-support split fibers (all points supported; support is
constant on fibers, verified)."""
import sys
sys.path.insert(0, ".")
import numpy as np, sympy as sp
from wave16_d1a_targeted import (Dm, snf_kernel, torsion_data,
                                 comp_supported, group_ids)

m = 128
D = Dm(m); q2 = 2 ** sp.factorint(D)[2]
print("q2 =", q2)
Z, Qmod = torsion_data(m, D)
pts = snf_kernel(m, q2)
assert len(pts) == q2
fib = group_ids(np.sort(pts, axis=1))
sup = comp_supported(pts, Z, Qmod, q2)
# seed-space orbit canon: seeds are (y0, y1) = (row[0], row[1])
seeds = pts[:, :2].astype(np.int64)
# orbit: S^j and R S^j for j < m, mod q2
canon = np.empty((len(pts), 2), dtype=np.int64)
ca, cb = seeds[:, 0].copy(), seeds[:, 1].copy()
ba, bb = ca.copy(), cb.copy()
for j in range(m):
    # candidate S^j seed = (ca, cb); candidate R S^j seed = (ca, 6ca-cb)
    x2 = ca; y2 = (6 * ca - cb) % q2
    upd = (ca < ba) | ((ca == ba) & (cb < bb))
    ba = np.where(upd, ca, ba); bb = np.where(upd, cb, bb)
    upd2 = (x2 < ba) | ((x2 == ba) & (y2 < bb))
    ba = np.where(upd2, x2, ba); bb = np.where(upd2, y2, bb)
    ca, cb = cb, (6 * cb - ca) % q2
canon[:, 0] = ba; canon[:, 1] = bb
gam = group_ids(canon)
from collections import defaultdict
# per fiber: orbit count + support
fib_orbits = defaultdict(set)
fib_sup = defaultdict(lambda: [0, 0])
for i in range(len(pts)):
    f = int(fib[i])
    fib_orbits[f].add(int(gam[i]))
    fib_sup[f][0] += int(sup[i]); fib_sup[f][1] += 1
split = [(f, len(o), fib_sup[f]) for f, o in fib_orbits.items() if len(o) > 1]
onsup = [(f, o, s) for (f, o, s) in split if s[0] == s[1]]
mixed = [(f, o, s) for (f, o, s) in split if 0 < s[0] < s[1]]
print(f"split fibers={len(split)} on-support={len(onsup)} mixed={len(mixed)}")
for (f, o, s) in sorted(onsup, key=lambda t: -t[1]):
    sz = int((fib == f).sum())
    print(f"  fiber size={sz} orbits={o} supported={s[0]}/{s[1]}")
