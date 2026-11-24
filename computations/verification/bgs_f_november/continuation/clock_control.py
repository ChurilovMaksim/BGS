"""Rational Darboux bounds for the explicit b_* test on the exactly flat clock control."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from fractions import Fraction as F
from functools import lru_cache
import json
Q=1<<36
K=128
def floorq(x):return (x.numerator*Q)//x.denominator
@lru_cache(None)
def bump(k):
    # k/K in [-1,1]. Values are outward-rounded integer numerators.
    if abs(k)>=K:return 0,0
    x=1/(1-F(k*k,K*K));n=512
    lo=(1-x/n)**n;hi=1/(1+x/n)**n
    return floorq(lo), -floorq(-hi)
def interval(k):
    a,b=bump(k),bump(k+1)
    return min(a[0],b[0]),max(a[1],b[1])
def convolution(t):
    u=v=0
    for k in range(-K,K):
        lo,hi=interval(k);p,q=interval(t-k-1)
        u+=lo*p;v+=hi*q
    return F(u,K*Q**2),F(v,K*Q**2)
H={t:convolution(int(t*K)) for t in [F(1,2),F(3,4),F(1)]}
imax=sum(F(interval(j)[1],K*Q) for j in range(-K,K))
# The common positive normalizer is 4 I^4. Convolution of two symmetric
# decreasing functions is symmetric decreasing (layer cake and interval overlaps).
diff=H[1][1]**2-F(1,8)*H[F(1,2)][0]**2-F(5,32)*H[F(3,4)][0]**2
assert diff<0
bound=diff/(4*imax**4)
assert bound<-F(1,1000)
print(json.dumps(dict(P_clock_upper_rational=str(bound),P_clock_upper_approx=float(bound),
                       input_cells=2*K,strict_threshold="-1/1000"),indent=2))
