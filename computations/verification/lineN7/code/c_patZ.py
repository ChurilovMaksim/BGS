"""N7 [N]: Zhat/Z_rho for the closed-form family point beta=(q+gamma)/4 (twist 1/2 + d_i), both signs; compare with N6 g_sign family ratio."""
import sys, json
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import *
from fractions import Fraction as Fr
def xy(n):
    x,y=1,0
    for _ in range(n): x,y=x+2*y,x+y
    return x,y
def mul(u,v): return (u[0]*v[0]+2*u[1]*v[1], u[0]*v[1]+u[1]*v[0])
out=[]
for p in [int(t) for t in sys.argv[1].split(',')]:
    m=3*p; k=(p-1)//2; q=xy(p)[0]; g=(xy(k+1)[0],xy(k)[1]); L=(1,0); seq=[]
    for i in range(m):
        v=mul(L,(q+g[0],g[1])); seq.append(float(Fr(2*v[0],4*q)%1)); L=mul(L,(3,2))
    for sg in (1,-1):
        h,nu=nu_rho(m,sg); tw=TW(m,nu,L=8,K=16); Z=Zbatch(tw,[[0.0]*m,seq,[(-t)%1 for t in seq]])
        rec=dict(p=p,sg=sg,ratio=[(Z[1]/Z[0]).real,(Z[1]/Z[0]).imag],ratio_neg=[(Z[2]/Z[0]).real,(Z[2]/Z[0]).imag]); print(json.dumps(rec),flush=True); out.append(rec)
json.dump(out,open('/workspace/bgs-lineN/N7/logs/c_patZ.json','w'),indent=1)
