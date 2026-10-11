"""Exact CSE trace controls by two independent calculations.

Route A: formal trace-log of weighted shifts.
Route B: Fourier constant coefficients of the full Vandermonde-fourth density.
No Jack recurrence is used in either route.
"""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import factorial
import json
from pathlib import Path
import sys

def mul(p,q):
    out=defaultdict(int)
    for e,a in p.items():
        for f,b in q.items():
            out[tuple(x+y for x,y in zip(e,f))]+=a*b
    return {e:c for e,c in out.items() if c}

def density(n):
    zero=(0,)*n
    poly={zero:1}
    for i in range(n):
        for j in range(i+1,n):
            e=[0]*n;e[i]=1;e[j]=-1;e=tuple(e)
            rev=tuple(-x for x in e)
            pair={zero:2,e:-1,rev:-1}
            poly=mul(poly,mul(pair,pair))
    assert poly[zero]==factorial(2*n)//2**n
    return poly

def direct_moment(N,n,degree,poly):
    numerator=0
    for positive in product(range(N),repeat=degree):
        for negative in product(range(N),repeat=degree):
            exponent=[0]*N
            for i in positive:exponent[i]+=n
            for i in negative:exponent[i]-=n
            numerator+=poly.get(tuple(-x for x in exponent),0)
    return F(numerator,poly[(0,)*N])

@lru_cache(None)
def trace_product(N,steps):
    # q=2k are odd integers. k -> k-s becomes q -> q-2s.
    allowed=set(range(1-2*N,2*N,2))
    total=F()
    for q0 in sorted(allowed):
        q=q0
        value=F(1)
        for s in steps:
            newq=q-2*s
            if newq not in allowed:
                value=F();break
            value*=F(q-s,q)
            q=newq
        if q==q0:total+=value
    return total

def compositions(a,b,length):
    if length==0:
        if a==0 and b==0:yield ()
        return
    for x in range(a+1):
        for y in range(b+1):
            if x+y==0:continue
            for rest in compositions(a-x,b-y,length-1):
                yield ((x,y),)+rest

def log_coefficient(N,n,a,b):
    total=F()
    mass=F()
    count=0
    for length in range(1,a+b+1):
        for composition in compositions(a,b,length):
            weight=F((-1)**(length+1),2*length)
            for x,y in composition:weight/=factorial(x)*factorial(y)
            steps=tuple((x-y)*n for x,y in composition)
            assert sum(steps)==(a-b)*n
            total+=weight*trace_product(N,steps)
            mass+=abs(weight);count+=1
    return total,mass,count

def mean_formula(N,n):
    if n>=2*N:return F(N)
    return F(n,2)+F(n,4)*sum(F(2,2*j+1)
        for j in range(abs(N-n),N))

def main(result_path):
    records=[]
    direct_cases=0
    shift_cases=0
    max_ratio=F()
    for N in (2,3,4):
        poly=density(N)
        for n in range(1,3*N+1):
            m2=direct_moment(N,n,1,poly)
            m4=direct_moment(N,n,2,poly)
            c2,_,_=log_coefficient(N,n,1,1)
            c4,mass,_=log_coefficient(N,n,2,2)
            assert mass==F(13,4)
            kappa=4*c4
            assert m2==c2==mean_formula(N,n)
            assert m4==2*m2*m2+kappa
            assert m4>=m2*m2
            assert abs(kappa)<=2600000*(N+n*n)
            direct_cases+=1
            records.append({"N":N,"n":n,"second":str(m2),"fourth":str(m4),
                "mixed_cumulant":str(kappa),"density_support":len(poly)})
    # Larger N and critical/supercritical times test denominators and clipping.
    for N in (5,8,16,32,64,128):
        times=sorted(set((1, max(1,N//2),N-1,N,N+1,2*N-1,2*N,3*N)))
        for n in times:
            c2,_,_=log_coefficient(N,n,1,1)
            c4,mass,_=log_coefficient(N,n,2,2)
            assert c2==mean_formula(N,n) and mass==F(13,4)
            kappa=4*c4
            assert abs(kappa)<=2600000*(N+n*n)
            assert 2*c2*c2+kappa>=c2*c2
            ratio=abs(kappa)/F(N+n*n)
            max_ratio=max(max_ratio,ratio)
            shift_cases+=1
    result={"all_passed":True,"arithmetic":"exact integer density; rational trace-log",
        "independent_density_cases":direct_cases,"larger_shift_cases":shift_cases,
        "density_N":[2,3,4],"density_trace_bound":"1<=n<=3N",
        "larger_N":[5,8,16,32,64,128],
        "larger_times":"1,floor(N/2),N-1,N,N+1,2N-1,2N,3N",
        "absolute_log_coefficient_mass":"13/4","max_tested_cumulant_ratio":str(max_ratio),
        "records":records,
        "non_claims":["Finite controls do not prove the general cumulant bound.",
                      "No deterministic chaotic propagator is tested."]}
    Path(result_path).write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:result[k] for k in ("all_passed","independent_density_cases",
        "larger_shift_cases","absolute_log_coefficient_mass","max_tested_cumulant_ratio")}))
if __name__=="__main__":main(sys.argv[1])

