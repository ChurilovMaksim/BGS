"""Wave 45, task 6, part 7: mechanism check at m=252 for the counted
fiber-0 pair (k=20 <-> 11): partial sums, e-table, and quadratic fit
of F via random row subsets.
"""
import numpy as np
import random
from collections import defaultdict

exec(open("wave45_F3_partial.py").read().split("analyse(180")[0])

m = 252
K, T, ci, reps = setup(m)
q = 729
by_k = {}
for rep, (f, C) in reps.items():
    if C[0] == 378 and C[1] % 27 == 0:
        by_k[C[1] // 27] = rep
print(f"m=252 fiber-0 k values: {sorted(by_k)}, ci mod 3 = {ci % 3}")
j1, j2 = by_k[20], by_k[11]
d = (T[:, j2] - T[:, j1]) % q
assert np.all(d % 243 == 0)
e = (d // 243) % 3
zeta = np.exp(2j * np.pi * ((ci * T[:, j1]) % q) / q)
parts = [complex(zeta[e == r].sum()) for r in range(3)]
S1 = sum(parts)
S2 = complex(np.exp(2j * np.pi * ((ci * T[:, j2]) % q) / q).sum())
print(f"pair 20<->11: e-counts={np.bincount(e, minlength=3).tolist()} "
      f"partials A={parts[0]:.4f} B={parts[1]:.4f} C={parts[2]:.4f}")
print(f"  S1={S1:.4f} |S1|={abs(S1):.4f} ratio S2/S1={S2/S1:.6f}")
Cs = [recover_C(tuple(K[i].tolist()), q) for i in range(q)]
tab = defaultdict(set)
for i in range(q):
    xb, yb = Cs[i][0] // 27 % 27, Cs[i][1] // 27 % 27
    tab[(xb % 3, yb % 3)].add(int(e[i]))
print(f"  e determined by (xbar%3,ybar%3)? {all(len(v)==1 for v in tab.values())}")
for key in sorted(tab):
    print(f"    {key}: e={sorted(tab[key])}")

# quadratic fit for j = k=20 at m=252
E = (ci * T[:, j1]) % q
assert np.all(E % 27 == 0)
F = (E // 27) % 27
bars = [(c[0] // 27 % 27, c[1] // 27 % 27) for c in Cs]
xj, yj = bars[j1]
idx_of = {b: i for i, b in enumerate(bars)}
rng = random.Random(7)
found = None
for trial in range(60):
    picks = rng.sample(range(q), 6)
    rows, rhs = [], []
    for i in picks:
        xb, yb = bars[i]
        dx, dy = (xb - xj) % 27, (yb - yj) % 27
        rows.append([dx * dx % 27, dy * dy % 27, dx * dy % 27, dx, dy, 1])
        rhs.append(int(F[i]))
    try:
        sol = np.linalg.solve(np.array(rows, dtype=float), np.array(rhs, dtype=float))
    except np.linalg.LinAlgError:
        continue
    if not all(abs(v - round(v)) < 1e-6 for v in sol):
        continue
    a, bb, cc, dd, ee, ff = [int(round(v)) % 27 for v in sol]
    bad = 0
    for i in range(q):
        xb, yb = bars[i]
        dx, dy = (xb - xj) % 27, (yb - yj) % 27
        pred = (a * dx * dx + bb * dy * dy + cc * dx * dy + dd * dx + ee * dy + ff) % 27
        if pred != int(F[i]):
            bad += 1
    if bad == 0:
        found = (a, bb, cc, dd, ee, ff)
        break
print(f"m=252 k=20 quadratic fit: {found} (None = not found in 60 trials)")
