"""
RUN 14 / Open Problem 1: UNMATCHED LABELS numerical exploration.

For general label patterns (a_1,a_2,a_3,a_4; b_1,b_2,b_3,b_4) and signs
(+,-,+,-), count solutions to
    a1 h1 - a2 h2 + a3 h3 - a4 h4     = 0  mod p
    b1/h1 - b2/h2 + b3/h3 - b4/h4     = 0  mod p
with all h_i in H.

Hypothesis: for GENERIC labels (no accidental degeneracy),
    sol(A,B) = O_F(k^4 / p^2).
Degenerate cases (proportional forms, v=0, etc.) may give more.

We scan many random label patterns across several (p, k) and record
sol / (k^4/p^2) ratios.
"""
import math, os, sys, json
import numpy as np
from sympy import primitive_root

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_formula_strong import find_orbit_H

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")


def sol_count(p, H, a, b):
    """
    Count solutions with signs (+,-,+,-) and labels a=(a1..a4), b=(b1..b4):
      a1 h1 - a2 h2 + a3 h3 - a4 h4 = 0
      b1/h1 - b2/h2 + b3/h3 - b4/h4 = 0
    Uses meet-in-the-middle on pairs (1,3) vs (2,4).
    """
    inv = {h: pow(h, p-2, p) for h in H}
    Hlist = sorted(H)
    left = {}
    for h1 in Hlist:
        s1 = a[0]*h1 % p
        t1 = b[0]*inv[h1] % p
        for h3 in Hlist:
            kk = ((s1 + a[2]*h3) % p, (t1 + b[2]*inv[h3]) % p)
            left[kk] = left.get(kk, 0) + 1
    total = 0
    for h2 in Hlist:
        s2 = (-a[1]*h2) % p   # sign is minus
        t2 = (-b[1]*inv[h2]) % p
        base_s = (s2) ; base_t = t2
        # need right side = -(a4 h4), -(b4 inv h4)
        for h4 in Hlist:
            kk = ((base_s - a[3]*h4) % p, (base_t - b[3]*inv[h4]) % p)
            if kk in left:
                total += left[kk]
    return total


def main():
    print("=== RUN 14: unmatched labels exploration ===")
    rng = np.random.default_rng(42)
    results = []

    test_cases = [
        (101, None), (199, None), (211, None), (4099, None)
    ]
    n_random_per_case = 30

    for (p, _) in test_cases:
        g = int(primitive_root(p))
        # pick a few subgroup sizes k dividing p-1
        divisors_k = [d for d in range(5, min(60, p))
                      if (p-1) % d == 0][:4]
        for k in divisors_k:
            alpha = pow(g, (p-1)//k, p)
            H = set(); x = 1
            for _ in range(k): H.add(x); x = x*alpha % p

            k4_over_p2 = k**4 / p**2
            ratios = []
            for trial in range(n_random_per_case):
                a = [int(rng.integers(1, p)) for _ in range(4)]
                b = [int(rng.integers(1, p)) for _ in range(4)]
                s = sol_count(p, H, a, b)
                if s > 0:
                    ratios.append(s / k4_over_p2)
            nonzero = len(ratios)
            max_ratio = max(ratios) if ratios else 0.0
            mean_ratio = float(np.mean(ratios)) if ratios else 0.0
            results.append(dict(
                p=p, k=k, n_trials=n_random_per_case,
                n_nonzero=nonzero,
                max_ratio=round(max_ratio, 3),
                mean_ratio=round(mean_ratio, 3)))
            print(f"p={p} k={k}: nonzero {nonzero}/{n_random_per_case}, "
                  f"max ratio={max_ratio:.2f}, mean={mean_ratio:.2f}, "
                  f"k^4/p^2={k4_over_p2:.4f}")

    json.dump(results, open(os.path.join(ART, "run14_unmatched_scan.json"), "w"),
              indent=1)
    print("saved artifacts/run14_unmatched_scan.json")

    # Summary
    all_ratios = [r["max_ratio"] for r in results]
    print(f"\nGlobal max ratio over all cases: {max(all_ratios):.2f}")


if __name__ == "__main__":
    main()
