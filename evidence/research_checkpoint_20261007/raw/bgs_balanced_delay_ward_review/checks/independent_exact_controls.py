#!/usr/bin/env python3
"""Finite exact controls only. No asymptotic or integrability claim is tested."""
import sympy as s, json, time, resource, os, sys
from pathlib import Path
resource.setrlimit(resource.RLIMIT_AS,(2*1024**3,2*1024**3))
resource.setrlimit(resource.RLIMIT_CPU,(180,190))
os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
t0=time.monotonic(); counts={}
def check(label, test):
    assert test,label
    counts[label]=counts.get(label,0)+1
# A separate exact representation: Q[t]/Phi_20, no radical simplification.
t=s.symbols('t'); K=s.QQ.alg_field_from_poly(s.Poly(s.cyclotomic_poly(20,t),t),'alpha'); a=K.unit
zero,one=K.zero,K.one
I=a**5; w=a**4; rt=one+2*w+2*w**4
check('cyclotomic_sqrt5',rt*rt==5*one)
def conj(x):
    z=zero
    for c in x.to_list():z=z/a+K.convert(c)
    return z
def mul(A,B):return [[sum((A[i][k]*B[k][j] for k in range(len(B))),zero) for j in range(len(B[0]))] for i in range(len(A))]
def adj(A):return [[conj(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]
def eye(n):return [[one if j==i else zero for j in range(n)] for i in range(n)]
p=[0,4,2,3,1]; V=[[w**(j*p[k])/rt for k in range(5)] for j in range(5)]
v=[[zero],[one/2],[-I/2],[I/2],[-one/2]]
check('cyclotomic_seed_unitary',mul(V,adj(V))==eye(5))
lam=mul(V,v)[1][0]*2
check('cyclotomic_seed_eigenvector',mul(V,v)==[[lam*x[0]] for x in v])
check('cyclotomic_lambda_modulus',lam*conj(lam)==one)
x=lam+one/lam
check('cyclotomic_noninteger_minpoly',5*x**4-20*x*x+16*one==zero)
check('cyclotomic_positive_root_branch_squared',x*x==2*one-2*one/rt)
y=s.symbols('y');check('rational_minpoly_irreducible',s.Poly(5*y**4-20*y*y+16,y).is_irreducible)
# Independently recover all characteristic coefficients from Newton identities.
tr=[K.convert(5)]; power=eye(5)
for k in range(1,6):
    power=mul(power,V);tr.append(sum((power[j][j] for j in range(5)),zero))
es=[one]
for k in range(1,6):es.append(sum(((-1)**(j-1)*es[k-j]*tr[j] for j in range(1,k+1)),zero)/k)
actual=[(-1)**k*es[k] for k in range(6)]
expected=[one]
for ev in [one,one,-one,lam,-one/lam]:
    nxt=[zero]*(len(expected)+1)
    for k,c in enumerate(expected):nxt[k]+=c;nxt[k+1]-=ev*c
    expected=nxt
check('cyclotomic_full_characteristic_polynomial',actual==expected)
check('cyclotomic_reverse_kernel_entry',V[1][2]*conj(V[2][1])==w**4/5)
b=[V[0][1:]]; d=[row[1:] for row in V[1:]]; u=v[1:]
check('cyclotomic_compression_normal',mul(d,adj(d))==mul(adj(d),d))
check('cyclotomic_compression_eigenvector',mul(d,u)==[[lam*z[0]] for z in u])
check('cyclotomic_compression_left_identity',mul(b,d)==[[-z/rt for z in b[0]]])
kappa=I*lam/(lam+one/rt)/rt
c1=kappa/2;c2=-I*kappa/2
re=lambda z:(z+conj(z))/2
im=lambda z:(z-conj(z))/(2*I)
minor=re(c1)*im(c2)-re(c2)*im(c1)
check('cyclotomic_leakage_rank2',minor!=zero and minor==-kappa*conj(kappa)/4)
# Independent rational unitary fixtures through the Cayley transform.
def simp(x):return s.cancel(s.expand_complex(x))
def smat(A):return A.applyfunc(simp)
def cayley(n):
    H=s.diag(*range(1,n+1))
    for k in range(n-1):H[k,k+1]=1+s.I*(k+1);H[k+1,k]=s.conjugate(H[k,k+1])
    return smat((s.eye(n)+s.I*H)*(s.eye(n)-s.I*H).inv())
z=s.symbols('z')
for n in [2,3,4]:
    T=cayley(n)*s.diag(*[1,s.I,-1,-s.I][:n]);T=smat(T)
    check('rational_colligation_unitary',smat(T*T.H)==s.eye(n))
    aa=T[0,0];bb=T[0,1:];cc=T[1:,0];dd=T[1:,1:]
    M=s.eye(n);M[0,0]=aa;M[0,1:]=-z*bb;M[1:,0]=cc;M[1:,1:]=s.eye(n-1)-z*dd
    delta=s.cancel(M.det()-(-1)**(n-1)*T.det()*(z*s.eye(n-1)-dd.H).det())
    check('rational_colligation_polynomial_identity',delta==0)
# Phase generator checked using direct second-order matrix jets, not a trace-generator formula.
def jadd(A,B):return [A[k]+B[k] for k in range(3)]
def jmul(A,B):return [sum((A[l]*B[k-l] for l in range(k+1)),s.S.Zero) for k in range(3)]
def jconj(A):return [s.conjugate(x) for x in A]
def jscale(A,c):return [c*x for x in A]
def jet_trace(V,a,m):
    n=V.rows;E=s.zeros(n);E[a,a]=1;D=[V,s.I*E*V,-E*V/2];P=[s.eye(n),s.zeros(n),s.zeros(n)]
    for _ in range(m):P=[smat(sum((P[l]*D[k-l] for l in range(k+1)),s.zeros(n))) for k in range(3)]
    return [s.trace(A) for A in P]
fixtures=[s.Integer(1),s.I,(3+4*s.I)/5,(-5+12*s.I)/13]
for n in [2,3,4]:
    W=cayley(n);eigs=fixtures[:n];V=smat(W*s.diag(*eigs)*W.H)
    weights=s.Matrix(n,n,lambda j,a:simp(W[a,j]*s.conjugate(W[a,j])))
    G=weights*weights.T;GH=(s.ones(n)+s.eye(n))/(n+1)
    zz=s.symbols('z0:'+str(n)); pt=lambda m:sum(q**m for q in zz)
    tests=[('pair'+str(m),pt(m)*pt(-m),m) for m in [1,2,4]]
    tests += [('quartic',pt(1)**2*pt(-1)**2,None),('mixed',(pt(1)**2*pt(-2)+pt(-1)**2*pt(2))/2,None)]
    for label,F,m in tests:
        grad=[s.I*zz[j]*s.diff(F,zz[j]) for j in range(n)]
        Hess=s.Matrix(n,n,lambda j,k:s.I*zz[k]*s.diff(grad[j],zz[k]))
        sub=dict(zip(zz,eigs));gg=[simp(x.subs(sub)) for x in grad];hh=Hess.subs(sub).applyfunc(simp)
        drift=s.Matrix(n,n,lambda j,k:0 if j==k else simp(s.I*(eigs[j]+eigs[k])/(eigs[j]-eigs[k])*(gg[j]-gg[k])))
        def op(C):return simp(sum(C[j,k]*(hh[j,k]/2+drift[j,k]/4) for j in range(n) for k in range(n)))
        direct=0
        for a in range(n):
            if m is not None:
                p=jet_trace(V,a,m);jj=jmul(p,jconj(p))
            else:
                p=jet_trace(V,a,1)
                if label=='quartic':jj=jmul(jmul(p,p),jconj(jmul(p,p)))
                else:
                    p2=jet_trace(V,a,2);vjet=jmul(jmul(p,p),jconj(p2));jj=jscale(jadd(vjet,jconj(vjet)),s.Rational(1,2))
            direct+=jj[2]
        check('rational_phase_generator_'+label,simp(direct-op(G))==0)
        radial=(sum(hh[j,j] for j in range(n))+sum(drift[j,k] for j in range(n) for k in range(n))/2)/(2*n)
        check('rational_haar_reference_normalization',simp(op(GH)-s.Rational(n,n+1)*radial)==0)
        check('rational_signed_defect_decomposition',simp(op(G)-op(G-GH)-s.Rational(n,n+1)*radial)==0)
# The diagonal ensemble catches a false claim of universal CUE phase stationarity.
q=s.symbols('q')
for n in range(1,9):
    cue=sum(m*q**m for m in range(1,n))+n*q**n/(1-q)
    check('abel_cue_sum',s.factor(cue-q*(1-q**n)/(1-q)**2)==0)
    if n>1:check('diagonal_noncue_control',s.factor(n*q/(1-q)-cue)!=0)
result={'status':'passed','counts':counts,'runtime_seconds':time.monotonic()-t0,'python':sys.version.split()[0],'sympy':s.__version__,'arithmetic':'Exact Q[t]/Phi_20 and Q(i)(z); deterministic rational Cayley fixtures','bounds':{'seed_dimension':5,'colligation_dimensions':[2,3,4],'generator_dimensions':[2,3,4],'pair_powers':[1,2,4],'extra_tests':['|Tr V|^4','Re((Tr V)^2 conjugate(Tr V^2))'],'abel_sum_dimensions':list(range(1,9))},'non_claims':['No tensor-uniform conclusion from finite computations','No numerical integration of the divergent delay moment','No actual-model overlap estimate','No compact-heat regularity theorem certified by code','No boundary or large-N limit taken']}
Path(__file__).resolve().parents[1].joinpath('results/independent_exact_controls.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
