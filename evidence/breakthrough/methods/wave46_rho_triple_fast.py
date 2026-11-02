# Fast triple test at q=577 over mixed-fiber pairs, with joint-key aggregation:
# per-pi bad counts, fail-both (no pair-pi works) counts, and witnesses.
import pickle, numpy as np, json, itertools
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
    return tuple(tuple(sorted(zip(ppp[r::t], oo[r::t]))) for r in range(t))
perms = [tuple((e*r+b) % 4 for r in range(4)) for e in (1,-1) for b in range(4)]
data = pickle.load(open("wave46_rho_groups.pkl", "rb"))
groups = data["groups"]
q = 577
APq = [pw(ALPHA, i, q) for i in range(32)]
Re = np.array([x[0] for x in APq], dtype=np.int64)
Im = np.array([x[1] for x in APq], dtype=np.int64)
xs = np.repeat(np.arange(q), q); ys = np.tile(np.arange(q), q)
Bmat = ((2*xs[:, None]*Re[None, :] + 4*ys[:, None]*Im[None, :]) % q).astype(np.int16)
print("Bmat ready", flush=True)
CLS = [np.arange(r, 32, 4) for r in range(4)]
def sig_matrix(fib, vals):
    return np.concatenate([np.sort(Bmat[:, fib[v]], axis=1) for v in vals], axis=1)
def joint_matrix(pseq):
    parts = []
    for r in range(4):
        cols = CLS[r]
        codes = np.array(pseq, dtype=np.int64)[cols][None, :] * q + Bmat[:, cols]
        parts.append(np.sort(codes, axis=1))
    return np.concatenate(parts, axis=1).astype(np.int32)
def perm_key(key32, pi):
    # key32: flat 32 int32 = 4 blocks of 8; return key with block r <- block pi[r]
    b = key32.reshape(4, 8)
    return b[list(pi)].reshape(-1).tobytes()
results = []
seenB2 = set()
for glob, mem in groups.items():
    if len(results) >= 20: break
    if len(mem) < 2: continue
    for (B2, Bq, mf) in mem:
        if not mf or B2 in seenB2: continue
        p = seq_fast(B2, AP8, 8192); a = seq_fast(Bq, AP17, 17)
        if len(set(p)) < 2 or len(set(a)) < 2: continue
        J = joints(p, a)
        partner = None
        for (B2b, Bqb, _) in mem:
            if (B2b, Bqb) == (B2, Bq): continue
            pb = seq_fast(B2b, AP8, 8192); ab = seq_fast(Bqb, AP17, 17)
            Jb = joints(pb, ab)
            pis = [pi for pi in perms if all(Jb[r] == J[pi[r]] for r in range(4))]
            if pis and any(pi != (0,1,2,3) for pi in pis):
                partner = (B2b, Bqb, pis, pb, ab); break
        if partner is None: continue
        B2b, Bqb, pis, pp, ap = partner
        FA, FAp = defaultdict(list), defaultdict(list)
        for i in range(32): FA[(p[i], a[i])].append(i)
        for j in range(32): FAp[(pp[j], ap[j])].append(j)
        vals = sorted(FA)
        SA = sig_matrix(FA, vals); SB = sig_matrix(FAp, vals)
        UA, invA = np.unique(SA, axis=0, return_inverse=True)
        UB, invB = np.unique(SB, axis=0, return_inverse=True)
        JA = joint_matrix(p); JB = joint_matrix(pp)
        UJA, invJA = np.unique(JA, axis=0, return_inverse=True)
        UJB, invJB = np.unique(JB, axis=0, return_inverse=True)
        # (sig, jkey) combos
        PA = np.stack([invA, invJA], axis=1)
        PB = np.stack([invB, invJB], axis=1)
        UPA, invPA, cntPA = np.unique(PA, axis=0, return_inverse=True, return_counts=True)
        UPB, invPB, cntPB = np.unique(PB, axis=0, return_inverse=True, return_counts=True)
        # representative rows
        repA = {}; repB = {}
        for idx, k in enumerate(invPA):
            if k not in repA: repA[k] = idx
        for idx, k in enumerate(invPB):
            if k not in repB: repB[k] = idx
        # B jkey lookup: bytes -> index into UJB
        bkey = {UJB[k].tobytes(): k for k in range(len(UJB))}
        # group by sig
        sigA = defaultdict(list); sigB = defaultdict(list)
        for k in range(len(UPA)):
            sigA[UPA[k][0]].append((UPA[k][1], int(cntPA[k]), repA[k]))
        for k in range(len(UPB)):
            sigB[UPB[k][0]].append((UPB[k][1], int(cntPB[k]), repB[k]))
        # map sig bytes for intersection (sig indices differ across sides!)
        sigA_bytes = {UA[s].tobytes(): s for s in sigA}
        sigB_bytes = {UB[s].tobytes(): s for s in sigB}
        common = set(sigA_bytes) & set(sigB_bytes)
        tot = 0; bad = {pi: 0 for pi in pis}; failboth = 0
        wit_pi = {pi: None for pi in pis}; wit_both = None
        for sb in common:
            sA, sB = sigA_bytes[sb], sigB_bytes[sb]
            CA = sigA[sA]; CB = sigB[sB]
            nA = sum(c for _, c, _ in CA); nB = sum(c for _, c, _ in CB)
            tot += nA * nB
            # good(pi) via key permutation
            for pi in pis:
                g = 0
                for (jk, c, _) in CA:
                    pk = perm_key(UJA[jk], pi)
                    if pk in bkey:
                        bk = bkey[pk]
                        for (jk2, c2, _) in CB:
                            if jk2 == bk: g += c * c2; break
                bad[pi] += nA * nB - g
            # fail-both via inclusion-exclusion over piset
            good_any = 0
            for rlen in range(1, len(pis) + 1):
                for S in itertools.combinations(pis, rlen):
                    inter = 0
                    for (jk, c, _) in CA:
                        pks = [perm_key(UJA[jk], pi) for pi in S]
                        if all(pk == pks[0] for pk in pks) and pks[0] in bkey:
                            bk = bkey[pks[0]]
                            for (jk2, c2, _) in CB:
                                if jk2 == bk: inter += c * c2; break
                    good_any += ((-1) ** (rlen + 1)) * inter
            failboth += nA * nB - good_any
            # witnesses (first found)
            for (jk, c, ra) in CA:
                for (jk2, c2, rb) in CB:
                    for pi in pis:
                        if wit_pi[pi] is None and perm_key(UJA[jk], pi) != UJB[jk2].tobytes():
                            wit_pi[pi] = ((int(xs[ra]), int(ys[ra])), (int(xs[rb]), int(ys[rb])))
                    if wit_both is None and all(perm_key(UJA[jk], pi) != UJB[jk2].tobytes() for pi in pis):
                        wit_both = ((int(xs[ra]), int(ys[ra])), (int(xs[rb]), int(ys[rb])))
        seenB2.add(B2)
        results.append({"A": [B2, Bq], "Ap": [B2b, Bqb], "pis": pis,
                        "nfib": len(FA), "common_sigs": len(common),
                        "pairs": tot, "bad": {str(k): v for k, v in bad.items()},
                        "failboth": failboth,
                        "wit_pi": {str(k): v for k, v in wit_pi.items()},
                        "wit_both": wit_both})
        print(f"A={B2},{Bq} Ap={B2b},{Bqb} pis={pis} nfib={len(FA)} "
              f"common={len(common)} pairs={tot} bad={bad} failboth={failboth}", flush=True)
        break
json.dump(results, open("wave46_rho_triple_fast.json", "w"))
print("TOTAL pairs:", sum(r["pairs"] for r in results),
      " TOTAL failboth:", sum(r["failboth"] for r in results))
