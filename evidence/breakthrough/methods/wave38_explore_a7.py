"""Wave 38 (a): verify (a mod 2, b mod 2) == V mod 2, V=(I-M^p)(y0,y_{-1})/Q.

M = [[6,-1],[1,0]] acting on state (y_{i+1}, y_i)? Use state (y_i, y_{i-1}):
M2 = [[6,-1],[1,0]] maps (y_i, y_{i-1}) -> (y_{i+1}, y_i) since
y_{i+1} = 6 y_i - y_{i-1}. Seed for V: (y_0, y_{-1}) = (y_0, y_{p-1}).
a = sum of e over odd i, b = sum over even i (one period), e from e_seq.
"""
import sys
sys.path.insert(0, ".")
import numpy as np
from collections import Counter, defaultdict
from wave16_d1a_targeted import Dm, torsion_data, group_ids
from wave36_2part import snf_kernel_i32, orbit_canon
from wave38_helpers import period_of, e_seq


def mat_pow_mod(M, p):
    # exact integer matrix power (small p, entries grow but p<=64 fine with Python ints)
    R = np.array([[1, 0], [0, 1]], dtype=object)
    B = M.astype(object)
    while p:
        if p & 1:
            R = R @ B
        B = B @ B
        p >>= 1
    return R


M = np.array([[6, -1], [1, 0]], dtype=object)
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
    bad = 0
    for i in range(len(pts)):
        f = int(fib[i])
        cat = ("split-onsup" if f in split_ids and f in onsup else
               "split-offsup" if f in split_ids else
               "nonsplit-onsup" if sup[i] else "nonsplit-offsup")
        y = pts[i].astype(np.int64)
        p = period_of(y)
        if p < 8:
            continue
        e = e_seq(y, q)
        # a = sum e over odd i in [0,p), b = sum over even i
        a = int(np.sum(e[1:p:2])) if p > 1 else 0
        b = int(np.sum(e[0:p:2]))
        # V = (I - M^p)(y0, y_{p-1}) / q  (exact integers)
        Mp = mat_pow_mod(M, p)
        I = np.array([[1, 0], [0, 1]], dtype=object)
        seed = np.array([int(y[0]), int(y[p - 1])], dtype=object)
        w = (I - Mp) @ seed
        assert w[0] % q == 0 and w[1] % q == 0, "period defect not divisible by q"
        V = (int(w[0] // q) % 2, int(w[1] // q) % 2)
        # Note: state convention: M maps (y_i, y_{i-1}) -> (y_{i+1}, y_i);
        # seed (y_0, y_{-1}); V components correspond to (a?, b?) up to order.
        pred = (a % 2, b % 2)
        pred_swap = (b % 2, a % 2)
        ok = (V == pred) or (V == pred_swap)
        if not ok:
            bad += 1
            if bad <= 3:
                print("   MISMATCH", cat, "p", p, "a,b mod2", pred, "V", V)
        rows[(cat, f"p={p}", f"ab={pred}", f"V={V}", f"match={'direct' if V == pred else 'swap' if V == pred_swap else 'NO'}")] += 1
    print("   mismatches:", bad)
    for k in sorted(rows, key=str):
        print("   ", k, rows[k])
