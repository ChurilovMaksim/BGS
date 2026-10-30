import math, numpy as np, json
from law import mdata
from step1b import Z2all, load
from step1c import divisors
rows=[]
for kick in ['k1','full']:
  for m in [9,11,13,15]:
    T=load(kick,m); h=mdata(m)['h']; Z=dict(Z2all(T,m))
    prim=[(2,8),(-2,8),(2,16),(-2,16)] if kick=='k1' else [(2,392),(-2,392),(2,784),(-2,784)]
    for a,b in prim:
        p=[nu for nu in Z if (b*nu-a)%(2*h)==0]
        if not p: continue
        Z0=Z[p[0]]
        for d in divisors(h):
            if d==1 or d*d>h: continue
            M=2*h//d
            # exact-level-d members: in F_d but not in F_{d'} for proper divisors d'<d of d
            mem=[nu for nu in Z if (b*nu-a)%M==0 and all((b*nu-a)%(2*h//dd)!=0 for dd in divisors(d) if dd<d)]
            if not mem: continue
            ratio=np.array([Z[n]*d*d/Z0 for n in mem])
            rows.append(dict(kick=kick,m=m,rho=[a,b],d=d,n=len(mem),mean_ratio=float(ratio.mean()),min=float(ratio.min()),max=float(ratio.max()),
                             fam_sum_over_Z0=float(sum(Z[n] for n in mem)/Z0), pred_phi_d_over_d2=None))
            print(f'{kick} m={m} rho=({a},{b}) |Z0|^2={Z0:.4g} d={d} members={len(mem)} mean(d^2|Z|^2/|Z0|^2)={ratio.mean():.4f} [{ratio.min():.3f},{ratio.max():.3f}]  sum/|Z0|^2={sum(Z[n] for n in mem)/Z0:.5f} vs (n/d^2)={len(mem)/d/d:.5f}')
json.dump(rows,open('../logs/dil_stats.json','w'))
