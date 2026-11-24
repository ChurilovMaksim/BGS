"""Symbolic checks of arithmetic signs and of the first variation of the expanding multiplier."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sympy as s
a,b,c,d,N=s.symbols('a b c d N',integer=True)
S=s.Matrix([[3,4],[2,3]])
B=s.Matrix([[3,-4],[-2,3]])
def even(z):return all(int(q)%2==0 for q in s.Poly(s.expand(z),a,b,c,d,N).coeffs())
assert even(N*(a*b+c*d+a*d-b*c-(a+c)*(b+d)))
z=B*s.Matrix([a,b]);assert even(N*(z[0]*z[1]-a*b))
z=S*s.Matrix([a,b]);assert even(z[0]*z[1]-a*b)
sign=s.diag(-1,1);assert B*sign==sign*S
gqq,gqp,gpp=s.symbols('gqq gqp gpp')
H=s.Matrix([[gqq,gqp],[gqp,gpp]]);J=s.Matrix([[0,1],[-1,0]])
r=s.Matrix([1,-1/s.sqrt(2)]);ell=s.Matrix([[s.Rational(1,2),-1/s.sqrt(2)]])
assert s.simplify(B*r-(3+2*s.sqrt(2))*r)==s.zeros(2,1)
assert s.simplify(ell*B-(3+2*s.sqrt(2))*ell)==s.zeros(1,2)
assert s.simplify((ell*J*H*r)[0]-(gqq-gpp/2)/s.sqrt(2))==0
print("Lattice cocycle, covariance, parity, and expanding multiplier: passed.")
