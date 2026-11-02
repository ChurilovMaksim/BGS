# Triple test at q=577 for a MIXED-fiber pair: does triple matching force
# joints under each pair-level pi? (Strong form of the common-pi step.)
import numpy as np
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
# candidate
B2, Bq = (8064, 8128), (16, 8)
B2p, Bqp = (384, 64), (5, 12)
p, pp = seq_fast(B2, AP8, 8192), seq_fast(B2p, AP8, 8192)
a, ap = seq_fast(Bq, AP17, 17), seq_fast(Bqp, AP17, 17)
assert sorted(zip(p, a)) == sorted(zip(pp, ap)), "pair globals differ!"
FA, FAp = defaultdict(list), defaultdict(list)
for i in range(32): FA[(p[i], a[i])].append(i)
for j in range(32): FAp[(pp[j], ap[j])].append(j)
assert set(FA) == set(FAp)
mf = {v: idx for v, idx in FA.items() if len({i % 4 for i in idx}) > 1}
print("mixed fibers of A:", list(mf.items())[:4], " total mixed:", len(mf))
print("nfibers:", len(FA), " fiber sizes:", sorted(len(v) for v in FA.values()))
perms = [tuple((e*r+b) % 4 for r in range(4)) for e in (1,-1) for b in range(4)]
J, Jp = joints(p, a), joints(pp, ap)
piset = [pi for pi in perms if all(Jp[r] == J[pi[r]] for r in range(4))]
print("pair pi-set:", piset)
# q=577 sequences for all C
q = 577
APq = [pw(ALPHA, i, q) for i in range(32)]
Re = np.array([x[0] for x in APq], dtype=np.int64)
Im = np.array([x[1] for x in APq], dtype=np.int64)
xs = np.repeat(np.arange(q), q)
ys = np.tile(np.arange(q), q)
Bmat = (2*xs[:, None]*Re[None, :] + 4*ys[:, None]*Im[None, :]) % q
Bmat = Bmat.astype(np.int16)
print("Bmat:", Bmat.shape, flush=True)
vals = sorted(FA)
def sig_matrix(fib):
    parts = []
    for v in vals:
        cols = fib[v]
        parts.append(np.sort(Bmat[:, cols], axis=1))
    return np.concatenate(parts, axis=1)
SA = sig_matrix(FA); SB = sig_matrix(FAp)
print("signatures built", flush=True)
UA, invA, cntA = np.unique(SA, axis=0, return_inverse=True, return_counts=True)
UB, invB, cntB = np.unique(SB, axis=0, return_inverse=True, return_counts=True)
print(f"distinct sigs A={len(UA)} B={len(UB)}", flush=True)
# intersect signatures via bytes
def to_dict(U, inv, cnt):
    d = {}
    for k in range(len(U)):
        d[U[k].tobytes()] = (k, cnt[k])
    return d
dA, dB = to_dict(UA, invA, cntA), to_dict(UB, invB, cntB)
common = set(dA) & set(dB)
print(f"common signatures: {len(common)}", flush=True)
# rows per signature
rowsA = defaultdict(list); rowsB = defaultdict(list)
for idx, k in enumerate(invA):
    if UA[k].tobytes() in common: rowsA[UA[k].tobytes()].append(idx)
for idx, k in enumerate(invB):
    if UB[k].tobytes() in common: rowsB[UB[k].tobytes()].append(idx)
tot_pairs = sum(len(rowsA[s]) * len(rowsB[s]) for s in common)
print(f"triple-matching (C,C') pairs: {tot_pairs}", flush=True)
# joints check per pi
bad = {pi: 0 for pi in piset}
bad_examples = {pi: [] for pi in piset}
checked = 0
for s in common:
    for ia in rowsA[s]:
        b = [int(v) for v in Bmat[ia]]
        Jb = joints(p, b)
        for ib in rowsB[s]:
            bp = [int(v) for v in Bmat[ib]]
            Jbp = joints(pp, bp)
            checked += 1
            for pi in piset:
                if not all(Jbp[r] == Jb[pi[r]] for r in range(4)):
                    bad[pi] += 1
                    if len(bad_examples[pi]) < 3:
                        bad_examples[pi].append(((int(xs[ia]), int(ys[ia])), (int(xs[ib]), int(ys[ib]))))
print(f"pairs checked: {checked}")
for pi in piset:
    print(f"  pi={pi}: JOINTS-BAD={bad[pi]} examples={bad_examples[pi]}")
