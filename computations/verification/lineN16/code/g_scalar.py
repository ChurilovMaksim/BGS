"""N16 (1) [N, exact up to binary64]: the SCALAR collision prefactor with carries |e|<=E, for fixed window length n:
  S_n^(E) = sum over letter-pair sequences with v = (1,-6,1)*e, |e_t|<=E, e supported in the window (start/end state (0,0)) of psi N.. Y N..^* psi^*
S_n^(0) = i.i.d. value psi K^n(Phi Phi^*) psi^*;  S_n^(15) = torus (Bohr) mean exactly (|e|<=15 is the full alphabet, N15 [P]).
Tests the N15 question directly: does the prefactor S_n^(E)/S_n^(0) converge as E grows (the N15 'share' was a proxy)?  usage: g_scalar.py E nmax"""
import sys, json, time, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N14/code'); import fastops as F
A=F.A; D=F.D; K=F.K; NS=list(A.NS); c=A.COEF0; s=F.s
E=int(sys.argv[1]); NM=int(sys.argv[2])
blocks={}
for k,ib,jb,B in zip(F.BK,F.BI,F.BJ,F.BB): blocks.setdefault(int(k),[]).append((int(ib),int(jb),c[k]/s*B))
def NYN(k1,k2,Y):
    T=np.zeros((D,D),complex)
    for ib,jb,B in blocks[k1]: T[ib*K:(ib+1)*K,:]+=B@Y[jb*K:(jb+1)*K,:]
    Z=np.zeros((D,D),complex)
    for ib,jb,B in blocks[k2]: Z[:,ib*K:(ib+1)*K]+=T[:,jb*K:(jb+1)*K]@B.conj().T
    return Z
def Tv(v,Y):
    Z=np.zeros((D,D),complex)
    for k,n in enumerate(NS):
        if (n-v) in NS: Z+=NYN(k,NS.index(n-v),Y)
    return Z
es=range(-E,E+1)
Ys={(0,0):np.outer(F.Phi,F.Phi.conj())}; out=[]; t0=time.time()
for n in range(1,NM+1):
    new={}
    for (a,b),Y in Ys.items():
        for e in es:
            v=e-6*a+b
            if abs(v)>60: continue
            # prune states that cannot return to (0,0) within the remaining NM-n steps is not needed for correctness
            Z=Tv(v,Y); new[(e,a)]=new.get((e,a),0)+Z
    Ys=new
    val=float(np.real(F.psi@Ys[(0,0)]@F.psi.conj())) if (0,0) in Ys else 0.0
    out.append(val); print(E,n,'%.6e'%val,len(Ys),round(time.time()-t0,1),flush=True)
json.dump(dict(E=E,S=out),open(f'/workspace/bgs-lineN/N16/logs/g_scalar_E{E}_n{NM}.json','w'))
