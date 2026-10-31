"""Float single-disc spectral radii of 3-step twisted products restricted to the reachable states (orbit of state 0).
Usage: twrad2.py K rho Lk"""
import numpy as np, json, sys, time
import sys; sys.path.insert(0,'/workspace/bgs-lineI/code')
from law import kick_ghat
from twist import build
K=int(sys.argv[1]); RHO=float(sys.argv[2]); Lk=int(sys.argv[3])
gh=kick_ghat('k1',2.0,Lk); d=7
lam=[];x,y=1,0
for i in range(3): lam.append((x,y)); x,y=(3*x+4*y)%d,(2*x+3*y)%d
def taus(bx,by): return [((2*(bx*lx+2*by*ly))%d)/d for (lx,ly) in lam]
seen=set(); classes=[]
for bx in range(d):
    for by in range(d):
        if bx==0 and by==0: continue
        t=tuple(taus(bx,by)); key=min(t[i:]+t[:i] for i in range(3))
        if key in seen: continue
        seen.add(key); classes.append(((bx,by),t))
def restricted(m,a,b):
    parts,nu,S=build(m,a,b,gh,RHO,K)
    tg={n:(P!=0).argmax(axis=0) for n,(Mn,P) in parts.items()}
    orb={0}; fr=[0]
    while fr:
        s=fr.pop()
        for n in tg:
            t=int(tg[n][s])
            if t not in orb: orb.add(t); fr.append(t)
    idx=sorted(orb)
    sub={n:(Mn,P[np.ix_(idx,idx)]) for n,(Mn,P) in parts.items()}
    for n,(Mn,P) in parts.items(): assert np.allclose(abs(P[np.ix_(idx,idx)]).sum(),abs(P[:,idx]).sum())
    return sub,idx
def Lop(sub,tau): return sum(np.exp(2j*np.pi*n*tau)*np.kron(Mn,P) for n,(Mn,P) in sub.items())
out={}
for m in (9,15):
  for (a,b) in ((2,16),(-2,16),(2,8)):
    t0=time.time(); sub,idx=restricted(m,a,b)
    L0=Lop(sub,0.0); ev=np.linalg.eigvals(L0); ev=ev[np.argsort(-abs(ev))]
    rec=dict(states=len(idx),idx=idx,mu=float(abs(ev[0])),mu_top=[float(x) for x in abs(ev[:6])],tw={})
    for (bx,by),t in classes:
        Ls=[Lop(sub,tt) for tt in t]; Q=Ls[2]@Ls[1]@Ls[0]
        e=np.sort(abs(np.linalg.eigvals(Q)))[::-1]
        rec['tw'][f'{bx},{by}']=dict(taus=t,r=float(e[0]**(1/3)),r2=float(e[1]**(1/3)))
    rw=max(v['r'] for v in rec['tw'].values()); rec['rtw_max']=rw
    print(m,(a,b),'states',len(idx),'mu',round(rec['mu'],6),'3rd',round(rec['mu_top'][2],6),'rtw_max',round(rw,6),'all',sorted(round(v['r'],4) for v in rec['tw'].values()),round(time.time()-t0),'s',flush=True)
    out[f'{m},{a},{b}']=rec
    json.dump(out,open(f'/workspace/bgs-lineJ/logs/twrad16_K{K}_r{RHO}_L{Lk}.json','w'),indent=1)
