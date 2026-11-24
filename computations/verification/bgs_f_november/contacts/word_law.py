"""Exact enumeration of equality types and alternative vertex words for a uniform chain."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from collections import Counter
from math import comb
import json

def patterns(n, prefix=(0,), largest=0):
    if len(prefix) == n:
        yield prefix
        return
    for v in range(largest+2):
        yield from patterns(n,prefix+(v,),max(largest,v))

def alternatives(w):
    arcs=Counter(zip(w,w[1:]))
    out={a: {b for s,b in arcs if a==s} for a in w}
    def count(a, left):
        if not left:
            return int(a==w[-1])
        val=0
        for b in out[a]:
            if arcs[a,b]:
                arcs[a,b]-=1
                val+=count(b,left-1)
                arcs[a,b]+=1
        return val
    return count(w[0],len(w)-1)-1

rows=[]
for n in range(3,10):
    types=0
    excess_by_distinct=[0]*(n+1)
    for w in patterns(n):
        types+=1
        excess_by_distinct[max(w)+1]+=alternatives(w)
    assert excess_by_distinct[-2:]==[0,0]
    assert excess_by_distinct[n-2]==comb(n+1,4)-comb(n-1,2)
    rows.append(dict(vertices=n,types=types,first_coefficient=excess_by_distinct[n-2],
                     falling_factorial_coefficients=excess_by_distinct))
print(json.dumps(rows,indent=2))
