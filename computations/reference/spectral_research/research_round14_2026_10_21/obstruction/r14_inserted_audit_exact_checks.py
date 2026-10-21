#!/usr/bin/env python3
"""Exact finite-algebra checks for the independent Round 14 inserted audit.

These checks validate general identities on a matrix with repeated eigenvalues
and repeated difference phases. They are not a numerical test of the original
tau=10^-80 family or its asymptotics.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
N = 4
EXP = [0, 0, 1, 2]
A = [[2, 1, 3, -2],
     [1, -1, 2, 4],
     [3, 2, 0, 5],
     [-2, 4, 5, -1]]
PAIRS = [(j, k) for j in range(N) for k in range(N)]

def cadd(z, w):
    return (z[0] + w[0], z[1] + w[1])

def cmul(z, w):
    return (z[0]*w[0] - z[1]*w[1], z[0]*w[1] + z[1]*w[0])

def cconj(z):
    return (z[0], -z[1])

def cscale(t, z):
    return (t*z[0], t*z[1])

def cpow_i(k):
    return [(F(1), F(0)), (F(0), F(1)),
            (F(-1), F(0)), (F(0), F(-1))][k % 4]

def csum(values):
    out = (F(0), F(0))
    for z in values:
        out = cadd(out, z)
    return out

def p(m):
    return csum(cpow_i(m * a) for a in EXP)

Q = [[A[j][l] if (EXP[j] - EXP[l]) % 4 == 0 else 0
      for l in range(N)] for j in range(N)]

def ad_entry(B, row, col):
    j, k = row
    l, m = col
    return B[j][l] * (k == m) - (j == l) * B[m][k]

projection_comparisons = 0
extra_collision_comparisons = 0
hs2_ad = F(0)
for row in PAIRS:
    for col in PAIRS:
        j, k = row
        l, m = col
        retained = (EXP[j] - EXP[k] - EXP[l] + EXP[m]) % 4 == 0
        projected = ad_entry(A, row, col) if retained else 0
        expected = ad_entry(Q, row, col)
        assert projected == expected
        hs2_ad += F(expected)**2
        projection_comparisons += 1
        if retained and j != l and k != m:
            assert projected == 0
            extra_collision_comparisons += 1

qhs2 = sum(F(x)**2 for row in Q for x in row)
trq = sum(Q[j][j] for j in range(N))
assert hs2_ad == 2*N*qhs2 - 2*trq**2
assert trq == 0
times = list(range(1, 6))
weights = {m: F(1, m+1) for m in times}
G = [
    sum(F(m) * weights[m] * cmul(cconj(p(m)), cpow_i(EXP[j]*m))[1]
        for m in times)
    for j in range(N)
]
assert sum(G) == 0
lhs = sum(g*g for g in G)
rhs = F(0)
for m in times:
    for n in times:
        first = cmul(cmul(cconj(p(m)), p(n)), p(m-n))
        second = cmul(cmul(cconj(p(m)), cconj(p(n))), p(m+n))
        rhs += F(1, 2) * m*n*weights[m]*weights[n]*(first[0]-second[0])
assert lhs == rhs

direct_derivative = F(0)
for m in times:
    inserted = csum(cscale(F(A[j][j]), cpow_i(EXP[j]*m)) for j in range(N))
    pprime = cscale(F(N*m), cmul((F(0), F(1)), inserted))
    direct_derivative += F(2, N*N)*weights[m]*cmul(cconj(p(m)), pprime)[0]
projected_derivative = -F(2, N)*sum(F(Q[j][j])*G[j] for j in range(N))
assert direct_derivative == projected_derivative

def exact(x):
    x = F(x)
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"

report = {
    "status": "passed",
    "scope": "General exact finite-dimensional identities; not original spectral asymptotics.",
    "N": N,
    "eigenvalue_exponents_mod_4": EXP,
    "projection_entry_comparisons": projection_comparisons,
    "additional_difference_collisions_checked": extra_collision_comparisons,
    "Q_HS_squared": exact(qhs2),
    "ad_Q_superoperator_HS_squared": exact(hs2_ad),
    "trace_G": exact(sum(G)),
    "G_HS_squared": exact(lhs),
    "triple_trace_sum": exact(rhs),
    "direct_parameter_derivative": exact(direct_derivative),
    "projected_parameter_derivative": exact(projected_derivative),
}
out = ROOT / "r14_inserted_audit_exact_checks.json"
out.write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))

