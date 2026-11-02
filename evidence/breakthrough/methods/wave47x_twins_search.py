# Wave 47x task B: twin search, split primes (f=1,2; 7 also f=3) + inert controls.
import math
from collections import defaultdict

def hensel_r(p, f):
    mod = p**f
    r0 = next(r for r in range(p) if (r*r - 2) % p == 0)
    r, m = r0, p
    while m < mod:
        # lift r mod m to mod m*p: try r + t*m
        for t in range(p):
            cand = r + t*m
            if (cand*cand - 2) % (m*p) == 0:
                r, m = cand, m*p; break
        else:
            raise RuntimeError("lift fail")
    return r % mod

def order_of(x, mod):
    o, y = 1, x
    while y != 1:
        y = y*x % mod; o += 1
        if o > mod: raise RuntimeError("order loop")
    return o

def vp(v, p, f):
    if v == 0: return f
    c = 0
    while v % p == 0:
        v //= p; c += 1
    return c

def scaling_match(X, o, mod, p, f):
    x1, x2 = X; o1, o2 = o
    v1, v2 = vp(o1, p, f), vp(o2, p, f)
    w1, w2 = vp(x1, p, f), vp(x2, p, f)
    if v1 >= f and v2 >= f: return w1 >= f and w2 >= f
    if v1 >= f:
        if w1 < f or v2 >= f: return w2 >= f
        return w2 == v2
    if v2 >= f:
        if w2 < f: return False
        return w1 == v1
    if w1 != v1 or w2 != v2: return False
    m1 = mod // (p**v1); m2 = mod // (p**v2)
    lam1 = ((x1 // (p**v1)) * pow(o1 // (p**v1), -1, m1)) % m1
    lam2 = ((x2 // (p**v2)) * pow(o2 // (p**v2), -1, m2)) % m2
    return lam1 % min(m1, m2) == lam2 % min(m1, m2)

def divisors(n):
    ds = [d for d in range(1, n+1) if n % d == 0]
    return ds

def search_split(p, f, nonunits_only=True):
    mod = p**f
    r = hensel_r(p, f)
    b = (17 + 12*r) % mod; bi = (17 - 12*r) % mod
    assert (b*bi) % mod == 1
    T = order_of(b, mod)
    bp = [1]*T; bm = [1]*T
    for k in range(1, T):
        bp[k] = bp[k-1]*b % mod; bm[k] = bm[k-1]*bi % mod
    divs = divisors(T)
    groups = defaultdict(list)
    rng = range(mod)
    for c1 in rng:
        for c2 in rng:
            if nonunits_only and (c1 % p != 0 and c2 % p != 0):
                continue
            t = [(c1*bp[k] + c2*bm[k]) % mod for k in range(T)]
            per = T
            for d in divs:
                if all(t[k] == t[k % d] for k in range(T)):
                    per = d; break
            groups[(per, tuple(sorted(t[:per])))].append((c1, c2))
    twins = []
    for (per, M), els in groups.items():
        if len(els) <= 1: continue
        rep = els[0]
        orbit = set()
        for rr in range(T):
            orbit.add((rep[0]*bp[rr] % mod, rep[1]*bm[rr] % mod))
            orbit.add((rep[1]*bp[rr] % mod, rep[0]*bm[rr] % mod))
        bad = [e for e in els if not any(scaling_match(e, o, mod, p, f) for o in orbit)]
        if bad:
            pats = sorted(set((vp(e[0], p, f), vp(e[1], p, f)) for e in els))
            twins.append(dict(per=per, size=len(els), pats=pats, bad=bad[:6], rep=rep, M=M))
    return dict(p=p, f=f, mod=mod, T=T, ngroups=len(groups), twins=twins)

def search_inert(p, f):
    # R/p^f with coords (a,b): element a+b*sqrt2; beta=(17,12); trace=2a.
    mod = p**f
    # beta powers as (x,y)
    bp = [(1, 0)]
    for k in range(1, mod*2):
        x, y = bp[-1]
        bp.append(((17*x + 24*y) % mod, (12*x + 17*y) % mod))
        if bp[-1] == (1, 0): break
    T = len(bp) - 1
    divs = divisors(T)
    groups = defaultdict(list)
    for a in range(mod):
        for bb in range(mod):
            if a % p != 0 or bb % p != 0: continue  # non-units only (both coords 0 mod p)
            if a == 0 and bb == 0: continue
            t = [(2*((a*bp[k][0] + 2*bb*bp[k][1]) % mod)) % mod for k in range(T)]
            per = T
            for d in divs:
                if all(t[k] == t[k % d] for k in range(T)):
                    per = d; break
            groups[(per, tuple(sorted(t[:per])))].append((a, bb))
    twins = []
    for (per, M), els in groups.items():
        if len(els) <= 1: continue
        rep = els[0]
        # dihedral orbit: beta^r * rep and beta^r * conj(rep); conj(a,b) = (a,-b)
        orbit = set()
        for rr in range(T):
            x, y = bp[rr]
            # rep * beta^rr: (a,b)*(x,y) = (a*x+2*b*y, a*y+b*x)
            orbit.add(((rep[0]*x + 2*rep[1]*y) % mod, (rep[0]*y + rep[1]*x) % mod))
            # conj(rep) = (a,-b)
            orbit.add(((rep[0]*x - 2*rep[1]*y) % mod, (rep[0]*y - rep[1]*x) % mod))
        bad = [e for e in els if not any(scaling_match(e, o, mod, p, f) for o in orbit)]
        if bad:
            twins.append(dict(per=per, size=len(els), bad=bad[:6], rep=rep))
    return dict(p=p, f=f, mod=mod, T=T, ngroups=len(groups), twins=twins)

if __name__ == "__main__":
    import sys
    for (p, f) in [(7,1),(17,1),(23,1),(31,1),(41,1),(47,1)]:
        res = search_split(p, f, nonunits_only=False)
        print(f"split p={p} f={f} mod={res['mod']} T={res['T']} groups={res['ngroups']} twin_groups={len(res['twins'])}", flush=True)
        for tw in res['twins'][:5]:
            print("   per", tw['per'], "size", tw['size'], "pats", tw['pats'], "bad", tw['bad'], flush=True)
