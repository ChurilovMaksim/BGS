#!/usr/bin/env python3
"""Exact scalar enclosure and independent quadrature for rare-phase testing.

Exact: outward-rounded integer arithmetic for C_*, rational e bounds, finite
copy comparisons and central-binomial inequalities. Numerical: angular,
elliptic and radial quadrature at fixed n. Neither replaces the asymptotic
proof. Optional plots require matplotlib and are not a core test dependency.
"""
from __future__ import annotations
import argparse,hashlib,json
from fractions import Fraction
from math import comb,factorial
from pathlib import Path
import mpmath as mp


class FixedInterval:
    """All endpoints are integers divided by one common positive scale."""
    def __init__(self,lo,hi,scale):
        assert lo<=hi and scale>0
        self.lo,self.hi,self.scale=lo,hi,scale
    @staticmethod
    def rational(p,q,scale):
        assert q>0
        return FixedInterval(p*scale//q,-(-p*scale//q),scale)
    def add(self,x):
        assert self.scale==x.scale
        return FixedInterval(self.lo+x.lo,self.hi+x.hi,self.scale)
    def sub(self,x):
        assert self.scale==x.scale
        return FixedInterval(self.lo-x.hi,self.hi-x.lo,self.scale)
    def mul(self,x):
        assert self.scale==x.scale
        products=[a*b for a in (self.lo,self.hi) for b in (x.lo,x.hi)]
        return FixedInterval(min(products)//self.scale,-(-max(products)//self.scale),self.scale)
    def inv(self):
        assert self.lo>0
        sq=self.scale*self.scale
        return FixedInterval(sq//self.hi,-(-sq//self.lo),self.scale)
    def times(self,n):
        assert n>=0
        return FixedInterval(self.lo*n,self.hi*n,self.scale)


def constant_certificate(terms,digits=60):
    scale=10**digits
    fact=factorial(80);partial=sum(fact//factorial(k) for k in range(81))
    elo=Fraction(partial,fact)
    ehi=elo+Fraction(82,81*factorial(81))
    ei=FixedInterval(elo.numerator*scale//elo.denominator,
                     -(-ehi.numerator*scale//ehi.denominator),scale)
    a=ei.inv();one=FixedInterval(scale,scale,scale)
    c=FixedInterval.rational(1,4,scale);series=FixedInterval(0,0,scale)
    for k in range(1,terms+1):
        left=FixedInterval(2*k*scale,2*k*scale,scale).sub(a).inv()
        right=FixedInterval((2*k-1)*scale,(2*k-1)*scale,scale).add(a).inv()
        series=series.add(c.mul(left.add(right)))
        c=c.mul(FixedInterval.rational((2*k-1)**2,4*(k+1)**2,scale))
    upper_expr=a.times(2).mul(one.sub(a).inv().add(a.inv()).sub(series))
    tail=a.mul(FixedInterval.rational(1,3*terms**3,scale))
    lower=upper_expr.lo-tail.hi;upper=upper_expr.hi
    assert lower>0 and upper-lower<scale//(terms**2)
    return {'terms':terms,'decimal_scale_digits':digits,
            'lower_numerator':str(lower),'upper_numerator':str(upper),
            'denominator':str(scale),'e_lower_numerator':str(ei.lo),
            'e_upper_numerator':str(ei.hi),
            'construction':'integer outward rounding; factorial-series e enclosure; analytic a/(3M^3) tail'}


def exact_checks(terms):
    checks=0
    for k in range(1,4097):
        central=comb(2*k,k)
        assert central*central*(3*k+1)<=16**k
        assert (3*k+1)*(2*k-1)**2>=4*k**3
        checks+=1
    assert 4*63**18>3*64**18
    assert 4*63**20<3*64**20
    central=comb(128,64)
    assert 64*central>127*(3*10**18)**2
    assert 8*factorial(129)>3*10**218
    certificate=constant_certificate(terms)
    return {'central_binomial_tail_checks':checks,'finite_copy_checks':4,
            'finite_example':{'photon_number':128,'mean_energy':1,
              'quantum_copies_for_075_success':10,
              'heterodyne_necessary_copies_strict_lower':'3e18',
              'unit_aperture_necessary_copies_strict_lower':'3e218'},
            'constant_interval':certificate}


def ck(k):
    return mp.mpf(comb(2*k,k))**2/(mp.mpf(16)**k*(2*k-1)**2)


def angular_F(t):
    t=mp.mpf(t)
    if t==0:return mp.mpf(0)
    if t>1:return t*angular_F(1/t)
    if t<mp.mpf('0.5'):
        total=mp.mpf(0);term=mp.mpf('0.25')*t*t;k=1
        while True:
            total+=term
            if abs(term)<mp.eps*max(t,mp.mpf(1)):break
            term*=mp.mpf((2*k-1)**2)/(4*(k+1)**2)*t*t;k+=1
            if k>10000:raise RuntimeError('series failed to converge')
        return 2*t-2*total
    parameter=min(mp.mpf(1),4*t/(1+t)**2)
    return mp.re(2*(1+t)*(1-2*mp.ellipe(parameter)/mp.pi))


def scaled_integral(n,E,beta,upper=mp.inf):
    u=E/mp.mpf(n)**beta
    x=mp.exp((mp.loggamma(n+1)+mp.log((1-u)/u))/n)
    def integrand(y):
        if y<=-x:return mp.mpf(0)
        t=mp.exp(n*mp.log1p(y/x))
        return mp.exp(-y)*angular_F(t)
    split=[-x]+[v for v in [-12,-4,-1,0,1,4,12] if -x<v<upper]
    split.append(upper)
    return x,mp.quad(integrand,split)


def numerical_checks(dps,expanded):
    with mp.workdps(dps):
        C=mp.quad(lambda y:mp.exp(-y)*angular_F(mp.exp(mp.e*y)),[-mp.inf,-2,0,2,mp.inf])
        angular=[]
        for t in [mp.mpf('0.01'),mp.mpf('.2'),mp.mpf(1),mp.mpf(5),mp.mpf(100)]:
            f=angular_F(t)
            direct=mp.quad(lambda phi:(abs(1+mp.sqrt(t)*mp.exp(1j*phi))-
                                      abs(1-mp.sqrt(t)*mp.exp(1j*phi)))**2,
                           [0,mp.pi/2,mp.pi,3*mp.pi/2,2*mp.pi])/(2*mp.pi)
            assert abs(f-direct)<mp.mpf('1e-25')
            assert min(1,t)<=f<=4*min(1,t)
            assert abs(f-t*angular_F(1/t))<mp.mpf('1e-25')
            angular.append({'t':str(t),'F':mp.nstr(f,24),'direct_difference':mp.nstr(abs(f-direct),8)})
        rows=[]
        for n in ([32,128,512,2048] if expanded else [32,128,512]):
            x,value=scaled_integral(n,mp.mpf(1),mp.mpf(1))
            rows.append({'n':n,'balance_squared_radius':mp.nstr(x,24),
                         'scaled_Hellinger':mp.nstr(value,24),
                         'relative_error_to_limit':mp.nstr(abs(value-C)/C,14)})
        assert abs(mp.mpf(rows[-1]['scaled_Hellinger'])-C)/C<mp.mpf('.1')
        profiles=[]
        for ell in [-4,-2,0,2,4]:
            value=mp.quad(lambda y:mp.exp(-y)*angular_F(mp.exp(mp.e*y)),[-mp.inf,ell])
            assert 0<value<C
            profiles.append({'offset':ell,'limit_profile':mp.nstr(value,24)})
        overlap=mp.mpf(63)/64
        success=lambda B:(1+mp.sqrt(1-overlap**(2*B)))/2
        heterodyne=8*mp.sqrt(mp.mpf(comb(128,64)))/mp.sqrt(127)
        return {'decimal_precision':dps,'C_quadrature':mp.nstr(C,45),
                'angular_cross_checks':angular,'finite_radial_diagnostics':rows,
                'boundary_profile':profiles,
                'finite_example':{'D':mp.nstr(mp.sqrt(127)/64,30),
                   'success_9':mp.nstr(success(9),30),'success_10':mp.nstr(success(10),30),
                   'heterodyne_necessary_lower_value':mp.nstr(heterodyne,30),
                   'unit_aperture_log10_lower':mp.nstr(mp.log10(8*mp.factorial(129)),30)},
                'scope':'numerical diagnostic only; constant certification is a separate exact calculation'}


def main():
    if not __debug__:raise RuntimeError('Do not disable assertions')
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--terms',type=int,default=2048);p.add_argument('--dps',type=int,default=50)
    p.add_argument('--expanded',action='store_true');p.add_argument('--output',type=Path)
    p.add_argument('--replay',type=Path)
    args=p.parse_args()
    if not 16<=args.terms<=32768 or args.dps<35:p.error('Require 16<=terms<=32768, dps>=35')
    exact=exact_checks(args.terms);numerical=numerical_checks(args.dps,args.expanded)
    ci=exact['constant_interval']
    rejected=0
    for lo,hi,s in [(2,1,1),(0,1,0),(0,1,-1)]:
        try:FixedInterval(lo,hi,s)
        except AssertionError:rejected+=1
        else:raise AssertionError('bad interval accepted')
    result={'status':'PASS','scope':'finite exact checks and separately labelled numerical diagnostics',
            'exact':exact,'numerical':numerical,'negative_controls':rejected,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if args.replay:
        args.replay.parent.mkdir(parents=True,exist_ok=True)
        args.replay.write_text(f"{args.terms} {ci['decimal_scale_digits']} {ci['lower_numerator']} {ci['upper_numerator']}\n")
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
