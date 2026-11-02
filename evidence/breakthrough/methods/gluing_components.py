"""Component-level Fix enumeration and affine-separation test for m=9,12.
Fix mod q = ker(H_m mod q), H = 6I - C - C^T, i.e. y_{i+1} = 6 y_i - y_{i-1},
periodic of period m. Solved via (A^m - I) v = 0 mod q, A = [[0,1],[-1,6]],
by iterating a and solving the linear congruence for b (no q^2 scan).
Affine group: p(j) = a*j + b mod m, a in (Z/m)^x, acting by (p.y)_j = y_{p(j)}.
Separation reading (R) per component: within each sorted-multiset class,
all vectors share one affine canonical form (lexicographic min over Aff).
"""
import json, math
from collections import defaultdict

def mat_mul(A, B):
    return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
            [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]

def mat_pow(A, n):
    R = [[1,0],[0,1]]
    while n:
        if n & 1: R = mat_mul(R, A)
        A = mat_mul(A, A); n >>= 1
    return R

def fix_mod(m, q):
    Am = mat_pow([[0,1],[-1,6]], m)
    P, Q = Am[0][0]-1, Am[0][1]
    Rr, S = Am[1][0], Am[1][1]-1
    out = []
    for a in range(q):
        rhs = (-P*a) % q
        g = math.gcd(Q, q)
        if rhs % g: continue
        Qr, qr = Q//g, q//g
        # Qr * b = rhs/g (mod qr); Qr invertible mod qr
        b0 = ((rhs//g) * pow(Qr % qr, -1, qr)) % qr if qr > 1 else 0
        for k in range(g):
            b = b0 + k*qr
            if (Rr*a + S*b) % q != 0: continue
            y = [a, b] if m >= 2 else [a]
            for i in range(1, m-1):
                y.append((6*y[i] - y[i-1]) % q)
            y = y[:m]
            # periodicity sanity: y_m should be a, y_{m+1} should be b
            assert (6*y[-1] - y[-2]) % q == a, (m, q, a, b, y)
            out.append(tuple(y))
    return out

def aff_perms(m):
    units = [a for a in range(m) if math.gcd(a, m) == 1]
    return [(a, b) for a in units for b in range(m)]

def canon(y, perms, m):
    best = None
    for a, b in perms:
        t = tuple(y[(a*j + b) % m] for j in range(m))
        if best is None or t < best: best = t
    return best

def analyze(m, q):
    vecs = fix_mod(m, q)
    perms = aff_perms(m)
    by_sorted = defaultdict(set)
    by_sorted_vecs = defaultdict(list)
    for v in vecs:
        c = canon(v, perms, m)
        s = tuple(sorted(v))
        by_sorted[s].add(c)
        by_sorted_vecs[s].append(v)
    bad = {s: cs for s, cs in by_sorted.items() if len(cs) > 1}
    return {
        "m": m, "q": q, "n_fix": len(vecs),
        "n_fibers": len(by_sorted),
        "aff_bad_fibers": len(bad),
        "bad_examples": [
            {"sorted": list(s), "n_canons": len(cs),
             "examples": [list(v) for v in by_sorted_vecs[s][:4]]}
            for s, cs in list(bad.items())[:5]
        ],
        "fiber_size_dist": {str(k): v for k, v in
            sorted(__import__('collections').Counter(
                len(vs) for vs in by_sorted_vecs.values()).items())},
    }

if __name__ == "__main__":
    results = {}
    for m, qs in [(9, [4, 49, 39601]), (12, [128, 81, 25, 49, 121])]:
        for q in qs:
            r = analyze(m, q)
            results[f"m{m}_q{q}"] = r
            print(m, q, "n_fix=", r["n_fix"], "fibers=", r["n_fibers"],
                  "aff_bad=", r["aff_bad_fibers"], "sizes=", r["fiber_size_dist"])
    json.dump(results, open("/home/hatch/workspace/bgs-breakthrough/methods/gluing_components_result.json", "w"), indent=1)
