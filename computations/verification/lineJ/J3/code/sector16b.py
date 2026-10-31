"""[N] (±2,16): structure of the 2-dim invariant blocks carrying c != 0."""
import sys, numpy as np
exec(open('code/sector16.py').read().split("u=np.ones(NS)")[0])
u=np.ones(NS); e0=np.zeros(NS); e0[pos[0]]=1
for c in cl:
    F=ev[:,c]; E=F@F.conj().T
    if len(c)!=2 or abs(np.vdot(u,E@e0))<1e-6: continue
    Bs=[F.conj().T@As[n]@F for n in range(b)]
    # try basis = eigenvectors of B_n for a generic n whose eigenvalues are distinct
    for n0 in range(1,b):
        wv,V=np.linalg.eig(Bs[n0])
        if abs(wv[0]-wv[1])>1e-6: break
    Vi=np.linalg.inv(V); Cs=[Vi@B@V for B in Bs]
    mono=all(min(abs(C[0,1])+abs(C[1,0]),abs(C[0,0])+abs(C[1,1]))<1e-9 for C in Cs)
    print('block, n0',n0,'monomial in eig basis of B_n0:',mono, 'diag?',all(abs(C[0,1])+abs(C[1,0])<1e-9 for C in Cs))
    print('   |B_n| patterns',[ (round(abs(C[0,0]),3),round(abs(C[0,1]),3)) for C in Cs[:6]])
