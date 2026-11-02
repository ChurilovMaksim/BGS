import numpy as np
from collections import defaultdict
from itertools import product

def fix_mod_q(P, q):
    vecs=[]
    y1_all=np.arange(q, dtype=np.int64)
    for y0 in range(q):
        a=np.full(q, y0, dtype=np.int64); b=y1_all.copy()
        seq=[a.copy(), b.copy()]
        for _ in range(P):
            c=(6*b-a)%q; a,b=b,c; seq.append(b.copy())
        ok=(seq[P]==y0)&(seq[P+1]==y1_all)
        for j in np.where(ok)[0]:
            vecs.append(tuple(int(seq[k][j]) for k in range(P)))
    return vecs

def d4():
    out=[]
    for b in range(4):
        for sgn in (1,-1):
            pi=tuple((sgn*i+b)%4 for i in range(4))
            if pi not in out: out.append(pi)
    return out
PIS=d4()
print("D4 size", len(PIS), PIS)

def per_class(p):
    return tuple(tuple(sorted(p[j] for j in range(len(p)) if j%4==r)) for r in range(4))

def pi_pattern(cp, cpp):
    # pi with cpp[r]==cp[pi[r]] for all r
    return [pi for pi in PIS if all(cpp[r]==cp[pi[r]] for r in range(4))]

def pi_v(v, vp):
    return [pi for pi in PIS if all(vp[r]==v[pi[r]] for r in range(4))]

# P=8 patterns
P=8; a=9; q=512
vecs=fix_mod_q(P,q)
print("patterns", len(vecs))
groups=defaultdict(list)
for v in vecs: groups[tuple(sorted(v))].append(v)
pcs={v: per_class(v) for v in vecs}
# precompute pattern pairs pi_pattern sets, and value positions by class
# For each pattern p, pos_by_value: value -> set of classes (mod4) where it occurs, and positions
from collections import Counter
# v types
vtypes={}
for a1,b1 in product(range(3), repeat=2):
    v=tuple((a1,b1,(-a1)%3,(-b1)%3))
    vtypes[v]= (a1,b1)
print("v types", len(vtypes))
# For each v, vp in D4 orbit: compute pi_v
# Abstract counterexample search: for pattern pair (p,pp) and v,vp with pi_v nonempty,
# check tau existence per-k: for each k, exists j with p[j]==pp[k] and j%4 in F_{k%4}
# where F_r = {s: v[s]==vp[r]}
# and pi_pattern intersect pi_v empty
found=[]
checked=0
for ms, vs in groups.items():
    for p in vs:
        # positions by value+class
        # for speed: for each value, set of classes where p has that value
        val_classes=defaultdict(set)
        for j,val in enumerate(p): val_classes[val].add(j%4)
        cp=pcs[p]
        for pp in vs:
            if pp==p: continue
            cpp=pcs[pp]
            pis_pat=pi_pattern(cp,cpp)
            if not pis_pat: 
                print("pattern lemma FAIL", p, pp); raise SystemExit
            for v, vp_candidates in [(v, [tuple(v[pi[r]] for r in range(4)) for pi in PIS]) for v in vtypes]:
                pass
            # loop v, vp
            for v in vtypes:
                # vp must be in D4 orbit of v (else pi_v empty, skip - compatibility vacuous? pi_v empty means component Lemma Y fails, not our case)
                for pi3 in PIS:
                    vp=tuple(v[pi3[r]] for r in range(4))
                    pis3=pi_v(v,vp)
                    if set(pis_pat)&set(pis3): continue
                    # tau existence per-k
                    F=[{s for s in range(4) if v[s]==vp[r]} for r in range(4)]
                    ok=True
                    for k,val in enumerate(pp):
                        if not (val_classes[val] & F[k%4]):
                            ok=False; break
                    if ok:
                        found.append((p,pp,v,vp,pis_pat,pis3))
                        print("ABSTRACT COUNTEREXAMPLE", "p=",p,"pp=",pp,"v=",v,"vp=",vp,"pi_pat=",pis_pat,"pi_v=",pis3)
                        if len(found)>=5: 
                            print("found>=5, stop"); raise SystemExit
    # progress
print("done, abstract counterexamples:", len(found))
