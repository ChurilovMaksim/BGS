"""Per-denominator (Kloosterman-type numerator average) bulk means: for each b, mean of |Z|^2/RMT over nonresonant nu with shortest vector (a,b)."""
import sys, numpy as np
from base import get
for spec in sys.argv[1:]:
    k,m=spec.split(':'); m=int(m); D=get(k,m); Z=D['Z']; RMT=float(D['RMT']); nr=~D['res']&~D['dil']
    b=np.abs(D['b']); x=Z/RMT
    B=np.unique(b[nr]); means=[]; cnt=[]
    for bb in B:
        s=nr&(b==bb)
        if s.sum()>=20: means.append(x[s].mean()); cnt.append(s.sum())
    means=np.array(means); cnt=np.array(cnt); Bs=B[[ (nr&(b==bb)).sum()>=20 for bb in B]]
    ex2=(x[nr]**2).mean(); noise=np.sqrt((ex2-x[nr].mean()**2)/cnt)
    z=(means-x[nr].mean())/noise
    print(f'{k} m={m}: #b={len(means)} overall nonres mean={x[nr].mean():.4f}; per-b z-score: rms={np.sqrt((z**2).mean()):.2f} (1 if per-b means are pure noise), max|z|={np.abs(z).max():.1f}')
    for lo,hi in [(1,16),(16,64),(64,256),(256,1024),(1024,4096)]:
        s=(Bs>=lo)&(Bs<hi)
        if s.any(): print(f'   b in [{lo},{hi}): n_b={s.sum():5d} weighted mean={np.average(means[s],weights=cnt[s]):.4f} rms z={np.sqrt((z[s]**2).mean()):.2f}')
