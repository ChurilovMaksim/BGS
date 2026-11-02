"""Wave 38 (a): A values for split points vs pQ/8; also B = A/2 structure."""
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
        if f not in split_ids:
            continue
        y = pts[i].astype(np.int64)
        p = period_of(y)
        if p < 8:
            continue
        E = int(np.sum(y[0:p:2])); O = int(np.sum(y[1:p:2]))
        A = E - O
        rows[(f"p={p}", f"A={A}", f"pQ/8={p*q//8}", f"A==pQ/8: {A == p*q//8}",
              f"AmodQ={A % q}")] += 1
    for k in sorted(rows, key=str):
        print("   ", k, rows[k])
