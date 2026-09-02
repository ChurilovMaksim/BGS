"""
RUN 43 KEY DIAGNOSTIC: Why is N_3 ~ k^2/p instead of naive k^3/p^2?
Measure conditional probability P(eqII holds | u4 in H).
If it is ~1/k (not ~1/p), there is hidden algebraic correlation --
that would EXPLAIN the sharp bound and be a real discovery.
"""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys, os, json
import numpy as np
from sympy import primitive_root

sys.path.insert(0, _BGS_ROOT + r"\src")
from master_formula_strong import find_orbit_H

ART=_BGS_ROOT + r"\artifacts"


def diagnose(p, H, a, b):
    inv={h:pow(h,p-2,p) for h in H}
    n_in_H=0        # pairs (u2,u3) with u4 in H
    n_both=0        # ...and eqII also holds
    tot=0
    for u2 in H:
        c=(a[0]-a[1]*u2)%p
        for u3 in H:
            tot+=1
            num=(c+a[2]*u3)%p
            u4=num*pow(a[3],p-2,p)%p
            if u4 in H:
                n_in_H+=1
                lhs=(b[0]-b[1]*inv[u2]+b[2]*inv[u3])%p
                rhs=(b[3]*inv[u4])%p
                if lhs==rhs: n_both+=1
    return dict(total=tot,n_u4inH=n_in_H,n_full=n_both,
                cond_frac=(n_both/n_in_H) if n_in_H else 0.0)


def main():
    rng=np.random.default_rng(2026)
    print("=== RUN 43 conditional-probability diagnostic ===")
    rows=[]
    for (p,k) in [(101,10),(101,25),(211,15),(401,20)]:
        g=int(primitive_root(p))
        alpha=pow(g,(p-1)//k,p)
        H=set(); x=1
        for _ in range(k): H.add(x); x=x*alpha%p
        agg=dict(n_u4inH=0,n_full=0,total=0)
        trials=40
        fracs=[]
        for t in range(trials):
            a=[int(rng.integers(1,p)) for _ in range(4)]
            b=[int(rng.integers(1,p)) for _ in range(4)]
            r=diagnose(p,H,a,b)
            agg["n_u4inH"]+=r["n_u4inH"]; agg["n_full"]+=r["n_full"]
            agg["total"]+=r["total"]
            if r["n_u4inH"]>0: fracs.append(r["cond_frac"])
        pooled=agg["n_full"]/agg["n_u4inH"] if agg["n_u4inH"] else 0
        naive_eqII=1/p
        alt_hyp=1/k
        print(f"p={p} k={k}: P(eqII|u4inH)={pooled:.5f}   "
              f"1/p={naive_eqII:.5f}  1/k={alt_hyp:.5f}")
        rows.append(dict(p=p,k=k,cond=pooled,one_over_p=naive_eqII,
                         one_over_k=alt_hyp))
    json.dump(rows, open(os.path.join(ART,"run43_condprob.json"),"w"),
              indent=1)


if __name__=="__main__":
    main()
