# Wave 47x, task E — count ALL rotation-family pairs in wave46_rho_groups.pkl,
# classified by mixed-fiber position layout.
import pickle
from collections import defaultdict, Counter
ALPHA = (3, 2)
def mul(a, b, M): return ((a[0]*b[0]+2*a[1]*b[1]) % M, (a[0]*b[1]+a[1]*b[0]) % M)
def pw(a, n, M):
    r = (1, 0)
    for _ in range(n): r = mul(r, a, M)
    return r
AP8 = [pw(ALPHA, i, 8192) for i in range(32)]
AP17 = [pw(ALPHA, i, 17) for i in range(32)]
def seq_fast(B, AP, M):
    return tuple((2*((B[0]*a[0]+2*B[1]*a[1]) % M)) % M for a in AP)
def joints(ppp, oo, t=4):
    return tuple(tuple(sorted(zip(ppp[r::t], oo[r::t]))) for r in range(4))
perms = [tuple((e*r+b) % 4 for r in range(4)) for e in (1, -1) for b in range(4)]
ROTS = {(1,2,3,0), (2,3,0,1), (3,0,1,2)}
ID = (0,1,2,3)
data = pickle.load(open("wave46_rho_groups.pkl", "rb"))
groups = data["groups"]
print(f"groups: {len(groups)}", flush=True)
cache = {}
def info(B2, Bq):
    if (B2, Bq) in cache: return cache[(B2, Bq)]
    p = seq_fast(B2, AP8, 8192); a = seq_fast(Bq, AP17, 17)
    F = defaultdict(list)
    for i in range(32): F[(p[i], a[i])].append(i)
    mixed = tuple(sorted(tuple(F[v]) for v in F if len({i % 4 for i in F[v]}) > 1))
    out = (joints(p, a), mixed, len(set(p)) >= 2 and len(set(a)) >= 2)
    cache[(B2, Bq)] = out
    return out
classes = Counter()
examples = {}
ngroups = 0
for glob, mem in groups.items():
    ngroups += 1
    if ngroups % 1000 == 0: print(f"  ...{ngroups} groups, cache={len(cache)}", flush=True)
    mem = [(B2, Bq) for (B2, Bq, mf) in mem if mf]
    infos = {}
    for m in mem:
        J, mixed, ok = info(*m)
        if ok: infos[m] = (J, mixed)
    mem = list(infos)
    for ii in range(len(mem)):
        for jj in range(len(mem)):
            if ii == jj: continue
            J, mixed = infos[mem[ii]]
            Jb, mixedb = infos[mem[jj]]
            pis = [pi for pi in perms if all(Jb[r] == J[pi[r]] for r in range(4))]
            if pis and any(pi in ROTS for pi in pis):
                key = (tuple(pis), mixed, mixedb)
                classes[key] += 1
                if key not in examples: examples[key] = (mem[ii], mem[jj])
print("TOTAL ordered rotation pairs:", sum(classes.values()))
for key, cnt in classes.most_common():
    pis, mixed, mixedb = key
    print(f"count={cnt} pis={pis} example={examples[key]}")
    print(f"   A mixed positions: {mixed}")
    print(f"   Ap mixed positions: {mixedb}")
