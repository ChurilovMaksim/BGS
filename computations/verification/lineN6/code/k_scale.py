"""N6 (2) [N]: size of the positive aliased linear part at level h_p after the W' normalisation, against RMT_m ~ 4m, the frozen
level-h_p main term, and the D7 scale.  P_m = phi^-1 * 2 rho * 2(d-2)/d^2 |Z_rho|^2 Re X  (lower bound uses phi(2h) <= h).
Re X: exact (p <= 13, logs/f_iso) or 4p Re(c_half + c_0) with c_half = 3.435779e-4 (g_sign), c_0 = 2.987e-5 (f_iso p=13)."""
import sys, json, math, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import *
exact={5:0.003532781881527897,7:0.010723807474251626,11:0.01649269773570629,13:0.01942921087800924}
c=3.435779e-4+2.987e-5
out=[]
for p in [5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79]:
    m=3*p; h,nu0=nu_rho(m,1); tw=TW(m,nu0,L=8,K=16); Z=abs(Zbatch(tw,[[0.0]*m])[0])
    x,y=1,1
    for _ in range(p-1): x,y=x+2*y,x+y
    d=x; ReX=exact.get(p,4*p*c)
    lz=2*math.log(Z); 
    logP=math.log(2*2*(d-2))-2*math.log(d)+lz+math.log(ReX)-math.log(h)
    logmain=math.log(2*(d-2))-2*math.log(d)+lz-math.log(h)
    rec=dict(p=p,m=m,ReX=ReX,log10_P=logP/math.log(10),P_over_m=math.exp(logP)/m,main_hp_over_m=math.exp(logmain)/m,
             D7_scale_over_m=1.0184224**m/m,Zroot=Z**(1/m))
    out.append(rec); print(json.dumps(rec),flush=True)
json.dump(out,open('logs/k_scale.json','w'),indent=1)
