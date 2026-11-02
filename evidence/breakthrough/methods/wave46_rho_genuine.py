# Genuine-pair census at m=32, (8192,17): group by global, flag mixed fibers.
import math
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
print(f"|G2|={len(G2)} |Gq|={len(Gq)} pairs={len(G2)*len(Gq)}", flush=True)
def v2(n):
    if n == 0: return 99
    c = 0
    while n % 2 == 0: n //= 2; c += 1
    return c
from collections import Counter
print("G2 min-v2 distribution:", dict(sorted(Counter(min(v2(x), v2(y)) for x, y in G2).items())))
print("G2 sample:", G2[:10])
AP8 = [pw(ALPHA, i, 8192) for i in range(32)]
AP17 = [pw(ALPHA, i, 17) for i in range(32)]
def seq_fast(B, AP, M):
    return tuple((2*((B[0]*a[0]+2*B[1]*a[1]) % M)) % M for a in AP)
P2 = [(B, seq_fast(B, AP8, 8192)) for B in G2]
Pq = [(B, seq_fast(B, AP17, 17)) for B in Gq]
def joints(ppp, oo, t=4):
    return tuple(tuple(sorted(zip(ppp[r::t], oo[r::t]))) for r in range(t))
perms = [tuple((e*r+b) % 4 for r in range(4)) for e in (1,-1) for b in range(4)]
def mixed(p, a):
    F = defaultdict(list)
    for i in range(32): F[(p[i], a[i])].append(i)
    return {v: idx for v, idx in F.items() if len({i % 4 for i in idx}) > 1}
groups = defaultdict(list)
nmixed_pairs = 0
mixed_examples = []
for (B2, p) in P2:
    for (Bq, a) in Pq:
        glob = tuple(sorted(zip(p, a)))
        mf = mixed(p, a)
        groups[glob].append((B2, Bq, bool(mf)))
        if mf:
            nmixed_pairs += 1
            if len(mixed_examples) < 5:
                mixed_examples.append((B2, Bq, list(mf.items())[:2]))
print(f"global groups: {len(groups)}; genuine pairs with mixed fibers: {nmixed_pairs}")
for e in mixed_examples: print("  mixed example:", e)
# among mixed pairs, groups with >=2 members and their pi-sets
nmixed_groups = 0
shown = 0
for glob, mem in groups.items():
    if len(mem) >= 2 and any(m[2] for m in mem):
        nmixed_groups += 1
        if shown < 5:
            shown += 1
            (B2, Bq, _) = mem[0]
            p = seq_fast(B2, AP8, 8192); a = seq_fast(Bq, AP17, 17)
            J = joints(p, a)
            desc = []
            for (B2b, Bqb, _) in mem[1:4]:
                pb = seq_fast(B2b, AP8, 8192); ab = seq_fast(Bqb, AP17, 17)
                Jb = joints(pb, ab)
                ps = [pi for pi in perms if all(Jb[r] == J[pi[r]] for r in range(4))]
                desc.append(((B2b, Bqb), ps))
            print(f"  mixed group: first={mem[0][:2]} nmem={len(mem)} partners(pi-sets)={desc}")
print(f"mixed groups with >=2 members: {nmixed_groups}")
import json
json.dump({"G2size": len(G2), "Gqsize": len(Gq), "groups": len(groups),
           "mixed_pairs": nmixed_pairs, "mixed_groups": nmixed_groups},
          open("wave46_rho_genuine_summary.json", "w"))
