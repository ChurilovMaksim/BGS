"""Outward Riemann bounds on the negative sector divided by the required plateau correction."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from fractions import Fraction as F
from math import factorial
import json
G=32768; Q=1<<44

def down(x):return x.numerator*Q//x.denominator
def up(x):return -down(-x)
def bump(k):
    if abs(k)>=G:return 0,0
    y=1/(1-F(k*k,G*G))
    if y>=40:
        # e>8/3 and (8/3)^40>2^44.
        assert F(8,3)**40>Q
        return 0,1
    u=y/64
    lo=sum((-u)**i/factorial(i) for i in range(16))
    hi=lo+u**16/factorial(16)
    a,b=down(lo),up(hi)
    for _ in range(6):
        a=a*a//Q;b=(b*b+Q-1)//Q
    return a,b
positive=[bump(i) for i in range(G+1)]
nodes={i:positive[abs(i)] for i in range(-G,G+1)}
cells=[(min(nodes[i][0],nodes[i+1][0]),max(nodes[i][1],nodes[i+1][1])) for i in range(-G,G)]
lo=[x for x,y in cells];hi=[y for x,y in cells]
def convolution(values):
    # Kronecker substitution: the slots are wider than every coefficient of the square.
    width=((len(values)*max(values)**2).bit_length()+7)//8
    poly=int.from_bytes(b''.join(v.to_bytes(width,'little') for v in values),'little')
    packed=(poly*poly).to_bytes((2*len(values)-1)*width,'little')
    start=len(values)-1
    return [int.from_bytes(packed[i*width:(i+1)*width],'little')
            for i in range(start,2*len(values)-1)]+[0]
cl=convolution(lo);ch=convolution(hi)
den=G*(2*G)**16*factorial(17)
factors=[(2*G)**(16-2*j)*(factorial(17)//factorial(2*j+1)) for j in range(1,8)]
def kernel(k):
    num=k*sum(v*k**(2*j) for j,v in enumerate(factors,1))
    return Q*num//den,(Q*(num+2*k**17)+den-1)//den
kernels=[kernel(k) for k in range(2*G+1)]
a=sum(kernels[k][0]*cl[k+1]**2 for k in range(2*G))
b=sum(kernels[k+1][1]*ch[k]**2 for k in range(2*G))
c=sum((k-G)*cl[k+1]**2 for k in range(G,2*G))
d=sum((k+1-G)*ch[k]**2 for k in range(G,2*G))
lower,upper=F(a*G,Q*d),F(b*G,Q*c)
assert F(299,100)<lower<upper<3
# Change the increasing numerator kernel to t^3/6 for the moving interval.
cubic_lo=F(sum(k**3*cl[k+1]**2 for k in range(2*G)),6*G**2*d)
cubic_hi=F(sum((k+1)**3*ch[k]**2 for k in range(2*G)),6*G**2*c)
assert 11<cubic_lo<cubic_hi<12
print(json.dumps(dict(cubic_lower=str(cubic_lo),cubic_upper=str(cubic_hi),
                      cubic_lower_decimal=float(cubic_lo),cubic_upper_decimal=float(cubic_hi),
                      grid_per_unit=G,lower=str(lower),upper=str(upper),
                      lower_decimal=float(lower),upper_decimal=float(upper)),indent=2))
