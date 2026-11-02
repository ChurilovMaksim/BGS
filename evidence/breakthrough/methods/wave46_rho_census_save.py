import math, pickle
from collections import defaultdict
ALPHA = (3, 2)
def mul(a, b, M): return ((a[0]*b[0]+2*a[1]*b[1]) % M, (a[0]*b[1]+a[1]*b[0]) % M)
def pw(a, n, M):
    r = (1, 0)
    for _ in range(n): r = mul(r, a, M)
    return r
def genuine(M, m):
    d = pw(ALPHA, m, M); d = ((d[0]-1) % M, d[1]); d0, d1 = d; sols = []
    for x in range(M):
        rhs = (-d1*x) % M; g = math.gcd(d0, M)
        if rhs % g: continue
        d0p, Mp, rhsp = d0//g, M//g, rhs//g
        y0 = (rhsp * pow(d0p, -1, Mp)) % Mp
        for k in range(g):
            y = y0 + k*Mp
            if (d0*x + 2*d1*y) % M == 0 and (d1*x + d0*y) % M == 0:
                sols.append((x, y))
    return sols
G2, Gq = genuine(8192, 32), genuine(17, 32)
AP8 = [pw(ALPHA, i, 8192) for i in range(32)]
AP17 = [pw(ALPHA, i, 17) for i in range(32)]
def seq_fast(B, AP, M):
    return tuple((2*((B[0]*a[0]+2*B[1]*a[1]) % M)) % M for a in AP)
P2 = [(B, seq_fast(B, AP8, 8192)) for B in G2]
Pq = [(B, seq_fast(B, AP17, 17)) for B in Gq]
groups = defaultdict(list)
for (B2, p) in P2:
    for (Bq, a) in Pq:
        glob = tuple(sorted(zip(p, a)))
        F = defaultdict(list)
        for i in range(32): F[(p[i], a[i])].append(i)
        mf = any(len({i % 4 for i in idx}) > 1 for idx in F.values())
        groups[glob].append((B2, Bq, mf))
print(f"groups={len(groups)}", flush=True)
with open("wave46_rho_groups.pkl", "wb") as f:
    pickle.dump({"G2": G2, "Gq": Gq, "groups": dict(groups)}, f)
print("saved wave46_rho_groups.pkl", flush=True)
