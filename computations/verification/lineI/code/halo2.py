"""Halo structure: within |theta|~1/2 window, split by b mod 8 and by (a,b) congruence; and theta profile at finer resolution."""
import sys, numpy as np
from base import get
for spec in sys.argv[1:]:
    k,m=spec.split(':'); m=int(m); D=get(k,m); Z=D['Z']; RMT=float(D['RMT']); nr=~D['res']&~D['dil']; phi=len(Z); h=int(D['h'])
    a=D['a']; b=D['b']; th=2*a/np.maximum(b,1); x=Z/RMT; l=np.hypot(a,b)
    win=nr&(np.abs(np.abs(th)-0.5)<0.1)&(l>32)
    print(f'== {k} m={m}: halo window n={win.sum()} mean x={x[win].mean():.3f}')
    for r in range(8):
        s=win&(b%8==r)
        if s.sum(): print(f'   b≡{r} mod 8: n={s.sum():7d} x={x[s].mean():.3f}')
    # dependence on distance |4a - sgn b|: e=b-4|a| (b = 4|a| + e)
    e=b-4*np.abs(a)
    for lo,hi in [(-1,2),(2,5),(5,10),(10,20),(20,50),(50,200),(200,10**9)]:
        s=nr&(np.abs(e)>=lo)&(np.abs(e)<hi)&(l>32)
        if s.sum()>10: print(f'   |b-4|a||in[{lo},{hi}): n={s.sum():7d} x={x[s].mean():.3f}  mean |th|-.5={np.mean(np.abs(th[s])-0.5):+.4f}')
