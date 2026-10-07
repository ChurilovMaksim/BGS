"""Exact cyclotomic coefficient test for a flat Fourier-row-permutation unitary.
No floating point enters occupation coefficients or their scalar products.
The separately printed Q singular norm is diagnostic only.
"""
import itertools,json,math,sys
from collections import defaultdict
from fractions import Fraction
import numpy as np
p=int(sys.argv[1]) if len(sys.argv)>1 else 5
cap=int(sys.argv[2]) if len(sys.argv)>2 else 6
sigma=[pow(i,3,p) for i in range(p)]
assert len(set(sigma))==p
class C:
 def __init__(self,x=0):
  if isinstance(x,C):self.v=x.v;return
  v=[0]*p
  if isinstance(x,int):v[0]=x
  else:
   for i,a in enumerate(x):v[i%p]+=a
  top=v[-1];self.v=tuple(a-top for a in v[:-1])
 @staticmethod
 def z(k):v=[0]*p;v[k%p]=1;return C(v)
 def __bool__(self):return any(self.v)
 def __add__(self,b):b=C(b);return C([a+d for a,d in zip(self.v,b.v)])
 __radd__=__add__
 def __neg__(self):return C([-a for a in self.v])
 def __sub__(self,b):return self+-C(b)
 def __mul__(self,b):
  b=C(b);v=[0]*p
  for i,a in enumerate(self.v):
   for j,d in enumerate(b.v):v[(i+j)%p]+=a*d
  return C(v)
 __rmul__=__mul__
 def conj(self):
  v=[0]*p
  for i,a in enumerate(self.v):v[-i%p]=a
  return C(v)
 def out(self):return list(self.v)
 def approx(self):return sum(a*np.exp(2j*np.pi*j/p)for j,a in enumerate(self.v))
def padd(A,B):
 out=A.copy()
 for e,v in B.items():out[e]=out.get(e,C())+v
 return {e:v for e,v in out.items() if v}
def pscale(A,c):return {e:v*c for e,v in A.items() if v*c}
def pmul(A,B):
 out={}
 for e,v in A.items():
  for f,w in B.items():
   k=tuple(a+b for a,b in zip(e,f));out[k]=out.get(k,C())+v*w
 return {e:v for e,v in out.items() if v}
def inner(A,B):return sum((v*B[e].conj() for e,v in A.items() if e in B),C())
zero=(0,)*p;one={zero:C(1)}
E=[one]
for k in range(1,min(p,cap)+1):
 ek={}
 for S in itertools.combinations(range(p),k):
  val=C()
  for perm in itertools.permutations(S):
   inv=sum(perm[i]>perm[j] for i in range(k)for j in range(i+1,k))
   exponent=sum(sigma[i]*j for i,j in zip(S,perm))
   val+=C.z(exponent)*(-1 if inv%2 else 1)
  e=tuple(int(i in S)for i in range(p))
  if val:ek[e]=val
 E.append(ek)
h=[one];power=[{}]
rows=[]
for m in range(1,cap+1):
 hm={}
 for k in range(1,min(m,p)+1):hm=padd(hm,pscale(pmul(E[k],h[m-k]),(-1)**(k+1)))
 h.append(hm)
 pm={}
 for k in range(1,min(m-1,p)+1):pm=padd(pm,pscale(pmul(E[k],power[m-k]),(-1)**(k+1)))
 if m<=p:pm=padd(pm,pscale(E[m],(-1)**(m-1)*m))
 power.append(pm)
 if m>=2:
  hook=padd(pmul(h[m-1],E[1]),pscale(h[m],-1))
  cross=inner(hm,hook);realcross=(cross+cross.conj())
  rows.append(dict(m=m,denominator=p**m,twice_real_M01=realcross.out(),M01_complex=cross.out(),B=inner(pm,pm).out(),boson_h_norm=inner(hm,hm).out(),hook_norm=inner(hook,hook).out()))
U=np.array([[np.exp(2j*np.pi*sigma[i]*j/p)/np.sqrt(p)for j in range(p)]for i in range(p)])
Q=U*U.T.conj()
print(json.dumps(dict(p=p,sigma=sigma,arithmetic='exact Z[zeta_p], then division by p^m',Q_operator_norm_float=float(np.linalg.norm(Q,2)),rows=rows),indent=2))
