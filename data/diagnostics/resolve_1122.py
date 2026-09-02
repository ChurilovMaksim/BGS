"""Resolve [1,1,2,2] origin: attribute each such solution to
(L-profile,R-profile) of its two triples; test prediction
[1122]=36k (from ab=-vw mechanism, even k only)."""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys
from collections import Counter
from sympy import primitive_root

sys.path.insert(0, _BGS_ROOT + r"\src")
from phase3_r6_families import enumerate_sols


def profile(tri):
    c = Counter(tri)
    return tuple(sorted(c.values()))


def main():
    for (p, k) in [(199, 22), (211, 14)]:
        g = int(primitive_root(p))
        alpha = pow(g, (p - 1) // k, p)
        H = set(); x = 1
        for _ in range(k):
            H.add(x); x = x * alpha % p
        sols = enumerate_sols(p, H)
        tab = Counter()
        ex = None
        for s in sols:
            gr = {}
            for i, v in enumerate(s):
                gr.setdefault(v, []).append(i)
            sizes = tuple(sorted(len(gg) for gg in gr.values()))
            if sizes == (1, 1, 2, 2):
                L, R = s[:3], s[3:]
                tab[(profile(L), profile(R))] += 1
                if ex is None:
                    ex = s
        pred = 36 * k
        got = sum(tab.values())
        print(f"(p,k)=({p},{k}): [1122]={got}  prediction 36k={pred} "
              f"{'MATCH' if got == pred else 'MISMATCH'}")
        for prof, c in sorted(tab.items()):
            print(f"   L{prof[0]} R{prof[1]}: {c}")
        if ex:
            print("   example:", ex)


if __name__ == "__main__":
    main()
