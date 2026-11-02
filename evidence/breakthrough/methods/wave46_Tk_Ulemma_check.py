"""Wave 46, task 9: extend the U-lemma verification (wave 38 (b)) to the
128 -> 256 step. For each on-support split fiber F at m=128, pick y in F,
compute p, U' = U*N/(Q*p) mod 2 with U = sum_{i<p} y_i z_i, and
W = sum_{i<4p} delta_i z_i mod 2 from one lift to m=256. Check:
  non-max p -> U' even (U = 0 mod Q/4);
  max p (= N/4) -> U' + W == pat_z (mod 2) for all 16 torsion rows,
where pat_z = 1 iff z-pattern non-constant mod 4.
Identical logic to wave38_explore_b.py, only the level pair changes.
"""
import sys
sys.path.insert(0, ".")
import numpy as np
from collections import Counter, defaultdict
from wave16_d1a_targeted import Dm, torsion_data, group_ids
from wave36_2part import snf_kernel_i32, orbit_canon
from wave38_helpers import period_of, lifts_of_point

m, q, m_hi, q_hi = 128, 131072, 256, 524288
N = m
pats = None
D = Dm(m)
Z, Qmod = torsion_data(m, D)
pats = []
for r in range(Z.shape[0]):
    pat = tuple(int(Z[r, i]) for i in range(4))
    assert all(int(Z[r, i]) == pat[i % 4] for i in range(m))
    pats.append(pat)
pat_z = [0 if len({v % 4 for v in pat}) == 1 else 1 for pat in pats]
print(f"m={m} q={q}: pat_z={pat_z} (sum {sum(pat_z)})")
pts = snf_kernel_i32(m, q)
print(f"kernel points: {len(pts)}")
Qm = np.array([qq % q for qq in Qmod], dtype=np.int64)
sup = ((2 * Qm[None, :] - pts.astype(np.int64) @ Z.astype(np.int64).T) % q == 0).all(axis=1)
fib = group_ids(np.sort(pts, axis=1))
ba, bb = orbit_canon(pts[:, :2].astype(np.int64), m, q)
gam = group_ids(np.stack([ba, bb], axis=1))
fib_orbits = defaultdict(set)
for i in range(len(pts)):
    fib_orbits[int(fib[i])].add(int(gam[i]))
split_ids = {f for f in fib_orbits if len(fib_orbits[f]) > 1}
onsup = {int(fib[i]) for i in range(len(pts)) if sup[i]}
print(f"on-support split fibers at m={m}: {len(split_ids & onsup)}")
n_max = n_nonmax = n_bad = 0
for f in sorted(split_ids & onsup):
    idx = [i for i in range(len(pts)) if int(fib[i]) == f]
    y = pts[idx[0]].astype(np.int64)
    p = period_of(y)
    o = len(fib_orbits[f])
    is_max = (p == N // 4)
    yper = y[:p]
    Uprime = []
    for pat in pats:
        zfull = np.array([pat[i % 4] for i in range(p)], dtype=np.int64)
        U = int(np.sum(yper * zfull))
        assert (U * N) % (q * p) == 0, f"U not divisible: U={U} N={N} q={q} p={p}"
        Uprime.append((U * N // (q * p)) % 2)
    lifts = lifts_of_point(pts[idx[0]], m_hi, q_hi, q)
    assert len(lifts) == 16, f"expected 16 lifts, got {len(lifts)}"
    s = lifts[0]
    d = ((s - np.tile(pts[idx[0]], m_hi // m)) // q) % 4
    W = []
    for pat in pats:
        zfull = np.array([pat[i % 4] for i in range(4 * p)], dtype=np.int64)
        W.append(int(np.sum(d[:4 * p] * zfull)) % 2)
    if is_max:
        ok = all((Uprime[r] + W[r]) % 2 == pat_z[r] for r in range(16))
        n_max += 1
        print(f"fiber{f} o={o} p={p} MAX U'={Uprime} W={W} match={ok}")
    else:
        ok = all(u == 0 for u in Uprime)
        n_nonmax += 1
        print(f"fiber{f} o={o} p={p} nonmax U'={Uprime} W={W} U'even={ok}")
    if not ok:
        n_bad += 1
print(f"TOTAL max={n_max} nonmax={n_nonmax} bad={n_bad}")
