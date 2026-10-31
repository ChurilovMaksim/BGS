"""Line L [N]: spectral radius r_abs of the ABSOLUTE exact-collision carry operator.
Collisions of k-blocks: v in Z^k with sum_j v_j lam^j = 0  <=>  v = (X^2-6X+1)E(X).
Weight of v: prod_j rho(v_j), rho(d) = sum_a |ghat(a)||ghat(a-d)|  (ghat = i^a J_a(1.8); rho(0)=1).
Carry states (e_{j-1}, e_j), |e|<=EMAX; transition (a,b)->(b,e) with weight rho(e-6b+a).
r_abs = spectral radius (power iteration on nonneg matrix)."""
import sys, numpy as np, itertools, json
from scipy.special import jv
EMAX=int(sys.argv[1]) if len(sys.argv)>1 else 8; X=float(sys.argv[2]) if len(sys.argv)>2 else 1.8
A=np.arange(-60,61); J=np.abs(jv(A,X))
def rho(d):
    d=int(d)
    if abs(d)>110: return 0.0
    s=0.0
    for a in range(-60,61):
        b=a-d
        if -60<=b<=60: s+=J[a+60]*J[b+60]
    return s
R={d:rho(d) for d in range(-200,201)}
print("rho(0..8):",[round(R[d],6) for d in range(9)], "sum|J|^2=",(J**2).sum(), "G=sum|J|=",J.sum())
es=range(-EMAX,EMAX+1); st=[(a,b) for a in es for b in es]; idx={s:i for i,s in enumerate(st)}
n=len(st); T=np.zeros((n,n))
for (a,b) in st:
    for e in es:
        d=e-6*b+a
        if abs(d)<=200: T[idx[(b,e)],idx[(a,b)]]+=R[d]
ev=np.linalg.eigvals(T); r=max(abs(ev))
# also excursion generating sum at z=1 via (I - T_restricted)^{-1}
print(f"EMAX={EMAX} states={n} r_abs={r:.10f}  r_abs^(1/2)={r**0.5:.8f}")
json.dump(dict(EMAX=EMAX,x=X,r_abs=float(r)),open(f'/workspace/bgs-lineL/logs/l2_rabs_E{EMAX}.json','w'))
