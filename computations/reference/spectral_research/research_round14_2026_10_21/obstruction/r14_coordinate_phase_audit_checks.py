"""Exact audit checks; Python standard library only."""
from pathlib import Path
from fractions import Fraction as F
import hashlib, json
root=Path(__file__).resolve().parent
source=root.parent/"structural"/"r14_original_coordinate_phase_bridge_test.md"
source_sha=hashlib.sha256(source.read_bytes()).hexdigest()
assert source_sha=="7b6657c8e1ca2ee91391509c2c97b9054715681a0afa2cedff94f8dd4c4ecc3f"
def z8(e):
    e %= 8
    row=[0,0,0,0]
    row[e%4]=1 if e<4 else -1
    return row
gauss_cases=0
for N in (1,3,5,7):
    for d in range(8):
        lhs=[0,0,0,0]
        for m in range(4):
            lhs=[x+y for x,y in zip(lhs,z8(2*d*m-3*N*m*m))]
        assert lhs==[2*x for x in z8(-3*N+3*N*d*d)]
        gauss_cases+=1
# Rational polynomial algebra; final variable I satisfies I^2=-1.
names=("Q","s","q","m","n","k","l","Fqq","B","Bq","pi","I")
zero=(0,)*len(names)
class Poly:
    def __init__(self,value=0,terms=None):
        self.terms={p:F(c) for p,c in (terms or {}).items() if c}
        if terms is None and value: self.terms[zero]=F(value)
    @staticmethod
    def coerce(v): return v if isinstance(v,Poly) else Poly(v)
    @staticmethod
    def var(name):
        e=[0]*len(names); e[names.index(name)]=1
        return Poly(terms={tuple(e):F(1)})
    def __add__(self,other):
        out=self.terms.copy()
        for p,c in self.coerce(other).terms.items(): out[p]=out.get(p,F())+c
        return Poly(terms=out)
    __radd__=__add__
    def __neg__(self): return Poly(terms={p:-c for p,c in self.terms.items()})
    def __sub__(self,o): return self+-self.coerce(o)
    def __rsub__(self,o): return self.coerce(o)+-self
    def __mul__(self,o):
        out={}
        for p,c in self.terms.items():
            for q,d in self.coerce(o).terms.items():
                e=[a+b for a,b in zip(p,q)]
                j=e[-1]; e[-1]=j%2; key=tuple(e)
                out[key]=out.get(key,F())+(-1)**(j//2)*c*d
        return Poly(terms=out)
    __rmul__=__mul__
    def __truediv__(self,o): return self*F(1,o)
    def __pow__(self,n):
        value=Poly(1)
        for _ in range(n): value=value*self
        return value
    def __eq__(self,o): return self.terms==self.coerce(o).terms
Q,s,q,m,n,k,l,Fqq,B,Bq,pi,I=[Poly.var(x) for x in names]
f0=lambda x,y:-(3*x*x-2*x*y+3*y*y)/8
assert f0(Q,s+4)-f0(Q,s)-(Q-3*s-6)==0
assert f0(Q+1,s)-f0(Q,s-3)-(-2*s+3)==0
assert f0(q,q+m)-f0(q,q+n)+(m-n)*q/2+3*(m*m-n*n)/8==0
assert 3*(Q-3*s)**2-(3*Q**2-2*Q*s+3*s**2)==-16*Q*s+24*s**2
direct=2*pi*l*Bq+2*pi**2*I*(k*l+l*l*Fqq)*B
symbol=-I*(2*pi*I*l*Bq+((2*pi*I)**2*k*l+(2*pi*I)**2*l*l*Fqq)*B/2)
assert direct==symbol
# Coefficients in units of 1/sqrt(2); exact cos(alpha),sin(alpha).
d_coeff=[F(2,100)*(F(-3,5)-F(4,5)),F(2,100)*(F(-3,5)+F(4,5))]
assert d_coeff==[F(-7,250),F(1,250)]
def r_second(c14,c2): return 196*c14*(1+c2)-4*(1-c14)*c2
assert r_second(1,1)==392 and r_second(-1,-1)==8
hessians=[]
for c14,c2,R2 in [(1,1,8),(-1,-1,392)]:
    V2=-196*c14+F(r_second(c14,c2),10)
    for cp in (F(-3,5),F(3,5)): hessians.append(V2+R2*cp/100)
assert hessians==[F(-19606,125),F(-19594,125),F(24306,125),F(24894,125)]
tau=F(1,10**80)
assert 400**2>2*250**2
assert 4*10**13*tau/6<F(1,800)
assert F(2*12297*3,250)-10**44*tau**3>200
audit=root/"r14_independent_coordinate_phase_audit.md"
result={
 "source_sha256":source_sha,
 "audit_sha256":hashlib.sha256(audit.read_bytes()).hexdigest(),
 "gauss_exact_cyclotomic_cases":gauss_cases,
 "deck_polynomial_identities":"passed",
 "weyl_subprincipal_sign":"passed in rational polynomial ring with I^2=-1",
 "unequal_sheet_unperturbed_phase":"passed",
 "even_alias_first_coefficients_in_units_of_1_over_sqrt2":[str(x) for x in d_coeff],
 "protected_hessians_div_pi2":[str(x) for x in hessians],
 "tau_smallness_and_200tau_margin":"passed by exact rational inequalities",
 "full_Hdiag_proved":False,"full_Hdiag_disproved":False}
(root/"r14_coordinate_phase_audit_checks.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))

