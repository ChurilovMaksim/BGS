"""N4 (C) [N]: sector-4 depth of isotropic points.  y = (bx + by sqrt2)/q, z4 = 1/4 (fixed point of x -> lam x on R^2/O^dual with
constant twist Tr(lam^i/4) = 1/2 mod 1, i.e. sector 4).  D(beta) = q * min_{w in O^dual} |N(y - 1/4 - w)|  (O^dual = (1/(2 sqrt2)) O).
Gauge lemma: slow window ~ log_lam(eps^2 q / D).  Groups |Zhat| on the isotropic lines by D (N2 TRACE-206 data)."""
import sys, json, math, numpy as np
m=int(sys.argv[1]); q=int(sys.argv[2])
Zh=np.load(f'/workspace/bgs-lineN/N2/logs/d_Zh_m{m}_q{q}_s1.npy'); s2=math.sqrt(2); R=int(4*math.sqrt(q))+40
a=np.arange(-R,R+1)[:,None]; b=np.arange(-R,R+1)[None,:]
w=b/2+a*s2/4; wc=b/2-a*s2/4
out=dict(m=m,q=q,lines={})
for r in [t for t in range(q) if (t*t-2)%q==0]:
    pts=[((r*t)%q,t) for t in range(1,q)]; groups={}
    for (bx,by) in pts:
        y=(bx+by*s2)/q; yc=(bx-by*s2)/q
        D=q*np.min(np.abs((y-0.25-w)*(yc-0.25-wc))); key=round(16*D)
        g=groups.setdefault(key,[0,0.0,0.0]); g[0]+=1; g[1]+=abs(Zh[bx,by]); g[2]=max(g[2],abs(Zh[bx,by]))
    tot=sum(g[1] for g in groups.values())
    rows=[dict(sixteenD=k,count=g[0],share=round(g[1]/tot,5),max_abs=round(g[2],4)) for k,g in sorted(groups.items())]
    out['lines'][r]=dict(total_abs=tot,rows=rows)
    print('line',r,'total',round(tot,3)); [print(' ',x) for x in rows[:10]]
json.dump(out,open(f'logs/c_depth4_m{m}_q{q}.json','w'),indent=1)
