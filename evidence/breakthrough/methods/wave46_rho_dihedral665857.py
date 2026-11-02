# Mixed-pair triple test at q=665857 (alpha^16=-1) via dihedral-option solving.
# Fiber {k,l,k+16,l+16} has q-multiset {w,z,-w,-z}; matching <=> (w',z') in
# D(w,z) (8 options). Solve C' from fiber 0's two equations, verify all.
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
assert pw(ALPHA, 16, q) == (q-1, 0) and pw(ALPHA, 32, q) == (1, 0)
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
assert sorted(zip(p, a)) == sorted(zip(pp, ap))
FA, FAp = defaultdict(list), defaultdict(list)
for i in range(32): FA[(p[i], a[i])].append(i)
for j in range(32): FAp[(pp[j], ap[j])].append(j)
vals = sorted(FA)
def reps(fib):
    # one representative per {i, i+16} pair
    return sorted(i for i in fib if i < 16)
RA = {v: reps(FA[v]) for v in vals}
RB = {v: reps(FAp[v]) for v in vals}
for v in vals:
    assert len(RA[v]) == 2 and len(RB[v]) == 2, (v, RA[v], RB[v])
print("all fibers: 2 pairs each; matched by pair-value:", len(vals), flush=True)
Re = [x[0] for x in APq]; Im = [x[1] for x in APq]
def wval(C, i): return (2*C[0]*Re[i] + 4*C[1]*Im[i]) % q
def seq_q(C): return [(2*C[0]*Re[i] + 4*C[1]*Im[i]) % q for i in range(32)]
def doptions(w, z):
    opts = {(w, z), ((-w) % q, (-z) % q), (w, (-z) % q), ((-w) % q, z),
            (z, w), ((-z) % q, (-w) % q), (z, (-w) % q), ((-z) % q, w)}
    return opts
import random
random.seed(11)
tot = 0; bad = {(1,2,3,0): 0, (2,1,0,3): 0}; badex = []
for trial in range(5):
    C = (random.randrange(q), random.randrange(q))
    if C == (0, 0): continue
    b = seq_q(C)
    # sanity: fiber values are (w,z,-w,-z)
    for v in vals:
        r1, r2 = RA[v]
        assert (b[r1+16] + b[r1]) % q == 0 and (b[r2+16] + b[r2]) % q == 0
    wz = {v: (b[RA[v][0]], b[RA[v][1]]) for v in vals}
    sols = {}
    v0, v1 = vals[0], vals[1]
    for o0 in doptions(*wz[v0]):
        for o1 in doptions(*wz[v1]):
            # solve from fiber v0's two equations on B side
            r1, r2 = RB[v0]
            A00, A01 = (2*Re[r1]) % q, (4*Im[r1]) % q
            A10, A11 = (2*Re[r2]) % q, (4*Im[r2]) % q
            det = (A00*A11 - A01*A10) % q
            if det == 0: continue
            inv = pow(det, -1, q)
            c0 = ((o0[0]*A11 - o0[1]*A01) * inv) % q
            c1 = ((A00*o0[1] - A10*o0[0]) * inv) % q
            Cp = (c0, c1)
            ok = True
            for v in vals:
                w2 = (wval(Cp, RB[v][0]), wval(Cp, RB[v][1]))
                if w2 not in doptions(*wz[v]): ok = False; break
            if ok: sols[(o0, o1)] = Cp
    print(f"trial {trial}: C={C} solutions={len(sols)}", flush=True)
    for Cp in sols.values():
        bp = seq_q(Cp)
        assert sorted(zip(p, a, b)) == sorted(zip(pp, ap, bp)), "triple mismatch?!"
        Jb, Jbp = joints(p, b), joints(pp, bp)
        tot += 1
        for pi in bad:
            if not all(Jbp[r] == Jb[pi[r]] for r in range(4)):
                bad[pi] += 1
                if len(badex) < 3: badex.append((C, Cp, pi))
print(f"triple-matching pairs tested: {tot}; bad: {bad}; examples: {badex}")
