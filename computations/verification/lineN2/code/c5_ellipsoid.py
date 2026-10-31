"""N2 (C5) [N]: ellipsoidal-norm upper estimate for the UNCONSTRAINED JSR of {L_tau: tau in R/Z} (V, sector 0 lift):
P = sum_{j<J} Lam^{-2j} (L_{1/2}^j)^* L_{1/2}^j (+ iterated averaging over tau grid), then
max_tau ||P^{1/2} L_tau P^{-1/2}|| on a fine tau grid.  usage: c5_ellipsoid.py K0 r K beta N0 Lam J NT iters"""
import sys, json, numpy as np, scipy.linalg as sl
sys.path.insert(0,'/workspace/bgs-lineF/code')
from lift import ops, wk1
K0=int(sys.argv[1]); r=float(sys.argv[2]); K=int(sys.argv[3]); beta=float(sys.argv[4]); N0=int(sys.argv[5])
Lam=float(sys.argv[6]); J=int(sys.argv[7]); NT=int(sys.argv[8]); iters=int(sys.argv[9])
Bn={}
for n in range(-N0,N0+1):
    V,E=ops(lambda m,n=n: 1.0 if m==n else 0.0, N0,K0,r,r,K,beta=beta); Bn[n]=V
ns=np.array(sorted(Bn)); Bst=np.stack([Bn[n] for n in ns]); w0=wk1(2.0,0); w=np.array([w0(int(n)) for n in ns])
def L(t): return np.tensordot(w*np.exp(2j*np.pi*ns*t),Bst,axes=1)
d=Bst.shape[1]; Lh=L(0.5)
P=np.zeros((d,d),dtype=complex); M=np.eye(d,dtype=complex)
for j in range(J): P+=M.conj().T@M/Lam**(2*j); M=Lh@M
taus=np.arange(NT)/NT; Ls=[L(t) for t in taus]
def score(P):
    H=sl.sqrtm(P); Hi=np.linalg.inv(H)
    v=[float(np.linalg.norm(H@Lt@Hi,2)) for Lt in Ls]; return max(v), taus[int(np.argmax(v))]
hist=[score(P)]; print(json.dumps(dict(it=0,max=hist[-1][0],arg=hist[-1][1])),flush=True)
for it in range(iters):
    # P <- I + Lam^{-2} * max-ish combination: use soft-max weights over tau of L^*PL
    Q=[Lt.conj().T@P@Lt for Lt in Ls]; nr=np.array([np.linalg.norm(q,2) for q in Q]); wts=np.exp(20*(nr/nr.max()-1)); wts/=wts.sum()
    P=np.eye(d)+sum(wt*q for wt,q in zip(wts,Q))/Lam**2*1.0 + 0.0*P
    P=(P+P.conj().T)/2; hist.append(score(P)); print(json.dumps(dict(it=it+1,max=hist[-1][0],arg=hist[-1][1])),flush=True)
json.dump(dict(Lam=Lam,J=J,NT=NT,hist=hist),open(f'logs/c5_ellipsoid_L{Lam}_J{J}.json','w'))
