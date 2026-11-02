# Wave 47, task 1 — single-q weak form: layout, linear map L, 8-pattern check.
# Representative mixed pair: A=((0,512),(0,1)) vs Ap=((0,512),(0,16)), pis={id,rev}.
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
def joints(ppp, oo, t=4):
    return tuple(tuple(sorted(zip(ppp[r::t], oo[r::t]))) for r in range(t))
perms = [tuple((e*r+b) % 4 for r in range(4)) for e in (1, -1) for b in range(4)]

# --- alpha identities mod 577 ---
print("alpha^8  =", pw(ALPHA, 8, MOD), "(expect (-1,0) mod 577)")
print("alpha^16 =", pw(ALPHA, 16, MOD), "(expect (1,0))")
print("alpha^4  =", pw(ALPHA, 4, MOD))

B2, Bq = (0, 512), (0, 1)
B2p, Bqp = (0, 512), (0, 16)
p, pp = seq_fast(B2, AP8, 8192), seq_fast(B2p, AP8, 8192)
a, ap = seq_fast(Bq, AP17, 17), seq_fast(Bqp, AP17, 17)
assert sorted(zip(p, a)) == sorted(zip(pp, ap)), "pair globals differ"
J, Jb = joints(p, a), joints(pp, ap)
pis = [pi for pi in perms if all(Jb[r] == J[pi[r]] for r in range(4))]
print("pair pi-set:", pis)
FA, FAp = defaultdict(list), defaultdict(list)
for i in range(32): FA[(p[i], a[i])].append(i)
for j in range(32): FAp[(pp[j], ap[j])].append(j)
print("--- A fibers (value -> positions, classes) ---")
for v in sorted(FA):
    idx = FA[v]
    print(v, idx, "classes:", sorted({i % 4 for i in idx}))
print("--- Ap fibers ---")
for v in sorted(FAp):
    idx = FAp[v]
    print(v, idx, "classes:", sorted({i % 4 for i in idx}))
# class p-multisets (for the q=3 argument)
for r in range(4):
    print(f"class {r}: A p-multiset {sorted(p[r::4])}  Ap p-multiset {sorted(pp[r::4])}")

# --- b-structure: base positions of mixed fibers ---
def mixed_info(F):
    out = {}
    for v, idx in F.items():
        cls = {i % 4 for i in idx}
        if len(cls) > 1:
            c1 = sorted(i for i in idx if i % 4 == 1)
            c3 = sorted(i for i in idx if i % 4 == 3)
            out[v] = (c1, c3)
    return out
MA, MAp = mixed_info(FA), mixed_info(FAp)
print("A mixed fibers:", MA)
print("Ap mixed fibers:", MAp)

def bseq(C):
    return [ (2*((C[0]*x[0]+2*C[1]*x[1]) % MOD)) % MOD for x in AP577 ]
# check b_{i+8} = -b_i, b_{i+16} = b_i
b = bseq((123, 45))
print("b antiperiod/period check:", all(b[(i+8) % 32] == (-b[i]) % MOD for i in range(32)),
      all(b[(i+16) % 32] == b[i] for i in range(32)))
# L: (b_5, b_7) as function of (b_1, b_3); Lp: (bp_a', bp_c') from (bp_a, bp_c)
def solve_L(base1, base3, targ1, targ3):
    # rows: for C=(1,0) and C=(0,1), get (x,y) and (t1,t2); solve t = L x
    import itertools
    cols = []
    for C in [(1, 0), (0, 1)]:
        s = bseq(C)
        cols.append(((s[base1], s[base3]), (s[targ1], s[targ3])))
    (x1, y1), (t1a, t2a) = cols[0]
    (x2, y2), (t1b, t2b) = cols[1]
    det = (x1*y2 - x2*y1) % MOD
    assert det != 0, "base map singular"
    inv = pow(det, -1, MOD)
    # L = T * X^{-1}
    def lin_comb(t1, t2):
        # returns (c1, c2) with t = c1*x + c2*y for both targets
        pass
    # X = [[x1, x2],[y1, y2]] columns are images; solve L rows:
    # row for t1: (r1, r2) with r1*x + r2*y = t1 for both samples
    def solve_row(t1, t2):
        # [x1 y1; x2 y2] [r1; r2] = [t1; t2]
        r1 = (t1*y2 - t2*y1) * inv % MOD
        r2 = (x1*t2 - x2*t1) * inv % MOD
        return (r1, r2)
    return (solve_row(t1a, t1b), solve_row(t2a, t2b), det)
A_mixed = sorted(MA)
Ap_mixed = sorted(MAp)
print("A mixed values:", A_mixed, " Ap mixed values:", Ap_mixed)
# base positions: min class-1 / class-3 position in each mixed fiber
def bases(M):
    bs = []
    for v in sorted(M):
        c1, c3 = M[v]
        bs.append((c1[0], c3[0]))
    return bs
bA = bases(MA); bAp = bases(MAp)
print("A bases (c1,c3) per mixed fiber:", bA, " Ap bases:", bAp)
(x1, y1) = bA[0]; (x2, y2) = bA[1]
L, detL = solve_L(x1, y1, x2, y2)[:2], solve_L(x1, y1, x2, y2)[2]
print("L rows (b_targ1 = r1*x + r2*y):", L, "det(base map):", detL)
(x1p, y1p) = bAp[0]; (x2p, y2p) = bAp[1]
Lp, detLp = solve_L(x1p, y1p, x2p, y2p)[:2], solve_L(x1p, y1p, x2p, y2p)[2]
print("Lp rows:", Lp, "det:", detLp)
print("L^2 =", "check in pattern section")
# verify L, Lp by random C
import random
random.seed(1)
for _ in range(20):
    C = (random.randrange(MOD), random.randrange(MOD))
    s = bseq(C)
    assert (L[0][0]*s[x1]+L[0][1]*s[y1]) % MOD == s[x2], "L row1 fail"
    assert (L[1][0]*s[x1]+L[1][1]*s[y1]) % MOD == s[y2], "L row2 fail"
    assert (Lp[0][0]*s[x1p]+Lp[0][1]*s[y1p]) % MOD == s[x2p], "Lp row1 fail"
    assert (Lp[1][0]*s[x1p]+Lp[1][1]*s[y1p]) % MOD == s[y2p], "Lp row2 fail"
print("L, Lp verified on 20 random C")
print("Lp == -L ?", Lp[0] == ((-L[0][0]) % MOD, (-L[0][1]) % MOD) and Lp[1] == ((-L[1][0]) % MOD, (-L[1][1]) % MOD))
# position-set closure: class-1 positions of each mixed fiber = {base, base+8, base+16, base+24}
for name, M in (("A", MA), ("Ap", MAp)):
    for v, (c1, c3) in M.items():
        assert c1 == sorted({(c1[0]+8*k) % 32 for k in range(4)}), (name, v, c1)
        assert c3 == sorted({(c3[0]+8*k) % 32 for k in range(4)}), (name, v, c3)
print("mixed-fiber position sets are +8/+16-closed: True")

# --- exact polynomial pattern check mod 577 ---
# linear form (c1, c2); quad (cxx, cxy, cyy); quartic (c40, c31, c22, c13, c04)
def ladd(f, g): return ((f[0]+g[0]) % MOD, (f[1]+g[1]) % MOD)
def lscale(f, k): return ((f[0]*k) % MOD, (f[1]*k) % MOD)
def lsub(f, g): return ((f[0]-g[0]) % MOD, (f[1]-g[1]) % MOD)
def lcompose(f, S):
    # f(x', y') with (x', y') = S (x, y); S rows s1, s2 as linear forms
    return ladd(lscale(S[0], f[0]), lscale(S[1], f[1]))
def sq(f):
    return ((f[0]*f[0]) % MOD, (2*f[0]*f[1]) % MOD, (f[1]*f[1]) % MOD)
def qadd(f, g): return tuple((a+b) % MOD for a, b in zip(f, g))
def qsub(f, g): return tuple((a-b) % MOD for a, b in zip(f, g))
def qmul(f, g):
    a, b, c = f; d, e, h = g
    return ((a*d) % MOD, (a*e+b*d) % MOD, (a*h+b*e+c*d) % MOD,
            (b*h+c*e) % MOD, (c*h) % MOD)
X = (1, 0); Y = (0, 1)
X2, Y2 = sq(X), sq(Y)
L1f, L2f = L[0], L[1]
L1s, L2s = sq(L1f), sq(L2f)
Lp1f, Lp2f = Lp[0], Lp[1]
patterns = []
for swap in (0, 1):
    for s1 in (1, MOD-1):
        for s2 in (1, MOD-1):
            if swap == 0:
                S = ((s1, 0), (0, s2))
                name = f"(x',y')=({'+' if s1==1 else '-'}x,{'+' if s2==1 else '-'}y)"
            else:
                S = ((0, s1), (s2, 0))
                name = f"(x',y')=({'+' if s1==1 else '-'}y,{'+' if s2==1 else '-'}x)"
            patterns.append((name, S))
def sub_locus_id_rev(S, var):
    # check id/rev systems with var ('x' or 'y') set to 0; returns (id_ok, rev_ok)
    def q_at0(q):
        # quad (cxx, cxy, cyy): x=0 -> cyy ; y=0 -> cxx
        return q[2] if var == 'x' else q[0]
    def k_at0(k):
        # quartic: x=0 -> c04 ; y=0 -> c40
        return k[4] if var == 'x' else k[0]
    xp, yp = lcompose(X, S), lcompose(Y, S)
    Lp1c, Lp2c = lcompose(Lp1f, S), lcompose(Lp2f, S)
    Xp2, Yp2 = sq(xp), sq(yp)
    Lp1s, Lp2s = sq(Lp1c), sq(Lp2c)
    I = [qsub(qadd(X2, L1s), qadd(Xp2, Lp1s)),
         qsub(qmul(X2, L1s), qmul(Xp2, Lp1s)),
         qsub(qadd(Y2, L2s), qadd(Yp2, Lp2s)),
         qsub(qmul(Y2, L2s), qmul(Yp2, Lp2s))]
    R = [qsub(qadd(X2, L1s), qadd(Yp2, Lp2s)),
         qsub(qmul(X2, L1s), qmul(Yp2, Lp2s)),
         qsub(qadd(Y2, L2s), qadd(Xp2, Lp1s)),
         qsub(qmul(Y2, L2s), qmul(Xp2, Lp1s))]
    id_ok = all(q_at0(q) == 0 for q in I[0:1]+I[2:3]) and all(k_at0(k) == 0 for k in [I[1], I[3]])
    rev_ok = all(q_at0(q) == 0 for q in R[0:1]+R[2:3]) and all(k_at0(k) == 0 for k in [R[1], R[3]])
    return id_ok, rev_ok
print("--- 8-pattern coverage ---")
all_covered = True
for name, S in patterns:
    xp, yp = lcompose(X, S), lcompose(Y, S)
    Lp1c, Lp2c = lcompose(Lp1f, S), lcompose(Lp2f, S)
    Xp2, Yp2 = sq(xp), sq(yp)
    Lp1s, Lp2s = sq(Lp1c), sq(Lp2c)
    I = [qsub(qadd(X2, L1s), qadd(Xp2, Lp1s)),
         qsub(qmul(X2, L1s), qmul(Xp2, Lp1s)),
         qsub(qadd(Y2, L2s), qadd(Yp2, Lp2s)),
         qsub(qmul(Y2, L2s), qmul(Yp2, Lp2s))]
    R = [qsub(qadd(X2, L1s), qadd(Yp2, Lp2s)),
         qsub(qmul(X2, L1s), qmul(Yp2, Lp2s)),
         qsub(qadd(Y2, L2s), qadd(Xp2, Lp1s)),
         qsub(qmul(Y2, L2s), qmul(Xp2, Lp1s))]
    id_ok = all(q == (0, 0, 0) for q in [I[0], I[2]]) and all(k == (0, 0, 0, 0, 0) for k in [I[1], I[3]])
    rev_ok = all(q == (0, 0, 0) for q in [R[0], R[2]]) and all(k == (0, 0, 0, 0, 0) for k in [R[1], R[3]])
    Msum = qsub(qadd(L1s, L2s), qadd(Lp1s, Lp2s))
    verdict = None
    if id_ok: verdict = "id identically"
    elif rev_ok: verdict = "rev identically"
    elif Msum[0] == 0 and Msum[2] == 0 and Msum[1] != 0:
        ix, rx = sub_locus_id_rev(S, 'x')
        iy, ry = sub_locus_id_rev(S, 'y')
        # sublocus x=0 means var='x' set to 0? careful: sub_locus var='x' sets x=0
        # M2 forces xy=0: cases y=0 (var 'y') and x=0 (var 'x')
        ok_y0 = iy or ry
        ok_x0 = ix or rx
        if ok_y0 and ok_x0:
            verdict = f"M2 forces xy=0 (Msum={Msum}); subloci covered (y=0:{'id' if iy else 'rev'}, x=0:{'id' if ix else 'rev'})"
        else:
            verdict = f"NOT COVERED: Msum={Msum}, subloci y0:{ok_y0} x0:{ok_x0}"
    else:
        verdict = f"NOT COVERED: Msum={Msum}"
    if "NOT COVERED" in verdict: all_covered = False
    print(f"{name}: {verdict}")
print("ALL PATTERNS COVERED:", all_covered)
