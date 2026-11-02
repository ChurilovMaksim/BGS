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

def split_fiber_orbit_reps(m, q):
    pts = kernel_points(m, q)
    fibers = defaultdict(list)
    for p in pts: fibers[tuple(sorted(p))].append(p)
    reps = []
    for key, members in fibers.items():
        orbs = gamma_orbits(members, m)
        if len(orbs) > 1: reps.append([sorted(o)[0] for o in orbs])
    return reps

m = 60
reps625 = split_fiber_orbit_reps(m, 625)
reps81 = split_fiber_orbit_reps(m, 81)
a_fixed = reps81[0][0]          # one locked 81-orbit representative
b_fixed = reps625[0][0]         # one 625-orbit representative
print("a_fixed orbit size check, b_fixed set")

for q0 in [49, 121, 361, 841]:
    pts0 = kernel_points(m, q0)
    blind625 = 0; blind81 = 0; total = 0
    for o in pts0:
        if all(v == 0 for v in o): continue
        total += 1
        # vary b over 625-orbits, a fixed: triple (a_i, b_i, o_i)
        for orbreps in reps625:
            ms = [tuple(sorted((a_fixed[i], b[i], o[i]) for i in range(m))) for b in orbreps]
            if len(set(ms)) < len(ms): blind625 += 1; break
        # vary a over 81-orbits, b fixed: triple (a_i, b_i, o_i)
        for orbreps in reps81:
            ms = [tuple(sorted((a[i], b_fixed[i], o[i]) for i in range(m))) for a in orbreps]
            if len(set(ms)) < len(ms): blind81 += 1; break
    print(f"q0={q0}: nonzero={total} triple-blind-for-625={blind625} triple-blind-for-81={blind81}")
