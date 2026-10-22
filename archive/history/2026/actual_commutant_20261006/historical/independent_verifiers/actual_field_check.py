import numpy as np,sympy as s,json,time
from pathlib import Path
R=Path('/workspace/shared/bgs_seven_adic_independent_review');S=R/'actual_source';q=s.symbols('q');F=s.Poly(s.cyclotomic_poly(49,q),q,modulus=5);degree=42
# Reduction table from exact remainders, not author's specialized reshape reduction.
tab=np.zeros((83,42),dtype=np.int64)
for k in range(83):
 for (j,),v in s.Poly(q**k,q,modulus=5).rem(F).terms():tab[k,j]=int(v)%5
zero=np.zeros(42,dtype=np.int64);one=zero.copy();one[0]=1
powers=tab[:49]
def mul(a,b):return np.convolve(a,b)@tab%5
def inv(a):
 z=s.invert(s.Poly.from_list(list(map(int,a[::-1])),q,modulus=5),F);v=zero.copy()
 for (j,),c in z.terms():v[j]=int(c)%5
 assert np.array_equal(mul(a,v),one)
 return v

def rank(A):
 A=A.copy()%5;r=0
 for c in range(A.shape[1]):
  inds=[k for k in range(r,len(A)) if np.any(A[k,c])]
  if not inds:continue
  A[[r,inds[0]]]=A[[inds[0],r]];iv=inv(A[r,c])
  for j in range(c,A.shape[1]):A[r,j]=mul(A[r,j],iv)
  for k in range(r+1,len(A)):
   coeff=A[k,c].copy()
   if np.any(coeff):
    for j in range(c+1,A.shape[1]):A[k,j]=(A[k,j]-mul(coeff,A[r,j]))%5
    A[k,c]=zero
  r+=1
  if r==len(A):break
 return r

def inverse(A):
 B=np.zeros((7,14,42),dtype=np.int64);B[:,:7]=A
 for i in range(7):B[i,i+7]=one
 for c in range(7):
  k=next(k for k in range(c,7) if np.any(B[k,c]));B[[k,c]]=B[[c,k]];iv=inv(B[c,c])
  for j in range(14):B[c,j]=mul(iv,B[c,j])
  for k in range(7):
   if k!=c:
    a=B[k,c].copy()
    for j in range(14):B[k,j]=(B[k,j]-mul(a,B[c,j]))%5
 return B[:,7:]
def dot(a,b):return sum((mul(x,y) for x,y in zip(a,b)),zero.copy())%5
def ev(expr):
 a=zero.copy()
 for (k,),v in s.Poly(s.sympify(expr),q,modulus=5).terms():a=(a+int(v)*powers[k%49])%5
 return a
start=time.time();yd=json.loads((S/'bounded_boundary_polynomials.json').read_text());kd=json.loads((S/'bounded_boundary_norm_input.json').read_text());dicts=[]
for k in range(1,7):
 V=np.zeros((7,7,42),dtype=np.int64)
 for t in range(7):
  for j in range(7):
   den=one.copy()
   for u in range(1,t+1):den=mul(den,mul((one+powers[(u+7*k*j)%49])%5,(one+powers[(u+7*k*j)%49])%5))
   V[t,j]=mul(powers[(7*k*j*(2*t+3))%49],inv(den))
 VI=inverse(V);y=[dot([powers[7*k*j%49] for j in range(7)],VI[:,t]) for t in range(7)]
 for j in range(7):assert np.array_equal(mul(y[j],ev(yd['denominator'])),ev(yd['y_numerators'][j]))
 qs=[inv(mul((one+powers[(7*k-1+7*k*j)%49])%5,(one+powers[(7*k-1+7*k*j)%49])%5)) for j in range(7)]
 kval=dot([mul(V[0,j],qs[j]) for j in range(7)],VI[:,0]);numer=sum((mul(ev(c),powers[7*k*j%49]) for j,c in enumerate(kd['coefficients_w'])),zero.copy())%5
 den=mul(ev(kd['denominator']),mul((one+powers[7])%5,(one+powers[7])%5))
 assert np.array_equal(mul(kval,den),numer)
 assert np.any(kval) and all(np.any(v) for v in y[1:])
 dicts.append(k)
print('Six direct extension-field dictionaries passed',flush=True)
# Actual B from Laurent polynomial; G acts using precomputed multiplication matrices.
b=[]
for x in range(49):
 z=powers[(x+25)%49];z7=powers[(7*(x+25))%49]
 rr=-mul(mul((z7-one)%5,(z7-one)%5),mul((z+one)%5,(z+one)%5))%5
 rr=mul(rr,inv(4*powers[(8*(x+25))%49]%5));b.append(4*rr%5)
assert sum(not np.any(v) for v in b)==7
mult=np.zeros((49,42,42),dtype=np.int64)
for k in range(49):
 for j in range(42):mult[k,:,j]=powers[(k+j)%49]
exps=np.array([[-pow(8,-1,49)*(3*x*x-2*x*y+3*y*y)%49 for y in range(49)] for x in range(49)])
GT=mult[exps]
def upper(v):return np.array([mul(b[x],v[(x+1)%49]) for x in range(49)])
def step(v):return (upper(v)+np.einsum('xyij,yj->xi',GT,v))%5
v=np.zeros((49,42),dtype=np.int64);v[0]=one;w=upper(v);K=[];D=[]
for t in range(49):
 K.append(v.copy());D.append((w-upper(v))%5);v=step(v);w=step(w)
rk=rank(np.array(K).transpose(1,0,2));rd=rank(np.array(D).transpose(1,0,2));assert rk==49 and rd==48
out={'direct_dictionary_w_powers':dicts,'base49_cyclic_rank':rk,'base49_commutator_rank':rd,'seven_zero_bonds':True,'seconds':time.time()-start};(R/'actual_field_results.json').write_text(json.dumps(out,indent=2));print(json.dumps(out),flush=True)
