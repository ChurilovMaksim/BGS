import sys, math
sys.path.insert(0, ".")
import numpy as np, sympy as sp
from wave16_d1a_targeted import Dm, snf_kernel, torsion_data, comp_supported, gamma_perms, lex_canon, group_ids
m,q=30,923521
D=Dm(m); Z,Qmod=torsion_data(m,D); perms=gamma_perms(m)
pts=snf_kernel(m,q); print("pts", pts.shape, flush=True)
fib=group_ids(np.sort(pts,axis=1)); print("fibers done", int(fib.max())+1, flush=True)
canon=lex_canon(pts,perms,chunk=500); gam=group_ids(canon); print("orbits done", int(gam.max())+1, flush=True)
n_fib=int(fib.max())+1; gf=np.empty(int(gam.max())+1,dtype=np.int64); gf[gam]=fib; opf=np.bincount(gf,minlength=n_fib)
sup=comp_supported(pts,Z,Qmod,q); print("supp", int(sup.sum()), flush=True)
onsup=[]
for f in np.where(opf>1)[0]:
    idx=np.where(fib==f)[0]
    if int(sup[idx].sum())==len(idx):
        onsup.append((int(len(idx)), int(len(set(gam[idx].tolist())))))
print(f"m={m} q={q}: onsup_splits={onsup} sum_sq={sum(sz*sz for sz,_ in onsup)} m2={m*m} m4={m**4}", flush=True)
