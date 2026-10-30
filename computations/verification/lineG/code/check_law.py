import numpy as np, math, random, sys
from law import *
random.seed(1)
ok=0; bad=0
for m,L in [(5,2),(5,3),(7,2)]:
    d=mdata(m); h=d['h']
    gh={n:complex(random.gauss(0,1),random.gauss(0,1))*0.5**abs(n) for n in range(-L,L+1)}
    units=[nu for nu in range(1,2*h,2) if math.gcd(nu,2*h)==1]
    for nu in random.sample(units,min(8,len(units))):
        zb=Z_brute(m,nu,gh)
        for ab in ratrec(nu,2*h):
            if ab[1]<=0: continue
            zl=Z_law(m,nu,gh,K=60,ab=ab)
            err=abs(zl-zb)/max(1,abs(zb))
            print(m,L,nu,ab,abs(zb),err); ok+= err<1e-9; bad+= err>=1e-9
print('OK',ok,'BAD',bad)
