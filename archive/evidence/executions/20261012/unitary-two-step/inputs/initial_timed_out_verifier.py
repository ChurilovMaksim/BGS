#!/usr/bin/env python3
"""Finite controls for a static unistochastic obstruction, not Schur evolution."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
from math import log, sqrt
from pathlib import Path
import argparse
import json
import numpy as np
import sympy as sp

def exact_unitary(n, seed):
    z=sp.eye(n)
    for k in range(1,n):
        a,b=(sp.Rational(3,5),sp.Rational(4,5)) if (k+seed)%2 else (sp.Rational(5,13),sp.Rational(12,13))
        r=sp.eye(n);r[0,0]=r[k,k]=a;r[0,k]=b;r[k,0]=-b;z=z*r
    return z*sp.diag(*[sp.I**((k+seed)%4) for k in range(n)])

def exact_correction(c,d):
    if c==d:return sp.eye(c.rows)
    v=c-d
    return (sp.eye(c.rows)-v*v.conjugate().T/(1-(d.conjugate().T*c)[0])).applyfunc(sp.simplify)

def exact_controls():
    cases=0
    for n in (8,12):
        for seed in (0,1):
            z=exact_unitary(n,seed);eye=sp.eye(n);a=sp.zeros(n,1);a[2:6,0]=sp.ones(4,1)/2
            left=exact_correction(z[:,1],a);w=(left*z).applyfunc(sp.simplify)
            r=w.conjugate().T[:,0];right=exact_correction(a,r);s=(w*right).applyfunc(sp.simplify)
            assert (z.conjugate().T*z).applyfunc(sp.simplify)==eye
            assert (s.conjugate().T*s).applyfunc(sp.simplify)==eye
            assert s[:,1]==a and s.conjugate().T[:,0]==a
            assert (s-z).rank()<=2
            p=s.applyfunc(lambda v:sp.simplify(v*sp.conjugate(v)))
            assert (p*p)[0,1]==sp.Rational(1,4)
            cases+=1
    n=sp.symbols('n',positive=True)
    den=(n+1)*(n+2)*(n+3)
    es2=2/(n+1);es3=6/((n+1)*(n+2));es22=4*(n+5)/den
    moment=sp.factor(n*es22+(1-es2-2*es3+2*es22)-1)
    expected=2*(n-1)*(n+4)/den
    assert sp.cancel(moment-expected)==0
    assert expected.subs(n,2)==sp.Rational(1,5)
    return {'Gaussian_rational_unitary_fixtures':cases,'dimensions':[8,12],
            'support_size':4,'exact_two_step_peak':'1/4',
            'Haar_fourth_Schatten_polynomial':str(moment),
            'coverage':'Exact finite construction, rank, unitarity and algebraic moment combination; no probability theorem is tested.'}

def correction(c,d):
    v=c-d
    if np.linalg.norm(v)<1e-14:return np.eye(c.size,dtype=complex)
    return np.eye(c.size)-np.outer(v,v.conj())/(1-np.vdot(d,c))

def numerical_controls():
    rng=np.random.default_rng(20261011);rows=[]
    for n in (32,64,128):
        for trial in range(2):
            g=(rng.standard_normal((n,n))+1j*rng.standard_normal((n,n)))/sqrt(2)
            z,r=np.linalg.qr(g);z=z*(np.diag(r)/np.abs(np.diag(r))).conj()
            b=int(n/log(2*n));a=np.zeros(n,dtype=complex);a[2:2+b]=1/sqrt(b)
            w=correction(z[:,1],a)@z;s=w@correction(a,w.conj().T[:,0])
            p=np.abs(s)**2
            unitarity=np.linalg.norm(s.conj().T@s-np.eye(n),ord=2)
            assert unitarity<1e-11
            assert abs((p@p)[0,1]-1/b)<1e-11
            singular=np.linalg.svd(s-z,compute_uv=False)
            assert singular[2]<1e-11
            rows.append({'n':n,'support_size':b,'max_intensity':float(p.max()),
                         'centered_intensity_operator_norm':float(np.linalg.norm(p-1/n,ord=2)),
                         'n_times_two_step_peak':float(n*(p@p)[0,1]),
                         'unitarity_error':float(unitarity)})
    return {'arithmetic':'float64 diagnostic only','seed':20261011,'cases':rows}

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path);args=parser.parse_args()
    result={'status':'PASS','exact':exact_controls(),'numerical':numerical_controls(),
            'non_claims':['No finite check proves the asymptotic existence theorem','No random Schur trajectory or flatness probability is tested','No chaotic quantizer or BGS counterexample is constructed','No world priority claim']}
    s=json.dumps(result,indent=2)+'\n'
    if args.output:
        with args.output.open('x',encoding='utf-8') as f:f.write(s)
    print(s,end='')
if __name__=='__main__':main()
