"""referee lineN20: own MC for joint/iid. Twists tau_k = (P_k tau0 + Q_k tau1) mod 1 with exact integer P_k,Q_k
(eps-recurrence tau_k = 2 tau_{k-1} + tau_{k-2}); own iid reference S0(n) = psi K^n(Phi Phi^*) psi^* with
K(Z) = sum_n |c_n/s|^2 M_n Z M_n^* (exact Fourier average over a uniform twist). usage: ref_mc.py n samples seed"""
import sys, json, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N14/code'); import fastops as F
sys.path.insert(0,'/workspace/bgs-lineN/N12/code'); import a_ops as A
n=int(sys.argv[1]); NS=int(sys.argv[2]); rng=np.random.default_rng(int(sys.argv[3])+7919)
# own iid reference
Z=np.outer(F.Phi,F.Phi.conj()).astype(complex); w=np.abs(A.COEF0/F.s)**2
S0=[]
for t in range(n):
    Z=sum(w[k]*(A.MS[k]@Z@A.MS[k].conj().T) for k in range(len(A.NS)))
    S0.append(float((F.psi@Z@F.psi.conj()).real))
P=[1,0]; Q=[0,1]
for k in range(2,2*n+1): P.append(2*P[-1]+P[-2]); Q.append(2*Q[-1]+Q[-2])
acc=[]
for b0 in range(0,NS,1000):
    m=min(1000,NS-b0); t0=rng.random(m); t1=rng.random(m)
    tau=[(P[k]*t0+Q[k]*t1)%1.0 for k in range(2*n+1)]
    VA=np.repeat(F.Phi[:,None].astype(complex),m,1); VB=VA.copy()
    for t in range(1,n+1):
        VA=F.step_batch(VA,tau[2*t]); VB=F.step_batch(VB,(-tau[2*t-1])%1.0)
    rA=np.abs(F.psi@VA)**2; rB=np.abs(F.psi@VB)**2; acc.append(np.stack([rA*rB,rA,rB]))
X=np.concatenate(acc,1); mu=X.mean(1); se=X.std(1)/np.sqrt(X.shape[1]); s0=S0[-1]
N16=json.load(open('/workspace/bgs-lineN/N16/logs/g_scalar_E0_n12.json'))['S'][n-1]
out=dict(n=n,samples=X.shape[1],S0_own=s0,S0_N16=N16,joint_over_iid=mu[0]/s0**2,se=se[0]/s0**2,A=mu[1]/s0,B=mu[2]/s0,
         joint_over_prod_torus=mu[0]/(mu[1]*mu[2]))
print(json.dumps(out)); json.dump(out,open(f'../logs/ref_mc_n{n}.json','w'),indent=1)
