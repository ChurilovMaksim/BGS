"""Exact rational certificates for gap windows, progression bounds and eigenphase transport."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
from math import isqrt, factorial
import json
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'research'))
from coefficients import raw_symbol, pell

C = F(593,500)
tau = F(1,10**80)
pi_lower = F(314159,100000)
pi_upper = F(314160,100000)
# The bounding fractions also follow from Machin's identity using alternating series.
def atan_bounds(x, pairs=8):
    part=sum((-1)**j*x**(2*j+1)/(2*j+1) for j in range(2*pairs))
    return part,part+x**(4*pairs+1)/(4*pairs+1)
s5,t5=atan_bounds(F(1,5)); s239,t239=atan_bounds(F(1,239))
assert pi_lower<16*s5-4*t239<16*t5-4*s239<pi_upper
def floor6(a):
    return str(F(a.numerator*10**6//a.denominator,10**6))
def ceil8(a):
    return str(F(-((-a.numerator*10**8)//a.denominator),10**8))
def sqrt_upper(a):
    n=10**12
    return F(isqrt(a.numerator*n*n//a.denominator)+1,n)
assert C*tau*(5*10**39)**2/pi_lower < F(1,10)
sine_lower = F(1,100)*(1-(F(5,2)/pi_lower)**2)-F(1,1000)
assert sine_lower > F(26,10000)
assert F(1,4)*(1-pi_upper**2/36)>F(18,100)
# exp(1/3)<7/5, from its series with a geometric remainder.
assert 1+F(1,3)+F(1,18)/(1-F(1,9))<F(7,5)

progressions = []
for k,lo,hi,goal in [(13,3,10**39,86),(175,10**70,2*10**70,221),
                     (185,10**72,2*10**72,140),(191,10**73,2*10**73,270)]:
    d=pell(k); ratio=F(4*k,3*d)
    # S^k=I mod d in split coordinate notation, certified explicitly.
    a,b=1,0
    for _ in range(k):
        a,b=(3*a+4*b)%d,(2*a+3*b)%d
    assert (a,b)==(1,0)
    prob=ratio*(F(1,2)+C*tau*hi**2/pi_lower)
    hit=prob+ratio/2
    delta=F(81,5000)/prob-F(49,40)
    count=(hi//d+1)//2-(((lo-1)//d+1)//2)
    assert delta>goal
    progressions.append(dict(k=k,divisor=str(d),min_N=str(lo),max_N=str(hi),count=count,
                             coverage_upper=ceil8(prob),hit_probability_upper=ceil8(hit),
                             delta_P_lower=floor6(delta)))

# Rigorous monotone cell bounds for the original bump and its convolution.
grid=128
scale=1<<40
@lru_cache(None)
def bump(j):
    if abs(j)>=grid:return 0,0
    x=1/(1-F(j*j,grid**2)); n=2048
    assert 0<x<n
    a=(1-x/n)**n; b=(1+x/n)**(-n)
    return a.numerator*scale//a.denominator, -((-b.numerator*scale)//b.denominator)
def cell(j):
    x,y=bump(j),bump(j+1)
    return min(x[0],y[0]),max(x[1],y[1])
cells={j:cell(j) for j in range(-grid,grid)}
den=grid*scale
ilo=F(sum(v[0] for v in cells.values()),den); ihi=F(sum(v[1] for v in cells.values()),den)
def convolution(i):
    low=high=0
    for j,(a,b) in cells.items():
        c,d=cells.get(i-j-1,(0,0))
        low+=a*c; high+=b*d
    den=grid*scale**2
    return F(low,den),F(high,den)
w_min=(convolution(1)[0]/(2*ihi**2))**2
# For m/N in [i/grid,(i+1)/grid), each term uses the upper endpoint for the ramp.
# At most N/grid+1 indices per bin; explicitly bound the rounding cost.
bin_total=sum(min(F(i+1,grid),1)*(convolution(i)[1]/(2*ilo**2))**2
              for i in range(2*grid))
cue=(F(1,grid)+F(1,10**70))*bin_total

A=raw_symbol(); L=94; T=2*L+1
lam=F(582843,100000) # strict upper bound for 3+2 sqrt(2)
assert (lam-3)**2>8
# For any |j|<=L all individual telescopes cost at most this amount.
# Each step contributes 80 tau * sum |c| * 14 * lambda^i.
err=80*tau*C*14*lam*(lam**L-1)/(lam-1)
def covariance_sum(n):
    weights={}
    for d,(re,im) in A.items():
        a,b=d
        for j in range(T):
            pair=weights.setdefault((a%n,b%n),[0,0])
            pair[0]+=re;pair[1]+=im
            a,b=(3*a+4*b)%n,(2*a+3*b)%n
    return F(sum(x*x+y*y for x,y in weights.values()),(T*4000)**2)
returns=[]
for k in (197,203,205,207,209):
    n=pell(k); pure=covariance_sum(n)
    speed=sqrt_upper(pure)+err
    centered=1-(k*tau*n*speed)**2/2
    val=w_min*max(centered,0)**2-cue
    assert k*grid<n
    returns.append(dict(k=k,period=str(n),pure_variance=str(pure),speed_upper=ceil8(speed),
                   return_real_lower=floor6(centered),delta_lower=floor6(val)))
assert cue<F(24,1000) and w_min>F(105,1000)
assert F(returns[3]['delta_lower'])>F(2,100)
a=F(26,100); outer_length=F(101,100); n=pell(207)
D=207*tau*n*F(46744,10**6)/(2*pi_lower)
model_hit=2*a+207*outer_length/n+outer_length*(D/a)**2
sine_hit=F(1,2)+sum((-1)**(j+1)*F(2**(2*j-1),factorial(2*j)*(2*j-1)*(2*j))
                     *(pi_lower if j%2 else pi_upper)**(2*j-2) for j in range(1,7))
assert sine_hit-model_hit>F(465,10**4)
print(json.dumps(dict(sine_functional_lower=floor6(sine_lower),progressions=progressions,
      h207_window=dict(model_upper=ceil8(model_hit), sine_lower=floor6(sine_hit), gap_lower=floor6(sine_hit-model_hit)),
      time_length=T,comparison_error_upper=ceil8(err),bump_w_lower=floor6(w_min),
      cue_upper=ceil8(cue),pell_returns=returns), indent=2))
