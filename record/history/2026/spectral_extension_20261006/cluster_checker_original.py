"""Independent exact F5[z]/Phi7 and pi^5 audit of frozen A175 cluster.
No imports from candidate implementation. F5 field/polynomial arithmetic is
schoolbook. Base characteristic polynomials and offset derivatives are also
verified by Leibniz determinants (120 permutations), independent of continuants.
"""
if not __debug__: raise RuntimeError('Assertions required')
import itertools, json, math, hashlib, time, platform
from pathlib import Path
from functools import lru_cache
ROOT=Path(__file__).resolve().parent
class Field:
 def __init__(self,mod):
  self.mod=mod;self.n=len(mod)-1;self.size=5**self.n
 def digits(self,x):
  a=[]
  for _ in range(self.n):a.append(x%5);x//=5
  return a
 def encode(self,a):return sum((x%5)*5**i for i,x in enumerate(a))
 @lru_cache(None)
 def add(self,a,b):return self.encode([(x+y)%5 for x,y in zip(self.digits(a),self.digits(b))])
 @lru_cache(None)
 def neg(self,a):return self.encode([-x for x in self.digits(a)])
 def sub(self,a,b):return self.add(a,self.neg(b))
 @lru_cache(None)
 def mul(self,a,b):
  if not a or not b:return 0
  aa,bb=self.digits(a),self.digits(b);c=[0]*(2*self.n-1)
  for j,x in enumerate(aa):
   for k,y in enumerate(bb):c[j+k]=(c[j+k]+x*y)%5
  for j in range(len(c)-1,self.n-1,-1):
   v=c[j]
   for k,w in enumerate(self.mod):c[j-self.n+k]=(c[j-self.n+k]-v*w)%5
  return self.encode(c[:self.n])
 def power(self,a,k):
  if k<0:return self.power(self.inverse(a),-k)
  b=1
  while k:
   if k&1:b=self.mul(b,a)
   a=self.mul(a,a);k//=2
  return b
 @lru_cache(None)
 def inverse(self,a):
  assert a;v=self.power(a,self.size-2);assert self.mul(v,a)==1;return v
F=Field([1]*7)
# Deterministic irreducibility criterion: Phi7 roots have order 7; ord_7(5)=6.
assert [pow(5,k,7) for k in range(1,7)]==[5,4,6,2,3,1]
assert F.power(5,7)==1 and F.power(5,1)!=1
add,neg,mul,sub=F.add,F.neg,F.mul,F.sub

def trim(p):
 p=list(p)
 while len(p)>1 and p[-1]==0:p.pop()
 return p

def pa(p,q):
 r=[0]*max(len(p),len(q))
 for j in range(len(r)):r[j]=add(p[j] if j<len(p) else 0,q[j] if j<len(q) else 0)
 return trim(r)

def pn(p):return trim([neg(v) for v in p])
def ps(p,c):return trim([mul(v,c) for v in p])
def pm(p,q):
 r=[0]*(len(p)+len(q)-1)
 for j,x in enumerate(p):
  for k,y in enumerate(q):r[j+k]=add(r[j+k],mul(x,y))
 return trim(r)
def pd(p,q):
 p=trim(p);quo=[0]*max(1,len(p)-len(q)+1);qi=F.inverse(q[-1])
 while p!=[0] and len(p)>=len(q):
  d=len(p)-len(q);c=mul(p[-1],qi);quo[d]=c
  for j,y in enumerate(q):p[j+d]=sub(p[j+d],mul(c,y))
  p=trim(p)
 return trim(quo),p

def egcd(a,b):
 a0,b0=list(a),list(b);s,t,u,v=[1],[0],[0],[1]
 while b!=[0]:
  q,r=pd(a,b);a,b=b,r;s,u=u,pa(s,pn(pm(q,u)));t,v=v,pa(t,pn(pm(q,v)))
 inv=F.inverse(a[-1]);g,s,t=ps(a,inv),ps(s,inv),ps(t,inv)
 assert pa(pm(s,a0),pm(t,b0))==g
 return g,s,t

def deriv(p):return trim([mul(j%5,p[j]) for j in range(1,len(p))] or [0])

# Coefficients in F[pi]/pi^5, with fixed precision and no division by pi.
K=5;ZERO=(0,)*K;ONE=(1,)+(0,)*(K-1)
def jc(c):return (c,)+(0,)*(K-1)
def ja(a,b):return tuple(add(x,y) for x,y in zip(a,b))
def jn(a):return tuple(neg(x) for x in a)
def js(a,b):return ja(a,jn(b))
def jm(a,b):
 c=[0]*K
 for j,x in enumerate(a):
  if x:
   for k,y in enumerate(b[:K-j]):
    if y:c[j+k]=add(c[j+k],mul(x,y))
 return tuple(c)
def ji(a):
 assert a[0];b=[F.inverse(a[0])]
 for k in range(1,K):
  s=0
  for j in range(1,k+1):s=add(s,mul(a[j],b[k-j]))
  b.append(neg(mul(s,b[0])))
 assert jm(a,tuple(b))==ONE
 return tuple(b)
def jp(a,k):
 if k<0:return jp(ji(a),-k)
 b=ONE
 while k:
  if k&1:b=jm(b,a)
  a=jm(a,a);k//=2
 return b
Q=(1,1,0,0,0);zeta=5;q=jm(jc(zeta),jp(Q,18));h=88
assert jp(q,7)==Q and jp(q,175)==ONE
@lru_cache(None)
def quantum_integer(x):return tuple(math.comb(x,j+1)%5 if x>=j+1 else 0 for j in range(K))
@lru_cache(None)
def R(x):
 x=x%175
 # Exact r(q^x)/eta after cancellation, then quotient modulo pi^5.
 a=jm(quantum_integer(x),ji(quantum_integer(h)))
 b=js(jp(q,h),ONE);c=ja(jp(q,x),ONE)
 den=jm(jc(4),jp(q,8*x))
 return jn(jm(jm(jm(a,a),jm(b,b)),jm(jm(c,c),ji(den))))
@lru_cache(None)
def D(x):
 # The exact 100*(Q^x-1)^2/(Q^x eta) and 20*R terms vanish mod pi^5.
 return jm(jc(3),jm(R(x),js(jp(q,x%175),jp(q,-(x%175)))))

def factor(x):
 c=F.power(sub(F.power(zeta,4),1),2)
 a=F.power(add(F.power(zeta,x%7),1),2)
 return mul(neg(pow(3,-2,5)),mul(c,mul(a,F.inverse(mul(4,F.power(zeta,8*x%7))))))
def r0(x):return mul(x*x%5,factor(x))
def rd(x):return mul(2*x%5,factor(x))
def d0(x):return mul(3,mul(r0(x),sub(F.power(zeta,x%7),F.power(zeta,-x%7))))
def dd(x):return mul(3,mul(rd(x),sub(F.power(zeta,x%7),F.power(zeta,-x%7))))
# Dual-polynomial pairs in y, used only for separate Leibniz determinant.
def da(a,b):return pa(a[0],b[0]),pa(a[1],b[1])
def dn(a):return pn(a[0]),pn(a[1])
def dm(a,b):return pm(a[0],b[0]),pa(pm(a[1],b[0]),pm(a[0],b[1]))
def leibniz(start):
 A=[[([0],[0]) for k in range(5)]for j in range(5)]
 for j in range(5):
  x=(start+j)%35;A[j][j]=([neg(d0(x)),1],[neg(dd(x))])
  if j<4:
   u=x+18;A[j][j+1]=A[j+1][j]=([neg(r0(u))],[neg(rd(u))])
 ans=([0],[0])
 for perm in itertools.permutations(range(5)):
  p=([1],[0])
  for j,k in enumerate(perm):p=dm(p,A[j][k])
  if sum(perm[j]>perm[k] for j in range(5)for k in range(j+1,5))%2:p=dn(p)
  ans=da(ans,p)
 return ans

def jpa(a,b):
 return [ja(a[j] if j<len(a) else ZERO,b[j] if j<len(b) else ZERO)for j in range(max(len(a),len(b)))]
def jpn(a):return [jn(x)for x in a]
def jps(a,c):return [jm(x,c)for x in a]
def char_jet(start):
 prev=[ONE];cur=[jn(D(start)),ONE]
 for j in range(1,5):
  x=(start+j)%175;b=R((start+j-1+h)%175)
  nxt=jpa([ZERO]+cur,jpn(jps(cur,D(x))))
  nxt=jpa(nxt,jpn(jps(prev,jm(b,b))))
  prev,cur=cur,nxt
 return cur

def source_encode(a):
 S=source_field
 return evaluate_poly(F.digits(a),source_zeta,S)
def evaluate_poly(p,x,f):
 ans=0
 for c in reversed(p):ans=f.add(f.mul(ans,x),c)
 return ans

start_time=time.perf_counter();records=[];certificates=[];jet_count=0;coefficient_count=0
# Source field reproduced by generic arithmetic, without log tables or numpy.
source_field=Field([1,0,1,3,1,0,1]);source_zeta=source_field.power(5,9)
assert source_field.power(source_zeta,7)==1 and source_zeta!=1
assert evaluate_poly([1]*7,source_zeta,source_field)==0
source_deriv=json.loads((ROOT/'source_snapshot/ramified_cluster_derivative.json').read_text())
source_base=json.loads((ROOT/'source_snapshot/pure_five_normalized_spectrum.json').read_text())
for x in range(175):
 assert R(x)[0]==r0(x) and D(x)[0]==d0(x)
 coefficient_count+=2
for cut in [2,7,12,17,22,27,32]:
 start=cut+1;p,z=leibniz(start);px=deriv(p)
 assert [source_encode(a)for a in p]==source_deriv[len(records)]['p']
 assert [source_encode(a)for a in z]==source_deriv[len(records)]['dp_doffset']
 assert [source_encode(a)for a in p]==source_base[0]['chain_characteristic_polynomials'][len(records)]
 for kind,b in [('X-derivative',px),('offset-derivative',z)]:
  g,a,c=egcd(p,b);assert g==[1]
  certificates.append({'kind':kind,'cut':cut,'left':p,'right':b,'bezout_left':a,'bezout_right':c,'gcd':g})
 basejet=char_jet(start);assert [a[0]for a in basejet]==p
 for k in range(5):
  shifted=char_jet((start+35*k)%175)
  # Normalize variable-length derivative coefficient lists.
  expected=[[0]*K for _ in p]
  for j in range(len(p)):expected[j][4]=mul((2*k)%5,z[j] if j<len(z) else 0)
  assert [js(a,b)for a,b in zip(shifted,basejet)]==[tuple(v)for v in expected]
  jet_count+=1
  # Check the actual coefficient dictionary for all 9 positions in each block.
  for j in range(5):
   x=(start+j)%175;xp=(x+35*k)%175
   assert js(D(xp),D(x))==(0,0,0,0,mul((2*k)%5,dd(x)))
   coefficient_count+=1
   if j<4:
    u=(x+h)%175;up=(u+35*k)%175
    assert js(R(up),R(u))==(0,0,0,0,mul((2*k)%5,rd(u)))
    coefficient_count+=1
 records.append({'cut':cut,'p':p,'partial_X':px,'partial_offset':z,'actual_base_characteristic_jet':basejet})
for j in range(7):
 for k in range(j+1,7):
  p,b=records[j]['p'],records[k]['p'];g,a,c=egcd(p,b);assert g==[1]
  certificates.append({'kind':'pair','cuts':[records[j]['cut'],records[k]['cut']],'left':p,'right':b,'bezout_left':a,'bezout_right':c,'gcd':g})
# Reconstruct actual N175 reduced chain polynomial from its five subblocks.
for j,cut in enumerate([12,37,62,87,112,137,162]):
 product=[1]
 for off in range(0,25,5):
  start=(cut+1+off)%175;index=((start-3)//5)%7
  product=pm(product,records[index]['p'])
 assert [source_encode(a)for a in product]==source_base[1]['chain_characteristic_polynomials'][j]
 assert egcd(product,deriv(product))[0]==[1]
# Quantum-integer identity and phase identity, all nonzero shifts.
for k in range(5):
 assert quantum_integer(35*k)==(0,0,0,0,2*k%5)
 assert jp(q,35*k)==ONE
# Cutting into 35 blocks really separates exactly the vanishing residue bonds.
assert [x for x in range(175)if R(x+h)[0]==0]==list(range(2,175,5))
# Independently retain the first possible interblock term in precision pi^9.
# This quotient still has characteristic 5 because v_pi(5)=20.
K=9;ZERO=(0,)*K;ONE=(1,)+(0,)*(K-1);Q=(1,1)+(0,)*(K-2)
q=jm(jc(zeta),jp(Q,18));quantum_integer.cache_clear();R.cache_clear();D.cache_clear()
cut_jets=[]
for x in range(2,175,5):
 u=(x+h)%175;b=R(u);v=next((j for j,c in enumerate(b)if c),None)
 assert v==(None if u%25==0 else 8)
 cut_jets.append({'bond_left':x,'u_mod175':u,'pi_valuation_below9':v,'coefficient_pi8':b[8]})
assert sum(c['pi_valuation_below9']==8 for c in cut_jets)==28
assert sum(c['pi_valuation_below9'] is None for c in cut_jets)==7
result={'claim':'Bounded exact field and pi^5 dictionary for actual normalized A175',
 'arithmetic':'F5[z]/(1+z+...+z^6); J=F5[z,pi]/(Phi7(z),pi^5)',
 'residue_root_encoding':5,'actual_root_jet':'q=z*(1+pi)^18; Q=1+pi',
 'source_field_modulus':source_field.mod,'source_residue_root_encoding':source_zeta,
 'field_irreducibility':'ord_7(5)=6; powers [5,4,6,2,3,1]',
 'base_blocks':records,'bezout_certificates':certificates,'interblock_pi9_jets':cut_jets,
 'checks':{'base_Leibniz_determinants':7,'permutations_per_determinant':120,
 'self_gcd':7,'offset_gcd':7,'pair_gcd':21,'independent_Bezout_identities':len(certificates),
 'actual_block_characteristic_pi5_identities':jet_count,'coefficient_identities':coefficient_count,
 'reconstructed_N175_residue_chain_polynomials':7,'source_json_matches':True,
 'interblock_pi9_jets':35,'internal_interblock_exact_pi_valuation8':28,'actual_zero_boundary_bonds':7},
 'elapsed_seconds':time.perf_counter()-start_time,'python':platform.python_version(),
 'nonclaims':['No uniform 5-adic depth theorem','No U simplicity','No BGS','No formal proof-assistant certificate']}
(ROOT/'independent_cluster_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'checks':result['checks'],'elapsed_seconds':result['elapsed_seconds']},indent=2))
