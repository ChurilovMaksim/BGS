import math, numpy as np, json
from law import mdata
from step1b import Z2all, load
V=[(16,70),(-16,70),(22,96),(-22,96),(34,96),(-34,96),(10,28),(-10,28),(-3,17),(3,17),(2,12),(-2,12),(4,18),(-4,18),(172,70),(-172,70),(134,140),(-134,140),(2,8),(2,16),(2,4),(6,16)]
out={}
for kick in ['k1']:
  for m in [9,11,13,15]:
    T=load(kick,m); h=mdata(m)['h']; Z=dict(Z2all(T,m)); base=np.mean(list(Z.values()))
    row={}
    for a,b in V:
        nus=[nu for nu in range(1,2*h,2) if (b*nu-a)%(2*h)==0 and nu in Z]
        row[f'{a},{b}']=Z[nus[0]] if nus else None
    out[m]=row
for a,b in V:
    k=f'{a},{b}'; vals=[out[m][k] for m in [9,11,13,15]]
    rat=[ (vals[i+1]/vals[i])**0.25 if vals[i] and vals[i+1] else None for i in range(3)]
    print(k, ['%.4g'%v if v else None for v in vals], 'r est', ['%.3f'%r if r else None for r in rat])
json.dump(out,open('../logs/tier2.json','w'))
