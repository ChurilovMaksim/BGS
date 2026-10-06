"""Independent full-branch, integer-frequency controls, exact cyclotomic arithmetic.
No author code imported; B inverse is rational adjugate/determinant, never mod N.
"""
import itertools,json,math,time
from collections import Counter
from pathlib import Path
import numpy as np
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form

def matrix(m):
 b=s.zeros(m)
 for i in range(m):
  b[i,i]+=6
  b[i,(i+1)%m]-=1
  b[i,(i-1)%m]-=1
 return b

def reduce_poly(arr,C):
 x=s.Symbol('x'); phi=s.Poly(s.cyclotomic_poly(C,x),x)
 terms=[(int(k[0]),int(v)) for k,v in phi.terms()]
 degree=phi.degree(); low=[(k,v) for k,v in terms if k!=degree]
 a=list(map(int,arr))
 for k in range(len(a)-1,degree-1,-1):
  coeff=a[k]
  if coeff:
   for j,v in low:a[k-degree+j]-=coeff*v
   a[k]=0
 return a[:degree]

def run(m,N,n):
 if (m,N) not in [(1,3),(2,3),(3,7),(4,3),(4,9)] or len(n) != m or any(type(v) is not int or abs(v)>9 for v in n):
  raise ValueError("outside certified exact int64 fixture bounds")
 B=matrix(m);D=int(B.det()); Adj=np.array(B.adjugate()).astype(np.int64)
 H=hermite_normal_form(B)
 reps=np.array(list(itertools.product(*(range(int(H[i,i])) for i in range(m)))),dtype=np.int64)
 if len(reps)!=D: raise RuntimeError("quotient count mismatch")
 # Distinctness of quotient representatives proved by HNF; independently check residue signatures.
 if len({tuple(z%D) for z in reps@Adj})!=D: raise RuntimeError("duplicate quotient residue")
 n=np.array(n,dtype=np.int64);C=8*N*D
 q=np.zeros(C,dtype=np.int64)
 for r0 in itertools.product(range(4),repeat=m):
  r=np.array(r0,dtype=np.int64);t=r-3*np.roll(r,1);v=t+4*reps
  num=N*N*np.einsum('ij,jk,ik->i',v,Adj,v)-3*N*N*D*int(r@r)+8*N*(v@Adj@n)+16*int(n@Adj@n)+(3*m*N-m)*N*D
  q+=np.bincount(num%C,minlength=C)
 # Raw modular metaplectic trace, with separate diagonal frequency insertions.
 j=np.array(list(itertools.product(range(N),repeat=m)),dtype=np.int64)
 b=np.array(B).astype(np.int64);inv8=pow(8,-1,N) if N>1 else 0
 phase=(-inv8*np.einsum('ij,jk,ik->i',j,b,j)+j@n)%N
 p=np.bincount(phase*(C//N),minlength=C)
 # Compare 4^m sqrt(D) P - N^(m/2) Q = 0, with Maslov and global e phase already in Q.
 # Exact radicals represented by quadratic Gauss sums or zeta_8+zeta_8^-1.
 if m==4:
  diff=(4**m*24)*(np.roll(p,C//8)+np.roll(p,-C//8))-N*N*q
 elif m==3 and N==7:
  # sqrt(7)=-i sum_{a mod7} e(a²/7).
  sqrt7q=sum((np.roll(q,((a*a)%7)*(C//7)-C//4) for a in range(7)),np.zeros(C,dtype=np.int64))
  diff=4**m*14*p-N*sqrt7q
 elif m==2:
  diff=4**m*4*(np.roll(p,C//8)+np.roll(p,-C//8))-N*q
 elif m==1 and N==3:
  sqrt3q=sum((np.roll(q,((a*a)%3)*(C//3)-C//4) for a in range(3)),np.zeros(C,dtype=np.int64))
  diff=4**m*2*p-sqrt3q
 else:raise ValueError((m,N))
 rem=reduce_poly(diff,C)
 if any(rem): raise RuntimeError((m,N,n.tolist(),[(i,v) for i,v in enumerate(rem) if v][:4]))
 return dict(m=m,N=N,frequency=n.tolist(),det=D,gcd=math.gcd(D,N),conductor=C,quotient_count=len(reps),cyclotomic_remainder_zero=True)

def main():
 started=time.time();results=[]
 for m,N in [(1,3),(2,3),(3,7),(4,3),(4,9)]:
  for n in [list(range(1,m+1)),[(-1)**i*(2*i+3) for i in range(m)]]:
   result=run(m,N,n);results.append(result);print(result,flush=True)
 print(json.dumps(dict(results=results,seconds=time.time()-started,arithmetic='integer histogram plus exact cyclotomic polynomial division; no floating point'),indent=2)+'\n')

if __name__ == '__main__':
 main()
