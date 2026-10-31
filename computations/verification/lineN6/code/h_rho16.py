"""N6 [N]: growth of Z_rho for rho=(+-2,16) vs (+-2,8), and the sector-1/2 family ratio for (2,16) at q=h_p."""
import sys, json, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import *
src=open('/workspace/bgs-lineN/N5/code/b_family.py').read().split("P=[int(t)")[0]; exec(src)
out=[]
for p in [5,7,11,19]:
    m=3*p; d=mdata(m); h=d['h']; M=2*h; q=hp(p); pw=lam_pows(m,q)
    nu16=next(x for x in [(pow(8,-1,h)+k*h)%M for k in (0,1)] if x%2==1); assert (16*nu16-2)%M==0
    h8,nu8=nu_rho(m,1)
    g=gen(q); i4=pow(4,-1,q); c=g
    for j in range(2*p):
        if ok(q,c): break
        if ok(q,(-c[0],-c[1])): c=(-c[0],-c[1]); break
        c=mul(c,(1,1))
    fam=taus_of((((q+c[0])*i4)%q,(c[1]*i4)%q),pw,q)
    r={}
    for lab,nu in [('8',nu8),('16',nu16)]:
        tw=TW(m,nu,L=8,K=16); Z=Zbatch(tw,[[0.0]*m,fam]); r[lab]=dict(absZ=abs(Z[0]),root=abs(Z[0])**(1/m),fam_ratio=[(Z[1]/Z[0]).real,(Z[1]/Z[0]).imag])
    rec=dict(p=p,m=m,**r); print(json.dumps(rec),flush=True); out.append(rec)
json.dump(out,open('logs/h_rho16.json','w'),indent=1)
