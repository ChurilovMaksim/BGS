#!/usr/bin/env python3
"""Outward-rounded INTEGER interval certificate for the Pell gamma constant.

Machin's identity bounds pi by alternating rational arctangent series.
Integer square root bounds sqrt(2). Taylor's remainder bounds each cosine.
The omitted positive tail is bounded geometrically. No floating-point
arithmetic or external special-function implementation is used.
"""

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
from dataclasses import dataclass
from fractions import Fraction
from math import factorial, isqrt
from pathlib import Path
import argparse
import json

S=10**60


def ceil_div(a: int, b: int) -> int:
    return -((-a)//b)

@dataclass(frozen=True)
class Interval:
    lo: int
    hi: int
    def __post_init__(self):
        assert self.lo<=self.hi
    @staticmethod
    def integer(n: int):
        return Interval(n*S,n*S)
    def __add__(self, other):
        return Interval(self.lo+other.lo,self.hi+other.hi)
    def __neg__(self):
        return Interval(-self.hi,-self.lo)
    def __sub__(self, other):
        return self+-other
    def __mul__(self, other):
        vals=[a*b for a in (self.lo,self.hi) for b in (other.lo,other.hi)]
        return Interval(min(vals)//S,ceil_div(max(vals),S))
    def divide(self, other):
        assert other.lo>0
        vals=[(a*S,b) for a in (self.lo,self.hi) for b in (other.lo,other.hi)]
        return Interval(min(a//b for a,b in vals),max(ceil_div(a,b) for a,b in vals))
    def divide_int(self, n: int):
        assert n>0
        return Interval(self.lo//n,ceil_div(self.hi,n))
    def power(self,n: int):
        assert n>=0
        out=Interval.integer(1)
        for _ in range(n):out=out*self
        return out


def atan_bounds(q: int, terms: int=80):
    partial=sum((Fraction((-1)**j,(2*j+1)*q**(2*j+1)) for j in range(terms)),Fraction(0))
    next_term=Fraction((-1)**terms,(2*terms+1)*q**(2*terms+1))
    return min(partial,partial+next_term),max(partial,partial+next_term)


def cosine(x: Interval, terms: int=50) -> Interval:
    assert 0<=x.lo<=x.hi<=4*S
    term=Interval.integer(1); total=term; minus_square=-(x*x)
    for j in range(1,terms+1):
        term=(term*minus_square).divide_int((2*j-1)*(2*j))
        total=total+term
    remainder=ceil_div(S*4**(2*terms+2),factorial(2*terms+2))
    return Interval(total.lo-remainder,total.hi+remainder)


def decimal(n: int) -> str:
    sign='-' if n<0 else ''; n=abs(n)
    return sign+str(n//S)+'.'+str(n%S).zfill(60)


def certificate() -> dict:
    lo5,hi5=atan_bounds(5);lo239,hi239=atan_bounds(239)
    lo=16*lo5-4*hi239; hi=16*hi5-4*lo239
    pi=Interval((lo*S).numerator//(lo*S).denominator,
                ceil_div((hi*S).numerator,(hi*S).denominator))
    sqrt2lo=isqrt(2*S*S)
    assert sqrt2lo*sqrt2lo<=2*S*S<(sqrt2lo+1)**2
    sqrt2=Interval(sqrt2lo,sqrt2lo+1)
    one=Interval.integer(1);two=Interval.integer(2)
    lam=Interval.integer(3)+two*sqrt2
    a=(Interval.integer(4)*pi).divide(sqrt2*(one+sqrt2))
    r=one.divide(lam);x=a;gamma=Interval.integer(3).divide_int(2)
    J=40
    for _ in range(J):
        gamma=gamma+two*(one-cosine(x))
        x=x*r
    tail=(a*a*r.power(2*J)).divide(one-r*r)
    gamma=Interval(gamma.lo,gamma.hi+tail.hi)
    # Forty certified decimal places must agree, independently of mpmath.
    assert gamma.lo//(10**20)==gamma.hi//(10**20)
    assert decimal(gamma.lo).startswith('5.6142206921511980716279652410177946307706')
    root=Path(__file__).resolve().parents[2]
    for name in ('mathematics/pell_phase_rate.md',):
        assert '5.614220692151' in (root/name).read_text(), name
    return {'producer':'computations/verification/pell_gamma_interval.py',
            'scope':'Exact integer interval arithmetic, Machin/arctangent and Taylor remainders, and a geometric tail; no floating-point rounding assumptions.',
            'scale_exponent':60,'terms':J,'lower_bound':decimal(gamma.lo),
            'upper_bound':decimal(gamma.hi),'tail_upper_bound':decimal(tail.hi),
            'status':'PASS'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args(); data=certificate();text=json.dumps(data,indent=2)+'\n'
    if args.output:args.output.write_text(text)
    print(text,end='')

if __name__=='__main__':main()
