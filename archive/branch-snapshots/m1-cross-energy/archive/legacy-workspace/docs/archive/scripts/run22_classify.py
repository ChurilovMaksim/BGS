"""
RUN 22: CLASSIFY all r=6 resonance solutions at small k.
Enumerate explicitly, cluster into combinatorial families,
identify closed forms.
"""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
import sys, os, json
from itertools import product
from sympy import primitive_root

sys.path.insert(0, _BGS_ROOT + r"\src")
from master_formula_strong import find_orbit_H

ART=_BGS_ROOT + r"\artifacts"


def all_solutions(p, H):
    """Brute force all (h1..h6) in H^6 satisfying resonance."""
    inv={h:pow(h,p-2,p) for h in H}
    Hlist=sorted(H); sols=[]
    # meet-in-middle: left (1,3,5) vs right (2,4,6)
    L={}
    for h1 in Hlist:
        s1=h1; t1=inv[h1]
        for h3 in Hlist:
            s13=(s1+h3)%p; t13=(t1+inv[h3])%p
            for h5 in Hlist:
                kk=((s13+h5)%p,(t13+inv[h5])%p)
                L.setdefault(kk,[]).append((h1,h3,h5))
    for h2 in Hlist:
        s2=(-h2)%p; t2=(-inv[h2])%p
        for h4 in Hlist:
            s24=(s2-h4)%p; t24=(t2-inv[h4])%p
            for h6 in Hlist:
                kk=((s24-h6)%p,(t24-inv[h6])%p)
                if kk in L:
                    for trip in L[kk]:
                        sols.append(trip+(h2,h4,h6))
    return sols


def classify(sol, p):
    """Return family label based on pattern."""
    h1,h2,h3,h4,h5,h6=sol
    if h1==h2 and h3==h4 and h5==h6: return "A:slotwise"
    if h1==h4 and h3==h2 and h5==h6: return "B:cross"
    if h1==-h2%p and h3==-h4%p and h5==-h6%p: return "C:negpair"
    # mixed types
    pairs=[]
    if h1==h2: pairs.append("a")
    elif (-h1)%p==h2: pairs.append("n")
    if h3==h4: pairs.append("a")
    elif (-h3)%p==h4: pairs.append("n")
    if h5==h6: pairs.append("a")
    elif (-h5)%p==h6: pairs.append("n")
    if len(pairs)==3: return f"M:{''.join(sorted(pairs))}"
    return "other"


def main():
    print("=== RUN 22: classify r=6 ===")
    results={}
    p=101
    g=int(primitive_root(p))
    for k in [4,5,6,8]:
        alpha=pow(g,(p-1)//k,p)
        H=set(); x=1
        for _ in range(k): H.add(x); x=x*alpha%p
        sols=all_solutions(p,H)
        from collections import Counter
        fams=Counter(classify(s,p) for s in sols)
        results[k]=dict(total=len(sols),families=dict(fams))
        print(f"k={k}: total={len(sols)}")
        for f,c in fams.most_common():
            print(f"   {f}: {c}")
    json.dump(results, open(os.path.join(ART,"run22_classify.json"),"w"), indent=1)


if __name__=="__main__":
    main()
