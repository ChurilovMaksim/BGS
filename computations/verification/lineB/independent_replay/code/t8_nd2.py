"""Independent ND^(2) check (pair sums of orbit actions) for m=3,5 at 60 digits."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import numpy as np, math, sys, mpmath as mp
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__))); from core import hm, CK
mp.mp.dps=60
def f(t):
    return sum(2*(mp.mpf(a.numerator)/a.denominator*mp.cos(2*mp.pi*k*t) - mp.mpf(b.numerator)/b.denominator*mp.sin(2*mp.pi*k*t)) for k,(a,b) in CK.items())
for m in [3,5]:
    h=math.isqrt(hm(m))//2; reps={}
    for x0 in range(h):
        for x1 in range(h):
            s=[x0,x1]
            for j in range(2,m): s.append((6*s[-1]-s[-2])%h)
            imgs=[tuple(np.roll(s,g)) for g in range(m)]+[tuple(np.roll(s[::-1],g)) for g in range(m)]
            reps.setdefault(min(imgs),s)
    S=[sum(f(mp.mpf(1)/2+mp.mpf(x)/h) for x in s) for s in reps.values()]
    n=len(S); vals1=sorted(S); gap1=min(vals1[i+1]-vals1[i] for i in range(n-1))
    P=sorted((S[i]+S[j],i,j) for i in range(n) for j in range(i,n))
    gaps=[P[i+1][0]-P[i][0] for i in range(len(P)-1)]
    print(f'm={m}: orbits={n} min gap of single actions={mp.nstr(gap1,5)}  #pair sums={len(P)} min gap of pair sums={mp.nstr(min(gaps),5)} (#gaps<1e-40: {sum(1 for g in gaps if g<1e-40)})')
