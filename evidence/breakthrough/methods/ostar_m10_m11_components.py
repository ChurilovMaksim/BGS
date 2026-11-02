"""Wave 5 task 1, step 1: per-component affine-separation test for m=10,11.
Reuses fix_mod / aff_perms / canon from gluing_components.py (same
conventions as the m=9/12 work): Fix mod q = ker(H_m mod q),
H = 6I - C - C^T; affine perms p(j) = a*j + b mod m, a in (Z/m)^x,
acting by (p.y)_j = y_{p(j)}; separation (R): within each sorted-multiset
class, all vectors share one affine canonical form (lex min over Aff).
For the large component q=124609 (m=11) the canon is computed with numpy
vectorised lex-min (chunked), not pure Python, to keep it tractable.
Outputs ostar_m10_m11_components.json and, for q=124609, the vector array
as ostar_m11_q124609.npy.
"""
import sys, json, math, time
from collections import defaultdict, Counter
sys.path.insert(0, '/home/hatch/workspace/bgs-breakthrough/methods')
from gluing_components import fix_mod, aff_perms, canon
import numpy as np

def verify_H(vecs, m, q):
    for v in vecs:
        for i in range(m):
            if (6*v[i] - v[i-1] - v[(i+1) % m]) % q != 0:
                return False
    return True

def analyze_small(m, q):
    t0 = time.time()
    vecs = fix_mod(m, q)
    perms = aff_perms(m)
    by_sorted = defaultdict(set)
    by_sorted_vecs = defaultdict(list)
    for v in vecs:
        s = tuple(sorted(v))
        by_sorted[s].add(canon(v, perms, m))
        by_sorted_vecs[s].append(v)
    bad = {s: cs for s, cs in by_sorted.items() if len(cs) > 1}
    okH = verify_H(vecs, m, q)
    return {
        "m": m, "q": q, "n_fix": len(vecs), "n_fibers": len(by_sorted),
        "aff_bad_fibers": len(bad), "H_ok": okH,
        "distinct_vectors": sum(1 for v in vecs if len(set(v)) == m),
        "repeated_vectors": sum(1 for v in vecs if len(set(v)) < m),
        "fiber_size_dist": {str(k): v for k, v in sorted(Counter(len(vs) for vs in by_sorted_vecs.values()).items())},
        "bad_examples": [
            {"sorted": list(s), "n_canons": len(cs),
             "examples": [list(v) for v in by_sorted_vecs[s][:4]]}
            for s, cs in list(bad.items())[:5]
        ],
        "seconds": round(time.time() - t0, 2),
    }, vecs

def analyze_large_numpy(m, q):
    """vecs via fix_mod; sorted fibers via numpy; canon via chunked
    vectorised lex-min over Aff perms."""
    t0 = time.time()
    vecs = fix_mod(m, q)
    arr = np.array(vecs, dtype=np.int64)
    np.save(f"/home/hatch/workspace/bgs-breakthrough/methods/ostar_m11_q{q}.npy", arr)
    # H check vectorised
    Hcheck = (6*arr - np.roll(arr, 1, axis=1) - np.roll(arr, -1, axis=1)) % q
    okH = bool(np.all(Hcheck == 0))
    sorted_keys = np.sort(arr, axis=1)
    uniq_sorted, sorted_counts = np.unique(sorted_keys, axis=0, return_counts=True)
    distinct = int(np.sum([len(set(v)) == m for v in vecs])) if False else None
    # distinct / repeated via numpy: sorted row has a duplicate iff any adjacent equal
    has_dup = np.any(sorted_keys[:, 1:] == sorted_keys[:, :-1], axis=1)
    repeated = int(np.sum(has_dup))
    # affine perms
    units = [a for a in range(m) if math.gcd(a, m) == 1]
    perms = np.array([[(a*j + b) % m for j in range(m)] for a in units for b in range(m)], dtype=np.int64)
    # canon, chunked
    canon_arr = np.empty_like(arr)
    CH = 2000
    INF = np.iinfo(np.int64).max
    for s in range(0, len(arr), CH):
        chunk = arr[s:s+CH]
        # permuted: (chunk, perm, coord) via fancy indexing chunk[:, perms]
        permuted = chunk[:, perms]  # shape (C, P, m)
        mask = np.ones(permuted.shape[:2], dtype=bool)
        for c in range(m):
            vals = np.where(mask, permuted[:, :, c], INF)
            mn = vals.min(axis=1, keepdims=True)
            mask &= (permuted[:, :, c] == mn)
        chosen = mask.argmax(axis=1)
        canon_arr[s:s+CH] = permuted[np.arange(len(chunk)), chosen]
    combo = np.concatenate([sorted_keys, canon_arr], axis=1)
    uniq_combo = np.unique(combo, axis=0)
    # orbits per fiber: count distinct combo rows per sorted key
    orbit_per_fiber = Counter()
    for row in uniq_combo:
        orbit_per_fiber[tuple(row[:m].tolist())] += 1
    bad_keys = [k for k, c in orbit_per_fiber.items() if c > 1]
    # bad examples: pick first bad keys, list vectors
    bad_examples = []
    sorted_to_vecs = {}
    # build dict only for bad keys (scan rows)
    bad_set = set(bad_keys)
    for v, sk in zip(vecs, sorted_keys):
        t = tuple(sk.tolist())
        if t in bad_set and len(sorted_to_vecs.get(t, [])) < 4:
            sorted_to_vecs.setdefault(t, []).append(list(v))
    for k in bad_keys[:5]:
        bad_examples.append({"sorted": list(k), "n_canons": orbit_per_fiber[k],
                             "examples": sorted_to_vecs.get(k, [])})
    return {
        "m": m, "q": q, "n_fix": len(vecs), "n_fibers": int(len(uniq_sorted)),
        "aff_bad_fibers": len(bad_keys), "H_ok": okH,
        "distinct_vectors": int(len(vecs) - repeated),
        "repeated_vectors": repeated,
        "fiber_size_dist": {str(k): int(v) for k, v in sorted(Counter(sorted_counts.tolist()).items())},
        "bad_examples": bad_examples,
        "seconds": round(time.time() - t0, 2),
    }, vecs

if __name__ == "__main__":
    results = {}
    for m, q in [(10, 32), (10, 841), (10, 1681), (11, 4), (11, 529)]:
        r, _ = analyze_small(m, q)
        results[f"m{m}_q{q}"] = r
        print(m, q, "n_fix=", r["n_fix"], "fibers=", r["n_fibers"],
              "aff_bad=", r["aff_bad_fibers"], "H_ok=", r["H_ok"],
              "distinct=", r["distinct_vectors"], "repeated=", r["repeated_vectors"],
              "sizes=", r["fiber_size_dist"], f"({r['seconds']}s)", flush=True)
    r, _ = analyze_large_numpy(11, 124609)
    results["m11_q124609"] = r
    print(11, 124609, "n_fix=", r["n_fix"], "fibers=", r["n_fibers"],
          "aff_bad=", r["aff_bad_fibers"], "H_ok=", r["H_ok"],
          "distinct=", r["distinct_vectors"], "repeated=", r["repeated_vectors"],
          "sizes=", r["fiber_size_dist"], f"({r['seconds']}s)", flush=True)
    json.dump(results, open("/home/hatch/workspace/bgs-breakthrough/methods/ostar_m10_m11_components.json", "w"), indent=1)
    print("written ostar_m10_m11_components.json")
