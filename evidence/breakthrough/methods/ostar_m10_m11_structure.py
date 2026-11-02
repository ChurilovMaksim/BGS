"""Wave 5 task 1, step 2: structure of component vectors for m=10,11.
For each component: periods, value-class patterns, A(v) vs D(v).
A(v) = {p.v : p in Aff, p.v in Fix mod q} (distinct vectors).
D(v) = {d.v : d in Dihedral} (dihedral always preserves Fix).
Dihedral perms: p(j) = j + b and p(j) = b - j (mod m), action (p.y)_j = y_{p(j)}.
"""
import sys, json, math
from collections import Counter, defaultdict
sys.path.insert(0, '/home/hatch/workspace/bgs-breakthrough/methods')
from gluing_components import fix_mod, aff_perms
import numpy as np

def dihedral_perms(m):
    perms = []
    for b in range(m):
        perms.append(tuple((j + b) % m for j in range(m)))
        perms.append(tuple((b - j) % m for j in range(m)))
    return sorted(set(perms))

def apply_perm(v, p, m):
    return tuple(v[p[j]] for j in range(m))

def analyze(m, q, vecs):
    perms = aff_perms(m)
    dperms = dihedral_perms(m)
    dperm_set = set(dperms)
    fixset = set(vecs)
    # periods: d|m, v[j]==v[j+d] for all j
    period_dist = Counter()
    for v in vecs:
        pers = [d for d in range(1, m+1) if m % d == 0 and all(v[j] == v[(j+d) % m] for j in range(m))]
        period_dist[min(pers)] += 1
    # A vs D
    a_sizes = Counter(); d_sizes = Counter()
    a_ne_d = 0; a_ne_d_examples = []
    nondihedral_effect_vecs = 0
    for v in vecs:
        A = set()
        for a, b in perms:
            w = tuple(v[(a*j + b) % m] for j in range(m))
            if w in fixset:
                A.add(w)
        D = set(apply_perm(v, p, m) for p in dperms)
        a_sizes[len(A)] += 1; d_sizes[len(D)] += 1
        if A != D:
            a_ne_d += 1
            if len(a_ne_d_examples) < 3:
                extra = sorted(A - D)
                # perms achieving first extra vector
                achieving = []
                for a, b in perms:
                    w = tuple(v[(a*j + b) % m] for j in range(m))
                    if extra and w == extra[0]:
                        achieving.append((a, b))
                a_ne_d_examples.append({"v": list(v), "A_size": len(A), "D_size": len(D),
                                        "extra_example": list(extra[0]) if extra else None,
                                        "achieving_perms": achieving[:4]})
    return {
        "m": m, "q": q, "n_fix": len(vecs),
        "period_dist": {str(k): v for k, v in sorted(period_dist.items())},
        "A_size_dist": {str(k): v for k, v in sorted(a_sizes.items())},
        "D_size_dist": {str(k): v for k, v in sorted(d_sizes.items())},
        "vectors_with_A_ne_D": a_ne_d,
        "examples_A_ne_D": a_ne_d_examples,
        "sample_vectors": [list(v) for v in vecs[:3]],
    }

if __name__ == "__main__":
    out = {}
    for m, q in [(10, 32), (10, 841), (10, 1681), (11, 4), (11, 529)]:
        vecs = fix_mod(m, q)
        r = analyze(m, q, vecs)
        out[f"m{m}_q{q}"] = r
        print(m, q, "periods=", r["period_dist"], "A sizes=", r["A_size_dist"],
              "D sizes=", r["D_size_dist"], "A!=D:", r["vectors_with_A_ne_D"], flush=True)
    # large component m=11 q=124609 from saved array
    arr = np.load("/home/hatch/workspace/bgs-breakthrough/methods/ostar_m11_q124609.npy")
    vecs = [tuple(row.tolist()) for row in arr]
    r = analyze(11, 124609, vecs)
    out["m11_q124609"] = r
    print(11, 124609, "periods=", r["period_dist"], "A sizes=", r["A_size_dist"],
          "D sizes=", r["D_size_dist"], "A!=D:", r["vectors_with_A_ne_D"], flush=True)
    json.dump(out, open("/home/hatch/workspace/bgs-breakthrough/methods/ostar_m10_m11_structure.json", "w"), indent=1)
    print("written ostar_m10_m11_structure.json")
