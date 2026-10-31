"""N9b [N]: singular-value / eigenvalue structure of single letters L_tau (8V lift, a=4): is the cocycle near rank one?"""
import sys, numpy as np
sys.path.insert(0,'/workspace/bgs-lineF/code')
from lift import ops, wk1
K0,r,K,beta,N0=3,1.2,20,2.5,10
Bn={}
for n in range(-N0,N0+1):
    V,E=ops(lambda m,n=n: 1.0 if m==n else 0.0, N0,K0,r,r,K,beta=beta); Bn[n]=V
ns=np.array(sorted(Bn)); Bst=np.stack([Bn[n] for n in ns]); w0=wk1(2.0,4); w=np.array([w0(int(n)) for n in ns])
L=lambda t: np.tensordot(w*np.exp(2j*np.pi*ns*t),Bst,axes=(0,0))
for t in (0,0.05,0.125,0.25,0.375,0.5):
    s=np.linalg.svd(L(t),compute_uv=False); ev=np.sort(np.abs(np.linalg.eigvals(L(t))))[::-1]
    print('tau',t,'sv',np.round(s[:5],4),'|ev|',np.round(ev[:4],4))
rng=np.random.default_rng(0)
for k in (2,4,8):
    y=rng.random(2); P=np.eye(140)
    for i in range(k): P=L(y[0])@P; y=np.array([y[1],(6*y[1]-y[0])%1])
    s=np.linalg.svd(P,compute_uv=False); print('k',k,'random product sv',s[:4]/s[0])
