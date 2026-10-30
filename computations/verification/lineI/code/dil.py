"""Dilation members of P* primaries: actual coset values vs Gauss main term |Z_rho|^2/d^2 (frozen TRACE-206 uses the main term)."""
import sys, numpy as np, json
from base import get, PSTAR
from step1c import divisors
from step1b import factor
out=[]
for spec in sys.argv[1:]:
    k,m=spec.split(':'); m=int(m); D=get(k,m); Z=D['Z']; nu=D['nu']; h=int(D['h']); phi=len(Z); RMT=float(D['RMT'])
    print(f'== {k} m={m} h={h}={factor(h)}')
    ds=[d for d in divisors(h) if d>1 and d*d<=h]
    tot_dev=0; tot_main=0
    for (A,B) in PSTAR[k]:
        p=np.nonzero((B*nu-A)%(2*h)==0)[0]
        if len(p)==0: print('  no primary',A,B); continue
        Z0=Z[p[0]]; used=np.zeros(phi,bool); used[p[0]]=True
        for d in ds:
            M=2*h//d; mem=((B*nu-A)%M==0)&~used; used|=mem
            n=mem.sum()
            if n==0: continue
            main=Z0/d/d; act=Z[mem].mean(); incl=main>=4*m
            dev=(act-main)*n/phi/m
            if incl: tot_dev+=dev; tot_main+=(main-RMT)*n/phi/m
            print(f'  rho=({A},{B}) d={d:7d} n={n:5d} main={main:11.4g} act_mean={act:11.4g} rel={act/main-1:+.4f} min/main={Z[mem].min()/main:.3f} max/main={Z[mem].max()/main:.3f} incl={incl} dev contrib W/m={dev:+.4f}')
            out.append(dict(kick=k,m=m,rho=[A,B],d=d,n=int(n),main=float(main),act=float(act),incl=bool(incl),dev=float(dev)))
    print(f'  total (included levels): main-term part {tot_main:+.4f}, deviation act-main {tot_dev:+.4f} (units of W/m)')
json.dump(out,open('../logs/dil.json','w'),indent=1)
