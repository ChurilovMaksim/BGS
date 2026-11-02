"""Wave 5 task 1, step 4: sample sanity check of the gluing arguments.
For random global y (tuple representation over prime-power components),
enumerate ALL dihedral effect combinations (D(v) per component, A=D was
verified in step 2) and check: sorted(candidate triples) == sorted(base
triples) AND affine tuple-canon(candidate) != affine tuple-canon(base)
would be a hit. Expect 0 hits if the arguments/conventions are right.
m=11: random y over all components (argument claims all y covered).
m=10: random y with q32 non-constant and q1681 pattern distinct (Tag B).
"""
import sys, random, math
sys.path.insert(0, '/home/hatch/workspace/bgs-breakthrough/methods')
from gluing_components import fix_mod, aff_perms
import numpy as np

def dihedral_perms(m):
    perms = []
    for b in range(m):
        perms.append(tuple((j + b) % m for j in range(m)))
        perms.append(tuple((b - j) % m for j in range(m)))
    return sorted(set(perms))

def D_list(v, dperms, m, fixset):
    out = []
    seen = set()
    for p in dperms:
        w = tuple(v[p[j]] for j in range(m))
        if w not in seen:
            seen.add(w); out.append(w)
    return out

def canon_tuples(triples, perms, m):
    best = None
    for p in perms:
        t = tuple(triples[p[j]] for j in range(m))
        if best is None or t < best: best = t
    return best

def check_y(vecs_by_comp, m, rng):
    # vecs_by_comp: list of (vecs, fixset, D-cache)
    chosen = [rng.choice(vs) for vs, _, _ in vecs_by_comp]
    triples = [tuple(v[j] for v in chosen) for j in range(m)]
    base_sorted = tuple(sorted(triples))
    aperms = aff_perms(m)
    # affine perms as position tuples
    aperm_tuples = [tuple((a*j + b) % m for j in range(m)) for a, b in aperms]
    base_canon = canon_tuples(triples, aperm_tuples, m)
    Dlists = []
    for (vs, fixset, _), v in zip(vecs_by_comp, chosen):
        Dlists.append(D_list(v, dihedral_perms(m), m, fixset))
    combos = 1
    for dl in Dlists: combos *= len(dl)
    hits = []
    # iterate combos via recursion
    def rec(idx, cur):
        if hits: return
        if idx == len(Dlists):
            cand = [tuple(cur[c][j] for c in range(len(cur))) for j in range(m)]
            if tuple(sorted(cand)) != base_sorted: return
            if canon_tuples(cand, aperm_tuples, m) == base_canon: return
            hits.append({"y": [list(v) for v in chosen], "combo": [list(w) for w in cur]})
            return
        for w in Dlists[idx]:
            cur.append(w); rec(idx+1, cur); cur.pop()
            if hits: return
    rec(0, [])
    return combos, hits

if __name__ == "__main__":
    rng = random.Random(12345)
    # m=11
    vecs11 = {}
    for q in (4, 529):
        vecs11[q] = fix_mod(11, q)
    arr = np.load("/home/hatch/workspace/bgs-breakthrough/methods/ostar_m11_q124609.npy")
    vecs11[124609] = [tuple(row.tolist()) for row in arr]
    comps11 = [(vecs11[q], set(vecs11[q]), None) for q in (4, 529, 124609)]
    tot = 0; hits_all = []
    for t in range(60):
        combos, hits = check_y(comps11, 11, rng)
        tot += combos
        if hits: hits_all.append(hits); print("m11 HIT", hits); break
    print(f"m11 sample: 60 y, {tot} combos, hits={len(hits_all)}", flush=True)
    # m=10 Tag B
    vecs10 = {}
    for q in (32, 841, 1681):
        vecs10[q] = fix_mod(10, q)
    comps10_base = [(vecs10[q], set(vecs10[q]), None) for q in (32, 841, 1681)]
    tot = 0; hits_all = []
    tried = 0
    while tried < 60:
        # sample with Tag B condition: q32 non-const, q1681 pattern distinct
        v32 = rng.choice(vecs10[32]); v1681 = rng.choice(vecs10[1681]); v841 = rng.choice(vecs10[841])
        if len(set(v32)) == 1: continue
        if len(set(v1681[:5])) != 5: continue
        # monkey-patch check_y by temporarily using chosen via rng? Instead inline:
        # use check_y with comps restricted: easiest is to call check_y on comps where
        # we force choice by seeding: skip; do direct check here via a helper
        # Reuse check_y logic by building comps with singletons
        comps = [( [v32], set(vecs10[32]), None), ([v841], set(vecs10[841]), None), ([v1681], set(vecs10[1681]), None)]
        # check_y picks rng.choice from singleton lists -> the chosen vectors
        combos, hits = check_y(comps, 10, rng)
        tried += 1; tot += combos
        if hits: hits_all.append(hits); print("m10 TagB HIT", hits); break
    print(f"m10 TagB sample: {tried} y, {tot} combos, hits={len(hits_all)}", flush=True)
