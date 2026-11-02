"""Wave 45, task 6, part 6b: fast fit of F[i,j] mod 27 as quadratic
in (dx, dy) = Cbar_i - Cbar_j, using numpy rational solve on
hand-picked rows, then verification on all 729 points.
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

for kk in [20, 11]:
    j = by_k[kk]
    E = (ci * T[:, j]) % q
    F = (E // 27) % 27
    Cs = [recover_C(tuple(K[i].tolist()), q) for i in range(q)]
    bars = [(c[0] // 27 % 27, c[1] // 27 % 27) for c in Cs]
    xj, yj = bars[j]
    idx_of = {b: i for i, b in enumerate(bars)}
    # hand-picked rows: (dx,dy) in {(0,0),(1,0),(0,1),(1,1),(2,0),(0,2)}
    picks = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]
    rows, rhs = [], []
    for (dx, dy) in picks:
        i = idx_of[((xj + dx) % 27, (yj + dy) % 27)]
        rows.append([dx * dx, dy * dy, dx * dy, dx, dy, 1])
        rhs.append(int(F[i]))
    sol = np.linalg.solve(np.array(rows, dtype=float), np.array(rhs, dtype=float))
    solr = [int(round(v)) % 27 for v in sol]
    print(f"k={kk} Cbar_j={(xj, yj)} coeffs (a,b,c,d,e,f) = {solr} (raw {sol})")
    a, bb, cc, d, ee, ff = solr
    bad = []
    for i in range(q):
        xb, yb = bars[i]
        dx, dy = (xb - xj) % 27, (yb - yj) % 27
        pred = (a * dx * dx + bb * dy * dy + cc * dx * dy + d * dx + ee * dy + ff) % 27
        if pred != int(F[i]):
            bad.append(i)
    print(f"  mismatches: {len(bad)} / 729")
    if bad:
        # show structure of mismatches: F - pred vs (dx, dy) mod 3?
        from collections import Counter
        diffs = Counter()
        for i in bad[:50]:
            xb, yb = bars[i]
            dx, dy = (xb - xj) % 27, (yb - yj) % 27
            pred = (a * dx * dx + bb * dy * dy + cc * dx * dy + d * dx + ee * dy + ff) % 27
            diffs[(int(F[i]) - pred) % 27] += 1
        print(f"  first-50 mismatch diffs: {dict(diffs)}")
