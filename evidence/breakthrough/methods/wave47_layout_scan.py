# Wave 47, task 1 — do other mixed pairs share the representative pair's layout?
# Layout = fiber position sets (A and Ap sides). Representative pair:
# A=((0,512),(0,1)) vs Ap=((0,512),(0,16)); canonical layout printed for comparison.
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
ID, REV = (0, 1, 2, 3), (0, 3, 2, 1)

def layout_of(B2, Bq):
    p = seq_fast(B2, AP8, 8192); a = seq_fast(Bq, AP17, 17)
    F = defaultdict(list)
    for i in range(32): F[(p[i], a[i])].append(i)
    # canonical: tuple of (value, tuple(positions)) sorted by value
    return tuple((v, tuple(F[v])) for v in sorted(F))

repA = layout_of((0, 512), (0, 1))
repAp = layout_of((0, 512), (0, 16))
print("representative A layout:")
for v, pos in repA: print("  ", v, pos)
print("representative Ap layout:")
for v, pos in repAp: print("  ", v, pos)

def pos_layout(B2, Bq):
    p = seq_fast(B2, AP8, 8192); a = seq_fast(Bq, AP17, 17)
    F = defaultdict(list)
    for i in range(32): F[(p[i], a[i])].append(i)
    return tuple(sorted(tuple(F[v]) for v in F))
rep_posA = pos_layout((0, 512), (0, 1))
rep_posAp = pos_layout((0, 512), (0, 16))
print("representative position-set layout (A):", rep_posA)
print("representative position-set layout (Ap):", rep_posAp)

data = pickle.load(open("wave46_rho_groups.pkl", "rb"))
groups = data["groups"]
found = []
scanned = 0
for glob, mem in groups.items():
    if len(found) >= 12 or scanned >= 2000: break
    scanned += 1
    for (B2, Bq, mf) in mem:
        if not mf: continue
        p = seq_fast(B2, AP8, 8192); a = seq_fast(Bq, AP17, 17)
        if len(set(p)) < 2 or len(set(a)) < 2: continue
        J = joints(p, a)
        for (B2b, Bqb, _) in mem:
            if (B2b, Bqb) == (B2, Bq): continue
            pb = seq_fast(B2b, AP8, 8192); ab = seq_fast(Bqb, AP17, 17)
            Jb = joints(pb, ab)
            pis = [pi for pi in perms if all(Jb[r] == J[pi[r]] for r in range(4))]
            if pis and any(pi != ID for pi in pis):
                LA, LAp = pos_layout(B2, Bq), pos_layout(B2b, Bqb)
                same = (LA == rep_posA and LAp == rep_posAp) or (LA == rep_posAp and LAp == rep_posA)
                found.append(((B2, Bq), (B2b, Bqb), pis, same))
                print(f"pair {(B2,Bq)} vs {(B2b,Bqb)} pis={pis} pos-layout identical: {same}", flush=True)
                break
        break
print(f"scanned {scanned} groups, found {len(found)} pairs with non-id pi; "
      f"identical position layout: {sum(1 for f in found if f[3])}/{len(found)}")
