"""Wave 38, task 4, exploration (a): drift of split-fiber points at m=32,64.

Reproduce: kernel points, fibers, support, orbits (wave36_2part machinery),
then for each point compute period p, one lift to next level, delta digits,
drift D_r, and (C,D) mod 4. Compare split vs non-split, on- vs off-support.
"""
import sys
sys.path.insert(0, ".")
import numpy as np
from collections import Counter, defaultdict
from wave16_d1a_targeted import Dm, torsion_data, group_ids
from wave36_2part import snf_kernel_i32, orbit_canon
from wave38_helpers import lifts_of_point


from wave38_helpers import period_of


def drift_of_point(y, m_hi, q_hi, q_lo):
    """Return (p, D list mod 4, C, Dcoef) for one lift, or None if no lifts."""
    lifts = lifts_of_point(y, m_hi, q_hi, q_lo)
    if not lifts:
        return None
    s = lifts[0]
    m_lo = len(y)
    # delta digits: s_i = y_{i mod m_lo} + q_lo * delta_i  (mod q_hi)
    d = ((s - np.tile(y, m_hi // m_lo)) // q_lo) % 4
    p = period_of(y)
    D = [int((d[(r + p) % m_hi] - d[r]) % 4) for r in range(p)]
    C = D[0]
    Dc = (D[1] - D[0]) % 4 if p >= 2 else 0
    return p, D, C, Dc, len(lifts)


from wave38_helpers import e_seq


for m, q, m_hi, q_hi in [(32, 8192, 64, 32768), (64, 32768, 128, 131072)]:
    pts = snf_kernel_i32(m, q)
    D = Dm(m)
    Z, Qmod = torsion_data(m, D)
    Qm = np.array([qq % q for qq in Qmod], dtype=np.int64)
    sup = ((2 * Qm[None, :] - pts.astype(np.int64) @ Z.astype(np.int64).T) % q == 0).all(axis=1)
    fib = group_ids(np.sort(pts, axis=1))
    ba, bb = orbit_canon(pts[:, :2].astype(np.int64), m, q)
    gam = group_ids(np.stack([ba, bb], axis=1))
    fib_orbits = defaultdict(set)
    fib_sup = defaultdict(lambda: [0, 0])
    for i in range(len(pts)):
        fib_orbits[int(fib[i])].add(int(gam[i]))
        fib_sup[int(fib[i])][0] += int(sup[i])
        fib_sup[int(fib[i])][1] += 1
    split_ids = {f for f in fib_orbits if len(fib_orbits[f]) > 1}
    onsup_split = {f for f in split_ids if fib_sup[f][0] == fib_sup[f][1]}
    print(f"== m={m}: points={len(pts)} split fibers={len(split_ids)} "
          f"on-support split={len(onsup_split)}")
    # drift stats by category
    cats = Counter()
    cd_examples = defaultdict(list)
    for i in range(len(pts)):
        f = int(fib[i])
        cat = ("split-onsup" if f in onsup_split else
               "split-offsup" if f in split_ids else
               "nonsplit-onsup" if sup[i] else "nonsplit-offsup")
        r = drift_of_point(pts[i], m_hi, q_hi, q)
        if r is None:
            cats[(cat, "nolift")] += 1
            continue
        p, Dd, C, Dc, nl = r
        odd = all(d % 2 == 1 for d in Dd)
        cats[(cat, f"p={p}", f"odd={odd}", f"C={C}", f"Dcoef={Dc}", f"nlifts={nl}")] += 1
        if len(cd_examples[(cat, odd)]) < 3:
            cd_examples[(cat, odd)].append((pts[i][:8].tolist(), p, Dd[:8], C, Dc))
    for k in sorted(cats):
        print("   ", k, cats[k])
    for k in sorted(cd_examples):
        print("   ex", k, cd_examples[k][:2])
    # verify e-identity on one split-onsup point
    for i in range(len(pts)):
        if int(fib[i]) in onsup_split:
            y = pts[i]
            p = period_of(y)
            r = drift_of_point(y, m_hi, q_hi, q)
            p2, Dd, C, Dc, nl = r
            assert p == p2
            e = e_seq(y, q)
            ok = True
            for rr in range(p):
                ssum = sum(j * int(e[(rr + j) % m]) for j in range(1, p)) % 4
                if ssum != Dd[rr]:
                    ok = False
            print(f"   e-identity check on split-onsup point (p={p}): {ok}, "
                  f"D={Dd}, e[:12]={e[:12].tolist()}")
            break
