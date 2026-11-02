"""Wave 35, task 3: direct row checks for the (816,17^4) counterexample.
For one representative C per split fiber (found via TM grouping):
build the kernel row mod 17^4, check recurrence + periodicity,
support via wave16 comp_supported, and row-orbit size via the
dihedral action on rows."""
import sys
sys.path.insert(0, ".")
import numpy as np
from wave16_d1a_targeted import Dm, torsion_data, comp_supported
from collections import defaultdict

m, p, f, mod, q = 816, 17, 2, 289, 17 ** 4
A = [(1, 0)]
for _ in range(m):
    a, b = A[-1]
    A.append(((3 * a + 4 * b) % mod, (2 * a + 3 * b) % mod))
assert A[m] == (1, 0)
d = next(j for j in range(1, m + 1) if A[j] == (1, 0))
print("d' =", d)
nC = mod * mod
a = np.repeat(np.arange(mod, dtype=np.int64), mod)
b = np.tile(np.arange(mod, dtype=np.int64), mod)
ca, cb = a.copy(), b.copy()
cyc = np.empty((nC, d), dtype=np.int64)
ba, bb = a.copy(), b.copy()
for j in range(d):
    aj, bj = A[j]
    cyc[:, j] = (2 * ca) % mod
    x1, y1 = ca, cb
    x2 = (a * aj - 2 * b * bj) % mod
    y2 = (a * bj - b * aj) % mod
    upd = (x1 < ba) | ((x1 == ba) & (y1 < bb))
    ba = np.where(upd, x1, ba); bb = np.where(upd, y1, bb)
    upd2 = (x2 < ba) | ((x2 == ba) & (y2 < bb))
    ba = np.where(upd2, x2, ba); bb = np.where(upd2, y2, bb)
    ca, cb = (3 * ca + 4 * cb) % mod, (2 * ca + 3 * cb) % mod
srt = np.sort(cyc, axis=1)
uf, inv, cnt = np.unique(srt, axis=0, return_inverse=True,
                         return_counts=True)
trip = np.empty(nC, dtype=[('f', np.int64), ('a', np.int64),
                           ('b', np.int64)])
trip['f'] = inv; trip['a'] = ba; trip['b'] = bb
ut = np.unique(trip)
cc = defaultdict(int)
for t in ut:
    cc[t['f']] += 1
split_ids = [fi for fi in range(len(uf)) if cc[fi] >= 2]
print("split fibers:", len(split_ids))
D = Dm(m); Z, Qmod = torsion_data(m, D)
for fi in split_ids:
    ci = int(np.where(inv == fi)[0][0])
    C = (int(a[ci]), int(b[ci]))
    ca2, cb2 = C
    row = []
    for j in range(m):
        row.append((mod * (2 * ca2)) % q)
        ca2, cb2 = (3 * ca2 + 4 * cb2) % mod, (2 * ca2 + 3 * cb2) % mod
    row = np.array(row, dtype=np.int64)
    rec = bool(np.all((np.roll(row, -1) - 6 * row + np.roll(row, 1)) % q == 0))
    sup = bool(comp_supported(row.reshape(1, -1), Z, Qmod, q)[0])
    orb = set()
    for k in range(m):
        orb.add(tuple(np.roll(row, -k).tolist()))
        orb.add(tuple(row[(k - np.arange(m)) % m].tolist()))
    print(f"  size={int(cnt[fi])} orbits={cc[fi]} C={C} rec={rec} "
          f"supported={sup} roworbit={len(orb)}")
