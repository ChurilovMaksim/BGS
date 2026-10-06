#!/usr/bin/env python3
"""Portable exact controls for the bounded growing-divisor exclusion.

Standard-library only; no floats, network, random choices, or file writes.
Finite polynomial/constant checks do not certify the analytic theorem.
All checks remain active under python -O; --inject-failure must exit nonzero.
"""
from fractions import Fraction as F
from math import factorial
import argparse
import json

class CheckFailure(RuntimeError):
    pass

def require(ok, label):
    if not ok:
        raise CheckFailure(label)

def ga(a=0,b=0):return (F(a),F(b))
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[0],-a[1])
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def power(a,n):
    out=ga(1)
    for _ in range(n):out=mul(out,a)
    return out
ZERO=ga();ONE=ga(1);I=ga(0,1)
def clean(p):return {k:c for k,c in p.items() if c!=ZERO}
def plus(p,q):
    r=dict(p)
    for k,c in q.items():r[k]=add(r.get(k,ZERO),c)
    return clean(r)
def scale(p,c):return clean({k:mul(v,c) for k,v in p.items()})
def times(p,q):
    r={}
    for (a,b),c in p.items():
        for (x,y),d in q.items():
            k=(a+x,b+y);r[k]=add(r.get(k,ZERO),mul(c,d))
    return clean(r)
def evaluate(p,z,w):
    out=ZERO
    for (a,b),c in p.items():out=add(out,mul(c,mul(power(z,a),power(w,b))))
    return out
PONE={(0,0):ONE}

def cosine(k):return {(k,0):ga(F(1,2)),(-k,0):ga(F(1,2))}
def actual_physical_symbol():
    c1,c7=cosine(1),cosine(7)
    r=times(plus(PONE,scale(c7,ga(-1))),plus(PONE,c1))
    sq={(1,0):ga(0,F(-1,2)),(-1,0):ga(0,F(1,2))}
    # Already includes the factor 1/100 from the p term of g.
    pterm={(0,1):ga(F(-3,1000),F(-4,1000)),(0,-1):ga(F(-3,1000),F(4,1000))}
    shifted={k:mul(c,ga(1 if k[0]%2==0 else -1)) for k,c in r.items()}
    out=plus(c7,scale(r,ga(F(1,10))))
    out=plus(out,scale(times(r,sq),ga(F(1,100))))
    out=plus(out,times(shifted,pterm))
    return plus(out,{(0,0):ga(F(-1,10))})

def make_filters():
    r=PONE
    for n in (2,5,6,7,8,9):r=times(r,{(0,0):ONE,(2,0):ga(F(1,n*n))})
    pq=times(times({(2,0):ONE,(1,0):neg(I)},r),{(0,0):ONE,(0,2):ONE})
    allq=times(r,{(0,0):ONE,(2,0):ONE})
    pp=times(allq,{(0,2):ONE,(0,1):neg(I)})
    return pq,pp

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inject-failure',action='store_true')
    args=parser.parse_args()
    g=actual_physical_symbol()
    require(len(g)==32,'32 physical Fourier modes')
    require((0,0) not in g,'centered physical symbol')
    require(all(g.get((-k,-l))==(c[0],-c[1]) for (k,l),c in g.items()),'real symbol')
    require(g[(1,0)]==ga(F(1,20),F(-1,200)),'primitive q coefficient')
    require(g[(0,1)]==ga(F(-3,1000),F(-4,1000)),'primitive p coefficient')
    moment=sum((abs(c[0])+abs(c[1]))*(k*k+l*l) for (k,l),c in g.items())
    require(moment==F(51451,1000),'exact Fourier moment')
    require(all(abs(k)+abs(l)<=10 for k,l in g),'strip support bound')
    qs=(0,1,-1,2,-2,5,-5,6,-6,7,-7,8,-8,9,-9)
    require(all(k in qs and l in (-1,0,1) for k,l in g),'rectangular support')
    filters=[]
    for p,target,multiplier in zip(make_filters(),((-1,0),(0,-1)),(ga(F(-4,3)),ga(-2))):
        require(max(a+b for a,b in p)==16,'filter total degree')
        require((0,0) not in p,'filter kills constants')
        require(all(c[0]==0 or c[1]==0 for c in p.values()),'pure real or imaginary coefficients')
        norm=sum(abs(c[0])+abs(c[1]) for c in p.values())
        require(norm==F(6409325,1143072) and norm<6,'filter exact l1 norm')
        hits=[]
        for k in qs:
            for l in (-1,0,1):
                val=evaluate(p,ga(0,k),ga(0,l))
                if (k,l)==target:require(val==multiplier,'selected multiplier')
                else:require(val==ZERO,'annihilated frequency')
                if val!=ZERO:hits.append([k,l])
        filters.append({'degree':16,'l1':str(norm),'hits':hits,'multiplier':[str(x) for x in multiplier]})
    normalized=[F(6*2*2500000*factorial(j+1)*400**(j+1),6**j) for j in range(17)]
    ordinary=[2*2500000*factorial(j+1)*400**(j+1) for j in range(18)]
    require(max(normalized)<10**55,'translated normalized remainder all orders 0..16')
    require(max(ordinary)<10**70,'translated ordinary remainder all orders 0..17')
    require(2*1000*100**18+F(10**70,10**80)<10**40,'normalized C17 upper bound')
    require(F(4,25)-F(1,10**25)>F(6,100),'finite type signal after remainder')
    ne,de=F(-32,129),F(-1,129)
    require(ne/32==F(-1,129) and (1+de)/32==F(4,129),'bad-set sqrt area exponents')
    require(-1-4*ne==F(-1,129) and -4*de==F(4,129),'good-set product exponents')
    require(-2-3*ne==F(-162,129) and -3*de==F(3,129),'alias tail exponents')
    require(2+F(4,129)==F(262,129),'whole span d squared loss')
    require(F(1,129)-F(262,129)*F(1,524)==F(1,258),'explicit delta rate')
    if args.inject_failure:require(False,'deliberate fault injection')
    print(json.dumps({'status':'passed','arithmetic':'exact rational Gaussian coefficients; standard library','physical_modes':len(g),'Fourier_moment':str(moment),'filters':filters,'translated_remainder_orders':[16,17],'max_filtered_remainder_prefactor':str(max(normalized)),'max_ordinary_remainder_prefactor':str(max(ordinary)),'compression_bound':'C_tau (d^262/N)^(1/129)','delta_range':'delta < 1/262','example_delta':'1/524','scope':'finite coefficients/filter/constants/exponents only; no analytic formal certification'},indent=2))

if __name__=='__main__':main()
