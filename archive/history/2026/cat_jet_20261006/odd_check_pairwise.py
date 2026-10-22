#!/usr/bin/env python3
"""Fresh arithmetic for the new pairwise input. No candidate-code imports.
Reconstruct accepted characteristic polynomials in F5[W]/Phi7, compare the
pinned t-encoding through an explicit embedding, and compute all three gcds.
"""
import json, itertools, time, platform
from pathlib import Path
ROOT=Path(__file__).resolve().parent
Z=(0,)*6; O=(1,0,0,0,0,0)
def check(b,msg):
 if not b:raise RuntimeError(msg)
def elt(*c):return tuple(list(c)+[0]*(6-len(c)))
def add(a,b):return tuple((x+y)%5 for x,y in zip(a,b))
def scale(a,c):return tuple(c*x%5 for x in a)
def sub(a,b):return add(a,scale(b,-1))
def mul(a,b):
 d=[0]*11
 for i in range(6):
  for j in range(6):d[i+j]+=a[i]*b[j]
 for i in range(10,5,-1):
  c=d[i]
  for j in range(7):d[i-j]-=c
 return tuple(x%5 for x in d[:6])
def power(a,k):
 v=O
 while k:
  if k%2:v=mul(v,a)
  a=mul(a,a);k//=2
 return v
def inv(a):
 check(a!=Z,'zero inverse');b=power(a,15623);check(mul(a,b)==O,'inverse');return b
def trim(p):
 p=p[:]
 while len(p)>1 and p[-1]==Z:p.pop()
 return p
def rem(a,b):
 a=trim(a);b=trim(b);bi=inv(b[-1])
 while a!=[Z] and len(a)>=len(b):
  c=mul(a[-1],bi);j=len(a)-len(b)
  for k,x in enumerate(b):a[k+j]=sub(a[k+j],mul(c,x))
  a=trim(a)
 return a
def gcd(a,b):
 while b!=[Z]:a,b=b,rem(a,b)
 return [mul(x,inv(a[-1])) for x in a]
def pmul(a,b):
 c=[Z]*(len(a)+len(b)-1)
 for j,x in enumerate(a):
  for k,y in enumerate(b):c[j+k]=add(c[j+k],mul(x,y))
 return trim(c)
def evaluate(cs,x):
 v=Z
 for c in cs[::-1]:v=add(mul(v,x),c)
 return v
def resultant(a,b):
 # Sylvester determinant by permutations, independent of Euclid.
 a=a[::-1];b=b[::-1];m=len(a)-1;n=len(b)-1;size=m+n
 rows=[]
 for j in range(n):rows.append([Z]*j+a+[Z]*(n-j-1))
 for j in range(m):rows.append([Z]*j+b+[Z]*(m-j-1))
 v=Z
 for p in itertools.permutations(range(size)):
  term=O
  for j,k in enumerate(p):term=mul(term,rows[j][k])
  sign=(-1)**sum(p[j]>p[k] for j in range(size) for k in range(j+1,size))
  v=add(v,scale(term,sign))
 return v
start=time.time();W=elt(0,1);t=elt(1,3,2,0,1)
check([pow(5,k,7) for k in range(1,7)]==[5,4,6,2,3,1],'irreducibility')
check(power(W,7)==O and W!=O,'seventh root')
check(power(t,9)==W,'pinned root embedding')
check(evaluate([elt(i) for i in [1,0,1,3,1,0,1]],t)==Z,'pinned field embedding')
def decode(x):return evaluate([elt(x//5**j%5) for j in range(6)],t)
# Accepted report, exact characteristic coefficients, in ascending order.
polys=[
 [elt(2,0,0,1,1),elt(4,0,4,1,1,4),elt(2,0,0,1,1),O],
 [elt(0,0,1,4,4,1),elt(4),O],
 [elt(4,0,2,1,1,2),elt(3,0,0,4,4),O]
]
ref=json.loads((ROOT/'inputs/oldform_second_jet_residue.json').read_text())
check(polys==[[decode(x) for x in b['characteristic_coefficients_descending'][::-1]] for b in ref['blocks']],'source coefficients')
rows=[]
for j,k in itertools.combinations(range(3),2):
 g=gcd(polys[j],polys[k]);res=resultant(polys[j],polys[k]);check(g==[O] and res!=Z,'pairwise gcd and resultant')
 rows.append({'blocks':[j,k],'gcd':g,'resultant':res})
product=[O]
for p in polys:product=pmul(product,p)
product_gcd=gcd(product,[scale(product[j],j) for j in range(1,len(product))]);check(product_gcd==[O],'degree-seven product is squarefree')
out={'arithmetic':'F5[W]/(1+W+W^2+W^3+W^4+W^5+W^6), coefficient arrays ascending','author_t_image':t,'polynomials_ascending':polys,'pairwise':rows,'full_product_derivative_gcd':product_gcd,'source_coefficients_match':True,'seconds':time.time()-start,'python':platform.python_version()}
(ROOT/'pairwise_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
