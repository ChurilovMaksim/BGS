"""
RUN 14c: Test hypothesis sol_generic = O(k) rather than O(k^4/p^2).
Scan larger k range and record max_sol / k ratio.
"""
import os, sys, json
import numpy as np
from sympy import primitive_root

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from run14_degeneracy import sol_count

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")


def main():
    rng = np.random.default_rng(777)
    print("=== RUN 14c: test sol = O(k) ===")
    results = []
    for p in (211, 401, 809):
        g = int(primitive_root(p))
        ks = [d for d in range(8, min(200, p)) if (p-1)%d==0][:5]
        for k in ks:
            alpha=pow(g,(p-1)//k,p)
            H=set(); x=1
            for _ in range(k): H.add(x); x=x*alpha%p
            mx=0
            for _ in range(400):
                a=[int(rng.integers(1,p)) for _ in range(4)]
                b=[int(rng.integers(1,p)) for _ in range(4)]
                s=sol_count(p,H,a,b)
                if s>mx: mx=s
            results.append(dict(p=p,k=k,max_sol=mx,sol_over_k=round(mx/k,2)))
            print(f"p={p} k={k}: max_sol={mx}, max_sol/k={mx/k:.2f}")
    json.dump(results,
              open(os.path.join(ART,"run14_Ok_test.json"),"w"), indent=1)


if __name__=="__main__":
    main()
