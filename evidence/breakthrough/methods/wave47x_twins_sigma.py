# Wave 47x task B: sigma dichotomy at 41^2, 17^2; mirror sigma' mod 137 at 137^2.
import math
def hensel_r(p, f):
    mod = p**f
    r0 = next(r for r in range(p) if (r*r - 2) % p == 0)
    r, m = r0, p
    while m < mod:
        for t in range(p):
            cand = r + t*m
            if (cand*cand - 2) % (m*p) == 0:
                r, m = cand, m*p; break
    return r % mod
def order_of(x, mod):
    o, y = 1, x
    while y != 1:
        y = y*x % mod; o += 1
    return o
def check(p, f, a=1):
    mod = p**f; r = hensel_r(p, f)
    b = (17 + 12*r) % mod; bi = (17 - 12*r) % mod
    T = order_of(b, mod)
    bp = [1]*T; bm = [1]*T
    for k in range(1, T):
        bp[k] = bp[k-1]*b % mod; bm[k] = bm[k-1]*bi % mod
    def cyc(c1, c2):
        return [(c1*bp[k] + c2*bm[k]) % mod for k in range(T)]
    t = cyc(p**a, 1); tp = cyc(0, 1); tx = cyc(1, 0)
    assert sorted(t) == sorted(tp) == sorted(tx), (p, f)
    idx = {v: k for k, v in enumerate(t)}
    sp = [idx[v] for v in tp]; sx = [idx[v] for v in tx]
    m = order_of(b % p, p)  # ord(b mod p) = ord(b mod p^a) for a=1
    print(f"p={p} f={f} T={T} ord(b mod p)={m}: mirror sigma'==id mod {m}? {all(sp[k] % m == k % m for k in range(T))} | cross sigma==-id mod {m}? {all((sx[k]+k) % m == 0 for k in range(T))}", flush=True)
    return sp, sx, T
check(41, 2)
check(17, 2)
# 137^2: mirror sigma' mod 137?
p, mod = 137, 137*137
r = hensel_r(p, 2)
b = (17 + 12*r) % mod; bi = (17 - 12*r) % mod
T = 2329
bp = [1]*T; bm = [1]*T
for k in range(1, T):
    bp[k] = bp[k-1]*b % mod; bm[k] = bm[k-1]*bi % mod
t = [(137*bp[k] + bm[k]) % mod for k in range(T)]
tp = [bm[k] for k in range(T)]
idx = {v: k for k, v in enumerate(t)}
sp = [idx[v] for v in tp]
print("137^2: mirror sigma'==id mod 17?", all(sp[k] % 17 == k % 17 for k in range(T)))
print("137^2: mirror sigma'==id mod 137?", all(sp[k] % 137 == k % 137 for k in range(T)))
print("137^2: mirror sigma'==id mod 2329?", sp == list(range(T)))
