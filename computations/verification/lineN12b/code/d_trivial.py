"""N12b [CA*] (float with crude rounding margin): t-uniform rigorous step bound in the ORIGINAL 2-norm,
||A(t)|| <= sum_n |w_4(n)| ||M_n||_F (+ D*RAD entrywise radius + Galerkin->true PERT), hence Gamma_out(any theta) <= that bound (k=1, no cells).
Rounding: each float sum inflated by (1+1e-12)."""
import sys, json, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N12/code'); import a_ops as A
fro=np.sqrt((np.abs(A.MS)**2).sum(axis=(1,2)))*(1+1e-12)
B=float((np.abs(A.COEF0)*(1+1e-12)*fro).sum()*(1+1e-12)+A.D*A.RAD*np.abs(A.COEF0).sum()+A.PERT)
res=dict(bound_triangle_Frobenius=B,D=int(A.D),RAD=float(A.RAD),PERT=float(A.PERT),mu_star=1.9154732,label='[CA*] t-uniform; useless vs T-prime')
print(json.dumps(res)); json.dump(res,open('logs/d_trivial.json','w'))
