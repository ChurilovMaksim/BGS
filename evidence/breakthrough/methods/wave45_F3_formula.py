"""Wave 45, task 6, part 5: find the formula for F[i,j] mod 3 and mod 9.

For fixed fiber-0 orbit j (m=180, k=20): cross-tabulate F[i,j] mod 3
against (xbar_i mod 3, ybar_i mod 3), and F mod 9 against
(xbar_i mod 9, ybar_i mod 9) summaries. Also check: are all C_i
divisible by 27 (i.e. is Cbar a bijection onto (Z/27)^2)?
"""
import numpy as np
from collections import Counter, defaultdict

exec(open("wave45_F3_partial.py").read().split("analyse(180")[0])

m = 180
K, T, ci, reps = setup(m)
q = 729
by_k = {}
for rep, (f, C) in reps.items():
    if C[0] == 378 and C[1] % 27 == 0:
        by_k[C[1] // 27] = rep
j = by_k[20]
E = (ci * T[:, j]) % q
assert np.all(E % 27 == 0)
F = (E // 27) % 27

# all C_i divisible by 27? bijection onto (Z/27)^2?
Cs = [recover_C(tuple(K[i].tolist()), q) for i in range(q)]
div27 = all(c[0] % 27 == 0 and c[1] % 27 == 0 for c in Cs)
bars = set((c[0] // 27 % 27, c[1] // 27 % 27) for c in Cs)
print(f"all C divisible by 27? {div27}; distinct Cbar: {len(bars)} (expect 729)")

# cross-tab F mod 3 vs (xbar mod 3, ybar mod 3)
tab = defaultdict(Counter)
for i in range(q):
    xb, yb = Cs[i][0] // 27 % 27, Cs[i][1] // 27 % 27
    tab[(xb % 3, yb % 3)][int(F[i] % 3)] += 1
print("F mod 3 vs (xbar%3, ybar%3): rows=(xb,yb), cols=F%3 -> count")
for key in sorted(tab):
    print(f"  {key}: {dict(sorted(tab[key].items()))}")

# F mod 3 vs ybar mod 9? and vs xbar mod 9?
for name, keyfn in [("ybar%9", lambda xb, yb: yb % 9),
                    ("xbar%9", lambda xb, yb: xb % 9)]:
    tab2 = defaultdict(Counter)
    for i in range(q):
        xb, yb = Cs[i][0] // 27 % 27, Cs[i][1] // 27 % 27
        tab2[keyfn(xb, yb)][int(F[i] % 3)] += 1
    print(f"F mod 3 vs {name}:")
    for key in sorted(tab2):
        print(f"  {key}: {dict(sorted(tab2[key].items()))}")
