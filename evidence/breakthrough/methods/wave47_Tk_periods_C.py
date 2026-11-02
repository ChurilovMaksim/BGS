"""Wave 47, task 10, script C: lift periods of the 10 fully-colliding
period<=4 source orbits, and (C, D) block drift per source.

For each source orbit at level m (m = 32, 64): take a point y, list all
its lifts to level 2m (wave38_helpers.lifts_of_point), compute each
lift's period and the Gamma-orbit canons of the lifts at level 2m.
Also (C, D) from the first lift's delta, as in wave38_explore_c2.
Prediction from block drift: for lift period q' with 4 | q' (q' = 4t),
t = min{t >= 1 : t*(C + D*r) == 0 mod 4 for all r}; q' is a multiple
of the source period q.
"""
import sys
sys.path.insert(0, ".")
import numpy as np
from collections import defaultdict
from wave16_d1a_targeted import Dm, torsion_data, group_ids
from wave36_2part import snf_kernel_i32, orbit_canon
from wave38_helpers import period_of, lifts_of_point


def analyze(m, q):
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
    onsup = {int(fib[i]) for i in range(len(pts)) if sup[i]}
    out = []
    for f, orbs in fib_orbits.items():
        if len(orbs) != 1 or f not in onsup:
            continue
        idx = [i for i in range(len(pts)) if int(fib[i]) == f]
        y = pts[idx[0]].astype(np.int64)
        p = period_of(y)
        if p > 4:
            continue
        lifts = lifts_of_point(y, 2 * m, 4 * q, q)
        if not lifts:
            continue
        ms = {tuple(sorted(lft.tolist())) for lft in lifts}
        if len(ms) != 1:
            continue  # only fully-colliding sources
        Yt = tuple((int(v) // (q // 32)) % 32 for v in y[:4])
        ybar = np.tile(y, 2)
        d = ((lifts[0].astype(np.int64) - ybar) // q) % 4
        diffs = [(int(d[r + 4]) - int(d[r])) % 4 for r in range(4)]
        C = diffs[0]
        Dd = (diffs[1] - diffs[0]) % 4
        assert all(diffs[r] == (C + Dd * r) % 4 for r in range(4))
        # lift periods + lift orbit canons at level 2m
        lpers = sorted({period_of(lft) for lft in lifts})
        seeds_hi = np.array([lft[:2] for lft in lifts], dtype=np.int64)
        ca, cb = orbit_canon(seeds_hi, 2 * m, 4 * q)
        lorbs = len({(int(a), int(b)) for a, b in zip(ca, cb)})
        out.append((Yt, p, len(idx), C, Dd,
                    tuple((C + Dd * r) % 4 for r in range(4)),
                    len(lifts), lpers, lorbs))
    return out


for m, q in [(32, 8192), (64, 32768)]:
    res = analyze(m, q)
    print(f"== m={m}: fully-colliding period<=4 sources: {len(res)}")
    for r in sorted(res, key=lambda t: (-t[2], t[1])):
        Yt, p, size, C, Dd, cdr, nl, lpers, lorbs = r
        # block-drift prediction for q' divisible by 4: t*(C+Dr)==0 for all r
        pred = None
        for t in range(1, 5):
            if all((t * v) % 4 == 0 for v in cdr):
                pred = 4 * t
                break
        print(f"   Y={Yt} q={p} size={size} C={C} D={Dd} C+Dr={cdr} "
              f"lifts={nl} lift_periods={lpers} lift_orbits={lorbs} "
              f"drift_pred_4t={pred}")
