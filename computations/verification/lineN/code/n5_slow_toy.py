"""N5 [N]: illustration of Theorem N3 (scarred conductors carry slow beta=1) in the K2 toy model (single-disc Galerkin,
bgs-lineI law.py, same as K2 n3_levels_toy.py). Conductor c = h_p (composite or prime), m = 3p, beta = 1 (=(1,0)) vs random beta.
Per-step rate |Tr prod L_{a/8+tau_i}|^{1/m}, max over sectors a; threshold 1.28359; untwisted rate for comparison."""
import sys, numpy as np, json
sys.path.insert(0,'/workspace/bgs-lineI/code')
from law import kick_ghat, MC, LAM
gh=kick_ghat('k1',2.0,10); K=40; RHO=2.6; c0=1/(LAM-1/LAM); C=-4*2*c0/8
ns=np.array([n for n,g in gh.items() if abs(g)>0]); Ms=np.array([gh[n]*np.exp(2j*np.pi*C*n*n/2)*MC(n,C,RHO,K) for n in ns])
def Lmat(t): return np.tensordot(np.exp(2j*np.pi*ns*t),Ms,1)
def taus(beta,c,m):
    b1,b2=beta; out=[]; a,b=1,0
    for i in range(m):
        x1=(b1*a+2*b2*b)%c
        out.append(((2*x1)%c)/c); a,b=(3*a+4*b)%c,(2*a+3*b)%c
    return out
def rate(beta,c,m):
    best=0; T=taus(beta,c,m)
    for a in (0,2,4,6):
        P=np.eye(K,dtype=complex)
        for t in T: P=Lmat((t+a/8)%1)@P
        best=max(best,abs(np.trace(P)))
    return best**(1/m)
def hseq(M):
    x,y=1,1; out={1:1}
    for mm in range(2,M+1):
        x,y=x+2*y,x+y
        if mm%2: out[mm]=x
    return out
H=hseq(400); rng=np.random.default_rng(7); res=[]
print("untwisted rate (c=1 i.e. all tau=0):", rate((0,0),1,45))
for p in [int(a) for a in sys.argv[1:]] or [11,13,17,19,23,29]:
    m=3*p; c=H[p]
    r1=rate((1,0),c,m); r2=rate((1,1),c,m)
    rr=[rate((int(rng.integers(c)),int(rng.integers(c))),c,m) for _ in range(5)]
    frac=2*np.log(c)/np.log(LAM)/p
    row=dict(p=p,m=m,c=str(c),log_lam_c=float(np.log(c)/np.log(LAM)),near0_fraction=float(frac),rate_beta1=float(r1),rate_beta_1p1=float(r2),
             rate_random=[float(x) for x in rr],threshold=1.28359)
    res.append(row); print(json.dumps(row),flush=True)
json.dump(res,open('/workspace/bgs-lineN/logs/n5_slow_toy.json','w'),indent=1)
