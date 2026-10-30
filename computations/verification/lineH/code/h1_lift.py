"""Line H, H1 [N]: cross-validation of the trustworthy small-|a|/b rows of h1_scan (Line G (a,b,k) operators, k1 kick, m=13)
with an independent discretisation: the Line F vertex/edge lift (lattice of discs, radius r) tensored with A_n^{(b)} on C^{b^2}.
Checks (i) lifted trace identity Tr Op^j  vs (1-lam^-j)(Tr V^j - Tr E^j), j=2..5, against the single-disc h1_scan operator,
(ii) leading |eig| of V vs h1_scan spectral radius.  Usage: h1_lift.py m K0 r K Lk Ksingle"""
import sys, json, math, numpy as np
sys.path.insert(0,'/workspace/bgs-lineG/code'); sys.path.insert(0,'/workspace/bgs-lineF/code')
from law import mdata, kick_ghat, MC, LAM, C0
from lift import blockmat, rnd
m=int(sys.argv[1]); K0=int(sys.argv[2]); r=float(sys.argv[3]); K=int(sys.argv[4]); Lk=int(sys.argv[5]); Ks=int(sys.argv[6])
d=mdata(m); h=d['h']; yp=d['yp']
gh=kick_ghat('k1',2.0,Lk)
rho=1.25*Lk/(LAM-1)+0.5
def An(n,b,k):
    psi0=yp%b; psi1=(3*yp-2*h)%b; S=b*b; us=np.arange(S)//b; ws=np.arange(S)%b
    ph=np.exp(-2j*np.pi*((k*((psi0*n*n+2*n*us)%b))%b)/b)
    tgt=(((6*us-ws+n*psi1)%b)*b+((us+n*psi0)%b)); A=np.zeros((S,S),complex); A[tgt,np.arange(S)]=ph; return A
def single(a,b,k):
    coef=-4*a*C0/b; S=b*b; Op=np.zeros((Ks*S,Ks*S),complex)
    for n,gn in gh.items(): Op+=np.kron(gn*np.exp(2j*np.pi*coef*n*n/2)*MC(n,coef,rho,Ks),An(n,b,k))
    return Op
def lifted(a,b,k):
    coef=-4*a*C0/b; S=b*b; nv=2*K0+1; ne=2*K0; B=K*S
    V=np.zeros((nv*B,)*2,complex); E=np.zeros((ne*B,)*2,complex)
    for n,gn in gh.items():
        w=gn*np.exp(2j*np.pi*coef*n*n/2); A=An(n,b,k)
        for kk in range(-K0,K0+1):
            j=rnd((kk+n)/LAM)
            if abs(j)>K0: continue
            V[(kk+K0)*B:(kk+K0+1)*B,(j+K0)*B:(j+K0+1)*B]+=w*np.kron(blockmat(n,kk,j,r,r,coef,K),A)
        for e in range(-K0,K0):
            j=rnd((e+n)/LAM); j2=rnd((e+1+n)/LAM)
            if j2!=j+1 or j<-K0 or j>K0-1: continue
            E[(e+K0)*B:(e+K0+1)*B,(j+K0)*B:(j+K0+1)*B]+=w*np.kron(blockmat(n,e+.5,j+.5,r,r,coef,K),A)
    return V,E
LIST=[tuple(int(t) for t in x.split(':')) for x in sys.argv[7].split(',')] if len(sys.argv)>7 else [(-1,3,1),(1,3,2),(-1,5,3),(1,5,2),(2,4,1),(3,5,1)]
for (a,b,k) in LIST:
    Op=single(a,b,k); V,E=lifted(a,b,k)
    ev=np.linalg.eigvals(V); ee=np.linalg.eigvals(E); es=np.linalg.eigvals(Op)
    tr=[]
    for j in range(2,6):
        t1=np.sum(es**j); t2=(1-LAM**-j)*(np.sum(ev**j)-np.sum(ee**j)); tr.append(abs(t1-t2)/max(abs(t2),1e-300))
    top=lambda x:[round(float(t),5) for t in np.sort(abs(x))[::-1][:4]]
    print(json.dumps(dict(K0=K0,r=r,K=K,Lk=Lk,a=a,b=b,k=k,single_top=top(es),liftV_top=top(ev),liftE_top=top(ee),trace_rel_j2_5=[float('%.2e'%t) for t in tr],dimV=V.shape[0])),flush=True)
