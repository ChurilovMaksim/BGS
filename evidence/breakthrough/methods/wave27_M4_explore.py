"""Wave 27, task 1: explore M4 mechanism at (108,3) mod 81.
R = Z[sqrt2] as pairs (a,b) mod 81. alpha = 3+2 sqrt2.
Exact integer arithmetic throughout. Repository untouched; no Lean.
"""
import json
from collections import Counter

P = 81
MOD = 81

def add(x, y): return ((x[0]+y[0]) % MOD, (x[1]+y[1]) % MOD)
def mul(x, y): return ((x[0]*y[0] + 2*x[1]*y[1]) % MOD, (x[0]*y[1] + x[1]*y[0]) % MOD)
def tr(x): return (2*x[0]) % MOD
def conj(x): return (x[0], (-x[1]) % MOD)

ALPHA = (3, 2)
# powers of alpha mod 81
pw = [(1, 0)]
for _ in range(200):
    pw.append(mul(pw[-1], ALPHA))
order = next(i for i in range(1, 200) if pw[i] == (1, 0))
print("order of alpha mod 81:", order)
GAMMA = pw[4]
print("gamma = alpha^4 =", GAMMA, " gamma-1 =", ((GAMMA[0]-1) % MOD, GAMMA[1]))
# gamma = 1 + 3u
u = (((GAMMA[0]-1)//3) % 27, (GAMMA[1]//3) % 27)
print("u mod 27 =", u, " u mod 3 =", (u[0] % 3, u[1] % 3))
# check gamma order mod 81
g = (1, 0)
gord = None
for i in range(1, 40):
    g = mul(g, GAMMA)
    if g == (1, 0):
        gord = i
        break
print("order of gamma mod 81:", gord)

M = 108
# sequences for all A in R/81
seqs = {}
for a in range(81):
    for b in range(81):
        A = (a, b)
        y = [tr(mul(A, pw[i])) for i in range(M)]
        seqs[A] = y

groups = {}
for A, y in seqs.items():
    groups.setdefault(tuple(sorted(y)), []).append(A)
print("num groups:", len(groups), " sizes:", sorted(Counter(len(v) for v in groups.values()).items()))

# D4 perms on classes mod 4
D4 = []
for eps in (1, -1):
    for s in range(4):
        D4.append(tuple((eps*r + s) % 4 for r in range(4)))

def class_multis(y):
    return [tuple(sorted(y[i] for i in range(M) if i % 4 == r)) for r in range(4)]

bad = 0
paircount = 0
for key, As in groups.items():
    cms = {A: class_multis(seqs[A]) for A in As}
    for i in range(len(As)):
        for j in range(i+1, len(As)):
            paircount += 1
            A, B = As[i], As[j]
            ok = any(all(cms[B][pi[r]] == cms[A][r] for r in range(4)) for pi in D4)
            if not ok:
                bad += 1
print("pairs checked:", paircount, " D4-bad pairs:", bad)

# collapsed structure: for each A, classes r with Tr(C_r u) == 0 mod 3
# C_r = A * alpha^r ; u mod 3 = (0,1) i.e. sqrt2
def collapsed_classes(A):
    out = []
    for r in range(4):
        C = mul(A, pw[r])
        # Tr(C*u) mod 3: u = (192,136) mod 81; use u mod 3 = sqrt2
        # Tr(C * sqrt2) = Tr((x+y sqrt2)*sqrt2) = Tr(2y + x sqrt2) = 4y
        if (4*C[1]) % 3 == 0:
            out.append(r)
    return out

coll_dist = Counter()
for A in seqs:
    coll_dist[len(collapsed_classes(A))] += 1
print("collapsed-class count distribution over A:", dict(coll_dist))
# check pairing: if 2 collapsed classes, do they differ by 2?
pairdiff = Counter()
for A in seqs:
    cc = collapsed_classes(A)
    if len(cc) == 2:
        pairdiff[(cc[1]-cc[0]) % 4] += 1
print("diff of the two collapsed classes:", dict(pairdiff))
