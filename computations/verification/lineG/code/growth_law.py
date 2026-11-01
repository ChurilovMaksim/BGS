"""Law values |Z(nu_rho)|^2 for primaries at m=9..29 (beyond class-sum reach), growth-rate estimates."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import math, json, time
from law import *
cfg={(2,8):(10,2.6,50),(-2,8):(10,2.6,50),(2,16):(10,2.6,50),(-2,16):(10,2.6,50),(2,4):(6,1.5,40),(-2,4):(6,1.5,40)}
out=[]
for (a,b),(L,rho,K) in cfg.items():
    gh=kick_ghat('k1',2.0,L); prev=None
    for m in range(9,31,2):
        h=mdata(m)['h']
        nu=next(nu for nu in range(1,2*h,2) if (b*nu-a)%(2*h)==0 and math.gcd(nu,2*h)==1) if b>=4 and h<10**7 else None
        if nu is None:
            # solve b nu ≡ a mod 2h directly: nu = (a/2)*(b/2)^{-1} mod h, then odd lift
            hh=h; nu=((a//2)*pow(b//2,-1,hh))%hh
            if nu%2==0: nu+=hh
            assert (b*nu-a)%(2*h)==0
        z2=abs(Z_law(m,nu,gh,K=K,rho=rho,ab=(a,b)))**2
        r=(z2/prev)**0.25 if prev else None; prev=z2
        rec=dict(a=a,b=b,m=m,Z2=z2,r=r,F_share_over_2m=z2/(totient_h:=None) if False else None)
        print(json.dumps(dict(a=a,b=b,m=m,Z2=z2,r_est=r)),flush=True); out.append(dict(a=a,b=b,m=m,Z2=z2,r_est=r))
json.dump(out,open('../logs/growth_law.json','w'))
