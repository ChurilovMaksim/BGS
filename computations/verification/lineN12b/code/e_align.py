"""N12b [N]: why coarse cones fail — alignment of the block output u_L(P_3(y)) with the past-iterated cone direction u(y') at
y' = F^3(y) + delta*e (e = stable or unstable unit direction of F), delta = 0, 1e-1..1e-6.  Required: sin <= (g - sigma2)/sigma1 at that cell
(g = (T'/MU)^3 = 0.414).  usage: e_align.py NS"""
import sys, json, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N12b/code'); from common import *
NSAMP=int(sys.argv[1]); TH=0.125; J=10; lam=3+2*np.sqrt(2)
es=np.array([1.0,1/lam]); es/=np.linalg.norm(es); eu=np.array([1.0,lam]); eu/=np.linalg.norm(eu)   # F(y0,y1)=(y1,6y1-y0): eigvecs (1,lam),(1,1/lam)
def udir(y):
    hist=[np.array(y)]; z=np.array(y)
    for i in range(J): z=np.array([(6*z[0]-z[1])%1,z[0]]); hist.append(z)
    v=np.ones(495,complex)
    for i in range(J,0,-1): v=M(hist[i][0])@v; v/=np.linalg.norm(v)
    return v
rng=np.random.default_rng(3); rows=[]; DL=[0,1e-1,1e-2,1e-3,1e-4,1e-5,1e-6]
while len(rows)<NSAMP:
    y=rng.random(2); z=y.copy(); ok=True
    for i in range(4):
        if inbox(z,TH): ok=False;break
        z=F(z)
    if not ok: continue
    ts=[y[0],y[1],(6*y[1]-y[0])%1]; P=M(ts[2])@M(ts[1])@M(ts[0]); Us,sv,Vh=np.linalg.svd(P); uL=Us[:,0]
    y3=F(F(F(y))); row=dict(s1=sv[0],s2=sv[1],need=(0.414-sv[1])/sv[0],stable={},unstable={})
    for d in DL:
        for nm,e in (('stable',es),('unstable',eu)):
            u=udir((y3+d*e)%1); row[nm][d]=float(np.sqrt(max(0,1-abs(u.conj()@uL)**2)))
    rows.append(row); print(len(rows),round(row['need'],3),{d:round(row['stable'][d],3) for d in DL},{d:round(row['unstable'][d],3) for d in DL[:4]},flush=True)
summ=dict(med_need=float(np.median([r['need'] for r in rows])),frac_need_neg=float(np.mean([r['need']<0 for r in rows])),
  med_sin_stable={d:float(np.median([r['stable'][d] for r in rows])) for d in DL},max_sin_stable={d:float(max(r['stable'][d] for r in rows)) for d in DL},
  med_sin_unstable={d:float(np.median([r['unstable'][d] for r in rows])) for d in DL})
print(json.dumps(summ,indent=1)); json.dump(dict(summary=summ,rows=rows),open('logs/e_align.json','w'),indent=1)
