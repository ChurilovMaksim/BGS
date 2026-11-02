# Wave 47, task 1 — cross-component consistency experiment at (577, 3).
# Pair: A=((0,512),(0,1)) vs Ap=((0,512),(0,16)). Quadruple matching =
# per-fiber (b577, b3) multisets equal. C3 = (s,t) in F3^2, f = (2s,2t,s,t).
import numpy as np
from collections import defaultdict
MOD = 577
ALPHA = (3, 2)
def mul(a, b, M): return ((a[0]*b[0]+2*a[1]*b[1]) % M, (a[0]*b[1]+a[1]*b[0]) % M)
def pw(a, n, M):
    r = (1, 0)
    for _ in range(n): r = mul(r, a, M)
    return r
AP8 = [pw(ALPHA, i, 8192) for i in range(32)]
AP17 = [pw(ALPHA, i, 17) for i in range(32)]
AP577 = [pw(ALPHA, i, MOD) for i in range(32)]
def seq_fast(B, AP, M):
    return tuple((2*((B[0]*a[0]+2*B[1]*a[1]) % M)) % M for a in AP)
def joints(ppp, oo, t=4):
    return tuple(tuple(sorted(zip(ppp[r::t], oo[r::t]))) for r in range(t))
perms = [tuple((e*r+b) % 4 for r in range(4)) for e in (1, -1) for b in range(4)]

B2, Bq = (0, 512), (0, 1)
B2p, Bqp = (0, 512), (0, 16)
p, pp = seq_fast(B2, AP8, 8192), seq_fast(B2p, AP8, 8192)
a, ap = seq_fast(Bq, AP17, 17), seq_fast(Bqp, AP17, 17)
FA, FAp = defaultdict(list), defaultdict(list)
for i in range(32): FA[(p[i], a[i])].append(i)
for j in range(32): FAp[(pp[j], ap[j])].append(j)
vals = sorted(FA)
assert sorted(FAp) == vals
print("fibers:", {v: FA[v] for v in vals})

# --- 577 side: Bmat, triple signatures, common rows ---
Re = np.array([x[0] for x in AP577], dtype=np.int64)
Im = np.array([x[1] for x in AP577], dtype=np.int64)
xs = np.repeat(np.arange(MOD), MOD); ys = np.tile(np.arange(MOD), MOD)
Bmat = ((2*xs[:, None]*Re[None, :] + 4*ys[:, None]*Im[None, :]) % MOD).astype(np.int16)
print("Bmat ready", flush=True)
def sig_matrix(F):
    return np.concatenate([np.sort(Bmat[:, F[v]], axis=1) for v in vals], axis=1)
SA = sig_matrix(FA); SB = sig_matrix(FAp)
UA, invA = np.unique(SA, axis=0, return_inverse=True)
UB, invB = np.unique(SB, axis=0, return_inverse=True)
# common triple signatures via bytes
setA = {UA[k].tobytes(): k for k in range(len(UA))}
setB = {UB[k].tobytes(): k for k in range(len(UB))}
common577 = set(setA) & set(setB)
print("common 577 triple signatures:", len(common577), "(wave 46: 83521)")
maskA = np.array([UA[k].tobytes() in common577 for k in invA])
maskB = np.array([UB[k].tobytes() in common577 for k in invB])
rowsA = np.where(maskA)[0]; rowsB = np.where(maskB)[0]
print("C577 rows in common sigs: A =", len(rowsA), " B =", len(rowsB))
BA = Bmat[rowsA]; BB = Bmat[rowsB]
# per-fiber position lists for quad codes
fibA = [np.array(FA[v], dtype=np.int64) for v in vals]
fibB = [np.array(FAp[v], dtype=np.int64) for v in vals]
C3list = [(s, t) for s in range(3) for t in range(3)]
def f_of(c3):
    s, t = c3
    return np.array([(2*s) % 3, (2*t) % 3, s % 3, t % 3], dtype=np.int64)
CLS = [np.arange(r, 32, 4) for r in range(4)]

def side_counts(B, fib):
    # returns: global quad-sig uniques Ug, count matrix (n_ug x 9)
    chunk_U = []
    chunk_inv = []
    for ci in range(9):
        f = f_of(C3list[ci])
        tag = f[np.arange(32) % 4]  # per-position tag
        codes = B.astype(np.int32)*3 + tag[None, :]
        parts = [np.sort(codes[:, fb], axis=1) for fb in fib]
        Q = np.concatenate(parts, axis=1).astype(np.int16)
        U, inv = np.unique(Q, axis=0, return_inverse=True)
        chunk_U.append(U); chunk_inv.append(inv)
    Uall = np.concatenate(chunk_U, axis=0)
    Ug, inv_all = np.unique(Uall, axis=0, return_inverse=True)
    n = len(Ug)
    counts = np.zeros((n, 9), dtype=np.int64)
    off = 0
    for ci in range(9):
        Uc = chunk_U[ci]
        gids = inv_all[off:off+len(Uc)]
        off += len(Uc)
        row_gid = gids[chunk_inv[ci]]
        bc = np.bincount(row_gid, minlength=n)
        counts[:, ci] = bc
    return Ug, counts

UgA, cntA = side_counts(BA, fibA)
print("A quad-sig uniques:", len(UgA), flush=True)
UgB, cntB = side_counts(BB, fibB)
print("B quad-sig uniques:", len(UgB), flush=True)
# common quad sigs
both = np.concatenate([UgA, UgB], axis=0)
Uboth, inv_both, cnt_both = np.unique(both, axis=0, return_inverse=True, return_counts=True)
common_mask = cnt_both == 2
print("common quad signatures:", int(common_mask.sum()))
# map: global id per side -> common index (or -1)
idA = inv_both[:len(UgA)]; idB = inv_both[len(UgA):]
common_ids = np.where(common_mask)[0]
pos_in_common = {int(g): k for k, g in enumerate(common_ids)}
maskA_c = np.array([int(g) in pos_in_common for g in idA])
maskB_c = np.array([int(g) in pos_in_common for g in idB])
cA = cntA[maskA_c]; cB = cntB[maskB_c]
# reorder to common order
ordA = np.array([pos_in_common[int(g)] for g in idA[maskA_c]])
ordB = np.array([pos_in_common[int(g)] for g in idB[maskB_c]])
cA_ord = np.zeros((len(common_ids), 9), dtype=np.int64)
cB_ord = np.zeros((len(common_ids), 9), dtype=np.int64)
cA_ord[ordA] = cA; cB_ord[ordB] = cB
T = cA_ord.T @ cB_ord
print("total quadruple pairs:", int(T.sum()))
print("T matrix (rows C3A, cols C3B), C3 order (s,t) = (0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2):")
print(T)
viol = 0; viol_detail = []
for i in range(9):
    for j in range(9):
        if T[i, j] == 0: continue
        s, t = C3list[i]; sp, tp = C3list[j]
        ok = (sp == s) and (tp in (t, (2*t) % 3))
        if not ok:
            viol += int(T[i, j]); viol_detail.append((C3list[i], C3list[j], int(T[i, j])))
print("VIOLATIONS (s'!=s or t' not in {t,2t}):", viol, viol_detail)
# relation breakdown
n_id = n_rev = n_both = 0
for i in range(9):
    for j in range(9):
        s, t = C3list[i]; sp, tp = C3list[j]
        if T[i, j] == 0: continue
        if t == 0:
            assert tp == 0
            n_both += int(T[i, j])
        elif tp == t: n_id += int(T[i, j])
        elif tp == (2*t) % 3: n_rev += int(T[i, j])
        else: print("UNEXPECTED relation", C3list[i], C3list[j])
print("C3-relation counts: id-type =", n_id, " rev-type =", n_rev, " both-type (t=0) =", n_both)

# --- witnesses: one quadruple pair per relation type, direct pi-set check ---
# find a common sig with cA[i]>0 and cB[j]>0 for chosen (i,j), then locate rows
def find_witness(i, j):
    cand = np.where((cA_ord[:, i] > 0) & (cB_ord[:, j] > 0))[0]
    assert len(cand) > 0, (i, j)
    k = int(cand[0])
    # global quad-sig row for side A at common index k: recover UgA row
    gA = int(idA[maskA_c][ordA == k][0]) if False else None
    # simpler: find UgA index whose both-id == common_ids[k]
    ugA_idx = np.where(idA == common_ids[k])[0][0]
    ugB_idx = np.where(idB == common_ids[k])[0][0]
    # locate a C577 row (A) with this quad sig and C3=i: recompute chunk i rows
    f = f_of(C3list[i])
    tag = f[np.arange(32) % 4]
    codes = BA.astype(np.int32)*3 + tag[None, :]
    parts = [np.sort(codes[:, fb], axis=1) for fb in fibA]
    Q = np.concatenate(parts, axis=1).astype(np.int16)
    target = UgA[ugA_idx]
    hits = np.where((Q == target[None, :]).all(axis=1))[0]
    assert len(hits) > 0
    rA = int(rowsA[hits[0]])
    f2 = f_of(C3list[j])
    tag2 = f2[np.arange(32) % 4]
    codes2 = BB.astype(np.int32)*3 + tag2[None, :]
    parts2 = [np.sort(codes2[:, fb], axis=1) for fb in fibB]
    Q2 = np.concatenate(parts2, axis=1).astype(np.int16)
    target2 = UgB[ugB_idx]
    hits2 = np.where((Q2 == target2[None, :]).all(axis=1))[0]
    assert len(hits2) > 0
    rB = int(rowsB[hits2[0]])
    return (int(xs[rA]), int(ys[rA])), (int(xs[rB]), int(ys[rB]))

def pi_sets(CA, CB):
    b = [int(v) for v in Bmat[np.where((xs == CA[0]) & (ys == CA[1]))[0][0]]] if False else None
    # direct: b_i = Tr(C alpha^i) mod 577 ; b3_i = Tr(C3 alpha^i) mod 3 (class-constant)
    def bseq(C, M):
        AP = [pw(ALPHA, i, M) for i in range(32)]
        return [ (2*((C[0]*x[0]+2*C[1]*x[1]) % M)) % M for x in AP ]
    bA577 = bseq(CA, 577); bB577 = bseq(CB, 577)
    JA = joints(p, bA577); JB = joints(pp, bB577)
    pis577 = [pi for pi in perms if all(JB[r] == JA[pi[r]] for r in range(4))]
    return pis577
# note: pi at 3 needs C3 values; handled by caller via f-relation; here verify 577 only + tag logic
for (i, j, label) in [(0, 0, "both-type t=0"), (1, 1, "id-type"), (1, 2, "rev-type")]:
    if T[i, j] == 0:
        print(f"witness {label} (C3A={C3list[i]}, C3B={C3list[j]}): no pairs"); continue
    CA, CB = find_witness(i, j)
    pis577 = pi_sets(CA, CB)
    print(f"witness {label}: C577={CA} C577'={CB} pi-set(577)={pis577}")
    # direct pi-set at 3 via joints with b3 sequences
    def bseq3(C3):
        AP3 = [pw(ALPHA, i, 3) for i in range(32)]
        return [ (2*((C3[0]*x[0]+2*C3[1]*x[1]) % 3)) % 3 for x in AP3 ]
    JA3 = joints(p, bseq3(C3list[i])); JB3 = joints(pp, bseq3(C3list[j]))
    pis3 = [pi for pi in perms if all(JB3[r] == JA3[pi[r]] for r in range(4))]
    print(f"   pi-set(3)={pis3}  common with {{id,rev}}: {set(pis577) & set(pis3) & {(0,1,2,3), (0,3,2,1)}}")
np.save("wave47_cross_T.npy", T)
print("saved wave47_cross_T.npy")
