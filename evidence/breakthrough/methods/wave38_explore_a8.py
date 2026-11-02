"""Wave 38 (a): odd-flip partner test + half-period shift check.

For each point y (period p>=8): check y_{i+p/2} - y_i mod Q pattern (should be
(Q/2)*nu_1 on even i, (Q/2)*nu_2 on odd i). Build z_i = y_i + (Q/2)*(i odd);
check z is a kernel sequence, its fiber, and whether its orbit differs.
"""
import sys
sys.path.insert(0, ".")
import numpy as np
from collections import Counter, defaultdict
from wave16_d1a_targeted import Dm, torsion_data, group_ids
from wave36_2part import snf_kernel_i32, orbit_canon
from wave38_helpers import period_of, e_seq


for m, q in [(32, 8192), (64, 32768)]:
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
    # map from sorted-multiset tuple to fiber id, and from orbit canon to orbit id
    fib_of_ms = {}
    for i in range(len(pts)):
        fib_of_ms[tuple(np.sort(pts[i]).tolist())] = int(fib[i])
    orb_of_canon = {}
    for i in range(len(pts)):
        orb_of_canon[(int(ba[i]), int(bb[i]))] = int(gam[i])
    print(f"== m={m} q={q}")
    rows = Counter()
    for i in range(len(pts)):
        f = int(fib[i])
        cat = ("split-onsup" if f in split_ids and f in onsup else
               "split-offsup" if f in split_ids else
               "nonsplit-onsup" if sup[i] else "nonsplit-offsup")
        y = pts[i].astype(np.int64)
        p = period_of(y)
        if p < 8:
            continue
        # half-period shift pattern over one period
        hp = (np.roll(y, -(p // 2))[:p] - y[:p]) % q
        # hp_i should be (Q/2)*nu_1 for i even, (Q/2)*nu_2 for i odd
        hq = hp // (q // 2)
        assert np.all(hp % (q // 2) == 0), "half-shift not multiple of Q/2"
        nu1 = int(hq[0]) if len(set(hq[0:p:2].tolist())) == 1 else -1
        nu2 = int(hq[1]) if len(set(hq[1:p:2].tolist())) == 1 else -1
        assert nu1 in (0, 1) and nu2 in (0, 1), f"nu bad: {nu1},{nu2}"
        # odd-flip z
        flip = np.zeros(p, dtype=np.int64)
        flip[1:p:2] = q // 2
        z = (y[:p] + flip) % q
        # z must be a kernel sequence of period dividing p: check recurrence mod q
        rec = (np.roll(z, -1) - 6 * z + np.roll(z, 1)) % q
        is_kernel = bool(np.all(rec == 0))
        # fiber of z (extend z to length m by repetition, since p | m)
        zfull = np.tile(z, m // p)
        zfib = fib_of_ms.get(tuple(np.sort(zfull).tolist()), None)
        same_fiber = (zfib == f)
        # orbit of z
        zba, zbb = orbit_canon(np.array([[int(z[0]), int(z[1])]], dtype=np.int64), m, q)
        zorb = orb_of_canon.get((int(zba[0]), int(zbb[0])), None)
        same_orbit = (zorb == int(gam[i]))
        rows[(cat, f"nu=({nu1},{nu2})", f"z_kernel={is_kernel}",
              f"z_same_fiber={same_fiber}", f"z_same_orbit={same_orbit}")] += 1
    for k in sorted(rows, key=str):
        print("   ", k, rows[k])
