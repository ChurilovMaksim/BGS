"""Sweep A_p(k) = sol6_even - skeleton across even-k configurations,
testing: does arithmetic excess vanish unless 3 | k?
Skeleton S(k)=5k(3k^2-9k+8); A = total - S."""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys, os, json
from sympy import primitive_root, primerange

sys.path.insert(0, _BGS_ROOT + r"\src")
from phase3_r6_families import enumerate_sols
from master_formula_strong import find_orbit_H

ART = _BGS_ROOT + r"\artifacts"
A_MAT = [2, 1, 1, 1]


def skel(k):
    return 5 * k * (3 * k * k - 9 * k + 8)


def main():
    rows = []
    ks = [6, 12, 18, 22, 24, 26]          # mix: mult-of-3 vs not
    for k in ks:
        got = 0
        for p in primerange(max(101, 4 * k), 2600):
            if (p - 1) % k != 0:
                continue
            H = find_orbit_H(p, A_MAT)
            if not H:
                continue
            g = int(primitive_root(p))
            alpha = pow(g, (p - 1) // k, p)
            Hs = set(); x = 1
            for _ in range(k):
                Hs.add(x); x = x * alpha % p
            tot = len(enumerate_sols(p, Hs))
            Ap = tot - skel(k)
            rows.append(dict(p=p, k=k, three_div=(k % 3 == 0),
                             total=tot, skeleton=skel(k),
                             A=Ap))
            print(f"k={k:2d} p={p:5d} 3|k={str(k%3==0):5s}: "
                  f"A={Ap:>7}", flush=True)
            got += 1
            if got >= 2:
                break
    json.dump(rows, open(os.path.join(ART,
        "phase3_Apk_sweep.json"), "w"), indent=1)

    print("\nSummary by 3|k:")
    for flag in (True, False):
        sub = [r for r in rows if r["three_div"] == flag]
        if sub:
            mx = max(abs(r["A"]) for r in sub)
            print(f"  3|k={flag}: n={len(sub)}, "
                  f"max|A|={mx}")


if __name__ == "__main__":
    main()
