"""
RUN 19: LARGE CAMPAIGN for refined resonance law.
Collect many samples of N_3 across wide range of (p,k,labels).
Fit distribution of ratio N_3 / (k^2/p).
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
    print("=== RUN 19 large campaign ===")
    all_ratios=[]
    meta=[]
    primes=list(primerange(100,2000))[:15]
    for p in primes:
        g=int(primitive_root(p))
        ks=[d for d in range(5,p//4) if (p-1)%d==0]
        if not ks: continue
        k=ks[len(ks)//2]   # middle divisor
        alpha=pow(g,(p-1)//k,p)
        H=set(); x=1
        for _ in range(k): H.add(x); x=x*alpha%p
        for t in range(200):
            a=[int(rng.integers(1,p)) for _ in range(4)]
            b=[int(rng.integers(1,p)) for _ in range(4)]
            n=n3_count(p,H,a,b)
            pred=k*k/p
            if pred>0.5:  # only meaningful when prediction > noise floor
                r=n/pred
                all_ratios.append(r)
                if len(meta)<5 or t<3:
                    meta.append(dict(p=p,k=k,n=n,pred=round(pred,3),
                                     ratio=round(r,3)))
    arr=np.array(all_ratios)
    print(f"total samples with pred>0.5: {len(arr)}")
    print(f"ratio stats: min={arr.min():.3f} q25={np.percentile(arr,25):.3f} "
          f"median={np.percentile(arr,50):.3f} q75={np.percentile(arr,75):.3f} "
          f"max={arr.max():.3f}")
    json.dump(dict(n=len(arr),
                   stats=dict(min=float(arr.min()),
                              q25=float(np.percentile(arr,25)),
                              med=float(np.percentile(arr,50)),
                              q75=float(np.percentile(arr,75)),
                              max=float(arr.max())),
                   samples=meta[:20]),
              open(os.path.join(ART,"run19_campaign.json"),"w"), indent=1)

if __name__=="__main__":
    main()
