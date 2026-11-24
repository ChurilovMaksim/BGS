"""Exact rational checks of the Abel energy deficit, including repeated points."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from fractions import Fraction as F
import json

def mul(z,w):
    a,b=z;c,d=w
    return a*c-b*d,a*d+b*c
def power(z,m):
    val=(F(1),F(0))
    for _ in range(m):
        val=mul(z,val)
    return val
def prove(points,r):
    n=len(points)
    def factor(z,w):
        return mul(z,(w[0],-w[1]))
    def poisson(z):
        return (1-r*r)/(1-2*r*z[0]+r*r)
    def fejer(z):
        return sum((n-abs(h))*power(z,abs(h))[0] for h in range(1-n,n))
    D=sum((n-abs(h))*r**(-h) for h in range(1-n,n))
    vals=[(i,j,factor(z,w)) for i,z in enumerate(points) for j,w in enumerate(points)]
    L=(sum(poisson(z) for _,_,z in vals)/n**2-1)/2
    low=F()
    for k in range(1,n-1):
        hk=sum((n-h)*(r**(k-h)-r**(h-k)) for h in range(k+1,n))/D
        low+=hk*sum(power(z,k)[0] for _,_,z in vals)/n**2
    off=sum(poisson(z)*fejer(z) for i,j,z in vals if i!=j)/(2*n*n*D)
    assert L-r**n/(1-r**n)==low+off and low>=0 and off>=0
    return dict(N=n, r=str(r), deficit=str(low+off))
i=(F(0),F(1));q=(F(3,5),F(4,5))
sets=[[power(i,j) for j in range(4)],[q,q,power(i,2),i], [power(q,j) for j in range(7)]]
print(json.dumps([prove(s,r) for s in sets for r in (F(1,2),F(7,8))],indent=1))
