import math, json, time, numpy as np
from law import *
from step1b import Z2all, load
gh=kick_ghat('k1',2.0,6)
out=[]
# validate L6 config at m=15 against class sums first, then m=17
for m in [15,17]:
    h=mdata(m)['h']
    Z=dict(Z2all(load('k1',m),m)) if m==15 else None
    for a,b in [(2,4),(-2,4),(6,16),(-6,16)]:
        nu=next(nu for nu in range(1,2*h,2) if (b*nu-a)%(2*h)==0 and math.gcd(nu,2*h)==1)
        z=Z_law(m,nu,gh,K=40,rho=1.5,ab=(a,b))
        r=dict(m=m,a=a,b=b,nu=nu,Z2=abs(z)**2,cls=(Z[nu] if Z else None)); print(json.dumps(r),flush=True); out.append(r)
json.dump(out,open('../logs/predict17_law2.json','w'))
