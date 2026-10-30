import sys, math, json, numpy as np, time
from law import *
from step1b import Z2all, load
P=[(-2,8),(2,8),(-2,16),(2,16),(-2,4),(2,4),(-6,16),(6,16),(-2,24),(2,24),(-6,8),(6,8),(-1,1),(1,1),(-2,12),(2,12),(-10,16),(10,16)]
gh=kick_ghat('k1',2.0,12)
out=[]
for m in [9,11,13,15]:
    T=load('k1',m); h=mdata(m)['h']; Z=dict(Z2all(T,m))
    for a,b in P:
        # find nu with b nu ≡ a mod 2h, nu odd unit
        cands=[nu for nu in range(1,2*h,2) if (b*nu-a)%(2*h)==0 and math.gcd(nu,2*h)==1] if b<=24 else []
        if not cands: continue
        nu=cands[0]; t=time.time()
        zl=Z_law(m,nu,gh,K=40,ab=(a,b))
        rel=abs(abs(zl)**2-Z[nu])/Z[nu]
        print(f'm={m} rho=({a},{b}) nu={nu} class|Z|^2={Z[nu]:.6g} law={abs(zl)**2:.6g} rel={rel:.1e} ({time.time()-t:.1f}s)',flush=True)
        out.append(dict(m=m,a=a,b=b,nu=nu,cls=Z[nu],law=abs(zl)**2))
json.dump(out,open('../logs/law_vs_class.json','w'))
