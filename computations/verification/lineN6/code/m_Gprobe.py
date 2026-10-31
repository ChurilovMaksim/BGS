"""N6 (1) [N] probe: sub-product norms G = max_I ||prod_{j in I} A_j|| / |mu|^|I| over the excursion steps, ||Pi_T||, in the Line F
certificate representation (K0=4, rho=1.2, beta=2.5, K=55) — decides feasibility of the [CA] route."""
import sys, math, numpy as np
sys.path.insert(0,'/workspace/bgs-lineF/code'); from lift import ops, LAM, C0
from scipy.special import jv
K0,K,N0=4,55,60; r=1.2; beta=2.5
def w(t): return lambda n: (1j)**(n%4)*jv(n,1.8)*np.exp(2j*np.pi*(C0*n*n/2+n*t))
V=lambda t: ops(w(t),N0,K0,r,0.8,K,beta=beta)[0]
L=V(0.5); ev,R=np.linalg.eig(L); i=np.argmax(abs(ev)); mu=ev[i]; Phi=R[:,i]
evl,Lv=np.linalg.eig(L.T); psi=Lv[:,np.argmin(abs(evl-mu))]
print('mu',mu,'||L||',np.linalg.norm(L,2),'||Pi||',np.linalg.norm(Phi)*np.linalg.norm(psi)/abs(psi@Phi))
a=(2-math.sqrt(2))/4; b=math.sqrt(2)/4
for name,KK in [('A',8),('B',8)]:
    if name=='A': ds=[-a*LAM**(-(-k)) for k in range(-KK,1)]+[a*LAM**(-(k-1)) for k in range(1,KK+1)]
    else: ds=[-b*LAM**(-abs(k)) for k in range(-KK,KK+1)]
    Ms=[V(0.5+d)/mu for d in ds]; G=0; n=len(Ms)
    for i0 in range(n):
        P=np.eye(L.shape[0])
        for j in range(i0,n):
            P=Ms[j]@P; G=max(G,np.linalg.norm(P,2))
    v=Phi.copy()
    for M in Ms: v=M@v
    print(name,'len',n,'G',G,'max single',max(np.linalg.norm(M,2) for M in Ms),'r',(psi@v)/(psi@Phi))
