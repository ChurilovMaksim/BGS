# Data-only check of E = 2m - 2m^2/p + ...: exact per-prime values (engine mode P, validated vs brute force),
# least-squares fit in 1/p over primes p = 3 mod 4 in [200, 4000] (no sqrt term there), and exact residuals.
import sys, numpy as np
sys.path.insert(0,'/workspace/audit/lineC/code')
from sym import *
def primes(a,b): return [q for q in range(a,b) if q>2 and all(q%d for d in range(2,int(q**.5)+1))]
for m in (5,6,7):
    ps=[q for q in primes(200,4000) if q%4==3][::6]
    vals=[]
    for p in ps:
        re,sq=evaluate(run_engine(m,p,2*m),p,symbolic=False); vals.append(float(re))
    ps_a=np.array(ps,float); y=np.array(vals)
    X=np.vstack([ps_a**-k for k in range(4)]).T
    coef=np.linalg.lstsq(X,y,rcond=None)[0]
    print(f"m={m}: fit over {len(ps)} primes p=3 mod 4 in [{ps[0]},{ps[-1]}]: c0={coef[0]:.6f} (2m={2*m}), c1={coef[1]:.3f} (-2m^2={-2*m*m}), c2~{coef[2]:.1f}")
    for p,v in list(zip(ps,vals))[:3]+list(zip(ps,vals))[-2:]:
        print(f"   p={p}: p^2*(E-2m+2m^2/p) = {p*p*(v-2*m+2*m*m/p):.4f}")
