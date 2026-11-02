"""Wave 32, task 3: RB3 check script (reproduces wave32_RB3.md).

Definitions (wave-16 code): kernel points mod q = Fix sequences of
y_{i+1} = 6 y_i - y_{i-1} (SNF kernel, exactly q points when q | D_m);
fiber = equal sorted multiset; support = torsion criterion
(2 Q(z) - y.z == 0 mod q for all z in Z); supported fiber = fiber
containing >= 1 supported point. Here q = q2 = 2-part of D_m.
"""
import sys
sys.path.insert(0, ".")
from wave16_d1a_targeted import (Dm, snf_kernel, torsion_data,
                                 comp_supported, group_ids)
import numpy as np, sympy as sp


def analyze(m):
    D = Dm(m)
    q2 = 2 ** sp.factorint(D)[2]
    Z, Qmod = torsion_data(m, D)
    pts = snf_kernel(m, q2)
    assert len(pts) == q2
    fib = group_ids(np.sort(pts, axis=1))
    sup = comp_supported(pts, Z, Qmod, q2)
    sizes, partial = [], 0
    for f in range(int(fib.max()) + 1):
        idx = np.where(fib == f)[0]
        s = int(sup[idx].sum())
        if s > 0:
            sizes.append(int(len(idx)))
        if 0 < s < len(idx):
            partial += 1
    return q2, len(Z), int(sup.sum()), sizes, partial


if __name__ == "__main__":
    # Sweep m = 3..128: count bound, supp_pts = q2/|Z|, no partials,
    # max size by v2(m).
    max_by_v2 = {}
    for m in range(3, 129):
        q2, nZ, nsup, sizes, partial = analyze(m)
        assert len(sizes) <= q2 <= 8 * m * m, (m, len(sizes), q2)
        assert nsup == q2 // nZ, (m, nsup, q2, nZ)
        assert partial == 0, (m, partial)
        v2 = sp.factorint(m).get(2, 0)
        max_by_v2[v2] = max(max_by_v2.get(v2, 0), max(sizes))
    print("ALL CHECKS PASS")
    print("max supported 2-fiber size by v2(m):",
          dict(sorted(max_by_v2.items())))
    # Explicit m=16 counterexample fiber (size 8, single orbit).
    m = 16
    D = Dm(m)
    q2 = 2 ** sp.factorint(D)[2]
    Z, Qmod = torsion_data(m, D)
    pts = snf_kernel(m, q2)
    fib = group_ids(np.sort(pts, axis=1))
    sup = comp_supported(pts, Z, Qmod, q2)
    for f in range(int(fib.max()) + 1):
        idx = np.where(fib == f)[0]
        if len(idx) == 8 and int(sup[idx].sum()) == 8:
            print("m=16 size-8 supported fiber, sorted multiset:",
                  sorted(pts[idx[0]].tolist()))
            for j in idx:
                print("   ", pts[j].tolist())
            break
