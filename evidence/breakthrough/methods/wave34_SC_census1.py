import sys, math
sys.path.insert(0, ".")
import numpy as np, sympy as sp
from wave16_d1a_targeted import Dm, snf_kernel, torsion_data, comp_supported, gamma_perms, lex_canon, group_ids

def census(m, cap=400000):
    D = Dm(m); fac = sp.factorint(D); qs = sorted(p**e for p,e in fac.items())
    Z, Qmod = torsion_data(m, D); perms = gamma_perms(m)
    print(f"== m={m} D={D} qs={qs}", flush=True)
    tot = 0
    for q in qs:
        if q > cap:
            print(f"   q={q}: SKIP", flush=True); continue
        pts = snf_kernel(m, q)
        fib = group_ids(np.sort(pts, axis=1))
        canon = lex_canon(pts, perms)
        gam = group_ids(canon)
        n_fib = int(fib.max())+1
        gam_fiber = np.empty(int(gam.max())+1, dtype=np.int64); gam_fiber[gam]=fib
        opf = np.bincount(gam_fiber, minlength=n_fib)
        sup = comp_supported(pts, Z, Qmod, q)
        onsup=[]
        for f in np.where(opf>1)[0]:
            idx = np.where(fib==f)[0]
            if int(sup[idx].sum())==len(idx):
                onsup.append((int(len(idx)), int(len(set(gam[idx].tolist())))))
        s = sum(sz*sz for sz,_ in onsup)
        tot += s
        print(f"   q={q}: fibers={n_fib} supp={int(sup.sum())} onsup_splits={onsup} sum_sq={s} m2={m*m} m4={m**4}", flush=True)
    print(f"   TOTAL sum_sq={tot} m4={m**4} slack={m**4/max(tot,1):.1f}x", flush=True)

for m in [5,7,11,13,19]:
    census(m)
