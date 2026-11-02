"""Wave 37, task 1 (retry): B(60) exactly.

Definitions (wave 36, extended): triple test fixes a locked rep and
varies the free component over its orbit reps; collision of the
sorted triple multisets = blind for that move. This script tests
ALL kernel sequences (including zero) at small components, level
representatives at large components, and full-tuple joint
compatibility for the free sets {625} and {81}.
"""
import math, sys
import numpy as np
from collections import defaultdict

M = 60

def mat_pow(Mm, e, q):
    def mul(A, B):
        return [(A[0]*B[0]+A[1]*B[2]) % q, (A[0]*B[1]+A[1]*B[3]) % q,
                (A[2]*B[0]+A[3]*B[2]) % q, (A[2]*B[1]+A[3]*B[3]) % q]
    R = [1, 0, 0, 1]; B = Mm[:]
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

def seq_from(y0, y1, m, q):
    y = [y0, y1]
    for i in range(2, m): y.append((6*y[-1]-y[-2]) % q)
    return tuple(y)

# ---------- split fibers at 81, 625 ----------
reps81 = split_fiber_orbit_reps(M, 81)
reps625 = split_fiber_orbit_reps(M, 625)
print(f"81 split fibers: {len(reps81)}, orbits each: {[len(r) for r in reps81]}", flush=True)
print(f"625 split fibers: {len(reps625)}, orbits each: {[len(r) for r in reps625]}", flush=True)
a_reps = reps81[0]            # 3 locked reps for 625-moves
b_reps = [r for fib in reps625 for r in fib]  # 10 locked reps for 81-moves

def triple_collides(fixed, orbreps, o, q0, qfree):
    """Collision of packed triple multisets across orbit reps."""
    base = [fixed[i]*(qfree*q0) + o[i] for i in range(M)]
    ms = set()
    for b in orbreps:
        key = tuple(sorted(base[i] + b[i]*q0 for i in range(M)))
        if key in ms: return True
        ms.add(key)
    return False

# ---------- small components: all sequences, all locked reps ----------
small = [49, 121, 361, 841]
small_results = {}
for q0 in small:
    pts0 = kernel_points(M, q0)
    assert len(pts0) == q0, (q0, len(pts0))
    # 625-moves: per (sequence, a-rep, 625-fiber) collision?
    b625_any = b625_all = b625_zero_any = b625_zero_all = 0
    b81_any = b81_all = b81_zero_any = b81_zero_all = 0
    for o in pts0:
        iszero = all(v == 0 for v in o)
        # 625-move: a in a_reps, fiber in reps625
        coll = [[triple_collides(a, fib, o, q0, 625) for fib in reps625] for a in a_reps]
        any625 = any(any(row) for row in coll)
        all625 = all(all(row) for row in coll)
        if any625: b625_any += 1
        if all625: b625_all += 1
        if iszero and any625: b625_zero_any += 1
        if iszero and all625: b625_zero_all += 1
        # 81-move: b in b_reps, fiber reps81[0]
        coll81 = [triple_collides(b, reps81[0], o, q0, 81) for b in b_reps]
        any81 = any(coll81); all81 = all(coll81)
        if any81: b81_any += 1
        if all81: b81_all += 1
        if iszero and any81: b81_zero_any += 1
        if iszero and all81: b81_zero_all += 1
    small_results[q0] = dict(n=q0, b625_any=b625_any, b625_all=b625_all,
                             b81_any=b81_any, b81_all=b81_all,
                             z625_any=b625_zero_any, z625_all=b625_zero_all,
                             z81_any=b81_zero_any, z81_all=b81_zero_all)
    print(f"q0={q0}: n={q0} blind625 any={b625_any} all={b625_all} "
          f"blind81 any={b81_any} all={b81_all} | zero: z625 any={b625_zero_any} "
          f"all={b625_zero_all} z81 any={b81_zero_any} all={b81_zero_all}", flush=True)

np.save("/tmp/wave37_small_results.npy", np.array([small_results], dtype=object))
print("SMALL DONE", flush=True)
