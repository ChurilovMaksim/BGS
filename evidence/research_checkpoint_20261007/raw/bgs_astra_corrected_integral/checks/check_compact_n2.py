"""Exact compact color-one functional check for a genuinely coupled 2x2 unitary.
Sparse super-polynomials, independent of all previous exterior implementations.
Arithmetic: fractions.Fraction; source ratios c,d are formal variables.
Checks through t^(2*ORDER), defaults ORDER=3. This is a finite check only.
"""
from fractions import Fraction as Q
from collections import defaultdict
import json,sys,time
ORDER=int(sys.argv[1]) if len(sys.argv)>1 else 3
N=2; NE=4*N+2
zeroexp=(0,)*NE
class P:
 def __init__(self,terms=None): self.t={k:v for k,v in (terms or {}).items() if v}
 @staticmethod
 def c(c):return P({(0,zeroexp):Q(c)})
 def __add__(self,b):
  if not isinstance(b,P):b=P.c(b)
  out=self.t.copy()
  for k,v in b.t.items():out[k]=out.get(k,Q(0))+v
  return P(out)
 __radd__=__add__
 def __neg__(self):return P({k:-v for k,v in self.t.items()})
 def __sub__(self,b):return self+-b
 def __mul__(self,b):
  if not isinstance(b,P):return P({k:v*b for k,v in self.t.items()})
  out=defaultdict(Q)
  for (i,e),v in self.t.items():
   for (j,f),w in b.t.items():
    if i&j:continue
    inv=sum((j&((1<<a)-1)).bit_count() for a in range(4*N) if i>>a&1)
    key=(i|j,tuple(x+y for x,y in zip(e,f)))
    out[key]+=v*w*(-1 if inv%2 else 1)
  return P(out)
 __rmul__=__mul__
 def __truediv__(self,b):return self*Q(1,b)
def ev(i):
 e=list(zeroexp);e[i]=1;return P({(0,tuple(e)):Q(1)})
def od(i):return P({(1<<i,zeroexp):Q(1)})
def mm(a,b):return [[sum((a[i][k]*b[k][j] for k in range(len(b))),P()) for j in range(len(b[0]))]for i in range(len(a))]
def diag(a):return [[a[i] if i==j else P() for j in range(len(a))] for i in range(len(a))]
def st(a):return sum((a[i][i]*(1 if i<N else -1) for i in range(2*N)),P())
def compact(F):
 out=defaultdict(Q)
 for (mask,e),coef in F.t.items():
  weight=Q(1)
  for i in range(N):
   odd=(mask>>(4*i))&15; z,zb,w,wb=e[4*i:4*i+4]
   if z!=zb:weight=0;break
   if odd==0:
    if (w,wb) not in [(0,0),(1,1)]:weight=0;break
   elif odd in (3,12):
    if w or wb:weight=0;break
    weight*=-Q(1,z+1)
   else:weight=0;break
  if weight:out[e[-2:]]+=coef*weight
 return {str(k):str(v) for k,v in sorted(out.items()) if v}
U=[[Q(3,5),Q(4,5)],[-Q(4,5),Q(3,5)]]
Z=[[P() for j in range(4)] for i in range(4)];T=[[P() for j in range(4)] for i in range(4)]
for i in range(N):
 z,zb,w,wb=[ev(4*i+j)for j in range(4)]
 gamma,beta,alpha,delta=[od(4*i+j)for j in range(4)]
 Z[i][i]=z;Z[i][i+N]=alpha;Z[i+N][i]=beta;Z[i+N][i+N]=w
 T[i][i]=zb;T[i][i+N]=gamma;T[i+N][i]=delta;T[i+N][i+N]=-wb
c,d=ev(8),ev(9)
AU=[[P.c(U[i%N][j%N])*(1 if i<N else c) if (i<N)==(j<N) else P() for j in range(4)]for i in range(4)]
BUadj=[[P.c(U[j%N][i%N])*(1 if i<N else d) if (i<N)==(j<N) else P() for j in range(4)]for i in range(4)]
M=mm(mm(mm(T,AU),Z),BUadj)
# exp(sum_k t^(2k) STr(M^k)/k): n f_n = sum_{k=1}^n Str(M^k) f_(n-k).
Mk=M; trace={}; F=[P.c(1)]; exact=[]
start=time.time()
for n in range(1,ORDER+1):
 if n>1:Mk=mm(Mk,M)
 trace[n]=st(Mk)
 F.append(sum((trace[k]*F[n-k] for k in range(1,n+1)),P())/n)
 exact.append(compact(F[n]))
 print('order',n,'terms',len(F[n].t),'compact',exact[-1],'seconds',time.time()-start,flush=True)
# Independent ordinary polynomial ratio and U(1)^2 Fourier projection, SymPy.
import sympy as s
x,y,cc,dd=s.symbols('x y c d')
p=s.Rational(3,5)*(x+y);h=x*y
hseries=[s.Integer(1),p]
for n in range(2,ORDER+1):hseries.append(s.expand(p*hseries[-1]-h*hseries[-2]))
r=[]
for n in range(ORDER+1):
 r.append(s.expand(hseries[n]-(cc*p*hseries[n-1] if n else 0)+(cc**2*h*hseries[n-2] if n>=2 else 0)))
checks=[]
for n in range(1,ORDER+1):
 rn=s.Poly(r[n],x,y); orig=s.expand(sum(v*v.subs(cc,dd) for _,v in rn.terms()))
 op=s.Poly(orig,cc,dd)
 expected={str(k):str(Q(int(v.p),int(v.q)))for k,v in sorted(op.terms()) if v}
 assert exact[n-1]==expected,(n,exact[n-1],expected)
 checks.append({'order_t':2*n,'coefficients':expected,'passed':True})
print(json.dumps({'unitary':[[str(v)for v in row]for row in U],'order':ORDER,'checks':checks,'finite_check_only':True,'seconds':time.time()-start},indent=2))
