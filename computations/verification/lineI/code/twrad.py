"""Float (single-disc Galerkin) spectral radii of the 3-step twisted products Q_beta = L_{tau2}L_{tau1}L_{tau0}
for resonances (+-2,8), d=7, all four operator cases (m=9,15,21,27), all 16 beta-classes (beta mod lambda-orbit).
r_tw(beta) = rho(Q_beta)^{1/3}. Also untwisted mu.  Output logs/twrad.json"""
import numpy as np, json, sys, time
import scipy.sparse.linalg as ssl
from law import kick_ghat
from twist import build
K=int(sys.argv[1]) if len(sys.argv)>1 else 40; RHO=float(sys.argv[2]) if len(sys.argv)>2 else 2.6
gh=kick_ghat('k1',2.0,10); d=7
lam=[];x,y=1,0
for i in range(3): lam.append((x,y)); x,y=(3*x+4*y)%d,(2*x+3*y)%d
def taus(bx,by): return [((2*(bx*lx+2*by*ly))%d)/d for (lx,ly) in lam]
# beta classes under beta -> beta*lambda (cyclic shift of taus)
seen=set(); classes=[]
for bx in range(d):
    for by in range(d):
        if bx==0 and by==0: continue
        t=tuple(taus(bx,by))
        key=min(t[i:]+t[:i] for i in range(3))
        if key in seen: continue
        seen.add(key); classes.append(((bx,by),t))
print('classes',len(classes),flush=True)
out={}
for m in (9,15,21,27):
  for (a,b) in ((2,8),(-2,8)):
    t0=time.time(); parts,nu,S=build(m,a,b,gh,RHO,K)
    items=[(n,Mn,P) for n,(Mn,P) in parts.items()]
    tg={n:(P!=0).argmax(axis=0) for n,Mn,P in items}; ph={n:P[tg[n],np.arange(S)] for n,Mn,P in items}
    def apply(v,tau):
        X=v.reshape(K,S); Y=np.zeros_like(X)
        for n,Mn,P in items:
            Y[:,tg[n]]+=np.exp(2j*np.pi*n*tau)*(Mn@X)*ph[n][None,:]
        return Y.ravel()
    def radius(ts):
        A=ssl.LinearOperator((K*S,K*S),matvec=lambda v: apply(apply(apply(v,ts[0]),ts[1]),ts[2]),dtype=complex)
        ev=ssl.eigs(A,k=4,which='LM',tol=1e-10,maxiter=20000,return_eigenvectors=False)
        return sorted(abs(ev),reverse=True)
    r0=radius([0,0,0]); rec=dict(mu=r0[0]**(1/3),mu_list=[x**(1/3) for x in r0],tw={})
    for (bx,by),t in classes:
        r=radius(t); rec['tw'][f'{bx},{by}']=dict(taus=t,r=r[0]**(1/3),r2=r[1]**(1/3))
    rw=max(v['r'] for v in rec['tw'].values()); rec['rtw_max']=rw
    print(m,(a,b),'mu',round(rec['mu'],6),'rtw_max',round(rw,6),'all',sorted(round(v['r'],4) for v in rec['tw'].values()),round(time.time()-t0),'s',flush=True)
    out[f'{m},{a},{b}']=rec
    json.dump(out,open(f'../logs/twrad_K{K}_r{RHO}.json','w'),indent=1)
