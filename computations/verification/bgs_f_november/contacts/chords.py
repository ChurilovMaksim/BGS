"""Exact checks of the critical-window reconnections and unlabelled paths."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from math import factorial, prod
from itertools import product, permutations
from collections import Counter
import json

def match(vertices):
    if not vertices:
        yield []
        return
    a=vertices[0]
    for j,b in enumerate(vertices[1:],1):
        for rest in match(vertices[1:j]+vertices[j+1:]):
            yield [(a,b)]+rest

def one_cycle(perm):
    n=len(perm)
    j=perm[1 % n]; steps=1
    while j!=0:
        j=perm[(j+1)%n];steps+=1
    return steps==n

results=[]
for r in range(1,8):
    n=2*r; good=total=0
    for pairs in match(list(range(n))):
        p=list(range(n))
        for a,b in pairs:
            p[a],p[b]=p[b],p[a]
        good+=one_cycle(p);total+=1
    expected=0 if r%2 else total//(r+1)
    assert good==expected and total==prod(range(1,n,2))
    results.append(dict(r=r,matchings=total,connected=good))

words_checked=0
for length in range(1,6):
    for w in product(range(2),repeat=length+1):
        edges=Counter(zip(w,w[1:]))
        actual=sum(Counter(zip(z,z[1:]))==edges for inner in product(range(2),repeat=length-1)
                   for z in [(w[0],*inner,w[-1])])
        # edge 0 is artificial (w[-1] to w[0]); edges 1..L start at w[0..L-1].
        sources=(w[-1],*w[:-1])
        labelled=sum(one_cycle(p) for p in permutations(range(length+1))
                     if all(sources[i]==sources[p[i]] for i in range(length+1)))
        assert labelled==actual*prod(factorial(k) for k in edges.values())
        words_checked+=1
print(json.dumps(dict(matchings=results,rooted_words_checked=words_checked),indent=2))
