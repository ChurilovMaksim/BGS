#!/usr/bin/env python3
"""Exact invariant-Hessian identity, sign-cone bound, and phase normalizations.

Symbolic polynomial identities use SymPy over Q. Other reported arithmetic is
integer/Gaussian-integer arithmetic. None of these checks proves BGS.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import random
import sympy as sp
from resonance_nondegeneracy_certificate import orbit_forms, orbit_key

def step(v,A):
    a,b,c,d=A
    return a*v[0]+b*v[1],c*v[0]+d*v[1]
def det(v,w): return v[0]*w[1]-v[1]*w[0]
def qa(v,A): return det(v,step(v,A))

def symbol_check():
    a,b,c,d,x,y,z,q,p=sp.symbols('a b c d x y z q p')
    g=(x*q*q+2*y*q*p+z*p*p)/2
    cg=g.subs({q:a*q+c*p,p:b*q+d*p},simultaneous=True)
    bracket=sp.expand(sp.diff(g,q)*sp.diff(cg,p)-sp.diff(g,p)*sp.diff(cg,q))
    computed=sp.expand(c*sp.diff(bracket,q,2)+(d-a)*sp.diff(bracket,q,p)-b*sp.diff(bracket,p,2))
    discriminant=(a+d)**2-4*(a*d-b*c)
    expected=(a+d)*((c*x+(d-a)*y-b*z)**2+discriminant*(x*z-y*y))
    assert sp.Poly(computed-expected,a,b,c,d,x,y,z).is_zero
    return {'identity':'L_Q{g,g composed with A^T}(0)=tr(A)*E_A(Hess(g)(0))','symbolic_remainder':'0','determinant_one_not_needed_for_this_algebraic_identity':True}

def cone_checks():
    rng=random.Random(20260906)
    matrices=((3,2,4,3),(2,1,1,1),(3,2,1,1),(1,2,2,5),(-3,-2,-4,-3))
    records=[]
    for A in matrices:
        a,b,c,d=A;t=a+d;Delta=t*t-4
        assert a*d-b*c==1 and abs(t)>2
        for radius in (1,2,3,4):
            modes=[(u,v) for u in range(radius+1) for v in range(-radius,radius+1) if u>0 or v>0]
            for positive in (False,True):
                for trial in range(5):
                    coeff=[rng.randint(0,3) if positive else rng.randint(-3,3) for _ in modes]
                    if not any(coeff):coeff[0]=1
                    M11=sum(k*v[0]**2 for v,k in zip(modes,coeff));M12=sum(k*v[0]*v[1] for v,k in zip(modes,coeff));M22=sum(k*v[1]**2 for v,k in zip(modes,coeff))
                    E=(c*M11+(d-a)*M12-b*M22)**2+Delta*(M11*M22-M12*M12)
                    weighted=0
                    for u,cu in zip(modes,coeff):
                        for v,cv in zip(modes,coeff):
                            w=step(v,A);D=det(u,w);minus=(u[0]-w[0],u[1]-w[1]);plus=(u[0]+w[0],u[1]+w[1])
                            weighted+=cu*cv*D*(qa(minus,A)-qa(plus,A))
                    assert weighted==-2*t*E
                    if positive:
                        lower=sum(k*abs(qa(v,A)) for k,v in zip(coeff,modes))**2
                        assert E>=lower>0
                    records.append({'A':list(A),'R':radius,'positive_coefficients':positive,'trial':trial,'E':E,'weighted_sum_over_pi':weighted})
    return records

def add(z,w):return z[0]+w[0],z[1]+w[1]
def mul(z,w):return z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0]
def conj(z):return z[0],-z[1]
def scale(a,z):return a*z[0],a*z[1]
def absolute_squared(z):return z[0]*z[0]+z[1]*z[1]

def oriented_window(v):
    def E(w):return 2*w[0]*w[0]+w[1]*w[1]
    w=v
    for _ in range(12):w=step(w,(3,-2,-4,3))
    values=[]
    for k in range(-12,13):values.append((E(w),w,k));w=step(w,(3,2,4,3))
    _,best,index=min(values);assert abs(index)<12
    assert E(best)<=E(step(best,(3,2,4,3))) and E(best)<=E(step(best,(3,-2,-4,3)))
    return best

def direct_full_fourier(modes,z):
    coeff={}
    for v,a in zip(modes,z):coeff[v]=a;coeff[(-v[0],-v[1])]=conj(a)
    raw=defaultdict(lambda:(0,0))
    for u,a in coeff.items():
        for v,b in coeff.items():
            w=step(v,(3,2,4,3));factor=-det(u,w)
            if factor:
                key=(u[0]+w[0],u[1]+w[1]);raw[key]=add(raw[key],scale(factor,mul(a,b)))
    sums=defaultdict(lambda:(0,0))
    for v,a in raw.items():
        if a!=(0,0):k=oriented_window(v);sums[k]=add(sums[k],a)
    return sum(absolute_squared(a) for a in sums.values())

def row_gamma(rows,z):
    result=0
    for row in rows:
        q=(0,0)
        for i,e,j,f,a in row['terms']:
            left=z[i] if e==1 else conj(z[i]);right=z[j] if f==1 else conj(z[j]);q=add(q,scale(a,mul(left,right)))
        result+=2*absolute_squared(q)
    return result

def phase_checks():
    rng=random.Random(706209);records=[]
    for R in (1,2,3):
        modes,rows=orbit_forms(R)
        for trial in range(12):
            z=[(rng.randint(-2,2),rng.randint(-2,2)) for _ in modes];exact=row_gamma(rows,z);independent=direct_full_fourier(modes,z);assert exact==independent
            records.append({'R':R,'trial':trial,'Gamma_over_pi_squared':exact})
    ties=[]
    for v in ((1,-1),(1,-2),(-1,2),(2,-4)):
        key,sg=orbit_key(v);other,negative=orbit_key((-v[0],-v[1]));assert key==other and sg==-negative;assert orbit_key(step(v,(3,2,4,3)))==(key,sg);ties.append({'v':list(v),'representative':list(key),'orientation':sg})
    modes,rows=orbit_forms(2);z=[(4 if v==(1,0) else -1 if v==(2,0) else 0,0) for v in modes];value=row_gamma(rows,z);assert value>0
    return records,ties,{'g':'4*b_(1,0)-b_(2,0)','Hessian_at_zero':'zero','Gamma_over_pi_squared':value}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);args=p.parse_args();phase,ties,negative=phase_checks()
    report={'status':'PASS','producer':'computations/verification/resonance_hessian_obstruction.py','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'symbolic':symbol_check(),'integer_hessian_cases':cone_checks(),'gaussian_integer_phase_cases':phase,'orientation_tie_controls':ties,'hessian_converse_negative_control':negative,'scope':'Exact polynomial/integer/Gaussian-integer identities only; no floating optimization or BGS inference.'}
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'status':report['status'],'hessian_cases':len(report['integer_hessian_cases']),'phase_cases':len(phase),'negative_control':negative},indent=2))
if __name__=='__main__':main()
