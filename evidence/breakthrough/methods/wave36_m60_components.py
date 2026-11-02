import math
from collections import defaultdict

def mat_pow(M, e, q):
    # 2x2 matrix [[a,b],[c,d]] times vector convention: state (y_{i+1}, y_i) = M (y_i, y_{i-1}), M=[[6,-1],[1,0]]
    def mul(A, B):
        return [ (A[0]*B[0]+A[1]*B[2])%q, (A[0]*B[1]+A[1]*B[3])%q,
                 (A[2]*B[0]+A[3]*B[2])%q, (A[2]*B[1]+A[3]*B[3])%q ]
    R = [1,0,0,1]; B = M[:]
    while e:
        if e & 1: R = mul(R, B)
        B = mul(B, B); e >>= 1
    return R

def kernel_points(m, q):
    # (y_{m+1}, y_m) = M^m (y_1, y_0); need == (y_1, y_0). Solve (M^m - I) v = 0 by brute force over y0, linear congruence for y1.
    Mm = mat_pow([6, q-1, 1, 0], m, q)
    a = (Mm[0]-1) % q; b = Mm[1] % q; c = Mm[2] % q; d = (Mm[3]-1) % q
    pts = []
    for y0 in range(q):
        # a*y1 + b*y0 == 0 (mod q); c*y1 + d*y0 == 0
        # solve first: g = gcd(a,q); need g | b*y0
        g = math.gcd(a, q)
        if (b*y0) % g != 0: continue
        # solutions y1 = y1_0 + k*(q/g)
        a1, q1 = a//g, q//g
        rhs = (-(b*y0)//g) % q1
        y1_0 = (pow(a1, -1, q1) * rhs) % q1 if q1 > 1 else 0
        step = q//g
        y1 = y1_0
        while y1 < q:
            if (c*y1 + d*y0) % q == 0:
                # build sequence
                y = [y0, y1]
                for i in range(2, m):
                    y.append((6*y[-1]-y[-2]) % q)
                if y[m % m] == y0:  # placeholder, periodicity checked via matrix already
                    pass
                pts.append(tuple(y))
            y1 += step
    return pts

def gamma_orbits(members, m):
    seen = set(); orbs = []
    ms = set(members)
    for p in members:
        if p in seen: continue
        orb = set()
        for k in range(m):
            orb.add(tuple(p[(i+k) % m] for i in range(m)))
            rev = tuple(p[(-i) % m] for i in range(m))
            orb.add(tuple(rev[(i+k) % m] for i in range(m)))
        orb &= ms; seen |= orb; orbs.append(orb)
    return orbs

for m, q in [(60, 81), (60, 625), (60, 128)]:
    pts = kernel_points(m, q)
    fibers = defaultdict(list)
    for p in pts: fibers[tuple(sorted(p))].append(p)
    splits = []
    for key, members in fibers.items():
        orbs = gamma_orbits(members, m)
        if len(orbs) > 1: splits.append((len(members), len(orbs), [len(o) for o in orbs]))
    print(f"m={m} q={q}: kernel={len(pts)} fibers={len(fibers)} splits={splits}")
    if q == 625 and splits:
        # distinct values in a split-fiber representative
        for key, members in fibers.items():
            orbs = gamma_orbits(members, m)
            if len(orbs) > 1:
                rep = members[0]
                print("  625 split rep distinct values:", len(set(rep)), "value counts sample:", sorted(set(rep))[:10])
                break
