"""N10 [N]/[H]: gas generating function for the resummed level-h_p isotropic sum X(p) (sg=+1 convention).
X = 2[ e^{pR} (sinh(2p w_o) + 1) - 1 ],  R = 2*sum_c phi_c  (even coefficient types c in {sqrt2,2,2sqrt2,4}, both signs),
w_o = w*(1+S_close) (odd single-bump activity incl. close-range merged classes).  Inputs: N10 logs a_gas_p47_G19.json."""
import json, numpy as np, cmath, math
d=json.load(open('/workspace/bgs-lineN/N10/logs/a_gas_p47_G19.json')); res=d['res']; ws=complex(*res[0]['r'])
from collections import defaultdict
T=defaultdict(dict)
for r in res[1:]:
    if r['type']!='tri': T[(r['type'],r['s'])][r['g']]=complex(*r['r'])/ws
phi={}; close=0
for key,v in T.items():
    inf=np.mean([v[g] for g in range(8,13)]); phi[key]=inf
for c in ['r2','2','2r2','4']: print('phi_%s'%c, phi[(c,1)], phi[(c,-1)])
# close-range correction per odd bump: deviations at g=1..6 for the distinct types r2, 2+r2 (= r2 at odd eps-positions), 2, 2r2, 4 (2-r2 duplicates 2+r2 shifted; its s=-1,g=1 is the family itself)
S=0
for key in [('r2',1),('r2',-1),('2+r2',1),('2+r2',-1),('2',1),('2',-1),('2r2',1),('2r2',-1),('4',1),('4',-1)]:
    v=T[key]; S+=sum(v[g]-phi[key] for g in range(1,7))
S*=2   # both sides (A-side small g and the mirror side near B, cf. g=k-5..k in the p=47 scan)
print('S_close',S,abs(S))
R=2*(phi[('r2',1)]+phi[('2',1)]+phi[('2r2',1)]+phi[('4',1)])
c0=2.9866e-5-6.599e-6j; c4=1.0413e-6-3.1164e-6j
print('R',R,' check 2(c0+c4)=',2*(c0+c4))
def X(p,wo,R): return 2*(cmath.exp(p*R)*(cmath.sinh(2*p*wo)+1)-1)
out=dict(ws=[ws.real,ws.imag],R=[R.real,R.imag],S=[S.real,S.imag],phi={k[0]+str(k[1]):[z.real,z.imag] for k,z in phi.items()})
rows=[]
for variant,wo in [('nominal',ws),('close+',ws*(1+S)),('close-',ws*(1-S))]:
    ps=np.arange(3,40001,2); Xs=np.array([X(p,wo,R) for p in ps])
    lin=4*ps*(ws+c0).real
    G=(np.abs(1+Xs)**2-1)/(2*lin)
    neg=ps[Xs.real<0]; m1=np.abs(1+Xs)
    i2=np.argmax(np.abs(Xs)>=2)
    r=dict(variant=variant,first_ReX_neg=int(neg[0]) if len(neg) else None,
           ReX_neg_frac=float(np.mean(Xs.real<0)),min_abs1pX=float(m1.min()),argmin_p=int(ps[m1.argmin()]),
           p_absX_ge2=int(ps[i2]),phase_at=float(cmath.phase(Xs[i2])),minG=float(G.min()),p_minG=int(ps[G.argmin()]))
    for pp in [47,101,1001,1165,1271,2001,4001,4221,5001,8001,10001,16001,20001,40001]:
        z=X(pp,wo,R); r['p%d'%pp]=[z.real,z.imag,abs(z),(abs(1+z)**2-1)/(2*4*pp*(ws+c0).real)]
    rows.append(r); print(json.dumps(r))
out['rows']=rows
json.dump(out,open('/workspace/bgs-lineN/N10/logs/b_genfun.json','w'),indent=1)
