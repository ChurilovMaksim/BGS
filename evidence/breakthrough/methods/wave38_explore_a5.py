"""Wave 38 (a): torsion z-patterns and their span.

Reproduce torsion_data's v,z construction for m=32; print the 16 period-4
patterns (z0,z1,z2,z3); compute the Z-span (via sympy Hermite/SNF) and test
membership of (1,-1,1,-1) [alternating] and (1,1,1,1) [constant].
"""
import sys
sys.path.insert(0, ".")
import numpy as np
import sympy as sp
from wave16_d1a_targeted import torsion_data, Dm

m = 32
D = Dm(m)
Z, Qmod = torsion_data(m, D)
print("Z shape:", Z.shape, " (rows = 16 torsion rows, length m)")
# period-4 patterns: first 4 entries of each row (rows are 4-periodic)
pats = []
for r in range(16):
    row = Z[r]
    pat = tuple(int(row[i]) for i in range(4))
    assert all(int(row[i]) == pat[i % 4] for i in range(m)), "not 4-periodic"
    pats.append(pat)
for p in sorted(set(pats)):
    print("  pattern:", p, "count:", pats.count(p))
M = sp.Matrix(pats)  # 16 x 4
print("rank over QQ:", M.rank())
# SNF of the pattern matrix to get the span structure
from sympy.matrices.normalforms import smith_normal_form
S = smith_normal_form(M)
print("SNF diag:", [S[i, i] for i in range(min(S.shape))])
# membership: solve M^T c = target over QQ, then check denominators
for target in [(1, -1, 1, -1), (1, 1, 1, 1), (1, 0, 1, 0), (0, 1, 0, 1)]:
    t = sp.Matrix(target)
    # least-squares / linear solve over QQ using the transpose system
    c, params = M.T.gauss_jordan_solve(t)
    resid = M.T * c - t
    print("target", target, "residual:", resid.T.tolist(),
          "solution (free params=0):", c.T.tolist())
    # also: is target in Z-span? check via SNF: target in lattice iff
    # coordinates in SNF basis are divisible by invariant factors
    print("   (check denominators above; integer coeffs iff all entries integral)")
