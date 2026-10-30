"""Halo profile vs e = b - q|a| (q=4: N≡±4 direction, q=8: N≡±8), exact e, both signs; contributions to W'/m."""
import sys, numpy as np, json
from base import get
res={}
for spec in sys.argv[1:]:
    k,m=spec.split(':'); m=int(m); D=get(k,m); Z=D['Z']; RMT=float(D['RMT']); nr=~D['res']&~D['dil']; phi=len(Z); h=int(D['h'])
    a=D['a']; b=D['b']; x=Z/RMT; l=np.hypot(a,b)
    for q in (4,8):
        e=b-q*np.abs(a); line=[]; tot=0; rows={}
        for ee in range(-40,41):
            s=nr&(e==ee)&(np.abs(a)>=4)
            if s.sum()<4: continue
            c=(Z[s]-RMT).sum()/phi/m; tot+=c; rows[ee]=(int(s.sum()),float(x[s].mean()),float(c))
        res[f'{spec}:q{q}']=rows
        print(f'== {k} m={m} q={q}: total contrib |e|<=40: {tot:+.4f} W/m')
        print('   '+' '.join(f'{ee}:{v[1]:.2f}' for ee,v in rows.items() if abs(ee)<=24))
        print('   counts: '+' '.join(f'{ee}:{v[0]}' for ee,v in rows.items() if abs(ee)<=6))
json.dump(res,open('../logs/halo3.json','w'))
