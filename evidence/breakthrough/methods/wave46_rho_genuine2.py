import math, json
from collections import defaultdict, Counter
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
def mixed(p, a):
    F = defaultdict(list)
    for i in range(32): F[(p[i], a[i])].append(i)
    return {v: idx for v, idx in F.items() if len({i % 4 for i in idx}) > 1}
groups = defaultdict(list)
for (B2, p) in P2:
    for (Bq, a) in Pq:
        glob = tuple(sorted(zip(p, a)))
        mf = mixed(p, a)
        groups[glob].append((B2, Bq, mf))
print(f"groups={len(groups)}", flush=True)
# degeneracy breakdown of mixed pairs
brk = Counter()
for mem in groups.values():
    for (B2, Bq, mf) in mem:
        if mf:
            cls = ("B2zero" if B2 == (0,0) else "B2nonzero") + "/" + \
                  ("Bqzero" if Bq == (0,0) else "Bqnonzero")
            brk[cls] += 1
print("mixed pairs by degeneracy:", dict(brk))
# nondegenerate mixed groups: >=2 members, some member mixed + nondegenerate
def joints(ppp, oo, t=4):
    return tuple(tuple(sorted(zip(ppp[r::t], oo[r::t]))) for r in range(t))
perms = [tuple((e*r+b) % 4 for r in range(4)) for e in (1,-1) for b in range(4)]
cands = []
for glob, mem in groups.items():
    if len(mem) < 2: continue
    for (B2, Bq, mf) in mem:
        if mf and B2 != (0,0) and Bq != (0,0):
            # pi-sets vs other members
            p = seq_fast(B2, AP8, 8192); a = seq_fast(Bq, AP17, 17)
            J = joints(p, a)
            ps = []
            for (B2b, Bqb, _) in mem:
                if (B2b, Bqb) == (B2, Bq): continue
                pb = seq_fast(B2b, AP8, 8192); ab = seq_fast(Bqb, AP17, 17)
                Jb = joints(pb, ab)
                pis = [pi for pi in perms if all(Jb[r] == J[pi[r]] for r in range(4))]
                ps.append(((B2b, Bqb), pis))
            cands.append({"A": [B2, Bq], "mf": [[list(v), idx] for v, idx in list(mf.items())[:3]],
                          "nmem": len(mem), "partners": [[[p[0][0], p[0][1]], p[1]] for p in ps[:8]]})
            break
print(f"nondegenerate mixed groups: {len(cands)}")
for c in cands[:6]:
    print(" CAND:", c["A"], "nmem:", c["nmem"], "mf sample:", c["mf"])
    print("   partners:", c["partners"][:4])
json.dump(cands, open("wave46_rho_mixed_nondeg.json", "w"))
print("saved wave46_rho_mixed_nondeg.json")
