"""N14 (A) [N] scoping: EXACT-collision second moment with phases kept (sesquilinear, not CP).
Single window lambda-chain.  Pairs of Fourier letter sequences (n, n') with sum_t (n_t-n'_t) lam^t = 0 in O  <=>  v_t = e_t - 6 e_{t-1} + e_{t-2},
carries e bounded |e|<=E (truncation).  State (e_{t-1}, e_{t-2}); map Y_(e,a) += T_v(Y_(a,b)),  T_v(Y) = sum_n N_n Y N_{n-v}^*.
E=0 is the i.i.d. operator K (rho 0.27255).  Growth rate of the total (trace-norm) mass = collision-sum rate per lambda-step.
usage: g_carry.py E iters"""
import sys, json, time, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N14/code'); import fastops as F
A=F.A; D=F.D; K=F.K; NS=list(A.NS); s=F.s; c=A.COEF0
E=int(sys.argv[1]); IT=int(sys.argv[2])
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
es=range(-E,E+1); states=[(a,b) for a in es for b in es]
Ys={st:np.zeros((D,D),complex) for st in states}; Ys[(0,0)]=np.outer(F.Phi,F.Phi.conj())
def mass(Ys): return sum(np.linalg.norm(Y,'nuc') if False else np.linalg.norm(Y) for Y in Ys.values())
rates=[]; t0=time.time(); m0=mass(Ys)
for it in range(IT):
    new={st:np.zeros((D,D),complex) for st in states}
    for (a,b),Y in Ys.items():
        if not np.any(Y): continue
        for e in es:
            v=e-6*a+b
            if abs(v)>60: continue
            new[(e,a)]+=Tv(v,Y)
    m1=mass(new); rates.append(m1/m0); m0=m1
    Ys={k:v/m1 for k,v in new.items()}; m0=1.0
    ret=float(np.real(F.psi.conj()@Ys[(0,0)]@F.psi))
    print(it,'rate %.6f'%rates[-1],'share(0,0) %.4f'%(np.linalg.norm(Ys[(0,0)])),round(time.time()-t0,1),flush=True)
json.dump(dict(E=E,rates=rates),open(f'/workspace/bgs-lineN/N15/logs/g_carry_E{E}.json','w'))
