#!/usr/bin/env python3
"""Independent audit, no author imports. Direct F5[W]/Phi7 polynomial arithmetic.
Actual coefficients are assembled from the raw trigonometric symbol. K is built
by products of Weyl matrices; characteristic polynomials by permutation determinants.
"""
if not __debug__: raise RuntimeError("Assertions are required")
import json, hashlib, itertools, platform, time
from pathlib import Path
from functools import lru_cache
from fractions import Fraction as Q
ROOT=Path(__file__).resolve().parent
START=time.time()
def add(a,b): return tuple((x+y)%5 for x,y in zip(a,b))
def neg(a): return tuple(-x%5 for x in a)
def sub(a,b): return add(a,neg(b))
Z=(0,)*6; ONE=(1,0,0,0,0,0); W=(0,1,0,0,0,0)
def const(a): return (a%5,0,0,0,0,0)
@lru_cache(None)
def mul(a,b):
 c=[0]*11
 for i,x in enumerate(a):
  for j,y in enumerate(b): c[i+j]+=x*y
 for j in range(10,5,-1):
  v=c[j]%5
  for k in range(j-6,j):c[k]-=v
 return tuple(x%5 for x in c[:6])
def power(a,n):
 if n<0:return power(inv(a),-n)
 ans=ONE
 while n:
  if n&1:ans=mul(ans,a)
  a=mul(a,a);n//=2
 return ans
def inv(a):
 assert a!=Z
 return power(a,15623)
def summ(xs):
 a=Z
 for x in xs:a=add(a,x)
 return a
def enc(a):return sum(c*5**j for j,c in enumerate(a))
def decode(v):return tuple(v//5**j%5 for j in range(6))
def evalpoly(cs,x):
 ans=Z
 for c in reversed(cs):ans=add(mul(ans,x),c)
 return ans
def zero(n,m=None):return [[Z for _ in range(m or n)]for _ in range(n)]
def ident(n):return [[ONE if i==j else Z for j in range(n)]for i in range(n)]
def madd(A,B):return [[add(x,y)for x,y in zip(a,b)]for a,b in zip(A,B)]
def mscale(c,A):return [[mul(c,x)for x in row]for row in A]
def mm(A,B):return [[summ(mul(a,b)for a,b in zip(row,col))for col in zip(*B)]for row in A]
def trace(A):return summ(A[j][j]for j in range(len(A)))
def nullspace(A):
 A=[row[:]for row in A]; nr=len(A);nc=len(A[0]);piv=[];r=0
 for j in range(nc):
  k=next((k for k in range(r,nr)if A[k][j]!=Z),None)
  if k is None:continue
  A[r],A[k]=A[k],A[r];A[r]=[mul(inv(A[r][j]),x)for x in A[r]]
  for k in range(nr):
   if k==r:continue
   v=A[k][j];A[k]=[sub(x,mul(v,y))for x,y in zip(A[k],A[r])]
  piv.append(j);r+=1
  if r==nr:break
 free=[j for j in range(nc)if j not in piv];V=zero(nc,len(free))
 for a,j in enumerate(free):
  V[j][a]=ONE
  for k,p in enumerate(piv):V[p][a]=neg(A[k][j])
 return V,free

def ptrim(a):
 while len(a)>1 and a[-1]==Z:a.pop()
 return a
def padd(a,b):return ptrim([add(a[j]if j<len(a)else Z,b[j]if j<len(b)else Z)for j in range(max(len(a),len(b)))])
def pmul(a,b):
 c=[Z]*(len(a)+len(b)-1)
 for j,x in enumerate(a):
  for k,y in enumerate(b):c[j+k]=add(c[j+k],mul(x,y))
 return ptrim(c)
def prem(a,b):
 a=a[:]
 while a!=[Z]and len(a)>=len(b):
  m=len(a)-len(b);c=mul(a[-1],inv(b[-1]))
  for j,x in enumerate(b):a[j+m]=sub(a[j+m],mul(c,x))
  ptrim(a)
 return a
def pgcd(a,b):
 while b!=[Z]:a,b=b,prem(a,b)
 return [mul(x,inv(a[-1]))for x in a]
def charpoly(A):
 n=len(A);p=[Z]
 for perm in itertools.permutations(range(n)):
  term=[const((-1)**sum(perm[i]>perm[j]for i in range(n)for j in range(i+1,n)))]
  for i,j in enumerate(perm):term=pmul(term,[neg(A[i][j]),ONE]if i==j else[neg(A[i][j])])
  p=padd(p,term)
 return p

# Irreducibility of Phi7 follows from ord_7(5)=6, checked directly.
assert [pow(5,k,7)for k in range(1,7)]==[5,4,6,2,3,1]
assert power(W,7)==ONE and W!=ONE
for x in [W,add(W,ONE),add(W,const(2))]:assert mul(x,inv(x))==ONE
# Identify exact embedding of the author's t without using its arithmetic.
g=next(decode(i)for i in range(2,15625)if all(power(decode(i),15624//p)!=ONE for p in [2,3,7,31]))
t63=power(g,15624//63)
t_candidates=[power(t63,k)for k in range(1,63)if power(power(t63,k),9)==W and evalpoly([const(j)for j in [1,0,1,3,1,0,1]],power(t63,k))==Z]
assert len(t_candidates)==1;t=t_candidates[0]
def from_author(x):return evalpoly([const(d)for d in decode(x)],t)

# Assemble exact raw centered symbol without author coefficient tables.
def ga(a,b=(Q(0),Q(0))):return(a[0]+b[0],a[1]+b[1])
def gm(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
r={}
for a,ca in {0:Q(1),7:Q(-1,2),-7:Q(-1,2)}.items():
 for b,cb in {0:Q(1),1:Q(1,2),-1:Q(1,2)}.items():r[a+b]=r.get(a+b,Q(0))+ca*cb
cs={}
def put(v,c):cs[v]=ga(cs.get(v,(Q(0),Q(0))),c)
put((0,7),(Q(1,2),Q(0)));put((0,-7),(Q(1,2),Q(0)));put((0,0),(Q(-1,10),Q(0)))
for b,c in r.items():
 put((0,b),(c/10,Q(0)))
 put((0,b+1),(Q(0),-c/200));put((0,b-1),(Q(0),c/200))
 put((1,b),(-3*c/1000,-4*c/1000));put((-1,b),(-3*c/1000,4*c/1000))
coeff={v:tuple(int(4000*x)for x in c)for v,c in cs.items()if c!=(0,0)}
assert len(coeff)==32 and (0,0)not in coeff
assert all(x.denominator==1 for c in cs.values()for x in [4000*c[0],4000*c[1]])
def vp_gauss(c):
 a,b=c;k=0
 while (2*a-b)%5==0 and (a+2*b)%5==0:a,b=(2*a-b)//5,(a+2*b)//5;k+=1
 return k
vals={v:vp_gauss(c)for v,c in coeff.items()}
assert all(vals[v]==0 for v in coeff if v[0]==1)
assert all(vals[v]==2 for v in coeff if v[0]==-1)
assert all(vals[v]>=1 for v in coeff if v[0]==0)

def sv(v,m):a,b=v;return((3*a+4*b)%m,(2*a+3*b)%m)
def spowv(v,k,m):
 for _ in range(k):v=sv(v,m)
 return v
wp=[power(W,j)for j in range(7)]
def T(v):
 a,b=v;return [[wp[b*(x+4*a)%7]if y==(x+a)%7 else Z for y in range(7)]for x in range(7)]
G=[[wp[-(3*x*x-2*x*y+3*y*y)%7]for y in range(7)]for x in range(7)]
tau=trace(G);H=mscale(inv(tau),G);I=ident(7);H2=mm(H,H)
assert mm(H2,H)==I and tau!=Z
for v in coeff:assert mm(G,T(v))==mm(T(sv(v,7)),G)
K=zero(7);pairs=[]
upper=[v for v in coeff if v[0]==1]
for v in upper:
 for u in upper:
  qv=2*v[1]**2-v[0]**2
  if qv!=2*u[1]**2-u[0]**2:continue
  ks=[k for k in range(6)if tuple((a+b)%5 for a,b in zip(v,spowv(u,k,5)))==(0,0)]
  assert len(ks)==1;k=ks[0];s=spowv(u,k,7)
  dv=(coeff[v][0]+2*coeff[v][1])%5;du=(coeff[u][0]+2*coeff[u][1])%5
  scalar=const(2*dv*du*pow(qv%5,-1,5));product=mm(T(v),T(s));om=v[0]*s[1]-v[1]*s[0]
  assert product==mscale(wp[4*om%7],T((v[0]+s[0],v[1]+s[1])))
  K=madd(K,mscale(scalar,product));pairs.append({'v':v,'u':u,'k_mod6':k,'norm':qv,'factor':enc(scalar),'weyl_label':[(v[j]+s[j])%7 for j in range(2)],'cocycle_coefficient':enc(mul(scalar,wp[4*om%7]))})
assert len(pairs)==17
ref=json.loads((ROOT/'inputs/oldform_second_jet_residue.json').read_text())
assert K==[[from_author(v)for v in row]for row in ref['matrix']]
assert {tuple(x['v'])for x in ref['pairs']}==set(upper)
for p in pairs:
 rp=next(x for x in ref['pairs']if tuple(x['v'])==p['v']and tuple(x['u'])==p['u'])
 assert rp['k_mod6']==p['k_mod6']and rp['weyl_label']==p['weyl_label']and from_author(rp['coefficient'])==decode(p['cocycle_coefficient'])
assert {from_author(x['eigenvalue'])for x in ref['blocks']}=={ONE,power(g,15624//3),power(g,2*15624//3)}
blocks=[]
for rb in ref['blocks']:
 gamma=from_author(rb['eigenvalue']);assert power(gamma,3)==ONE
 P=mscale(const(2),madd(madd(I,mscale(inv(gamma),H)),mscale(power(gamma,-2),H2)))
 assert mm(P,P)==P
 V,free=nullspace(madd(H,mscale(neg(gamma),I)));PV=mm(P,mm(K,V));C=[PV[j]for j in free]
 assert mm(V,C)==PV
 cp=charpoly(C);der=[mul(const(j),cp[j])for j in range(1,len(cp))];gcd=pgcd(cp,der)
 assert gcd==[ONE]
 assert cp[::-1]==[from_author(x)for x in rb['characteristic_coefficients_descending']]
 assert C==[[from_author(x)for x in row]for row in rb['compression']]
 blocks.append({'gamma':enc(gamma),'dimension':len(C),'compression':[[enc(x)for x in row]for row in C],'characteristic_coefficients_descending':[enc(x)for x in cp[::-1]],'gcd_coefficients':[enc(x)for x in gcd]})
assert [x['dimension']for x in blocks]==[3,2,2]
result={'field':'F5[W]/(W^6+W^5+W^4+W^3+W^2+W+1), base5 encodings','author_t_image':enc(t),'independent_coefficients':[{'v':v,'d':c,'valuation_at_i_2':vals[v]}for v,c in sorted(coeff.items())],'pairs':pairs,'matrix':[[enc(x)for x in row]for row in K],'blocks':blocks,'all_candidate_matrix_pair_compression_polynomials_match':True,'seconds':time.time()-START,'python':platform.python_version()}
(ROOT/'residue_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'blocks':blocks,'author_t_image':enc(t),'seconds':time.time()-START},indent=2))
