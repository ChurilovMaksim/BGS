"""Wave 41, task 4: S-tuple dihedral lemma check.

For each (m, q): compute component fibers (sorted multiset) and, for
every point, the class sums S_r = sum_{i = r mod C} y_i (mod q), where
C = 4 if 4|m, C = 2 if m = 2 mod 4, C = 1 if m odd. Check that within
each fiber, all S-tuples are dihedral permutations of each other
(rotations + reversal for C=4; swap-or-equal for C=2; trivial for
C=1). Any fiber violating this is printed in full.
"""
import sys

import numpy as np
import sympy as sp

sys.path.insert(0, ".")
from wave16_d1a_targeted import Dm, group_ids, snf_kernel  # noqa: E402

ENUM_CAP = 2_000_000


def dihedral_orbit(tup):
    c = len(tup)
    out = set()
    for k in range(c):
        rot = tuple(tup[(r - k) % c] for r in range(c))
        out.add(rot)
        rev = tuple(tup[(k - r) % c] for r in range(c))
        out.add(rev)
    return out


def check_m(m):
    D = Dm(m)
    qs = [p ** e for p, e in sp.factorint(D).items()]
    C = 4 if m % 4 == 0 else (2 if m % 2 == 0 else 1)
    print(f"== m={m} C={C} qs={qs}", flush=True)
    bad_total = 0
    for q in qs:
        if q > ENUM_CAP or q * m > 150_000_000:
            print(f"   q={q}: SKIP", flush=True)
            continue
        pts = snf_kernel(m, q)
        fib = group_ids(np.sort(pts, axis=1))
        # class sums mod q
        S = np.zeros((len(pts), C), dtype=np.int64)
        for r in range(C):
            S[:, r] = pts[:, r::C].sum(axis=1) % q
        n_fib = int(fib.max()) + 1
        bad = 0
        for f in range(n_fib):
            idx = np.where(fib == f)[0]
            if len(idx) == 1:
                continue
            tups = [tuple(S[i].tolist()) for i in idx]
            orb = dihedral_orbit(tups[0])
            if any(t not in orb for t in tups):
                bad += 1
                if bad <= 3:
                    print(f"   VIOLATION q={q} fiber={f} size={len(idx)} "
                          f"distinct_tuples={sorted(set(tups))[:10]}",
                          flush=True)
        print(f"   q={q}: fibers={n_fib} S-tuple violations={bad}", flush=True)
        bad_total += bad
    print(f"== m={m}: TOTAL VIOLATIONS = {bad_total}", flush=True)
    return bad_total


if __name__ == "__main__":
    total = 0
    for m in [int(a) for a in sys.argv[1:]]:
        total += check_m(m)
    print(f"GRAND TOTAL VIOLATIONS = {total}", flush=True)
