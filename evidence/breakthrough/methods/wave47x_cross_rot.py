# Wave 47x, task E — cross-component consistency at (577,3) for rotation pairs R1, R2.
# Quadruple matching = per-fiber (b577, b3) multisets equal. Checks the exact
# C3-relation + witnesses with direct pi-set intersection.
import numpy as np, sys
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
def bseq(C, M):
    AP = [pw(ALPHA, i, M) for i in range(32)]
    return [ (2*((C[0]*x[0]+2*C[1]*x[1]) % M)) % M for x in AP ]
# --- verify q=3 tag structure: b3(i) depends only on class, f=(2s,2t,s,t) ---
for C3 in [(1, 0), (0, 1), (1, 2), (2, 1)]:
    s, t = C3
    b = bseq(C3, 3)
    f = [(2*s) % 3, (2*t) % 3, s % 3, t % 3]
    assert all(b[i] == f[i % 4] for i in range(32)), (C3, b, f)
print("q=3 tag structure verified: b3(i) = f[class(i)], f=(2s,2t,s,t)", flush=True)

Re = np.array([x[0] for x in AP577], dtype=np.int64)
Im = np.array([x[1] for x in AP577], dtype=np.int64)
xs = np.repeat(np.arange(MOD), MOD); ys = np.tile(np.arange(MOD), MOD)
Bmat = ((2*xs[:, None]*Re[None, :] + 4*ys[:, None]*Im[None, :]) % MOD).astype(np.int16)
print("Bmat ready", flush=True)
C3list = [(s, t) for s in range(3) for t in range(3)]
def f_of(c3):
    s, t = c3
    return np.array([(2*s) % 3, (2*t) % 3, s % 3, t % 3], dtype=np.int64)

def run(name, B2, Bq, B2p, Bqp, rel_ok, rel_label):
    print(f"===== {name}: A={B2},{Bq} Ap={B2p},{Bqp}", flush=True)
    p, pp = seq_fast(B2, AP8, 8192), seq_fast(B2p, AP8, 8192)
    a, ap = seq_fast(Bq, AP17, 17), seq_fast(Bqp, AP17, 17)
    FA, FAp = defaultdict(list), defaultdict(list)
    for i in range(32): FA[(p[i], a[i])].append(i)
    for j in range(32): FAp[(pp[j], ap[j])].append(j)
    vals = sorted(FA)
    assert sorted(FAp) == vals
    J, Jb = joints(p, a), joints(pp, ap)
    pis = [pi for pi in perms if all(Jb[r] == J[pi[r]] for r in range(4))]
    print(f"  pis={pis}", flush=True)
    def sig_matrix(F):
        return np.concatenate([np.sort(Bmat[:, F[v]], axis=1) for v in vals], axis=1)
    SA = sig_matrix(FA); SB = sig_matrix(FAp)
    UA, invA = np.unique(SA, axis=0, return_inverse=True)
    UB, invB = np.unique(SB, axis=0, return_inverse=True)
    setA = {UA[k].tobytes(): k for k in range(len(UA))}
    setB = {UB[k].tobytes(): k for k in range(len(UB))}
    common577 = set(setA) & set(setB)
    print(f"  common 577 triple signatures: {len(common577)}", flush=True)
    maskA = np.array([UA[k].tobytes() in common577 for k in invA])
    maskB = np.array([UB[k].tobytes() in common577 for k in invB])
    rowsA = np.where(maskA)[0]; rowsB = np.where(maskB)[0]
    BA = Bmat[rowsA]; BB = Bmat[rowsB]
    fibA = [np.array(FA[v], dtype=np.int64) for v in vals]
    fibB = [np.array(FAp[v], dtype=np.int64) for v in vals]
    def side_counts(B, fib):
        chunk_U, chunk_inv = [], []
        for ci in range(9):
            f = f_of(C3list[ci])
            tag = f[np.arange(32) % 4]
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
            counts[:, ci] = np.bincount(gids[chunk_inv[ci]], minlength=n)
        return Ug, counts
    UgA, cntA = side_counts(BA, fibA)
    print(f"  A quad-sig uniques: {len(UgA)}", flush=True)
    UgB, cntB = side_counts(BB, fibB)
    print(f"  B quad-sig uniques: {len(UgB)}", flush=True)
    both = np.concatenate([UgA, UgB], axis=0)
    Uboth, inv_both, cnt_both = np.unique(both, axis=0, return_inverse=True, return_counts=True)
    common_mask = cnt_both == 2
    print(f"  common quad signatures: {int(common_mask.sum())}", flush=True)
    idA = inv_both[:len(UgA)]; idB = inv_both[len(UgA):]
    common_ids = np.where(common_mask)[0]
    pos_in_common = {int(g): k for k, g in enumerate(common_ids)}
    maskA_c = np.array([int(g) in pos_in_common for g in idA])
    maskB_c = np.array([int(g) in pos_in_common for g in idB])
    cA = cntA[maskA_c]; cB = cntB[maskB_c]
    ordA = np.array([pos_in_common[int(g)] for g in idA[maskA_c]])
    ordB = np.array([pos_in_common[int(g)] for g in idB[maskB_c]])
    cA_ord = np.zeros((len(common_ids), 9), dtype=np.int64)
    cB_ord = np.zeros((len(common_ids), 9), dtype=np.int64)
    cA_ord[ordA] = cA; cB_ord[ordB] = cB
    T = cA_ord.T @ cB_ord
    print(f"  total quadruple pairs: {int(T.sum())}")
    print("  T matrix rows C3A, cols C3B (order (0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)):")
    print(T)
    viol = 0; viol_detail = []
    for i in range(9):
        for j in range(9):
            if T[i, j] == 0: continue
            if not rel_ok(C3list[i], C3list[j]):
                viol += int(T[i, j]); viol_detail.append((C3list[i], C3list[j], int(T[i, j])))
    print(f"  RELATION VIOLATIONS: {viol} {viol_detail}")
    # witnesses: one per relation type present
    def find_witness(i, j):
        cand = np.where((cA_ord[:, i] > 0) & (cB_ord[:, j] > 0))[0]
        assert len(cand) > 0, (i, j)
        k = int(cand[0])
        ugA_idx = np.where(idA == common_ids[k])[0][0]
        ugB_idx = np.where(idB == common_ids[k])[0][0]
        f = f_of(C3list[i]); tag = f[np.arange(32) % 4]
        codes = BA.astype(np.int32)*3 + tag[None, :]
        Q = np.concatenate([np.sort(codes[:, fb], axis=1) for fb in fibA], axis=1).astype(np.int16)
        hits = np.where((Q == UgA[ugA_idx][None, :]).all(axis=1))[0]
        assert len(hits) > 0
        rA = int(rowsA[hits[0]])
        f2 = f_of(C3list[j]); tag2 = f2[np.arange(32) % 4]
        codes2 = BB.astype(np.int32)*3 + tag2[None, :]
        Q2 = np.concatenate([np.sort(codes2[:, fb], axis=1) for fb in fibB], axis=1).astype(np.int16)
        hits2 = np.where((Q2 == UgB[ugB_idx][None, :]).all(axis=1))[0]
        assert len(hits2) > 0
        rB = int(rowsB[hits2[0]])
        return (int(xs[rA]), int(ys[rA])), (int(xs[rB]), int(ys[rB]))
    seen_types = set()
    for i in range(9):
        for j in range(9):
            if T[i, j] == 0: continue
            key = rel_label(C3list[i], C3list[j])
            if key in seen_types: continue
            seen_types.add(key)
            CA, CB = find_witness(i, j)
            bA577 = bseq(CA, 577); bB577 = bseq(CB, 577)
            JA = joints(p, bA577); JB = joints(pp, bB577)
            pis577 = [pi for pi in perms if all(JB[r] == JA[pi[r]] for r in range(4))]
            JA3 = joints(p, bseq(C3list[i], 3)); JB3 = joints(pp, bseq(C3list[j], 3))
            pis3 = [pi for pi in perms if all(JB3[r] == JA3[pi[r]] for r in range(4))]
            common_pi = set(pis577) & set(pis3) & set(pis)
            print(f"  witness {key}: C3A={C3list[i]} C3B={C3list[j]} C577={CA} C577'={CB}")
            print(f"    pi-set(577)={pis577} pi-set(3)={pis3} common-in-pis={common_pi} OK={len(common_pi) > 0}")
            assert len(common_pi) > 0, "NO COMMON PI IN WITNESS"
    print(f"  {name} DONE: violations={viol}, witness types={seen_types}", flush=True)

def rel_R1(cA, cB):
    s, t = cA; sp, tp = cB
    return sp == (2*s) % 3 and tp in (t, (2*t) % 3)
def lab_R1(cA, cB):
    s, t = cA; sp, tp = cB
    if t == 0: return "both-type (t=0)"
    return "PI2-type (tp=t)" if tp == t else "ROT-type (tp=2t)"
def rel_R2(cA, cB):
    s, t = cA; sp, tp = cB
    return tp == (2*t) % 3 and sp in (s, (2*s) % 3)
def lab_R2(cA, cB):
    s, t = cA; sp, tp = cB
    if s == 0: return "both-type (s=0)"
    return "PI2-type (sp=s)" if sp == s else "ROT-type (sp=2s)"
run("R1", (0, 512), (0, 1), (0, 512), (7, 0), rel_R1, lab_R1)
run("R2", (0, 512), (1, 5), (0, 512), (1, 12), rel_R2, lab_R2)
print("ALL DONE")
