"""N17b (2) [N, TW law L=8 K=16 — truncated transfer law, rel. err ~2e-5 on |Z|^2 at m=15]: Dev_d(rho) = sum_{nu in M_d(rho)} (|Z_nu|^2 - |Z_rho|^2/d^2)
for rho=(+-2,8), all included levels d | h_m with d <= DMAX, members nu = nu_rho + (2h/d) j, gcd(j,d)=1, nu unit (all divisors <= sqrt h are
included levels at these m, so the frozen 'not a member of a smaller level' rule is gcd(j,d)=1). usage: c_member_dev.py m DMAX"""
import sys, json, math, time, numpy as np, warnings
warnings.filterwarnings('ignore')
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import *
from sympy import divisors, totient, factorint
m=int(sys.argv[1]); DMAX=int(sys.argv[2])
p=m//3; x,y=1,1
for _ in range(p-1): x,y=x+2*y,x+y
hp=x
res=dict(m=m,DMAX=DMAX,rows=[])
for sg in (1,-1):
    h,nu0=nu_rho(m,sg); M=2*h; phi=int(totient(M)); RMT=4*m-m*m/h
    Z0=abs(Zbatch(TW(m,nu0,L=8,K=16),np.zeros((1,m)))[0])**2
    for d in divisors(h):
        if d<=1 or d*d>h or d>DMAX: continue
        if Z0/d/d<4*m: res['rows'].append(dict(rho=[2*sg,8],d=int(d),included=False)); continue
        cls='hp' if d==hp else ('hp-div' if hp%d==0 else ('inherited' if d%hp==0 else ('K' if (h//hp)%d==0 else 'mixed')))
        t0=time.time(); S=0.0; n=0; mx=0.0
        for j in range(1,d):
            if math.gcd(j,d)!=1: continue
            nu=(nu0+(M//d)*j)%M
            if math.gcd(nu,M)!=1: continue
            z=abs(Zbatch(TW(m,nu,L=8,K=16),np.zeros((1,m)))[0])**2
            S+=z; n+=1; mx=max(mx,z)
        dev=S-n*Z0/d/d
        row=dict(rho=[2*sg,8],d=int(d),cls=cls,included=True,n_d=n,Zrho2=Z0,Dev=dev,Dev_over_phim=dev/phi/m,
                 main_over_phim=n*Z0/d/d/phi/m,Dev_rel_main=dev/(n*Z0/d/d),max_member_over_main=mx/(Z0/d/d),sec=round(time.time()-t0,1))
        res['rows'].append(row)
        print(json.dumps(row),flush=True)
    res[f'phi_{sg}']=phi
json.dump(res,open(f'logs/c_member_dev_m{m}.json','w'),indent=1)
