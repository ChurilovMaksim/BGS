import sys
sys.path.insert(0, ".")
import numpy as np, sympy as sp
from wave16_d1a_targeted import Dm, snf_kernel, torsion_data, comp_supported, gamma_perms, lex_canon, group_ids
def census1(m,q):
    D=Dm(m); Z,Qmod=torsion_data(m,D); perms=gamma_perms(m)
    pts=snf_kernel(m,q); fib=group_ids(np.sort(pts,axis=1)); canon=lex_canon(pts,perms,chunk=500); gam=group_ids(canon)
    n_fib=int(fib.max())+1; gf=np.empty(int(gam.max())+1,dtype=np.int64); gf[gam]=fib; opf=np.bincount(gf,minlength=n_fib)
    sup=comp_supported(pts,Z,Qmod,q)
    onsup=[]
    for f in np.where(opf>1)[0]:
        idx=np.where(fib==f)[0]
        if int(sup[idx].sum())==len(idx):
            onsup.append((int(len(idx)), int(len(set(gam[idx].tolist())))))
    print(f"m={m} q={q} (p|m={q and (list(sp.factorint(q).keys())[0] in [d for d in range(2,m+1) if m%d==0])}): fibers={n_fib} supp={int(sup.sum())} onsup_splits={onsup}", flush=True)
census1(21,2401)   # p=7|21, e=4: split expected iff p|m+e>=4 sufficient
census1(42,2401)   # p=7|42, e=4
census1(14,28561)  # p=13, 13 not | 14, e=4: no split expected by p|m rule
