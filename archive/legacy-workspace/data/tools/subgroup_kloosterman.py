#!/usr/bin/env python3
"""
subgroup_kloosterman.py — Line C artifact
=========================================

Compute S(a,b) = sum_{h in H} e_p(a*h + b/h) for H a multiplicative
subgroup of F_p^* of order k, to mpmath 30-digit precision.

Sums evaluated DIRECTLY (BruteForce mode) for the calibrator (k = 1
rank-1 reduction) and head-to-head (k = 4, 8, 12 at p in {41, 113, 521}).

Usage:
    python tools/subgroup_kloosterman.py --calibrator
    python tools/subgroup_kloosterman.py --head-to-head
    python tools/subgroup_kloosterman.py --k sweep
"""
import argparse
import json
import math
import sys
from pathlib import Path

import mpmath as mp

# --- Global mpmath context ---
mp.mp.dps = 40   # 40 decimal digits; round to 30 in output

TWO_PI = mp.mpf(2) * mp.pi


def primitive_root(p):
    """Smallest primitive root of F_p^*. Brute force for p up to ~10^4."""
    p = int(p)
    if p == 2:
        return 1
    phi = p - 1
    # factor phi
    n = phi
    factors = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.add(d)
            n //= d
        d += 1
    if n > 1:
        factors.add(n)
    for g in range(2, p):
        ok = True
        for q in factors:
            if pow(g, phi // q, p) == 1:
                ok = False
                break
        if ok:
            return g
    raise RuntimeError(f"no primitive root found for p={p}")


def subgroup(p, k):
    """Multiplicative subgroup of F_p^* of order k; H = <g^((p-1)/k)>."""
    p = int(p)
    k = int(k)
    if (p - 1) % k != 0:
        raise ValueError(f"k={k} does not divide p-1={p-1}")
    g = primitive_root(p)
    step = (p - 1) // k
    alpha = pow(g, step, p)
    H = []
    x = 1
    for _ in range(k):
        H.append(x)
        x = (x * alpha) % p
    assert len(set(H)) == k, f"subgroup construction failed for p={p}, k={k}"
    return alpha, H


def kloosterman_subgroup(p, k, a, b):
    """
    S(a,b) = sum_{h in H} e_p(a*h + b/h)   computed at mp.dps precision.

    Here p is the modulus and e_p(x) = exp(2*pi*i*x / p).
    """
    p = int(p)
    a = int(a) % p
    b = int(b) % p
    _, H = subgroup(p, k)
    s = mp.mpc(0, 0)
    p_mp = mp.mpf(p)
    a_mp = mp.mpf(a)
    b_mp = mp.mpf(b)
    for h in H:
        h_mp = mp.mpf(h)
        inv = mp.mpf(pow(h, -1, p))   # exact integer mod p
        phase = (a_mp * h_mp + b_mp * inv) / p_mp
        s += mp.exp(TWO_PI * mp.mpc(0, 1) * phase)
    return s

def main():
    out = Path(__file__).parent.parent / "artifacts" / "ring2"
    out.mkdir(parents=True, exist_ok=True)

    ap = argparse.ArgumentParser()
    ap.add_argument("--calibrator", action="store_true")
    ap.add_argument("--head-to-head", action="store_true")
    ap.add_argument("--single", nargs=4, type=int)
    args = ap.parse_args()

    if args.calibrator:
        # Calibrator: rank-1 case H = F_p^* (k = p-1). Then S(a,b) is the
        # ordinary Kloosterman sum, |S| <= 2*sqrt(p) by Weil (genus 1 curve
        # x + y + x*y*0 = 1 / via Kloosterman-sheaf trace). See OSV §2.2:
        # "K_q(G;a,b) << q^{1/2}".
        results = []
        for p in [7, 11, 13, 17, 19, 23, 29, 31, 37, 41]:
            a, b = 1, 1
            k = p - 1
            S = kloosterman_subgroup(p, k, a, b)
            weil = 2.0 * float(mp.sqrt(mp.mpf(p)))
            results.append({
                "p": p, "k": k, "a": a, "b": b,
                "S": mp.nstr(S, 30),
                "|S|": float(mp.nstr(abs(S), 12)),
                "Weil_2sqrtp": weil,
                "passes_Weil": float(mp.nstr(abs(S), 12)) <= weil + 1e-10,
            })
        with open(out / "line_C_calibrator.json", "w") as f:
            json.dump(results, f, indent=2)
        print("Wrote artifacts/ring2/line_C_calibrator.json")
        for r in results:
            print(f"  p={r['p']:3d} k={r['k']:2d} a=b=1: |S| = {r['|S|']:9.5f}  "
                  f"Weil<=2sqrt(p)={r['Weil_2sqrtp']:8.4f}  pass={r['passes_Weil']}")
        return

    if args.head_to_head:
        # Head-to-head: p in {41, 113, 521}. The brief asks for k in {4, 8, 12};
        # 8 does not divide 40, 12 does not divide 40/112/520, so we use
        # the closest valid k's. We honor the spirit (k << p) and report
        # the full table at every (p, k) with k | p-1 from {4, 5, 8, 10, 13}.
        configs = []
        for p in [41, 113, 521]:
            valid_ks = [k for k in [4, 5, 8, 10, 13, 20, 26] if (p - 1) % k == 0]
            for k in valid_ks:
                _, H = subgroup(p, k)
                best = (0.0, 0, 0, 0, 0)
                rows = []
                # grid over a in {1..min(k, 6)}, b in {1..min(k, 6)} (k coprime).
                A = [x for x in range(1, min(k + 1, 8)) if math.gcd(x, p) == 1]
                B = [x for x in range(1, min(k + 1, 8)) if math.gcd(x, p) == 1]
                for a in A:
                    for b in B:
                        S = kloosterman_subgroup(p, k, a, b)
                        mag = float(mp.nstr(abs(S), 12))
                        rows.append({"a": a, "b": b, "S": mp.nstr(S, 30), "|S|": mag})
                        if mag > best[0]:
                            best = (mag, a, b, mp.nstr(S, 30), rows[-1])
                configs.append({
                    "p": p, "k": k,
                    "H_size": len(H),
                    "H_first5": H[:5],
                    "alpha": primitive_root(p),
                    "alpha_step": (p - 1) // k,
                    "sup_|S|": best[0],
                    "argmax": {"a": best[1], "b": best[2], "S_30": best[3]},
                    "rows": rows,
                })
        with open(out / "line_C_head_to_head.json", "w") as f:
            json.dump(configs, f, indent=2)
        print("Wrote artifacts/ring2/line_C_head_to_head.json")
        for c in configs:
            print(f"  p={c['p']:3d} k={c['k']:2d} |H|={c['H_size']:2d}  "
                  f"sup |S| = {c['sup_|S|']:8.5f}  at a={c['argmax']['a']} b={c['argmax']['b']}")
        return

    ap.print_help()


if __name__ == "__main__":
    main()
