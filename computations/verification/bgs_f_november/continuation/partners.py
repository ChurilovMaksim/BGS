"""Check the individual-word partner construction and its injectivity; no numerical phases."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from collections import Counter
from itertools import combinations, permutations,product
import json

def edges(w):
    return Counter(zip(w,w[1:]+w[:1]))
def turns(w):
    return Counter((w[j-1],x,w[(j+1)%len(w)]) for j,x in enumerate(w))
def canonical(w):
    return min(w[i:]+w[:i] for i in range(len(w)))
def reorder(w, cuts, order):
    starts=sorted(cuts); seq=w+w
    sections=[seq[a:b] for a,b in zip(starts,starts[1:]+[starts[0]+len(w)])]
    return tuple(x for j in order for x in sections[j])
def good_triples(w,t):
    marks=[]
    E=edges(w)
    for v in set(w):
        candidates=[j for j,x in enumerate(w) if x==v and j>t and
                    E[w[j-1],v]==1 and E[v,w[(j+1)%len(w)]]==1]
        marks.extend(combinations(candidates,3))
    images=set()
    for cuts in marks:
        y=reorder(w,cuts,(0,2,1))
        assert edges(w)==edges(y)
        erased=turns(w)-turns(y)
        decoded=sorted(next(j for j in range(len(w)) if (w[j-1],w[j])==(a,v)) for a,v,b in erased)
        assert tuple(decoded)==tuple(cuts)
        yw=canonical(y)
        assert yw!=canonical(w) and yw not in images
        images.add(yw)
        assert any((y+y)[j:j+t+1]==w[:t+1] for j in range(len(w)))
    return len(images)
example=(2,1,3,0,4,1,5,0,6,1,7,0,8,1,9,0)
count=good_triples(example,0)
images={canonical(example)}
for v in (0,1):
    result=set()
    for w in images:
        cuts=[j for j,x in enumerate(w) if x==v]
        for order in permutations(range(1,len(cuts))):
            out=canonical(reorder(w,cuts,(0,)+order))
            assert edges(out)==edges(w) and out not in result
            result.add(out)
    images=result
assert len(images)==36
cases=0;triples=0
for w in product(range(3),repeat=8):
    triples+=good_triples(w,1);cases+=1
print(json.dumps(dict(quadruple_visit_example_partners=len(images),single_triple_example=count,
                      exhaustive_small_words=cases,exhaustive_distinct_single_partners=triples),indent=2))
