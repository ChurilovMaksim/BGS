"""K4b [N]: the block averages that actually arise. On a prime level q, tau_i = Tr(beta lam^i)/q, so a k-block is a function of
y = beta lam^i in O/q ~ T^2 (cat-map dynamics y -> lam y). If the orbit of beta under <lam^k> equidistributes in O/q (BGK-type range),
the order-free product bound gives the rate R_k^cat = exp( E_y log||L_{tau_{k-1}(y)}...L_{tau_0(y)}||_op / k ), y uniform in O/q.
Compute it at q = 2^127-1 (exact integer phases) and compare with iid rates and with 1.2836."""
import sys, numpy as np, json
sys.path.insert(0,'/workspace/bgs-lineI/code')
from law import kick_ghat, MC, LAM
gh=kick_ghat('k1',2.0,10); K=40; RHO=2.6; c0=1/(LAM-1/LAM); C=-4*2*c0/8
ns=[n for n,gn in gh.items() if abs(gn)>0]
Ms=np.array([gh[n]*np.exp(2j*np.pi*C*n*n/2)*MC(n,C,RHO,K) for n in ns]); ns=np.array(ns)
L=lambda t: np.tensordot(np.exp(2j*np.pi*ns*t),Ms,1)
q=2**127-1; KMAX=64
ab=[(1,0)]
for j in range(KMAX): a,b=ab[-1]; ab.append((3*a+4*b,2*a+3*b))
rng=np.random.default_rng(3); res=[]
for k in (6,12,24,36,48,64):
    N=1200 if k<=24 else 600; lo=[]
    for _ in range(N):
        y1=int(rng.integers(0,2**62))*2**65+int(rng.integers(0,2**62)); y2=int(rng.integers(0,2**62))*2**65+int(rng.integers(0,2**62))
        y1%=q; y2%=q; P=np.eye(K,dtype=complex)
        for j in range(k):
            a,b=ab[j]; t=((2*(y1*a+2*y2*b))%q)/q
            P=L(t)@P
            nP=np.linalg.norm(P,2)
        lo.append(np.log(np.linalg.norm(P,2)))
    lo=np.array(lo); r=dict(k=k,N=N,R_cat=float(np.exp(lo.mean()/k)),se_logR=float(lo.std()/np.sqrt(N)/k)); res.append(r); print(r,flush=True)
json.dump(dict(rows=res,threshold=1.2836,q='2^127-1'),open('logs/k4_catrate.json','w'),indent=1)
