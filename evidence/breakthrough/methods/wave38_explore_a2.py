"""Wave 38 (a) follow-up: (E,O) sums vs drift oddness; m=32 full table.

E = sum of y over even positions of one period, O = sum over odd positions.
Drift Lemma <=> (2E-6O)/Q odd and (2O-6E)/Q odd  (sums of e over odd/even i).
Check E-3O and O-3E mod Q, and E',O' mod 32 (E=(Q/32)E' etc.).
"""
import sys
sys.path.insert(0, ".")
import numpy as np
from collections import Counter, defaultdict
from wave16_d1a_targeted import Dm, torsion_data, group_ids
from wave36_2part import snf_kernel_i32, orbit_canon
from wave38_helpers import period_of


def eo_of(y, p):
    yy = y.astype(np.int64)
    E = int(np.sum(yy[0:p:2]))
    O = int(np.sum(yy[1:p:2]))
    return E, O


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
    for i in range(len(pts)):
        fib_orbits[int(fib[i])].add(int(gam[i]))
    split_ids = {f for f in fib_orbits if len(fib_orbits[f]) > 1}
    onsup = set()
    for i in range(len(pts)):
        if sup[i]:
            onsup.add(int(fib[i]))
    print(f"== m={m} q={q}")
    rows = Counter()
    for i in range(len(pts)):
        f = int(fib[i])
        cat = ("split-onsup" if f in split_ids and f in onsup else
               "split-offsup" if f in split_ids else
               "nonsplit-onsup" if sup[i] else "nonsplit-offsup")
        y = pts[i]
        p = period_of(y)
        if p < 8:
            rows[(cat, f"p={p}", "short")] += 1
            continue
        E, O = eo_of(y, p)
        a = (2 * E - 6 * O) // q if (2 * E - 6 * O) % q == 0 else None
        b = (2 * O - 6 * E) // q if (2 * O - 6 * E) % q == 0 else None
        if a is None or b is None:
            rows[(cat, f"p={p}", "E/O nondiv")] += 1
            continue
        rows[(cat, f"p={p}", f"a_odd={a % 2 == 1}", f"b_odd={b % 2 == 1}",
              f"E-3O={(E - 3 * O) % q}", f"O-3E={(O - 3 * E) % q}")] += 1
    for k in sorted(rows, key=str):
        print("   ", k, rows[k])
