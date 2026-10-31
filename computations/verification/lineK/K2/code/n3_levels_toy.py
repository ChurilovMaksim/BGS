"""N3 [N]: toy twisted traces at actual prime levels q | h_{3p}: per-step rate max_beta |Tr prod_{i<m} L_{a/8 + tau_i(beta)}|^{1/m},
tau_i = Tr(beta lam^i)/q, compared with the d=7 survivor 1.28359.  Weil-range level: all orbits (exhaustive).  Open-range level:
random beta + 'slow' beta (small coordinates)."""
import sys, numpy as np, json, os, sympy
sys.path.insert(0,'/workspace/bgs-lineI/code')
from law import kick_ghat, MC, LAM
gh=kick_ghat('k1',2.0,10); K=40; RHO=2.6; c0=1/(LAM-1/LAM); C=-4*2*c0/8
ns=np.array([n for n,g in gh.items() if abs(g)>0]); Ms=np.array([gh[n]*np.exp(2j*np.pi*C*n*n/2)*MC(n,C,RHO,K) for n in ns])
def Lmat(t): return np.tensordot(np.exp(2j*np.pi*ns*t),Ms,1)
def lam_pow(i,q):
    a,b=1,0
    for _ in range(i): a,b=(3*a+4*b)%q,(2*a+3*b)%q
    return a,b
def taus(beta,q,m):
    b1,b2=beta; out=[]; a,b=1,0
    for i in range(m):
        x1=(b1*a+2*b2*b)%q   # beta*lam^i = x1 + x2 sqrt2 ; Tr = 2 x1
        out.append((2*x1)%q/q); a,b=(3*a+4*b)%q,(2*a+3*b)%q
    return out
def Zhat(beta,q,m,cache):
    best=0
    T=taus(beta,q,m)
    for a in (0,2,4,6):
        P=np.eye(K,dtype=complex)
        for t in T:
            key=round((t+a/8)%1,15)
            if key not in cache: cache[key]=Lmat(key)
            P=cache[key]@P
        best=max(best,abs(np.trace(P)))
    return best
def orbit_reps(q,r):
    seen=np.zeros((q,q),bool); reps=[]
    for b1 in range(q):
        for b2 in range(q):
            if (b1,b2)==(0,0) or seen[b1,b2]: continue
            reps.append((b1,b2)); x1,x2=b1,b2
            for _ in range(r):
                seen[x1,x2]=True; x1,x2=(3*x1+4*x2)%q,(2*x1+3*x2)%q
    return reps
res=[]
p=int(sys.argv[1]) if len(sys.argv)>1 else 37
m=3*p
d7=None
for q,mode in [(int(x.split(':')[0]),x.split(':')[1]) for x in sys.argv[2:]]:
    s=[t for t in range(q) if t*t%q==2][0]; l=(3+2*s)%q; r=sympy.n_order(l,q)
    cache={}; vals=[]
    if mode=='all':
        reps=orbit_reps(q,r)
        for bt in reps: vals.append((Zhat(bt,q,m,cache),bt))
    else:
        rng=np.random.default_rng(1)
        cand=[(int(rng.integers(q)),int(rng.integers(q))) for _ in range(300)]+[(x,y) for x in range(0,6) for y in range(0,6) if (x,y)!=(0,0)]
        for bt in cand: vals.append((Zhat(bt,q,m,cache),bt))
    vals.sort(reverse=True)
    rate=vals[0][0]**(1/m)
    row=dict(p=p,m=m,q=q,r=int(r),log_p_q=round(np.log(q)/np.log(p),2),mode=mode,n_beta=len(vals),max_rate=float(rate),argmax=vals[0][1],
             median_rate=float(np.median([v[0] for v in vals])**(1/m)),threshold=1.28359)
    res.append(row); print(json.dumps(row),flush=True)
json.dump(res,open(f'logs/n3_levels_toy_p{p}.json','w'),indent=1)
