"""Exact Fourier, pressure-variation, fixed-point and Heisenberg-corridor calculations."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from fractions import Fraction as F
from pathlib import Path
import sys,json
root=Path(__file__).resolve().parent
sys.path.insert(0,str(root.parent/'research'))
from coefficients import raw_symbol,pell
# Fourier coefficients with the common factor sqrt(2)*pi omitted.
G={}; A={}
for (a,b),(x,y) in raw_symbol().items():
    sign=1-2*(a*b%2)
    G[b,a]=(F(sign*x,4000),F(sign*y,4000))
    f=b*b-F(a*a,2)
    A[b,a]=tuple(f*c for c in G[b,a])
def cov(power):
    s=F(0);imag=F(0)
    for (b,a),(x,y) in A.items():
        for _ in range(power):b,a=3*b-2*a,-4*b+3*a
        z,w=A.get((b,a),(0,0))
        s+=x*z+y*w;imag+=y*z-x*w
    assert imag==0
    return s
c0,c1=cov(0),cov(1)
assert cov(2)==cov(3)==0 and c0+2*c1>0
def hess(p_twice):
    # q=0, p=0 or 1/2; output Hessian in units pi^2
    return [
        sum(-4*fun(b,a)*(1-2*(a*p_twice%2))*x for (b,a),(x,y) in G.items())
        for fun in [lambda b,a:b*b,lambda b,a:b*a,lambda b,a:a*a]]
fixed=[hess(i) for i in (0,1)]
assert fixed==[[F(-196)+F(392,10)-F(24,500),0,0],[F(-196)+F(392,10)+F(24,500),0,0]]
N=pell(209);t=100;rho=F(1,20)
assert F(N,10**80)<F(501,1000)
s=F(4,100)*F(501,1000)
eta=s/(1-s)
assert (1+eta)**2-1<rho
assert (1+eta)**2<2
c=F(18,10**6)
two=2*rho**t+N*rho**(2*t)
repeat=N**4*(F(2,N)**(t+1))
assert c*c-two-repeat>F(323,10**12)
def txt(a):
    if isinstance(a,list):return list(map(txt,a))
    return str(a)
print(json.dumps(dict(hessians_over_pi_squared=txt(fixed),cov0_over_2pi_squared=str(c0),
    cov1_over_2pi_squared=str(c1),variance_over_pi_squared=str(2*(c0+2*c1)),
    pressure_gap_second_order_over_pi_squared=str((c0+2*c1)/4),
    corridor_signed_lower="3.23e-10",mixing_upper="1/20",N=str(N)),indent=2))
