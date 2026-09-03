"""
RUN 44 DECISIVE: Measure MEAN of N_3 over random labels.
Discriminates k^3/p^2 (independence) vs k^2/p (hidden correlation).
"""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
import sys, os, json
import numpy as np
from sympy import primitive_root

sys.path.insert(0, _BGS_ROOT + r"\src")
from run17_bad_patterns import n3_count

ART=_BGS_ROOT + r"\artifacts"


def main():
    rng=np.random.default_rng(777)
    print("=== RUN 44 mean-N3 scaling ===")
    rows=[]
    for (p,k,trials) in [(101,10,3000),(101,20,2000),
                         (211,21,2000),(401,40,1500)]:
        g=int(primitive_root(p))
        alpha=pow(g,(p-1)//k,p)
        H=set(); x=1
        for _ in range(k): H.add(x); x=x*alpha%p
        tot=0; nz=0
        for t in range(trials):
            a=[int(rng.integers(1,p)) for _ in range(4)]
            b=[int(rng.integers(1,p)) for _ in range(4)]
            n=n3_count(p,H,a,b)
            tot+=n
            if n>0: nz+=1
        mean=tot/trials
        pred_indep=k**3/p**2
        pred_corr=k**2/p
        which="INDEP" if abs(mean-pred_indep)<abs(mean-pred_corr) else "CORR"
        rows.append(dict(p=p,k=k,trials=trials,mean=mean,
                         nz_frac=nz/trials,
                         pred_k3p2=pred_indep,pred_k2p=pred_corr,
                         verdict=which))
        print(f"p={p} k={k}: mean={mean:.4f}  "
              f"k^3/p^2={pred_indep:.4f}  k^2/p={pred_corr:.3f}"
              f"  nz%={100*nz/trials:.1f}  -> {which}")
    json.dump(rows, open(os.path.join(ART,"run44_mean.json"),"w"), indent=1)


if __name__=="__main__":
    main()
