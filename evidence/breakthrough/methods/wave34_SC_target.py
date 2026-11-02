import sys, math
sys.path.insert(0, ".")
import numpy as np, sympy as sp
from wave16_d1a_targeted import Dm, snf_kernel, torsion_data, comp_supported, gamma_perms, lex_canon, group_ids
def vp(n,p):
    c=0
    while n%p==0: n//=p; c+=1
    return c
def census1(m,q):
    D=Dm(m); Z,Qmod=torsion_data(m,D); perms=gamma_perms(m)
    pts=snf_kernel(m,q); fib=group_ids(np.sort(pts,axis=1)); canon=lex_canon(pts,perms,chunk=500); gam=group_ids(canon)
    n_fib=int(fib.max())+1; gf=np.empty(int(gam.max())+1,dtype=np.int64); gf[gam]=fib; opf=np.bincount(gf,minlength=n_fib)
    sup=comp_supported(pts,Z,Qmod,q)
    onsup=[]
    for f in np.where(opf>1)[0]:
        idx=np.where(fib==f)[0]
        if int(sup[idx].sum())==len(idx):
            p=list(sp.factorint(q).keys())[0]
            depths=[vp(math.gcd(int(np.gcd.reduce(s)),q),p) for s in pts[idx]]
            onsup.append((int(len(idx)), int(len(set(gam[idx].tolist()))), min(depths), max(depths)))
    print(f"m={m} q={q}: fibers={n_fib} supp={int(sup.sum())} onsup_splits(size,orbits,mindepth,maxdepth)={onsup} sum_sq={sum(sz*sz for sz,_,_,_ in onsup)} m2={m*m}", flush=True)
census1(108,6561)
census1(150,15625)
