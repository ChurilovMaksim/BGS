#!/usr/bin/env python3
"""Exact bounded checks; universal proof is in real_absorption_addendum.md."""
import sympy as s, json, time, platform
start=time.time();a,x,y=s.symbols('a x y',real=True)
l=x+s.I*y
lhs=s.expand(4*(1-a*l)*(1-a*s.conjugate(l))-(1+a)**2*(1-l)*(1-s.conjugate(l)))
rhs=(1-a)*((1+3*a)*(1-x*x-y*y)+2*(1-a)*(1+x))
assert s.expand(lhs-rhs)==0
points=[s.Rational(j,4)+s.I*s.Rational(k,4) for j in range(-4,5) for k in range(-4,5) if j*j+k*k<=16]
alphas=[s.Rational(j,8) for j in range(9)]
count=0
for aa in alphas:
 for ll in points:
  diff=s.simplify((1-aa*ll)*(1-aa*s.conjugate(ll))-(1+aa)**2*s.Rational(1,4)*(1-ll)*(1-s.conjugate(ll)))
  assert diff>=0;count+=1
matrices=[s.diag(-1,-1),s.Matrix([[s.Rational(1,2),s.Rational(1,8)],[0,s.Rational(1,2)]]),s.Matrix([[s.I/2,2],[0,-s.I/3]])]
# Last fixture tests the stronger spectral-radius statement and is not a norm contraction.
for M in matrices:
 for aa in alphas:
  d=M.rows;D=(s.eye(d)-aa*M).det();D1=(s.eye(d)-M).det()
  assert s.simplify(D*s.conjugate(D)-((1+aa)/2)**(2*d)*D1*s.conjugate(D1))>=0
# Exact actual-body-shaped controls using finite auxiliary unitaries.
U=s.eye(3)-s.Rational(1,7)*s.Matrix([1,2,3])*s.Matrix([[1,2,3]])
Z=s.diag(s.Rational(1,3)+s.I/5,-s.Rational(1,4)+s.I/7,-s.Rational(1,12)-12*s.I/35)
A=U*Z*U.conjugate().T*Z.conjugate().T
for aa in alphas:
 D=(s.eye(3)-aa*A).det();D1=(s.eye(3)-A).det()
 assert s.simplify(D*s.conjugate(D)-((1+aa)/2)**6*D1*s.conjugate(D1))>=0
assert s.Abs(1-s.I/2*(-3*s.I/4))==s.Rational(5,8)
assert (1+s.Abs(s.I/2))*s.Abs(1+3*s.I/4)/2==s.Rational(15,16)
out={'arithmetic':'Exact SymPy rational/complex polynomial arithmetic','symbolic_factorization':True,'scalar_rational_disk_points':len(points),'alpha_values':[str(q) for q in alphas],'scalar_cases':count,'matrix_fixtures':3,'matrix_cases':27,'body_shaped_matrix_cases':9,'contains_nondiagonalizable_fixture':True,'contains_noncontractive_spectral_radius_fixture':True,'complex_alpha_counterexample':True,'runtime_seconds':time.time()-start,'python':platform.python_version(),'sympy':s.__version__,'non_claims':['No actual U_N instantiated','No complex-source or derivative theorem','No supersymmetric measure or tail theorem','Finite checks do not replace the universal algebraic proof']}
print(json.dumps(out,indent=2))
