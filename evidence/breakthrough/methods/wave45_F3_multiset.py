"""Wave 45, task 6, part 3: exponent multisets within e-classes.

For a fiber-0 orbit j at m=180 (pair k=20<->11) and the fiber-1 orbit
at m=252: for each e-class, look at the multiset of exponents
ci*T[i,j] mod 729. Test: is it invariant under +243 shift (which
would force the partial sum to 0)? What is its mod-27 / mod-81 profile?
"""
import math
import numpy as np
from collections import Counter

exec(open("wave45_F3_partial.py").read().split("analyse(180")[0])

def multiset_report(m, c0_target, k_hi, k_lo):
    K, T, ci, reps = setup(m)
    q = 729
    by_k = {}
    for rep, (f, C) in reps.items():
        if C[0] == c0_target and C[1] % 27 == 0:
            by_k[C[1] // 27] = rep
    j1, j2 = by_k[k_hi], by_k[k_lo]
    d = (T[:, j2] - T[:, j1]) % q
    e = (d // 243) % 3
    exps = (ci * T[:, j1]) % q
    print(f"===== m={m} C0={c0_target} pair {k_hi}<->{k_lo} =====")
    for r in range(3):
        E = exps[e == r]
        cnt = Counter(E.tolist())
        # invariance under +243: multiset {v} vs {v+243}
        shift = Counter(((E + 243) % q).tolist())
        inv243 = (cnt == shift)
        # mod 27 profile
        mod27 = Counter((E % 27).tolist())
        mod81 = Counter((E % 81).tolist())
        S = complex(np.exp(2j * np.pi * E / q).sum())
        print(f"  class e={r}: n={len(E)} sum={S:.6f} |sum|={abs(S):.4f} "
              f"inv+243={inv243} distinct={len(cnt)}")
        print(f"    mod27 profile: {sorted(mod27.items())[:12]}")
        print(f"    mod81 distinct count: {len(mod81)}; top values: {mod81.most_common(5)}")
        # if not invariant, show the difference multiset
        if not inv243:
            diff = cnt - shift
            print(f"    cnt-shift nonzero entries: {len(diff)} e.g. {list(diff.items())[:6]}")

multiset_report(180, 378, 20, 11)
multiset_report(252, 405, 15, 6)
