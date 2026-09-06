"""
RUN 15: Distinguish O(k) vs O(k^4/p^2) vs O(max(k, k^4/p^2)).
Fix k, vary p over wide range. Track max_sol / predictions.
"""
import os, sys, json
import numpy as np
from sympy import primitive_root, primerange

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from run14_degeneracy import sol_count

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")


def main():
    rng = np.random.default_rng(2026)
    print("=== RUN 15: scaling test ===")
    results = []
    target_k_list = [8, 16, 32]

    for k_target in target_k_list:
        primes = [p for p in primerange(100, 5000)
                  if (p-1) % k_target == 0][:6]
        for p in primes:
            g = int(primitive_root(p))
            alpha = pow(g, (p-1)//k_target, p)
            H = set(); x = 1
            for _ in range(k_target): H.add(x); x = x*alpha % p
            mx = 0
            for _ in range(300):
                a=[int(rng.integers(1,p)) for _ in range(4)]
                b=[int(rng.integers(1,p)) for _ in range(4)]
                s=sol_count(p,H,a,b)
                if s>mx: mx=s
            kp2 = k_target**4 / p**2
            rec = dict(k=k_target, p=p, max_sol=mx,
                       ratio_over_k=round(mx/k_target, 3),
                       ratio_over_k4p2=round(mx/max(kp2,1e-9), 2),
                       ratio_over_max=round(mx/max(k_target,kp2), 3))
            results.append(rec)
            print(f"k={k_target} p={p}: max={mx} "
                  f"/k={rec['ratio_over_k']:.2f} "
                  f"/k4p2={rec['ratio_over_k4p2']:.2f} "
                  f"/max={rec['ratio_over_max']:.2f}")

    json.dump(results,
              open(os.path.join(ART,"run15_scaling.json"),"w"), indent=1)

    # Summary
    print("\nSummary of /max ratios:", end=" ")
    rmaxes = [r["ratio_over_max"] for r in results]
    print(f"min={min(rmaxes)}, max={max(rmaxes):.2f}")


if __name__ == "__main__":
    main()
