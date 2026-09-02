"""DECISIVE: brute-force pair classifier for r=6 arithmetic strata.
Group 3-subsets of H by (sum, recip-sum); inside each group count
unordered pairs by intersection size j=0,1,2 (j=3 impossible off
diagonal). Tests candidate lock: N1==N0 and N2==N0/2."""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys, os, json
from itertools import combinations
from sympy import primitive_root

sys.path.insert(0, _BGS_ROOT + r"\src")
ART = _BGS_ROOT + r"\artifacts"


def classify(p, k):
    g = int(primitive_root(p))
    alpha = pow(g, (p - 1) // k, p)
    H = []; x = 1
    for _ in range(k):
        H.append(x); x = x * alpha % p
    inv = {h: pow(h, p - 2, p) for h in H}
    groups = {}
    for tri in combinations(H, 3):
        s = sum(tri) % p
        r = sum(inv[h] for h in tri) % p
        groups.setdefault((s, r), []).append(frozenset(tri))
    N = {0: 0, 1: 0, 2: 0}
    for lst in groups.values():
        if len(lst) < 2:
            continue
        for i in range(len(lst)):
            for j2 in range(i + 1, len(lst)):
                j = len(lst[i] & lst[j2])
                N[j] = N.get(j, 0) + 1
    return N


def main():
    cfgs = [(199, 22), (331, 22), (131, 26), (521, 26),
            (101, 10), (211, 14), (401, 16), (101, 20)]
    out = []
    print(f"{'cfg':>12} {'N0':>6} {'N1':>6} {'N2':>6}  "
          f"N1/N0  N2/N0   pred36*N0")
    for (p, k) in cfgs:
        N = classify(p, k)
        n0, n1, n2 = N.get(0, 0), N.get(1, 0), N.get(2, 0)
        r10 = round(n1 / n0, 3) if n0 else None
        r20 = round(n2 / n0, 3) if n0 else None
        out.append(dict(p=p, k=k, N0=n0, N1=n1, N2=n2,
                        strata_pred=dict(s16=72 * n0,
                                         s11112=72 * n1,
                                         s1122=72 * n2)))
        print(f"({p},{k}): {n0:>6} {n1:>6} {n2:>6}  "
              f"{r10}  {r20}   {72*n0}")
    json.dump(out, open(os.path.join(ART,
        "phase3_pair_classifier.json"), "w"), indent=1)
    print("saved artifacts/phase3_pair_classifier.json")


if __name__ == "__main__":
    main()
