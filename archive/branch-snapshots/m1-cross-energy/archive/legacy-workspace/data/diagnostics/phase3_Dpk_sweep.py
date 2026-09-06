"""D_p(k) sweep: all-distinct r6 family (= disjoint triple pairs with
equal sum & reciprocal sum) across odd-k configurations.
Compare with uniform-collision prediction k^6/p^2."""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys, os, json
import numpy as np
from sympy import primitive_root

sys.path.insert(0, _BGS_ROOT + r"\src")
from phase3_r6_families import enumerate_sols

ART = _BGS_ROOT + r"\artifacts"


def D_of(p, k):
    g = int(primitive_root(p))
    alpha = pow(g, (p - 1) // k, p)
    H = set(); x = 1
    for _ in range(k):
        H.add(x); x = x * alpha % p
    sols = enumerate_sols(p, H)
    d = sum(
        1 for s in sols if len(set(s)) == 6)
    return d


def main():
    rows = []
    grid = [(211, 15), (211, 21), (211, 35),
            (101, 25), (401, 25), (101, 10),   # 10 even sanity
            (241, 15), (241, 30),              # 30 even check
            (401, 31), (307, 51)]
    for (p, k) in grid:
        if (p - 1) % k != 0:
            print(f"skip ({p},{k})"); continue
        d = D_of(p, k)
        uni = k ** 6 / p ** 2
        dev = d - uni
        rows.append(dict(p=p, k=k, parity=k % 2, D=d,
                         uniform=round(uni, 1), dev=round(dev, 1),
                         ratio=round(d / uni, 3) if uni > 0 else None))
        print(f"p={p} k={k} ({'E' if k%2==0 else 'o'}): "
              f"D={d:>7}  k^6/p^2={uni:>10.1f}  "
              f"ratio={d/uni if uni>0 else float('nan'):.3f}")
    json.dump(rows, open(os.path.join(ART, "phase3_Dpk_sweep.json"),
                         "w"), indent=1)
    # quick scaling look at odd points only
    odds = [r for r in rows if r["parity"] == 1]
    if len(odds) >= 3:
        x = np.array([r["uniform"] for r in odds])
        y = np.array([abs(r["dev"]) for r in odds])
        A = np.vstack([np.sqrt(np.abs(x)), np.ones_like(x)]).T
        coef, *_ = np.linalg.lstsq(A, y, rcond=None)
        print(f"\nodd pts fit |dev| ~ a*sqrt(u)+b: "
              f"a={coef[0]:.2f} b={coef[1]:.2f}")
    print("saved artifacts/phase3_Dpk_sweep.json")


if __name__ == "__main__":
    main()
