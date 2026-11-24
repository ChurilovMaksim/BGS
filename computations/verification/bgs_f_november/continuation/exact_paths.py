"""Integer enumeration for F_3. All displayed signed totals are exact fractions."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from collections import Counter,defaultdict
from fractions import Fraction
from itertools import product
import json

def norm3(c):
    a,b,d=c
    return a*a+b*b+d*d-a*b-a*d-b*d
def run(m):
    edge_hist=Counter();phases=defaultdict(lambda:[0,0,0]);cyclic=0;single=0
    for w in product(range(3),repeat=m):
        edges=tuple(zip(w,w[1:]+w[:1]));counts=Counter(edges)
        prefix=w[:2]
        sig=tuple(counts[i,j] for i in range(3) for j in range(3))
        edge_hist[prefix,sig]+=1
        phase=sum(i*j for i,j in edges)%3
        phases[prefix][phase]+=1
        cyclic+=len({w[i:]+w[:i] for i in range(m) if edges[i]==prefix})
        for v in range(3):
            cuts=sum(w[j]==v and counts[w[j-1],v]==1 and counts[v,w[(j+1)%m]]==1
                     for j in range(2,m))
            single+=cuts*(cuts-1)*(cuts-2)//6
    total=sum(map(norm3,phases.values()))
    included=sum(x*x for x in edge_hist.values())
    n=3**m
    assert total==n
    assert total-cyclic-single<0 and included>cyclic
    return dict(m=m,N=3,t=1,common_initial_edge_total=str(Fraction(total,n)),
                cyclic=str(Fraction(cyclic,n)),single_switch_positive=str(Fraction(single,n)),
                actual_negative_complement=str(Fraction(total-cyclic-single,n)),
                all_matching_edge_multisets_noncyclic=str(Fraction(included-cyclic,n)),
                all_other_edge_multisets=str(Fraction(total-included,n)))
print(json.dumps([run(7),run(9)],indent=2))
