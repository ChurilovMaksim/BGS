# Wave 47, task 1 — nondegenerate quadruple witnesses, built from wave-46 triple
# witnesses: (1,1) vs (1,576) fails under id (=> passes under rev);
# (1,1) vs (239,408) fails under reversal (=> passes under id).
# Pair: ((0,512),(0,1)) vs ((0,512),(0,16)). C3 id-type: (0,1)->(0,1);
# rev-type: (0,1)->(0,2). Check quadruple matching + pi-sets at 577 and 3.
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
p = seq_fast((0, 512), AP8, 8192); pp = seq_fast((0, 512), AP8, 8192)
a = seq_fast((0, 1), AP17, 17); ap = seq_fast((0, 16), AP17, 17)
FA, FAp = defaultdict(list), defaultdict(list)
for i in range(32): FA[(p[i], a[i])].append(i)
for j in range(32): FAp[(pp[j], ap[j])].append(j)
def bseq(C, M):
    AP = [pw(ALPHA, i, M) for i in range(32)]
    return [ (2*((C[0]*x[0]+2*C[1]*x[1]) % M)) % M for x in AP ]
def check(C577, C577p, C3, C3p, label):
    b = bseq(C577, 577); bp = bseq(C577p, 577)
    b3 = bseq(C3, 3); b3p = bseq(C3p, 3)
    # quadruple matching: per fiber, sorted (b577, b3) == sorted (bp577, bp3)
    ok = True
    for v in sorted(FA):
        lhs = sorted((b[i], b3[i]) for i in FA[v])
        rhs = sorted((bp[j], b3p[j]) for j in FAp[v])
        if lhs != rhs: ok = False
    JA = joints(p, b); JB = joints(pp, bp)
    pis577 = [pi for pi in perms if all(JB[r] == JA[pi[r]] for r in range(4))]
    JA3 = joints(p, b3); JB3 = joints(pp, b3p)
    pis3 = [pi for pi in perms if all(JB3[r] == JA3[pi[r]] for r in range(4))]
    common = sorted(set(pis577) & set(pis3) & {ID, REV})
    print(f"{label}: quadruple_match={ok} pi577={pis577} pi3={pis3} common(id/rev)={common}")
    return ok and len(common) > 0
r1 = check((1, 1), (1, 576), (0, 1), (0, 2), "rev-type")
r2 = check((1, 1), (239, 408), (0, 1), (0, 1), "id-type")
print("BOTH WITNESSES PASS:", r1 and r2)
