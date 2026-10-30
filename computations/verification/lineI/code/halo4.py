"""Generalized-dilation (halo) law test: for delta = nu - nu_rho, shortest (c,d') with d' delta ≡ c (mod 2h).
Dilations are c=0. Test y = (|Z|^2-RMT) d'^2/|Z_rho|^2 as a function of c (independent of d', m?)."""
import sys, numpy as np, json
from base import get, reduce_vec, PSTAR
out={}
for spec in sys.argv[1:]:
    k,m=spec.split(':'); m=int(m); D=get(k,m); Z=D['Z']; nu=D['nu']; RMT=float(D['RMT']); phi=len(Z); h=int(D['h'])
    for (A,B) in PSTAR[k][:2]:
        p=np.nonzero((B*nu-A)%(2*h)==0)[0][0]; Z0=Z[p]; nu0=nu[p]
        dl=(nu-nu0)%(2*h); c,dp,_,_=reduce_vec(dl,2*h)
        sel=(dp>0)&~D['res']
        y=(Z-RMT)*dp.astype(float)**2/Z0
        print(f'== {k} m={m} rho=({A},{B}) |Z_rho|^2={Z0:.4g}')
        rows={}
        for cc in range(-12,13):
            for lo,hi in [(8,64),(64,512),(512,4096),(4096,10**9)]:
                s=sel&(c==cc)&(dp>=lo)&(dp<hi)
                if s.sum()>=3: rows[(cc,lo)]=(int(s.sum()),float(np.mean(y[s])),float(np.median(y[s])))
        for cc in range(-12,13):
            line=f'  c={cc:+3d}: '+' '.join(f"d'[{lo},..):n={rows[(cc,lo)][0]:5d} mean y={rows[(cc,lo)][1]:9.4f}" for lo in [8,64,512,4096] if (cc,lo) in rows)
            print(line)
        out[f'{spec}:{A},{B}']={f'{a_},{b_}':v for (a_,b_),v in rows.items()}
json.dump(out,open('../logs/halo4.json','w'))
