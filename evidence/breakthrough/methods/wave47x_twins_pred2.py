# Wave 47x task B: CORRECTED classification prediction samples.
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
        else: raise RuntimeError("lift fail")
    return r % mod
def order_of(x, mod):
    o, y = 1, x
    while y != 1:
        y = y*x % mod; o += 1
    return o
def cyc(c1, c2, b, bi, T, mod):
    bp = [1]*T; bm = [1]*T
    for k in range(1, T):
        bp[k] = bp[k-1]*b % mod; bm[k] = bm[k-1]*bi % mod
    return sorted((c1*bp[k] + c2*bm[k]) % mod for k in range(T))
for (p, f) in [(31,2),(41,2),(47,2),(17,2),(7,3)]:
    mod = p**f; r = hensel_r(p, f)
    b = (17 + 12*r) % mod; bi = (17 - 12*r) % mod
    T = order_of(b, mod)
    vT = 0; t = T
    while t % p == 0: t //= p; vT += 1
    for a in range(1, f):
        cond = (vT + a >= f)
        for (y, x) in [(1, 1), (2, 3)]:   # x UNIT (corrected)
            MC = cyc((p**a * x) % mod, y, b, bi, T, mod)
            for d in [y, (y + p**a) % mod]:
                Mm = cyc(0, d, b, bi, T, mod); Mc = cyc(d, 0, b, bi, T, mod)
                print(f"p={p} f={f} a={a} cond={cond} C=({p**a}*{x},{y}) d={d}: mirror {MC==Mm} cross {MC==Mc}", flush=True)
        # NEG: d with d/y not in <b> (checked via (d/y)^T != 1)
        y, x = 1, 1
        MC = cyc((p**a * x) % mod, y, b, bi, T, mod)
        for d in [y+1, y+2]:
            inb = pow(d * pow(y, -1, mod) % mod, T, mod) == 1
            Mm = cyc(0, d, b, bi, T, mod); Mc = cyc(d, 0, b, bi, T, mod)
            print(f"p={p} f={f} a={a} NEG d={d} d/y in <b>? {inb}: mirror {MC==Mm} cross {MC==Mc}", flush=True)
