"""Independent bounded controls for the P/L proof audit; not an analytic proof."""
from pathlib import Path
import hashlib, json, itertools, math
import sympy as s
import mpmath as mp
from sympy.matrices.normalforms import hermite_normal_form,smith_normal_form
from sympy.polys.domains import ZZ
root=Path('/workspace/shared/bgs_paired_box_cancellation')
repo=Path('/workspace/shared/BGS')
S=s.Matrix([[3,4],[2,3]])
x,y,r,z,w,l=s.symbols('x y r z w l')
S0=lambda x,y,r:-(3*x*x-2*x*(y+r)+3*(y+r)**2)/8
assert s.expand(S0(x+z,y+w,r)-S0(x,y,r+w-3*z)-(-2*z*y-2*r*z-2*w*z+3*z*z))==0
assert s.expand(S0(x,y,r+4*l)-S0(x,y,r)-(l*x-3*l*y-3*l*r-6*l*l))==0
mod1=lambda a: a-s.floor(a)
omega=lambda a,b:a[0]*b[1]-a[1]*b[0]
def Q(pt,m):
 n=(S**m-s.eye(2))*s.Matrix(pt)
 return mod1((omega(pt,n)-n[0]*n[1])/2)
def BM(m):
 B=6*s.eye(m)
 for i in range(m):
  B[i,(i+1)%m]-=1; B[i,(i-1)%m]-=1
 return B
rows=[]
for m in [1,2]:
 B=BM(m); D=int(B.det()); Bi=B.inv();L=S**m-s.eye(2)
 H=hermite_normal_form(B); counts={}; checked=0
 for rt in itertools.product(range(4),repeat=m):
  rv=s.Matrix(rt);tv=s.Matrix([rt[j]-3*rt[(j-1)%m] for j in range(m)])
  for nt in itertools.product(*[range(int(H[j,j])) for j in range(m)]):
   nv=s.Matrix(nt);vc=tv+4*nv;xc=Bi*vc
   pt=(mod1(xc[0]),mod1((xc[1%m]+rt[0]-3*xc[0])/4))
   assert all(v.q==1 for v in L*s.Matrix(pt))
   F=(vc.T*Bi*vc)[0]/8-3*sum(v*v for v in rt)/s.Integer(8)
   assert mod1(F-Q(pt,m))==0
   counts[pt]=counts.get(pt,0)+1
   checked+=1
 assert len(counts)==D and set(counts.values())=={4**m}
 pair_count=0; annihilator=[]
 for d in counts:
  nd=L*s.Matrix(d);allzero=True
  for pt in counts:
   ps=tuple(mod1(pt[i]+d[i]) for i in [0,1]);bv=mod1(omega(pt,nd))
   assert mod1(Q(ps,m)-Q(pt,m)-Q(d,m)-bv)==0
   allzero=allzero and bv==0;pair_count+=1
  if allzero:annihilator.append(d)
 assert annihilator==[(0,0)]
 dc=L.inv()*s.Matrix([0,1]); gc=4*Bi[:,0]
 assert dc[0]==gc[0] and dc[1]==(gc[1%m]-3*gc[0])/4==-s.Rational(1,2)
 rows.append(dict(m=m,D=D,listed_classes=checked,multiplicity=4**m,
  polarization_pairs=pair_count,smith_B=[str(v) for v in smith_normal_form(B,domain=ZZ).diagonal()],
  smith_fixed=[str(v) for v in smith_normal_form(L,domain=ZZ).diagonal()],
  winding_lift=[str(v) for v in dc],cycle_green_column=[str(v) for v in gc]))
# Separate physical-matrix phase and normalization checks, using 80-digit
# evaluation only as a finite diagnostic (no exact or asymptotic claim).
mp.mp.dps=80
def emp(v):return mp.exp(2j*mp.pi*mp.mpf(str(v)))
cat=[]
for m in range(1,5):
 A=S**m;a,b=int(A[0,0]),int(A[1,0]);U=math.gcd(a-1,b)
 grid=[(s.Rational(j,U),s.Rational(k,U if m%2 else 2*U)) for j in range(U) for k in range(U if m%2 else 2*U)]
 for N in [1,3,5,7]:
  inv8=pow(8,-1,N) if N>1 else 0
  M=mp.matrix(N,N)
  for j in range(N):
   for k in range(N):M[j,k]=emp(s.Rational((-inv8*(3*j*j-2*j*k+3*k*k))%N,N))/mp.sqrt(N)
  Mn=M**m;tr=sum(Mn[j,j] for j in range(N))
  gauss=sum(emp(N*Q(pt,m)) for pt in grid)
  target=emp(s.Rational(3*m*N,8))*mp.exp(-1j*mp.pi*m/4)*gauss/mp.sqrt(len(grid))
  err=abs(tr-target);assert err<mp.mpf('1e-70')
  cat.append(dict(m=m,N=N,absolute_error=mp.nstr(err,8)))
# Exact resolvent controls at a deliberately enlarged eta, both Hessian signs.
eta=s.Rational(1,10000);norms=[]
for m in range(1,13):
 B=BM(m);K=B/4;G0=K.inv()
 dist=lambda i,j:min(abs(i-j),m-abs(i-j))
 wn=lambda A:max(sum(2**dist(i,j)*abs(A[i,j]) for j in range(m)) for i in range(m))
 assert wn(G0)<=2
 E=s.zeros(m)
 for i in range(m):
  # Per-edge Rxx=Rxy=Ryy=eta, accumulated cyclically, including m=1,2.
  j=(i+1)%m
  E[i,i]+=eta;E[j,j]+=eta;E[i,j]+=eta;E[j,i]+=eta
 assert wn(E)<=6*eta
 for sign in [-1,1]:
  G=(K-sign*E).inv()
  assert wn(G)<=3 and wn(G-G0)<=36*eta and wn(G*E)<=18*eta
 norms.append(dict(m=m,K_inverse_weighted_norm=str(wn(G0)),E_weighted_norm_over_eta=str(wn(E)/eta)))
manifest=json.loads((root/'source_manifest.json').read_text())
sources=[]
for src in manifest['sources']:
 got=hashlib.sha256((repo/src['path']).read_bytes()).hexdigest()
 sources.append(dict(path=str(repo/src['path']),sha256=got,manifest_sha256=src['sha256'],matches_manifest=(got==src['sha256'])))
for name in ['paired_character_identity.md','winding_defect_locality.md','source_manifest.json']:
 sources.append(dict(path=str(root/name),sha256=hashlib.sha256((root/name).read_bytes()).hexdigest()))
result=dict(scope='Bounded exact algebra and 80-digit finite physical-trace diagnostics; no proof of infinite analytic claims by computation',
 symbolic_P1_P2=True,exact_small_cycles=rows,physical_trace_diagnostics=cat,
 weighted_resolvent_diagnostics=norms,source_pins=sources)
(root/'independent_review/check_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['source_pins','physical_trace_diagnostics']},indent=2))
