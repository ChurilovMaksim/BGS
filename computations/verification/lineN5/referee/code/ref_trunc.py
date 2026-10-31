"""Referee [N]: truncation robustness of the family ratio Zhat_fam/Z0 and of Zhat(1/2..)/Z0 at p = 19 (twlaw L, K varied)."""
import sys, json, math
sys.path.insert(0,'/workspace/bgs-lineL/L2/code'); sys.path.insert(0,'/workspace/bgs-lineI/code')
from law import mdata
from twlaw import TW, lam_pows, taus_of
p=19; m=3*p; q=9369319; d=mdata(m); h=d['h']; M=2*h
x0=(pow(4,-1,M//2))%(M//2); nu0=min(x for x in (x0,x0+M//2) if x%2==1)
tf=taus_of((2342678,4684065),lam_pows(m,q),q); out=[]
for L,K in [(6,24),(8,32),(10,40),(12,48)]:
    tw=TW(m,nu0,L=L,K=K); Z0=tw.Z([0.0]*m); r=tw.Z(tf)/Z0; hh=tw.Z([0.5]*m)/Z0
    out.append(dict(L=L,K=K,absZ0=abs(Z0),ratio_abs=abs(r),ratio_arg=math.atan2(r.imag,r.real),half=[hh.real,hh.imag])); print(out[-1],flush=True)
json.dump(out,open('logs/ref_trunc_p19.json','w'),indent=1)
