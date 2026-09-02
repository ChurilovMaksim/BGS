"""PHASE 3: full partition-family decomposition of sol_6 across
(p,k) with both parities; per-family counts -> candidate laws."""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys, os, json
import numpy as np
from sympy import primitive_root

sys.path.insert(0, _BGS_ROOT + r"\src")
from master_formula_strong import find_orbit_H

ART = _BGS_ROOT + r"\artifacts"


def fam_label(sol):
    groups = {}
    for i, v in enumerate(sol):
        groups.setdefault(v, []).append(i)
    blocks = tuple(sorted(tuple(sorted(g)) for g in groups.values()))
    # canonical name: pattern of block sizes + whether -signs involved
    sizes = sorted(len(b) for b in blocks)
    neg_pairs = sum(
        1 for b in blocks if len(b) == 2
        and any(sol[b[0]] == (-sol[b[1]]) % 10**9 for _ in [0]))
    return f"sizes{sizes}", blocks


def enumerate_sols(p, H):
    inv = {h: pow(h, p - 2, p) for h in H}
    Hl = sorted(H)
    L = {}
    for h1 in Hl:
        s1 = h1; t1 = inv[h1]
        for h3 in Hl:
            s13 = (s1 + h3) % p; t13 = (t1 + inv[h3]) % p
            for h5 in Hl:
                kk = ((s13 + h5) % p, (t13 + inv[h5]) % p)
                L.setdefault(kk, []).append((h1, h3, h5))
    out = []
    for h2 in Hl:
        for h4 in Hl:
            s24 = (h2 + h4) % p          # MATCHES left sum (resonance)
            t24 = (inv[h2] + inv[h4]) % p
            for h6 in Hl:
                kk = ((s24 + h6) % p, (t24 + inv[h6]) % p)
                if kk in L:
                    for trip in L[kk]:
                        out.append(trip + (h2, h4, h6))
    return out


def main():
    results = {}
    cases = [(211, 10), (211, 14), (211, 15),
             (101, 10), (101, 20), (401, 16)]
    for (p, k) in cases:
        g = int(primitive_root(p))
        alpha = pow(g, (p - 1) // k, p)
        H = set(); x = 1
        for _ in range(k):
            H.add(x); x = x * alpha % p
        sols = enumerate_sols(p, H)
        from collections import Counter
        cnt = Counter(fam_label(s)[0] for s in sols)
        top = cnt.most_common(12)
        results[f"{p}_{k}"] = dict(
            k=k, parity=k % 2, minus1=bool((p - 1) in H),
            total=len(sols), families=dict(top),
            ratio_total_over_k3=round(len(sols) / k**3, 3))
        print(f"\np={p} k={k} ({'even' if k%2==0 else 'odd'}, "
              f"-1inH={bool((p-1) in H)}): total={len(sols)} "
              f"({len(sols)/k**3:.3f}*k^3)")
        for lab, c in top:
            print(f"   {lab:16s} {c:>8}  ({c/k**3:.3f}*k^3)")
    json.dump(results,
              open(os.path.join(ART, "phase3_r6.json"), "w"),
              indent=1)
    print("\nsaved artifacts/phase3_r6.json")


if __name__ == "__main__":
    main()
