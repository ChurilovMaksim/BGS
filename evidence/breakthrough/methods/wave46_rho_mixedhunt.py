# Hunt mixed-class-fiber pairs (A,A') with equal pair-globals.
from collections import defaultdict
ALPHA = (3, 2)
def mul(a, b, M): return ((a[0]*b[0]+2*a[1]*b[1]) % M, (a[0]*b[1]+a[1]*b[0]) % M)
def pw(a, n, M):
    r = (1, 0)
    while n:
        if n & 1: r = mul(r, a, M)
        a = mul(a, a, M); n >>= 1
    return r
print("ord check: alpha^8 mod 17:", pw(ALPHA, 8, 17), " alpha^4 mod 17:", pw(ALPHA, 4, 17))
def seq(B, M):
    ap = [pw(ALPHA, i, M) for i in range(32)]
    return [(2*mul(B, a, M)[0]) % M for a in ap]
def joints(ppp, oo, t=4):
    return tuple(tuple(sorted(zip(ppp[r::t], oo[r::t]))) for r in range(t))
perms = [tuple((e*r+b) % 4 for r in range(4)) for e in (1,-1) for b in range(4)]
def pset(p, a, pp, ap):
    J, Jp = joints(p, a), joints(pp, ap)
    return [pi for pi in perms if all(Jp[r] == J[pi[r]] for r in range(4))]
def fibers_of(p, a):
    F = defaultdict(list)
    for i in range(32): F[(p[i], a[i])].append(i)
    return F
def mixed_fibers(p, a):
    return {v: idx for v, idx in fibers_of(p, a).items() if len({i % 4 for i in idx}) > 1}
import random
random.seed(123)
found = []
tries = 0
while len(found) < 3 and tries < 400:
    tries += 1
    x, y = random.randrange(8192), random.randrange(8192)
    p = seq((x, y), 8192)
    # cross-class p-colliding position pairs
    byval = defaultdict(list)
    for i, v in enumerate(p): byval[v].append(i)
    cpairs = []
    for v, idx in byval.items():
        for a1 in range(len(idx)):
            for a2 in range(a1+1, len(idx)):
                if idx[a1] % 4 != idx[a2] % 4: cpairs.append((idx[a1], idx[a2]))
    if not cpairs: continue
    i, ip = cpairs[0]
    # solve a[i]==a[ip] for Bq mod 17: (Bq.d)_0 = 0 where d = alpha^i - alpha^ip
    ai, aip = pw(ALPHA, i, 17), pw(ALPHA, ip, 17)
    d = ((ai[0]-aip[0]) % 17, (ai[1]-aip[1]) % 17)
    sols = []
    for bx in range(17):
        for by in range(17):
            if (bx*d[0] + 2*by*d[1]) % 17 == 0: sols.append((bx, by))
    if not sols: continue
    Bq = sols[0]
    a = seq(Bq, 17)
    mf = mixed_fibers(p, a)
    if not mf: continue
    glob = sorted(zip(p, a))
    # partner search: vary Bq' (B2 fixed), then B2' (Bq fixed)
    partners = []
    for bx in range(17):
        for by in range(17):
            if (bx, by) == Bq: continue
            ap2 = seq((bx, by), 17)
            if sorted(zip(p, ap2)) == glob:
                partners.append(((x, y), (bx, by), pset(p, a, p, ap2)))
    for x2 in range(8192):
        for y2 in range(8192):
            if (x2, y2) == (x, y): continue
            p2 = seq((x2, y2), 8192)
            if sorted(zip(p2, a)) == glob:
                partners.append(((x2, y2), Bq, pset(p, a, p2, a)))
    if partners:
        print(f"A=({(x,y)},{Bq}) mixed fibers: {list(mf.items())[:2]} "
              f"partners={len(partners)}")
        for pt in partners[:6]:
            print("   partner:", pt[0], pt[1], "pi-set:", pt[2])
        found.append(((x, y), Bq, partners))
print(f"tries={tries} mixed pairs with partners found={len(found)}")
import json
json.dump([{"B2": f[0], "Bq": f[1],
            "partners": [[p[0], p[1], p[2]] for p in f[2][:20]]} for f in found],
          open("wave46_rho_mixedpairs.json", "w"))
print("saved wave46_rho_mixedpairs.json")
