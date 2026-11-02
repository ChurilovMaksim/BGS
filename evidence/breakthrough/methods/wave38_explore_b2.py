"""Wave 38 (b) mechanism: U values, U mod Q, class sums S_r for max/non-max."""
import sys
sys.path.insert(0, ".")
import numpy as np
from collections import defaultdict
from wave16_d1a_targeted import Dm, torsion_data, group_ids
from wave36_2part import snf_kernel_i32, orbit_canon
from wave38_helpers import period_of


def z_patterns(m):
    D = Dm(m)
    Z, Qmod = torsion_data(m, D)
    pats = []
    for r in range(Z.shape[0]):
        pat = tuple(int(Z[r, i]) for i in range(4))
        assert all(int(Z[r, i]) == pat[i % 4] for i in range(m))
        pats.append(pat)
    return pats


for m, q in [(32, 8192), (64, 32768)]:
    N = m
    pats = z_patterns(m)
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
    for f in sorted(split_ids & onsup)[:3]:
        idx = [i for i in range(len(pts)) if int(fib[i]) == f]
        y = pts[idx[0]].astype(np.int64)
        p = period_of(y)
        is_max = (p == N // 4)
        print(f"  fiber{f} o={len(fib_orbits[f])} p={p} {'MAX' if is_max else 'nonmax'}")
        # class sums S_r over one period
        Sr = [int(np.sum(y[r:p:4])) for r in range(4)]
        print(f"    S_r={Sr}  S_r mod Q={[s % q for s in Sr]}  S_r/(Q/4)={[s/(q//4) for s in Sr]}")
        for ri, pat in enumerate(pats[:4]):
            zfull = np.array([pat[i % 4] for i in range(p)], dtype=np.int64)
            U = int(np.sum(y[:p] * zfull))
            print(f"    pat{ri}={pat} U={U} UmodQ={U % q} U'={(U*N//(q*p)) % 2} "
                  f"(U*N/(q*p)={U*N//(q*p)})")
