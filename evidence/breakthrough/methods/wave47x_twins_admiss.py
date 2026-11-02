# Wave 47x task B: admissibility (ord alpha, alpha^u == -1 solvable?) + classification prediction samples.
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
def vp(v, p, f):
    if v == 0: return f
    c = 0
    while v % p == 0: v //= p; c += 1
    return c
print("=== admissibility: ord(alpha) mod p^f, alpha^u==-1 solvable? ===")
for (p, f) in [(7,2),(7,3),(17,2),(23,2),(31,2),(41,2),(47,2)]:
    mod = p**f; r = hensel_r(p, f)
    a1 = (3 + 2*r) % mod; a2 = (3 - 2*r) % mod
    o1, o2 = order_of(a1, mod), order_of(a2, mod)
    o = o1*o2//math.gcd(o1, o2)
    solv = (o % 2 == 0) and (pow(a1, o//2, mod) == mod-1) and (pow(a2, o//2, mod) == mod-1)
    b = (17 + 12*r) % mod; T = order_of(b, mod)
    print(f"p={p} f={f} mod={mod} ord(alpha)={o} (comps {o1},{o2}) alpha^u==-1? {solv}  ord(beta)=T v_p(T)={vp(T,p,f) if T%p==0 else 0}")
print()
print("=== classification prediction samples: C=(p^a*x, y) vs D=(0,d) and D=(d,0), d==y mod p^a ===")
def cycle_vals(c1, c2, b, bi, T, mod):
    bp = [1]*T; bm = [1]*T
    for k in range(1, T):
        bp[k] = bp[k-1]*b % mod; bm[k] = bm[k-1]*bi % mod
    return [(c1*bp[k] + c2*bm[k]) % mod for k in range(T)]
for (p, f) in [(31,2),(41,2),(47,2),(7,3)]:
    mod = p**f; r = hensel_r(p, f)
    b = (17 + 12*r) % mod; bi = (17 - 12*r) % mod
    T = order_of(b, mod)
    vT = 0; t = T
    while t % p == 0: t //= p; vT += 1
    for a in range(1, f):
        cond = (vT + a >= f)
        # sample: y = 1+ p^a (unit, ==1 mod p^a... use y=1), x = p^a, d = y (== y mod p^a), plus d = y + p^a
        ok_mirror = ok_cross = None
        for (y, x) in [(1, p**a), (2, 3*p**a)]:
            MC = sorted(cycle_vals(p**a*x % mod if False else (p**a*x) % mod, y, b, bi, T, mod))
            # note: C=(p^a*x, y): first comp p^a*x has valuation >= a
            for d in (y, (y + p**a) % mod):
                MDm = sorted(cycle_vals(0, d, b, bi, T, mod))   # D'=(0,d) mirror
                MDc = sorted(cycle_vals(d, 0, b, bi, T, mod))   # D=(d,0) cross
                ok_mirror = (MC == MDm); ok_cross = (MC == MDc)
                print(f"p={p} f={f} a={a} cond(v_p(T)+a>=f)={cond} y={y} d={d}: mirror M==M? {ok_mirror} cross M==M? {ok_cross}", flush=True)
        # negative sample: d NOT == y mod p^a should differ (unless d/y in <b>)
        y, x = 1, p**a
        MC = sorted(cycle_vals((p**a*x) % mod, y, b, bi, T, mod))
        d_bad = (y + 1) % mod
        print(f"p={p} f={f} a={a} NEG d={d_bad} (not == y mod p^a): mirror? {sorted(cycle_vals(0, d_bad, b, bi, T, mod)) == MC} cross? {sorted(cycle_vals(d_bad, 0, b, bi, T, mod)) == MC}", flush=True)
