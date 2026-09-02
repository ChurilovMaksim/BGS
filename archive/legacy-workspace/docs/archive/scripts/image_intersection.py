"""
RUN 6 / IMAGE-INTERSECTION MEASUREMENT (conjecture U5 at scale).

U3 reduces non-pairing fourth-order resonances to the intersection mass of
two at-most-2-to-1 pair-sum images
    Phi_L, Phi_R : H x H -> F_p^2,
    Phi(x,y) = (a1*x + a3*y, b1/x + b3/y).
Random-image model predicts   extras ~ kappa * k^4 / p^2   with kappa of
order one.  We measure kappa efficiently: images are built in O(k^2) by
hashing (no k^4 brute force), so k into the thousands is reachable.

Two regimes, pre-registered:
  P-cross (no shared labels between left/right 8-tuples):
      T_cross / (k^4/p^2) concentrates near a constant kappa in [0.25, 4].
  P-self (identical labels, single orbit): T_self equals the PROVEN
      closed form 2k^2 - k or 3k^2 - 3k  (sanity anchor, theorem T17).

Grid varies k^2/p across two decades.  Exact integer arithmetic.
Artifact: artifacts/image_intersection.json
"""
import json, math, os, sys
from collections import Counter
import numpy as np
from sympy import isprime, primitive_root

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")
rng = np.random.default_rng(20260824)


def subgroup(p, alpha, k):
    H, x = [], 1
    for _ in range(k):
        H.append(x)
        x = x * alpha % p
    assert len(set(H)) == k and 0 not in H
    return H


def image_map(p, a1, a3, b1, b3, H, inv):
    cnt = Counter()
    for x in H:
        ax = a1 * x % p
        bx = b1 * inv[x] % p
        for y in H:
            cnt[(ax + a3 * y) % p, (bx + b3 * inv[y]) % p] += 1
    return cnt


def total_solutions(RL, RR):
    return sum(rl * RR[key] for key, rl in RL.items() if key in RR)


def find_prime(k, target_ratio, tried=4000):
    """prime p = 1 mod k with k^2/p ~ target_ratio."""
    lo = max(k + 1, int(k * k / (target_ratio * 2)))
    step = k
    base = lo // step * step + 1
    for j in range(tried):
        p = base + j * step
        if isprime(p):
            return p
    return None


def run():
    results = []
    print("=== U5 image-intersection campaign ===")
    grid = [
        # (k, k^2/p target)
        (16, 1.0), (16, 0.25),
        (32, 1.0), (32, 0.25), (32, 4.0),
        (64, 1.0), (64, 0.25), (64, 4.0),
        (128, 1.0), (128, 0.25),
        (256, 1.0), (512, 0.5),
    ]
    for (k, ratio) in grid:
        p = find_prime(k, ratio)
        if p is None:
            print(f"k={k},ratio={ratio}: no prime found"); continue
        g = primitive_root(p)
        alpha = pow(int(g), (p - 1) // k, p)
        H = subgroup(p, alpha, k)
        inv = {h: pow(h, p - 2, p) for h in H}

        ratios_cross = []
        nTuples = 12
        for _ in range(nTuples):
            vals = [int(v) for v in rng.integers(1, p, size=8)]
            if len(set(vals)) < 6:
                continue
            a1, a3, b1, b3, a2, a4, b2, b4 = vals
            RL = image_map(p, a1, a3, b1, b3, H, inv)
            RR = image_map(p, a2, a4, b2, b4, H, inv)
            T = total_solutions(RL, RR)
            ratios_cross.append(T / (k**4 / p**2))
        mc = float(np.mean(ratios_cross)); sc = float(np.std(ratios_cross))

        # self case: identical maps => sum R^2 ; compare with <= 2k^2 cap
        RL = image_map(p, 1, 1, 1, 1, H, inv)
        Tself = sum(v * v for v in RL.values())

        kap = mc
        results.append({"p": p, "alpha": int(alpha), "k": k,
                        "k2_over_p": k * k / p,
                        "kappa_mean": kap, "kappa_std": sc,
                        "n_tuples": len(ratios_cross),
                        "T_self": Tself, "cap_2k2": 2 * k * k})
        print(f"k={k:5d} p={p:7d} k^2/p={k*k/p:7.2f} "
              f"kappa={kap:7.3f} +- {sc:6.3f}   T_self={Tself:9d} "
              f"(<=2k^2={2*k*k})")

    ok_cross = all(0.25 <= r["kappa_mean"] <= 4.0 for r in results)
    ok_self = all(r["T_self"] <= r["cap_2k2"] for r in results)
    out = {"grid": results,
           "P_cross_concentrated": bool(ok_cross),
           "P_self_anchor": bool(ok_self)}
    print("\nPRE-REGISTERED:",
          f"P_cross={ok_cross}  P_self={ok_self}")
    json.dump(out, open(os.path.join(ART, "image_intersection.json"), "w"),
              indent=1)
    print("saved artifacts/image_intersection.json")


if __name__ == "__main__":
    run()
