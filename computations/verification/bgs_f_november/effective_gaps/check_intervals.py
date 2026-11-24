"""Outward-rounded rational enclosures of the original N=49 phase gaps."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from argparse import ArgumentParser
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import factorial, isqrt
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from spectrum.bgs_packet_check import COEFFICIENTS, SQUARES, exact_first_order, p_log, rho_at, split

SCALE = 10**50
DIGITS = 10**8
N = 49
M = 21
TAME = {pow(3, j, 7): j % 3 for j in range(6)}


def ceiling_div(x, d):
    return -((-x)//d)


@dataclass(frozen=True)
class Real:
    lo: int
    hi: int

    @classmethod
    def rational(cls, x):
        scaled = Fraction(x)*SCALE
        return cls(scaled.numerator//scaled.denominator,
                   ceiling_div(scaled.numerator,scaled.denominator))

    def __add__(self, other):
        return Real(self.lo+other.lo, self.hi+other.hi)

    def __neg__(self):
        return Real(-self.hi,-self.lo)

    def __sub__(self, other):
        return self+-other

    def __mul__(self, other):
        vals = [a*b for a in (self.lo,self.hi) for b in (other.lo,other.hi)]
        return Real(min(vals)//SCALE,ceiling_div(max(vals),SCALE))

    def quotient(self, d):
        assert d > 0
        return Real(self.lo//d,ceiling_div(self.hi,d))

    def square(self):
        vals = self.lo**2, self.hi**2
        lo = 0 if self.lo<=0<=self.hi else min(vals)
        return Real(lo//SCALE,ceiling_div(max(vals),SCALE))

    def contains_zero(self):
        return self.lo <= 0 <= self.hi


@dataclass(frozen=True)
class Complex:
    re: Real
    im: Real

    def __add__(self, other):
        return Complex(self.re+other.re,self.im+other.im)

    def __mul__(self, other):
        return Complex(self.re*other.re-self.im*other.im,
                       self.re*other.im+self.im*other.re)

    def conj(self):
        return Complex(self.re,-self.im)

    def scale(self, real):
        return Complex(self.re*real,self.im*real)


ZERO = Real(0,0)
CZERO = Complex(ZERO,ZERO)


def pi_bounds():
    def arctan_inverse(base):
        low = sum(Fraction((-1)**j,(2*j+1)*base**(2*j+1)) for j in range(48))
        high = low+Fraction(1,97*base**97)
        return Real(Real.rational(low).lo,Real.rational(high).hi)

    return (Real.rational(16)*arctan_inverse(5)
            -Real.rational(4)*arctan_inverse(239))


PI = pi_bounds()


@lru_cache(None)
def root(x,n):
    j = x%n
    if 2*j>n:
        j -= n
    angle = (PI*Real.rational(2*j)).quotient(n)
    assert -4*SCALE<=angle.lo<=angle.hi<=4*SCALE
    square = angle.square()
    cosine, sine = Real.rational(1), angle
    ce, si = cosine,sine
    for r in range(1,45):
        ce = ((-ce)*square).quotient((2*r)*(2*r-1))
        si = ((-si)*square).quotient((2*r+1)*(2*r))
        cosine = cosine+ce
        sine = sine+si
    assert 4**89*SCALE<factorial(89)
    return Complex(cosine+Real(-1,1),sine+Real(-1,1))


def states(ell,h):
    basis = [[CZERO]*N for _ in range(2)]
    for x in range(1,N):
        if x%7:
            sign = int(x%7 not in SQUARES)
            basis[sign][x] = root(ell*p_log(x,2)%N,N)*root(h*TAME[x%7]%3,3)
    return basis


def apply_A(basis):
    result = [[CZERO]*N for _ in range(2)]
    rho = rho_at(2)
    half = pow(2,-1,N)
    for v,(real,imaginary) in COEFFICIENTS.items():
        a,b = split(v,rho,N)
        c = Complex(Real.rational(Fraction(real,4000)),
                    Real.rational(Fraction(imaginary,4000)))
        for x in range(N):
            multiplier = c*root(b*(x+half*a)%N,N)
            y = (x+a)%N
            for sign in (0,1):
                result[sign][x] = result[sign][x]+multiplier*basis[sign][y]
    return result


def second_matrix(ell,h):
    V = states(ell,h)
    B = apply_A(V)
    rho = rho_at(2)
    inv_gamma = pow(3+2*rho,-1,N)
    inv_gamma_log = p_log(inv_gamma,2)
    coefficients = []
    for r in range(1,M):
        # (lambda+M)/(lambda-M), extended by zero on lambda, equals
        # sum_{r=1}^{m-1}(1-2r/m)(M/lambda)^r.
        lam_inverse_power = (root(-r*ell*inv_gamma_log%N,N)
                             *root(-r*h*TAME[inv_gamma%7]%3,3))
        phase = Complex(ZERO,Real.rational(Fraction(2*r-M,2*M*M)))
        coefficients.append(lam_inverse_power*phase)

    result = [[CZERO for _ in range(2)] for _ in range(2)]
    for r,phase in enumerate(coefficients,1):
        step = pow(inv_gamma,r,N)
        for p in (0,1):
            for q in (0,1):
                inner = CZERO
                for x in range(N):
                    inner = inner + B[p][x].conj()*B[q][step*x%N]
                result[p][q] = result[p][q]+phase*inner
    assert result[0][0].im.contains_zero() and result[1][1].im.contains_zero()
    for op in ('re','im'):
        left,right = getattr(result[0][1],op),getattr(result[1][0].conj(),op)
        assert (left-right).contains_zero()
    return result


def gap_coefficient(ell,h):
    H = second_matrix(ell,h)
    discriminant = ((H[0][0].re-H[1][1].re).square()
                    +Real.rational(4)*(H[0][1].re.square()+H[0][1].im.square()))
    assert discriminant.lo>0
    lo = isqrt(discriminant.lo*DIGITS**2//SCALE)
    hi = isqrt(discriminant.hi*DIGITS**2//SCALE)+1
    assert 100 < lo < hi == lo+1
    return lo,hi


def compute():
    version = exact_first_order(2)
    assert version[4]==version[6]==[3,0]
    t0 = Fraction(N,10**80)
    assert Fraction(4,M)>Fraction(19,100)
    # Approximation on each Schur circle. Budget includes inverse,
    # off-diagonal blocks, the diagonal Taylor term and common phase.
    inv_max = Fraction(2)*M/4
    inverse_change_per_t = Fraction(10)*(Fraction(M,4))**2
    budget = 4*inverse_change_per_t + 8*inv_max + 60
    assert budget < 10**4
    assert 10**4*t0 < Fraction(1,10**10)
    rows = {}
    for ell in (4,6):
        for h in range(3):
            lo,hi = gap_coefficient(ell,h)
            rows[f"{ell}:{h}"] = {
                "coefficient": [str(Fraction(j,DIGITS)) for j in (lo,hi)],
                "gap_radians": [str(Fraction(j,DIGITS)*t0**2) for j in (lo-1,hi+1)],
                "coefficient_decimal": [f"{j/DIGITS:.8f}" for j in (lo,hi)],
            }
    return {"n":N,"rational_kick":str(t0),"rounding_grid":SCALE,
            "circles_radius_coefficient":"1/10000000000",
            "schur_bound":str(budget),"doublets":rows}


if __name__=="__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--verify",action="store_true")
    args = parser.parse_args()
    results = json.dumps(compute(),indent=2)+"\n"
    path = ROOT/"effective_gaps/data/intervals.json"
    if args.verify:
        assert results==path.read_text()
        print("Original N=49 doublet gap intervals verified.")
    else:
        path.write_text(results)
        print("Wrote",path)
