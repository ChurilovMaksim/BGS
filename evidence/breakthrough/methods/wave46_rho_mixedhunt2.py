from collections import defaultdict
ALPHA = (3, 2)
def mul(a, b, M): return ((a[0]*b[0]+2*a[1]*b[1]) % M, (a[0]*b[1]+a[1]*b[0]) % M)
def pw(a, n, M):
    r = (1, 0)
    while n:
        if n & 1: r = mul(r, a, M)
        a = mul(a, a, M); n >>= 1
    return r
AP8 = [pw(ALPHA, i, 8192) for i in range(32)]
AP17 = [pw(ALPHA, i, 17) for i in range(32)]
print("alpha^8 mod 17:", pw(ALPHA, 8, 17), "alpha^4 mod 17:", pw(ALPHA, 4, 17), flush=True)
def seq_fast(B, AP, M):
    return [(2*((B[0]*a[0]+2*B[1]*a[1]) % M)) % M for a in AP]
def joints(ppp, oo, t=4):
    return tuple(tuple(sorted(zip(ppp[r::t], oo[r::t]))) for r in range(t))
perms = [tuple((e*r+b) % 4 for r in range(4)) for e in (1,-1) for b in range(4)]
def pset(p, a, pp, ap):
    J, Jp = joints(p, a), joints(pp, ap)
    return [pi for pi in perms if all(Jp[r] == J[pi[r]] for r in range(4))]
def mixed_fibers(p, a):
    F = defaultdict(list)
    for i in range(32): F[(p[i], a[i])].append(i)
    return {v: idx for v, idx in F.items() if len({i % 4 for i in idx}) > 1}
import random
random.seed(123)
found = []
tries = 0
while len(found) < 3 and tries < 60:
    tries += 1
    x, y = random.randrange(8192), random.randrange(8192)
    p = seq_fast((x, y), AP8, 8192)
    byval = defaultdict(list)
    for i, v in enumerate(p): byval[v].append(i)
    cpairs = []
    for v, idx in byval.items():
        for a1 in range(len(idx)):
            for a2 in range(a1+1, len(idx)):
                if idx[a1] % 4 != idx[a2] % 4: cpairs.append((idx[a1], idx[a2]))
    if not cpairs: continue
    i, ip = cpairs[0]
    ai, aip = AP17[i], AP17[ip]
    d = ((ai[0]-aip[0]) % 17, (ai[1]-aip[1]) % 17)
    sols = [(bx, by) for bx in range(17) for by in range(17)
            if (bx*d[0] + 2*by*d[1]) % 17 == 0]
    if not sols: continue
    Bq = sols[0]
    a = seq_fast(Bq, AP17, 17)
    mf = mixed_fibers(p, a)
    if not mf: continue
    print(f"try {tries}: A=({(x,y)},{Bq}) mixed fibers: {list(mf.items())[:2]}", flush=True)
    glob = sorted(zip(p, a))
    partners = []
    for bx in range(17):
        for by in range(17):
            if (bx, by) == Bq: continue
            ap2 = seq_fast((bx, by), AP17, 17)
            if sorted(zip(p, ap2)) == glob:
                partners.append(((x, y), (bx, by), pset(p, a, p, ap2)))
    print(f"   Bq'-partners: {len(partners)}", flush=True)
    for x2 in range(8192):
        for y2 in range(8192):
            if (x2, y2) == (x, y): continue
            p2 = seq_fast((x2, y2), AP8, 8192)
            if sorted(zip(p2, a)) == glob:
                partners.append(((x2, y2), Bq, pset(p, a, p2, a)))
    print(f"   total partners: {len(partners)}", flush=True)
    if partners:
        for pt in partners[:6]:
            print("   partner:", pt[0], pt[1], "pi-set:", pt[2], flush=True)
        found.append(((x, y), Bq, partners))
print(f"tries={tries} mixed pairs with partners found={len(found)}")
import json
json.dump([{"B2": f[0], "Bq": f[1],
            "partners": [[p[0], p[1], p[2]] for p in f[2][:20]]} for f in found],
          open("wave46_rho_mixedpairs.json", "w"))
print("saved wave46_rho_mixedpairs.json")
