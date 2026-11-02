# Wave 47x task B: P-feeding exhibit. A-side twin cycles mod 49; B-side s=(1,2,4) mod 7 (T=3, g=3).
from collections import Counter
import math
modA, b, bi = 49, 39, 44
def cycleA(c1, c2, T=21):
    bp = [1]*T; bm = [1]*T
    for k in range(1, T):
        bp[k] = bp[k-1]*b % modA; bm[k] = bm[k-1]*bi % modA
    return [(c1*bp[k] + c2*bm[k]) % modA for k in range(T)]
t  = cycleA(21, 30)   # C
tp = cycleA(0, 2)     # D' mirror twin
tx = cycleA(2, 0)     # D cross twin
s = [1, 2, 4]         # mod 7, S=(0,1) split coords; distinct, negation-free, nonzero
assert len(set(s)) == 3 and all((s[i]+s[j]) % 7 != 0 for i in range(3) for j in range(3))
u = 21  # lcm(21,3)
def block0(tcyc):
    return Counter((tcyc[j % 21], s[j % 3]) for j in range(u))
B0, Bp, Bx = block0(t), block0(tp), block0(tx)
print("g = gcd(21,3) =", math.gcd(21, 3))
print("mirror twin: block0' == block0 ?", Bp == B0)
print("cross  twin: block0' == block0 ?", Bx == B0)
# P equality: block1 = -block0 on both sides, so block0 equality <=> P equality.
# non-mechanism checks for (t', s) vs (t, s)
units49 = [lam for lam in range(49) if math.gcd(lam, 7) == 1]
def dihedral_variants(tcyc):
    T = len(tcyc); out = set()
    for rr in range(T):
        out.add(tuple(tcyc[(k+rr) % T] for k in range(T)))
        out.add(tuple(tcyc[(rr-k) % T] for k in range(T)))
    return out
tvars = dihedral_variants(t)
tp_tup, tx_tup = tuple(tp), tuple(tx)
print("t' in dihedral orbit of t?", tp_tup in tvars)
print("t' = lam*dihedral(t)?", any(tuple((lam*v) % modA for v in var) == tp_tup for lam in units49 for var in tvars))
print("t_cross in dihedral orbit of t?", tx_tup in tvars)
print("t_cross = lam*dihedral(t)?", any(tuple((lam*v) % modA for v in var) == tx_tup for lam in units49 for var in tvars))
# valuation patterns (split coords): C=(21,30) pat (1,0); D'=(0,2) pat (inf,0); D=(2,0) pat (0,inf)
# => t' cannot be dihedral/scaling image of t (patterns preserved under dihedral+scaling).
# g=1 triviality demo: B-side period 5 at mod 29 (inert), u=lcm(21,5)=105; block0 must equal Cartesian product.
modC = 29
pwc = [(1, 0)]
for _ in range(10):
    x, y = pwc[-1]
    pwc.append(((17*x + 24*y) % modC, (12*x + 17*y) % modC))
def cycleC(S):
    a, bb = S; return [(2*((a*x + 2*bb*y) % modC)) % modC for (x, y) in pwc[:5]]
s5 = None
for a in range(modC):
    for bb in range(modC):
        if a == 0 and bb == 0: continue
        v = cycleC((a, bb))
        if len(set(v)) == 5:
            s5 = v; break
    if s5: break
u1 = 105
B0_1 = Counter((t[j % 21], s5[j % 5]) for j in range(u1))
cart = Counter((a_, b_) for a_ in t for b_ in s5)
print("g=1 demo (B-side mod 29, T=5): block0 == Cartesian product ?", B0_1 == cart)
