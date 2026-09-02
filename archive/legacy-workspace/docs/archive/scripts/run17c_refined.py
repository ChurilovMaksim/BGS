"""RUN 17c: Test refined conjecture sol = O(max(k, k^3/p))."""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
import sys, os, json
import numpy as np
from sympy import primitive_root
sys.path.insert(0, _BGS_ROOT + r"\src")
from run17_bad_patterns import n3_count

ART=_BGS_ROOT + r"\artifacts"

def main():
    rng=np.random.default_rng(999)
    print("=== RUN 17c: test N3 ~ k^2/p ===")
    res=[]
    for p in (211, 257, 401, 809):
        g=int(primitive_root(p))
        ks=[d for d in range(5,min(p//2,300)) if (p-1)%d==0][-6:]
        for k in ks:
            alpha=pow(g,(p-1)//k,p)
            H=set(); x=1
            for _ in range(k): H.add(x); x=x*alpha%p
            mx=0
            for t in range(1500):
                a=[int(rng.integers(1,p)) for _ in range(4)]
                b=[int(rng.integers(1,p)) for _ in range(4)]
                n=n3_count(p,H,a,b)
                if n>mx: mx=n
            pred=k*k//p + 1
            res.append(dict(p=p,k=k,max_N3=mx,pred_k2_over_p=pred,
                            ratio=round(mx/max(pred,1),2)))
            print(f"p={p} k={k}: max_N3={mx}, ceil(k^2/p)+1={pred}, "
                  f"ratio={mx/max(pred,1):.2f}")
    json.dump(res, open(os.path.join(ART,"run17c_N3_scaling.json"),"w"), indent=1)

if __name__=="__main__":
    main()
