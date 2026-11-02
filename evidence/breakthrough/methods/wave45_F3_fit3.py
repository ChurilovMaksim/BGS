"""Wave 45, task 6, part 6c: is the quadratic part of F universal?
Test k=20's coeffs on all fiber-0 orbits at m=180; for others, fix
(a,b,c)=(19,16,0) and fit (d,e,f) from 3 rows, verify on all.
"""
import numpy as np

exec(open("wave45_F3_partial.py").read().split("analyse(180")[0])

m = 180
K, T, ci, reps = setup(m)
q = 729
by_k = {}
for rep, (f, C) in reps.items():
    if C[0] == 378 and C[1] % 27 == 0:
        by_k[C[1] // 27] = rep
Cs = [recover_C(tuple(K[i].tolist()), q) for i in range(q)]
bars = [(c[0] // 27 % 27, c[1] // 27 % 27) for c in Cs]
idx_of = {b: i for i, b in enumerate(bars)}

a0, b0, c0 = 19, 16, 0
for kk in sorted(by_k):
    j = by_k[kk]
    E = (ci * T[:, j]) % q
    F = (E // 27) % 27
    xj, yj = bars[j]
    # test k=20 coeffs
    a, bb, cc, d, ee, ff = 19, 16, 0, 21, 21, 13
    bad_full = 0
    for i in range(q):
        xb, yb = bars[i]
        dx, dy = (xb - xj) % 27, (yb - yj) % 27
        pred = (a * dx * dx + bb * dy * dy + cc * dx * dy + d * dx + ee * dy + ff) % 27
        if pred != int(F[i]):
            bad_full += 1
    # fit (d,e,f) with (a,b,c) fixed, from rows (0,0),(1,0),(0,1)
    rows, rhs = [], []
    for (dx, dy) in [(0, 0), (1, 0), (0, 1)]:
        i = idx_of[((xj + dx) % 27, (yj + dy) % 27)]
        rows.append([dx, dy, 1])
        rhs.append((int(F[i]) - (a0 * dx * dx + b0 * dy * dy + c0 * dx * dy)) % 27)
    sol = np.linalg.solve(np.array(rows, dtype=float), np.array(rhs, dtype=float))
    d2, e2, f2 = [int(round(v)) % 27 for v in sol]
    bad_fit = 0
    for i in range(q):
        xb, yb = bars[i]
        dx, dy = (xb - xj) % 27, (yb - yj) % 27
        pred = (a0 * dx * dx + b0 * dy * dy + c0 * dx * dy + d2 * dx + e2 * dy + f2) % 27
        if pred != int(F[i]):
            bad_fit += 1
    print(f"k={kk:2d} Cbar_j={(xj, yj)}: k20-coeffs mismatches={bad_full}, "
          f"refit (d,e,f)=({d2},{e2},{f2}) mismatches={bad_fit}")
