"""Line F: lifted (vertex/edge) 49-state resonance operators for the Line B full kick (float exploration).
 (L phi)_c(u,sig) = sum_n ghat(n) e(s c0 (x u + x^2/2) + b n/8 + gamma (n sig + n^2/2)/49) phi_{c'}((u+x)/lam, lam_7^{-1}(sig+n)),  x = n/7,
 c' = round((c+x)/lam) (vertex), edge as in lift.py.  Claim (3 not| m): Z_m(nu_res) = (1-lam^-m) sum_b c_b (Tr V_b^m - Tr E_b^m)."""
import sys, json, math, numpy as np
sys.path.insert(0,'computations/verification/lineE/step2')
from lawlib import law_params
from tm49 import DP, csec
from cmp_full import KICKS, ghat_of
from lift import blockmat, rnd, LAM, C0
def ops49(G, s, b, K0, r, rE, K, P, a=7):
    A2=a*a; nv=2*K0+1; ne=2*K0
    V=np.zeros((nv*K*A2,)*2,complex); E=np.zeros((ne*K*A2,)*2,complex)
    for n,gn in G.items():
        if gn==0: continue
        x=n/a; w=gn*np.exp(2j*np.pi*(s*C0*x*x/2+b*n/8)); D=DP(n,P).T
        for k in range(-K0,K0+1):
            j=rnd((k+x)/LAM)
            if abs(j)>K0: continue
            Bm=np.kron(blockmat(x,k,j,r,r,s*C0,K),D)
            V[(k+K0)*K*A2:(k+K0+1)*K*A2,(j+K0)*K*A2:(j+K0+1)*K*A2]+=w*Bm
        for e in range(-K0,K0):
            j=rnd((e+x)/LAM); j2=rnd((e+1+x)/LAM)
            if j2!=j+1 or j<-K0 or j>K0-1: continue
            Bm=np.kron(blockmat(x,e+.5,j+.5,rE,rE,s*C0,K),D)
            E[(e+K0)*K*A2:(e+K0+1)*K*A2,(j+K0)*K*A2:(j+K0+1)*K*A2]+=w*Bm
    return V,E
if __name__=='__main__':
    K0=int(sys.argv[1]); K=int(sys.argv[2]); Lg=int(sys.argv[3]); eta=2.0
    G=ghat_of(KICKS['full'],eta,Lg)
    res={}
    for s in (1,-1):
        P=law_params(5,7,s)
        for b in (0,2,4,6):
            V,E=ops49(G,s,b,K0,1.2,0.8,K,P)
            ev=np.linalg.eigvals(V); ee=np.linalg.eigvals(E)
            res[(s,b)]=(ev,ee)
            o=np.sort(abs(ev))[::-1]; oe=np.sort(abs(ee))[::-1]
            print(json.dumps(dict(s=s,b=b,V_top=[round(t,6) for t in o[:6]],E_top=[round(t,6) for t in oe[:4]])),flush=True)
    sys.path.insert(0,'computations/verification/lineE/step2')
    from cmp_full import Zclass
    from lawlib import nu_res
    for m in (5,7,11,13):
        T=np.load(f'computations/verification/lineE/referee/logs/T_full_eta2.0_m{m}.npy')
        for s in (1,-1):
            P=law_params(m,7,s); cs=csec(P['kappa'])
            Z=(1-LAM**-m)*sum(cs[b]*(np.sum(res[(s,b)][0]**m)-np.sum(res[(s,b)][1]**m)) for b in (0,2,4,6))
            zc=Zclass(T,m,nu_res(m,7,s))
            print(json.dumps(dict(m=m,s=s,Z2_class=zc,Z2_lift49=abs(Z)**2,rel=abs(abs(Z)**2-zc)/zc)),flush=True)
