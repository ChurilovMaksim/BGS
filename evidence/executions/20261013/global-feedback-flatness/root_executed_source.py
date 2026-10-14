"""Exact non-symmetric row-energy controls and finite small-gap diagnostics.
Bounded: size 16 exact, size 64 complex128, 90 s wall, one BLAS thread.
No asymptotic theorem or probability experiment is certified.
"""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
from pathlib import Path
from collections import Counter
from functools import lru_cache
import json
import sympy as sp
import numpy as np

w=sp.Symbol('w')

@lru_cache(None)
def row_integrals(a,terms,old):
    q=w/(1-a*w);qc=1/(w-a)
    expr=sp.cancel(sum(count*((x+q*z)*(x+qc*z))**2 for (x,z),count in terms))
    inc=sp.cancel(expr-old)
    result=[]
    for power in [1,2]:
        f=sp.cancel(inc**power/w)
        result.append(sp.simplify(sp.residue(f,w,0)+sp.residue(f,w,a)))
    return result


def exact_rows():
    n=16;s=sp.Matrix(n,n,lambda i,j:sp.Rational((-1)**((int(i)&int(j)).bit_count()),4))
    rot=sp.eye(n)
    for j in [0]:rot[j:j+2,j:j+2]=sp.Matrix([[sp.Rational(3,5),-sp.Rational(4,5)],[sp.Rational(4,5),sp.Rational(3,5)]])
    s=s*rot;assert s*s.T==sp.eye(n) and s!=s.T
    p=s.applyfunc(lambda x:x*x);delta=max(p);k=p*p;cases=[]
    for i in [0,3]:
        old=sum(p[i,j]**2 for j in range(n));positive=sum(p[i,j]*k[i,j] for j in range(n))
        buckets=[0]*6;mean=raw=0
        for e in range(n):
            terms=tuple(sorted(Counter((s[i,j],s[i,e]*s[e,j]) for j in range(n) if j!=e).items()))
            aa=bb=cc=dd=ff=0
            for j in range(n):
                if j==e:continue
                x=p[i,j];alpha=s[i,e]*s[e,j]*s[i,j];b=p[i,e]*p[e,j]
                aa+=2*x*alpha;bb+=4*x*b;cc+=alpha**2;dd+=2*alpha*b;ff+=b*b
            r=p[i,e]**2
            for z,coefficient in enumerate([r,aa,bb,cc,dd,ff]):buckets[z]+=coefficient**2
            if e==i:continue
            first,second=row_integrals(s[e,e],terms,old);mean+=first/n;raw+=second/n
            phase=sp.I;q=phase/(1-s[e,e]*phase)
            direct=sum(count*sp.simplify((x+q*z)*sp.conjugate(x+q*z))**2 for (x,z),count in terms)-old
            coeff=-r+q*aa+sp.conjugate(q*aa)+q*sp.conjugate(q)*bb+q*q*cc+sp.conjugate(q*q*cc)+q*q*sp.conjugate(q)*dd+sp.conjugate(q*q*sp.conjugate(q)*dd)+(q*sp.conjugate(q))**2*ff
            assert sp.simplify(direct-coeff)==0
        bounds=[delta**2*old,10*delta**2*old,16*delta**2*positive,delta**2*positive,4*delta**3*positive,delta**4*old]
        assert all(a<=b for a,b in zip(buckets,bounds))
        c=2*delta/(1-delta)**2+delta*(1+delta)/(1-delta)**3;d=4/(1-delta)+2*delta/(1-delta)**2
        assert n*mean<=-(1-c)*old+d*positive+p[i,i]**2
        assert raw<=3500*delta**2*(old+positive)/n
        cases.append({'row':i,'mean':str(sp.simplify(mean)),'raw_second':str(sp.simplify(raw)),'energy':str(old),'positive_scalar':str(positive),'coefficient_bound_ratios':[str(sp.simplify(a/b)) for a,b in zip(buckets,bounds)]})
    return {'n':n,'delta':str(delta),'nonsymmetric_scattering':True,'scope':'General drift and variance only; delta exceeds 1/16 and no small-gap drift is asserted here.','cases':cases,'cached_integrands':row_integrals.cache_info().currsize}


def small_gap_rows():
    n=64;s=np.array([[(-1)**((i&j).bit_count())/8 for j in range(n)] for i in range(n)],float)
    c,t=1599/1601,80/1601;rot=np.eye(n)
    for j in [0]:rot[j:j+2,j:j+2]=[[c,-t],[t,c]]
    s=s@rot;p=abs(s)**2;delta=float(p.max());rho=float(np.linalg.norm(p-np.ones((n,n))/n,2));assert delta<=1/16 and rho<=1/10
    rows=[]
    for matrix in [s,s.T]:
        pp=abs(matrix)**2
        for i in [0,7]:
            old=float(np.dot(pp[i],pp[i]));mean=raw=0;max_range_ratio=0
            for e in range(n):
                if e==i:continue
                keep=[j for j in range(n) if j!=e];a=matrix[e,e]
                for j in range(128):
                    phase=np.exp(2j*np.pi*(j+.31)/128);q=phase/(1-a*phase)
                    row=matrix[i,keep]+q*matrix[i,e]*matrix[e,keep]
                    inc=float(np.dot(abs(row)**2,abs(row)**2)-old)
                    mean+=inc/(128*n);raw+=inc*inc/(128*n)
                    max_range_ratio=max(max_range_ratio,abs(inc)/(8*delta*np.sqrt(old)+34*delta**2))
            target=-old/(3*n)+5/n**2+delta**2/n
            positive=float(np.dot(pp[i],(pp@pp)[i]));assert mean<=target+1e-13
            assert raw<=3500*delta**2*(old+positive)/n+1e-13 and max_range_ratio<=1+1e-12
            rows.append({'transpose':matrix is not s,'label':i,'quadrature_mean':mean,'quadrature_raw_second':raw,'range_ratio':max_range_ratio})
    return {'n':n,'delta':delta,'rho':rho,'phase_grid':128,'cases':rows,'non_claim':'Finite double quadrature is not a proof of the circle integral or stochastic tails.'}


def main():
    result={'exact_rows':exact_rows(),'small_gap_rows':small_gap_rows(),'non_claim':'Finite controls do not prove all-time flatness or BGS.'}
    Path('/workspace/scratch/06745ba532e4/research_session/row_feedback_energy_controls_20261013.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

if __name__=='__main__':main()
