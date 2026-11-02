# Extended: 500 random C's at q=665857, det guard, solve from fiber 0 or 1.
from collections import defaultdict
ALPHA = (3, 2)
def mul(a, b, M): return ((a[0]*b[0]+2*a[1]*b[1]) % M, (a[0]*b[1]+a[1]*b[0]) % M)
def pw(a, n, M):
    r = (1, 0)
    while n:
        if n & 1: r = mul(r, a, M)
        a = mul(a, a, M); n >>= 1
    return r
q = 665857
AP8 = [pw(ALPHA, i, 8192) for i in range(32)]
AP17 = [pw(ALPHA, i, 17) for i in range(32)]
APq = [pw(ALPHA, i, q) for i in range(32)]
def seq_fast(B, AP, M):
    return tuple((2*((B[0]*a[0]+2*B[1]*a[1]) % M)) % M for a in AP)
def joints(ppp, oo, t=4):
    return tuple(tuple(sorted(zip(ppp[r::t], oo[r::t]))) for r in range(t))
B2, Bq = (8064, 8128), (16, 8)
B2p, Bqp = (384, 64), (5, 12)
p, pp = seq_fast(B2, AP8, 8192), seq_fast(B2p, AP8, 8192)
a, ap = seq_fast(Bq, AP17, 17), seq_fast(Bqp, AP17, 17)
FA, FAp = defaultdict(list), defaultdict(list)
for i in range(32): FA[(p[i], a[i])].append(i)
for j in range(32): FAp[(pp[j], ap[j])].append(j)
vals = sorted(FA)
RB = {v: sorted(i for i in FAp[v] if i < 16) for v in vals}
RA = {v: sorted(i for i in FA[v] if i < 16) for v in vals}
Re = [x[0] for x in APq]; Im = [x[1] for x in APq]
def wval(C, i): return (2*C[0]*Re[i] + 4*C[1]*Im[i]) % q
def seq_q(C): return [(2*C[0]*Re[i] + 4*C[1]*Im[i]) % q for i in range(32)]
def doptions(w, z):
    return {(w, z), ((-w) % q, (-z) % q), (w, (-z) % q), ((-w) % q, z),
            (z, w), ((-z) % q, (-w) % q), (z, (-w) % q), ((-z) % q, w)}
# det guard for both candidate base fibers
for v in vals[:2]:
    r1, r2 = RB[v]
    det = ((2*Re[r1])*(4*Im[r2]) - (4*Im[r1])*(2*Re[r2])) % q
    print(f"fiber {v}: reps {RB[v]} det={det} (0 means singular)", flush=True)
import random
random.seed(11)
tot = 0; bad = {(1,2,3,0): 0, (2,1,0,3): 0}; nsol = 0
for trial in range(500):
    C = (random.randrange(q), random.randrange(q))
    if C == (0, 0): continue
    b = seq_q(C)
    wz = {v: (b[RA[v][0]], b[RA[v][1]]) for v in vals}
    sols = set()
    for base in vals[:2]:
        r1, r2 = RB[base]
        A00, A01 = (2*Re[r1]) % q, (4*Im[r1]) % q
        A10, A11 = (2*Re[r2]) % q, (4*Im[r2]) % q
        det = (A00*A11 - A01*A10) % q
        if det == 0: continue
        inv = pow(det, -1, q)
        for o in doptions(*wz[base]):
            c0 = ((o[0]*A11 - o[1]*A01) * inv) % q
            c1 = ((A00*o[1] - A10*o[0]) * inv) % q
            Cp = (c0, c1)
            if all((wval(Cp, RB[v][0]), wval(Cp, RB[v][1])) in doptions(*wz[v]) for v in vals):
                sols.add(Cp)
    nsol += len(sols)
    for Cp in sols:
        bp = seq_q(Cp)
        assert sorted(zip(p, a, b)) == sorted(zip(pp, ap, bp))
        Jb, Jbp = joints(p, b), joints(pp, bp)
        tot += 1
        for pi in bad:
            if not all(Jbp[r] == Jb[pi[r]] for r in range(4)): bad[pi] += 1
print(f"trials=500 triple-matching pairs={tot} (solutions counted with multiplicity across bases removed) bad={bad}")
