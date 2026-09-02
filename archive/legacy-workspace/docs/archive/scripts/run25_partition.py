"""
RUN 25 (deep): COMPLETE CLASSIFICATION of r=6 solutions by set
partition of slots. For each partition pi of {1..6}, count solutions
where h_i == h_j iff i,j in same block (up to sign pattern).
Then identify closed form per block type.
"""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
import sys, os, json, itertools
from sympy import primitive_root
sys.path.insert(0, _BGS_ROOT + r"\src")
from master_formula_strong import find_orbit_H

ART=_BGS_ROOT + r"\artifacts"


def set_partitions(n):
    """Generate all set partitions of {0,...,n-1} as list of frozensets."""
    if n==0: return [[]]
    def rec(rest, done):
        if not rest: yield done; return
        first=rest[0]; rest=rest[1:]
        for i,blk in enumerate(done):
            yield from rec(rest, done[:i]+[blk|{first}]+done[i+1:])
        yield from rec(rest, done+[ {first} ])
    yield from rec(list(range(1,n)), [ {0} ])


def classify_by_partition(sol):
    """Return canonical partition label."""
    h=sol
    # group indices by value
    groups={}
    for i,v in enumerate(h):
        groups.setdefault(v,[]).append(i)
    parts=frozenset(frozenset(g) for g in groups.values())
    return parts


def main():
    print("=== RUN 25 deep classification ===")
    p=211
    g=int(primitive_root(p))
    results={}
    for k in [6,10,14]:
        alpha=pow(g,(p-1)//k,p)
        H=set(); x=1
        for _ in range(k): H.add(x); x=x*alpha%p
        inv={h:pow(h,p-2,p) for h in H}
        Hlist=sorted(H)
        sols=[]
        L={}
        for h1 in Hlist:
            for h3 in Hlist:
                s13=(h1+h3)%p; t13=(inv[h1]+inv[h3])%p
                for h5 in Hlist:
                    kk=((s13+h5)%p,(t13+inv[h5])%p)
                    L.setdefault(kk,[]).append((h1,h3,h5))
        for h2 in Hlist:
            for h4 in Hlist:
                s24=(-h2-h4)%p; t24=(-inv[h2]-inv[h4])%p
                for h6 in Hlist:
                    kk=((s24-h6)%p,(t24-inv[h6])%p)
                    if kk in L:
                        for trip in L[kk]: sols.append(trip+(h2,h4,h6))
        fams={}
        for s in sols:
            lbl=tuple(sorted(tuple(sorted(blk)) for blk in classify_by_partition(s)))
            fams[lbl]=fams.get(lbl,0)+1
        top=sorted(fams.items(),key=lambda t:-t[1])[:8]
        results[k]=dict(total=len(sols),
                        families={str(l):c for l,c in top})
        print(f"\nk={k}: total={len(sols)}")
        for l,c in top:
            blocks=[list(b) for b in l]
            print(f"   {blocks}: {c}")
    json.dump(results, open(os.path.join(ART,"run25_partition.json"),"w"),
              indent=1, default=str)


if __name__=="__main__":
    main()
