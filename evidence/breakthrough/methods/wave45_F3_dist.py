"""Wave 45, task 6, part 4: full distribution of F = (ci*T/27) mod 27
within each e-class, for a fiber-0 orbit and the fiber-1 orbit.
"""
import numpy as np
from collections import Counter

exec(open("wave45_F3_partial.py").read().split("analyse(180")[0])

def dist_report(m, c0_target, k_hi, k_lo):
    K, T, ci, reps = setup(m)
    q = 729
    by_k = {}
    for rep, (f, C) in reps.items():
        if C[0] == c0_target and C[1] % 27 == 0:
            by_k[C[1] // 27] = rep
    j1, j2 = by_k[k_hi], by_k[k_lo]
    d = (T[:, j2] - T[:, j1]) % q
    e = (d // 243) % 3
    E = (ci * T[:, j1]) % q
    assert np.all(E % 27 == 0)
    F = (E // 27) % 27
    print(f"===== m={m} C0={c0_target} pair {k_hi}<->{k_lo} =====")
    for r in range(3):
        Fr = F[e == r]
        cnt = Counter(Fr.tolist())
        S = complex(np.exp(2j * np.pi * Fr / 27).sum())
        print(f"  class e={r}: sum={S:.6f} |sum|={abs(S):.4f}")
        print(f"    F distribution (value: count): {sorted(cnt.items())}")

dist_report(180, 378, 20, 11)
dist_report(252, 405, 15, 6)
