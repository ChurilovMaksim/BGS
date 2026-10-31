"""N2 (D) [N]: inherited level c=h_p (prime cases p=5,7: h=41,239), true TRACE-206 twisted sums via L2 twlaw
(Line G/I transfer law, L=8, K=32 as in L2 full_level.py).  Splits the level-h_p mass into unit / isotropic parts:
  U = (1/q^2) sum_{N(beta)!=0} |Zhat|   (the 'pressure' quantity, weight <= 2/q^2 each)
  I = (1/q)   sum_{iso beta != 0} |Zhat| (weight (q-2)/q^2 each)
and their m-th roots vs the target 1.28359.  Saves Zhat array.  usage: d_level_split.py m q [sign]"""
import sys, json, time, numpy as np; sys.path.insert(0,'/workspace/bgs-lineL/L2/code')
from twlaw import *
m=int(sys.argv[1]); q=int(sys.argv[2]); sg=int(sys.argv[3]) if len(sys.argv)>3 else 1
d=mdata(m); h=d['h']; M=2*h; assert h%q==0
x0=(sg*pow(4,-1,M//2))%(M//2); nu0=min(x for x in (x0,x0+M//2) if x%2==1); assert (8*nu0-2*sg)%M==0
tw=TW(m,nu0,L=8,K=32); pw=lam_pows(m,q)
t0=time.time(); Zh=np.zeros((q,q),complex); seen=np.zeros((q,q),bool); nrun=0
for bx in range(q):
    for by in range(q):
        if seen[bx,by]: continue
        z=tw.Z(taus_of((bx,by),pw,q)); nrun+=1; x=(bx,by)
        while not seen[x]:
            seen[x]=True; Zh[x]=z; x=((3*x[0]+4*x[1])%q,(2*x[0]+3*x[1])%q)
np.save(f'logs/d_Zh_m{m}_q{q}_s{sg}.npy',Zh)
g=np.arange(q); BX,BY=np.meshgrid(g,g,indexing='ij'); N=(BX*BX-2*BY*BY)%q
Zn=np.abs(Zh); unit=(N!=0); iso=(N==0); iso[0,0]=False
U=Zn[unit].sum()/q**2; I=Zn[iso].sum()/q; T=1.28359
res=dict(res=f'({2*sg},8)',m=m,q=q,runs=nrun,absZ=float(Zn[0,0]),U=float(U),U_rate=float(U**(1/m)),I=float(I),I_rate=float(I**(1/m)),
 target=T,max_unit_rate=float(Zn[unit].max()**(1/m)),max_iso_rate=float(Zn[iso].max()**(1/m)),
 frac_U_from_top1pct=float(np.sort(Zn[unit])[::-1][:max(1,unit.sum()//100)].sum()/Zn[unit].sum()),
 Z0_over_q2_rate=float((Zn[0,0]/q**2)**(1/m)),sec=round(time.time()-t0,1))
print(json.dumps(res),flush=True)
