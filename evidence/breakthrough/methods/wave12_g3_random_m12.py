"""Wave 12, task 4 (G3): random full Fix_m vectors, m=12, look for a pair
with the same exact multiset but Pi_q intersection empty across all q||D
(equivalently, an exact per-class failure, since an exact pi would lie in
every Pi_q). Random CRT sampling: each component vector chosen uniformly
from Fix_m mod q (enumerated by fix_mod_q), combined by CRT.
Chunked; collisions on sorted exact multiset are checked exactly.
"""
import sys, math, time
sys.path.insert(0, '/home/hatch/workspace/bgs-breakthrough/methods')
import numpy as np
from wave11_perclass_component import fix_mod_q, d_t_perms

m = 12
qs = [128, 81, 25, 49, 121]
D = 1
for q in qs: D *= q
print("D =", D, flush=True)
comps = []
for q in qs:
    v = fix_mod_q(m, q)
    print(f"  q={q} n={len(v)}", flush=True)
    comps.append(v)
# CRT coefficients: value = sum comp * (D/q) * inv(D/q mod q) mod D
coeffs = []
for q in qs:
    Mi = D // q
    coeffs.append(Mi * pow(Mi, -1, q) % D)
coeffs = np.array(coeffs, dtype=np.int64)

rng = np.random.default_rng(20261101)
t = math.gcd(m, 4)
perms = d_t_perms(t)
cls_idx = [[i for i in range(m) if i % t == r] for r in range(t)]

def pi_set_for_pair(vec_a, vec_b):
    """vec_a, vec_b: exact vectors (length m). Return set of pi in D_t
    that work for EVERY q (marginal per-class multisets mod q), or empty."""
    good = set(perms)
    for qi, q in enumerate(qs):
        a = vec_a % q; b = vec_b % q
        pa = [tuple(sorted(a[idx])) for idx in cls_idx]
        pb = [tuple(sorted(b[idx])) for idx in cls_idx]
        good_q = set()
        for pi in perms:
            if all(pb[r] == pa[pi[r]] for r in range(t)):
                good_q.add(pi)
        good &= good_q
        if not good:
            return good, qi
    return good, None

def exact_canon(vec):
    pc = tuple(tuple(sorted(vec[idx])) for idx in cls_idx)
    best = None
    for pi in perms:
        cand = tuple(pc[pi[r]] for r in range(t))
        if best is None or cand < best: best = cand
    return best

N = 2000000
CH = 100000
seen = {}  # sorted bytes -> (vec, comp_indices)
collisions = 0; pi_empty = 0; exact_bad = 0
t0 = time.time()
for start in range(0, N, CH):
    n = min(CH, N - start)
    # exact values via CRT, component by component
    vals = np.zeros((n, m), dtype=np.int64)
    comp_idx = []
    for qi, (q, v) in enumerate(zip(qs, comps)):
        idx = rng.integers(0, len(v), size=n)
        comp_idx.append(idx)
        vals = (vals + v[idx].astype(np.int64) * int(coeffs[qi])) % D
    srt = np.sort(vals, axis=1)
    for j in range(n):
        key = srt[j].tobytes()
        ent = seen.get(key)
        if ent is None:
            seen[key] = vals[j].copy()
        else:
            collisions += 1
            other = ent
            good, bad_qi = pi_set_for_pair(other, vals[j])
            if not good:
                pi_empty += 1
                print(f"PI-EMPTY pair! bad_qi={bad_qi} (q={qs[bad_qi] if bad_qi is not None else None})", flush=True)
                print(f"  vec_a={tuple(other)}", flush=True)
                print(f"  vec_b={tuple(vals[j])}", flush=True)
            if exact_canon(other) != exact_canon(vals[j]):
                exact_bad += 1
                print(f"EXACT per-class failure pair!", flush=True)
                print(f"  vec_a={tuple(other)}", flush=True)
                print(f"  vec_b={tuple(vals[j])}", flush=True)
    print(f"chunk {start+n}/{N} seen={len(seen)} collisions={collisions} pi_empty={pi_empty} exact_bad={exact_bad} time={time.time()-t0:.0f}s", flush=True)
print(f"TOTAL samples={N} distinct_multisets={len(seen)} collisions={collisions} pi_empty={pi_empty} exact_bad={exact_bad}")
