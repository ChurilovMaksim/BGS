# Triple test at q=577 over many diverse MIXED-fiber pairs.
import pickle, numpy as np, json
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
def sig_matrix(Bmat, fib, vals):
    parts = [np.sort(Bmat[:, fib[v]], axis=1) for v in vals]
    return np.concatenate(parts, axis=1)
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
        SA = sig_matrix(Bmat, FA, vals); SB = sig_matrix(Bmat, FAp, vals)
        UA, invA = np.unique(SA, axis=0, return_inverse=True)
        UB, invB = np.unique(SB, axis=0, return_inverse=True)
        setA = {UA[k].tobytes(): k for k in range(len(UA))}
        setB = {UB[k].tobytes() for k in range(len(UB))}
        rowsA = defaultdict(list); rowsB = defaultdict(list)
        for idx, k in enumerate(invA):
            if UA[k].tobytes() in setB: rowsA[UA[k].tobytes()].append(idx)
        for idx, k in enumerate(invB):
            if UB[k].tobytes() in setA: rowsB[UB[k].tobytes()].append(idx)
        tot = sum(len(rowsA[s])*len(rowsB[s]) for s in rowsA)
        bad = {pi: 0 for pi in pis}; badex = {pi: [] for pi in pis}
        for s in rowsA:
            for ia in rowsA[s]:
                b = [int(v) for v in Bmat[ia]]; Jb = joints(p, b)
                for ib in rowsB[s]:
                    bp = [int(v) for v in Bmat[ib]]; Jbp = joints(pp, bp)
                    for pi in pis:
                        if not all(Jbp[r] == Jb[pi[r]] for r in range(4)):
                            bad[pi] += 1
                            if len(badex[pi]) < 2:
                                badex[pi].append(((int(xs[ia]), int(ys[ia])), (int(xs[ib]), int(ys[ib]))))
        seenB2.add(B2)
        results.append({"A": [B2, Bq], "Ap": [B2b, Bqb], "pis": pis,
                        "nfib": len(FA), "common_sigs": len(rowsA),
                        "pairs": tot, "bad": {str(k): v for k, v in bad.items()},
                        "badex": {str(k): v for k, v in badex.items()}})
        print(f"A={B2},{Bq} Ap={B2b},{Bqb} pis={pis} nfib={len(FA)} "
              f"common={len(rowsA)} pairs={tot} bad={bad}", flush=True)
        break
json.dump(results, open("wave46_rho_triple_loop.json", "w"))
print("TOTAL pairs:", sum(r["pairs"] for r in results),
      " TOTAL bad:", sum(sum(v for v in r["bad"].values()) for r in results))
