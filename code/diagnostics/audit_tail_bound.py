"""
RUN 36 AUDIT-3: Systematic search for violations of N_3 <= floor(k^2/p)+1.
Find true constant c* such that N_3 <= c*(k^2/p+1).
"""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys, os, json
import numpy as np
from sympy import primitive_root, primerange
sys.path.insert(0, _BGS_ROOT + r"\src")
from reduced_resonance import n3_count

ART=_BGS_ROOT + r"\artifacts"


def main():
    rng=np.random.default_rng(2026)
    print("=== RUN 36 audit tight-bound constant ===")
    records=[]
    for p in list(primerange(50,1500)):
        g=int(primitive_root(p))
        ks=[d for d in range(4,p//3) if (p-1)%d==0]
        if not ks: continue
        k=int(rng.choice(ks))
        alpha=pow(g,(p-1)//k,p)
        H=set(); x=1
        for _ in range(k): H.add(x); x=x*alpha%p
        mx=0
        trials=500
        for t in range(trials):
            a=[int(rng.integers(1,p)) for _ in range(4)]
            b=[int(rng.integers(1,p)) for _ in range(4)]
            n=n3_count(p,H,a,b)
            if n>mx: mx=n
        kp=k*k/p
        pred_floor=kp//1+1   # floor + 1
        ratio_strict=mx/pred_floor if pred_floor>0 else float('inf')
        ratio_loose=mx/(kp+1)
        records.append(dict(p=p,k=k,maxN3=mx,
                            floor_plus1=pred_floor,
                            r_strict=round(ratio_strict,3),
                            r_loose=round(ratio_loose,3)))
    arr_s=np.array([r["r_strict"] for r in records])
    arr_l=np.array([r["r_loose"] for r in records])
    print(f"configs tested: {len(records)}")
    print(f"vs floor+1: min={arr_s.min():.2f} med={np.median(arr_s):.2f} "
          f"max={arr_s.max():.2f}")
    print(f"vs k^2/p+1: min={arr_l.min():.2f} med={np.median(arr_l):.2f} "
          f"max={arr_l.max():.2f}")
    json.dump(records, open(os.path.join(ART,"run36_audit.json"),"w"), indent=1)


if __name__=="__main__":
    main()
