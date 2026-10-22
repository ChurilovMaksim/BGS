import sympy as s,json,time
from pathlib import Path
R=Path('/workspace/shared/bgs_seven_adic_independent_review');S=R/'actual_source';q,w=s.symbols('q w');start=time.time()
def expand_t(t):
 a=[s.Integer(0)]*7;a[2*t%7]=1
 for u in range(t+1,7):
  a=[s.expand(a[k]+2*q**u*a[(k-1)%7]+q**(2*u)*a[(k-2)%7]) for k in range(7)]
 return a
C=s.Matrix([expand_t(t) for t in range(7)]);yd=json.loads((S/'bounded_boundary_polynomials.json').read_text());den=s.sympify(yd['denominator']);yn=s.Matrix([[s.sympify(v) for v in yd['y_numerators']]])
r=s.Matrix([[C[0,(k-5)%7] for k in range(7)]])
assert all(s.expand(v)==0 for v in yn*C-den*r)
print('Exact seven y numerator identities passed',flush=True)
DM=s.polys.matrices.DomainMatrix.from_Matrix(C).convert_to(s.GF(5).poly_ring(q));AI,ad=DM.inv_den();AI=AI.to_Matrix();ad=ad.as_expr()
kd=json.loads((S/'bounded_boundary_norm_input.json').read_text());kden=s.sympify(kd['denominator']);loaded=[s.sympify(v) for v in kd['coefficients_w']]
# Directly square the seven-term inverse, retaining the pair indices independently.
K=[0]*7
for i in range(7):
 for j in range(7):
  shift=(i+j)%7
  weight=(-1)**(i+j)*q**(14-i-j)
  K[shift]+=weight*sum(C[0,(a-i-j)%7]*AI[a,0] for a in range(7))
K=[s.Poly(s.expand(K[j]-K[6]),q,modulus=5).as_expr() for j in range(6)]
for j in range(6):assert s.Poly(s.expand(K[j]*kden-loaded[j]*ad),q,modulus=5).is_zero
P=DM.det().as_expr()
assert s.Poly(den,q,modulus=5).monic()==s.Poly(P,q,modulus=5).monic()
assert s.Poly(kden,q,modulus=5).monic()==s.Poly(P,q,modulus=5).monic()
print('K numerator and denominator identities passed',flush=True)
# Norm by multiplication operator in basis1,w,...,w5 modulo Phi7, rather than resultant.
N=s.zeros(6)
for c in range(6):
 for k,coeff in enumerate(loaded):
  exponent=(c+k)%7
  if exponent==6:
   for j in range(6):N[j,c]-=coeff
  else:N[exponent,c]+=coeff
ndm=s.polys.matrices.DomainMatrix.from_Matrix(N).convert_to(s.GF(5).poly_ring(q));norm=s.Poly(ndm.det().as_expr(),q,modulus=5)
pinned=json.loads((S/'bounded_boundary_norm.json').read_text());want=s.Poly.from_list(pinned['norm_coefficients'],q,modulus=5)
assert norm==want
out={'seven_y_identities':True,'K_identity':True,'denominators_associate_P':True,'independent_norm_matrix_determinant_matches':True,'norm_degree':norm.degree(),'seconds':time.time()-start}
(R/'actual_algebra_results.json').write_text(json.dumps(out,indent=2));print(json.dumps(out),flush=True)
