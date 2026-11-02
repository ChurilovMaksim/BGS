"""Wave 24, task 4 (follow-up): extension sweeps for orbit-rep pairs (0,2)
and (1,2) of the 81-split fiber. The main sweep tested only reps
(orbs[0], orbs[1]); a mixing fiber witnessed by a different rep pair
would be missed. Same multiset-mod-P filter as wave24_m48_deficit.py
section (b), filter only (no recheck). Repository untouched; no Lean.
"""
import json, sys
import numpy as np
sys.path.insert(0, ".")
from wave16_d1a_targeted import Dm, snf_kernel, sample_kernel_points

m = 48
D = Dm(m)
QS = [25, 49, 81, 121, 289, 2048, 9409, 332929, 1329409, 188485441]
P1, P2 = 1_000_000_007, 998244353
KqP = {}
for q in QS:
    dq = D // q
    KqP[q] = (((dq * pow(dq % q, -1, q)) % D) % P1,
              ((dq * pow(dq % q, -1, q)) % D) % P2)
d81 = np.load("wave24_comp_81.npz")
K81, fib81, gam81 = d81["K"], d81["fib"], d81["gam"]
d2048 = np.load("wave24_comp_2048.npz")
K2048, fib2048 = d2048["K"], d2048["fib"]
gf = np.empty(int(gam81.max()) + 1, dtype=np.int64)
gf[gam81] = fib81
opf = np.bincount(gf, minlength=int(fib81.max()) + 1)
split81 = sorted(np.where(opf > 1)[0].tolist())
f81 = split81[0]
idx81 = np.where(fib81 == f81)[0]
gam = gam81[idx81]
orbs = sorted(set(gam.tolist()))
sup2048_fibs = sorted(set(fib2048[d2048["sup"]].tolist()))
other_qs = [q for q in QS if q not in (2048, 81)]
big_sample = sample_kernel_points(m, 188485441, 200000, np.random.default_rng(11))

for (o0, o1) in ((0, 2), (1, 2)):
    a0 = K81[idx81[gam == orbs[o0]][0]]
    a1 = K81[idx81[gam == orbs[o1]][0]]
    survivors = []
    for qt in other_qs:
        T = big_sample if qt == 188485441 else snf_kernel(m, qt)
        nz = ~np.all(T == 0, axis=1)
        Tnz, nz_idx = T[nz], np.where(nz)[0]
        for f2048 in sup2048_fibs:
            p0 = K2048[np.where(fib2048 == f2048)[0][0]]
            for st in range(0, len(Tnz), 20000):
                ch = Tnz[st:st + 20000]
                hit = np.ones(len(ch), dtype=bool)
                for pi, P in enumerate((P1, P2)):
                    if not hit.any():
                        break
                    base = (KqP[2048][pi] * (p0 % P)) % P
                    A0 = (KqP[81][pi] * (a0 % P)) % P
                    A1 = (KqP[81][pi] * (a1 % P)) % P
                    V0 = (base[None, :] + A0[None, :] + (KqP[qt][pi] * (ch % P)) % P) % P
                    V1 = (base[None, :] + A1[None, :] + (KqP[qt][pi] * (ch % P)) % P) % P
                    hit &= np.all(np.sort(V0, axis=1) == np.sort(V1, axis=1), axis=1)
                for h in np.where(hit)[0]:
                    survivors.append({"f2048": int(f2048), "f81": int(f81),
                                      "qt": int(qt), "t_idx": int(nz_idx[st + h])})
        if qt != 188485441:
            del T
        print(f"  rep pair ({o0},{o1}) qt={qt} survivors so far={len(survivors)}",
              flush=True)
    fn = f"wave24_sweep_survivors_{o0}{o1}.json"
    with open(fn, "w") as fh:
        json.dump(survivors, fh)
    print(f"rep pair ({o0},{o1}): TOTAL survivors={len(survivors)} WROTE {fn}", flush=True)
