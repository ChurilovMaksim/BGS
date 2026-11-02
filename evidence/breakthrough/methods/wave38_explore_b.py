"""Wave 38 (b): defect identification. For each on-support split fiber F at
level j, pick y in F, compute p, U' = U*N/(Q*p) mod 2 with U = sum_{i<p} y_i z_i,
and W = sum_{i<4p} delta_i z_i mod 2 from one lift. Check:
  non-max p -> U' even;  max p -> U' + W == pat_z (mod 2),
where pat_z = 1 iff z-pattern non-constant mod 4.
z-patterns: period-4 patterns of torsion rows (level-independent).
"""
import sys
sys.path.insert(0, ".")
import numpy as np
from collections import Counter, defaultdict
from wave16_d1a_targeted import Dm, torsion_data, group_ids
from wave36_2part import snf_kernel_i32, orbit_canon
from wave38_helpers import period_of, lifts_of_point


def z_patterns(m):
    D = Dm(m)
    Z, Qmod = torsion_data(m, D)
    pats = []
    for r in range(Z.shape[0]):
        pat = tuple(int(Z[r, i]) for i in range(4))
        assert all(int(Z[r, i]) == pat[i % 4] for i in range(m))
        pats.append(pat)
    return pats


for m, q, m_hi, q_hi in [(32, 8192, 64, 32768), (64, 32768, 128, 131072)]:
    N = m
    pats = z_patterns(m)
    pat_z = [0 if len({v % 4 for v in pat}) == 1 else 1 for pat in pats]
    print(f"== m={m} q={q}: pat_z={pat_z} (sum {sum(pat_z)})")
    pts = snf_kernel_i32(m, q)
    D = Dm(m)
    Z, Qmod = torsion_data(m, D)
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
    rows = Counter()
    for f in sorted(split_ids & onsup):
        idx = [i for i in range(len(pts)) if int(fib[i]) == f]
        y = pts[idx[0]].astype(np.int64)
        p = period_of(y)
        o = len(fib_orbits[f])
        is_max = (p == N // 4)
        # U' per torsion row
        yper = y[:p]
        Uprime = []
        for pat in pats:
            zfull = np.array([pat[i % 4] for i in range(p)], dtype=np.int64)
            U = int(np.sum(yper * zfull))
            assert (U * N) % (q * p) == 0, f"U not divisible: U={U} N={N} q={q} p={p}"
            Uprime.append((U * N // (q * p)) % 2)
        # W per torsion row from one lift
        lifts = lifts_of_point(pts[idx[0]], m_hi, q_hi, q)
        assert len(lifts) == 16, f"expected 16 lifts, got {len(lifts)}"
        s = lifts[0]
        d = ((s - np.tile(pts[idx[0]], m_hi // m)) // q) % 4
        W = []
        for pat in pats:
            zfull = np.array([pat[i % 4] for i in range(4 * p)], dtype=np.int64)
            W.append(int(np.sum(d[:4 * p] * zfull)) % 2)
        # check the identification
        if is_max:
            ok = all((Uprime[r] + W[r]) % 2 == pat_z[r] for r in range(16))
            rows[(f"fiber{f}", f"o={o}", f"p={p}", "MAX",
                  f"U'={Uprime}", f"W={W}", f"match={ok}")] += 1
        else:
            ok = all(u == 0 for u in Uprime)
            rows[(f"fiber{f}", f"o={o}", f"p={p}", "nonmax",
                  f"U'={Uprime}", f"W={W}", f"U'even={ok}")] += 1
    for k in sorted(rows, key=str):
        print("   ", k, rows[k])
