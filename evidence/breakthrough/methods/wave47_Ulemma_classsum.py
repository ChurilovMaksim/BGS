"""Wave 47, task 6: verify the class-sum proof of the 2-part U-lemma.
For each on-support split fiber at level m (Q=2^(2j+3)), with class sums
S_r = sum_{k<p/4} y_{4k+r}, check:
 (R) class-sum recurrence S_2 = 6*S_1 - S_0, S_3 = 35*S_1 - 6*S_0 (mod Q);
 (D) S_0 = 0 mod Q/32 and S_1 = 3*S_0 mod Q/4 (proved facts);
 (N) nonmax p: U = 0 mod Q/4 for all 16 patterns (PROVED in note);
 (M) max p: tau0 = S_0/(Q/32) even, k = (S_1-3*S_0)/(Q/4) odd,
     and U = (Q/4)*pat_z mod Q/2 for all 16 patterns (CSL-max).
Usage: python3 wave47_Ulemma_classsum.py [m]  (default 32)
"""
import sys; sys.path.insert(0, ".")
import numpy as np
from collections import defaultdict
from wave16_d1a_targeted import Dm, torsion_data, group_ids
from wave36_2part import snf_kernel_i32, orbit_canon
from wave38_helpers import period_of

m = int(sys.argv[1]) if len(sys.argv) > 1 else 32
q = 2 ** (2 * (m.bit_length() - 1) + 3)
D = Dm(m)
Z, Qmod = torsion_data(m, D)
pats = [tuple(int(Z[r, i]) for i in range(4)) for r in range(Z.shape[0])]
pat_z = [0 if len({v % 4 for v in pat}) == 1 else 1 for pat in pats]
pts = snf_kernel_i32(m, q)
Qm = np.array([qq % q for qq in Qmod], dtype=np.int64)
sup = ((2 * Qm[None, :] - pts.astype(np.int64) @ Z.astype(np.int64).T) % q == 0).all(axis=1)
fib = group_ids(np.sort(pts, axis=1))
ba, bb = orbit_canon(pts[:, :2].astype(np.int64), m, q)
gam = group_ids(np.stack([ba, bb], axis=1))
fib_orbits = defaultdict(set)
for i in range(len(pts)): fib_orbits[int(fib[i])].add(int(gam[i]))
split_ids = {f for f in fib_orbits if len(fib_orbits[f]) > 1}
onsup = {int(fib[i]) for i in range(len(pts)) if sup[i]}
N = m
n_max = n_nonmax = n_bad = 0
for f in sorted(split_ids & onsup):
    idx = [i for i in range(len(pts)) if int(fib[i]) == f]
    y = pts[idx[0]].astype(np.int64)
    p = period_of(y); o = len(fib_orbits[f])
    yper = y[:p]; K = p // 4
    S = [int(np.sum(yper[r::4])) % q for r in range(4)]
    assert (S[2] - (6*S[1] - S[0])) % q == 0, "recurrence S2 fails"
    assert (S[3] - (35*S[1] - 6*S[0])) % q == 0, "recurrence S3 fails"
    assert S[0] % (q // 32) == 0, "S0 mod Q/32 fails"
    assert (S[1] - 3*S[0]) % (q // 4) == 0, "S1=3S0 mod Q/4 fails"
    U = []
    for pat in pats:
        zfull = np.array([pat[i % 4] for i in range(p)], dtype=np.int64)
        U.append(int(np.sum(yper * zfull)) % q)
    if p == N // 4:
        tau0 = (S[0] // (q // 32)) % 2
        k = ((S[1] - 3*S[0]) // (q // 4)) % 2
        ok = (tau0 == 0 and k == 1 and
              all(U[r] % (q // 2) == (q // 4) * pat_z[r] for r in range(16)))
        n_max += 1
        print(f"MAX o={o} p={p} S0/(Q/32)={S[0]//(q//32)} tau0={tau0} k={k} ok={ok}")
    else:
        ok = all(u % (q // 4) == 0 for u in U)
        n_nonmax += 1
        print(f"nonmax o={o} p={p} ok={ok}")
    if not ok: n_bad += 1
print(f"TOTAL m={m}: max={n_max} nonmax={n_nonmax} bad={n_bad}")
