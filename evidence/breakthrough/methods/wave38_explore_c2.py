"""Wave 38 (c2): fully-colliding period<=4 orbits: Y-types + (C,D) block drift.

For each non-split on-support orbit of period<=4 at level j, take a point y,
one lift y' (delta = (y'-ybar)/Q), compute C,D from delta_{r+4}-delta_r = C+D*r
(mod 4), and the number of distinct lift multisets. Compare fully-colliding
Y-types across j=5 (m=32) and j=6 (m=64)."""
import sys
sys.path.insert(0, ".")
import numpy as np
from collections import defaultdict
from wave16_d1a_targeted import Dm, torsion_data, group_ids
from wave36_2part import snf_kernel_i32, orbit_canon
from wave38_helpers import period_of, lifts_of_point


def analyze(m, q):
    N = m
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
        # distinct lift multisets
        ms = {tuple(sorted(lft.tolist())) for lft in lifts}
        # Y-type: y/(q//32) mod 32, first 4 values
        Yt = tuple((int(v) // (q // 32)) % 32 for v in y[:4])
        # (C,D) from first lift's delta
        yb = y[: 2 * N]  # y repeated? y has length N; lift length 2N; ybar = y tiled
        ybar = np.tile(y, 2)
        d = ((lifts[0].astype(np.int64) - ybar) // q) % 4
        # delta_{r+4} - delta_r = C + D*r mod 4, for r=0..3 (use r=0,1 to solve)
        diffs = [(int(d[r + 4]) - int(d[r])) % 4 for r in range(4)]
        C = diffs[0]
        Dd = (diffs[1] - diffs[0]) % 4
        ok = all(diffs[r] == (C + Dd * r) % 4 for r in range(4))
        assert ok, f"block drift not affine: {diffs}"
        out.append((Yt, p, len(idx), len(ms), C, Dd, tuple((C + Dd * r) % 4 for r in range(4))))
    return out


for m, q in [(32, 8192), (64, 32768)]:
    res = analyze(m, q)
    full = [r for r in res if r[3] == 1]
    print(f"== m={m}: period<=4 non-split onsup orbits with lifts: {len(res)}, "
          f"fully colliding: {len(full)}")
    for r in sorted(full, key=lambda t: (-t[2], t[1])):
        print(f"   Y={r[0]} p={r[1]} size={r[2]} C={r[4]} D={r[5]} C+Dr={r[6]}")
    if m == 32:
        full32 = {r[0] for r in full}
    else:
        full64 = {r[0] for r in full}
        print(f"   Y-types match m=32: {full64 == full32}")
    # also: distribution of (C,D) vs full collision
    from collections import Counter
    cnt = Counter((r[3] == 1, r[6]) for r in res)
    print(f"   (full, C+Dr) counts: {dict(cnt)}")
