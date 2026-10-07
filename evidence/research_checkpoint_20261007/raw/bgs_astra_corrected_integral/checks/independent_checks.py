"""Independent finite exact checks of compact projector and Abel controls.
No author checker imported. Exterior algebra uses sorted tuples and exact Q(i).
Inverse Berezinian uses its BB Schur complement, not supertrace exponential.
Compact-kernel computation is modulo an explicitly C-annihilated monomial ideal.
"""
from fractions import Fraction as F
from itertools import permutations, product
from collections import defaultdict
import json,sys,time,platform,hashlib

class G:
    __slots__=('r','i')
    def __init__(self,r=0,i=0):
        if isinstance(r,G):self.r,self.i=r.r,r.i
        else:self.r,self.i=F(r),F(i)
    def __add__(self,b):
        b=G(b);return G(self.r+b.r,self.i+b.i)
    __radd__=__add__
    def __neg__(self):return G(-self.r,-self.i)
    def __sub__(self,b):return self+-G(b)
    def __mul__(self,b):
        b=G(b);return G(self.r*b.r-self.i*b.i,self.r*b.i+self.i*b.r)
    __rmul__=__mul__
    def conj(self):return G(self.r,-self.i)
    def __bool__(self):return bool(self.r or self.i)
    def __eq__(self,b):b=G(b);return self.r==b.r and self.i==b.i
    def __repr__(self):return str(self.r) if not self.i else f'({self.r})+({self.i})i'

N=int(sys.argv[1]) if len(sys.argv)>1 else 3
ORDER=int(sys.argv[2]) if len(sys.argv)>2 else 2
NE=4*N+3; PX=4*N; CX=PX+1; DX=PX+2
ZE=(0,)*NE

def viable(odd,e):
    # All removed monomials belong to a multiplicative ideal annihilated by C.
    if e[PX]>ORDER:return False
    for site in range(N):
        inds={j%4 for j in odd if j//4==site}
        if not (inds<={0,1} or inds<={2,3}):return False
        w,wb=e[4*site+2:4*site+4]
        if w>1 or wb>1 or (inds and (w or wb)):return False
    return True

class P:
    def __init__(self,d=None):self.d={k:G(v) for k,v in (d or {}).items() if v}
    @staticmethod
    def c(x):return P({((),ZE):G(x)}) if x else P()
    def __add__(self,b):
        if not isinstance(b,P):b=P.c(b)
        d=self.d.copy()
        for k,v in b.d.items():d[k]=d.get(k,G())+v
        return P(d)
    __radd__=__add__
    def __neg__(self):return P({k:-v for k,v in self.d.items()})
    def __sub__(self,b):return self+-b
    def __mul__(self,b):
        if not isinstance(b,P):return P({k:v*b for k,v in self.d.items()})
        d={}
        for (o,e),v in self.d.items():
            for (p,f),w in b.d.items():
                if set(o)&set(p):continue
                odd=tuple(sorted(o+p));ee=tuple(a+b for a,b in zip(e,f))
                if not viable(odd,ee):continue
                sign=(-1)**sum(i>j for i in o for j in p)
                key=(odd,ee);d[key]=d.get(key,G())+sign*v*w
        return P(d)
    __rmul__=__mul__
    def __bool__(self):return bool(self.d)

def even(k):
    e=list(ZE);e[k]=1;return P({((),tuple(e)):1})
def odd(k):return P({((k,),ZE):1})
def eye(n):return [[P.c(int(i==j)) for j in range(n)] for i in range(n)]
def mm(a,b):return [[sum((a[i][k]*b[k][j] for k in range(len(b))),P()) for j in range(len(b[0]))] for i in range(len(a))]
def add(a,b):return [[x+y for x,y in zip(ar,br)]for ar,br in zip(a,b)]
def neg(a):return [[-x for x in row]for row in a]
def scale(a,x):return [[x*y for y in row]for row in a]
def parity(p):return (-1)**sum(p[i]>p[j]for i in range(len(p))for j in range(i+1,len(p)))
def det(a):
    ans=P()
    for perm in permutations(range(len(a))):
        term=P.c(parity(perm))
        for i,j in enumerate(perm):term=term*a[i][j]
        ans=ans+term
    return ans

def compact(poly):
    out={}
    for (o,e),v in poly.d.items():
        weight=F(1)
        for i in range(N):
            z,zb,w,wb=e[4*i:4*i+4]
            local=tuple(j%4 for j in o if j//4==i)
            if z!=zb:weight=0;break
            if local==():
                if (w,wb) not in ((0,0),(1,1)):weight=0;break
            elif local in ((0,1),(2,3)):
                if w or wb:weight=0;break
                weight*=-F(1,z+1)
            else:weight=0;break
        if weight:
            key=e[PX:];out[key]=out.get(key,G())+weight*v
    return {k:v for k,v in out.items() if v}

def identg(n):return [[G(i==j)for j in range(n)]for i in range(n)]
def gmm(a,b):return [[sum((a[i][k]*b[k][j]for k in range(len(b))),G())for j in range(len(b[0]))]for i in range(len(a))]
def rot(n,i,j,c,s):
    a=identg(n);a[i][i]=a[j][j]=G(c);a[i][j]=G(s);a[j][i]=G(-s);return a

def makeU(n):
    if n==1:return [[G(0,1)]]
    U=rot(n,0,1,F(3,5),F(4,5))
    P=identg(n);P[1][1]=G(0,1);U=gmm(U,P)
    if n>=3:
        U=gmm(U,rot(n,1,2,F(5,13),F(12,13)))
        U=gmm(U,rot(n,0,2,F(8,17),F(15,17)))
    if n>=4:U=gmm(U,rot(n,2,3,F(7,25),F(24,25)))
    return U

# Recompute a finite local pairing table, including the empty and D_0 states.
# B,C are unnormalized here, so their norms must be 1/k exactly.
z,zb,w,wb=[even(j)for j in range(4)]
ga,be,al,de=[odd(j)for j in range(4)]
def ppow(p,n):
    a=P.c(1)
    for _ in range(n):a=a*p
    return a
states=[]
for k in range(7):states.append(('A',k,ppow(z,k),ppow(zb,k),G(1)))
for k in range(1,7):
    states.append(('B',k,ppow(z,k-1)*al,-de*ppow(zb,k-1),G(F(1,k))))
    states.append(('C',k,ppow(z,k-1)*be,ga*ppow(zb,k-1),G(F(1,k))))
for l in range(7):
    ket=ppow(z,l)*w;bra=ppow(zb,l)*wb
    if l:ket=ket-l*ppow(z,l-1)*al*be;bra=bra+l*ppow(zb,l-1)*ga*de
    states.append(('D',l,ket,bra,G(1)))
localchecks=0
for i,(_,_,ket,_,norm) in enumerate(states):
    for j,(_,_,_,bra,_) in enumerate(states):
        got=compact(ket*bra);want={(0,0,0):norm} if i==j else {}
        assert got==want,(i,j,got,want)
        localchecks+=1

start=time.monotonic();U=makeU(N);Us=[[U[j][i].conj()for j in range(N)]for i in range(N)]
assert gmm(U,Us)==identg(N)
Z=[[P()for _ in range(2*N)]for _ in range(2*N)]
T=[[P()for _ in range(2*N)]for _ in range(2*N)]
for i in range(N):
    z,zb,w,wb=[even(4*i+j)for j in range(4)]
    ga,be,al,de=[odd(4*i+j)for j in range(4)]
    Z[i][i]=z;Z[i][N+i]=al;Z[N+i][i]=be;Z[N+i][N+i]=w
    T[i][i]=zb;T[i][N+i]=ga;T[N+i][i]=de;T[N+i][N+i]=-wb
c,d,p=even(CX),even(DX),even(PX)
AU=[[P.c(U[i%N][j%N])*(1 if i<N else c) if (i<N)==(j<N) else P() for j in range(2*N)]for i in range(2*N)]
BU=[[P.c(Us[i%N][j%N])*(1 if i<N else d) if (i<N)==(j<N) else P() for j in range(2*N)]for i in range(2*N)]
M=mm(mm(mm(T,AU),Z),BU)
BB=[row[:N]for row in M[:N]];BF=[row[N:]for row in M[:N]]
FB=[row[:N]for row in M[N:]];FF=[row[N:]for row in M[N:]]
X=scale(BB,p);a=add(eye(N),neg(X));ainv=eye(N);power=eye(N)
for k in range(1,ORDER+1):power=mm(power,X);ainv=add(ainv,power)
D=add(eye(N),neg(scale(FF,p)))
Schur=add(D,neg(scale(mm(mm(FB,ainv),BF),p*p)))
da=det(a);h=P.c(1)-da;dai=P.c(1);power=P.c(1)
for k in range(1,ORDER+1):power=power*h;dai=dai+power
answer=compact(det(Schur)*dai)
print('compact finished',N,ORDER,'seconds',round(time.monotonic()-start,3),flush=True)

# Ordinary determinant coefficients, using principal minors and formal phase
# exponents. No superalgebra, compact moments, or Wick contraction is reused.
import sympy as s
x=s.symbols('x0:'+str(N));cc,dd=s.symbols('c d')
sm=s.Matrix([[s.Rational(v.r.numerator,v.r.denominator)+s.I*s.Rational(v.i.numerator,v.i.denominator)for v in row]for row in U])
from itertools import combinations
char=[s.Integer(1)]
for k in range(1,N+1):
    char.append(s.expand((-1)**k*sum(sm.extract(J,J).det()*s.prod(x[j]for j in J)for J in combinations(range(N),k))))
hseries=[s.Integer(1)]
for n in range(1,ORDER+1):hseries.append(s.expand(-sum(char[k]*hseries[n-k]for k in range(1,min(n,N)+1))))
ret=[]
for n in range(ORDER+1):ret.append(s.Poly(s.expand(sum(cc**k*char[k]*hseries[n-k]for k in range(min(n,N)+1))),*x))
expected={};checks=[]
for n,r in enumerate(ret):
    val=s.expand(sum(v*s.conjugate(v).subs({s.conjugate(cc):dd})for _,v in r.terms()))
    for (ce,de),coef in s.Poly(val,cc,dd).terms():
        cr,ci=s.expand_complex(coef).as_real_imag()
        gg=G(F(int(cr.p),int(cr.q)),F(int(ci.p),int(ci.q)))
        if gg:expected[n,ce,de]=gg
    got={k:v for k,v in answer.items()if k[0]==n};want={k:v for k,v in expected.items()if k[0]==n}
    assert got==want,(n,got,want)
    checks.append({'degree_t':2*n,'coefficient_count':len(got),'passed':True})
# An independent closed-path dynamic program computes the squared trace moment.
def trace_phase_coeff(m):
    trace={}
    for starti in range(N):
        dp={(starti,(0,)*N):G(1)}
        for step in range(m):
            nxt={}
            for (i,ex),v in dp.items():
                ex2=list(ex);ex2[i]+=1;ex2=tuple(ex2)
                for j in range(N):
                    key=(j,ex2);nxt[key]=nxt.get(key,G())+v*U[i][j]
            dp={k:v for k,v in nxt.items()if v}
        for (end,ex),v in dp.items():
            if end==starti:
                assert ex[starti]>=1 # conditional nonzero Fourier charge
                trace[ex]=trace.get(ex,G())+v
    return {k:v for k,v in trace.items()if v}
tracechecks=[]
for m in range(1,ORDER+1):
    coeffs=trace_phase_coeff(m)
    B=sum((v*v.conj()for v in coeffs.values()),G())
    derivative=sum((ce*de*v for (deg,ce,de),v in answer.items()if deg==m),G())
    assert derivative==B and B.i==0 and B.r>=0,(m,derivative,B)
    tracechecks.append({'m':m,'B_N_m':repr(B),'phase_monomials':len(coeffs),'source_derivative_passed':True})

# Abel controls: exact algebraic inequalities on a specified rational grid.
abel=[]
for n in range(1,9):
    for q in (F(1,10),F(1,3),F(1,2),F(4,5),F(99,100)):
        bound=n*(1+q)/(2*(1-q));diagonal=n*q/(1-q);clock=n*n*q**n/(1-q**n)
        assert diagonal<=bound and clock<=bound
        abel.append({'N':n,'q':str(q),'diagonal_slack':str(bound-diagonal),'clock_slack':str(bound-clock)})
result={'status':'passed','N':N,'order_p':ORDER,'degree_t':2*ORDER,'U':[[repr(v)for v in row]for row in U],
 'arithmetic':'exact Gaussian rationals Q(i); SymPy rational complex principal minors',
 'compact_method':'BB Schur inverse Berezinian in C-annihilated quotient',
 'local_pairing_count':localchecks,'trace_source_checks':tracechecks,'compact_checks':checks,'exact_coefficients':{str(k):repr(v)for k,v in sorted(answer.items())},
 'abel_controls':abel,'python':platform.python_version(),'sympy':s.__version__,'elapsed_seconds':time.monotonic()-start,
 'nonclaims':['No finite check proves arbitrary N identity or bound.','No universality conclusion.']}
print(json.dumps(result,indent=2),flush=True)
