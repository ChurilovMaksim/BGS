#!/usr/bin/env python3
"""Exact finite algebra and independent controls for the Heisenberg-note audit.

SymPy rational/complex Laurent algebra; Fraction digit tests; complex128
matrix checks. No source theorem, asymptotic cancellation, nonlinear FIO,
Planck-scale FUP, CUE universality, or priority claim is certified by this run.
Resource caps: matrices N<=32, factorial cycles k<=5, integer digit side
length <=4096; no Monte Carlo.
"""

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import argparse
import hashlib
import importlib.util
import itertools
import json
import math
import platform
from fractions import Fraction
from pathlib import Path

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]


def symbol_check():
    z, w = sp.symbols('z w', nonzero=True)
    cos = lambda n: (z**n + z**(-n))/2
    sin = lambda n: (z**n - z**(-n))/(2*sp.I)
    r = sp.expand((1-cos(7))*(1+cos(1)))
    cp = ((-3-4*sp.I)*w+(-3+4*sp.I)/w)/10
    g = sp.expand(cos(7)+r/10+r*sin(1)/100-sp.Rational(1,10)
                  +r.subs(z,-z)*cp/100)
    coefficients = {}
    for term in sp.Add.make_args(g):
        powers = term.as_powers_dict()
        n, m = int(powers.get(z,0)), int(powers.get(w,0))
        coefficients[n,m] = coefficients.get((n,m),0)+term/(z**n*w**m)
    coefficients = {k: sp.simplify(v) for k,v in coefficients.items() if v!=0}
    assert len(coefficients)==32
    assert set(n for n,m in coefficients)=={0,-9,-8,-7,-6,-5,-2,-1,1,2,5,6,7,8,9}
    expected0 = {-9:-sp.I/800, -8:-sp.Rational(1,40)-sp.I/400,
                 -7:sp.Rational(9,20), -6:-sp.Rational(1,40)+sp.I/400,
                 -5:sp.I/800, -2:sp.I/400, -1:sp.Rational(1,20)+sp.I/200}
    expected = {(n,0):v for n,v in expected0.items()}
    expected.update({(-n,0):sp.conjugate(v) for n,v in expected0.items()})
    shifted_r = {0:1, -1:-sp.Rational(1,2), 1:-sp.Rational(1,2),
                 -6:-sp.Rational(1,4), 6:-sp.Rational(1,4),
                 -7:sp.Rational(1,2), 7:sp.Rational(1,2),
                 -8:-sp.Rational(1,4), 8:-sp.Rational(1,4)}
    for n,v in shifted_r.items():
        expected[n,1]=v*(-3-4*sp.I)/1000
        expected[n,-1]=v*(-3+4*sp.I)/1000
    assert coefficients==expected
    assert sp.simplify(abs(coefficients[-1,0])**2)==sp.Rational(101,40000)
    assert all(sp.simplify(abs(coefficients[-1,m])**2)==sp.Rational(1,160000)
               for m in (-1,1))
    x=sp.symbols('x')
    R=sp.prod(1+x*x/sp.Integer(n*n) for n in (2,5,6,7,8,9))
    polynomials=[]
    for degree,p in ((14,x*(x-sp.I)*R),(15,x*x*(x-sp.I)*R)):
        poly=sp.Poly(p,x)
        assert poly.degree()==degree
        assert sum(abs(c) for c in poly.all_coeffs())==sp.Rational(6409325,2286144)
        assert abs(poly.eval(-sp.I))==sp.Rational(4,3)
        for n in (0,1,-2,2,-5,5,-6,6,-7,7,-8,8,-9,9):
            assert poly.eval(sp.I*n)==0
        polynomials.append({'degree':degree,'coefficients_high_to_low':list(map(str,poly.all_coeffs()))})
    phi=sp.expand(g.subs(z,-z)-g)
    dq=lambda f:sp.expand(sp.I*z*sp.diff(f,z))
    dp=lambda f:sp.expand(sp.I*w*sp.diff(f,w))
    for point in (1,-1):
        assert sp.simplify(dq(phi).subs(z,point))==0
        assert sp.simplify(dp(phi).subs(z,point))==0
    hess=sp.simplify(4*dq(dq(phi)).subs(z,1))  # actual derivative / pi^2
    assert sp.simplify(hess-(sp.Rational(8840,25)+sp.Rational(96,25)*cp))==0
    assert sp.simplify(4*dq(dq(phi)).subs(z,-1)+hess)==0
    c0=(sp.sqrt(101)*sp.sin(sp.pi/7)-1)/100
    return coefficients, {'coefficients':{str(k):str(v) for k,v in sorted(coefficients.items())},
        'annihilators':polynomials,'c0_diagnostic':float(c0.evalf()),
        'kappa_diagnostic':float((4*c0/3/sp.Rational(6409325,2286144)).evalf()),
        'half_shift_hessian_div_pi_squared':str(hess),
        'half_shift_hessian_range_div_pi_squared':['8744/25','8936/25']}


def matrix_checks(coefficients):
    results=[]
    for n in (19,21,31):
        j=np.arange(n)
        T=lambda a,b:np.eye(n)[(j+a)%n]*np.exp(2j*np.pi*b*((j+pow(2,-1,n)*a)%n)/n)[:,None]
        W=lambda a,b:((-1)**(a*b))*T(a,b)
        ordinary=sum(complex(c)*W(m,k) for (k,m),c in coefficients.items())
        wrong=sum(complex(c)*T(m,k) for (k,m),c in coefficients.items())
        r=lambda q:(1-np.cos(14*np.pi*q))*(1+np.cos(2*np.pi*q))
        q=j/n
        v=np.cos(14*np.pi*q)+r(q)/10+r(q)*np.sin(2*np.pi*q)/100-.1
        b=(-3-4j)/5*r((j+pow(2,-1,n))/n)/200
        direct=np.diag(v).astype(complex)
        direct[j,(j+1)%n]=b
        direct[(j+1)%n,j]=b.conjugate()
        err=float(np.linalg.norm(ordinary-direct,2))
        wrong_distance=float(np.linalg.norm(wrong-direct,'fro')**2/n)
        assert err<2e-13 and wrong_distance>1e-5
        xx,yy=np.meshgrid(j,j,indexing='ij')
        residue=(-pow(8,-1,n)*(3*xx*xx-2*xx*yy+3*yy*yy))%n
        metaplectic=np.exp(2j*np.pi*residue/n)/np.sqrt(n)
        egorov=0.
        multiplication=0.
        for a,bv,c,d in ((1,7,-1,2),(-1,-8,2,-5),(0,1,1,0)):
            phase=np.exp(2j*np.pi*(pow(2,-1,n)*(a*d-bv*c)%n)/n)
            multiplication=max(multiplication,float(np.linalg.norm(T(a,bv)@T(c,d)-phase*T(a+c,bv+d),2)))
            egorov=max(egorov,float(np.linalg.norm(metaplectic@T(a,bv)@metaplectic.conj().T-T(3*a+4*bv,2*a+3*bv),2)))
        assert multiplication<2e-12 and egorov<2e-12
        results.append({'N':n,'ordinary_dictionary_error':err,
                        'wrong_raw_dictionary_squared_normalized_HS':wrong_distance,
                        'raw_multiplication_error':multiplication,'egorov_error':egorov})
    return results


def action_constant_checks(coefficients):
    # |c| <= |Re c|+|Im c|, so this is an exact conservative certificate.
    mass=sum(abs(sp.re(c))+abs(sp.im(c)) for c in coefficients.values())
    assert mass<2
    assert max(abs(n)+abs(m) for n,m in coefficients)<=10
    # Elementary pi<22/7, pi>3; exp(22/35)<2 can be checked separately
    # by its Taylor series with a geometric tail, entirely rationally.
    x=Fraction(22,35)
    total=sum(x**j/math.factorial(j) for j in range(16))
    tail=x**16/Fraction(math.factorial(16))/(1-x/17)
    assert total+tail<2
    assert 4*Fraction(44,7)*9<300
    assert 4*Fraction(44,7)**2*9*10<20000
    assert 600*Fraction(1,10**8)<Fraction(1,400)
    assert 240000*Fraction(1,10**8)<Fraction(1,2)
    ordinary=[];normalized=[]
    for j in range(1,16):
        bound=10**8*math.factorial(j-1)*800**(j-1)
        assert bound<10**61
        assert Fraction(bound,6**j)<10**49
        ordinary.append(str(bound));normalized.append(str(Fraction(bound,6**j)))
    assert Fraction(6409325,2286144)<3
    assert Fraction(4,9)*Fraction(13,700)>Fraction(8,1000)
    assert Fraction(10**49,10**52)<Fraction(4,1000)
    return {'coefficient_absolute_mass_upper':str(mass),
            'C15_rational_upper_bounds':ordinary,'normalized_q_derivative_upper_bounds_using_2pi_gt_6':normalized,
            'analytic_flow_time_threshold':'1e-8','finite_type_time_threshold':'1e-52',
            'actual_time':'1e-80/(2*pi)','remainder_constants':{'C15':'1e61','normalized_q':'1e49'}}


def cycles(p):
    unseen=set(range(len(p)))
    out=[]
    while unseen:
        start=min(unseen); current=start; cycle=[]
        while current in unseen:
            unseen.remove(current);cycle.append(current);current=p[current]
        out.append(cycle)
    return out


def cycle_benchmark(n,modes):
    ans=0
    for p in itertools.permutations(range(len(modes))):
        cs=cycles(p);term=(-1)**(len(modes)-len(cs))
        for c in cs:
            if sum(modes[j] for j in c):term=0;break
            s=0;ss=[]
            for j in c:ss.append(s);s+=modes[j]
            term*=max(n-max(ss)+min(ss),0)
        ans+=term
    return ans


def cue_checks():
    path=ROOT/'supplement/fixed_map/report-audit/verify.py'
    spec=importlib.util.spec_from_file_location('cue_prior_verifier',path)
    reference=importlib.util.module_from_spec(spec);spec.loader.exec_module(reference)
    def factorial_mobius(n,m):
        answer=Fraction(0)
        for p in reference.partitions(len(m)):
            mu=math.prod((-1)**(len(b)-1)*math.factorial(len(b)-1) for b in p)
            answer+=mu*reference.cue_moment(n,tuple(sum(m[j] for j in b) for b in p))
        return answer
    count=0
    for n in range(1,6):
        for k in range(1,5):
            for m in itertools.product((-n,-1,0,1,n),repeat=k):
                assert cycle_benchmark(n,m)==factorial_mobius(n,m),(n,m)
                count+=1
    samples=[]
    for n in (1,2,3,4):
        for m in ((0,0,0,0,0),(1,-1,2,-2,0),(n,n,-n,-n,0),(1,1,1,1,-4)):
            got=cycle_benchmark(n,m)
            expected=Fraction(0)
            for p in reference.partitions(len(m)):
                mu=math.prod((-1)**(len(b)-1)*math.factorial(len(b)-1) for b in p)
                expected+=mu*reference.vandermonde_moment(n,tuple(sum(m[j] for j in b) for b in p))
            assert got==expected
            samples.append({'N':n,'modes':list(m),'factorial_benchmark':got})
    return {'cycle_vs_cumulant_mobius_cases':count,'cycle_vs_independent_density_cases':samples}


def digits(x,m,k):
    ans=[]
    for _ in range(k):
        x*=m; d=x.numerator//x.denominator;ans.append(d);x-=d
    return ans


def digit_checks():
    # Rational samples never have a terminating base-M expansion.
    checks=0
    for m in (3,5,7,9):
        for numerator in range(1,19):
            x=Fraction(numerator,19)
            for y in (((1-m)*x)%1,(x+Fraction(1,2))%1):
                assert all(a!=b for a,b in zip(digits(x,m,8),digits(y,m,8)))
                checks+=1
        for j in range(m):
            y=(Fraction(j,m)+Fraction(m-1,m*m)+Fraction(1,19*m*m))%1
            yy=digits(y,m,2)
            assert yy==[j,m-1]
            assert any(a==b for a,b in zip((j,0),yy))
            assert any(a==b for a,b in zip(((j-1)%m,m-1),yy))
    for m in (4,6,8):
        for numerator in range(1,19):
            x=Fraction(numerator,19)
            for y in ((-x)%1,(x+Fraction(1,m-1))%1):
                assert all(a!=b for a,b in zip(digits(x,m,8),digits(y,m,8)))
                checks+=1
    even_exact=[]
    for m in (4,6,8):
        for k in range(1,5):
            n=m**k;d=(n-1)//(m-1)
            for x in range(n):
                a=x;b=n-1-x;c=(x+d)%n
                for _ in range(k):
                    assert a%m!=b%m and a%m!=c%m
                    a//=m;b//=m;c//=m
            even_exact.append({'base':m,'k':k,'N':n,'fourier_line_shift':d,
                               'both_entire_discrete_support_lines_checked':True,'compression_norm_proof_target':1})
    binary=[]
    for k in range(1,6):
        n=2**k;j=np.arange(n)
        points=np.column_stack((j,n-1-j))
        f=np.exp(-2j*np.pi*(points@points.T)/n)/n
        norm=float(np.linalg.norm(f,2));target=math.sqrt(2/n)
        assert abs(norm-target)<3e-14
        binary.append({'k':k,'N':n,'norm':norm,'exact_formula':target})
    eta=Fraction(1,1000);q=Fraction(1,7)-eta;qp=Fraction(1,7)+eta
    assert int(q*7)!=int(qp*7) and qp-q<Fraction(1,7)
    return {'rational_line_membership_checks':checks,'digits_per_point':8,
            'even_base_exact_support_cases':even_exact,
            'binary_norm_cases':binary,'adjacent_strip_counterexample':{'q':str(q),'q_prime':str(qp),'distance':str(qp-q)}}


def fejer_checks():
    rows=[]
    for n in (3,7,11):
        theta=np.arange(n)/n+.08*np.sin(np.arange(n)) / n
        a=np.arange(n*n).reshape(n,n)/n**2+1j*np.eye(n)
        for m in (2,3,5):
            c=.2
            assert c*m/n<=.5
            delta=(theta[:,None]-theta[None,:]+.5)%1-.5
            q=float(np.sum(abs(a[abs(delta)<=c/n])**2)/n)
            correlations=sum((1-abs(t)/m)*np.sum(abs(a)**2*np.exp(2j*np.pi*t*delta))/n for t in range(1-m,m))
            positive=np.sum(abs(a)**2*abs(sum(np.exp(2j*np.pi*t*delta) for t in range(m)))**2/m)/n
            assert abs(correlations-positive)<2e-13
            bound=math.pi**2*float(positive)/(4*m)
            assert q<=bound+1e-13
            rows.append({'N':n,'M':m,'Q':q,'positive_Fejer_bound':bound})
    return rows


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    coefficients,symbol=symbol_check()
    data={'status':'PASS','date':'2026-09-30','arithmetic':'exact SymPy rationals/Gaussian rationals, Fraction; complex128 separately',
          'python':platform.python_version(),'sympy':sp.__version__,'numpy':np.__version__,
          'symbol':symbol,'action_constants':action_constant_checks(coefficients),
          'matrix':matrix_checks(coefficients),'cue':cue_checks(),
          'digits':digit_checks(),'fejer':fejer_checks(),
          'non_claims':['asymptotic finite-type proof','Cohen FUP theorem','quantum FIO identification','deterministic CUE','priority or independent refereeing']}
    sources=['computations/verification/heisenberg_note_audit.py','mathematics/frozen_phase_finite_type.md',
             'mathematics/offdiagonal_digit_fup.md','mathematics/heisenberg_trace_support.md',
             'mathematics/frozen_commutator_action.md',
             'supplement/fixed_map/report-audit/verify.py']
    data['source_sha256']={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({'status':'PASS','cycle_cases':data['cue']['cycle_vs_cumulant_mobius_cases'],
                      'matrix_cases':len(data['matrix']),'digit_cases':data['digits']['rational_line_membership_checks'],
                      'output':str(args.output) if args.output else None}))


if __name__=='__main__':
    main()
