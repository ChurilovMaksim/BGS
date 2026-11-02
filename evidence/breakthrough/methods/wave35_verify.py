"""Wave 35, task 3, stage 3: exact verification of the (816,17^4)
counterexample + 2-part census at m=128.

1. Exact (hash-free) TM census at (816,289) and (147,343) via np.unique
   on sorted cycles.
2. Direct row checks: representatives' rows mod 17^4 satisfy recurrence
   + periodicity, support via wave16 comp_supported, orbit sizes via
   dihedral action on rows.
3. 2-part census at m=128 (seed-space orbits + sorted rows).
"""
import sys, math
sys.path.insert(0, ".")
import numpy as np, sympy as sp
from wave16_d1a_targeted import (Dm, snf_kernel, torsion_data,
                                 comp_supported, gamma_perms, lex_canon,
                                 group_ids)

def tm_exact(m, p, f):
    mod = p ** f
    A = [(1, 0)]
    for _ in range(m):
        a, b = A[-1]
        A.append(((3 * a + 4 * b) % mod, (2 * a + 3 * b) % mod))
    assert A[m] == (1, 0)
    d = next(j for j in range(1, m + 1) if A[j] == (1, 0))
    nC = mod * mod
    # cycles (nC, d) via iteration
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
    from collections import defaultdict
    cc = defaultdict(int)
    for t in ut:
        cc[t['f']] += 1
    res = [(int(cnt[fi]), cc[fi]) for fi in range(len(uf)) if cc[fi] >= 2]
    print(f"  TM-EXACT m={m} p={p} f={f}: split={len(res)} "
          f"sizes/orbits={sorted(res, reverse=True)}")
    return res, uf, inv, ba, bb, cyc, d, A

res816, uf816, inv816, ba816, bb816, cyc816, d816, A816 = tm_exact(816, 17, 2)
res147, *_ = tm_exact(147, 7, 3)

# --- direct row checks for (816,17^4) ---
m, p, f, mod, q = 816, 17, 2, 289, 17 ** 4
D = Dm(m); Z, Qmod = torsion_data(m, D)
# Use full-run arrays: rebuild C list + fiber id + orbit canon from
# the exact run by re-running the loop once more (memory OK: 83521 x 136)
nC = mod * mod
a = np.repeat(np.arange(mod, dtype=np.int64), mod)
b = np.tile(np.arange(mod, dtype=np.int64), mod)
ca, cb = a.copy(), b.copy()
cyc = np.empty((nC, d816), dtype=np.int64)
ba, bb = a.copy(), b.copy()
for j in range(d816):
    aj, bj = Aarr[j]
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
uf2, inv2, cnt2 = np.unique(srt, axis=0, return_inverse=True,
                            return_counts=True)
trip = np.empty(nC, dtype=[('f', np.int64), ('a', np.int64),
                           ('b', np.int64)])
trip['f'] = inv2; trip['a'] = ba; trip['b'] = bb
ut = np.unique(trip)
from collections import defaultdict
cc = defaultdict(int); firstC = {}
for t in ut:
    cc[t['f']] += 1
split_ids = [fi for fi in range(len(uf2)) if cc[fi] >= 2]
print(f"  exact rerun split count: {len(split_ids)} (expect 18)")
# one representative C per split fiber + its full orbit size + support
for fi in split_ids:
    ci = int(np.where(inv2 == fi)[0][0])
    C = (int(a[ci]), int(b[ci]))
    # build row mod q: y_j = mod * Tr(C alpha^j) mod q, j < m
    ca2, cb2 = C
    row = []
    for j in range(m):
        row.append((mod * (2 * ca2)) % q)
        ca2, cb2 = (3 * ca2 + 4 * cb2) % mod, (2 * ca2 + 3 * cb2) % mod
    row = np.array(row, dtype=np.int64)
    # recurrence + periodicity check
    rec = np.all((np.roll(row, -1) - 6 * row + np.roll(row, 1)) % q == 0)
    # support check (single row)
    sup = comp_supported(row.reshape(1, -1), Z, Qmod, q)[0]
    # orbit size via dihedral action on the row
    orb = set()
    for k in range(m):
        orb.add(tuple(np.roll(row, -k).tolist()))
        orb.add(tuple(row[(k - np.arange(m)) % m].tolist()))
    print(f"  fiber size={int(cnt2[fi])} orbits={cc[fi]} C={C} "
          f"rec={bool(rec)} supported={bool(sup)} roworbit={len(orb)}")
