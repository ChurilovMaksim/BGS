"""N2 (C) [N]: float estimate of the twisted 'joint spectral radius along cat-map orbits'
Lambda_k = max_{sector a, y in torus} ||P_k(y)||_op^{1/k},  P_k(y) = L_{a,tau_{k-1}} ... L_{a,tau_0},
tau_{j+1} = 6 tau_j - tau_{j-1} (mod 1), (tau_0,tau_1) on a grid; lifted Line F vertex/edge operators (lift.py),
twist = extra letter phase e(n tau).  Also: spectral radii at periodic points of small period (lower bounds for JSR).
usage: c_jsr_float.py typ K0 r K beta N0 grid kmax"""
import sys, math, json, time, numpy as np
sys.path.insert(0,'/workspace/bgs-lineF/code')
from lift import ops, wk1, LAM, C0
typ=sys.argv[1]; K0=int(sys.argv[2]); r=float(sys.argv[3]); K=int(sys.argv[4]); beta=float(sys.argv[5])
N0=int(sys.argv[6]); G=int(sys.argv[7]); kmax=int(sys.argv[8])
rE=r
Bn={}
for n in range(-N0,N0+1):
    V,E=ops(lambda m,n=n: 1.0 if m==n else 0.0, N0,K0,r,rE,K,beta=beta)
    Bn[n]=V if typ=='V' else E
ns=sorted(Bn)
def L(a,tau,w):
    return sum(w[n]*np.exp(2j*np.pi*n*tau)*Bn[n] for n in ns)
out=dict(typ=typ,K0=K0,r=r,K=K,beta=beta,N0=N0,grid=G,kmax=kmax,sectors={})
t0=time.time()
for a in (0,2,4,6):
    w0=wk1(2.0,a); w={n:w0(n) for n in ns}
    L0=L(a,0.0,w); ev=np.linalg.eigvals(L0); rho0=float(max(abs(ev)))
    # untwisted norms
    P=np.eye(L0.shape[0]); un=[]
    for k in range(1,kmax+1): P=L0@P; un.append(float(np.linalg.norm(P,2))**(1/k))
    # grid sup of ||P_k(y)||^{1/k}
    # precompute L at all twist values on grid (tau in (1/G)Z): twist sequence stays on grid since A integer
    Lg=[L(a,t/G,w) for t in range(G)]
    best=[0.0]*kmax; arg=[None]*kmax
    for t0_ in range(G):
        for t1_ in range(G):
            P=np.eye(L0.shape[0],dtype=complex); x0,x1=t0_,t1_
            for k in range(1,kmax+1):
                P=Lg[x0]@P; x0,x1=x1,(6*x1-x0)%G
                if k>=2:
                    nv=float(np.linalg.norm(P,2))**(1/k)
                    if nv>best[k-1]: best[k-1]=nv; arg[k-1]=(t0_,t1_)
    # periodic points of small period n on grid G: those with A^n tau = tau (mod 1) -- only grid-compatible ones
    per=[]
    for n in (1,2,3,4,5,6):
        bestp=0.0; argp=None
        for t0_ in range(G):
            for t1_ in range(G):
                x0,x1=t0_,t1_; seq=[]
                for i in range(n): seq.append(x0); x0,x1=x1,(6*x1-x0)%G
                if (x0,x1)!=(t0_,t1_): continue
                P=np.eye(L0.shape[0],dtype=complex)
                for s in seq: P=Lg[s]@P
                rr=float(max(abs(np.linalg.eigvals(P))))**(1/n)
                if rr>bestp: bestp=rr; argp=(t0_,t1_)
        per.append((n,bestp,argp))
    out['sectors'][a]=dict(rho_untwisted=rho0,untwisted_norm_rate=un,grid_sup_rate=best,argmax=arg,periodic_specrad=per)
    print(json.dumps({'a':a,'rho0':rho0,'unt_k':[round(u,4) for u in un],'sup_k':[round(b,4) for b in best],'arg':arg[-1],'per':per,'sec':round(time.time()-t0)}),flush=True)
json.dump(out,open(f'logs/c_jsr_{typ}_K0{K0}_r{r}_K{K}_b{beta}_G{G}_k{kmax}.json','w'),indent=1)
