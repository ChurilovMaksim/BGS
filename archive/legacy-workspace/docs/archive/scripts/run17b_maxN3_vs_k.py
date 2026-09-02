"""RUN 17b: max N_3 as function of k at fixed p."""
import sys, os
import numpy as np
from sympy import primitive_root
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + r"\BGS\src")
from run17_bad_patterns import n3_count

def main():
    rng=np.random.default_rng(555)
    print("=== RUN 17b ===")
    for p in (401,):
        g=int(primitive_root(p))
        for k in [10,20,40,80,100,200]:
            if (p-1)%k!=0: continue
            alpha=pow(g,(p-1)//k,p)
            H=set(); x=1
            for _ in range(k): H.add(x); x=x*alpha%p
            mx=0; arg=None
            for t in range(3000):
                a=[int(rng.integers(1,p)) for _ in range(4)]
                b=[int(rng.integers(1,p)) for _ in range(4)]
                n=n3_count(p,H,a,b)
                if n>mx: mx=n; arg=(a,b)
            print(f"p={p} k={k}: max_N3={mx}")

if __name__=="__main__":
    main()
