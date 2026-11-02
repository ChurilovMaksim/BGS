import math
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

def split_fibers(m, q):
    pts = kernel_points(m, q)
    fibers = defaultdict(list)
    for p in pts: fibers[tuple(sorted(p))].append(p)
    out = []
    for key, members in fibers.items():
        orbs = gamma_orbits(members, m)
        if len(orbs) > 1: out.append((key, [sorted(o)[0] for o in orbs]))
    return out

def period(seq):
    m = len(seq)
    for d in range(1, m+1):
        if m % d == 0 and all(seq[i] == seq[i % d] for i in range(m)):
            return d
    return m

def recover_C(seq, q):
    # seq_i = Tr(C alpha^i), alpha = 3+2sqrt2, C = x + y sqrt2 (q odd)
    # y0 = 2x, y1 = 2(3x+4y)  (mod q)
    inv2 = pow(2, -1, q); inv4 = pow(4, -1, q)
    x = (seq[0]*inv2) % q
    y = ((seq[1]*inv2 - 3*x)*inv4) % q
    return (x, y)

def check_C(seq, C, q):
    x, y = C
    # Tr((x+y s)(3+2s)^i): use recurrence values
    vals = [seq[0], seq[1]]
    # verify first two by construction; verify a later one via recurrence on C-side
    # sequence from C: t_i = Tr(C alpha^i); t_0=2x, t_1=2(3x+4y), recurrence t_{i+1}=6 t_i - t_{i-1}
    t = [ (2*x) % q, (2*(3*x+4*y)) % q ]
    for i in range(2, len(seq)): t.append((6*t[-1]-t[-2]) % q)
    return tuple(t) == tuple(seq)

m = 60
sf625 = split_fibers(m, 625)
sf81 = split_fibers(m, 81)
print(f"625 split fibers: {len(sf625)}, orbit counts: {[len(r) for _, r in sf625]}")
print(f"81 split fibers: {len(sf81)}, orbit counts: {[len(r) for _, r in sf81]}")
a_fixed = sf81[0][1][0]
print(f"a_fixed period: {period(a_fixed)}")
for fi, (key, reps) in enumerate(sf625):
    print(f"--- 625 fiber {fi}: {len(reps)} orbits, rep periods: {[period(r) for r in reps]}")
    Cs = []
    for r in reps:
        C = recover_C(r, 625)
        ok = check_C(r, C, 625)
        Cs.append(C)
        print(f"    rep C={C} check={ok}")
    # relations between C's: differences and ratios
    C0 = Cs[0]
    for C in Cs[1:]:
        d = ((C[0]-C0[0]) % 625, (C[1]-C0[1]) % 625)
        print(f"    C-C0 = {d}")
