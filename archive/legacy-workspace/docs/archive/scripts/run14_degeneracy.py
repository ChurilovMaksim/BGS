"""
RUN 14b: Identify which unmatched-label patterns give LARGE sol counts,
and check whether they are DEGENERATE (proportional forms, v=0, etc.).

Degeneracy criteria for the pair-map (h1,h3) -> (u,v):
    u = a1 h1 + a3 h3
    v = b1/h1 + b3/h3
Proportional forms <=> exists lambda != 0 with b1=lambda*a1, b3=lambda*a3
(up to swapping slots). Then u,v become dependent and fibre can be large.
"""
import math, os, sys, json
import numpy as np
from sympy import primitive_root

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_formula_strong import find_orbit_H

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")


def sol_count(p, H, a, b):
    inv = {h: pow(h, p-2, p) for h in H}
    Hlist = sorted(H)
    left = {}
    for h1 in Hlist:
        s1 = a[0]*h1 % p; t1 = b[0]*inv[h1] % p
        for h3 in Hlist:
            kk = ((s1+a[2]*h3)%p, (t1+b[2]*inv[h3])%p)
            left[kk] = left.get(kk,0)+1
    tot = 0
    for h2 in Hlist:
        s2=(-a[1]*h2)%p; t2=(-b[1]*inv[h2])%p
        for h4 in Hlist:
            kk=((s2-a[3]*h4)%p,(t2-b[3]*inv[h4])%p)
            if kk in left: tot+=left[kk]
    return tot


def is_degenerate(p, a, b):
    """Check whether any pair-slot form is proportional or degenerate."""
    # slot pair {1,3}: proportional iff a1*b3 == a3*b1 mod p
    prop13 = (a[0]*b[2] - a[2]*b[0]) % p == 0
    prop24 = (a[1]*b[3] - a[3]*b[1]) % p == 0
    # also cross-proportional (a1,b1) parallel to (a3,b3)? same thing here
    # v=0 degenerate iff both b entries vanish (excluded since b_i in [1,p))
    return prop13 or prop24


def main():
    print("=== RUN 14b: degenerate vs generic ===")
    rng = np.random.default_rng(123)
    results = []

    for (p, k_list) in [(101,[10,20,25]), (199,[11,18]),
                        (211,[13,21]), (4099,[21,35])]:
        g = int(primitive_root(p))
        for k in k_list:
            if (p-1)%k!=0: continue
            alpha = pow(g,(p-1)//k,p)
            H=set(); x=1
            for _ in range(k): H.add(x); x=x*alpha%p

            n_degen_nonzero = n_gen_nonzero = 0
            max_ratio_gen = 0.0
            max_ratio_deg = 0.0
            k4p2 = k**4/p**2
            for trial in range(200):
                a=[int(rng.integers(1,p)) for _ in range(4)]
                b=[int(rng.integers(1,p)) for _ in range(4)]
                s=sol_count(p,H,a,b)
                dg=is_degenerate(p,a,b)
                if s>0:
                    ratio=s/k4p2
                    if dg:
                        n_degen_nonzero+=1
                        max_ratio_deg=max(max_ratio_deg,ratio)
                    else:
                        n_gen_nonzero+=1
                        max_ratio_gen=max(max_ratio_gen,ratio)
            results.append(dict(p=p,k=k,
                                gen_nonzero=n_gen_nonzero,
                                degen_nonzero=n_degen_nonzero,
                                max_r_gen=round(max_ratio_gen,2),
                                max_r_deg=round(max_ratio_deg,2)))
            print(f"p={p} k={k}: generic nz={n_gen_nonzero}/200 "
                  f"(max r={max_ratio_gen:.2f}), "
                  f"degen nz={n_degen_nonzero}/200 "
                  f"(max r={max_ratio_deg:.2f})")

    json.dump(results, open(os.path.join(ART,"run14_degeneracy.json"),"w"),
              indent=1)
    print("saved artifacts/run14_degeneracy.json")


if __name__=="__main__":
    main()
