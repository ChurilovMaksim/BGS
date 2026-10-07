#!/usr/bin/env python3
"""Exact bounded N=3 checks; no asymptotic or actual-map numerical claim."""
import hashlib, itertools, json, platform, sys, time
from pathlib import Path
import sympy as s
start=time.time(); root=Path(__file__).resolve().parent
N=3; pairs=list(itertools.product(range(N),repeat=2)); I=s.eye(N); IH=s.eye(N*N)
v=s.Matrix([1,2,2])/3; U=I-2*v*v.T
omega=(-1+s.I*s.sqrt(3))/2
Zs=[s.diag(*[s.expand(omega**(b*j)) for j in range(N)]) for b in range(N)]
def simp(M): return M.applyfunc(s.expand)
def ad(W): return s.Matrix(N*N,N*N,lambda a,b:W[pairs[a][0],pairs[b][0]]*s.conjugate(W[pairs[a][1],pairs[b][1]]))
def pin(A): return s.Matrix(N*N,N*N,lambda a,b:A[a,b] if (pairs[a][1]-pairs[a][0]-pairs[b][1]+pairs[b][0])%N==0 else 0)
def zero(x):
 if isinstance(x,s.MatrixBase): assert simp(x)==s.zeros(x.rows,x.cols),str(x)
 else: assert s.expand(x)==0,str(x)
def hs(x,y): return (x.conjugate().T*y)[0]
def vec(X): return s.Matrix([X[j,k] for j,k in pairs])
def norm2(x): return s.expand(hs(x,x))
def sqabs(z): return s.expand(z*s.conjugate(z))
Ps=[s.diag(*[int((k-j)%N==c) for j,k in pairs]) for c in range(N)]
Rs=[simp(ad(Z)) for Z in Zs]
checks=[]; data={}
zero(U*U-I); T=ad(U); D=pin(T)
for label,zt in [('untwisted',(1,1,1)),('negative_twist',(1,-1,1)),('complex_twist',(1,s.I,-1))]:
 V=ad(s.diag(*zt)); W=s.diag(*zt)*U; A=ad(W); B=pin(A); S=A-B
 zero(A-V*T);zero(B-V*D);zero(A.conjugate().T*A-IH)
 Ab=[simp(R*A*R.conjugate().T) for R in Rs]
 zero(B-sum(Ab,s.zeros(9))/N)
 zero(S-sum([P*(P*A-A*P)-(P*A-A*P)*P for P in Ps],s.zeros(9))/2)
 Apows=[A**k for k in range(7)]
 Cpower=[[simp(R*Apows[k]*R.conjugate().T) for k in range(7)] for R in Rs]
 vals=[]
 for m in range(1,7):
  marked=s.expand(m*s.trace(A**(m-1)*S))
  trace_formula=m*(sqabs(s.trace(W**m))-sum(sqabs(s.trace(W**(m-1)*Z*W*Z.conjugate().T)) for Z in Zs)/N)
  zero(marked-trace_formula)
  ward=-s.Rational(m,2)*sum(s.trace((P*A**(m-1)-A**(m-1)*P)*(P*A-A*P)) for P in Ps)
  zero(marked-ward)
  finite_ward=sum(sum(s.trace(simp((Cp[k]-Apows[k])*(C-A))*Apows[m-1-k]) for k in range(m)) for C,Cp in zip(Ab,Cpower))/N
  zero(marked-finite_ward)
  vals.append(str(marked))
 X=W-s.trace(W)*I/N; x=vec(X); zero(A*x-x)
 commuting_dir=s.expand(s.re(hs(x,S*x))); rhs=sum(norm2(x-C*x) for C in Ab)/(2*N)
 zero(commuting_dir-rhs); assert commuting_dir>=0
 K=A.conjugate().T*S
 for x_test in [IH[:,j] for j in range(9)]+[vec(X),s.Matrix(range(9))]:
  lhs=s.expand(s.re(hs(x_test,K*x_test)));rhs=sum(norm2(A*x_test-C*x_test) for C in Ab)/(2*N)
  zero(lhs-rhs); assert lhs>=0
 data[label]={'endpoint_sources_m1_to_m6':vals,'commutant_dirichlet_form':str(commuting_dir)}
 print('Fixture passed:',label,flush=True)
 checks.append(f'{label}: unitary, twisted pinching/twirl, double commutator, trace formula, both Ward identities m=1..6, commutant and rotated Dirichlet forms')
# Exact characteristic polynomials in the charge basis.
lam=s.Symbol('lambda'); charpolys=[]
for c in range(N):
 block=s.Matrix(N,N,lambda j,k:U[j,k]*U[(j+c)%N,(k+c)%N])
 cp=s.factor(block.charpoly(lam).as_expr());charpolys.append(str(cp))
 if c==0: zero(cp-(lam-1)*(9*lam+7)*(27*lam-11)/243)
 else: zero(cp-(9*lam+1)*(81*lam**2-24*lam-25)/729)
# |4 +/- sqrt(241)|/27 < 7/9 because sqrt(241)<17.
assert 241<17**2; data['charge_block_characteristic_polynomials']=charpolys;data['centered_D_norm']='7/9'
x=vec(U-I/3); sx=(T-D)*x
zero(hs(x,sx)-s.Rational(256,243)); zero(2*s.trace(T*(T-D))-s.Rational(2816,243))
data['commutant_source_matrix']=str(s.Matrix(N,N,list(sx)))
# Direct once-counted cyclic path enumeration, occupation mask kept literal.
allpol=[s.Rational(0)]*3;offpol=[s.Rational(0)]*3
for xword in itertools.product(range(N),repeat=2):
 for yword in itertools.product(range(N),repeat=2):
  c=[(yword[j]-xword[j])%N for j in range(2)];sw=sum(c[j]!=c[(j+1)%2] for j in range(2))
  wt=s.prod(U[xword[j],xword[(j+1)%2]]*s.conjugate(U[yword[j],yword[(j+1)%2]]) for j in range(2))
  allpol[sw]+=wt
  if sorted(xword)!=sorted(yword):offpol[sw]+=wt
zero(allpol[0]-s.Rational(779,243));zero(allpol[2]-s.Rational(1408,243));zero(offpol[0]-s.Rational(1046,729));zero(offpol[2]-s.Rational(3200,729))
# Direct polynomial trace and gauge conjugation checks at finite z values.
Y=s.diag(1,s.I,-1); RY=ad(Y); Tg=ad(Y*U*Y.conjugate().T);Dg=pin(Tg)
zero(Tg-RY*T*RY.conjugate().T);zero(Dg-RY*D*RY.conjugate().T)
for z in [0,s.Rational(2,3),1]:
 M=z*T+(1-z)*D;Mg=z*Tg+(1-z)*Dg
 zero(s.trace(M*M)-allpol[0]-z*z*allpol[2])
 for m in range(1,5):zero(s.trace(M**m)-s.trace(Mg**m))
data['m2_total_switch_polynomial_coefficients']=[str(t) for t in allpol]
data['m2_offcharge_switch_polynomial_coefficients']=[str(t) for t in offpol]
data['m2_offcharge_endpoint_source']=str(2*offpol[2])
checks+=['Exact charge-block characteristic polynomials prove centered norm 7/9','All 81 ordered N=3,m=2 path pairs enumerated exactly; literal occupation and switch masks','Direct trace-polynomial equality and simultaneous-diagonal gauge invariance at z=0,2/3,1; m=1..4']
result={'status':'PASS','arithmetic':'Q(i,sqrt(3)), exact SymPy expressions; no tolerances or randomness','checks':checks,'results':data,'runtime_seconds':time.time()-start,'python':sys.version,'sympy':s.__version__,'non_claims':['No test of the literal BGS fixed-coupling map','No asymptotic endpoint estimate','No extrapolation from N=3; universal statements use the accompanying algebraic proof']}
(root/'exact_results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
