#!/usr/bin/env python3
"""Exact additional checks of genuinely nonnormal left/right boosts and orientation."""
import json
import sympy as s
q=s.Rational; ii=s.I
adj=lambda A:A.conjugate().T
simp=lambda A:A.applyfunc(s.simplify)
zero=lambda A:all(s.simplify(a)==0 for a in A)
# Exact unitary, generally non-Hermitian/non-symmetric mixing.
G12=s.Matrix([[q(3,5),q(4,5),0],[-q(4,5),q(3,5),0],[0,0,1]])
G23=s.Matrix([[1,0,0],[0,q(5,13),q(12,13)],[0,-q(12,13),q(5,13)]])
U=G12*s.diag(1,ii,(3+4*ii)/5)*G23
assert zero(U*adj(U)-s.eye(3))
A=s.Matrix([[q(1,8),ii/7],[0,q(1,9)]])
B=s.Matrix([[0,q(1,10)],[q(1,11),0]])
zs=[A,B,-A-B]
for z in zs:
 D=s.eye(2)-z*adj(z)
 assert D[0,0]>0 and s.simplify(D.det())>0
Z=s.diag(*zs); Q=s.kronecker_product(U,s.eye(2)); I=s.eye(6)
da=s.simplify((I-Q*Z*adj(Q)*adj(Z)).det())
db=s.simplify((I-adj(Q)*Z*Q*adj(Z)).det())
assert s.simplify(db-s.conjugate(da))==0
assert s.im(da)!=0  # This is a genuinely complex orientation check.
# Rational singular data make C_L and C_R exact and unequal.
L=s.Matrix([[q(3,5),q(4,5)],[-q(4,5),q(3,5)]])
R=s.Matrix([[q(5,13),q(12,13)],[-q(12,13),q(5,13)]])*s.diag(1,ii)
D=s.diag(q(3,5),q(5,13)); C=s.diag(q(5,4),q(13,12))
A=simp(L*D*adj(R)); Z=s.diag(A,-A)
CL=s.diag(L*C*adj(L),L*C*adj(L)); CR=s.diag(R*C*adj(R),R*C*adj(R))
assert not zero(A*adj(A)-adj(A)*A)
assert not zero(CL-CR)
assert zero(CL*Z-Z*CR)
assert zero(CL*CL*(s.eye(4)-Z*adj(Z))-s.eye(4))
assert zero(CR*CR*(s.eye(4)-adj(Z)*Z)-s.eye(4))
g=CL.row_join(Z*CR).col_join((adj(Z)*CL).row_join(CR))
gi=CL.row_join(-Z*CR).col_join((-adj(Z)*CL).row_join(CR))
J=s.diag(*([1]*4+[-1]*4)); assert zero(adj(g)*J*g-J); assert zero(gi*g-s.eye(8))
Us=s.Matrix([[q(3,5),4*ii/5],[4*ii/5,q(3,5)]])
Q=s.kronecker_product(Us,s.eye(2)); T=gi*s.diag(Q,Q)*g
F=CL*(Q-Z*Q*adj(Z))*CL; G=CL*(Q*Z-Z*Q)*CR
assert zero(T[:4,:4]-F) and zero(T[:4,4:]-G)
assert zero(F*adj(F)-G*adj(G)-s.eye(4))
a=s.simplify((s.eye(4)-Q*Z*adj(Q)*adj(Z)).det())
d=s.simplify((s.eye(4)-Z*adj(Z)).det())
f=s.simplify(F.det())
assert s.simplify(f*s.conjugate(f)-a*s.conjugate(a)/d**2)==0
print(json.dumps({'arithmetic':'exact SymPy rational complex arithmetic','orientation':{'N':3,'k':2,'det_action':str(da),'imaginary_part_nonzero':True,'conjugate_opposite_orientation':True},'nonnormal_boost':{'N':2,'k':2,'left_right_factors_distinct':True,'rational_singular_values':['3/5','5/13'],'positive_defect':True,'J_unitarity':True,'F_G_blocks':True,'FFstar_minus_GGstar_identity':True,'determinant_action_identity':True},'result':'All exact identities passed; no universal numerical inference.'},indent=2))
