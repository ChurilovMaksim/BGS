"""Line L3 (3) [N]: inherited / rank-p levels. Compare Zhat^{(3p)}_beta (direct), the spectral form via the p-step operator Pi_beta
(m=3p automaton constants): c_{3p} Tr[R Pi^3], and Zhat^{(p)}_beta (m=p, level q | h_p) on the isotropic line.
usage: inherit_test.py p q"""
import sys, json, math, numpy as np; sys.path.insert(0,'/workspace/bgs-lineL/L2/code')
from twlaw import *
p=int(sys.argv[1]); q=int(sys.argv[2]); m=3*p
def nu_of(mm):
    M=2*mdata(mm)['h']; x0=pow(4,-1,M//2); nu=min(x for x in (x0,x0+M//2) if x%2==1); return nu
tw3=TW(m,nu_of(m),L=8,K=32)
hp=mdata(p)['h']; twp=TW(p,nu_of(p),L=8,K=32) if hp%q==0 else None
pw=lam_pows(m,q)
def step_op(tw,taus):
    # full p-step operator on (state,K) space as matrix acting on X (S,K,K): build by applying to basis
    K,S=tw.K,tw.S
    X=np.zeros((S,K,S*K),complex)
    for s in range(S):
        for k in range(K): X[s,k,s*K+k]=1
    for t in taus:
        Y=np.zeros_like(X)
        for n in tw.ns:
            c=np.exp(2j*np.pi*n*t)
            Y[tw.tgt[n]]+=np.matmul(tw.Mn[n],X)*(tw.ph[n]*c)[:,None,None]
        X=Y
    return X.reshape(S*K,S*K)
s=next(x for x in range(q) if (x*x-2)%q==0)
rows=[]
for t in [1,2,3,5,7,11]:
    b=((t*s)%q,t%q); tau=taus_of(b,pw,q)
    assert all(abs(tau[i]-tau[i+p])<1e-12 for i in range(2*p))
    z3=tw3.Z(tau)
    Pi=step_op(tw3,tau[:p]); P3=Pi@Pi@Pi
    K=tw3.K; S=tw3.S
    # readout: start state 0 (identity in K), sum over final states, trace over K
    R=sum(P3[s2*K:(s2+1)*K,0:K] for s2 in range(S))
    z3s=(1-LAM**(-m))*np.trace(R)
    ev=np.linalg.eigvals(Pi); ev=ev[np.argsort(-abs(ev))]
    zp=twp.Z(taus_of(b,lam_pows(p,q),q)) if twp else None
    rows.append(dict(t=t,z3=[z3.real,z3.imag],z3_spec_err=abs(z3-z3s),abs_z3=abs(z3),top_eigs=[abs(e) for e in ev[:4]],
        top_eig_cubed=abs(ev[0])**3, zp=None if zp is None else [zp.real,zp.imag], abs_zp_cubed=None if zp is None else abs(zp)**3))
    print(json.dumps(rows[-1]),flush=True)
json.dump(dict(p=p,q=q,m=m,rows=rows),open(f'/workspace/bgs-lineL/L3/logs/inherit_p{p}_q{q}.json','w'),indent=1)
