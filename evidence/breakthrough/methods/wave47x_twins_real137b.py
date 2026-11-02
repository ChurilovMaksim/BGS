# unit B-side at 137? + negation-freeness of t, t' at 137^2
import math
p, mod = 137, 137*137
r = next(r for r in range(p) if (r*r - 2) % p == 0)
# b0 mod 137
b0 = (17 + 12*r) % p; bi0 = pow(b0, -1, p)
bp0 = [1]*17; bm0 = [1]*17
for k in range(1, 17):
    bp0[k] = bp0[k-1]*b0 % p; bm0[k] = bm0[k-1]*bi0 % p
found = None
for s1 in range(p):
    for s2 in range(p):
        if s1 == 0 or s2 == 0: continue  # unit in split coords = both nonzero
        sv = [(s1*bp0[k] + s2*bm0[k]) % p for k in range(17)]
        if len(set(sv)) != 17: continue
        if any((sv[i] + sv[j]) % p == 0 for i in range(17) for j in range(17)): continue
        found = (s1, s2); break
    if found: break
print("unit B-side S at 137:", found)
# negation-freeness of t, t' at 137^2 (values = <b>, odd order => -1 not in <b>)
r2 = r
m = p
while m < mod:
    for t_ in range(p):
        cand = r2 + t_*m
        if (cand*cand - 2) % (m*p) == 0:
            r2, m = cand, m*p; break
r2 %= mod
b = (17 + 12*r2) % mod; bi = (17 - 12*r2) % mod
T = 2329
bp = [1]*T; bm = [1]*T
for k in range(1, T):
    bp[k] = bp[k-1]*b % mod; bm[k] = bm[k-1]*bi % mod
t = [(137*bp[k] + bm[k]) % mod for k in range(T)]
tp = [bm[k] for k in range(T)]
S = set(t)
print("t negation-free?", all((-v) % mod not in S for v in t))
print("t' values == t values as sets?", set(tp) == S)
