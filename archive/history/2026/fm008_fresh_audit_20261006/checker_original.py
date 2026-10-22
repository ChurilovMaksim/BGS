#!/usr/bin/env python3
"""Independent FM008 finite controls; no imports from project verifiers.
Exact checks support the written derivation, not the all-N theorem.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import gcd, comb
from pathlib import Path
from collections import defaultdict
import hashlib, json
import sympy as s

ROOT=Path(__file__).resolve().parent

def vroot(n,d):
    order=n//gcd(n,d)
    if order==1: raise ValueError('zero root difference')
    b=0
    while order%5==0: order//=5;b+=1
    return Q(1,4*5**(b-1)) if order==1 else Q(0)

def valuation_controls():
    formula_cases=bond_cases=0
    mininc=Q(1);maxrho=Q(0)
    for n in range(3,502,2):
        a=0;M=n
        while M%5==0: a+=1;M//=5
        h=pow(2,-1,n)
        cuts=[x for x in range(n) if 7*(x+h)%n==0]
        assert len(cuts)==gcd(n,7)
        for d in range(1,n):
            lhs=vroot(n,d)
            rhs=Q(0)
            if a and d%M==0:
                rhs=Q(1,4*5**(a-1))+sum((Q(5)**(k-a) for k in range(1,a) if d%5**k==0),Q(0))
            assert lhs==rhs;formula_cases+=1
        if n%7:
            x0=(cuts[0]+1)%n
            path=[(x0+j)%n for j in range(n)]
            for j in range(n-1):
                d=(path[j]+h)%n
                rho=2*vroot(n,7*d)
                assert 0<=rho<=Q(1,2)
                inc=Q(3,4)-rho
                assert Q(1,4)<=inc<=Q(3,4)
                assert Q(1,2)+2*rho>0
                mininc=min(mininc,inc);maxrho=max(maxrho,rho);bond_cases+=1
    return dict(dimensions=list(range(3,502,2)),root_formula_cases=formula_cases,path_bonds=bond_cases,max_rho=str(maxrho),min_D_increment=str(mininc))

def balances():
    # Enumerate all subset sizes at four complete dimensions; selected ranks
    # are explicitly bounded in higher 5-primary or mixed-tame examples.
    scopes=[(3,range(4)),(5,range(6)),(9,range(10)),(15,range(16)),(25,range(6)),(75,range(4)),(125,range(4))]
    count=0; details=[]
    for n,ranks in scopes:
        a=0;M=n
        while M%5==0:a+=1;M//=5
        vr={d:vroot(n,d) for d in range(1,n)}
        for r in ranks:
            lower=sum((Q(r-d)*vr[d] for d in range(1,r)),Q(0))
            for I in combinations(range(n),r):
                actual=sum((vr[y-x] for x,y in combinations(I,2)),Q(0))
                assert actual>=lower
                # Independently count occupancy and compare convex minimum.
                for modulus in [M*5**k for k in range(a)]:
                    occ=[0]*modulus
                    for x in I:occ[x%modulus]+=1
                    pairs=sum(c*(c-1)//2 for c in occ)
                    q,b=divmod(r,modulus)
                    best=(modulus-b)*q*(q-1)//2+b*(q+1)*q//2
                    assert pairs>=best
                count+=1
            assert sum((vr[y-x] for x,y in combinations(range(n-r,n),2)),Q(0))==lower
        details.append(dict(N=n,ranks=list(ranks),subsets=sum(comb(n,r) for r in ranks)))
    return dict(scopes=details,subsets=count)

z=s.symbols('z');I=s.I

def ladd(a,b):
    c=dict(a)
    for k,v in b.items():c[k]=s.expand(c.get(k,0)+v)
    return {k:v for k,v in c.items() if v!=0}
def lscale(a,c):return {k:s.expand(v*c) for k,v in a.items()}
def lmul(a,b):
    c={}
    for (q,p),v in a.items():
        for (q1,p1),w in b.items():c[(q+q1,p+p1)]=s.expand(c.get((q+q1,p+p1),0)+v*w)
    return {k:v for k,v in c.items() if v!=0}

def model_controls():
    c7={(7,0):s.Rational(1,2),(-7,0):s.Rational(1,2)}
    c1={(1,0):s.Rational(1,2),(-1,0):s.Rational(1,2)}
    sin={(1,0):1/(2*I),(-1,0):-1/(2*I)}
    r=lmul(ladd({(0,0):1},lscale(c7,-1)),ladd({(0,0):1},c1))
    cpa={(0,1):(-3-4*I)/10,(0,-1):(-3+4*I)/10}
    f=ladd(ladd(ladd(c7,lscale(r,s.Rational(1,10))),lscale(lmul(r,sin),s.Rational(1,100))),lscale(lmul(r,cpa),s.Rational(1,100)))
    f=ladd(f,{(0,0):-s.Rational(1,10)})
    rpoly=sum(v*z**q for (q,p),v in r.items())
    assert s.simplify(rpoly+(z**7-1)**2*(z+1)**2/(4*z**8))==0
    cases=[]
    for n in [3,5,9,15,25,35,49]:
        h=pow(2,-1,n);phi=s.Poly(s.cyclotomic_poly(n,z),z,domain=s.QQ_I)
        def red(v):return s.Poly(s.expand(v),z,domain=s.QQ_I).rem(phi).as_expr()
        def ev(poly,x):return sum(v*z**((q*x)%n) for (q,p),v in poly.items())
        raw=[[0]*n for _ in range(n)]
        for (q,p),v in f.items():
            for x in range(n):raw[x][(x+p)%n]+=v*z**((q*(x+h*p))%n)
        for x in range(n):
            for y in range(n):
                expected=0
                if y==x:expected=ev(c7,x)+ev(r,x)/10+ev(r,x)*ev(sin,x)/100-s.Rational(1,10)
                elif y==(x+1)%n:expected=(-3-4*I)*ev(r,x+h)/1000
                elif y==(x-1)%n:expected=(-3+4*I)*ev(r,x-h)/1000
                assert red(raw[x][y]-expected)==0,(n,x,y)
        # Arithmetic kernel identity after the single-cut cyclic path ordering.
        if n%7:
            x0=(1-h)%n;k=pow(8,-1,n);cross=pow(4,-1,n)
            for j in range(n):
                for l in range(n):
                    x=(x0+j)%n;y=(x0+l)%n
                    raw_exp=-k*(3*x*x-2*x*y+3*y*y)
                    # constant + row-only + column-only + jl term
                    fact_exp=-4*k*x0*x0-4*k*x0*(j+l)-3*k*(j*j+l*l)+cross*j*l
                    assert (raw_exp-fact_exp)%n==0
        cases.append(dict(N=n,entry_equalities=n*n,cut_count=gcd(n,7)))
    return dict(raw_Fourier_modes=len(f),r_factorization=True,cases=cases)

def extremal_weight_controls():
    checked=0
    for n,maxrank in [(3,3),(5,5),(9,9),(15,5),(25,4),(75,3),(125,3)]:
        h=pow(2,-1,n);x0=(1-h)%n
        weights=[Q(0)]
        for j in range(n-1):
            rho=2*vroot(n,7*((x0+j+h)%n))
            weights.append(weights[-1]+Q(3,4)-rho)
        for r in range(maxrank+1):
            lo=sum(weights[:r],Q(0));hi=sum(weights[n-r:],Q(0)) if r else Q(0)
            for idx in combinations(range(n),r):
                w=sum((weights[j] for j in idx),Q(0))
                assert w>=lo and w<=hi
                assert (w==lo)==(idx==tuple(range(r)))
                assert (w==hi)==(idx==tuple(range(n-r,n)))
                checked+=1
    # Negative control: a composite Fourier position minor really can vanish.
    phi=s.Poly(s.cyclotomic_poly(9,z),z)
    positional_minor=s.det(s.Matrix([[z**((i*j)%9) for j in (0,3)] for i in (0,3)]))
    assert s.Poly(positional_minor,z).rem(phi).is_zero
    return dict(subset_weight_tests=checked,zero_position_basis_minor='F9 rows (0,3), columns (0,3); exact zero')

def alternant_controls():
    # A synthetic integral Jordan degeneration independently checks the
    # polynomial division/reduction and the left/right orientation. This is
    # expressly not an actual-model spectral certification.
    xs=s.symbols('x0:3');X=s.symbols('X');t=s.symbols('t')
    report=[]
    for n in range(2,7):
        diag=[t*(j+1) for j in range(n)]
        low=[t*(j+2) for j in range(n-1)]
        phi=[s.Integer(1)]
        for j in range(n-1):phi.append(s.expand((X-diag[j])*phi[j]-(low[j-1]*phi[j-1] if j else 0)))
        psi=[None]*n;psi[-1]=s.Integer(1)
        for j in range(n-1,0,-1):psi[j-1]=s.expand((X-diag[j])*psi[j]-(low[j]*psi[j+1] if j<n-1 else 0))
        checked=0
        for r in range(1,min(n,3)+1):
            delta=s.prod(xs[b]-xs[a] for a in range(r) for b in range(a+1,r))
            for idx in combinations(range(n),r):
                for polys,left in [(phi,False),(psi,True)]:
                    det=s.det(s.Matrix([[polys[j].subs(X,xs[k]) for k in range(r)] for j in idx]))
                    quotient,rem=s.div(det,delta,*xs[:r],t)
                    assert rem==0
                    reduction=quotient.subs({t:0,**{x:0 for x in xs[:r]}})
                    target=(-1)**(r*(r-1)//2) if left and idx==tuple(range(n-r,n)) else (1 if not left and idx==tuple(range(r)) else 0)
                    assert reduction==target,(n,r,idx,left,reduction,target)
                    checked+=1
        report.append(dict(N=n,alternants=checked))
    return dict(scopes=report,total=sum(x['alternants'] for x in report))

if __name__=='__main__':
    result={'scope':'Independent exact finite controls, not a universal proof. No author checker imports.','valuation':valuation_controls(),'balanced_residues':balances(),'actual_model':model_controls(),'alternants':alternant_controls(),'unique_corner':extremal_weight_controls()}
    result['status']='PASS'
    (ROOT/'independent_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
