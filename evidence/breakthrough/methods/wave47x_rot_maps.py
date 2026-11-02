# Wave 47x, task E — solve the linear maps L, Lp for rotation families R1, R2.
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
def bseq(C):
    return [ (2*((C[0]*x[0]+2*C[1]*x[1]) % MOD)) % MOD for x in AP577 ]
def fibers(B2, Bq):
    p = seq_fast(B2, AP8, 8192); a = seq_fast(Bq, AP17, 17)
    F = defaultdict(list)
    for i in range(32): F[(p[i], a[i])].append(i)
    return F
def mixed_bases(F):
    # mixed fibers sorted by value; bases = (min pos of each class-part), classes sorted
    out = []
    for v in sorted(F):
        idx = F[v]
        cls = sorted({i % 4 for i in idx})
        if len(cls) > 1:
            out.append((v, tuple(min(i for i in idx if i % 4 == c) for c in cls), cls))
    return out
def solve_map(b1, b2):
    # b1, b2: pairs of base positions; return rows (r1, r2) with t_k = r_k . (b_a, b_b)
    cols = []
    for C in [(1, 0), (0, 1)]:
        s = bseq(C)
        cols.append(((s[b1[0]], s[b1[1]]), (s[b2[0]], s[b2[1]])))
    (x1, y1), (t1a, t2a) = cols[0]
    (x2, y2), (t1b, t2b) = cols[1]
    det = (x1*y2 - x2*y1) % MOD
    assert det != 0, "singular base map"
    inv = pow(det, -1, MOD)
    def solve_row(t1, t2):
        return ((t1*y2 - t2*y1) * inv % MOD, (x1*t2 - x2*t1) * inv % MOD)
    return (solve_row(t1a, t1b), solve_row(t2a, t2b))
def matmul(M, N):
    return tuple(tuple(sum(M[i][k]*N[k][j] for k in range(2)) % MOD for j in range(2)) for i in range(2))
def matneg(M):
    return tuple(tuple((-x) % MOD for x in row) for row in M)
def matswap(M):
    # swap rows then swap cols? print variants
    return M

def analyze(name, A, Ap):
    FA, FAp = fibers(*A), fibers(*Ap)
    MA, MAp = mixed_bases(FA), mixed_bases(FAp)
    print(f"===== {name}: A={A} Ap={Ap}")
    print("  A mixed:", MA)
    print("  Ap mixed:", MAp)
    assert len(MA) == 2 and len(MAp) == 2, "need exactly 2 mixed fibers per side"
    (v1, b1, c1), (v2, b2, c2) = MA
    (w1, d1, e1), (w2, d2, e2) = MAp
    print("  pair-values A:", v1, v2, " Ap:", w1, w2, " values match:", (v1, v2) == (w1, w2))
    L = solve_map(b1, b2)
    Lp = solve_map(d1, d2)
    print("  A bases b1,b2:", b1, b2, " L =", L)
    print("  Ap bases d1,d2:", d1, d2, " Lp =", Lp)
    print("  L^2 =", matmul(L, L), " Lp^2 =", matmul(Lp, Lp))
    print("  Lp == L ?", Lp == L, " Lp == -L ?", Lp == matneg(L))
    # check +8 closure + sign structure on random C
    import random
    random.seed(7)
    for C in [(random.randrange(MOD), random.randrange(MOD)) for _ in range(5)]:
        s = bseq(C)
        assert all(s[(i+8) % 32] == (-s[i]) % MOD for i in range(32))
        assert all(s[(i+16) % 32] == s[i] for i in range(32))
        assert (L[0][0]*s[b1[0]]+L[0][1]*s[b1[1]]) % MOD == s[b2[0]]
        assert (L[1][0]*s[b1[0]]+L[1][1]*s[b1[1]]) % MOD == s[b2[1]]
        assert (Lp[0][0]*s[d1[0]]+Lp[0][1]*s[d1[1]]) % MOD == s[d2[0]]
        assert (Lp[1][0]*s[d1[0]]+Lp[1][1]*s[d1[1]]) % MOD == s[d2[1]]
    print("  L, Lp verified on random C; b antiperiod/period ok")
    # fiber b-multiset structure: for each mixed fiber, class-part multisets
    C = (123, 45)
    s = bseq(C)
    for tag, F, M in (("A", FA, MA), ("Ap", FAp, MAp)):
        for (v, bs, cs) in M:
            idx = F[v]
            parts = {c: sorted(s[i] for i in idx if i % 4 == c) for c in cs}
            print(f"  {tag} fiber {v}: class-part b-multisets {parts}")

analyze("R1", ((0, 512), (0, 1)), ((0, 512), (7, 0)))
analyze("R2", ((0, 512), (1, 5)), ((0, 512), (1, 12)))
analyze("FINE", ((2048, 512), (0, 4)), ((0, 512), (1, 5)))
