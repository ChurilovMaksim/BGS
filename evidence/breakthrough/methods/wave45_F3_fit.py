"""Wave 45, task 6, part 6: fit F[i,j] mod 27 as a polynomial in
(Cbar_i - Cbar_j). Ansatz: F = a*dx^2 + b*dy^2 + c*dx*dy + d*dx + e*dy + f
(mod 27), dx = xbar_i - xbar_j, dy = ybar_i - ybar_j (mod 27).
Solve mod 27 via brute-force-free linear algebra: solve mod 3, lift.
Simpler: use sympy Matrix over ZZ and SNF-style solve, or just try
fitting over integers with rational solve then reduce mod 27.
Here: use least-squares-free approach — pick 6 points, solve the
6x6 system over Z/27 by trying Smith normal form via sympy.
"""
import numpy as np
from collections import Counter

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
F = (E // 27) % 27
Cs = [recover_C(tuple(K[i].tolist()), q) for i in range(q)]
bars = [(c[0] // 27 % 27, c[1] // 27 % 27) for c in Cs]
xj, yj = bars[j]
print(f"j Cbar = {(xj, yj)}")

import sympy as sp
# Build the design matrix rows [dx^2, dy^2, dx*dy, dx, dy, 1] mod 27
rows, rhs = [], []
for i in range(q):
    xb, yb = bars[i]
    dx, dy = (xb - xj) % 27, (yb - yj) % 27
    rows.append([dx * dx % 27, dy * dy % 27, dx * dy % 27, dx, dy, 1])
    rhs.append(int(F[i]))
A = sp.Matrix(rows)
b = sp.Matrix(rhs)
# Solve A x = b mod 27: augment and use SNF via hermite_normal_form on transpose?
# Easiest: solve over rationals with linsolve on a subset, then verify mod 27.
# Take first 6 independent rows.
import itertools
sol = None
for combo in itertools.combinations(range(30), 6):
    M6 = sp.Matrix([rows[c] for c in combo])
    if M6.det() % 3 != 0:  # invertible mod 3 -> solvable mod 27 uniquely-ish
        b6 = sp.Matrix([rhs[c] for c in combo])
        try:
            x = M6.LUsolve(b6)
        except Exception:
            continue
        # x may be rational; check integrality mod 27
        if all(v.q == 1 for v in x):
            sol = [int(v) % 27 for v in x]
            break
print(f"candidate coeffs (a,b,c,d,e,f) mod 27: {sol}")
if sol:
    a, bb, cc, d, ee, ff = sol
    bad = 0
    for i in range(q):
        xb, yb = bars[i]
        dx, dy = (xb - xj) % 27, (yb - yj) % 27
        pred = (a * dx * dx + bb * dy * dy + cc * dx * dy + d * dx + ee * dy + ff) % 27
        if pred != int(F[i]):
            bad += 1
    print(f"mismatches over all 729 points: {bad}")
