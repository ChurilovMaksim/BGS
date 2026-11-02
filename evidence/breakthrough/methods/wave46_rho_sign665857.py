# Sign-pattern test at q=665857 (alpha^16=-1, alpha^32=1) for both GPL families.
# Fibers are {k,k+16}; q-multiset on a fiber is {w,-w}. Triple matching <=>
# per matched fiber pair w' = +/- w. Enumerate all 2^16 sign patterns, solve
# for C' from 2 fibers, verify all 16, check joints under pair-pi.
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
print("alpha^16 mod q:", pw(ALPHA, 16, q), " alpha^32 mod q:", pw(ALPHA, 32, q))
assert pw(ALPHA, 16, q) == (q-1, 0) and pw(ALPHA, 32, q) == (1, 0)
def seq(B, M):
    ap = [pw(ALPHA, i, M) for i in range(32)]
    return [(2*mul(B, a, M)[0]) % M for a in ap]
def joints(ppp, oo, t=4):
    return tuple(tuple(sorted(zip(ppp[r::t], oo[r::t]))) for r in range(t))
def test_family(name, B2, B2p, Bq, Bqp, pi):
    p, pp, a, ap = seq(B2, 8192), seq(B2p, 8192), seq(Bq, 17), seq(Bqp, 17)
    assert sorted(zip(p, a)) == sorted(zip(pp, ap)), "pair globals differ"
    # fiber partitions by pair-value
    FA, FAp = defaultdict(list), defaultdict(list)
    for i in range(32): FA[(p[i], a[i])].append(i)
    for j in range(32): FAp[(pp[j], ap[j])].append(j)
    assert set(FA) == set(FAp), "fiber value sets differ"
    # matched fiber pairs in canonical order; representatives
    vals = sorted(FA)
    repsA, repsAp = [], []
    for v in vals:
        repsA.append(FA[v][0]); repsAp.append(FAp[v][0])
    # q-sequence linear coefficients: b_i = (2*C0*Re_i + 4*C1*Im_i) % q
    apq = [pw(ALPHA, i, q) for i in range(32)]
    Re = [x[0] for x in apq]; Im = [x[1] for x in apq]
    def w_of(C, rep): return (2*C[0]*Re[rep] + 4*C[1]*Im[rep]) % q
    def seq_q(C): return [(2*C[0]*Re[i] + 4*C[1]*Im[i]) % q for i in range(32)]
    import random
    random.seed(7)
    tot_sols = 0; bad = 0; tested = 0
    for trial in range(3):
        C = (random.randrange(q), random.randrange(q))
        if C == (0, 0): continue
        w = [w_of(C, r) for r in repsA]
        # solve C' from fibers 0,1: 2*C0'*Re + 4*C1'*Im = eps*w (mod q)
        # try fiber pairs until invertible
        sols = {}
        for mask in range(1 << 16):
            eps = [1 if (mask >> k) & 1 == 0 else -1 for k in range(16)]
            target = [(eps[k]*w[k]) % q for k in range(16)]
            # solve using fibers 0,1
            r0, r1 = repsAp[0], repsAp[1]
            A00, A01 = (2*Re[r0]) % q, (4*Im[r0]) % q
            A10, A11 = (2*Re[r1]) % q, (4*Im[r1]) % q
            det = (A00*A11 - A01*A10) % q
            if det == 0: continue
            inv = pow(det, -1, q)
            c0 = ((target[0]*A11 - target[1]*A01) * inv) % q
            c1 = ((A00*target[1] - A10*target[0]) * inv) % q
            Cp = (c0, c1)
            if all(w_of(Cp, repsAp[k]) == target[k] for k in range(16)):
                sols[mask] = Cp
        tot_sols += len(sols)
        for mask, Cp in sols.items():
            b, bp = seq_q(C), seq_q(Cp)
            assert sorted(zip(p, a, b)) == sorted(zip(pp, ap, bp)), "triple mismatch?!"
            Jb, Jbp = joints(p, b), joints(pp, bp)
            ok = all(Jbp[r] == Jb[pi[r]] for r in range(4))
            tested += 1
            if not ok:
                bad += 1
                print(f"  BAD: C={C} mask={mask} Cp={Cp}")
    print(f"{name}: triple-matching (C,C') solutions tested={tested} "
          f"patterns-with-solution per C avg={tot_sols/3:.1f}  JOINTS-BAD={bad}")
test_family("reversal", (128,64), (128,64), (8,8), (9,9), (3,2,1,0))
test_family("swap", (2944,1856), (6016,832), (13,2), (13,2), (1,0,3,2))
