# Wave 45, task 1 — reversal-family inheritance check (m=32, (8192,17)+577).
# Verifies: witness pair, fibers, rho, alpha^16=1, graph C=alpha*conj(C'),
# pointwise b'∘rho=b, joints at 577 under reversal, pi-set survey.
from collections import defaultdict
ALPHA = (3, 2)
def mul(a, b, M): return ((a[0]*b[0]+2*a[1]*b[1]) % M, (a[0]*b[1]+a[1]*b[0]) % M)
def pw(a, n, M):
    r = (1, 0)
    while n:
        if n & 1: r = mul(r, a, M)
        a = mul(a, a, M); n >>= 1
    return r
def conj(z, M): return (z[0], (-z[1]) % M)
m, q2, q, t = 32, 8192, 17, 4
MOD = 577
def seq(B, M):
    ap = [pw(ALPHA, i, M) for i in range(m)]
    return [(2*mul(B, a, M)[0]) % M for a in ap]
p = seq((128, 64), q2); a = seq((8, 8), q); ap = seq((9, 9), q)
assert sorted(zip(p, a)) == sorted(zip(p, ap)), "pair globals differ"
def joints(pp, oo): return tuple(tuple(sorted(zip(pp[r::t], oo[r::t]))) for r in range(t))
perms = [tuple((e*r+b) % t for r in range(t)) for e in (1, -1) for b in range(t)]
J, Jp = joints(p, a), joints(p, ap)
assert [pi for pi in perms if all(Jp[r] == J[pi[r]] for r in range(t))] == [(3, 2, 1, 0)]
rho = lambda i: (15-i) % 32
assert all((p[rho(i)], ap[rho(i)]) == (p[i], a[i]) for i in range(m)), "rho not a witness"
assert pw(ALPHA, 16, MOD) == (1, 0), "alpha^16 != 1 mod 577R"
assert conj(pw(ALPHA, 15, MOD), MOD) == ALPHA
import random
random.seed(11)
REV = (3, 2, 1, 0)
for _ in range(200):
    s, tt = random.randrange(MOD), random.randrange(MOD)
    if s == 0 and tt == 0: continue
    C = ((3*s-4*tt) % MOD, (2*s-3*tt) % MOD); Cp = (s, tt)
    assert mul(ALPHA, conj(Cp, MOD), MOD) == C, "graph identity fails"
    b, bp = seq(C, MOD), seq(Cp, MOD)
    assert all(bp[rho(i)] == b[i] for i in range(m)), "pointwise identity fails"
    assert sorted(zip(p, a, b)) == sorted(zip(p, ap, bp)), "triple mismatch"
    Jb, Jbp = joints(p, b), joints(p, bp)
    ps = [pi for pi in perms if all(Jbp[r] == Jb[pi[r]] for r in range(t))]
    assert REV in ps, f"reversal missing from pi-set(577): {ps}"
print("REVERSAL FAMILY: all checks PASS (witness, rho, graph, pointwise identity, pi-set)")
