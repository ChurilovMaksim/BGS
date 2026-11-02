# Independent witness extraction for the strong-form counterexample (pair 1).
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
B2, Bq = (0, 512), (0, 1)
B2p, Bqp = (0, 512), (0, 16)
p, pp = seq_fast(B2, AP8, 8192), seq_fast(B2p, AP8, 8192)
a, ap = seq_fast(Bq, AP17, 17), seq_fast(Bqp, AP17, 17)
assert sorted(zip(p, a)) == sorted(zip(pp, ap)), "pair globals differ"
FA, FAp = defaultdict(list), defaultdict(list)
for i in range(32): FA[(p[i], a[i])].append(i)
for j in range(32): FAp[(pp[j], ap[j])].append(j)
mf = {v: idx for v, idx in FA.items() if len({i % 4 for i in idx}) > 1}
print("mixed fibers:", list(mf.items()))
print("fiber sizes:", sorted(len(v) for v in FA.values()))
q = 577
APq = [pw(ALPHA, i, q) for i in range(32)]
Re = np.array([x[0] for x in APq], dtype=np.int64)
Im = np.array([x[1] for x in APq], dtype=np.int64)
xs = np.repeat(np.arange(q), q); ys = np.tile(np.arange(q), q)
Bmat = ((2*xs[:, None]*Re[None, :] + 4*ys[:, None]*Im[None, :]) % q).astype(np.int16)
vals = sorted(FA)
def sig_of_row(row, fib):
    return tuple(tuple(sorted(int(Bmat[row, i]) for i in fib[v])) for v in vals)
# group rows by signature (A side and B side)
from collections import defaultdict
gA, gB = defaultdict(list), defaultdict(list)
for idx in range(len(xs)):
    gA[sig_of_row(idx, FA)].append(idx)
    gB[sig_of_row(idx, FAp)].append(idx)
common = [s for s in gA if s in gB]
print(f"common signatures: {len(common)}")
ID, REV = (0,1,2,3), (0,3,2,1)
found = {}
for s in common:
    done = len(found) == 2
    if done: break
    for ia in gA[s][:3]:
        b = [int(v) for v in Bmat[ia]]; Jb = joints(p, b)
        for ib in gB[s][:3]:
            bp = [int(v) for v in Bmat[ib]]; Jbp = joints(pp, bp)
            assert sorted(zip(p, a, b)) == sorted(zip(pp, ap, bp)), "triple mismatch!"
            for pi, name in ((ID, "id"), (REV, "reversal")):
                if name not in found and not all(Jbp[r] == Jb[pi[r]] for r in range(4)):
                    found[name] = ((int(xs[ia]), int(ys[ia])), (int(xs[ib]), int(ys[ib])))
                    print(f"WITNESS fail-under-{name}: C={found[name][0]} Cp={found[name][1]}")
        if len(found) == 2: break
print("witnesses:", found)
