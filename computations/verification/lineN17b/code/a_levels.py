"""N17b (2) [N]: list the frozen TRACE-206 levels d | h_m (m=3p), 1<d<=sqrt(h_m), included iff |Z_rho|^2/d^2 >= 4m (Z_rho from twb, [N]),
classified as: divisor of h_p ('hp-div'), d = h_p ('hp'), multiple of h_p ('inherited'), divisor of K_p=h_m/h_p ('K'), mixed product ('mixed')."""
import sys, json, math
from sympy import factorint, divisors
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import *
out=[]
for p in [3,5,7,11,13]:
    m=3*p; h,nu0=nu_rho(m,1)
    x,y=1,1
    for _ in range(p-1): x,y=x+2*y,x+y
    hp=x; K=h//hp; assert h%hp==0
    tw=TW(m,nu0,L=8,K=16); Z0=abs(Zbatch(tw,[[0.0]*m])[0])
    levs=[]
    for d in divisors(h):
        if d<=1 or d*d>h: continue
        inc=Z0**2/d**2>=4*m
        if d==hp: c='hp'
        elif hp%d==0: c='hp-div'
        elif d%hp==0: c='inherited'
        elif K%d==0: c='K'
        else: c='mixed'
        levs.append(dict(d=int(d),cls=c,included=bool(inc),fac={str(k):v for k,v in factorint(d).items()}))
    r=dict(p=p,m=m,h=str(h),h_fac={str(k):v for k,v in factorint(h).items()},hp=hp,K=str(K),Zrho=Z0,sqrt_h=math.isqrt(h),levels=levs)
    out.append(r); print(p,m,'h=',h,factorint(h),'|Z|=%.3e'%Z0, [(l['d'],l['cls'],l['included']) for l in levs],flush=True)
json.dump(out,open('logs/a_levels.json','w'),indent=1)
