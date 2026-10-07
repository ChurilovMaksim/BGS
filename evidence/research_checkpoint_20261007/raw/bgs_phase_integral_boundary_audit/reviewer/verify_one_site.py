import sympy as s
from functools import reduce
# Independent exterior-algebra calculation with ordered generators gamma,beta,alpha,delta.
a,b,c,d,z,zb,w,wb,t,x,T=s.symbols('a b c d z zb w wb t x T')
class E:
 def __init__(self,v): self.v={k:s.expand(c) for k,c in (v if isinstance(v,dict) else {0:s.sympify(v)}).items() if c!=0}
 def __add__(self,o):
  o=o if isinstance(o,E) else E(o); v=self.v.copy()
  for k,c in o.v.items(): v[k]=v.get(k,0)+c
  return E(v)
 __radd__=__add__
 def __neg__(self): return E({k:-v for k,v in self.v.items()})
 def __sub__(self,o): return self+-coerce(o)
 def __rsub__(self,o): return coerce(o)+-self
 def __mul__(self,o):
  o=coerce(o); v={}
  for i,ci in self.v.items():
   for j,cj in o.v.items():
    if i&j:continue
    inv=sum(1 for p in range(4) for q in range(4) if i>>p&1 and j>>q&1 and p>q)
    v[i|j]=v.get(i|j,0)+(-1)**inv*ci*cj
  return E(v)
 __rmul__=__mul__
 def inv(self):
  body=self.v.get(0,0); nil=self-E(body); out=E(1/body); term=E(1/body)
  for k in range(1,5): term=term*(-nil)*E(1/body);out=out+term
  return out
 def norm(self):return E({k:s.factor(v) for k,v in self.v.items()})
def coerce(o):return o if isinstance(o,E) else E(o)
gamma,beta,alpha,delta=[E({1<<j:1}) for j in range(4)]
Z=[[E(z),alpha],[beta,E(w)]]
Ztilde=[[E(zb),gamma],[delta,E(-wb)]]
def matmul(A,B):return [[sum((A[i][k]*B[k][j] for k in range(2)),E(0)) for j in range(2)]for i in range(2)]
def one_minus(A):return [[E(int(i==j))-A[i][j] for j in range(2)]for i in range(2)]
def invsdet(M):
 # D-C A^-1 B divided by A; BB body cannot vanish for |ab|<1.
 return (M[1][1]-M[1][0]*M[0][0].inv()*M[0][1])*M[0][0].inv()
def sdet(M):return invsdet(M).inv()
AZB=[[Z[i][j]*[a,c][i]*[b,d][j] for j in range(2)]for i in range(2)]
S=sdet(one_minus(matmul(Ztilde,Z))).norm()
F=invsdet(one_minus(matmul(Ztilde,AZB))).norm()
SF=(S*F).norm()
def radial(expr):return s.factor(s.expand(expr).subs(z*zb,t).subs(w*wb,x))
q,r,u,v=a*b,c*d,b*c,a*d
J,H=1-q*t,1+x
expected=(1-x)*(1+r*x)/(H**3*J)-(u+v+2*q*r*t*x)/(H**2*J**2)+q*r*(1-t)*(1+q*t)/(H*J**3)
assert s.factor(radial(SF.v[15])-expected)==0
print('PASS direct inverse Berezinian exterior algebra -> bulk integrand')
assert s.factor(radial(F.v[15])-q*r*(1+q*t)/J**3)==0
print('PASS inverse Berezinian quartic coefficient')
L=gamma*beta+alpha*delta+gamma*w*delta*z-alpha*wb*beta*zb
Omega2=-L*E(1/(2*H))
# Quartic surface multiplication sees degree-2 SF; quartic derivative sees body SF.
surf_top=radial((Omega2*SF).v.get(15,0)).subs(t,1)
body=radial(SF.v[0]);surf_top+=body.subs(t,1)/(2*H**2)+2*s.diff(body,t).subs(t,1)/(4*H)
assert s.factor(surf_top-(1+r*x)/(2*H**2*(1-q)))==0
print('PASS source surface operator including normal derivative')
# Verify closed radial integrals using derivatives, with removable q=0 handled by continuation.
q0,r0,u0,v0=s.symbols('q r u v')
ell=-s.log(1-q0)/q0
B=(1-r0)*ell*T/(1+T)**2+((2*r0-u0-v0)*T/(1+T)-r0*s.log(1+T))/(1-q0)
Surf=((1-r0)*T/(1+T)+r0*s.log(1+T))/(1-q0)
# integrate t analytically via elementary primitives.
I=(q0/(1-q0)+s.log(1-q0))/q0**2
bulk_t=ell*(1-T)*(1+r0*T)/(1+T)**3-(u0+v0)/((1-q0)*(1+T)**2)+q0*r0*I*(1-T)/(1+T)**2
assert s.simplify(s.diff(B,T)-bulk_t)==0
assert s.simplify(s.diff(Surf,T)-(1+r0*T)/((1-q0)*(1+T)**2))==0
assert B.subs(T,0)==0 and Surf.subs(T,0)==0
assert s.simplify(B+Surf-(1-r0)*ell*T/(1+T)**2-(1+r0-u0-v0)*T/((1-q0)*(1+T)))==0
print('PASS exact cutoff antiderivatives and combined expression')
print('bulk(T) =', B)
print('surface(T) =', Surf)
print('combined limit = (1+cd-bc-ad)/(1-ab)')
