#!/usr/bin/env python3
"""Exact degree-eight local-field controls, no candidate imports.
Q[rho]/(rho^8+5rho^6+10rho^4+10rho^2+5), eta=1+rho^2.
This polynomial is Eisenstein, hence v5(sum c_j rho^j)=min(v5(c_j)+j/8).
"""
from fractions import Fraction as Q
from pathlib import Path
from functools import lru_cache
import json,time,platform
ROOT=Path(__file__).resolve().parent
Z=(Q(0),)*8;ONE=(Q(1),)+(Q(0),)*7
MOD=[5,0,10,0,10,0,5,0,1]
def check(b,msg):
 if not b:raise RuntimeError(msg)
def elt(*cs):return tuple([Q(c) for c in cs]+[Q(0)]*(8-len(cs)))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def sub(a,b):return add(a,neg(b))
def scale(a,c):return tuple(c*x for x in a)
@lru_cache(None)
def mul(a,b):
 c=[Q(0)]*15
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b):
    if y:c[i+j]+=x*y
 for i in range(14,7,-1):
  x=c[i]
  if x:
   for j in range(9):c[i-8+j]-=x*MOD[j]
 return tuple(c[:8])
def power(a,k):
 v=ONE
 while k:
  if k%2:v=mul(v,a)
  a=mul(a,a);k//=2
 return v
def vp_int(a):
 a=abs(a);k=0
 if not a:return 1000000
 while a%5==0:a//=5;k+=1
 return k
def val(a):return min((Q(vp_int(x.numerator)-vp_int(x.denominator))+Q(j,8) for j,x in enumerate(a) if x),default=Q(1000000))
def pmul(a,b):
 c=[Q(0)]*(len(a)+len(b)-1)
 for j,x in enumerate(a):
  for k,y in enumerate(b):c[j+k]+=x*y
 return c
def mm(A,B):
 C=[[Z for _ in B[0]] for _ in A]
 for i in range(len(A)):
  for k in range(len(B)):
   if A[i][k]!=Z:
    for j in range(len(B[0])):C[i][j]=add(C[i][j],mul(A[i][k],B[k][j]))
 return C
def ident(n):return [[ONE if i==j else Z for j in range(n)] for i in range(n)]
def mpow(A,k):
 V=ident(len(A))
 while k:
  if k%2:V=mm(V,A)
  A=mm(A,A);k//=2
 return V
start=time.time();rho=elt(0,1);eta=elt(1,0,1)
rhoinv=elt(0,-2,0,-2,0,-1,0,Q(-1,5));check(mul(rho,rhoinv)==ONE,'rho inverse')
rhop={j:power(rho,j) if j>=0 else power(rhoinv,-j) for j in range(-4,5)}
ep=[power(eta,j) for j in range(5)];check(power(eta,5)==ONE and eta!=ONE,'eta primitive')
# Lagrange interpolation of functions on the five integers.
lag=[]
for x in range(5):
 p=[Q(1)];d=1
 for y in range(5):
  if y!=x:p=pmul(p,[-y,1]);d*=x-y
 lag.append([c/d for c in p])
records=[]
for a in range(5):
 for b in range(5):
  C=[[Z for _ in range(5)] for _ in range(5)]
  for l in range(5):
   for k in range(5):
    s=Z
    for x in range(5):s=add(s,scale(ep[b*(x+3*a)%5],lag[x][l]*((x+a)%5)**k))
    C[l][k]=mul(rhop[k-l],s)
    if l==k:C[l][k]=sub(C[l][k],ONE)
  minimum=min(val(x) for row in C for x in row)
  check(minimum>=Q(1,8),'small Weyl translation')
  records.append({'a':a,'b':b,'minimum_valuation':str(minimum) if (a or b) else 'infinity'})
# Unitarity phase is irrelevant for the lattice sum: either sqrt5 sign gives
# the same lattice and sixth-power identity. Use Gauss normalization here.
g=add(add(ONE,scale(ep[1],2)),scale(ep[4],2));check(mul(g,g)==elt(5),'Gauss square')
gi=scale(g,Q(1,5))
M=[[mul(gi,ep[-2*(3*x*x-2*x*y+3*y*y)%5]) for y in range(5)] for x in range(5)]
check(mpow(M,6)==ident(5),'cat sixth power')
tr=Z
for j in range(5):tr=add(tr,M[j][j])
check(tr==neg(ONE),'Gauss-normalized trace')
# Exact covariance on all 25 raw Weyls, checked over the same field.
def T(a,b):return [[ep[b*(x+3*a)%5] if y==(x+a)%5 else Z for y in range(5)] for x in range(5)]
for a in range(5):
 for b in range(5):check(mm(M,T(a,b))==mm(T((3*a+4*b)%5,(2*a+3*b)%5),M),'raw covariance')
out={'field_polynomial_ascending':MOD,'valuation_normalization':'v5(5)=1; v5(rho)=1/8','all_25_small_translation_checks':records,'gauss_square':5,'gauss_normalized_trace':-1,'cat_sixth_power_identity':True,'weyl_covariance_checks':25,'python':platform.python_version(),'seconds':time.time()-start}
(ROOT/'lattice_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
