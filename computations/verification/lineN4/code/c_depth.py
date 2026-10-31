"""N4 (C) [N]: isotropic points at q | h_p by 'depth' k(beta) = min |N(b)|/q over lifts b = beta mod q (b in the prime ideal).
Gauge lemma => slow window length ~ log_lam(q/k).  Reads N2 TRACE-206 twisted sums d_Zh_m{m}_q{q}_s1.npy (Zh[bx,by])."""
import sys, json, numpy as np
m=int(sys.argv[1]); q=int(sys.argv[2])
Zh=np.load(f'/workspace/bgs-lineN/N2/logs/d_Zh_m{m}_q{q}_s1.npy')
X=4*q; Y=3*q
x=np.arange(-X,X+1)[:,None]; y=np.arange(-Y,Y+1)[None,:]
N=np.abs(x*x-2*y*y)
out=dict(m=m,q=q,lines={})
for r in [t for t in range(q) if (t*t-2)%q==0]:
    sel=((x-r*y)%q==0)&(N>0)
    xs,ys=np.nonzero(sel); bx=(x[xs,0])%q; by=(y[0,ys])%q; kk=N[xs,ys]//q
    depth={}
    for a,b,k in zip(bx,by,kk):
        key=(int(a),int(b))
        if key not in depth or k<depth[key]: depth[key]=int(k)
    pts=[((r*t)%q,t) for t in range(1,q)]
    miss=[p for p in pts if p not in depth]
    rows=sorted(((depth.get(p,-1),abs(Zh[p]),p) for p in pts),key=lambda z:-z[1])
    tot=sum(abs(Zh[p]) for p in pts)
    bydepth={}
    for d,a,p in rows: bydepth[d]=bydepth.get(d,0)+a
    out['lines'][r]=dict(missing=len(miss),total_abs=tot,top=[(d,round(a,3)) for d,a,p in rows[:12]],
        share_by_depth=sorted(((d,round(v/tot,4)) for d,v in bydepth.items()),key=lambda z:z[0])[:15],
        signed_total=abs(sum(Zh[p] for p in pts)))
    print(r,json.dumps(out['lines'][r]),flush=True)
json.dump(out,open(f'logs/c_depth_m{m}_q{q}.json','w'),indent=1)
