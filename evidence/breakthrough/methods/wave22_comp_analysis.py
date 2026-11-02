import sys, json
sys.path.insert(0, ".")
import numpy as np
from wave16_d1a_targeted import (Dm, snf_kernel, torsion_data, comp_supported,
                                 gamma_perms, lex_canon, group_ids)
import sympy as sp

m = 36
D = Dm(m)
fac = sp.factorint(D)
qs = sorted([p**e for p, e in fac.items()])
Z, Qmod = torsion_data(m, D)
perms = gamma_perms(m)
out = {"m": m, "D": D, "qs": qs, "V4": len(Z), "supp_size": D // len(Z), "components": {}}
print(f"== m={m} D={D} qs={qs} |V4|={len(Z)} |supp|={D//len(Z)}", flush=True)
for q in qs:
    pts = snf_kernel(m, q)
    assert len(pts) == q
    fib = group_ids(np.sort(pts, axis=1))
    canon = lex_canon(pts, perms)
    gam = group_ids(canon)
    n_fib = int(fib.max()) + 1
    gam_fiber = np.empty(int(gam.max()) + 1, dtype=np.int64)
    gam_fiber[gam] = fib
    opf = np.bincount(gam_fiber, minlength=n_fib)
    split_fibs = np.where(opf > 1)[0]
    sup = comp_supported(pts, Z, Qmod, q)
    details = []
    for f in split_fibs:
        idx = np.where(fib == f)[0]
        details.append({"fiber": int(f), "size": int(len(idx)),
                        "n_orbits": int(len(set(gam[idx].tolist()))),
                        "n_supp": int(sup[idx].sum()),
                        "orbit_sizes": sorted([int((gam[idx]==g).sum()) for g in set(gam[idx].tolist())])})
    n_full = n_part = n_empty = 0
    for f in range(n_fib):
        idx = np.where(fib == f)[0]
        s = int(sup[idx].sum())
        if s == len(idx): n_full += 1
        elif s == 0: n_empty += 1
        else: n_part += 1
    rec = {"pts": int(len(pts)), "n_fibers": n_fib, "n_split_fibers": int(len(split_fibs)),
           "comp_supp_points": int(sup.sum()), "fibers_full_supp": n_full,
           "fibers_partial_supp": n_part, "fibers_empty_supp": n_empty,
           "split_details": details}
    out["components"][str(q)] = rec
    print(f"   q={q}: pts={len(pts)} fibers={n_fib} split={len(split_fibs)} "
          f"supp_pts={int(sup.sum())} full/partial/empty={n_full}/{n_part}/{n_empty}", flush=True)
    for d in details:
        print(f"      split fiber={d['fiber']} size={d['size']} orbits={d['n_orbits']} "
              f"orbit_sizes={d['orbit_sizes']} supp={d['n_supp']}", flush=True)
with open("wave22_comp_analysis.json", "w") as fh:
    json.dump(out, fh, indent=1, default=str)
print("WROTE wave22_comp_analysis.json")
