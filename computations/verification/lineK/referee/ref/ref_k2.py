# Referee: independent recomputation of K2 threshold l_m = L_m^{1/m} (continuous s optimisation), crossover by bisection.
from mpmath import mp, mpf, log, sqrt, exp, findroot
import math
mp.dps=30
mu=mpf('1.9154753'); xi=mpf('2.4586893'); K=mpf('0.009985'); eps=1+sqrt(2)
def logl(m,SZ):
    p=m//3; P=2*p+1; w=math.floor(m*log(eps)/log(P))
    T=log(mpf('0.01')*K/2)+m*log(xi)-log(SZ)-2*m*log(mu)
    best=None
    for i in range(1,4000):
        s=mpf(i)/4000
        E=-log(1-mpf(7)**(-s))-w*log(1-mpf(P)**(-s))
        v=(E-T)/(1-s)/m
        if best is None or v<best: best=v
    return best
def nontriv(m,SZ): return logl(m,SZ) < (m*log(eps)-log(2))/(2*m)
for SZ in (mpf(10)**8, mpf(10)**14):
    lo,hi=3*10**7, 3*10**10
    assert not nontriv(lo,SZ) and nontriv(hi,SZ)
    while hi/lo>1.01:
        mid=int(math.sqrt(lo*hi)); mid-=mid%3
        if nontriv(mid,SZ): hi=mid
        else: lo=mid
    print('S_Z=%g crossover m in [%.3e, %.3e]'%(SZ,lo,hi))
for m in (501,3027,300009):
    print(m, float(exp(logl(m,mpf(10)**8))), 'eta*log(2p+1)=', float((logl(m,mpf(10)**8)/log(mu*mu/xi)-1)*log(2*(m//3)+1)))
