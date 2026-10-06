"""Independent exact symbolic/rational coefficient check. Float strings in output are display only; every acceptance assertion is exact."""
import sympy as s
from fractions import Fraction as F
from math import factorial
import json
z,w=s.symbols('z w'); I=s.I
cos=lambda n:(z**n+z**-n)/2
sin=lambda n:(z**n-z**-n)/(2*I)
r=(1-cos(7))*(1+cos(1))
g=s.expand(cos(7)+r/10+r*sin(1)/100+r.subs(z,-z)*((-3-4*I)*w+(-3+4*I)/w)/1000-s.Rational(1,10))
coeff={}
for a in s.Add.make_args(g):
 p=a.as_powers_dict(); key=(int(p.get(z,0)),int(p.get(w,0)))
 coeff[key]=coeff.get(key,0)+a/z**key[0]/w**key[1]
coeff={k:s.expand(v) for k,v in coeff.items() if v!=0}
assert sum((abs(s.re(v))+abs(s.im(v)))*(k*k+l*l) for (k,l),v in coeff.items())==s.Rational(51451,1000)
assert max(k*k+l*l for k,l in coeff)<100
for a,b,expected in [(0,0,-19606),(0,1,-19594),(1,0,24306),(1,1,24894)]:
 for j in range(2): assert s.expand(sum(I*v*key[j]*(-1)**((key[0]*a+key[1]*b)%2) for key,v in coeff.items()))==0
 for j in range(2):
  for m in range(2):
   h=s.expand(sum(-4*v*key[j]*key[m]*(-1)**((key[0]*a+key[1]*b)%2) for key,v in coeff.items()))
   assert h==(s.Rational(expected,125) if j==m==0 else 0)

def add(a,b): return a[0]+b[0],a[1]+b[1]
def mul(a,b):
 c=[x*y for x in a for y in b]; return min(c),max(c)
def scale(a,b):return mul(a,(b,b))
def power(a,n):
 if n==0:return F(1),F(1)
 if n%2:return a[0]**n,a[1]**n
 return (F(0) if a[0]<=0<=a[1] else min(a[0]**n,a[1]**n), max(a[0]**n,a[1]**n))
def atan(n):
 val=sum((F((-1)**j,(2*j+1)*n**(2*j+1)) for j in range(90)),F(0)); return val,val+F(1,181*n**181)
p=add(scale(atan(5),16),scale(atan(239),-4)); pi=(F('3.14159265358979323846'),F('3.14159265358979323847'));assert pi[0]<p[0]<p[1]<pi[1]
from functools import lru_cache
@lru_cache(None)
def trig(n,odd):
 n=n%7
 if n>3:n-=7
 x=scale(pi,F(2*n,7)); val=(F(0),F(0))
 for j in range(21):val=add(val,scale(power(x,2*j+odd),F((-1)**j,factorial(2*j+odd))))
 err=F(4**(41+odd),factorial(41+odd));return val[0]-err,val[1]+err
out={}
for name,aq,ap in [('I',1,1),('-I',-1,-1),('R0',1,-1),('-R0',-1,1)]:
 val=(F(0),F(0))
 for a,b in [(1,2),(4,1),(2,4)]:
  for (k,l),v in coeff.items():
   n=k*aq*a+l*ap*b
   term=add(scale(trig(n,0),F(s.re(v))),scale(trig(n,1),-F(s.im(v))))
   val=add(val,scale(term,4*(140*k*k-70*l*l)))
 out[name]=val
bounds={'-I':('-520.048877703','-520.048877702'),'R0':('568.942361931','568.942361932'),'-R0':('-1088.991239635','-1088.991239634')}
for name,(lo,hi) in bounds.items():
 d=add(out['I'],scale(out[name],-1));assert F(lo)<=d[0]<=d[1]<=F(hi)
t=F(1,10**12);L=3000;M=200000;B=400;e0=1800000000
# e^x <= 1/(1-x), 0<=x<1, provides a rational bound.
assert 8400*M+(M*B+L*L)/(2*(1-L*t))<e0
rem=4*7**3*(3*e0+3*(L+e0*t)**2+(L+e0*t)**3*t)
assert rem<8*10**12
print(json.dumps({'status':'passed','independence':'Direct symbolic Laurent expansion, independent power-sum rational interval implementation; no author helper imports','coefficients_over_pi_squared':{n:[str(float(v)) for v in vv] for n,vv in out.items()},'exact_pair_remainder_upper':str(rem),'assertions':'Fourier moment, radius, all fixed-point derivatives, all three decimal difference intervals, uniform remainder constant'},indent=2))
