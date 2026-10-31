"""Referee [N]: recheck of N6's 'near-0 family' (p=19, s=1656277 on the line (w,1), w = sqrt_mod(2,q)) and the 16D=1 family point s=1087
with the twlaw law at (L,K) = (8,32) and (10,40); also its twist profile (distance to 0 and to 1/2)."""
import sys, json, math, numpy as np
sys.path.insert(0,'/workspace/bgs-lineL/L2/code'); sys.path.insert(0,'/workspace/bgs-lineI/code')
from law import mdata
from twlaw import TW, lam_pows, taus_of
from sympy import sqrt_mod
p=19; m=57; q=9369319; w=int(sqrt_mod(2,q)); d=mdata(m); h=d['h']; M=2*h
x0=(pow(4,-1,M//2))%(M//2); nu0=min(x for x in (x0,x0+M//2) if x%2==1)
pw=lam_pows(m,q); out={}
for L,K in [(8,32),(10,40)]:
    tw=TW(m,nu0,L=L,K=K); Z0=tw.Z([0.0]*m)
    for s in (1087,1656277):
        t=taus_of(((s*w)%q,s),pw,q); r=tw.Z(t)/Z0
        out[f'{s}_L{L}']=[r.real,r.imag]
        if L==8: out[f'{s}_profile']=''.join('0' if min(x,1-x)<0.05 else ('h' if abs(x-0.5)<0.05 else '.') for x in t[:p])
print(json.dumps(out,indent=1)); json.dump(out,open('logs/ref_near0.json','w'),indent=1)
