"""Exact unit-orbit sums at moduli 49 and 343. The lifting proof is in section 8."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys,json
from pathlib import Path
from collections import defaultdict
from fractions import Fraction as F
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'research'))
from coefficients import raw_symbol
A=raw_symbol()
def run(n):
    m=3*n//7;groups=defaultdict(list);orb={};length={}
    for a,b in A:
        v=(a%n,b%n)
        if v not in orb:
            w=v;step=0
            while w not in orb:
                orb[w]=v;w=((3*w[0]+4*w[1])%n,(2*w[0]+3*w[1])%n);step+=1
            assert w==v
            length[v]=step
        groups[orb[v]].append((a,b))
    total=F()
    for rep,ds in groups.items():
        x,y=(sum(A[d][i] for d in ds) for i in (0,1))
        total+=F(m*(x*x+y*y),4000**2*length[rep])
        assert length[rep]==(m//7 if all(z%7==0 for z in rep) else m)
    return dict(N=n,coefficient=str(total),orbits=len(groups),joined=[ds for ds in groups.values() if len(ds)>1])
r=[run(n) for n in (49,343,2401)]
assert [x['coefficient'] for x in r]==['11370483/4000000','11370883/4000000','11370883/4000000']
assert A[(0,7)]==A[(0,-7)]==(1800,0) and len(A)==32
print(json.dumps(r,indent=1))
