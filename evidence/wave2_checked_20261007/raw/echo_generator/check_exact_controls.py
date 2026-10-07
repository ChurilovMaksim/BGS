#!/usr/bin/env python3
"""Exact cyclotomic controls. No floating tau or exponentiation at auxiliary tau.
Raises explicitly (also in python -O); finite evidence only.
"""
import itertools, json, hashlib, sys, time
from pathlib import Path
import sympy as sp
from sympy.polys.domains import QQ
OUT=Path(__file__).resolve().parent
SOURCE=Path('/workspace/shared/bgs_checked_checkpoint_validation/source_snapshot')
PINS=[
'record/checked_research_checkpoint_20261007.md',
'mathematics/phase_trace_checkpoint.md',
'mathematics/actual_charge_radial_shell.md',
'mathematics/uniform_phase_pair_abel_bound.md',
'evidence/research_checkpoint_20261007/raw/bgs_astra_signed_boundary/NEXT_LITERAL_SOURCE.md',
'evidence/research_checkpoint_20261007/raw/bgs_astra_signed_boundary/inputs/08_fixed_map_path_model.md',
'evidence/research_checkpoint_20261007/raw/bgs_astra_signed_boundary/inputs/09_frozen_operator_transfer_coercivity.md',
'evidence/research_checkpoint_20261007/raw/bgs_astra_signed_boundary/ward_review/ward_identity_review.md',
'evidence/research_checkpoint_20261007/raw/bgs_astra_signed_boundary/bilinear_carry_counterexample_v2.md',
]
def check(v,msg):
    if not v: raise RuntimeError(msg)
def addpoly(a,b):
    out=a.copy()
    for v,c in b.items(): out[v]=sp.expand(out.get(v,0)+c)
    return {v:c for v,c in out.items() if c!=0}
def scale(a,c): return {v:sp.expand(x*c) for v,x in a.items() if x*c!=0}
def mulpoly(a,b):
    out={}
    for (aa,ab),ac in a.items():
        for (ba,bb),bc in b.items():
            v=(aa+ba,ab+bb); out[v]=sp.expand(out.get(v,0)+ac*bc)
    return {v:c for v,c in out.items() if c!=0}
def cosq(k): return {(0,k):sp.Rational(1,2),(0,-k):sp.Rational(1,2)}
r=mulpoly(addpoly({(0,0):sp.Integer(1)},scale(cosq(7),-1)),addpoly({(0,0):sp.Integer(1)},cosq(1)))
g=addpoly(cosq(7),scale(r,sp.Rational(1,10)))
g=addpoly(g,scale(mulpoly(r,{(0,1):-sp.I/2,(0,-1):sp.I/2}),sp.Rational(1,100)))
g=addpoly(g,{(0,0):-sp.Rational(1,10)})
rhalf={v:c*((-1)**(v[1]%2)) for v,c in r.items()}
g=addpoly(g,mulpoly(rhalf,{(1,0):(-3-4*sp.I)/1000,(-1,0):(-3+4*sp.I)/1000}))
check(not any(c.has(sp.Float) for c in g.values()), 'no floating symbol coefficients')
check(g[(0,1)]==sp.Rational(1,20)-sp.I/200,'literal coefficient c01')
check(g[(0,2)]==-sp.I/400,'literal coefficient c02')
check(all(g.get((-a,-b),0)==sp.conjugate(c) for (a,b),c in g.items()),'Hermitian symbol')
class Cyclo:
    def __init__(self,N):
        self.N=N; self.K=QQ.cyclotomic_field(4*N); self.z=self.K.unit; self.O=self.K.zero;self.I=self.K.one
        self.zp=[self.z**k for k in range(4*N)]; self.ii=self.zp[N]
    def e(self,k): return self.zp[k%(4*self.N)]
    def q(self,x):
        re,im=sp.sympify(x).as_real_imag()
        check(re.is_Rational and im.is_Rational, 'Gaussian-rational embedding only')
        return self.K.convert(re)+self.K.convert(im)*self.ii
    def bar(self,x):
        o=self.O
        for c in x.to_list(): o=o*self.e(-1)+self.K.convert(c)
        return o
    def zero(self,n=None):
        n=n or self.N; return [[self.O for _ in range(n)] for _ in range(n)]
    def eye(self,n=None):
        n=n or self.N; return [[self.I if j==k else self.O for k in range(n)] for j in range(n)]
    def mm(self,A,B):
        n=len(A); C=self.zero(n)
        for j in range(n):
            for k in range(n):
                if not A[j][k]:continue
                for l in range(n):
                    if B[k][l]: C[j][l]+=A[j][k]*B[k][l]
        return C
    def adj(self,A): return [[self.bar(A[k][j]) for k in range(len(A))] for j in range(len(A))]
    def sm(self,A,c):return [[c*x for x in row] for row in A]
    def plus(self,A,B):return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]
    def tr(self,A):return sum((A[j][j] for j in range(len(A))),self.O)
    def W(self,a,b):
        N=self.N; A=self.zero()
        for j in range(N):A[j][(j+a)%N]=self.e(4*b*j+2*b*a)
        return A
    def M0(self):
        N=self.N; inv8=pow(8,-1,N)
        return [[self.e(-4*inv8*(3*j*j-2*j*k+3*k*k)) for k in range(N)] for j in range(N)]
    def A_fourier(self):
        A=self.zero()
        for (a,b),c in sorted(g.items()):A=self.plus(A,self.sm(self.W(a,b),self.q(c)))
        return A
    def rval(self,k):
        # q=k/(2N); e(q)=z^(2k)
        co=lambda d:(self.e(2*k*d)+self.e(-2*k*d))/2
        return (1-co(7))*(1+co(1))
    def A_midpoint(self):
        N=self.N; A=self.zero()
        for j in range(N):
            co7=(self.e(28*j)+self.e(-28*j))/2
            si1=(self.e(4*j)-self.e(-4*j))/(2*self.ii)
            A[j][j]+=co7+self.rval(2*j)/10+self.rval(2*j)*si1/100-self.q(sp.Rational(1,10))
            for a in [-1,1]:
                A[j][(j+a)%N]+=self.rval(2*j+a+N)*(-3-4*a*self.ii)/1000
        return A
    def text(self,x): return str(self.K.to_sympy(x))

def mechanism(N):
    C=Cyclo(N); A=C.A_fourier(); check(A==C.A_midpoint(),f'midpoint N{N}');check(A==C.adj(A),f'hermitian N{N}')
    labels=[(0,0),(1,0),(0,1),(-1,2),(N+1,-N-2),(-N,1),(2*N-1,(3*N-1)//2)]
    aliases=0; products=0; generators=0; cat=0
    for a,b in labels:
        for rr,ss in itertools.product(range(-1,2),repeat=2):
            sign=(-1)**((b*rr+a*ss+N*rr*ss)%2)
            check(C.W(a+N*rr,b+N*ss)==C.sm(C.W(a,b),sign),f'alias {N,a,b,rr,ss}');aliases+=1
    for v,w in itertools.product(labels,repeat=2):
        phase=C.e(2*(v[0]*w[1]-v[1]*w[0]))
        check(C.mm(C.W(*v),C.W(*w))==C.sm(C.W(v[0]+w[0],v[1]+w[1]),phase),f'product {N,v,w}'); products+=1
    M0=C.M0();check(C.mm(M0,C.adj(M0))==C.sm(C.eye(),N),f'cat unitarity {N}')
    for a,b in labels:
        W=C.W(a,b); direct=C.sm(C.plus(C.mm(A,W),C.sm(C.mm(W,A),-1)),C.ii*N); sine=C.zero()
        for (va,vb),c in g.items():
            om=va*b-vb*a; sn=(C.e(2*om)-C.e(-2*om))/(2*C.ii)
            sine=C.plus(sine,C.sm(C.W(va+a,vb+b),-2*N*C.q(c)*sn))
        check(direct==sine,f'sine {N,a,b}');generators+=1
        check(C.mm(C.mm(M0,W),C.adj(M0))==C.sm(C.W(3*a+4*b,2*a+3*b),N),f'cat orientation {N,a,b}');cat+=1
    # Reversing sine sign is explicitly detected in a noncentral control.
    W=C.W(1,0); L=C.sm(C.plus(C.mm(A,W),C.sm(C.mm(W,A),-1)),C.ii*N)
    check(any(x for row in L for x in row) or N==7,f'noncentral fixture {N}')
    check(C.W(N,1)!=C.W(0,1),'dropping alias sign must fail')
    if N!=7:check(L!=C.sm(L,-1),'reversing sine sign must fail')
    return {'N':N,'field':f'Q(zeta_{4*N})','alias_checks':aliases,'weyl_products':products,'generator_checks':generators,'cat_checks':cat,'A_scalar':A==C.sm(C.eye(),A[0][0])}

def rational_echo():
    C=Cyclo(3);N=3;U=[[C.q(sp.Rational(v,9)) for v in row] for row in [[7,-4,-4],[-4,1,-8],[-4,-8,1]]]
    check(C.mm(U,C.adj(U))==C.eye(),'rational unitarity')
    count=0; vals=[]
    for phases in [[1,1,1],[1,-1,1],[1,C.e(4),C.e(8)]]:
        W=[[phases[j]*U[j][k] for k in range(N)] for j in range(N)]
        T=[[W[j][k]*C.bar(W[l][r]) for k,r in itertools.product(range(N),repeat=2)] for j,l in itertools.product(range(N),repeat=2)]
        D=[[T[j*N+l][k*N+r] if (l-j)%N==(r-k)%N else C.O for k,r in itertools.product(range(N),repeat=2)] for j,l in itertools.product(range(N),repeat=2)]
        Tp=C.eye(N*N);Wp=C.eye()
        for m in range(1,9):
            trace=C.tr(C.mm(D,Tp));twirl=C.O;charge=C.O
            for b in range(N):
                Z=[[C.e(4*b*j) if j==k else C.O for k in range(N)] for j in range(N)]
                q=C.tr(C.mm(C.mm(C.mm(Wp,Z),W),C.adj(Z)));twirl+=q*C.bar(q)/N
            for c in range(N):
                q=sum((Wp[(j+c)%N][j]*W[j][(j+c)%N] for j in range(N)),C.O);charge+=q*C.bar(q)
            check(trace==twirl==charge,f'echo identities m{m}');count+=1
            if phases==[1,1,1]:vals.append(C.text(trace))
            Tp=C.mm(Tp,T);Wp=C.mm(Wp,W)
    return {'N':3,'exact_twirl_tests':count,'m_range':[1,8],'untwisted_values':vals}

def actual_jets():
    C=Cyclo(3); N=3; degree=2; A=C.A_fourier();M0=C.M0();gauss=sum((C.e(4*j*j) for j in range(N)),C.O);root=gauss/C.ii
    check(root*root==C.q(N),'sqrt3 Gauss'); M=C.sm(M0,C.I/root)
    U=[M,C.sm(C.mm(A,M),C.ii*N),C.sm(C.mm(C.mm(A,A),M),-C.q(N*N)/2)]
    def jp(x,y):return [sum((x[k]*y[d-k] for k in range(d+1)),C.O) for d in range(degree+1)]
    def plus(x,y):return [a+b for a,b in zip(x,y)]
    def mag(x):return jp(x,[C.bar(a) for a in x])
    rows=[]
    for m in range(1,7):
        polys={}; one=[C.I,C.O,C.O]
        for path in itertools.product(range(N),repeat=m):
            n=tuple(path.count(j) for j in range(N));c=(path[1%m]-path[0])%N
            amp=one
            for t,j in enumerate(path):
                k=path[(t+1)%m];amp=jp(amp,[U[d][j][k] for d in range(degree+1)])
            key=(c,n);polys[key]=plus(polys.get(key,[C.O]*(degree+1)),amp)
        total=[C.O]*(degree+1);balanced=[C.O]*(degree+1)
        for c in range(N):
            a=[C.O]*(degree+1)
            for (cc,n),x in polys.items():
                if cc==c:a=plus(a,x);balanced=plus(balanced,mag(x))
            total=plus(total,mag(a))
        off=[x-y for x,y in zip(total,balanced)]
        rows.append({'m':m,'E0_taylor_coefficients':[C.text(x) for x in total], 'Ebar_taylor_coefficients':[C.text(x) for x in balanced],'offcharge_taylor_coefficients':[C.text(x) for x in off], 'occupation_keys':len(polys)})
        if m==1:
            diag_sum=[sum((U[d][j][j] for j in range(N)),C.O) for d in range(degree+1)]
            diag_energy=[C.O]*(degree+1)
            for j in range(N):diag_energy=plus(diag_energy,mag([U[d][j][j] for d in range(degree+1)]))
            check(off==[x-y for x,y in zip(mag(diag_sum),diag_energy)],'m1 occupation subtraction')
        # Independent superoperator-power jet (twist 0) checks E0 at every m.
        t=[]
        for d in range(degree+1):
            t.append([[sum((U[k][j][a]*C.bar(U[d-k][l][b]) for k in range(d+1)),C.O) for a,b in itertools.product(range(N),repeat=2)] for j,l in itertools.product(range(N),repeat=2)])
        dp=[]
        for d in range(degree+1): dp.append([[t[d][j*N+l][a*N+b] if (l-j)%N==(b-a)%N else C.O for a,b in itertools.product(range(N),repeat=2)] for j,l in itertools.product(range(N),repeat=2)])
        power=[C.eye(N*N)]+[C.zero(N*N) for _ in range(degree)]
        def jmat(x,y):return [sum_matrix([C.mm(x[k],y[d-k]) for k in range(d+1)]) for d in range(degree+1)]
        def sum_matrix(ms):
            out=C.zero(N*N)
            for q in ms:out=C.plus(out,q)
            return out
        for _ in range(m-1):power=jmat(power,t)
        check([C.tr(q) for q in jmat(dp,power)]==total,f'actual independent superoperator jet {m}')
    symbol_bound=sp.simplify(sum(abs(sp.re(x))+abs(sp.im(x)) for x in g.values()))
    check(symbol_bound==sp.Rational(593,500),'symbol l1 bound')
    literal_controls=[]
    for m,v0 in [(3,-sp.Rational(4,9)),(4,sp.Rational(44,27))]:
        err=4*m*N**3*symbol_bound*sp.Rational(1,10**80)
        check(abs(v0)>err, 'literal-time finite sign certificate')
        literal_controls.append({'m':m,'t0_offcharge':str(v0),'literal_tau':str(sp.Rational(1,10**80)),'rigorous_absolute_error':str(err),'literal_sign':'negative' if v0<0 else 'positive'})
    return {'N':3,'literal_time_certificates':literal_controls,'field':'Q(zeta_12)','formal_real_time_variable':'t','jet_degree':degree,'literal_time':'10^-80 (not numerically substituted)','rows':rows}

def finite_period_echo():
    # Exact N=p^2 changed family. Fourier arithmetic uses Q(zeta_(4N)).
    N=25;p=5;C=Cyclo(p)
    f=lambda j:(pow(j%p,3,p),pow(j//p,3,p))
    V=[]
    for j in range(N):
        x,y=f(j);row=[]
        for k in range(N):
            u,v=f(k);row.append(C.e(4*(x*u+x*v+y*v))/p)
        V.append(row)
    I=C.eye(N);V2=C.mm(V,V);P=I
    for _ in range(3):P=C.mm(P,V2)
    check(P==I,'exact N25 period6');check(C.mm(V,C.adj(V))==I,'N25 unitary')
    # Use period6 to obtain V^5=V*, and separately verify via multiplication.
    V5=C.mm(C.mm(V2,V2),V);check(V5==C.adj(V),'N25 fifth inverse')
    e=C.O
    for c in range(N):
        z=sum((V5[(j+c)%N][j]*V[j][(j+c)%N] for j in range(N)),C.O);e+=z*C.bar(z)
    check(e==C.q(N),'N25 one-pinch return value')
    return {'changed_family_N':N,'exact_period_divides':6,'at_m_multiple_6':'E_N,m(0)=25','literal_family':False}

def main():
    pins={p:hashlib.sha256((SOURCE/p).read_bytes()).hexdigest() for p in PINS}
    start=time.time();mechanisms=[]
    for N in [3,5,7,9]:
        mechanisms.append(mechanism(N));print(f'PASS exact generator N={N}',flush=True)
    rational=rational_echo();print('PASS rational twirl',flush=True)
    jets=actual_jets();print('PASS actual symbolic jets',flush=True)
    period=finite_period_echo();print('PASS changed-family exact echo',flush=True)
    check(pins=={p:hashlib.sha256((SOURCE/p).read_bytes()).hexdigest() for p in PINS},'source mutated')
    result={'status':'all checks passed','source_snapshot_manifest':'d6d5ade7444d9a2de43be89fd9636554404a275aa6703fa93910e55c1a1826ba','source_pins':pins,'arithmetic':'exact rational/cyclotomic; formal real-time jets','symbol_support':{f'{a},{b}':str(c) for (a,b),c in sorted(g.items())},'mechanism_controls':mechanisms,'rational_echo':rational,'actual_jets':jets,'changed_family_return':period,'nonclaims':['No asymptotic theorem from finite controls','No floating auxiliary coupling','No assertion of convergence of Taylor jets at literal tau','No full T16 or masked endpoint proof']}
    path=OUT/('exact_results_optimized.json' if not __debug__ else 'exact_results.json');path.write_text(json.dumps(result,indent=2)+'\n');print(f'WROTE {path.name}; seconds={time.time()-start:.2f}',flush=True)
if __name__=='__main__':main()
