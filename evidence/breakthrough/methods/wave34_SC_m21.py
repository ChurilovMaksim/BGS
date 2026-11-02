import sys, math
sys.path.insert(0, ".")
import numpy as np, sympy as sp
from wave16_d1a_targeted import Dm, snf_kernel, torsion_data, comp_supported, gamma_perms, lex_canon, group_ids
def vp(n,p):
    c=0
    while n%p==0: n//=p; c+=1
    return c
def census(m, cap=400000):
    D=Dm(m); fac=sp.factorint(D); qs=sorted(p**e for p,e in fac.items())
    Z,Qmod=torsion_data(m,D); perms=gamma_perms(m)
    print(f"== m={m} D={D} qs={qs}", flush=True)
    tot=0
    for q in qs:
        if q>cap: print(f"   q={q}: SKIP", flush=True); continue
        pts=snf_kernel(m,q); fib=group_ids(np.sort(pts,axis=1)); canon=lex_canon(pts,perms,chunk=500); gam=group_ids(canon)
        n_fib=int(fib.max())+1; gf=np.empty(int(gam.max())+1,dtype=np.int64); gf[gam]=fib; opf=np.bincount(gf,minlength=n_fib)
        sup=comp_supported(pts,Z,Qmod,q)
        onsup=[]
        for f in np.where(opf>1)[0]:
            idx=np.where(fib==f)[0]
            if int(sup[idx].sum())==len(idx):
                p=list(sp.factorint(q).keys())[0]
                depths=set(vp(math.gcd(int(np.gcd.reduce(s)),q),p) for s in pts[idx])
                onsup.append((int(len(idx)), int(len(set(gam[idx].tolist()))), sorted(depths)))
        s=sum(sz*sz for sz,_,_ in onsup); tot+=s
        print(f"   q={q}: fibers={n_fib} supp={int(sup.sum())} onsup={onsup} sum_sq={s}", flush=True)
    print(f"   TOTAL sum_sq={tot} m4={m**4} m5={m**5} slack5={m**5/max(tot,1):.1f}x", flush=True)
census(21)
census(63)
