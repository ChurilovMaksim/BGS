"""
RUN 20: PRECISE CONSTANT CAMPAIGN.
Determine universal constant c in N_3 <= c*(k^2/p + 1) across many configs.
"""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
import sys, os, json
import numpy as np
from sympy import primitive_root, primerange
sys.path.insert(0, _BGS_ROOT + r"\src")
from run17_bad_patterns import n3_count

ART=_BGS_ROOT + r"\artifacts"

def main():
    rng=np.random.default_rng(20260824)
    print("=== RUN 20: constant campaign ===")
    records=[]
    primes=list(primerange(100,3000))
    np.random.shuffle(primes)
    for p in primes[:25]:
        g=int(primitive_root(p))
        ks=[d for d in range(5,p//3) if (p-1)%d==0]
        if len(ks)<2: continue
        for k in [ks[0],ks[-1]]:   # smallest and largest divisor
            alpha=pow(g,(p-1)//k,p)
            H=set(); x=1
            for _ in range(k): H.add(x); x=x*alpha%p
            mx=0; nz=0; trials=400
            for t in range(trials):
                a=[int(rng.integers(1,p)) for _ in range(4)]
                b=[int(rng.integers(1,p)) for _ in range(4)]
                n=n3_count(p,H,a,b)
                if n>mx: mx=n
                if n>0: nz+=1
            pred=k*k/p + 1
            ratio=mx/pred
            frac_nz=nz/trials
            records.append(dict(p=p,k=k,max_N3=mx,
                                pred=pred, ratio=round(ratio,3),
                                frac_nonzero=round(frac_nz,4)))
            print(f"p={p} k={k}: max_N3={mx}, pred={pred:.3f}, "
                  f"ratio={ratio:.3f}, fracNZ={frac_nz:.3f}")
    arr=np.array([r["ratio"] for r in records])
    print(f"\nGlobal: min={arr.min():.3f} med={np.median(arr):.3f} max={arr.max():.3f}")
    json.dump(records, open(os.path.join(ART,"run20_constant.json"),"w"), indent=1)

if __name__=="__main__":
    main()
