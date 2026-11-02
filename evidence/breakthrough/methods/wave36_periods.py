import math
from collections import defaultdict

def mat_pow(M, e, q):
    def mul(A, B):
        return [ (A[0]*B[0]+A[1]*B[2])%q, (A[0]*B[1]+A[1]*B[3])%q,
                 (A[2]*B[0]+A[3]*B[2])%q, (A[2]*B[1]+A[3]*B[3])%q ]
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

def min_period(seq):
    m = len(seq)
    for d in range(1, m+1):
        if m % d == 0 and all(seq[i] == seq[i % d] for i in range(m)):
            return d
    return m

def gamma_orbits(members, m):
    seen = set(); orbs = []; ms = set(members)
    for p in members:
        if p in seen: continue
        orb = set()
        for k in range(m):
            orb.add(tuple(p[(i+k) % m] for i in range(m)))
            rev = tuple(p[(-i) % m] for i in range(m))
            orb.add(tuple(rev[(i+k) % m] for i in range(m)))
        orb &= ms; seen |= orb; orbs.append(orb)
    return orbs

m = 60
# split fiber reps at 81, 625
for q in [81, 625]:
    pts = kernel_points(m, q)
    fibers = defaultdict(list)
    for p in pts: fibers[tuple(sorted(p))].append(p)
    for key, members in fibers.items():
        orbs = gamma_orbits(members, m)
        if len(orbs) > 1:
            rep = sorted(orbs[0])[0]
            print(f"q={q} split rep: period={min_period(rep)} distinct={len(set(rep))}")
# base kernel seq (first nonzero) periods at other odd components
for q in [49, 121, 361, 841]:
    pts = kernel_points(m, q)
    nz = [p for p in pts if any(v != 0 for v in p)]
    periods = sorted(set(min_period(p) for p in nz))
    print(f"q={q}: kernel={len(pts)} nonzero periods present={periods} (first nz period={min_period(nz[0])})")
