"""N3 (J) [N]: plain operator norm max_tau ||A^E_tau|| and spectral radii for the E family in the Line F space (K0=4,rho=0.8,K=40)."""
import sys, json, numpy as np
sys.path.insert(0,'/workspace/bgs-lineF/code')
from lift import ops, wk1
K0,r,K,N0,NT=4,0.8,40,60,64
Bn={}
for n in range(-N0,N0+1):
    V,E=ops(lambda m,n=n: 1.0 if m==n else 0.0, N0,K0,r,r,K,beta=0.0); Bn[n]=E
ns=np.array(sorted(Bn)); Bst=np.stack([Bn[n] for n in ns]); w0=wk1(2.0,0); w=np.array([w0(int(n)) for n in ns])
out=[]
for t in (np.arange(NT)+0.5)/NT:
    L=np.tensordot(w*np.exp(2j*np.pi*ns*t),Bst,axes=1); out.append((float(np.linalg.norm(L,2)),float(max(abs(np.linalg.eigvals(L))))))
o=np.array(out); res=dict(max_norm=float(o[:,0].max()),max_rho=float(o[:,1].max()))
print(json.dumps(res)); json.dump(res,open('logs/j_E_plain.json','w'))
