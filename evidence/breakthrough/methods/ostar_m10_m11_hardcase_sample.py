"""Wave 5 task 1, step 5: targeted Python cross-checks of the hardest cases.
(a) m=10 remaining set: random y with q841 non-distinct AND (q32 const OR
    q1681 pattern non-distinct); all dihedral effect combos; expect 0 hits.
(b) m=11 both-nontrivial-reflection case: random y with q529 and q124609
    both reflection-symmetric (non-zero); all dihedral effect combos;
    expect 0 hits (this is the case the reflection argument must cover).
Hit definition (tuple representation, as in the C++ search): sorted
candidate triples == sorted base triples AND affine tuple-canon differs.
"""
import sys, random
sys.path.insert(0, '/home/hatch/workspace/bgs-breakthrough/methods')
from gluing_components import fix_mod, aff_perms
import numpy as np

def dihedral_perms(m):
    perms = []
    for b in range(m):
        perms.append(tuple((j + b) % m for j in range(m)))
        perms.append(tuple((b - j) % m for j in range(m)))
    return sorted(set(perms))

def D_list(v, dperms, m):
    out, seen = [], set()
    for p in dperms:
        w = tuple(v[p[j]] for j in range(m))
        if w not in seen: seen.add(w); out.append(w)
    return out

def canon_tuples(triples, perm_tuples, m):
    best = None
    for p in perm_tuples:
        t = tuple(triples[p[j]] for j in range(m))
        if best is None or t < best: best = t
    return best

def check_y(chosen, m, aperm_tuples, dperms):
    triples = [tuple(v[j] for v in chosen) for j in range(m)]
    base_sorted = tuple(sorted(triples))
    base_canon = canon_tuples(triples, aperm_tuples, m)
    Dlists = [D_list(v, dperms, m) for v in chosen]
    combos = 1
    for dl in Dlists: combos *= len(dl)
    hits = []
    def rec(idx, cur):
        if hits: return
        if idx == len(Dlists):
            cand = [tuple(cur[c][j] for c in range(len(cur))) for j in range(m)]
            if tuple(sorted(cand)) != base_sorted: return
            if canon_tuples(cand, aperm_tuples, m) == base_canon: return
            hits.append(cur.copy()); return
        for w in Dlists[idx]:
            cur.append(w); rec(idx+1, cur); cur.pop()
            if hits: return
    rec(0, [])
    return combos, hits

if __name__ == "__main__":
    rng = random.Random(999)
    # (a) m=10 remaining
    v32 = fix_mod(10, 32); v841 = fix_mod(10, 841); v1681 = fix_mod(10, 1681)
    aperms10 = [tuple((a*j + b) % 10 for j in range(10)) for a, b in aff_perms(10)]
    dperms10 = dihedral_perms(10)
    rem841 = [v for v in v841 if len(set(v)) < 10]
    const32 = [v for v in v32 if len(set(v)) == 1]
    patnd1681 = [v for v in v1681 if len(set(v[:5])) < 5]
    tot = 0; tried = 0
    while tried < 200:
        a = rng.choice(rem841)
        if rng.random() < 0.5:
            b = rng.choice(const32); c = rng.choice(v1681)
        else:
            b = rng.choice(v32); c = rng.choice(patnd1681)
        combos, hits = check_y([b, a, c], 10, aperms10, dperms10)
        tried += 1; tot += combos
        if hits: print("m10 REMAINING HIT", hits); break
    print(f"m10 remaining sample: {tried} y, {tot} combos, hits={1 if hits else 0}", flush=True)
    # (b) m=11 reflection-reflection
    v4 = fix_mod(11, 4); v529 = fix_mod(11, 529)
    arr = np.load("/home/hatch/workspace/bgs-breakthrough/methods/ostar_m11_q124609.npy")
    v124609 = [tuple(row.tolist()) for row in arr]
    aperms11 = [tuple((a*j + b) % 11 for j in range(11)) for a, b in aff_perms(11)]
    dperms11 = dihedral_perms(11)
    # reflection-symmetric = dihedral orbit size 11 (from step 2: A size 11)
    # recompute D size cheaply via stabiliser: vector invariant under some reflection
    def is_refl_sym(v, m):
        for b in range(m):
            if all(v[(b - j) % m] == v[j] for j in range(m)):
                return True
        return False
    refl529 = [v for v in v529 if len(set(v)) > 1 and is_refl_sym(v, 11)]
    refl124609 = [v for v in v124609 if len(set(v)) > 1 and is_refl_sym(v, 11)]
    print(f"refl counts: 529->{len(refl529)}, 124609->{len(refl124609)}", flush=True)
    tot = 0; tried = 0
    while tried < 100:
        a = rng.choice(v4); b = rng.choice(refl529); c = rng.choice(refl124609)
        combos, hits = check_y([a, b, c], 11, aperms11, dperms11)
        tried += 1; tot += combos
        if hits: print("m11 REFL HIT", hits); break
    print(f"m11 refl-refl sample: {tried} y, {tot} combos, hits={1 if hits else 0}", flush=True)
