"""N6 (2) [N]: full isotropic aliased sum at level d = h_p (squarefree), m = 3p, rho = (sg 2, 8), true TRACE-206 law (L2 TW, batched).
X_d = sum_{beta != 0, Nm beta == 0 mod d} Zhat(beta) / Z_rho  (exact enumeration over orbits of <lam, -1, conj>).
Also per-orbit slow-step counts and the 16D=1 family share.  usage: f_iso.py p K [sg]"""
import sys, json, time, numpy as np
from sympy import factorint, sqrt_mod
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import *
p=int(sys.argv[1]); K=int(sys.argv[2]); sg=int(sys.argv[3]) if len(sys.argv)>3 else 1
m=3*p
def hp(p):
    x,y=1,1
    for _ in range(p-1): x,y=x+2*y,x+y
    return x
d=hp(p); fac=list(factorint(d)); assert all(e==1 for e in factorint(d).values())
# iso points mod each prime r: lines x = +-w y
comps=[]
for r in fac:
    w=sqrt_mod(2,r); pts=[(0,0)]
    for y in range(1,r):
        pts.append(((w*y)%r,y)); pts.append(((-w*y)%r,y))
    comps.append((r,np.array(pts,dtype=object)))
# CRT combine
X=np.array([0],dtype=object); Y=np.array([0],dtype=object); mod=1
for r,pts in comps:
    e1=(r*pow(r,-1,mod))%(mod*r) if mod>1 else 0   # ==1 mod mod? build idempotents
    # beta = a mod mod, b mod r
    u=mod*pow(mod,-1,r)   # ==0 mod mod, ==1 mod r
    v=r*pow(r,-1,mod) if mod>1 else 0
    nx=[];ny=[]
    for (bx,by) in pts:
        nx.append((X*v+bx*u)%(mod*r)); ny.append((Y*v+by*u)%(mod*r))
    X=np.concatenate(nx); Y=np.concatenate(ny); mod*=r
assert mod==d
X=X.astype(np.int64); Y=Y.astype(np.int64)
nz=(X!=0)|(Y!=0); X=X[nz]; Y=Y[nz]; N=len(X)
assert np.all(((X.astype(object)**2-2*Y.astype(object)**2)%d)==0)
key=X*d+Y
# canonical rep over group <lam,-1,conj>
best=key.copy(); cx,cy=X.copy(),Y.copy()
for i in range(p):
    for (sx,sy) in [(1,1),(-1,-1),(1,-1),(-1,1)]:
        k=((sx*cx)%d)*d+((sy*cy)%d); best=np.minimum(best,k)
    cx,cy=(3*cx+4*cy)%d,(2*cx+3*cy)%d
reps,cnt=np.unique(best,return_counts=True)
assert cnt.sum()==N
h,nu0=nu_rho(m,sg); tw=TW(m,nu0,L=8,K=K); pw=lam_pows(m,d)
z0=Zbatch(tw,[[0.0]*m])[0]
T=np.array([taus_of((int(r//d),int(r%d)),pw,d) for r in reps])
t0=time.time(); Z=np.zeros(len(reps),complex); B=32
for i in range(0,len(reps),B): Z[i:i+B]=Zbatch(tw,T[i:i+B])
dist=np.minimum(np.abs(((T+0.5)%1)-0.5),np.abs((T%1)-0.5))   # distance to {0,1/2}
slow=(dist<0.05).sum(1)
ratio=Z/z0; Xd=(cnt*ratio).sum()
order=np.argsort(-np.abs(cnt*ratio))
top=[dict(rep=[int(reps[j]//d),int(reps[j]%d)],size=int(cnt[j]),ratio=[ratio[j].real,ratio[j].imag],abs=abs(ratio[j]),slow=int(slow[j]),
          near0=int((np.abs(((T[j]+0.5)%1)-0.5)<0.05).sum()),nearhalf=int((np.abs((T[j]%1)-0.5)<0.05).sum())) for j in order[:25]]
# cumulative by slow-count threshold
cum={int(s):complex((cnt*ratio)[slow>=s].sum()) for s in sorted(set(slow.tolist()))}
res=dict(p=p,m=m,d=d,fac=fac,K=K,sg=sg,Npts=int(N),norbits=int(len(reps)),Zrho=[z0.real,z0.imag],X=[Xd.real,Xd.imag],absX=abs(Xd),
         twoReX_plus_absX2=float(2*Xd.real+abs(Xd)**2),sec=round(time.time()-t0,1),
         cum_by_slow={k:[v.real,v.imag] for k,v in cum.items()},top=top)
json.dump(res,open(f'logs/f_iso_p{p}_K{K}_s{sg}.json','w'),indent=1)
print(json.dumps({k:res[k] for k in ['p','d','norbits','X','absX','twoReX_plus_absX2','sec']}))
for t in top[:10]: print(t)
