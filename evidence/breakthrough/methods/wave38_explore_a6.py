"""Wave 38 (a) refined: E+O mod Q, A mod Q, period constancy on fibers."""
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
    fib_periods = defaultdict(set)
    fib_EO = defaultdict(set)
    fib_A = defaultdict(set)
    for i in range(len(pts)):
        f = int(fib[i])
        fib_orbits[f].add(int(gam[i]))
        y = pts[i].astype(np.int64)
        p = period_of(y)
        fib_periods[f].add(p)
        E = int(np.sum(y[0:p:2])); O = int(np.sum(y[1:p:2]))
        fib_EO[f].add((E + O) % q)
        fib_A[f].add((E - O) % (q // 4))
    split_ids = {f for f in fib_orbits if len(fib_orbits[f]) > 1}
    onsup = {int(fib[i]) for i in range(len(pts)) if sup[i]}
    print(f"== m={m} q={q}")
    # period constancy on fibers?
    multi_period = [f for f in fib_periods if len(fib_periods[f]) > 1]
    print("   fibers with >1 period:", len(multi_period),
          " (total fibers:", len(fib_periods), ")")
    multi_EO = [f for f in fib_EO if len(fib_EO[f]) > 1]
    print("   fibers with >1 E+O mod Q:", len(multi_EO))
    multi_A = [f for f in fib_A if len(fib_A[f]) > 1]
    print("   fibers with >1 A mod Q/4:", len(multi_A))
    rows = Counter()
    for f in fib_periods:
        cat = ("split-onsup" if f in split_ids and f in onsup else
               "split-offsup" if f in split_ids else "nonsplit")
        p = next(iter(fib_periods[f]))
        eo = next(iter(fib_EO[f])) if len(fib_EO[f]) == 1 else None
        av = next(iter(fib_A[f])) if len(fib_A[f]) == 1 else None
        rows[(cat, f"p={p}", f"EOmodQ={eo}", f"AmodQ4={av}")] += 1
    for k in sorted(rows, key=str):
        print("   ", k, rows[k])
