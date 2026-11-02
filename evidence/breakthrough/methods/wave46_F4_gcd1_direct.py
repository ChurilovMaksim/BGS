# Direct mod-p^2 verification: enumerate kernel_points(m, p^2) exactly as wave38,
# group by sorted multiset, canonical dihedral form via minimal-period base cycle.
import math, sys
from collections import defaultdict

def mat_pow(M, e, q):
    def mul(A, B):
        return [(A[0]*B[0]+A[1]*B[2])%q, (A[0]*B[1]+A[1]*B[3])%q,
                (A[2]*B[0]+A[3]*B[2])%q, (A[2]*B[1]+A[3]*B[3])%q]
    R = [1,0,0,1]; B = M[:]
    while e:
        if e & 1: R = mul(R, B)
        B = mul(B, B); e >>= 1
    return R

def kernel_points(m, q):
    Mm = mat_pow([6, q-1, 1, 0], m, q)
    a = (Mm[0]-1) % q; b = Mm[1] % q; c = Mm[2] % q; d = (Mm[3]-1) % q
    pts = []
    for y0 in range(q):
        g = math.gcd(a, q)
        if (b*y0) % g != 0: continue
        a1, q1 = a//g, q//g
        rhs = (-(b*y0)//g) % q1
        y1_0 = (pow(a1, -1, q1) * rhs) % q1 if q1 > 1 else 0
        step = q//g; y1 = y1_0
        while y1 < q:
            if (c*y1 + d*y0) % q == 0:
                y = [y0, y1]
                for i in range(2, m): y.append((6*y[-1]-y[-2]) % q)
                pts.append(tuple(y))
            y1 += step
    return pts

def min_period(s):
    # KMP prefix function on the closed sequence; period must divide len(s)
    n = len(s); pi = [0]*n; k = 0
    for i in range(1, n):
        while k and s[i] != s[k]: k = pi[k-1]
        if s[i] == s[k]: k += 1
        pi[i] = k
    d = n - pi[-1]
    assert n % d == 0, (n, d)
    return d

def canon_cycle(t):
    d = len(t)
    rots = [tuple(t[(i+k) % d] for i in range(d)) for k in range(d)]
    rev = (t[0],) + tuple(t[d-1-i] for i in range(d-1))
    rrots = [tuple(rev[(i+k) % d] for i in range(d)) for k in range(d)]
    return min(rots + rrots)

def check(m, p):
    q = p*p
    pts = kernel_points(m, q)
    div = all(v % p == 0 for s in pts for v in s)
    periods = defaultdict(int)
    fibers = defaultdict(set)
    for s in pts:
        d = min_period(s); periods[d] += 1
        fibers[tuple(sorted(s))].add(canon_cycle(s[:d]))
    split = {k: v for k, v in fibers.items() if len(v) > 1}
    print(f"m={m} q={q}: kernel points={len(pts)} (expect {q}), all divisible by {p}: {div}, "
          f"periods={dict(periods)}, fibers={len(fibers)}, split fibers={len(split)}", flush=True)
    if split:
        k, v = next(iter(split.items()))
        print(f"  FIRST SPLIT multiset head={k[:8]}... n_orbits={len(v)}", flush=True)

if __name__ == "__main__":
    m, p = int(sys.argv[1]), int(sys.argv[2])
    check(m, p)
