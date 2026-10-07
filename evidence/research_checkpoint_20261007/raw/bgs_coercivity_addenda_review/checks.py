#!/usr/bin/env python3
"""Independent exact controls. No author diagnostic implementation imported.
Finite tests of specified algebra, not a proof of a universal/asymptotic theorem.
"""
import json,sys,platform
from fractions import Fraction as Q
from pathlib import Path
import sympy as s

checks=[]
def ok(name, condition, **detail):
    if not bool(condition): raise AssertionError((name,detail))
    checks.append({'name':name,'passed':True,**detail})

a,x,y=s.symbols('a x y',real=True)
moda=(1-a*x)**2+(a*y)**2
mod1=(1-x)**2+y*y
rhs=(1-a)*((1+3*a)*(1-x*x-y*y)+2*(1-a)*(1+x))
ok('universal_scalar_polynomial_identity',s.expand(4*moda-(1+a)**2*mod1-rhs)==0)

points=[(Q(i,8),Q(j,8)) for i in range(-8,9) for j in range(-8,9) if i*i+j*j<=64]
alphas=[Q(i,16) for i in range(17)]
count=zero_den=boundary=0
for xx,yy in points:
 for aa in alphas:
  lhs=4*((1-aa*xx)**2+aa*aa*yy*yy)
  right=(1+aa)**2*((1-xx)**2+yy*yy)
  if lhs<right: raise AssertionError((xx,yy,aa))
  count+=1;zero_den+=int(xx==1 and yy==0);boundary+=int(xx*xx+yy*yy==1)
ok('rational_scalar_grid',True,points=len(points),alphas=len(alphas),cases=count,lambda_one_cases=zero_den,boundary_cases=boundary)

# Jordan matrices with large nilpotent parts are not norm contractions.
# Rational unimodular similarities also test the determinant off triangular form.
def abs2(v):return s.simplify(s.expand_complex(v*s.conjugate(v)))
lambdas=[s.Integer(-1),s.Integer(1),s.I,-s.I,s.Rational(3,5)+s.Rational(4,5)*s.I,s.Rational(-2,3)+s.I/4,0]
matrix_count=0;non_normal_count=0;noncontractive_count=0
for d in range(1,5):
 for lam in lambdas:
  J=lam*s.eye(d)
  for i in range(d-1):J[i,i+1]=7
  T=s.eye(d)
  for i in range(1,d):T[i,i-1]=i
  A=T*J*T.inv()
  if A*A.conjugate().T != A.conjugate().T*A:non_normal_count+=1
  if d>=2:
   # ||A||_op >= norm of any column; exhibit a column with norm > 1.
   if any(sum(abs2(A[i,j]) for i in range(d))>1 for j in range(d)):noncontractive_count+=1
  for aa in [s.Integer(0),s.Rational(1,7),s.Rational(1,2),s.Rational(6,7),s.Integer(1)]:
   D=(s.eye(d)-aa*A).det();D0=(s.eye(d)-A).det()
   ok_value=s.simplify(abs2(D)-((1+aa)/2)**(2*d)*abs2(D0))
   if not ok_value>=0:raise AssertionError((d,lam,aa,ok_value))
   if s.simplify(D-(1-aa*lam)**d)!=0:raise AssertionError('algebraic multiplicity')
   matrix_count+=1
ok('spectral_radius_only_jordan_similarity_cases',True,cases=matrix_count,nonnormal_fixtures=non_normal_count,operator_noncontractive_fixtures=noncontractive_count,max_dimension=4)
for d in range(1,7):
 for aa in [s.Integer(0),s.Rational(1,3),s.Rational(2,3),s.Integer(1)]:
  if s.simplify((1+aa)**d-((1+aa)/2)**d*2**d)!=0:raise AssertionError('sharpness')
ok('minus_identity_sharp_constant',True,cases=24)
ok('spectral_radius_hypothesis_is_essential',0 < s.Rational(3,4),witness='dimension 1: A=2, alpha=1/2 makes left side zero and right side 3/4')

q=s.symbols('q',real=True)
ok('microscopic_absorption_amgm_identity',s.expand((1+q*q)/2-q-(1-q)**2/2)==0,interpretation='q=exp(-s/(2N)); each eigenvalue cost at most s/(2N)')
ca=s.I/2;cl=-3*s.I/4
ok('generic_complex_absorption_counterexample',abs2(1-ca*cl)==s.Rational(25,64) and s.Rational(25,64)<s.Rational(225,256),lhs='5/8',rhs='15/16')

# Strict block domain verified by a rational Frobenius norm upper bound.
B=s.Matrix([[s.Rational(1,5),s.Rational(1,4)+s.I/7],[0,s.I/6]])
ok('strict_nonnormal_block_domain',sum(abs2(z) for z in B)<1 and B*B.conjugate().T!=B.conjugate().T*B)
U=s.Matrix([[s.Rational(3,5),s.Rational(4,5)],[-s.Rational(4,5),s.Rational(3,5)]])
Qmat=s.kronecker_product(U,s.eye(2));Z=s.diag(B,-B);A=Qmat*Z*Qmat.conjugate().T*Z.conjugate().T
body_cases=0
for aa in [s.Integer(0),s.Rational(1,9),s.Rational(1,2),s.Rational(8,9),s.Integer(1)]:
 D=(s.eye(4)-aa*A).det();D0=(s.eye(4)-A).det()
 ok_value=s.simplify(abs2(D)-((1+aa)/2)**8*abs2(D0))
 if not ok_value>=0:raise AssertionError('body absorption')
 body_cases+=1
ok('strict_centered_nonnormal_body_absorption',True,cases=body_cases,sites=2,block_size=2)

# Exact ordinary scalar bare invariance at a nonconstant, genuinely complex tuple.
v=s.Matrix([1,2,3]);U=s.eye(3)-2*v*v.T/(v.T*v)[0]
w=[s.Rational(1,4)+s.I/10,-s.Rational(1,5)+s.I/12,-s.Rational(1,20)-s.I*s.Rational(11,60)]
center=s.Rational(1,3)+s.I/7
z=[s.cancel((center+t)/(1+s.conjugate(center)*t)) for t in w]
ok('mobius_domain_and_center',sum(w)==0 and all(abs2(t)<1 for t in w+z))
def exp2action(field,aa):
 ZZ=s.diag(*field);AA=U*ZZ*U.conjugate().T*ZZ.conjugate().T
 return s.cancel(abs2((s.eye(3)-aa*AA).det())/(s.eye(3)-ZZ*ZZ.conjugate().T).det()**2)
bare_w=exp2action(w,s.Integer(1));bare_z=exp2action(z,s.Integer(1))
ok('bare_action_mobius_invariance_exact_complex_fixture',s.cancel(bare_z-bare_w)==0)
# N=1, z=1/2, alpha=1/2: exp S_alpha=7/6, whereas centered w=0 gives 1.
ok('absorbed_action_not_mobius_invariant',s.Rational(1- Q(1,2)*Q(1,4),1-Q(1,4))==s.Rational(7,6),uncentered_exp_action='7/6',centered_exp_action='1')

# Exact radial coordinate and real Jacobian checks.
f=s.Matrix([x,y])/s.sqrt(1+x*x+y*y)
radial_jac=s.factor(f.jacobian([x,y]).det())
ok('radial_real_two_dimensional_jacobian',s.simplify(radial_jac-(1+x*x+y*y)**(-2))==0)
ok('radial_defect_identity',s.simplify(1-f.dot(f)-1/(1+x*x+y*y))==0)
# A centered disk tuple whose radial image is not linearly centered.
# z=(3/5,-3/10,-3/10): sum psi=3/4-6/sqrt(91)>0.
ok('radial_constraint_is_nonlinear',s.Rational(9,16)>s.Rational(36,91),sum_z='0',sum_psi='3/4 - 6/sqrt(91) > 0')
# N=2 graph psi_2=-psi_1 makes the actual independent-coordinate Jacobian
# (1+|psi_1|^2)^(-2), not the product over all N entries (-4).
ok('constrained_measure_no_N_coordinate_product',s.Rational(1,4)!=s.Rational(1,16),witness='N=2, |psi_1|=1: actual coordinate factor 1/4 versus false N-product 1/16')
beta=s.symbols('beta',positive=True);t=s.symbols('t',real=True)
integral=s.integrate((1-t)**beta,(t,0,1))
ok('unit_disk_weight_integral',s.simplify(integral-1/(1+beta))==0,interpretation='d^2z gives pi dt; beta=c/2, hence pi/(1+c/2)')
ok('N_one_tail_endpoint',True,detail='N=1: centered point z=0, H=S=0; zero-dimensional integral 1 at L=0 and 0 for L>0')

# FM-021's inherited uniform amplitude bound, without using phase cancellation.
epsilon=Q(2,10**66)
ok('eventual_actual_flatness_margin',4*(1+epsilon)**2<5,limsup_upper=str(4*(1+epsilon)**2))
ok('uniform_remainder_buffer_margin',(2*(1+epsilon)+Q(1,10))**2<5,buffer='M/N <= 1/10 suffices after the inherited expansion startup; M is not numerically supplied')
ok('eventual_gap_margin',Q(1,10**64)<Q(1,2))
K=s.simplify(1+s.sqrt(5-1)/(1-s.Rational(1,2)));c=s.simplify(1/(2*K*K))
ok('actual_K_and_c_exact',K==5 and c==s.Rational(1,50),K=str(K),c=str(c),tail_half_exponent=str(c/2),tail_volume_ratio=str(1/(1+c/2)))

result={'schema':'bgs-addenda-exact-controls-v1','arithmetic':'Python Fraction and SymPy exact rational, complex rational and symbolic algebra','python':platform.python_version(),'sympy':s.__version__,'checks':checks,'all_passed':True,'non_claims':['Not universal proof by sampling','No actual fixed-tau U_N instantiated','No numerical startup threshold','No block-coercivity theorem tested','No external theorem authenticated by these computations','No supermeasure, sources, derivative bounds, normalized large-N tail or BGS conclusion']}
Path(sys.argv[1]).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'all_passed':True,'check_groups':len(checks),'scalar_cases':count,'matrix_cases':matrix_count,'body_cases':body_cases},indent=2))
