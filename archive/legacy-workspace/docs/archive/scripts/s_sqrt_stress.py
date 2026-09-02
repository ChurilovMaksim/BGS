"""
RUN 8-A / STRESS TEST of the square-root law for twisted subgroup
Kloosterman sums  S(a,b) = sum_{h in H} e_p(a h + b/h).

Katz-tier (tier ii of U4) needs: sup_{(a,b)!=(0,0)} |S| << min(k, p^{1/2})
-- ideally ~ sqrt(k) x polylog (random-walk scale).
Falsification search:
  * random (a,b) grid per subgroup;
  * structured families: b = +-a, b = c*a (c in small set), a*b = const,
    a = 0 or b = 0 (monomial cases, known theory -- reported separately).
Report max |S|/sqrt(k), quantiles, spike list.
Exact arithmetic (cispi on integer residues). Artifact: artifacts/s_sqrt_stress.json
Pre-registered: if max_random/sqrt(k) stays <= 8 across regimes -> support;
a spike > 16 sqrt(k) at generic (a,b) => DISCOVERY (hidden invariant).
"""
import json, os
import numpy as np
from sympy import isprime, primitive_root

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")
rng = np.random.default_rng(20260824)


def subgroup(p, alpha, k):
    H, x = [], 1
    for _ in range(k):
        H.append(x)
        x = x * alpha % p
    return H


def find_prime_near(k, expo_target):
    """prime p ~ k^(1/expo_target) with p = 1 mod k."""
    approx = int(k ** (1.0 / expo_target))
    lo = max(k + 1, approx - 400 * k)
    base = lo // k * k + 1
    best = None
    for j in range(800):
        p = base + j * k
        if isprime(p):
            return p
    return None


def run():
    out = {"regimes": []}
    for expo in ("1/4", "1/3", "1/2"):
        k = {("1/4"): 64, ("1/3"): 128, ("1/2"): 512}[expo]
        p = find_prime_near(k, float(eval(expo)))
        if p is None:
            continue
        g = primitive_root(p)
        alpha = pow(int(g), (p - 1) // k, p)
        H = subgroup(p, alpha, k)
        inv = [pow(h, p - 2, p) for h in H]
        Hf = np.array(H, dtype=np.int64)
        Invf = np.array(inv, dtype=np.int64)

        def S(a, b):
            ph = (a * Hf + b * Invf) % p
            z = np.exp(2j * np.pi * ph / p)
            return abs(z.sum())

        nrand = 2500
        vals = []
        Aarr = rng.integers(1, p, size=nrand)
        Barr = rng.integers(1, p, size=nrand)
        for a, b in zip(Aarr, Barr):
            vals.append(S(int(a), int(b)))
        vals = np.array(vals)
        sq = math.isqrt(k)
        fam = {}
        for cname, gen in (
            ("b=a", lambda i: (Hf[i], Hf[i])),
            ("b=-a", lambda i: (Hf[i], (-Hf[i]) % p)),
            ("ab=1", lambda i: (Hf[i], inv[i])),
            ("a=0", lambda i: (0, Hf[i])),
            ("b=0", lambda i: (Hf[i], 0)),
        ):
            fvals = [S(*gen(i)) for i in range(k)]
            fam[cname] = {"max": float(max(fvals)),
                          "over_sq": float(max(fvals) / sq)}
        rec = {
            "expo": expo, "k": k, "p": p,
            "random_max_over_sq": float(vals.max() / sq),
            "random_median_over_sq": float(np.median(vals) / sq),
            "random_q95_over_sq": float(np.quantile(vals, 0.95) / sq),
            "families": fam,
        }
        out["regimes"].append(rec)
        print(f"[{expo}] k={k} p={p}: random max/sqrt(k)={rec['random_max_over_sq']:.2f} "
              f"median={rec['random_median_over_sq']:.2f} q95={rec['random_q95_over_sq']:.2f}")
        for cn, fv in fam.items():
            print(f"    family {cn:6s}: max/sqrt(k)={fv['over_sq']:.2f}")

    json.dump(out, open(os.path.join(ART, "s_sqrt_stress.json"), "w"), indent=1)
    print("saved artifacts/s_sqrt_stress.json")


import math
run()
