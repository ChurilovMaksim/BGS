"""N11b [N]: EXACT mixed-class contribution to Y at composite d = h_p (p=11: 23*353):
points beta mod d with N beta = 0 mod qi (iso part) and N beta != 0 mod qu (unit part), all of them (or a random sample, fraction f),
orbit-reduced as j_exactdev; Y_mixed = (1/n) sum kappa_d(N beta) Zhat/Z with exact S_d.  usage: d_mixed.py p qi qu [f]"""
import sys, json, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import *
p=int(sys.argv[1]); qi=int(sys.argv[2]); qu=int(sys.argv[3]); f=float(sys.argv[4]) if len(sys.argv)>4 else 1.0
def hp(p):
    x,y=1,1
    for _ in range(p-1): x,y=x+2*y,x+y
    return x
d=hp(p); assert d==qi*qu or qi==1; m=3*p; md=mdata(m); h=md['h']; yp=md['yp']
h_,nu0=nu_rho(m,1); tw=TW(m,nu0,L=8,K=16); pw=lam_pows(m,d)
S=[]
for j in range(1,d):
    nu=nu0+2*h*j//d
    if np.gcd(nu,d)!=1 or np.gcd((j*yp)%d,d)!=1: continue   # N6: t unit, nu unit
    S.append((j*yp)%d)
n=len(S)
bx,by=np.meshgrid(np.arange(d),np.arange(d),indexing='ij'); bx=bx.ravel(); by=by.ravel()
Nm=(bx*bx-2*by*by)%d
sel=((Nm%qi==0)&(Nm%qu!=0)) if qi>1 else (np.gcd(Nm,d)==1); bx,by,Nm=bx[sel],by[sel],Nm[sel]
best=bx*d+by; cx,cy=bx.copy(),by.copy()
for i in range(p):
    for (sx,sy) in [(1,1),(-1,-1),(1,-1),(-1,1)]:
        best=np.minimum(best,((sx*cx)%d)*d+((sy*cy)%d))
    cx,cy=(3*cx+4*cy)%d,(2*cx+3*cy)%d
reps,inv,cnt=np.unique(best,return_inverse=True,return_counts=True)
rng=np.random.default_rng(1); take=np.arange(len(reps)) if f>=1 else np.sort(rng.choice(len(reps),int(f*len(reps)),replace=False))
Z0=Zbatch(tw,[[0.0]*m])[0]
T=np.array([taus_of((int(reps[k]//d),int(reps[k]%d)),pw,d) for k in take]); Zr=np.zeros(len(take),complex)
for i in range(0,len(take),32): Zr[i:i+32]=Zbatch(tw,T[i:i+32])
r=Zr/Z0
u=np.arange(d); kap=np.zeros(d,complex)
for t in S: kap+=np.exp(2j*np.pi*((pow(int(t),-1,d)*u)%d)/d)
Nrep=((reps[take]//d)**2-2*(reps[take]%d)**2)%d
w=cnt[take]/f
Ym=(w*kap[Nrep]*r).sum()/n
ab=np.abs(r); order=np.argsort(-ab)[:15]
res=dict(p=p,d=d,qi=qi,qu=qu,f=f,n=n,npoints=int(sel.sum()),nreps=len(reps),nsampled=len(take),
  kappa_on_class_max=float(np.abs(kap[Nrep]).max()),Ymixed=[Ym.real,Ym.imag],absYmixed=abs(Ym),
  sum_abs_r_weighted=float((w*ab).sum()),bound_2sum_over_n=float((w*ab*np.abs(kap[Nrep])).sum()/n),max_abs_r=float(ab.max()),
  top=[dict(beta=[int(reps[take[k]]//d),int(reps[take[k]]%d)],absr=float(ab[k]),orbit=int(cnt[take[k]])) for k in order])
print(json.dumps(res)); json.dump(res,open(f'logs/d_mixed_p{p}_{qi}_{qu}.json','w'),indent=1)
