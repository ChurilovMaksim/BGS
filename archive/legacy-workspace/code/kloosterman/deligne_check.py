"""
RUN 9-THEOREM / verify the DELIGNE bound for the complete intersection

    V : sum_i lam_i x_i = 0,   sum_i mu_i / x_i = 0   on (G_m)^4,

    |delta_N| := | N - (p-1)^4/p^2 |  <=  C * p^{3/2}

for generic (lam, mu) labels (non-degenerate quadruples).
Counting via sorted-array intersection: O(p^2 log p).
Artifact: artifacts/deligne_check.json
Pre-register: ratio delta_N / p^{3/2} bounded by an O(10) constant,
roughly stable across p and across generic label sets.
"""
import json, math, os
import numpy as np
from sympy import isprime

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")
rng = np.random.default_rng(31337)


def count_N(p, lam, mu):
    """N = #{(x1..x4) in (F_p^x)^4 : lam.x = 0 mod p, mu.(1/x) = 0 mod p}
    lam = (l1,l2,l3,l4), mu = (m1,m2,m3,m4); uses pairing of (x1,x2) with
    (x3,x4): l1 x1 + l2 x2 = -(l3 x3 + l4 x4), same for mu-part."""
    xs = np.arange(1, p, dtype=np.int64)
    inv = np.array([pow(int(x), p - 2, p) for x in xs], dtype=np.int64)

    def pair_keys(a, b, inv_a, inv_b):
        # keys over all pairs (x_i, x_j): a*x_i + b*x_j , inv_a/x_i + inv_b/x_j
        n = len(xs)
        K1 = (a * xs[:, None] + b * xs[None, :]) % p
        K2 = (inv_a * inv[inv_a * 0 + slice(None)] if False else None)
        return K1

    # build pair tables for (1,2):
    K12a = (lam[0] * xs[:, None] + lam[1] * xs[None, :]) % p
    K12b = (mu[0] * inv[:, None] + mu[1] * inv[None, :]) % p
    key12 = (K12a * p + K12b).ravel()
    del K12a, K12b
    K34a = ((-lam[2]) * xs[:, None] - lam[3] * xs[None, :]) % p
    K34b = ((-mu[2]) * inv[:, None] - mu[3] * inv[None, :]) % p
    key34 = (K34a * p + K34b).ravel()
    del K34a, K34b

    key12.sort(); key34.sort()
    # count matches via searchsorted merge
    i = j = cnt = 0
    n1, n2 = len(key12), len(key34)
    while i < n1 and j < n2:
        if key12[i] == key34[j]:
            ii = i
            while ii < n1 and key12[ii] == key12[i]:
                ii += 1
            jj = j
            while jj < n2 and key34[jj] == key34[j]:
                jj += 1
            cnt += (ii - i) * (jj - j)
            i, j = ii, jj
        elif key12[i] < key34[j]:
            i += 1
        else:
            j += 1
    return cnt


def run():
    out = {"cases": []}
    for p in (1013, 2053, 4099):
        if not isprime(p):
            p += 1
            while not isprime(p):
                p += 1
        for trial in range(2):
            lam = [int(v) for v in rng.integers(1, p, size=4)]
            mu = [int(v) for v in rng.integers(1, p, size=4)]
            N = count_N(p, lam, mu)
            N0 = (p - 1) ** 4 / p ** 2
            delta = abs(N - N0)
            ratio = delta / p ** 1.5
            out["cases"].append({"p": p, "trial": trial, "N": N,
                                 "N0": N0, "delta": float(delta),
                                 "ratio_over_p15": ratio})
            print(f"p={p}: N={N}  N0={N0:.1f}  |dN|={delta:.3e}  "
                  f"|dN|/p^1.5={ratio:8.2f}")
    rs = [c["ratio_over_p15"] for c in out["cases"]]
    out["verdict"] = {"max_ratio": max(rs),
                      "stable": bool(max(rs) / min(rs) < 20)}
    print("PRE-REGISTER verdict:", out["verdict"])
    json.dump(out, open(os.path.join(ART, "deligne_check.json"), "w"),
              indent=1)
    print("saved artifacts/deligne_check.json")


run()
