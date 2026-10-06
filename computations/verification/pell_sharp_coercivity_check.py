#!/usr/bin/env python3
"""Exact and independent finite checks of the sharp single-orbit problem.

The proof uses Fejer--Riesz to realize its minimizing autocorrelations.
Integer/Fraction computations below check its algebra independently; mpmath
root solving checks sample spectral factors but is not an existence proof.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import argparse
from collections import defaultdict
from fractions import Fraction as Q
import hashlib
from itertools import product
import json
from pathlib import Path
import subprocess
import sys
import mpmath as mp


DEFAULT = (3,2,4,3)
def step(v, mat=DEFAULT):
    a,b,c,d=mat
    return (a*v[0]+b*v[1],c*v[0]+d*v[1])
def back(v, mat=DEFAULT):
    a,b,c,d=mat
    return (d*v[0]-b*v[1],-c*v[0]+a*v[1])
def det(v,w): return v[0]*w[1]-v[1]*w[0]
def sign(v): return min(v,(-v[0],-v[1]))
def energy(v): return 2*v[0]*v[0]+v[1]*v[1]


def orbit_key(v, mat=DEFAULT):
    if v==(0,0): raise ValueError('zero frequency')
    v=sign(v)
    for _ in range(1000):
        options=[v,sign(step(v,mat)),sign(back(v,mat))]
        best=min(options,key=lambda w:(energy(w),w))
        if best==v: return v
        v=best
    raise RuntimeError('orbit descent failed')


def direct_gamma(v,c, mat=DEFAULT):
    # Compute the entire Fourier polynomial {g,Cg}/(4*pi^2), then orbit-reduce.
    vv=[v]
    for _ in range(len(c)): vv.append(step(vv[-1],mat))
    h=defaultdict(int)
    for j,cj in enumerate(c):
        for k,ck in enumerate(c):
            z=cj*ck*det(vv[j],vv[k+1])
            if z==0: continue
            minus=(vv[j][0]-vv[k+1][0],vv[j][1]-vv[k+1][1])
            plus=(vv[j][0]+vv[k+1][0],vv[j][1]+vv[k+1][1])
            h[sign(minus)]+=z
            h[sign(plus)]-=z
    orbits=defaultdict(int)
    for w,z in h.items():
        if z: orbits[orbit_key(w,mat)]+=z
    return 2*sum(z*z for z in orbits.values())


def autocorr(c):
    return [sum(c[j]*c[j+k] for j in range(len(c)-k)) for k in range(len(c))]


def d_sequence(v,upto,mat=DEFAULT):
    w=v;out=[0]
    for _ in range(upto):
        w=step(w,mat);out.append(det(v,w))
    return out


def formula_gamma(v,c,mat=DEFAULT):
    corr=autocorr(c)+[0,0]
    ds=d_sequence(v,len(c)+1,mat)
    return 4*sum(ds[r]**2*(corr[r-1]-corr[r+1])**2 for r in range(1,len(c)+1))


def optimal_correlations(v,m,mat=DEFAULT):
    ds=d_sequence(v,2*m+1,mat)
    inv=[Q(1,ds[2*k+1]**2) for k in range(m+1)]
    total=sum(inv)
    a=[sum(inv[k:])/total for k in range(m+1)]+[Q(0)]
    # Dirichlet energy certificate, exact rational arithmetic.
    e=sum(ds[2*k+1]**2*(a[k]-a[k+1])**2 for k in range(m+1))
    assert e==1/total and a[0]==1
    # Explicit strict positive definiteness: |sum nonconstant terms| < 1.
    assert 2*sum(a[1:])<1
    return total,a[:-1],4/total


def exact_controls():
    rows=[]
    for v in ((1,0),(0,1),(1,1)):
        for c in product((-1,0,1),repeat=5):
            if not any(c): continue
            direct=direct_gamma(v,c)
            formula=formula_gamma(v,c)
            assert direct==formula
            c0=sum(x*x for x in c)
            lo=min(j for j,x in enumerate(c) if x)
            hi=max(j for j,x in enumerate(c) if x)
            total,_,_=optimal_correlations(v,(hi-lo)//2)
            assert Q(formula)>=4*c0*c0/total
            rows.append([*v,*c,direct])
    rational=[]
    for m in range(9):
        total,a,opt=optimal_correlations((1,0),m)
        rational.append({'M':m,'S_M':str(total),'optimal_Gamma_over_pi_squared':str(opt),
                         'correlations':[str(x) for x in a]})
    return rows,rational


def numerical_factors():
    result=[]
    with mp.workdps(100):
        for m in (0,1,2,3,5,7):
            total,aq,opt=optimal_correlations((1,0),m)
            a=[mp.mpf(x.numerator)/x.denominator for x in aq]
            if m==0: b=[mp.mpf(1)]
            else:
                def equations(*b):
                    return tuple(sum(b[j]*b[j+k] for j in range(m+1-k))-a[k] for k in range(m+1))
                root=mp.findroot(equations,tuple([mp.mpf(1)]+a[1:]),tol=mp.mpf('1e-90'),maxsteps=40)
                b=list(root)
            c=[mp.mpf(0)]*(2*m+1)
            c[::2]=b
            error=max(abs(sum(b[j]*b[j+k] for j in range(m+1-k))-a[k]) for k in range(m+1))
            expected=mp.mpf(opt.numerator)/opt.denominator
            actual=formula_gamma((1,0),c)
            assert error<mp.mpf('1e-80')
            assert abs(actual-expected)<mp.mpf('1e-65')
            result.append({'M':m,'factor_coefficients':[mp.nstr(x,65) for x in b],
                           'autocorrelation_residual':mp.nstr(error,10),
                           'objective_residual':mp.nstr(abs(actual-expected),10)})
        lam=3+2*mp.sqrt(2)
        ds=d_sequence((1,0),121)
        sm=sum(mp.mpf(1)/(ds[2*k+1]**2) for k in range(60))
        tail=1/(mp.mpf(16))*lam**(-240)/(1-lam**-4)
        # Monotonic inversion supplies a rigorous tail bracket in exact real
        # arithmetic; displayed decimals are not interval-certified rounding.
        ratio=1/(16*sm)
        constant={'ratio_to_one_mode':mp.nstr(ratio,70),
                  'sum_terms':60,'analytic_tail_bound_S':mp.nstr(tail,15),
                  'finite_M1_ratio':'1225/1226',
                  'rounding':'100 decimal arithmetic, not outward interval rounding'}
    return result,constant



def other_maps():
    summary=[]
    for mat in ((2,1,1,1),(3,1,2,1),(1,2,2,5)):
        assert mat[0]*mat[3]-mat[1]*mat[2]==1
        checks=0
        for v in ((1,0),(0,1),(1,1)):
            for c in product((-1,0,1),repeat=4):
                if not any(c): continue
                direct=direct_gamma(v,c,mat)
                formula=formula_gamma(v,c,mat)
                assert direct==formula
                first=min(j for j,x in enumerate(c) if x)
                last=max(j for j,x in enumerate(c) if x)
                total,_,_=optimal_correlations(v,(last-first)//2,mat)
                assert Q(formula)>=4*sum(x*x for x in c)**2/total
                checks+=1
        total,_,minimum=optimal_correlations((1,0),1,mat)
        summary.append({'matrix':list(mat),'exact_checks':checks,'M1_Gamma_over_pi_squared':str(minimum)})
    return summary

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cpp',type=Path)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    rows,rational=exact_controls()
    cpp_status='NOT_RUN'
    if args.cpp:
        text=subprocess.check_output([str(args.cpp.resolve())],text=True,timeout=25)
        cpp=json.loads(text)
        assert cpp['rows']==rows
        cpp_status='PASS'
    factors,constant=numerical_factors()
    report={'producer':'computations/verification/pell_sharp_coercivity_check.py','status':'PASS','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope':'Exact finite polynomial/orbit checks and rational energy identities; numerical sample factors are not the general Fejer--Riesz proof.',
            'cpp_crosscheck':cpp_status,'exact_cases':len(rows),'exact_rows':rows,'other_hyperbolic_maps':other_maps(),
            'rational_optimizers':rational,'sample_factors':factors,'sharp_constant':constant}
    text=json.dumps(report,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text)
    else:
        print(text,end='')
    print('PASS:',len(rows),'exact cases; sample factors:',len(factors),'C++:',cpp_status,file=sys.stderr)
    print('sharp ratio',constant['ratio_to_one_mode'],file=sys.stderr)

if __name__=='__main__': main()
