"""Wave 27, task 1: (a) N(A') vs N(A) mod 81 for pairs in a group;
(b) vertex-fiber collisions between the two collapsed classes.
Exact arithmetic at (108,3).
"""
from collections import Counter

MOD = 81
def mul(x, y): return ((x[0]*y[0] + 2*x[1]*y[1]) % MOD, (x[0]*y[1] + x[1]*y[0]) % MOD)
def tr(x): return (2*x[0]) % MOD
def norm(x): return (x[0]*x[0] - 2*x[1]*x[1]) % MOD

ALPHA = (3, 2)
pw = [(1, 0)]
for _ in range(200):
    pw.append(mul(pw[-1], ALPHA))
M = 108
seqs = {}
for a in range(81):
    for b in range(81):
        A = (a, b)
        seqs[A] = [tr(mul(A, pw[i])) for i in range(M)]
groups = {}
for A, y in seqs.items():
    groups.setdefault(tuple(sorted(y)), []).append(A)

# (a) norm check
norm_bad = 0
norm_checked = 0
for key, As in groups.items():
    n0 = norm(As[0])
    for A in As[1:]:
        norm_checked += 1
        if norm(A) != n0:
            norm_bad += 1
print("norm: pairs checked:", norm_checked, " N(A')!=N(A) mod 81:", norm_bad)

# (b) vertex fibers for the two collapsed classes
def rigid_vertex_fiber(C):
    # returns (w mod 27, rigid value mod 81) or None
    if C[1] % 3 != 0:
        return None
    Cx, Cy = C[0] % 27, C[1] % 27
    T1 = (2*(3*Cx + 2*Cy)) % 27
    T1p = (T1//3) % 9
    t1 = T1p % 3
    X9, Y9 = C[0] % 9, C[1] % 9
    T2 = (2*(2*X9 + 12*Y9)) % 9
    t2 = T2 % 3
    if t2 == 0:
        return ("degenerate",)
    a0 = (2 - t1*pow(t2, -1, 3)) % 3
    S = (a0*T1p + (a0*(a0-1)//2)*T2) % 9
    w = (tr(C) + 9*(S % 3)) % 27
    rigid = (tr(C) + 9*S) % 81
    return (w, rigid)

collide = 0
total2 = 0
for A in seqs:
    if A[0] % 3 == 0 and A[1] % 3 == 0:
        continue
    coll = []
    for r in range(4):
        C = mul(A, pw[r])
        if C[1] % 3 == 0:
            coll.append((r, C))
    if len(coll) == 2:
        total2 += 1
        w1 = rigid_vertex_fiber(coll[0][1])
        w2 = rigid_vertex_fiber(coll[1][1])
        if w1[0] == w2[0]:
            collide += 1
print("unit A with exactly 2 collapsed classes:", total2,
      " vertex-fiber collisions:", collide)
