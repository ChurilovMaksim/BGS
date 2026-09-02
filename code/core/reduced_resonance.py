"""
RUN 17: Characterize BAD unmatched label patterns (large N_3).
Find all (a,b) in (F_p^x)^8 with N_3 >= threshold; look for algebraic
structure (factorisation of the bidegree-2 polynomial, proportionalities,
etc.).
"""
import os, sys, json
import numpy as np
from sympy import primitive_root

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_formula_strong import find_orbit_H


def n3_count(p, H, a, b):
    """Count reduced solutions (u2,u3,u4) in H^3 satisfying
    a1 - a2 u2 + a3 u3 - a4 u4     = 0
    b1 - b2/u2 + b3/u3 - b4/u4     = 0
    (signs absorbed). Returns count."""
    inv={h:pow(h,p-2,p) for h in H}
    cnt=0
    # Precompute map (u2,u3) -> required u4 from eq1
    req={}
    for u2 in H:
        for u3 in H:
            num=(a[0]-a[1]*u2+a[2]*u3)%p
            if a[3]==0: continue
            u4=num*pow(a[3],p-2,p)%p
            req.setdefault((u2,u3),u4)
    for (u2,u3),u4 in req.items():
        if u4 not in H: continue
        # check eq2
        lhs=(b[0]-b[1]*inv[u2]+b[2]*inv[u3])%p
        rhs=(b[3]*inv[u4])%p
        if lhs==rhs: cnt+=1
    return cnt


def poly_factorises(p, a, b):
    """
    Bidegree-2 polynomial after eliminating u4:
      F(u2,u3) = (a1-a2*u2+a3*u3)*(b1-b3/u2-b2/u3)+b4*a3? ...
    We work with cleared-denominator version:
      G(u2,u3)=(a1-a2*u2+a3*u3)*(b1*u2*u3-b3*u3-b2*u2)-b4*a3? ...
    Simpler: test whether conic has rational components over F_p
    by checking if discriminant (as quadratic in u3) is a perfect
    square for many u2.
    """
    # For fixed u2, F as quadratic in u3: A u3^2+B u3+C
    # A = a3*(b1*u2-b2)*1? -- need concrete expansion; skip heavy algebra,
    # use numeric probe: count u2 where disc is QR.
    return None  # placeholder


def main():
    print("=== RUN 17: find BAD patterns ===")
    rng=np.random.default_rng(31337)
    p=101
    g=int(primitive_root(p))
    k=10
    alpha=pow(g,(p-1)//k,p)
    H=set(); x=1
    for _ in range(k): H.add(x); x=x*alpha%p
    Hlist=sorted(H)

    bad=[]
    trials=20000
    for t in range(trials):
        a=[int(rng.integers(1,p)) for _ in range(4)]
        b=[int(rng.integers(1,p)) for _ in range(4)]
        n=n3_count(p,H,a,b)
        if n>=5:
            bad.append((n,a,b))
            if len(bad)>=15: break
    print(f"found {len(bad)} patterns with N_3>=5 out of {t+1} trials")
    for (n,a,b) in bad[:10]:
        print(f"  N_3={n} a={a} b={b}")

    # Check proportionality conditions on bad set
    def prop(x,y,z,w): return (x*w-y*z)%p==0
    n_prop13=n_prop24=n_cross=0
    for (n,a,b) in bad:
        p13=prop(a[0],b[0],a[2],b[2])
        p24=prop(a[1],b[1],a[3],b[3])
        cr =prop(a[0],b[0],a[3],b[3])
        if p13: n_prop13+=1
        if p24: n_prop24+=1
        if cr: n_cross+=1
    print(f"among bad: prop13={n_prop13}, prop24={n_prop24}, cross={n_cross}")


if __name__=="__main__":
    main()
