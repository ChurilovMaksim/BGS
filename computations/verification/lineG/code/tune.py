import sys, math, json, numpy as np, time
from law import *
from step1b import Z2all, load
PR=[(-2,8),(2,8),(-2,16),(2,16),(-2,4),(2,4),(-6,16),(6,16)]
def nu_of(m,a,b):
    h=mdata(m)['h']
    for nu in range(1,2*h,2):
        if (b*nu-a)%(2*h)==0 and math.gcd(nu,2*h)==1: return nu
cfgs=[(8,1.9,40),(8,2.2,50),(10,2.6,50),(6,1.5,40)]
for m in [13,15]:
    T=load('k1',m); Z=dict(Z2all(T,m))
    for a,b in PR:
        nu=nu_of(m,a,b); s=f'm={m} ({a},{b}) class={Z[nu]:.7g}'
        for L,rho,K in cfgs:
            gh=kick_ghat('k1',2.0,L)
            try: zl=abs(Z_law(m,nu,gh,K=K,rho=rho,ab=(a,b)))**2
            except Exception as e: zl=float('nan')
            s+=f' | L{L} r{rho} K{K}: {zl:.7g} ({abs(zl-Z[nu])/Z[nu]:.1e})'
        print(s,flush=True)
