"""Wave 14, task 1: G1 at f=3 — numerical groundwork.

Part A: for odd primes p, compute L0 = order of alpha = 3+2*sqrt(2) mod p
in R/p, and k = v_p(alpha^L0 - 1) (valuation in R: min of coefficient
valuations). Cases at f=3 are (k,s) with s = 3-k: (3,0), (2,1), (1,2).
k>=2 is the Wieferich-type condition; s=0 at f=2 (k=2) is the case whose
rigidity proof in wave 13 has a possible real-case gap, tested in Part B.

Part B: for each k=2 prime with 4|L0, L0>=12, test the explicit pair
A = (1,0), A' = A*(1 + p*sqrt(2)) = (1,p) mod p^2, m = L0, t = 4:
same global multiset? per-class tuples D_4-related?
Also brute-force all A in R/p^2 for small p.

Part C: exhaustive G1' check at f=3, (m,p) = (36,3), modulus 27.
"""
import sys
from math import gcd

def mul(x, y, n):
    a, b = x; c, d = y
    return ((a*c + 2*b*d) % n, (a*d + b*c) % n)

def pw(x, e, n):
    r = (1, 0)
    while e:
        if e & 1: r = mul(r, x, n)
        x = mul(x, x, n); e >>= 1
    return r

def primes_upto(N):
    sieve = bytearray(b'\x01') * (N+1)
    sieve[0:2] = b'\x00\x00'
    for i in range(2, int(N**0.5)+1):
        if sieve[i]:
            sieve[i*i:N+1:i] = b'\x00' * ((N - i*i)//i + 1)
    return [i for i in range(N+1) if sieve[i]]

def vp_int(v, p):
    c = 0
    while v % p == 0 and v != 0:
        v //= p; c += 1
    return c

def order_and_k(p):
    # order of alpha mod p
    x = (3 % p, 2 % p)
    cur = x; L0 = 1
    while cur != (1, 0):
        cur = mul(cur, x, p); L0 += 1
        if L0 > 2*p + 2: raise RuntimeError(f"order not found p={p}")
    # alpha^L0 mod p^4
    a4 = pw((3, 2), L0, p**4)
    k = min(vp_int(a4[0]-1, p) if a4[0] != 1 else 99,
            vp_int(a4[1], p) if a4[1] != 0 else 99)
    return L0, k

def d_orbit(t, tup):
    # D_t orbit of a tuple of class multisets (t classes), dihedral action
    # r -> r+b and r -> -r+b
    out = set()
    for b in range(t):
        out.add(tuple(tup[(i+b) % t] for i in range(t)))
        out.add(tuple(tup[(-i+b) % t] for i in range(t)))
    return out

def check_pair(p, m, t, A, Ap):
    """Return (global_equal, perclass_D_related, detail). Sequences mod p^2."""
    n = p*p
    alpha = (3, 2)
    def seq(Av):
        vals = []
        cur = (1, 0)
        for i in range(m):
            vals.append((2 * ((Av[0]*cur[0] + 2*Av[1]*cur[1]) % n)) % n)
            cur = mul(cur, alpha, n)
        return vals
    def classes(vals):
        return tuple(tuple(sorted(vals[i] for i in range(m) if i % t == r))
                     for r in range(t))
    v, vp = seq(A), seq(Ap)
    geq = sorted(v) == sorted(vp)
    cp, cpp = classes(v), classes(vp)
    rel = cpp in d_orbit(t, cp)
    return geq, rel, (cp, cpp)

def main():
    print("=== Part A: L0 and k for odd primes <= 1000 ===")
    k2, k3 = [], []
    for p in primes_upto(1000):
        if p == 2: continue
        L0, k = order_and_k(p)
        if k >= 3: k3.append((p, L0, k))
        elif k == 2: k2.append((p, L0, k))
    print("k>=3 primes:", k3)
    print("k=2 primes:", k2)
    print()
    print("=== Part B: f=2 s=0 test, A=(1,0) vs A'=(1,p), m=L0, t=4 ===")
    for (p, L0, k) in k2:
        if L0 % 4 != 0 or L0 < 12:
            print(f"p={p} L0={L0}: skipped (4|L0 and L0>=12 fail)")
            continue
        geq, rel, (cp, cpp) = check_pair(p, L0, 4, (1, 0), (1, p))
        print(f"p={p} L0={L0}: global_equal={geq} D4_related={rel}")
        if geq and not rel:
            print("  *** COUNTEREXAMPLE to G1' at f=2, s=0 ***")
            for r in range(4):
                print(f"  class {r}: A={cp[r]}  A'={cpp[r]}")
    print()
    print("=== Part B2: brute force f=2 s=0 for small k=2 primes ===")
    for (p, L0, k) in k2:
        if p > 13 or L0 % 4 != 0: continue
        n = p*p; m = L0; t = 4
        alpha = (3, 2)
        # precompute alpha powers mod n
        pwrs = [(1, 0)]
        for i in range(1, m): pwrs.append(mul(pwrs[-1], alpha, n))
        groups = {}
        for a in range(n):
            for b in range(n):
                vals = tuple((2*((a*pwrs[i][0] + 2*b*pwrs[i][1]) % n)) % n
                             for i in range(m))
                g = tuple(sorted(vals))
                cl = tuple(tuple(sorted(vals[i] for i in range(m) if i % t == r))
                           for r in range(t))
                groups.setdefault(g, []).append(cl)
        bad = 0; tot = 0
        for g, cls in groups.items():
            tot += 1
            orb = d_orbit(t, cls[0])
            if any(c not in orb for c in cls): bad += 1
        print(f"p={p} L0={L0}: groups={tot} bad_groups={bad}")
    print()
    print("=== Part C: exhaustive G1' at f=3, (m,p)=(36,3), mod 27 ===")
    p, m, t, n = 3, 36, 4, 27
    alpha = (3, 2)
    pwrs = [(1, 0)]
    for i in range(1, m): pwrs.append(mul(pwrs[-1], alpha, n))
    groups = {}
    for a in range(n):
        for b in range(n):
            vals = tuple((2*((a*pwrs[i][0] + 2*b*pwrs[i][1]) % n)) % n
                         for i in range(m))
            g = tuple(sorted(vals))
            cl = tuple(tuple(sorted(vals[i] for i in range(m) if i % t == r))
                       for r in range(t))
            groups.setdefault(g, []).append(cl)
    bad = 0
    for g, cls in groups.items():
        orb = d_orbit(t, cls[0])
        if any(c not in orb for c in cls): bad += 1
    print(f"(36,3) mod 27: sequences=729 groups={len(groups)} bad_groups={bad}")

if __name__ == "__main__":
    main()
