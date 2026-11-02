# Wave 47x, task E — enumerate rotation-family mixed pairs at m=32.
# A rotation pi is (r -> r+b) with b != 0, i.e. (1,2,3,0), (2,3,0,1), (3,0,1,2).
import pickle
from collections import defaultdict
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

def fibers(B2, Bq):
    p = seq_fast(B2, AP8, 8192); a = seq_fast(Bq, AP17, 17)
    F = defaultdict(list)
    for i in range(32): F[(p[i], a[i])].append(i)
    return p, a, F

def show(B2, Bq, tag):
    p, a, F = fibers(B2, Bq)
    print(f"--- {tag} B2={B2} Bq={Bq} nfib={len(F)}")
    for v in sorted(F):
        idx = F[v]
        print(f"    {v} pos={idx} classes={sorted({i % 4 for i in idx})}")

data = pickle.load(open("wave46_rho_groups.pkl", "rb"))
groups = data["groups"]
found = []
for glob, mem in groups.items():
    if len(found) >= 12: break
    if len(mem) < 2: continue
    for (B2, Bq, mf) in mem:
        if not mf: continue
        p, a, F = fibers(B2, Bq)
        if len(set(p)) < 2 or len(set(a)) < 2: continue
        J = joints(p, a)
        for (B2b, Bqb, _) in mem:
            if (B2b, Bqb) == (B2, Bq): continue
            pb, ab, Fb = fibers(B2b, Bqb)
            Jb = joints(pb, ab)
            pis = [pi for pi in perms if all(Jb[r] == J[pi[r]] for r in range(4))]
            if pis and any(pi in ROTS for pi in pis):
                print(f"PAIR {(B2,Bq)} vs {(B2b,Bqb)} pis={pis}", flush=True)
                show(B2, Bq, "A ")
                show(B2b, Bqb, "Ap")
                found.append(((B2, Bq), (B2b, Bqb), pis))
                break
        break
print(f"TOTAL rotation pairs found: {len(found)}")
for f in found: print(f)
