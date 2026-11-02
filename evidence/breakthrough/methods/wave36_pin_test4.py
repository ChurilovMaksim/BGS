import math, numpy as np
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

def kernel_points_np(m, q):
    Mm = mat_pow([6, q-1, 1, 0], m, q)
    a = (Mm[0]-1) % q; b = Mm[1] % q; c = Mm[2] % q; d = (Mm[3]-1) % q
    y0 = np.arange(q, dtype=np.int64)
    g = math.gcd(a, q)
    mask = (b*y0) % g == 0
    y0m = y0[mask]
    a1, q1 = a//g, q//g
    inv = pow(a1, -1, q1) if q1 > 1 else 0
    y1_0 = ((-(b*y0m)//g) * inv) % q1
    pts = []
    step = q//g
    for k in range(g):
        y1 = y1_0 + k*step
        ok = (c*y1 + d*y0m) % q == 0
        for yy0, yy1 in zip(y0m[ok].tolist(), y1[ok].tolist()):
            pts.append((yy0, yy1))
    return pts

def seq_from(y0, y1, m, q):
    y = [y0, y1]
    for i in range(2, m): y.append((6*y[-1]-y[-2]) % q)
    return tuple(y)

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

def split_reps_bruteforce(m, q):
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
    fibers = defaultdict(list)
    for p in pts: fibers[tuple(sorted(p))].append(p)
    reps = []
    for key, members in fibers.items():
        orbs = gamma_orbits(members, m)
        if len(orbs) > 1: reps.append([sorted(o)[0] for o in orbs])
    return reps

m = 60
reps625 = split_reps_bruteforce(m, 625)
reps81 = split_reps_bruteforce(m, 81)
a_fixed = reps81[0][0]; b_fixed = reps625[0][0]

def triple_blind(o, fixed, orbreps):
    ms = [tuple(sorted((fixed[i], b[i], o[i]) for i in range(m))) for b in orbreps]
    return len(set(ms)) < len(ms)

for q0 in [1681, 3481, 72361, 361201, 5202961]:
    pts = kernel_points_np(m, q0)
    nz = [p for p in pts if p != (0, 0)]
    print(f"q0={q0}: kernel pts={len(pts)}", flush=True)
    # test up to 6 nonzero kernel points (first few by y0)
    tested = 0; b625 = 0; b81 = 0
    for (y0, y1) in nz[:6]:
        o = seq_from(y0, y1, m, q0)
        if any(triple_blind(o, a_fixed, orbreps) for orbreps in reps625): b625 += 1
        if any(triple_blind(o, b_fixed, orbreps) for orbreps in reps81): b81 += 1
        tested += 1
    print(f"   tested {tested} kernel seqs: blind625={b625} blind81={b81}", flush=True)
