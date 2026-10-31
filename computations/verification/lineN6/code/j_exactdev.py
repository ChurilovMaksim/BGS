"""N6 (2) [N]: EXACT level-d deviation for prime d = h_p from all d^2 twisted sums (orbit-reduced), via the proved G3 member formula
  Z_t = (G_d(t)/d^2) sum_beta e(tbar Nm beta/d) Zhat(beta),  members nu = nu_rho + 2hj/d (j != 0, nu unit), t = j y' mod d.
Reports Dev_d, Lin_d (linear part), the isotropic linear part 2(d-2)/d^2 |Z|^2 Re X, the frozen main term (d-2)|Z_rho|^2/d^2, and
the positivity check Dev >= Lin.  usage: j_exactdev.py p [sg]"""
import sys, json, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import *
p=int(sys.argv[1]); sg=int(sys.argv[2]) if len(sys.argv)>2 else 1
def hp(p):
    x,y=1,1
    for _ in range(p-1): x,y=x+2*y,x+y
    return x
d=hp(p); m=3*p; md=mdata(m); h=md['h']; yp=md['yp']
h_,nu0=nu_rho(m,sg); tw=TW(m,nu0,L=8,K=16); pw=lam_pows(m,d)
bx,by=np.meshgrid(np.arange(d),np.arange(d),indexing='ij'); key=(bx*d+by).ravel()
best=key.copy(); cx,cy=bx.ravel().copy(),by.ravel().copy()
for i in range(p):
    for (sx,sy) in [(1,1),(-1,-1),(1,-1),(-1,1)]:
        best=np.minimum(best,((sx*cx)%d)*d+((sy*cy)%d))
    cx,cy=(3*cx+4*cy)%d,(2*cx+3*cy)%d
reps,inv=np.unique(best,return_inverse=True)
T=np.array([taus_of((int(r//d),int(r%d)),pw,d) for r in reps]); Zr=np.zeros(len(reps),complex)
for i in range(0,len(reps),32): Zr[i:i+32]=Zbatch(tw,T[i:i+32])
Zh=Zr[inv]; Z0=Zh[0]
Nm=((bx.ravel()**2-2*by.ravel()**2)%d)
A=np.zeros(d,complex); np.add.at(A,Nm,Zh)          # A_u
Gd=lambda t: np.sum(np.exp(-2j*np.pi*((t*Nm)%d)/d))
dev=0.0; lin=0.0; S=[]
for j in range(1,d):
    nu=nu0+2*h*j//d
    if nu%d==0: continue
    t=(j*yp)%d; tb=pow(t,-1,d); S.append(t)
    ph=np.exp(2j*np.pi*((tb*np.arange(d))%d)/d)
    tot=(ph*A).sum(); E=tot-Z0
    Zt2=abs(tot)**2/d**2               # |G|=d
    dev+=Zt2-abs(Z0)**2/d**2; lin+=2*(np.conj(Z0)*E).real/d**2
iso=(Nm==0); iso[0]=False; X=Zh[iso].sum()/Z0
res=dict(p=p,m=m,d=d,sg=sg,nS=len(S),absZrho=abs(Z0),main=(len(S))*abs(Z0)**2/d**2,Dev=dev,Lin=lin,Dev_minus_Lin=dev-lin,
         Lin_iso=2*len(S)/d**2*abs(Z0)**2*X.real,X=[X.real,X.imag],Dev_over_main=dev/(len(S)*abs(Z0)**2/d**2),
         Lin_over_main=lin/(len(S)*abs(Z0)**2/d**2),twoReX=2*X.real,twoReX_plus_absX2=2*X.real+abs(X)**2,norbits=len(reps))
print(json.dumps(res)); json.dump(res,open(f'logs/j_exactdev_p{p}_s{sg}.json','w'),indent=1)
