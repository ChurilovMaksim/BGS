"""N15 (1) pre-flight [N]: Bohr-mean identity check.  For a window of n steps with twists d_t = red(u_t), u_{t+1} = 6u_t - u_{t-1}
(lambda-recurrence), the EXACT-collision (all carries) second moment equals the Lebesgue mean over the 2-torus of
|psi prod_t X(d_t) Phi|^2 with (u_0,u_1) ~ Unif(T^2) (cat map M=[[0,1],[-1,6]]) [P: Bohr mean of an almost-periodic polynomial
with frequencies in Z[lam]; Z[lam] collisions = carries].  Compare with the i.i.d. value psi*K^n(Phi Phi*)psi (carry range 0).
usage: g_torus.py nmax nsamp chunk seed"""
import sys, json, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N14/code'); import fastops as F
nmax,ns,ch,seed=map(int,sys.argv[1:5]); rng=np.random.default_rng(seed)
A=F.A; c=A.COEF0; s=F.s
# iid reference
blocks={}
for k,ib,jb,B in zip(F.BK,F.BI,F.BJ,F.BB): blocks.setdefault(int(k),[]).append((int(ib),int(jb),c[k]/s*B))
D=F.D; K=F.K
def Kmap(Y):
    Z=np.zeros((D,D),complex)
    for k in blocks:
        T=np.zeros((D,D),complex)
        for ib,jb,B in blocks[k]: T[ib*K:(ib+1)*K,:]+=B@Y[jb*K:(jb+1)*K,:]
        for ib,jb,B in blocks[k]: Z[:,ib*K:(ib+1)*K]+=T[:,jb*K:(jb+1)*K]@B.conj().T
    return Z
Y=np.outer(F.Phi,F.Phi.conj()); iid=[]
for n in range(1,nmax+1): Y=Kmap(Y); iid.append(float(np.real(F.psi@Y@F.psi.conj())))
# psi here is a row functional: value = psi @ v ; |.|^2 = psi Y psi^*  (psi complex): use conj correctly
iid=[]; Y=np.outer(F.Phi,F.Phi.conj())
for n in range(1,nmax+1): Y=Kmap(Y); iid.append(float(np.real(F.psi@Y@F.psi.conj())))
acc=np.zeros(nmax); acc2=np.zeros(nmax); tot=0
while tot<ns:
    m=min(ch,ns-tot); u0=rng.random(m); u1=rng.random(m)
    V=np.repeat(F.Phi[:,None].astype(complex),m,axis=1); a,b=u0,u1
    for n in range(nmax):
        d=b-np.floor(b+0.5); V=F.step_batch(V,d); val=np.abs(F.psi@V)**2
        acc[n]+=val.sum(); acc2[n]+=(val**2).sum(); a,b=b,(6*b-a)%1.0
    tot+=m
mean=acc/tot; se=np.sqrt(np.maximum(acc2/tot-mean**2,0)/tot)
out=dict(n=list(range(1,nmax+1)),torus_mean=mean.tolist(),se=se.tolist(),iid=iid,ratio=(mean/np.array(iid)).tolist(),nsamp=tot)
for n in range(nmax): print(n+1,'torus %.4e +- %.1e  iid %.4e  ratio %.3f'%(mean[n],se[n],iid[n],mean[n]/iid[n]),flush=True)
json.dump(out,open(f'/workspace/bgs-lineN/N15/logs/g_torus_{nmax}_{ns}_{seed}.json','w'),indent=1)
