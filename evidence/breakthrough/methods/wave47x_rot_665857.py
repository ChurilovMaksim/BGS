# Wave 47x, task E — triple matching at q=665857 (alpha^16 = -1) for rotation
# pairs R1, R2. Complete per-D solver: for a base fiber, try every ordered pair
# of target-multiset values at two nonsingular solving positions, solve C',
# verify ALL fibers' multisets. (No doptions assumption: works for size-8 fibers.)
import random
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
Re = [x[0] for x in APq]; Im = [x[1] for x in APq]
def seq_fast(B, AP, M):
    return tuple((2*((B[0]*a[0]+2*B[1]*a[1]) % M)) % M for a in AP)
def seq_q(C):
    return [(2*C[0]*Re[i] + 4*C[1]*Im[i]) % q for i in range(32)]
def joints(ppp, oo, t=4):
    return tuple(tuple(sorted(zip(ppp[r::t], oo[r::t]))) for r in range(t))
perms = [tuple((e*r+b) % 4 for r in range(4)) for e in (1, -1) for b in range(4)]
print("alpha^8 =", pw(ALPHA, 8, q), " alpha^16 =", pw(ALPHA, 16, q), flush=True)

def run(name, A, Ap, trials=300, seed=5):
    B2, Bq = A; B2p, Bqp = Ap
    p, pp = seq_fast(B2, AP8, 8192), seq_fast(B2p, AP8, 8192)
    a, ap = seq_fast(Bq, AP17, 17), seq_fast(Bqp, AP17, 17)
    FA, FAp = defaultdict(list), defaultdict(list)
    for i in range(32): FA[(p[i], a[i])].append(i)
    for j in range(32): FAp[(pp[j], ap[j])].append(j)
    vals = sorted(FA)
    assert sorted(FAp) == vals
    J, Jb = joints(p, a), joints(pp, ap)
    pis = [pi for pi in perms if all(Jb[r] == J[pi[r]] for r in range(4))]
    # base fiber: first mixed fiber; solving positions: two Ap positions with det != 0
    base = None
    for v in vals:
        if len({i % 4 for i in FA[v]}) > 1:
            base = v; break
    assert base is not None
    posB = FAp[base]
    r1 = r2 = None
    for x in posB:
        for y in posB:
            if x == y: continue
            det = ((2*Re[x])*(4*Im[y]) - (4*Im[x])*(2*Re[y])) % q
            if det != 0:
                r1, r2 = x, y; break
        if r1 is not None: break
    assert r1 is not None, "no nonsingular solving pair"
    A00, A01 = (2*Re[r1]) % q, (4*Im[r1]) % q
    A10, A11 = (2*Re[r2]) % q, (4*Im[r2]) % q
    det = (A00*A11 - A01*A10) % q
    inv = pow(det, -1, q)
    print(f"===== {name}: base fiber {base}, solving positions ({r1},{r2}), pis={pis}", flush=True)
    random.seed(seed)
    tot_sol = 0; pi_hist = defaultdict(int); examples = []
    for t in range(trials):
        C = (random.randrange(q), random.randrange(q))
        if C == (0, 0): continue
        d = seq_q(C)
        target = {v: sorted(d[i] for i in FA[v]) for v in vals}
        tvals = sorted(set(target[base]))
        sols = set()
        for v1 in tvals:
            for v2 in tvals:
                c0 = ((v1*A11 - v2*A01) * inv) % q
                c1 = ((A00*v2 - A10*v1) * inv) % q
                Cp = (c0, c1)
                if Cp in sols: continue
                dp = seq_q(Cp)
                if all(sorted(dp[j] for j in FAp[v]) == target[v] for v in vals):
                    sols.add(Cp)
        for Cp in sols:
            dp = seq_q(Cp)
            assert sorted(zip(p, a, d)) == sorted(zip(pp, ap, dp))
            Jd, Jdp = joints(p, d), joints(pp, dp)
            pset = tuple(pi for pi in perms if all(Jdp[r] == Jd[pi[r]] for r in range(4)))
            pi_hist[pset] += 1
            if len(examples) < 3: examples.append((C, Cp, pset))
        tot_sol += len(sols)
    print(f"  trials={trials} triple-matching pairs={tot_sol} pi-set histogram={dict(pi_hist)}")
    for e in examples: print(f"  example C={e[0]} Cp={e[1]} pi-set={e[2]}")
    print(f"  {name} DONE", flush=True)

run("R1", ((0, 512), (0, 1)), ((0, 512), (7, 0)))
run("R2", ((0, 512), (1, 5)), ((0, 512), (1, 12)))
print("ALL DONE")
