import math, json, time, numpy as np
from law import *
m=17; d=mdata(m); h=d['h']
gh=kick_ghat('k1',2.0,10)
out=[]
for a,b in [(2,8),(-2,8),(2,16),(-2,16),(2,4),(-2,4),(6,16),(-6,16)]:
    nu=next(nu for nu in range(1,2*h,2) if (b*nu-a)%(2*h)==0 and math.gcd(nu,2*h)==1)
    t=time.time(); z=Z_law(m,nu,gh,K=50,rho=2.6,ab=(a,b))
    r=dict(m=m,a=a,b=b,nu=nu,N=pow(nu,-1,h),Z2=abs(z)**2,secs=time.time()-t); print(json.dumps(r),flush=True); out.append(r)
json.dump(out,open('../logs/predict17_law.json','w'))
