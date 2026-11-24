"""Symbolic identities entering the transfer formula, over polynomial rings of characteristic zero."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sympy as s
a,b,x,y,h,v=s.symbols("a b x y h v")
S=s.Matrix([[3,4],[2,3]])
def omega(u,w):
    return u[0]*w[1]-u[1]*w[0]
vec=s.Matrix([a,b]); A,B=S*vec
def kernel(q,r):
    return -(3*q*q-2*q*r+3*r*r)/8
lhs=kernel(x,y-a)+b*(y-a/2)
rhs=B*(x+A/2)+kernel(x+A,y)
assert s.expand(lhs-rhs)==0
P=s.Matrix([[h,2*v],[v,h]])
assert s.simplify(P**2-s.eye(2)-2*h*P)==-(h*h-2*v*v+1)*s.eye(2)
z=s.Matrix(s.symbols("z0 z1"));w=s.Matrix(s.symbols("w0 w1"))
assert s.expand(omega(vec,S*w)-omega(S*z+vec,S*w)+omega(z,w))==0
q2=s.sqrt(2)
assert s.simplify((A+q2*B)-(3+2*q2)*(a+q2*b))==0
assert s.simplify((A-q2*B)-(3-2*q2)*(a-q2*b))==0
from coefficients import raw_symbol
c=raw_symbol()
assert all(c.get((-i,-j))==(re,-im) for (i,j),(re,im) in c.items())
assert sum(abs(re)+abs(im) for re,im in c.values())==4744
print("Egorov kernel, Pell identity modulo the norm equation, symplectic telescoping, stable/unstable coordinates, and Hermitian symbol: passed.")
