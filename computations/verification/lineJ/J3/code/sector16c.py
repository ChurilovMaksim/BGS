"""[N] (±2,16): find a monomial basis for each 2-dim c!=0 block (eigenbasis of some word B_w); report phases in units of 1/16 (after
normalising the basis), the c value, and whether entries are 16th roots of unity times {0,1}."""
import sys, numpy as np, itertools, json
exec(open('code/sector16.py').read().split("u=np.ones(NS)")[0])
u=np.ones(NS); e0=np.zeros(NS); e0[pos[0]]=1
out=[]
for c in cl:
    F=ev[:,c]; E=F@F.conj().T; cc=np.vdot(u,E@e0)
    if len(c)!=2 or abs(cc)<1e-6: continue
    Bs=[F.conj().T@As[n]@F for n in range(b)]
    words=[(n,) for n in range(b)]+[(n,k) for n in range(b) for k in range(b)]
    found=None
    for w in words:
        M=np.eye(2,dtype=complex)
        for n in w: M=Bs[n]@M
        wv,V=np.linalg.eig(M)
        if abs(wv[0]-wv[1])<1e-6: continue
        Vi=np.linalg.inv(V); Cs=[Vi@B@V for B in Bs]
        if all(min(abs(C[0,1])+abs(C[1,0]),abs(C[0,0])+abs(C[1,1]))<1e-9 for C in Cs): found=(w,V,Cs); break
    if found is None: print('no monomial basis found'); continue
    w,V,Cs=found
    # rescale basis vector 2 so that a nonzero off-diagonal / entries become unimodular roots
    print('block word',w,'c',np.round(cc,6))
    print('   pattern', ['D' if abs(C[0,1])<1e-9 else 'X' for C in Cs])
    print('   |entries|',sorted(set(round(abs(x),6) for C in Cs for x in C.ravel() if abs(x)>1e-9)))
