"""Wave 38 (a) mechanism hunt: half-period flip, alternating sum, at m=32,64.

For each point: p, A = E-O (alternating sum over one period),
half-flip vector h_i = (y_{i+p/2} + y_i) mod Q, and its pattern.
"""
import sys
sys.path.insert(0, ".")
import numpy as np
from collections import Counter, defaultdict
from wave16_d1a_targeted import Dm, torsion_data, group_ids
from wave36_2part import snf_kernel_i32, orbit_canon
from wave38_helpers import period_of


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
            rows[(cat, f"p={p}", "short")] += 1
            continue
        E = int(np.sum(y[0:p:2])); O = int(np.sum(y[1:p:2]))
        A = E - O
        # half-flip: h_i = (y_{i+p/2} + y_i) mod q, i < p/2 (y p-periodic)
        h = (np.roll(y, -(p // 2))[:p] + y[:p]) % q
        hhalf = h[:p // 2]
        uniq = sorted(set(hhalf.tolist()))
        rows[(cat, f"p={p}", f"A={A}", f"h_uniq={uniq[:6]}", f"n_huniq={len(uniq)}")] += 1
    for k in sorted(rows, key=str):
        print("   ", k, rows[k])
