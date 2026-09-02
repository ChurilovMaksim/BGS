import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
"""Pinpoint the k=22 anomaly: strata diff between p=199 (A=3960)
and p=331 (A=0). Same abstract group H (order 22), different ambient
field -> which stratum carries the difference?"""
import sys, os, json
from collections import Counter
from sympy import primitive_root

sys.path.insert(0, _BGS_ROOT + r"\src")
from phase3_r6_families import enumerate_sols


def strata(p, k):
    g = int(primitive_root(p))
    alpha = pow(g, (p - 1) // k, p)
    H = set(); x = 1
    for _ in range(k):
        H.add(x); x = x * alpha % p
    sols = enumerate_sols(p, H)

    def lab(s):
        gr = {}
        for i, v in enumerate(s):
            gr.setdefault(v, []).append(i)
        return tuple(sorted(len(gg) for gg in gr.values()))
    return Counter(lab(s) for s in sols), len(sols)


def main():
    t1, n1 = strata(199, 22)
    t2, n2 = strata(331, 22)
    print(f"p=199: total={n1}   p=331: total={n2}   "
          f"diff={n1-n2}")
    keys = sorted(set(t1) | set(t2))
    for kk in keys:
        a, b = t1.get(kk, 0), t2.get(kk, 0)
        mark = "  <== DIFF" if a != b else ""
        print(f"  {kk}: {a:>6} vs {b:>6}{mark}")
        if a != b and abs(a - b) == n1 - n2:
            print("       ^ carries entire difference")
    json.dump({"199": {str(k): v for k, v in t1.items()},
               "331": {str(k): v for k, v in t2.items()}},
              open(os.path.join(
                  _BGS_ROOT +
                  r"\artifacts", "phase3_k22_anomaly.json"), "w"),
              indent=1)


if __name__ == "__main__":
    main()
