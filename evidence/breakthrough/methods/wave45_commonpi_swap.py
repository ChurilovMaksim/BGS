# Wave 45, task 1 — swap-family inheritance check (m=32, (8192,17)+577).
# Verifies: swap witness pair, rho' (block reversal), graph
# C = mult((-3,2))*conj(C'), identity (-3,-2)*alpha^7 = 1,
# pointwise b∘rho' = b', joints at 577 under swap, pi-set survey.
from collections import defaultdict
ALPHA = (3, 2)
def mul(a, b, M): return ((a[0]*b[0]+2*a[1]*b[1]) % M, (a[0]*b[1]+a[1]*b[0]) % M)
def pw(a, n, M):
    r = (1, 0)
    while n:
        if n & 1: r = mul(r, a, M)
        a = mul(a, a, M); n >>= 1
    return r
m, q2, q, t = 32, 8192, 17, 4
MOD = 577
def seq(B, M):
    ap = [pw(ALPHA, i, M) for i in range(m)]
    return [(2*mul(B, a, M)[0]) % M for a in ap]
p = seq((2944, 1856), q2); pp = seq((6016, 832), q2); a = seq((13, 2), q)
assert sorted(zip(p, a)) == sorted(zip(pp, a)), "pair globals differ"
def joints(ppp, oo): return tuple(tuple(sorted(zip(ppp[r::t], oo[r::t]))) for r in range(t))
perms = [tuple((e*r+b) % t for r in range(t)) for e in (1, -1) for b in range(t)]
J, Jp = joints(p, a), joints(pp, a)
SWAP = (1, 0, 3, 2)
assert [pi for pi in perms if all(Jp[r] == J[pi[r]] for r in range(t))] == [SWAP]
FA = defaultdict(list); FP = defaultdict(list)
for i in range(m):
    FA[(p[i], a[i])].append(i); FP[(pp[i], a[i])].append(i)
used = set(); rho = {}
for j in range(m):
    cands = [i for i in FA[(pp[j], a[j])] if i % 4 == SWAP[j % 4] and i not in used]
    assert cands, "rho' not constructible"
    rho[j] = cands[0]; used.add(cands[0])
assert all((p[rho[j]], a[rho[j]]) == (pp[j], a[j]) for j in range(m)), "rho' not a witness"
assert pw(ALPHA, 16, MOD) == (1, 0)
assert mul((-3 % MOD, -2 % MOD), pw(ALPHA, 7, MOD), MOD) == (1, 0)
import random
random.seed(13)
for _ in range(200):
    s, tt = random.randrange(MOD), random.randrange(MOD)
    if s == 0 and tt == 0: continue
    C = ((-3*s-4*tt) % MOD, (2*s+3*tt) % MOD); Cp = (s, tt)
    b, bp = seq(C, MOD), seq(Cp, MOD)
    assert all(b[rho[j]] == bp[j] for j in range(m)), "pointwise identity fails"
    assert sorted(zip(p, a, b)) == sorted(zip(pp, a, bp)), "triple mismatch"
    Jb, Jbp = joints(p, b), joints(pp, bp)
    ps = [pi for pi in perms if all(Jbp[r] == Jb[pi[r]] for r in range(t))]
    assert ps == [SWAP], f"pi-set(577) != swap: {ps}"
print("SWAP FAMILY: all checks PASS (witness, rho', graph, pointwise identity, pi-set)")
