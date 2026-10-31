"""N3 (G) [N]: extremal quadratic norm search for the free twist family {L_tau} (Line F lifted V or E operator, sector 0):
minimise f(R) = max_tau sigma_max(R L_tau R^{-1}) over invertible R (|||x||| = |Rx|), via Adam on a log-sum-exp surrogate over a
tau grid.  If f < Lam_target uniformly in tau (Lipschitz margin), then every product satisfies ||prod L_tau_i|| <= cond(R) f^n:
the JSR of the free family (>= the torus Lambda) is <= f.  usage: g_ext_norm.py typ K0 r K beta N0 NT iters lr temp"""
import sys, json, time, numpy as np, scipy.linalg as sl
sys.path.insert(0,'/workspace/bgs-lineF/code')
from lift import ops, wk1
typ=sys.argv[1]; K0=int(sys.argv[2]); r=float(sys.argv[3]); K=int(sys.argv[4]); beta=float(sys.argv[5]); N0=int(sys.argv[6])
NT=int(sys.argv[7]); iters=int(sys.argv[8]); lr=float(sys.argv[9]); temp=float(sys.argv[10]); tag=sys.argv[11] if len(sys.argv)>11 else ""
Bn={}
for n in range(-N0,N0+1):
    V,E=ops(lambda m,n=n: 1.0 if m==n else 0.0, N0,K0,r,r,K,beta=beta); Bn[n]=V if typ=='V' else E
ns=np.array(sorted(Bn)); Bst=np.stack([Bn[n] for n in ns]); w0=wk1(2.0,0); w=np.array([w0(int(n)) for n in ns])
def L(t): return np.tensordot(w*np.exp(2j*np.pi*ns*t),Bst,axes=1)
taus=(np.arange(NT)+0.5)/NT; Ls=np.stack([L(t) for t in taus]); d=Ls.shape[1]
Lh=L(0.5); rho_half=max(abs(np.linalg.eigvals(Lh)))
# init: Lyapunov-type P from the extremal operator at rate slightly above its spectral radius
lam0=rho_half*1.03; P=np.zeros((d,d),complex); M=np.eye(d,dtype=complex)
for j in range(300): P+=M.conj().T@M/lam0**(2*j); M=Lh@M
P+=1e-6*np.trace(P).real/d*np.eye(d)
R=np.linalg.cholesky(P).conj().T
import os
if os.environ.get('RINIT'): R=np.load(os.environ['RINIT']); print('warm start',os.environ['RINIT'],flush=True)
def evals(R):
    Ri=np.linalg.inv(R); out=[]
    for Lt in Ls:
        X=R@Lt@Ri; U,s,Vh=np.linalg.svd(X); out.append((s[0],U[:,0],Vh[0].conj(),X,Ri))
    return out
mA=np.zeros_like(R); vA=np.zeros(R.shape); b1,b2=0.9,0.999; hist=[]; best=(1e9,None); t0=time.time()
for it in range(iters):
    ev=evals(R); s=np.array([e[0] for e in ev]); f=s.max()
    if f<best[0]: best=(f,R.copy())
    wts=np.exp(temp*(s/f-1)); wts/=wts.sum()
    G=np.zeros_like(R)
    for wt,(sv,u,v,X,Ri) in zip(wts,ev):
        if wt<1e-6: continue
        # d sigma = Re(u^* (dR L Ri - X dR Ri) v) ; with L Ri v = Ri X v
        a=(Ls[0]*0)  # placeholder to keep shapes clear
        Lv=Ri@(X@v); Riv=Ri@v
        G+=wt*(np.outer(u,Lv.conj()) - np.outer(X.conj().T@u,Riv.conj()))
    G=G/ f
    mA=b1*mA+(1-b1)*G; vA=b2*vA+(1-b2)*np.abs(G)**2
    step=lr*(mA/(1-b1**(it+1)))/(np.sqrt(vA/(1-b2**(it+1)))+1e-12)
    R=R-step*np.linalg.norm(R)/np.sqrt(d*d)
    if it%25==0 or it==iters-1:
        hist.append(dict(it=it,f=float(f),argtau=float(taus[int(s.argmax())]),cond=float(np.linalg.cond(R)),sec=round(time.time()-t0)))
        print(json.dumps(hist[-1]),flush=True)
        np.save(f'logs/g_R_{typ}_K0{K0}_K{K}_NT{NT}{tag}.npy',best[1])
np.save(f'logs/g_R_{typ}_K0{K0}_K{K}_NT{NT}{tag}.npy',best[1])
json.dump(dict(typ=typ,K0=K0,r=r,K=K,beta=beta,N0=N0,NT=NT,rho_half=float(rho_half),best=float(best[0]),hist=hist),
          open(f'logs/g_ext_norm_{typ}_K0{K0}_K{K}_NT{NT}{tag}.json','w'),indent=1)
