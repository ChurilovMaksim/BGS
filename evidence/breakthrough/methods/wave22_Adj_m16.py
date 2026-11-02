"""Wave 22, task 4 (part 2): Adj separator test at m=16 (sampling).

m=16: D = 1773462177792 = 2048 * 9 * 289 * 332929. A wave-18-style
Gamma-normalized census would need ~1.7e11 representatives, so it is
infeasible; this script does two feasible things instead:
  (a) lifts of the 10 component split fibers at q=2048 (all
      off-support, per component analysis) with other components fixed
      to supported points, and tests Adj separation on the lifted
      global split fibers;
  (b) a gluing-split search: sample supported global points y, apply
      relative dihedral shifts to pairs of components (32x32 per pair),
      and look for y' with the same global multiset but a different
      Gamma-canon (a gluing split). Every gluing split found is tested
      for Adj separation.
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

m = 16
D = Dm(m)
fac = sp.factorint(D)
qs = [p ** e for p, e in fac.items()]
print(f"m={m} D={D} prime powers={qs}", flush=True)
assert D == 1773462177792 and sorted(qs) == [9, 289, 2048, 332929]

Z, Qmod = torsion_data(m, D)
perms = gamma_perms(m)
print(f"|V4|={len(Z)} perms={len(perms)}", flush=True)
assert len(perms) == 32

K = {}
for q in qs:
    dq = D // q
    K[q] = (dq * pow(dq % q, -1, q)) % D

comp = {}
for q in qs:
    pts = snf_kernel(m, q)
    assert len(pts) == q
    fib = group_ids(np.sort(pts, axis=1))
    sup = comp_supported(pts, Z, Qmod, q)
    canon = lex_canon(pts, perms)
    gam = group_ids(canon)
    comp[q] = {"pts": pts, "fib": fib, "sup": sup, "gam": gam}
    n_fib = int(fib.max()) + 1
    # support fiber-constancy: each fiber all-supported or all-unsupported
    const = True
    for f in range(n_fib):
        s = sup[fib == f]
        if s.any() and not s.all():
            const = False
            break
    gam_fiber = np.empty(int(gam.max()) + 1, dtype=np.int64)
    gam_fiber[gam] = fib
    opf = np.bincount(gam_fiber, minlength=n_fib)
    n_split = int((opf > 1).sum())
    print(f"  q={q}: pts={len(pts)} fibers={n_fib} split={n_split} "
          f"supp={int(sup.sum())} support_fiber_constant={const}", flush=True)


def adj_of(y):
    return tuple(sorted(tuple(sorted((int(y[i]), int(y[(i + 1) % m]))))
                        for i in range(m)))


# ---- (a) lifts of component splits at q=2048 ----
fixed = {}
for q in qs:
    sup = comp[q]["sup"]
    fixed[q] = comp[q]["pts"][np.where(sup)[0][0]] if sup.any() \
        else comp[q]["pts"][0]
print("fixed supported points chosen (q=2048 has supported points: "
      f"{bool(comp[2048]['sup'].any())})", flush=True)

lift_results = []
q0 = 2048
pts, fib, gam = comp[q0]["pts"], comp[q0]["fib"], comp[q0]["gam"]
gam_fiber = np.empty(int(gam.max()) + 1, dtype=np.int64)
gam_fiber[gam] = fib
opf = np.bincount(gam_fiber, minlength=int(fib.max()) + 1)
for f in np.where(opf > 1)[0]:
    idx = np.where(fib == f)[0]
    lifts = {}
    for q in qs:
        lifts[q] = pts[idx] if q == q0 else np.tile(fixed[q], (len(idx), 1))
    glob = np.zeros((len(idx), m), dtype=np.int64)
    for q in qs:
        glob = (glob + K[q] * lifts[q]) % D
    gfib = group_ids(np.sort(glob, axis=1))
    assert len(set(gfib.tolist())) == 1, "lift broke the fiber!"
    gcan = lex_canon(glob, perms)
    ggam = group_ids(gcan)
    gsup = global_supported(glob, Z, Qmod, D)
    n_sup = int(gsup.sum())
    pat = "FULL" if n_sup == len(idx) else "PARTIAL" if n_sup > 0 else "EMPTY"
    # Adj per global orbit
    adj_vals = []
    for g in sorted(set(ggam.tolist())):
        j = np.where(ggam == g)[0][0]
        adj_vals.append(adj_of(glob[j]))
    ok = len(set(adj_vals)) == len(adj_vals)
    lift_results.append({"q": q0, "fiber": int(f), "size": int(len(idx)),
                         "n_global_orbits": int(len(adj_vals)),
                         "n_supp": n_sup, "pattern": pat,
                         "adj_separates": bool(ok)})
    print(f"  LIFT q={q0} fiber={f} size={len(idx)} "
          f"orbits={len(adj_vals)} supp={n_sup} -> {pat} adj_ok={ok}",
          flush=True)

# ---- (b) gluing-split search on sampled supported points ----
rng = np.random.default_rng(22)
# sample components: 2048-component from supported points only
sup2048 = comp[2048]["pts"][comp[2048]["sup"]]
print(f"supported 2048-points: {len(sup2048)}", flush=True)

N = 2000
samp = {}
for q in qs:
    if q == 2048:
        sel = rng.integers(0, len(sup2048), size=N)
        samp[q] = sup2048[sel]
    else:
        sel = rng.integers(0, q, size=N)
        samp[q] = comp[q]["pts"][sel]
Y = np.zeros((N, m), dtype=np.int64)
for q in qs:
    Y = (Y + K[q] * samp[q]) % D
# sanity: all sampled points supported
assert bool(global_supported(Y, Z, Qmod, D).all())
print(f"sampled {N} supported global points", flush=True)

pairs = [(qs[i], qs[j]) for i in range(len(qs)) for j in range(i + 1, len(qs))]
print(f"component pairs: {pairs}", flush=True)

found = {}  # (fiber_tuple, canon_tuple) -> record
n_checks = 0
for yi in range(N):
    y = Y[yi]
    sy = tuple(sorted(y.tolist()))
    cy = tuple(lex_canon(y[None, :], perms)[0].tolist())
    for (q1, q2) in pairs:
        c1 = y % q1
        c2 = y % q2
        # 32x32 shifted candidates, vectorized
        g1 = c1[perms]          # (32, m)
        g2 = c2[perms]          # (32, m)
        # y' = y + K1*(g1-c1) + K2*(g2-c2) mod D, over all (a,b)
        d1 = (K[q1] * (g1 - c1)) % D    # (32, m)
        d2 = (K[q2] * (g2 - c2)) % D    # (32, m)
        cand = (y[None, None, :] + d1[:, None, :] + d2[None, :, :]) % D
        cand = cand.reshape(-1, m)
        n_checks += len(cand)
        sc = np.sort(cand, axis=1)
        match = (sc == np.array(sy)).all(axis=1)
        for mi in np.where(match)[0]:
            yp = cand[mi]
            if (yp == y).all():
                continue
            cp = tuple(lex_canon(yp[None, :], perms)[0].tolist())
            if cp == cy:
                continue  # same orbit, not a split
            key = (sy, cp)
            if key in found:
                continue
            ay, ayp = adj_of(y), adj_of(yp)
            sup_yp = bool(global_supported(yp[None, :], Z, Qmod, D)[0])
            found[key] = {
                "y": y.tolist(), "yp": yp.tolist(),
                "adj_y": [list(p) for p in ay],
                "adj_yp": [list(p) for p in ayp],
                "adj_differs": ay != ayp,
                "yp_supported": sup_yp,
                "pair": [int(q1), int(q2)],
            }
            print(f"  GLUING SPLIT sample={yi} pair=({q1},{q2}) "
                  f"adj_differs={ay != ayp} yp_supported={sup_yp}", flush=True)
    if (yi + 1) % 500 == 0:
        print(f"  ... {yi + 1}/{N} sampled, checks={n_checks}, "
              f"gluing splits found={len(found)}", flush=True)

n_adj_ok = sum(1 for r in found.values() if r["adj_differs"])
print(f"DONE: checks={n_checks} gluing splits found={len(found)} "
      f"Adj separates {n_adj_ok}/{len(found)}", flush=True)

with open("/home/hatch/workspace/bgs-breakthrough/methods/"
          "wave22_Adj_m16.json", "w") as fh:
    json.dump({"D": int(D), "lifts": lift_results,
               "n_sampled": N, "n_checks": int(n_checks),
               "gluing_splits": list(found.values())}, fh, indent=1)
print("wrote wave22_Adj_m16.json", flush=True)
