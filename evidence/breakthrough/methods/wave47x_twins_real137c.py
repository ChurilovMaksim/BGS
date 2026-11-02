from collections import Counter
import math
p, mod = 137, 137*137
r = next(r for r in range(p) if (r*r - 2) % p == 0)
m = p
while m < mod:
    for t_ in range(p):
        cand = r + t_*m
        if (cand*cand - 2) % (m*p) == 0:
            r, m = cand, m*p; break
r %= mod
b = (17 + 12*r) % mod; bi = (17 - 12*r) % mod
T = 2329
bp = [1]*T; bm = [1]*T
for k in range(1, T):
    bp[k] = bp[k-1]*b % mod; bm[k] = bm[k-1]*bi % mod
t = [(137*bp[k] + bm[k]) % mod for k in range(T)]
tp = [bm[k] for k in range(T)]
# unit B-side S=(1,2) at 137
b0 = b % p; bi0 = pow(b0, -1, p)
bp0 = [1]*17; bm0 = [1]*17
for k in range(1, 17):
    bp0[k] = bp0[k-1]*b0 % p; bm0[k] = bm0[k-1]*bi0 % p
s = [(1*bp0[k] + 2*bm0[k]) % p for k in range(17)]
print("s distinct?", len(set(s)) == 17, "negfree?", all((s[i]+s[j]) % p != 0 for i in range(17) for j in range(17)))
B0 = Counter((t[j], s[j % 17]) for j in range(T))
Bp = Counter((tp[j], s[j % 17]) for j in range(T))
print("unit B-side S=(1,2): block0' == block0 ?", Bp == B0)
# t' not reversal of t? reversal = cycle of Cbar=(1,137)
trev = [(1*bp[k] + 137*bm[k]) % mod for k in range(T)]
print("t' == reversal of t?", tp == trev, "| t' == t?", tp == t)
