"""Bulk mean of |Z|^2/RMT by the shape of the shortest vector: ratio |a|/b (coupling |theta|=2|a|/b) and length."""
import sys, numpy as np
from base import get
for spec in sys.argv[1:]:
    k,m=spec.split(':'); m=int(m); D=get(k,m); Z=D['Z']; RMT=float(D['RMT']); nr=~D['res']&~D['dil']; phi=len(Z)
    a=np.abs(D['a']).astype(float); b=np.abs(D['b']).astype(float); x=Z/RMT; l=np.hypot(a,b); h=int(D['h'])
    r=a/np.maximum(b,1)
    print(f'== {k} m={m}')
    for lo,hi in [(0,0.1),(0.1,0.3),(0.3,1),(1,3),(3,10),(10,1e9)]:
        s=nr&(r>=lo)&(r<hi)
        for L0,L1 in [(0,64),(64,np.sqrt(h)),(np.sqrt(h),1e9)]:
            t=s&(l>=L0)&(l<L1)
            if t.sum()<10: continue
            print(f'  |a|/b in [{lo},{hi}) l in [{L0:.0f},{L1:.0f}): n={t.sum():8d} frac={t.mean():.2e} mean x={x[t].mean():.4f} contrib W/m={(Z[t]-RMT).sum()/phi/m:+.4f}')
