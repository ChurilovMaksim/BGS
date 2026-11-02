import sys, math
sys.path.insert(0, ".")
import numpy as np, sympy as sp
from wave16_d1a_targeted import Dm, snf_kernel, torsion_data, comp_supported, gamma_perms, lex_canon, group_ids

def period(seq):
    m=len(seq)
    for t in range(1,m+1):
        if m%t==0 and all(seq[i]==seq[i%t] for i in range(m)): return t
    return m

def inspect(m,q):
    D=Dm(m); Z,Qmod=torsion_data(m,D); perms=gamma_perms(m)
    pts=snf_kernel(m,q); fib=group_ids(np.sort(pts,axis=1)); canon=lex_canon(pts,perms); gam=group_ids(canon)
    n_fib=int(fib.max())+1; gf=np.empty(int(gam.max())+1,dtype=np.int64); gf[gam]=fib; opf=np.bincount(gf,minlength=n_fib)
    sup=comp_supported(pts,Z,Qmod,q)
    print(f"== m={m} q={q} supp_total={int(sup.sum())}", flush=True)
    for f in np.where(opf>1)[0]:
        idx=np.where(fib==f)[0]
        if int(sup[idx].sum())!=len(idx): continue
        seqs=pts[idx]
        gcds=[math.gcd(int(np.gcd.reduce(s)),q) for s in seqs[:6]]
        pers=sorted(set(period(s) for s in seqs))
        # distinct values count in first seq, and mod p^(e-1) pattern: reduce seq mod q//p
        p=None
        for pp in sp.factorint(q): p=pp
        red = np.sort(seqs % (q//p), axis=1)
        nred = len(set(map(tuple, red.tolist())))
        print(f"  fiber size={len(idx)} orbits={len(set(gam[idx].tolist()))} orbit_sizes={sorted(np.bincount(gam[idx]).tolist())} periods={pers} gcds_sample={gcds} n_distinct_mod_q_over_p={nred}", flush=True)
        print(f"    example seq: {seqs[0].tolist()}", flush=True)

inspect(12,81); inspect(30,625); inspect(36,729); inspect(32,8192)
