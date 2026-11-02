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

def kernel_line(m, q):
    """Return (param, gen) where sequences are t*gen pattern: gen is (y0,y1) for t=1 if parametrized by y0,
    or None if fallback needed. Returns function seq(t)."""
    Mm = mat_pow([6, q-1, 1, 0], m, q)
    a = (Mm[0]-1) % q; b = Mm[1] % q; c = Mm[2] % q; d = (Mm[3]-1) % q
    if math.gcd(a, q) == 1:
        ainv = pow(a, -1, q); r = (-b * ainv) % q  # y1 = r*y0
        def seq(t):
            y0 = t % q; y1 = (r * y0) % q
            y = [y0, y1]
            for i in range(2, m): y.append((6*y[-1]-y[-2]) % q)
            return tuple(y)
        # validate second equation for a few t
        for t in [1, 2, 7, 12345 % q]:
            y = seq(t)
            assert (c*y[1] + d*y[0]) % q == 0, f"second eq fails q={q} t={t}"
        return seq
    if math.gcd(b, q) == 1:
        binv = pow(b, -1, q); r = (-a * binv) % q  # y0 = r*y1
        def seq(t):
            y1 = t % q; y0 = (r * y1) % q
            y = [y0, y1]
            for i in range(2, m): y.append((6*y[-1]-y[-2]) % q)
            return tuple(y)
        for t in [1, 2, 7]:
            y = seq(t)
            assert (c*y[1] + d*y[0]) % q == 0
        return seq
    return None

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
    # reuse earlier brute kernel for q<=841
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
    # fixed = sequence at locked component; orbreps = orbits of free component
    ms = [tuple(sorted((fixed[i], b[i], o[i]) for i in range(m))) for b in orbreps]
    return len(set(ms)) < len(ms)

for q0, p in [(1681, 41), (3481, 59), (72361, 269), (361201, 601), (5202961, 2281)]:
    seq = kernel_line(m, q0)
    if seq is None:
        print(f"q0={q0}: kernel line FAILED (no unit row)"); continue
    res = {}
    for t in [1, p]:
        o = seq(t)
        if all(v == 0 for v in o):
            res[t] = "zero"; continue
        b625 = any(triple_blind(o, a_fixed, orbreps) for orbreps in reps625)
        b81 = any(triple_blind(o, b_fixed, orbreps) for orbreps in reps81)
        res[t] = f"blind625={b625} blind81={b81}"
    print(f"q0={q0}: {res}")
