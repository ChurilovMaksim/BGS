"""[N] fixed-period levels d (primes q with small rank r(q), and 49): twisted radii r_tw(d) = max over beta in O/d \ {0} and sectors
a in {0,2,4,6} of r(prod_{i<per} L_{a/8+tau_i})^{1/per}, tau_i = Tr(beta lam^i)/d, per = ord_d(lam) (period of the twist).
Also the rms radius over beta.  Family L_tau as in lyap.py (b=8, single-disc Galerkin K=40, rho=2.6)."""
import sys, numpy as np, json
sys.path.insert(0,'/workspace/bgs-lineI/code')
from law import kick_ghat, MC, LAM
gh=kick_ghat('k1',2.0,10); K=40; RHO=2.6; c0=1/(LAM-1/LAM); C=-c0
Mn={n:gn*np.exp(2j*np.pi*C*n*n/2)*MC(n,C,RHO,K) for n,gn in gh.items() if abs(gn)>0}
cache={}
def L(t):
    t=round(t%1,12)
    if t not in cache: cache[t]=sum(np.exp(2j*np.pi*n*t)*M for n,M in Mn.items())
    return cache[t]
def lampow(d):   # lam^i mod d as (x,y): x + y sqrt2
    out=[]; x,y=1,0
    while True:
        out.append((x,y)); x,y=(3*x+4*y)%d,(2*x+3*y)%d
        if (x,y)==(1,0): return out
res={}
for d in (7,41,239,199,23,353,79,49,31,103,47):
    pw=lampow(d); per=len(pw)
    seen=set(); rads=[]
    for bx in range(d):
        for by in range(d):
            if bx==0 and by==0: continue
            taus=[((2*(bx*x+2*by*y))%d)/d for (x,y) in pw]
            key=min(tuple(taus[i:]+taus[:i]) for i in range(per))   # cyclic shift = same spectrum
            if key in seen: continue
            seen.add(key)
            best=0
            for a in (0,2,4,6):
                Q=np.eye(K,dtype=complex)
                for t in taus: Q=L(a/8+t)@Q
                best=max(best,max(abs(np.linalg.eigvals(Q)))**(1/per))
            rads.append(best)
        if len(seen)>400: break
    rads=np.array(rads)
    res[d]=dict(period=per,classes=len(rads),r_max=float(rads.max()),r_rms=float(np.sqrt((rads**(2*per)).mean())**(1/per)),r_median=float(np.median(rads)))
    print(d,res[d],flush=True)
json.dump(res,open('logs/levels_survey.json','w'),indent=1)
