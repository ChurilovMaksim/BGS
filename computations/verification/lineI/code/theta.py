"""Bulk mean of |Z|^2/RMT as a function of the real coupling theta=2a/b (shortest vector), fine bins, by height band."""
import sys, numpy as np, json
from base import get
out={}
for spec in sys.argv[1:]:
    k,m=spec.split(':'); m=int(m); D=get(k,m); Z=D['Z']; RMT=float(D['RMT']); nr=~D['res']&~D['dil']; phi=len(Z); h=int(D['h'])
    a=D['a'].astype(float); b=D['b'].astype(float); x=Z/RMT; l=np.hypot(a,b)
    th=2*a/np.maximum(b,1)
    edges=np.linspace(-1.2,1.2,49)
    print(f'== {k} m={m}  (bins of theta=2a/b; columns: l<sqrt(h)/4, sqrt(h)/4<=l<sqrt(h), l>=sqrt(h))')
    rows=[]
    for i in range(len(edges)-1):
        s=nr&(th>=edges[i])&(th<edges[i+1]); line=f'  th[{edges[i]:+.2f},{edges[i+1]:+.2f})'
        row=[]
        for L0,L1 in [(0,np.sqrt(h)/4),(np.sqrt(h)/4,np.sqrt(h)),(np.sqrt(h),1e9)]:
            t=s&(l>=L0)&(l<L1); v=x[t].mean() if t.sum()>5 else np.nan; row.append((int(t.sum()),float(v)))
            line+=f'  n={t.sum():7d} x={v:6.3f}'
        print(line); rows.append(row)
    out[spec]=rows
json.dump(out,open('../logs/theta.json','w'))
