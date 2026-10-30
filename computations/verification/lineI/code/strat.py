"""Height-stratified decomposition of W'_m (TRACE-206 definition) over dyadic shortest-vector length bins."""
import sys, numpy as np, json
from base import get
out={}
for spec in sys.argv[1:]:
    k,m=spec.split(':'); m=int(m); D=get(k,m); Z=D['Z']; phi=len(Z); h=int(D['h']); RMT=float(D['RMT'])
    l=np.sqrt(D['a'].astype(float)**2+D['b'].astype(float)**2); nr=~D['res']
    F=Z.mean(); Res=(Z[D['res']]-RMT).sum()/phi; W=(F-RMT-Res)
    print(f"== {k} m={m} h={h} W'/m={W/m:+.4f}  sqrt(2h)={np.sqrt(2*h):.0f}")
    rows=[]; kmax=int(np.log2(l.max()))+1; cum=0
    for kk in range(0,kmax+1):
        sel=nr&(l>=2**kk)&(l<2**(kk+1))
        if not sel.any(): continue
        c=(Z[sel]-RMT).sum()/phi/m; cum+=c
        rows.append(dict(k=kk,n=int(sel.sum()),frac=float(sel.mean()),mean_x=float(Z[sel].mean()/RMT),contrib=float(c),cum=float(cum),
                         Ex2=float(((Z[sel]/RMT)**2).mean()),maxx=float(Z[sel].max()/RMT)))
        r=rows[-1]; print(f"  l in [2^{kk},2^{kk+1}): n={r['n']:8d} frac={r['frac']:.2e} mean|Z|^2/RMT={r['mean_x']:8.4f} contrib W'/m={c:+.4f} cum={cum:+.4f} E[x^2]={r['Ex2']:9.2f} max x={r['maxx']:8.1f}")
    out[spec]=rows
json.dump(out,open('../logs/strat.json','w'),indent=1)
