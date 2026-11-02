# Wave 47x task B: REAL P-collision instance via mirror twin at 137^2, B-side at 137, u=2329, g=17.
from collections import Counter
import math
p = 137; mod = p*p  # 18769
# hensel r mod 18769 with r^2 == 2
r = next(r for r in range(p) if (r*r - 2) % p == 0)
m = p
while m < mod:
    for t in range(p):
        cand = r + t*m
        if (cand*cand - 2) % (m*p) == 0:
            r, m = cand, m*p; break
r %= mod
assert (r*r - 2) % mod == 0
b = (17 + 12*r) % mod; bi = (17 - 12*r) % mod
assert (b*bi) % mod == 1
def order_of(x, md):
    o, y = 1, x
    while y != 1:
        y = y*x % md; o += 1
    return o
T = order_of(b, mod)
print("ord(beta) mod 137^2 =", T, "= 17*137?", T == 17*137)
# alpha admissibility: ord(alpha) and alpha^2329 == -1 ?
a1 = (3 + 2*r) % mod; a2 = (3 - 2*r) % mod
oa = order_of(a1, mod)
print("ord(alpha) mod 137^2 =", oa, "alpha^2329 == (-1,-1)?", pow(a1, 2329, mod) == mod-1 and pow(a2, 2329, mod) == mod-1)
# twin cycles: C=(137,1) pattern (1,0); D'=(0,1) mirror; D=(1,0) cross
bp = [1]*T; bm = [1]*T
for k in range(1, T):
    bp[k] = bp[k-1]*b % mod; bm[k] = bm[k-1]*bi % mod
def cyc(c1, c2):
    return [(c1*bp[k] + c2*bm[k]) % mod for k in range(T)]
t = cyc(137, 1); tp = cyc(0, 1); tx = cyc(1, 0)
print("periods all T?", len(t) == T, "distinct t:", len(set(t)) == T)
print("M(C)==M(D'):", sorted(t) == sorted(tp), " M(C)==M(D):", sorted(t) == sorted(tx))
# sigma profiles
idx = {v: k for k, v in enumerate(t)}
sp = [idx[v] for v in tp]; sx = [idx[v] for v in tx]
print("mirror sigma'(k)==k mod 17 for all k?", all(sp[k] % 17 == k % 17 for k in range(T)))
print("mirror sigma' == id mod 2329 (i.e. sigma'=id)?", sp == list(range(T)))
print("cross sigma(k)==-k mod 17 for all k?", all((sx[k] + k) % 17 == 0 for k in range(T)))
print("cross sigma(k)==k mod 17?", all(sx[k] % 17 == k % 17 for k in range(T)))
# B-side at 137: b0 = beta mod 137 first comp; find S=(s1,s2) with 17 distinct negation-free values
b0 = b % p; bi0 = pow(b0, -1, p)
bp0 = [1]*17; bm0 = [1]*17
for k in range(1, 17):
    bp0[k] = bp0[k-1]*b0 % p; bm0[k] = bm0[k-1]*bi0 % p
print("ord(beta) mod 137 =", order_of(b0, p))
Sfound = None
for s1 in range(p):
    for s2 in range(p):
        if s1 % p == 0 and s2 % p == 0: continue
        sv = [(s1*bp0[k] + s2*bm0[k]) % p for k in range(17)]
        if len(set(sv)) != 17: continue
        if any((sv[i] + sv[j]) % p == 0 for i in range(17) for j in range(17)): continue
        Sfound = (s1, s2); s = sv; break
    if Sfound: break
print("B-side S =", Sfound, "s distinct+negfree:", Sfound is not None)
# P test: u = 2329 = lcm(2329, 17); block0 over j in Z/2329
u = 2329
B0 = Counter((t[j], s[j % 17]) for j in range(u))
Bp = Counter((tp[j], s[j % 17]) for j in range(u))
Bx = Counter((tx[j], s[j % 17]) for j in range(u))
print("g = gcd(2329,17) =", math.gcd(2329, 17))
print("mirror twin: block0' == block0 ?", Bp == B0, " => P(t',s)==P(t,s)?", Bp == B0)
print("cross  twin: block0' == block0 ?", Bx == B0)
