#!/usr/bin/env python3
"""Finite reference-only checks; no random Schur or BGS law is tested.

Exact polynomial calculations and separate 60-digit density quadrature.
The atom at x is included explicitly; x=1/2 tests the pole/edge merger.
"""
from __future__ import annotations
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
from math import comb
import argparse
import json
from pathlib import Path
import mpmath as mp
import sympy as sp


def compositions(total, parts):
    if parts==1:
        yield (total,)
    else:
        for first in range(1,total-parts+2):
            for tail in compositions(total-first,parts-1):
                yield (first,*tail)


def exact_reference_polynomials():
    x = sp.symbols('x')
    f = [sp.Integer(1)]
    for k in range(1, 9):
        value = sum(sp.Rational(comb(k,a)*comb(k,b)*comb(2*k-2-a-b,k-1-a-b),k)*(-x)**b
                    for a in range(k) for b in range(k-a))
        f.append(sp.expand(value))
        if k>1:
            recursive = ((1-x)*f[k-1]
                         +sum(f[a]*f[k-a] for a in range(1,k))
                         -x*sum(f[a]*f[k-1-a] for a in range(1,k-1)))
            assert sp.expand(value-recursive)==0
        forcing = sum(sp.Rational(k,q)*sum(sp.prod(f[a] for a in gaps)
                                           for gaps in compositions(k,2*q))
                      for q in range(1,k//2+1))
        # Independent positive-gap count for the repaired entry forcing.
        merged = sum(2*sp.prod(f[a] for a in gaps[1:-1])*f[gaps[0]+gaps[-1]]
                     for q in range(1,k//2+1) for gaps in compositions(k,2*q+1))
        one_boundary = sum(2*sp.prod(f[a] for a in gaps)
                           for q in range(1,k//2+1) for gaps in compositions(k,2*q))
        assert sp.expand(merged+one_boundary-forcing)==0
        assert sp.expand(-x*sp.diff(value,x)+(k-1)*value-forcing)==0
        assert value.subs(x,1)==1
    assert [v.subs(x,0) for v in f[1:]]==[1,2,6,22,90,394,1806,8558]
    return x,f


def density_controls(x_symbol, polynomials):
    mp.mp.dps=60
    samples=[sp.Rational(0),sp.Rational(1,5),sp.Rational(49,100),sp.Rational(1,2),
             sp.Rational(51,100),sp.Rational(4,5),sp.Rational(99,100),sp.Rational(1)]
    maximum=mp.mpf(0)
    count=0
    for exact_x in samples:
        x=mp.mpf(str(sp.numer(exact_x)))/int(sp.denom(exact_x))
        atom=mp.mpf(0) if x<=mp.mpf('0.5') else 2-1/x
        da=(mp.sqrt(2*(1-x))-1)**2
        width=4*mp.sqrt(2*(1-x))
        for r in range(5):
            def integrand(theta):
                half=mp.sin(theta/2)**2
                h=x+da+width*half
                if x==mp.mpf('0.5'):
                    weight=width*mp.cos(theta/2)**2/(2*mp.pi*h)
                else:
                    weight=width**2*mp.sin(theta)**2/(8*mp.pi*h*(da+width*half))
                return h**r*weight
            continuous=mp.mpf(0) if x==1 else mp.quad(integrand,[0,mp.pi/2,mp.pi])
            observed=continuous+atom*x**r
            expected_exact=polynomials[r].subs(x_symbol,exact_x)
            expected=mp.mpf(str(sp.numer(expected_exact)))/int(sp.denom(expected_exact))
            error=abs(observed-expected)
            maximum=max(maximum,error)
            assert error<mp.mpf('1e-35'),(str(exact_x),r,str(error))
            count+=1
    return {'arithmetic':'60-digit mpmath quadrature, diagnostic only',
            'retained_fractions':[str(x) for x in samples], 'orders':[0,1,2,3,4],
            'density_and_atom_moment_checks':count,'maximum_absolute_error':mp.nstr(maximum,12)}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    x,f=exact_reference_polynomials()
    result={'status':'PASS','exact_arithmetic':'SymPy rational polynomial arithmetic',
            'exact_reference_orders':list(range(1,9)),
            'polynomials':[str(v) for v in f[1:]],'density_diagnostics':density_controls(x,f),
            'non_claims':['Numerical quadrature is not a certified integral bound',
                          'No stochastic Schur asymptotic theorem is tested',
                          'No flatness probability, freeness of actual matrices, or BGS law']}
    serialized=json.dumps(result,indent=2)+'\n'
    if args.output:
        with args.output.open('x',encoding='utf-8') as stream:
            stream.write(serialized)
    print(serialized,end='')


if __name__=='__main__':
    main()
