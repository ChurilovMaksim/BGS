"""N20 [N, Monte Carlo]: does the JOINT (A,B) pair see collisions beyond the single-window lambda-carries?
eps-chain on T^2: (tau_0, tau_1) uniform, tau_k = 2 tau_{k-1} + tau_{k-2} mod 1 (eps-recurrence of N14 digits.py).
A-window letters X(tau_{2t}), B-window letters X(-tau_{2t-1}), t = 1..n.  r = psi X(d_n)...X(d_1) Phi.
Compare E_torus[|r_A|^2 |r_B|^2] with the i.i.d. product S0(n)^2 (S0 = psi K^n(Phi Phi^*) psi^*, N16 g_scalar E=0),
and the single-window torus means E|r_A|^2, E|r_B|^2 with S0(n).  usage: joint_torus_mc.py n samples seed"""
import sys, json, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N14/code'); import fastops as F
n=int(sys.argv[1]); NSAMP=int(sys.argv[2]); rng=np.random.default_rng(int(sys.argv[3])); BS=2000
IID=len(sys.argv)>4 and sys.argv[4]=="iid"   # control: all eps-twists i.i.d. uniform (must give joint/iid ~ 1)
S0=json.load(open('/workspace/bgs-lineN/N16/logs/g_scalar_E0_n12.json'))['S'][n-1]
acc=[];
for b0 in range(0,NSAMP,BS):
    m=BS; tau=[rng.random(m),rng.random(m)]
    for k in range(2,2*n+2): tau.append(rng.random(m) if IID else (2*tau[-1]+tau[-2])%1.0)
    VA=np.repeat(F.Phi[:,None].astype(complex),m,1); VB=VA.copy()
    for t in range(1,n+1):
        VA=F.step_batch(VA,tau[2*t]); VB=F.step_batch(VB,(-tau[2*t-1])%1.0)
    rA=np.abs(F.psi@VA)**2; rB=np.abs(F.psi@VB)**2
    acc.append(np.stack([rA*rB,rA,rB]))
X=np.concatenate(acc,axis=1); mu=X.mean(1); se=X.std(1)/np.sqrt(X.shape[1])
out=dict(n=n,samples=int(X.shape[1]),S0=S0,joint_over_iid=float(mu[0]/S0**2),joint_se=float(se[0]/S0**2),
         A_over_iid=float(mu[1]/S0),A_se=float(se[1]/S0),B_over_iid=float(mu[2]/S0),B_se=float(se[2]/S0),
         joint_over_product_of_torus=float(mu[0]/(mu[1]*mu[2])))
print(out); json.dump(out,open(f'../logs/joint_torus_mc_n{n}'+('_iid' if IID else '')+'.json','w'),indent=1)
