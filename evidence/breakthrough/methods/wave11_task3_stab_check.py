# Verification of Lemma S (stabilizer adjustment) for all Fix patterns at P=8,16.
import numpy as np
from collections import Counter
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
def per_class(p):
    return tuple(tuple(sorted(p[j] for j in range(len(p)) if j%4==r)) for r in range(4))
for P,q in [(8,512),(16,2048)]:
    vecs=fix_mod_q(P,q)
    vtypes=[tuple((a1,b1,(-a1)%3,(-b1)%3)) for a1,b1 in product(range(3), repeat=2)]
    fails=0; total=0
    for p in vecs:
        cp=per_class(p)
        Stab=[d for d in PIS if all(cp[d[r]]==cp[r] for r in range(4))]
        for v in vtypes:
            blocks={}
            for r, val in enumerate(v): blocks.setdefault(val,set()).add(r)
            Fblocks=list(blocks.values())
            for gamma in PIS:
                ok=True
                for F in Fblocks:
                    u1=Counter(); u2=Counter()
                    for s in F: u1.update(cp[s])
                    for s in F: u2.update(cp[gamma[s]])
                    if u1!=u2: ok=False; break
                if not ok: continue
                total+=1
                if not any(all({delta[gamma[s]] for s in F}==F for F in Fblocks) for delta in Stab):
                    fails+=1
                    print("FAIL",P,p,v,gamma)
    print(f"P={P} patterns={len(vecs)} gamma-cases={total} fails={fails}")
