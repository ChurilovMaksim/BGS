"""TASK B: even-k strata compensation at (p,k)=(241,30).
Thm r6 predicts total = 5k(3k^2-9k+8)=365700 regardless of D_p(k).
Here D=50760 != 0, so other strata must absorb -50760.
Full partition table -> identify which."""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys, os, json
from collections import Counter
from sympy import primitive_root

sys.path.insert(0, _BGS_ROOT + r"\src")
from phase3_r6_families import enumerate_sols

ART = _BGS_ROOT + r"\artifacts"


def main():
    p, k = 241, 30
    g = int(primitive_root(p))
    alpha = pow(g, (p - 1) // k, p)
    H = set(); x = 1
    for _ in range(k):
        H.add(x); x = x * alpha % p
    sols = enumerate_sols(p, H)

    def sizes_label(s):
        groups = {}
        for i, v in enumerate(s):
            groups.setdefault(v, []).append(i)
        return tuple(sorted(len(g) for g in groups.values()))

    cnt = Counter(sizes_label(s) for s in sols)
    pred = 5 * k * (3 * k * k - 9 * k + 8)
    print(f"(p,k)=({p},{k}): total={len(sols)} predicted={pred} "
          f"{'MATCH' if len(sols)==pred else 'MISMATCH'}")
    # reference decomposition from pure-combinatorial even-k table:
    # known exact pieces: [6]=k, [2,4]=9k(k-1); others fitted forms
    ref = {
        (2, 2, 2): None,      # unknown closed form (even case)
        (1, 1, 1, 3): 18 * k * (k - 2),
        (2, 4): 9 * k * (k - 1),
        (6): k,
    }
    print("\nstrata:")
    for lab, c in sorted(cnt.items()):
        note = ""
        if lab in ref and ref[lab] is not None:
            ok = (c == ref[lab])
            note = f"formula={ref[lab]} {'OK' if ok else 'DEVIATES'}"
        print(f"  {lab}: {c:>7}  {note}")
    json.dump({str(k): v for k, v in cnt.items()},
              open(os.path.join(ART,
                  "phase3_compensation_241_30.json"), "w"), indent=1)
    print("saved artifacts/phase3_compensation_241_30.json")


if __name__ == "__main__":
    main()
