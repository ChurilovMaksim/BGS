"""Wave 8 task 1: explore Lemma Y per prime-power component (fast version).

Fix_m mod q via kernel of (M^m - I) mod q, M=[[6,-1],[1,0]].
Then sequences from kernel vectors by recurrence.
Checks cyclicity (a generator with a unit entry) and:
  multiset {c*g_i}  ->  class-sum vector Y mod q up to D_t ?
A failure lifts (CRT, other components 0) to a global Lemma Y counterexample.
"""
import math
import numpy as np
import sympy as sp
from collections import defaultdict

def D_of_m(m):
    s_prev, s_cur = 2, 6
    if m == 1:
        return 4
    for _ in range(2, m + 1):
        s_prev, s_cur = s_cur, 6 * s_cur - s_prev
    return s_cur - 2

def mat_pow_mod(M, e, q):
    # 2x2
    R = np.array([[1, 0], [0, 1]], dtype=object)
    B = M.copy()
    while e:
        if e & 1:
            R = (R @ B) % q
        B = (B @ B) % q
        e >>= 1
    return R

def fix_mod_q(m, q):
    M = np.array([[6, q - 1], [1, 0]], dtype=object)
    A = mat_pow_mod(M, m, q)
    a11 = (int(A[0, 0]) - 1) % q
    a12 = int(A[0, 1]) % q
    a21 = int(A[1, 0]) % q
    a22 = (int(A[1, 1]) - 1) % q
    vecs = []
    # vectorised kernel scan in chunks of a
    b = np.arange(q, dtype=np.int64)
    for a in range(q):
        lhs1 = (a11 * a + a12 * b) % q
        lhs2 = (a21 * a + a22 * b) % q
        for bb in b[(lhs1 == 0) & (lhs2 == 0)]:
            vecs.append((a, int(bb)))
    pts = []
    for (a, bb) in vecs:
        seq = [a, bb]
        for _ in range(m):
            seq.append((6 * seq[-1] - seq[-2]) % q)
        # verify period (should hold by kernel construction)
        assert seq[m] == a and seq[m + 1] == bb
        pts.append(tuple(seq[:m]))
    return pts

def class_sums(vec, m, t, q):
    Y = [0] * t
    for i, v in enumerate(vec):
        Y[i % t] = (Y[i % t] + v) % q
    return tuple(Y)

def d_t_orbit(vec, t):
    out = set()
    for b in range(t):
        out.add(tuple(vec[(r + b) % t] for r in range(t)))
        out.add(tuple(vec[(-r + b) % t] for r in range(t)))
    return out

def analyse(m, q):
    pts = fix_mod_q(m, q)
    t = math.gcd(m, 4)
    # max scalar-orbit size (cyclicity test)
    maxorb = 0
    for p in pts:
        s = {tuple((c * x) % q for x in p) for c in range(q)}
        maxorb = max(maxorb, len(s))
    by_ms = defaultdict(set)
    by_ms_ex = defaultdict(list)
    for vec in pts:
        ms = tuple(sorted(vec))
        Y = class_sums(vec, m, t, q)
        canon = min(d_t_orbit(Y, t))
        by_ms[ms].add(canon)
        by_ms_ex[ms].append((vec, Y))
    bad = {ms: v for ms, v in by_ms.items() if len(v) > 1}
    bad_ex = None
    if bad:
        ms, v = next(iter(bad.items()))
        bad_ex = (ms, sorted(v), by_ms_ex[ms][:4])
    return {'m': m, 'q': q, 'n_fix': len(pts), 'max_scalar_orbit': maxorb,
            'n_multisets': len(by_ms),
            'bad_multisets': len(bad), 'bad_example': bad_ex}

for m in [4, 6, 8, 10, 12, 14, 16, 18, 20]:
    D = D_of_m(m)
    fac = sp.factorint(D)
    print(f"=== m={m} D={D} factor={fac}", flush=True)
    for p, e in fac.items():
        q = p ** e
        if q > 5000:
            print(f"  q={q} SKIP (>5000)", flush=True)
            continue
        r = analyse(m, q)
        print(f"  q={q} n_fix={r['n_fix']} max_scalar_orbit={r['max_scalar_orbit']} n_multisets={r['n_multisets']} bad={r['bad_multisets']}", flush=True)
        if r['bad_example']:
            print(f"    BAD multiset={r['bad_example'][0]} orbits={r['bad_example'][1]} examples={r['bad_example'][2]}", flush=True)
