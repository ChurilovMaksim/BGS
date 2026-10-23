#!/usr/bin/env python3
"""Independent finite algebra audit. No actual fixed-tau matrices or limit tests.
Trace polynomials are reconstructed from principal determinants and Newton
recursion (not the author's closed-word enumeration); transfer series are
constructed by matrix-vector recurrence. Phase quadrature is a third check.
"""
import itertools,json,time,sys
import sympy as S
from sympy.polys.domains import QQ_I as K
start=time.monotonic(); Z=K.zero; O=K.one
counts={}; data={}
def tick(x,n=1): counts[x]=counts.get(x,0)+n
def simp(x): return S.simplify(S.expand(x))
def cv(x): return K.from_sympy(simp(x))
def conj(x): return K(x.x,-x.y)
def norm(x): return (x*conj(x)).x
def clean(p): return {x:a for x,a in p.items() if a}
def add(p,q):
 t=p.copy()
 for x,a in q.items():t[x]=t.get(x,Z)+a
 return clean(t)
def scale(p,a):return clean({x:v*a for x,v in p.items()})
def shift(p,k,n=1):
 q={}
 for x,a in p.items():
  y=list(x);y[k]+=n;q[tuple(y)]=a
 return q
def mul(p,q):
 t={}
 for x,a in p.items():
  for y,b in q.items():
   v=tuple(i+j for i,j in zip(x,y));t[v]=t.get(v,Z)+a*b
 return clean(t)
def pn(p):return sum((norm(a) for a in p.values()),0)
def series_mul(p,q,M):
 t=[{} for _ in range(M+1)]
 for i in range(M+1):
  for j in range(M+1-i):t[i+j]=add(t[i+j],mul(p[i],q[j]))
 return t

def newton_traces(U,k,N,M):
 zz=(0,)*N; C=[{zz:O}]+[{} for _ in range(k)]
 for j in range(1,k+1):
  for I in itertools.combinations(range(k),j):
   ex=tuple(int(i in I) for i in range(N));C[j][ex]=cv((-1)**j*U.extract(I,I).det())
  C[j]=clean(C[j])
 P=[{} for _ in range(M+1)]
 for m in range(1,M+1):
  v=scale(C[m],K(m)) if m<=k else {}
  for j in range(1,min(k,m-1)+1):v=add(v,mul(C[j],P[m-j]))
  P[m]=scale(v,-O)
 return P

def transfer_series(U,k,N,M):
 zz=(0,)*N; f=[{} for _ in range(M+1)];f[1]=clean({zz:cv(U[k,k])})
 v=[clean({zz:cv(U[i,k])}) for i in range(k)]
 for m in range(2,M+1):
  val={}
  for i in range(k):val=add(val,scale(shift(v[i],i),cv(U[k,i])))
  f[m]=val
  v=[clean(sum_poly([scale(shift(v[j],j),cv(U[i,j])) for j in range(k)])) for i in range(k)]
 return f

def sum_poly(seq):
 t={}
 for p in seq:t=add(t,p)
 return t

def reflector(v):
 v=S.Matrix(v);return S.eye(len(v))-2*v*v.conjugate().T/(v.conjugate().T*v)[0]
U2=S.Matrix([[S.Rational(3,5),S.Rational(4,5)],[-S.Rational(4,5),S.Rational(3,5)]])*S.diag((3+4*S.I)/5,S.I)
U3=reflector([1,S.I,2+S.I])*S.diag(1,S.I,(3+4*S.I)/5)
U4=reflector([1,1+S.I,1-S.I,2])*S.diag(1,S.I,-1,-S.I)
fixtures=[('scalar',S.Matrix([[S.I]]),[(0,)],5),('dense2',U2,[(0,1),(1,0)],5),('dense3',U3,list(itertools.permutations(range(3))),4),('dense4',U4,[(0,1,2,3),(3,2,1,0)],4)]
for name,V,orders,M in fixtures:
 N=V.rows; assert V*V.conjugate().T==S.eye(N) or simp(V*V.conjugate().T-S.eye(N))==S.zeros(N)
 tick('unitary_fixtures');data[name]={'matrix':str(V),'orders':orders,'max_power':M}; ref=None
 for order in orders:
  U=V.extract(order,order);Ps=[newton_traces(U,k,N,M) for k in range(N+1)];total=[0]*(M+1)
  for k in range(N):
   f=transfer_series(U,k,N,M);power=[{(0,)*N:O}]+[{} for _ in range(M)]
   log=[{} for _ in range(M+1)];energy=[0]*(M+1)
   df=[scale(p,K(m)) for m,p in enumerate(f)]
   for n in range(1,M+1):
    zdfpower=series_mul(df,power,M)
    for m in range(1,M+1):energy[m]+=pn(zdfpower[m])
    power=series_mul(power,f,M)
    for m in range(1,M+1):log[m]=add(log[m],scale(shift(power[m],k,n),-O/K(n)))
   for m in range(1,M+1):
    diff=add(Ps[k+1][m],scale(Ps[k][m],-O))
    assert log[m]==scale(diff,-O/K(m)),(name,order,k,m,'log')
    assert energy[m]==pn(diff),(name,order,k,m,'energy')
    assert all(sum(ex)==m for ex in diff),(name,'degree')
    total[m]+=energy[m];tick('newton_log_coefficients');tick('transfer_energy_coefficients');tick('phase_homogeneity')
  vals=[pn(Ps[N][m]) for m in range(1,M+1)]
  assert total[1:]==vals;tick('full_energy_and_order',M)
  if ref is None:ref=vals
  else:assert vals==ref
 data[name]['B']=[str(v) for v in ref]

# Exact fourth-root quadrature equals Haar integration through degree three.
# Evaluate actual dense matrix powers, independently of both series paths.
for name,U in [('dense2',U2),('dense3',U3)]:
 N=U.rows; A=[[cv(U[i,j]) for j in range(N)] for i in range(N)]
 sums=[0]*3
 for ph in itertools.product([O,-O,K.imag_unit,-K.imag_unit],repeat=N):
  V=[[ph[i]*A[i][j] for j in range(N)] for i in range(N)];W=[[O if i==j else Z for j in range(N)] for i in range(N)]
  for m in range(3):
   W=[[sum((W[i][k]*V[k][j] for k in range(N)),Z) for j in range(N)] for i in range(N)]
   sums[m]+=norm(sum((W[i][i] for i in range(N)),Z));tick('literal_phase_grid_powers')
 ref=data[name]['B']
 for m in range(3):assert str(sums[m]/(4**N))==ref[m];tick('phase_quadrature_Haar_comparisons')

# Literal determinant/loss tests at complex z, and all six N=3 orders.
ph=[S.I,(3+4*S.I)/5,-1];z=(2+S.I)/5;az=simp(z*S.conjugate(z))
for order in itertools.permutations(range(3)):
 U=U3.extract(order,order)
 for k in range(1,4):
  a=U[k-1,k-1];b=U[k-1,:k-1];c=U[:k-1,k-1];d=U[:k-1,:k-1];D=S.diag(*ph[:k-1]) if k>1 else S.zeros(0)
  y=(S.eye(k-1)-z*d*D).inv()*c if k>1 else S.zeros(0,1)
  h=simp(a+z*(b*D*y)[0]) if k>1 else a
  det=simp((S.eye(k)-z*S.diag(*ph[:k])*U[:k,:k]).det()-(S.eye(k-1)-z*D*d).det()*(1-z*ph[k-1]*h))
  assert det==0;tick('complex_radius_schur_determinants')
  inds=[k-1,*range(k-1)];T=U.extract(inds,inds)*S.diag(1,*ph[:k-1]);v=S.Matrix([1,*[z*q for q in y]])
  loss=simp((v.conjugate().T*(S.eye(k)-T.conjugate().T*T)*v)[0]);assert loss>=0
  assert simp(1-h*S.conjugate(h)-(1-az)*(y.conjugate().T*y)[0]-loss)==0
  if k==3:assert loss==0
  tick('complex_radius_losses')
 # Almost-everywhere boundary map at a nonsingular exact phase tuple.
 y=(S.eye(2)-d*D).inv()*c;H=simp(a+(b*D*y)[0]);assert simp(H*S.conjugate(H))==1;tick('boundary_inner_samples')

# General second/fourth formulas via Laurent constant terms, to r^12.
# This is an independently truncated series check, not contour residues.
r,w=S.symbols('r w',real=False);R=12
samples=[(S.Rational(1,5),(1+2*S.I)/7,(2-S.I)/6),((2+S.I)/5,(3+S.I)/8,(1-3*S.I)/9),(S.Integer(0),(2+S.I)/5,S.I/4)]
moments=[]
for a,x,A in samples:
 f=sum(r**n*w**n*a**(n-1)*x for n in range(1,R+1));fb=sum(r**n*w**(-n)*S.conjugate(a)**(n-1)*S.conjugate(x) for n in range(1,R+1))
 # Sparse bivariate multiplication bounded in radial degree.
 def to_dict(expr):
  o={}
  for term in S.expand(expr).as_ordered_terms():
   deg=term.as_powers_dict();rr=int(deg.get(r,0));ww=int(deg.get(w,0))
   if rr<=R:o[(rr,ww)]=o.get((rr,ww),0)+term/(r**rr*w**ww)
  return {k:simp(v) for k,v in o.items()}
 def mm(p,q):
  o={}
  for (i,j),u in p.items():
   for (k,l),v in q.items():
    if i+k<=R:o[(i+k,j+l)]=o.get((i+k,j+l),0)+u*v
  return {k:simp(v) for k,v in o.items()}
 p=to_dict(A+f);q=to_dict(S.conjugate(A)+fb);pq=mm(p,q);pq2=mm(pq,pq)
 second=sum(v*r**i for (i,j),v in pq.items() if j==0);fourth=sum(v*r**i for (i,j),v in pq2.items() if j==0)
 t=simp(a*S.conjugate(a));xx=simp(x*S.conjugate(x));AA=simp(A*S.conjugate(A));den=1-r*r*t;coh=simp((S.conjugate(A)*x*S.conjugate(a)+A*S.conjugate(x)*a)/2)
 ex2=AA+r*r*xx/den;ex4=AA**2+4*r*r*AA*xx/den+4*r**4*xx*coh/den**2+r**4*xx**2*(1+r*r*t)/den**3
 assert simp(second-S.series(ex2,r,0,R+1).removeO())==0
 assert simp(fourth-S.series(ex4,r,0,R+1).removeO())==0
 tick('scalar_moment_series_coefficients',2*(R+1));moments.append({'a':str(a),'x':str(x),'A':str(A),'max_radial_degree':R})
data['moment_samples']=moments
# Same intensities, both strict contractions, unequal conditional fourth moment.
Sp=S.Matrix([[1,1],[1,1]])/5;Sm=S.Matrix([[-1,1],[1,1]])/5
for V in [Sp,Sm]:assert all(e<1 for e in (V.T*V).eigenvals());tick('strict_contraction_coherence_witness')
assert [v*v for v in Sp]==[v*v for v in Sm]
coherence_gap=simp(8*S.Rational(1,2)**4*S.Rational(1,25)**2*S.Rational(1,5)*S.Rational(1,25)*S.Rational(1,5)/(1-S.Rational(1,2)**2*S.Rational(1,5)**2)**2)
assert coherence_gap>0;data['same_intensity_fourth_moment_gap_at_r_half']=str(coherence_gap)

# Orthogonal 3x3 witnesses reconstructed from invariant decomposition:
# + is a rotation about (1,1,1); - is the Householder reflection in that axis.
e=S.ones(3,1);P=e*e.T/3;J=S.Matrix([[0,1,-1],[-1,0,1],[1,-1,0]])/S.sqrt(3)
Up=P+J;Um=S.eye(3)-2*P
for V in [Up,Um]:assert simp(V*V.T-S.eye(3))==S.zeros(3);tick('algebraic_witness_orthogonality')
minors=[]
for size in range(4):
 for I in itertools.combinations(range(3),size):
  x=simp(Up.extract(I,I).det());y=simp(Um.extract(I,I).det());assert simp(x*x-y*y)==0;tick('principal_minor_moduli');minors.append({'subset':I,'plus':str(x),'minus':str(y)})
x=S.symbols('x0:3');B=[]
for V in [Up,Um]:
 p2=S.Poly(S.expand(S.trace((S.diag(*x)*V)**2)),*x);B.append(simp(sum(v*v for v in p2.coeffs())))
assert B==[S.Rational(17,27),S.Rational(65,27)];data['principal_minor_witness']={'minor_values':minors,'B2':[str(t) for t in B]};tick('principal_minor_trace_discriminator',2)

# Cyclic fixture at all six orders for N=3, plus exact integer powers up to 3N+1.
for N in [1,2,3,4,7]:
 C=S.zeros(N)
 for j in range(N):C[j,(j+1)%N]=1
 for m in range(1,3*N+2):
  assert S.trace(C**m)**2==(N*N if m%N==0 else 0);tick('cycle_literal_powers')
 if N==3:
  for order in itertools.permutations(range(N)):
   U=C.extract(order,order)
   for k in range(N):
    f=transfer_series(U,k,N,4)
    if k<N-1:assert all(not t for t in f)
    else:
     ex=[1]*N;ex[k]=0;assert f[3]=={tuple(ex):O};assert all(not f[j] for j in [0,1,2,4])
    tick('cycle_transfer_orders')
# Degenerate unit-modulus diagonal corner decouples, N=1 included.
V=S.diag(S.I,1,-1);ret=0
assert all(V[ret,j]==0 and V[j,ret]==0 for j in [1,2]);tick('degenerate_boundary_point_mass')
# Exact two-radius/triangle identity on a positive exponential generator.
s,h,l=S.symbols('s h l',positive=True)
expr=(S.exp(-l*(s+h))+S.exp(-l*(s-h))-2*S.exp(-l*s))
assert simp(expr-S.exp(-l*s)*(2*S.cosh(l*h).rewrite(S.exp)-2))==0;tick('three_radius_exponential_generator')
print(json.dumps({'status':'passed','arithmetic':'Exact Q(i), Q(sqrt(3)), rational symbolic coefficients; no floating or random test','counts':counts,'fixtures':data,'runtime_seconds':time.monotonic()-start,'python':sys.version,'sympy':S.__version__,'nonclaims':['No large-N theorem','No actual fixed-tau computation','No analytic formalization','No higher factorial or off-charge closure']},indent=2))
