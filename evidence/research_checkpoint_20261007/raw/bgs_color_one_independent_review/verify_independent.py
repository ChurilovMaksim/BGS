#!/usr/bin/env python3
"""Independent exact checks: exterior algebra, matrix Berezinian, radial integrals.
Python/SymPy exact arithmetic; mpmath quadrature only as a separate diagnostic.
No canonical files are read or changed by this verifier.
"""
import sympy as s
import json, pathlib
from functools import reduce
x,y=s.symbols('x y', positive=True)
z,tz,w,tw,a,b,c,d,T=s.symbols('z tz w tw a b c d T')
k,l=s.symbols('k l', integer=True, nonnegative=True)
p,q,r,L=s.symbols('p q r L')
class E:
    # Exterior generators in order gamma,beta,alpha,delta, whose top coefficient
    # is +1 under source (4.8): d_alpha d_delta d_gamma d_beta.
    def __init__(self, terms=0): self.v=terms.copy() if isinstance(terms,dict) else ({0:s.sympify(terms)} if terms!=0 else {})
    def __add__(self,o):
        o=o if isinstance(o,E) else E(o);v=self.v.copy()
        for i,t in o.v.items(): v[i]=v.get(i,0)+t
        return E(v)
    __radd__=__add__
    def __neg__(self): return E({i:-t for i,t in self.v.items()})
    def __sub__(self,o): return self+-asE(o)
    def __rsub__(self,o): return asE(o)+-self
    def __mul__(self,o):
        o=asE(o);v={}
        for i,u in self.v.items():
            for j,t in o.v.items():
                if i&j: continue
                inv=sum(1 for h in range(4) for jh in range(4) if (i>>h)&1 and (j>>jh)&1 and h>jh)
                v[i|j]=v.get(i|j,0)+(-1)**inv*u*t
        return E(v)
    __rmul__=__mul__
    def __truediv__(self,o): return self*asE(o).inverse()
    def inverse(self):
        body=self.v.get(0,0);assert body!=0
        nil=(self-E(body))*(1/body);out=E(1);term=E(1)
        for _ in range(4): term=term*(-nil);out=out+term
        return out*(1/body)
    def simp(self): return E({i:s.factor(t) for i,t in self.v.items() if s.simplify(t)!=0})
    def sub(self,m): return E({i:t.subs(m,simultaneous=True) for i,t in self.v.items()})
    def coeff(self,i): return s.factor(self.v.get(i,0))
    def dleft(self,h):
        return E({i^(1<<h):(-1)**((i&((1<<h)-1)).bit_count())*t for i,t in self.v.items() if i&(1<<h)})
def asE(o): return o if isinstance(o,E) else E(o)
def mm(A,B):return [[sum((A[i][k]*B[k][j] for k in range(2)),E()) for j in range(2)] for i in range(2)]
def one_minus(A):return [[(1 if i==j else 0)-A[i][j] for j in range(2)] for i in range(2)]
def ber(A):return (A[0][0]-A[0][1]/A[1][1]*A[1][0])/A[1][1]
def ber_inv(A):return (A[1][1]-A[1][0]/A[0][0]*A[0][1])/A[0][0]
def rad(t):return s.factor(s.cancel(t.subs({tz:x/z,tw:-y/w})))
def equal(f,g):assert s.simplify(s.factor(s.together(f-g)))==0,(f,g)
def equalE(f,g):
    for i in range(16): equal(f.coeff(i),g.coeff(i))
gamma,beta,alpha,delta=[E({1<<i:s.Integer(1)}) for i in range(4)]
G=gamma*beta*alpha*delta
# Direct left-derivative implementation, independent of coefficient convention.
equal(G.dleft(1).dleft(0).dleft(3).dleft(2).coeff(0),1)
Z=[[E(z),alpha],[beta,E(w)]];Zt=[[E(tz),gamma],[delta,E(tw)]]
S=ber(one_minus(mm(Zt,Z))).simp()
Q=gamma*beta+alpha*delta+gamma*w*delta*z+alpha*tw*beta*tz
S_expected=E((1-tz*z)/(1-tw*w))-Q/((1-tw*w)**2)+G*((1+tw*w)/(1-tw*w)**3)
equalE(S,S_expected)
AZB=[[E(a*b*z),a*d*alpha],[c*b*beta,E(c*d*w)]]
M=one_minus(mm(Zt,AZB)); F=ber_inv(M).simp()
equalE((ber(M)*F).simp(),E(1))
B=rad((S*F).coeff(15))
p0=a*b;q0=c*d;r0=a*d+b*c
B_expected=(1-y)*(1+q0*y)/((1+y)**3*(1-p0*x))-(r0+2*p0*q0*x*y)/((1+y)**2*(1-p0*x)**2)+p0*q0*(1-x)*(1+p0*x)/((1+y)*(1-p0*x)**3)
equal(B,B_expected)
# Surface operator: Omega_2 times SF_2, Omega_4 multiplication times SF_0,
# plus normal derivative of SF_0 BEFORE x=1. Angular reduction gives factor 2.
SF=S*F
Omega2=-Q/(2*(1-tw*w))
H=2*(rad((Omega2*SF).coeff(15))+rad(SF.coeff(0))/(2*(1+y)**2)+2*x*s.diff(rad(SF.coeff(0)),x)/(4*(1+y))).subs(x,1)
H=s.factor(H);H_expected=(1+q0*y)/((1-p0)*(1+y)**2);equal(H,H_expected)
# Derive the x integrals from exact primitives.
primitive0=-s.log(1-p*x)/p
primitive2=x/(1-p*x)
primitive_x=1/(p*p*(1-p*x))+s.log(1-p*x)/(p*p)
equal(s.diff(primitive0,x),1/(1-p*x))
equal(s.diff(primitive2,x),1/(1-p*x)**2)
equal(s.diff(primitive_x,x),x/(1-p*x)**2)
# Integration by parts for the third bulk term:
equal(s.diff(x/(1-p*x)**2,x),(1+p*x)/(1-p*x)**3)
J=(1/(1-p)-L)/p
Bx=L*(1-y)*(1+q*y)/(1+y)**3-r/((1-p)*(1+y)**2)-2*p*q*J*y/(1+y)**2+p*q*J/(1+y)
Bx_expected=L*(1-q)*(1-y)/(1+y)**3+(q*(1-y)-r)/((1-p)*(1+y)**2)
equal(Bx,Bx_expected)
Hgen=(1+q*y)/((1-p)*(1+y)**2)
combined=L*(1-q)*(1-y)/(1+y)**3+(1+q-r)/((1-p)*(1+y)**2)
equal(Bx+Hgen,combined)
BulkT=L*(1-q)*T/(1+T)**2+((2*q-r)*T/(1+T)-q*s.log(1+T))/(1-p)
SurfT=((1-q)*T/(1+T)+q*s.log(1+T))/(1-p)
TotalT=L*(1-q)*T/(1+T)**2+(1+q-r)*T/((1-p)*(1+T))
equal(BulkT+SurfT,TotalT)
equal(s.diff(BulkT,T),Bx_expected.subs(y,T))
equal(s.diff(SurfT,T),Hgen.subs(y,T))
equal(BulkT.subs(T,0),0);equal(SurfT.subs(T,0),0)
exact=(1+q0-r0)/(1-p0)
equal(exact,1+(a-c)*(b-d)/(1-a*b))
# Reproducing-kernel four diagonal families, independently from the matrices.
family1=E(x**k)
family2=-k*alpha*delta*x**(k-1)  # Table 1; (4.43)-(4.45) print a mismatching index.
family3=k*beta*gamma*x**(k-1)
family4=-(E(z*w)-l*alpha*beta)*(E(tw*tz)-l*gamma*delta)*x**(l-1)
def family_densities(test):
    B=rad((S*test).coeff(15))
    U=S*test
    H=2*(rad((Omega2*U).coeff(15))+rad(U.coeff(0))/(2*(1+y)**2)+2*x*s.diff(rad(U.coeff(0)),x)/(4*(1+y))).subs(x,1)
    return s.factor(B),s.factor(H)
B1,H1=family_densities(family1);equal(B1,x**k*(1-y)/(1+y)**3);equal(H1,1/(1+y)**2)
B2,H2=family_densities(family2);equal(B2,k*x**(k-1)/(1+y)**2);equal(H2,0)
B3,H3=family_densities(family3);equal(B3,k*x**(k-1)/(1+y)**2);equal(H3,0)
Btypo,Htypo=family_densities(-k*alpha*gamma*x**(k-1));equal(Btypo,0);equal(Htypo,0)
B4,H4=family_densities(family4)
# Integrate x polynomial for integer l=0 separately; l>=1 symbolic powers.
B4expected=l*l*(1-x)*x**(l-1)/(1+y)-2*l*y*x**l/(1+y)**2+y*(1-y)*x**l/(1+y)**3
equal(B4,B4expected);equal(H4,y/(1+y)**2)
B4x=l/(l+1)/(1+y)-2*l*y/(l+1)/(1+y)**2+y*(1-y)/(l+1)/(1+y)**3
C4=(l+(l+2)*y)/((l+1)*(1+y)**3)
equal(B4x+H4,C4)
# Closed integrals: int (1+y)^-2=1, int (1+y)^-3=1/2,
# int y(1+y)^-3=1/2, so family4 total is 1 for all l>=0.
equal((l+(l+2))/(2*(l+1)),1)
# Phase series coefficient extraction to order 9 checks the exact elementary formula.
t=s.symbols('t')
for n in range(10):
    total=sum((a**i*b**j*(1 if i==j else 0)-c*a**i*b**j*(1 if i+1==j else 0)-d*a**i*b**j*(1 if i==j+1 else 0)+c*d*a**i*b**j*(1 if i==j else 0) for i in range(n+1) for j in range(n+1) if i+j<=n),s.Integer(0))
    expected=s.series(((1+c*d)-t*(c*b+d*a))/(1-t*t*a*b),t,0,n+1).removeO().subs(t,1)
    equal(total,expected)
# Numeric check only: smooth periodic phase average vs exact for complex sources.
import mpmath as mp
mp.mp.dps=45
cases=[(.2,.3,0,0),(.2,.3,.4,.5),(0,.3,.4,.5),(.2,.3,.2,.3),(.2+.1j,.3-.15j,.4+.2j,-.3+.1j)]
nums=[]
for aa,bb,cc,dd in cases:
    aa,bb,cc,dd=map(mp.mpc,(aa,bb,cc,dd))
    pp,qq,rr=aa*bb,cc*dd,aa*dd+bb*cc
    ex=(1+qq-rr)/(1-pp)
    ph=mp.quad(lambda theta:(1-cc*mp.exp(1j*theta))*(1-dd*mp.exp(-1j*theta))/((1-aa*mp.exp(1j*theta))*(1-bb*mp.exp(-1j*theta))),[0,mp.pi,2*mp.pi])/(2*mp.pi)
    assert abs(ex-ph)<mp.mpf('1e-40')
    ll=-mp.log(1-pp)/pp if pp else 1
    row={'a':str(aa),'b':str(bb),'c':str(cc),'d':str(dd),'exact':str(ex),'phase_error':str(abs(ex-ph)),'cutoffs':[]}
    for tt in (10,1000,1000000):
        bu=ll*(1-qq)*tt/(1+tt)**2+((2*qq-rr)*tt/(1+tt)-qq*mp.log(1+tt))/(1-pp)
        su=((1-qq)*tt/(1+tt)+qq*mp.log(1+tt))/(1-pp)
        to=ll*(1-qq)*tt/(1+tt)**2+ex*tt/(1+tt)
        assert abs(bu+su-to)<mp.mpf('1e-40')
        row['cutoffs'].append({'T':tt,'bulk':str(bu),'surface':str(su),'sum':str(to),'error':str(abs(to-ex))})
    nums.append(row)
out={'status':'all exact assertions passed','arithmetic':'SymPy rational function identities over Q(a,b,c,d,x,y), plus left exterior derivatives and symbolic radial primitives','symbolic_checks':['source Berezin orientation','matrix-derived S agrees with (4.16)','two-pivot Berezinian inverse','general-source bulk coefficient','normal-derivative surface coefficient','radial primitives','finite common-cutoff formulas','all four kernel norm families (k>=1 where applicable,l>=0)','literal (4.43)-(4.45) misprinted-index product has zero pairing','phase constant terms through total bosonic degree 9'],'numeric_scope':'5 parameter examples; 45-digit phase quadrature and cutoff evaluations','numeric_checks':nums,'nonclaims':['No uniform-in-sitecount microscopic bound','No graph spectral counterexample','No convergence audit for arbitrary test-function spaces','No general higher-flavor boundary functional']}
pathlib.Path(__file__).with_name('checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='numeric_checks'},indent=2))
