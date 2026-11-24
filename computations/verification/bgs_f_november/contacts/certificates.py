"""Exact arithmetic behind the norm estimates, overlap exponent and prime-power orders."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import json
from fractions import Fraction as F
from math import gcd
from itertools import combinations

# Conservative replacements exp(-.8)<1/2 and exp(-.8 sqrt(2))<1/3.
assert 1+F(4,5)+F(4,5)**2/2>2
x=F(4,5)*F(141,100)
assert sum(x**j/z for j,z in enumerate([1,1,2,6,24,120]))>3 and F(141,100)**2<2
low=20*sum(2*80*F(1,10**80)*2*b*6**21 for b in range(1,31))
high=20*2*F(1,3)**31/(1-F(1,3))
tail=2*F(1,3)/(1-F(1,3))*F(1,2)**20/(1-F(1,2))
total=low+high+tail
assert total<F(1,10**5)
assert 101*total < 1

# Counts for two matchings. Number of free vertex labels after selecting equalities.
def components(m, shift, edges1, edges2):
    parent=list(range(2*m))
    def root(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]]
            i=parent[i]
        return i
    for edges,off in [(edges1,0),(edges2,shift)]:
        for i in edges:
            parent[root(i)]=root(m+(i+off)%m)
    return len({root(i) for i in range(2*m)})
cases=0
for m in range(2,7):
    for shift in range(1,m):
        g=gcd(m,shift)
        for k in range(m+1):
            a=list(combinations(range(m),k))
            for a1 in a:
                for a2 in a:
                    free=components(m,shift,a1,a2)
                    assert free<=2*m-2*k+F(k*g,m)
                    cases+=1

def action(a,b,n):
    return (3*a+4*b)%n,(2*a+3*b)%n

def order_and_cycles(p,j):
    n=p**j
    todo={(a,b) for a in range(n) for b in range(n)}
    lengths={}
    while todo:
        v=next(iter(todo)); w=v; length=0
        while w in todo:
            todo.remove(w)
            length+=1
            w=action(*w,n)
        assert w==v
        lengths[length]=lengths.get(length,0)+1
    assert sum(lengths.values())==n
    assert max(lengths)==(p+1)*p**(j-1)
    return dict(N=n,cycles=sum(lengths.values()),lengths=lengths)
rows=[]
for p,js in [(3,range(1,6)),(5,range(1,4))]:
    a,b=1,0
    for i in range(1,p+2):
        a,b=action(a,b,p*p)
        assert ((a%p,b%p)==(1,0))==(i==p+1)
    assert (a,b)!=(1,0)
    rows.extend(order_and_cycles(p,j) for j in js)
print(json.dumps(dict(sum_classical_norms_upper=str(total),strict_threshold="1e-5",
                      graph_cases=cases,prime_power_orbits=rows),indent=2))
