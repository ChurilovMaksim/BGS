"""Wave 25, task 5 (part 4): gluing-split search at m=20 (sampled).

m=20: D = 2046573816377472 = 128*9*361*841*1681*3481, and there are
NO component split fibers at all (wave25_lifts.py), so any split
fiber must be a gluing split. Search: sample supported global points
(128-component drawn from its 8 supported points, all other
components fully supported), apply relative dihedral shifts to pairs
of components (40x40 per pair, 15 pairs), and look for y' with the
same global multiset but a different Gamma-canon. Every split found
is tested for: C(y) separation, Adj separation, sorted(w) equality
(i.e. whether it is a failing (fiber,w)-class), and S(y) constancy
on the class. Pair-component shifts only (3+ component shifts
missed, as in wave 22).
Exact integers for all reported statistics (Python ints on reps).
Repository untouched; no Lean build.
"""
import json
import sys

import numpy as np
import sympy as sp

sys.path.insert(0, ".")
from wave16_d1a_targeted import (Dm, snf_kernel, torsion_data,
                                 comp_supported, global_supported,
                                 gamma_perms, lex_canon, group_ids)

m = 20
D = Dm(m)
fac = sp.factorint(D)
qs = [p ** e for p, e in fac.items()]
print(f"m={m} D={D} prime powers={qs}", flush=True)
assert D == 2046573816377472

Z, Qmod = torsion_data(m, D)
perms = gamma_perms(m)
print(f"|V4|={len(Z)} perms={len(perms)}", flush=True)
assert len(perms) == 40

K = {}
for q in qs:
    dq = D // q
    K[q] = (dq * pow(dq % q, -1, q)) % D

comp = {}
for q in qs:
    pts = snf_kernel(m, q)
    assert len(pts) == q
    sup = comp_supported(pts, Z, Qmod, q)
    comp[q] = {"pts": pts, "sup": sup}
    print(f"  q={q}: pts={q} comp_supp={int(sup.sum())}", flush=True)

rng = np.random.default_rng(2501)
N = 4000
samp = {}
for q in qs:
    sup_pts = comp[q]["pts"][comp[q]["sup"]]
    if len(sup_pts) == q:
        sel = rng.integers(0, q, size=N)
        samp[q] = comp[q]["pts"][sel]
    else:
        sel = rng.integers(0, len(sup_pts), size=N)
        samp[q] = sup_pts[sel]
        print(f"  q={q}: sampling from {len(sup_pts)} supported points",
              flush=True)
Y = np.zeros((N, m), dtype=np.int64)
for q in qs:
    Y = (Y + K[q] * samp[q]) % D
assert bool(global_supported(Y, Z, Qmod, D).all())
print(f"sampled {N} supported global points", flush=True)

pairs = [(qs[i], qs[j]) for i in range(len(qs)) for j in range(i + 1, len(qs))]
print(f"component pairs: {len(pairs)}", flush=True)


def stats_py(y):
    y = [int(v) for v in y]
    hv = [6 * y[i] - y[(i - 1) % m] - y[(i + 1) % m] for i in range(m)]
    assert all(v % D == 0 for v in hv), "Hy not divisible by D"
    w = [v // D for v in hv]
    S = sum(y[i] * w[i] for i in range(m))
    A = sum(y[i] * y[(i + 1) % m] for i in range(m))
    C = sum(y[i] * y[(i + 1) % m] * abs(y[i] - y[(i + 1) % m])
            for i in range(m))
    Adj = tuple(sorted(tuple(sorted((y[i], y[(i + 1) % m])))
                       for i in range(m)))
    return {"S": S, "A": A, "C": C, "sorted_w": sorted(w), "Adj": Adj}


found = {}
n_checks = 0
for yi in range(N):
    y = Y[yi]
    sy = tuple(sorted(y.tolist()))
    cy = tuple(lex_canon(y[None, :], perms)[0].tolist())
    sy_arr = np.array(sy)
    for (q1, q2) in pairs:
        c1 = y % q1
        c2 = y % q2
        g1 = c1[perms]
        g2 = c2[perms]
        d1 = (K[q1] * (g1 - c1)) % D
        d2 = (K[q2] * (g2 - c2)) % D
        cand = (y[None, None, :] + d1[:, None, :] + d2[None, :, :]) % D
        cand = cand.reshape(-1, m)
        n_checks += len(cand)
        sc = np.sort(cand, axis=1)
        match = (sc == sy_arr).all(axis=1)
        for mi in np.where(match)[0]:
            yp = cand[mi]
            if (yp == y).all():
                continue
            cp = tuple(lex_canon(yp[None, :], perms)[0].tolist())
            if cp == cy:
                continue
            key = (sy, cp)
            if key in found:
                continue
            st_y, st_yp = stats_py(y), stats_py(yp)
            sup_yp = bool(global_supported(yp[None, :], Z, Qmod, D)[0])
            found[key] = {
                "y": y.tolist(), "yp": yp.tolist(),
                "pair": [int(q1), int(q2)],
                "yp_supported": sup_yp,
                "same_sorted_w": st_y["sorted_w"] == st_yp["sorted_w"],
                "S_equal": st_y["S"] == st_yp["S"],
                "A_equal": st_y["A"] == st_yp["A"],
                "C_differs": st_y["C"] != st_yp["C"],
                "Adj_differs": st_y["Adj"] != st_yp["Adj"],
                "S_y": st_y["S"], "S_yp": st_yp["S"],
                "C_y": st_y["C"], "C_yp": st_yp["C"],
            }
            print(f"  GLUING SPLIT sample={yi} pair=({q1},{q2}) "
                  f"same_w={st_y['sorted_w'] == st_yp['sorted_w']} "
                  f"S_eq={st_y['S'] == st_yp['S']} "
                  f"C_diff={st_y['C'] != st_yp['C']} "
                  f"Adj_diff={st_y['Adj'] != st_yp['Adj']} "
                  f"yp_sup={sup_yp}", flush=True)
    if (yi + 1) % 500 == 0:
        print(f"  ... {yi + 1}/{N} sampled, checks={n_checks}, "
              f"gluing splits found={len(found)}", flush=True)

n_same_w = sum(1 for r in found.values() if r["same_sorted_w"])
n_s_eq = sum(1 for r in found.values() if r["S_equal"])
n_c_diff = sum(1 for r in found.values() if r["C_differs"])
n_adj_diff = sum(1 for r in found.values() if r["Adj_differs"])
print(f"DONE: checks={n_checks} gluing splits found={len(found)} "
      f"same_sorted_w={n_same_w} S_equal={n_s_eq} "
      f"C_differs={n_c_diff}/{len(found)} "
      f"Adj_differs={n_adj_diff}/{len(found)}", flush=True)

with open("/home/hatch/workspace/bgs-breakthrough/methods/"
          "wave25_glue20.json", "w") as fh:
    json.dump({"D": int(D), "n_sampled": N, "n_checks": int(n_checks),
               "n_gluing_splits": len(found),
               "n_same_sorted_w": n_same_w,
               "n_S_equal": n_s_eq,
               "n_C_differs": n_c_diff,
               "n_Adj_differs": n_adj_diff,
               "splits": list(found.values())}, fh, indent=1)
print("wrote wave25_glue20.json", flush=True)
