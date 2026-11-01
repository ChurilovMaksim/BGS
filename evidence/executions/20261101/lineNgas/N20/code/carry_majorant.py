"""N20 [N float scan; the decisive inequality is re-checked in exact rationals in Lean (carry_cw)]:
scalar majorant automata on the 633 carry pair states.  Edge (a,b)->(b,c) with letter-difference v = c-6b+a gets weight
kappa0 = 0.28 if v = 0 (i.i.d. letter pairs, certified rate) and kappa1 otherwise.  Scan: largest kappa1 with rho(M) <= 0.30."""
import json, numpy as np
cert=json.load(open('../logs/carry_graph_cert.json')); S=[tuple(s) for s in cert['states']]; idx={s:i for i,s in enumerate(S)}
n=len(S); A0=np.zeros((n,n)); A1=np.zeros((n,n))
for (a,b) in S:
    for c in range(-15,16):
        if abs(c-6*b+a)<=60 and (b,c) in idx:
            (A0 if c-6*b+a==0 else A1)[idx[(a,b)],idx[(b,c)]]=1
rho=lambda M: max(abs(np.linalg.eigvals(M)))
print('v=0 edges',int(A0.sum()),'v!=0 edges',int(A1.sum()),'rho(A0)',rho(A0),'rho(A0+A1)',rho(A0+A1))
lo,hi=0.0,1.0
for _ in range(60):
    m=(lo+hi)/2
    if rho(0.28*A0+m*A1)<=0.30: lo=m
    else: hi=m
print('kappa1* (rho<=0.30) = %.4e'%lo)
res=dict(n0=int(A0.sum()),n1=int(A1.sum()),rho_A0=float(rho(A0)),rho_A=float(rho(A0+A1)),kappa1_star=lo,
         rho_at_kappa1_star=float(rho(0.28*A0+lo*A1)))
# per-step equivalent of measured isolated-carry entry weights (N16 g_triple Yc-relative): c=1: 7.0e-3 over 3 steps
res['measured_c1_entry_per_step']=(7.0e-3*0.28**3)**(1/3)
print(res); json.dump(res,open('../logs/carry_majorant.json','w'),indent=1)
