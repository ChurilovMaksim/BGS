"""N14: the 200 'short' types (N12-F1) reduced to classes alpha=e/2 mod +-eps^Z; separate relabellings of model types from genuine
short clusters; certified (c2_mid, [CA-fp] core functional) sum over DISTINCT genuine classes of |w|_up, per-site x2."""
import json, math
from fractions import Fraction
rows=[json.loads(l) for l in open('/workspace/bgs-lineN/N14/logs/c2_mid.jsonl')]
r2=math.sqrt(2); lam=3+2*r2
def mul(u,v): return (u[0]*v[0]+2*u[1]*v[1], u[0]*v[1]+u[1]*v[0])
def norm_class(a,b):
    if (a,b)==(0,0): return None
    for _ in range(200):
        x1=a+b*r2; x2=a-b*r2
        if x1<0: a,b=-a,-b; continue
        q=x1/abs(x2)
        if q>=lam*(1-1e-12): a,b=mul((a,b),(-1,1)); continue    # times eps^{-1} = sqrt2-1
        if q<1: a,b=mul((a,b),(1,1)); continue
        return (a,b)
MODEL={(1,0),(0,1),(2,0),(0,2)}
cls={}; relab=0; zero=0
for r in rows:
    if r['kind']!='short': continue
    e=r['e']
    if e[0]%2 or e[1]%2: print('odd e?',e)
    c=norm_class(e[0]//2,e[1]//2)
    if c is None: zero+=1; continue
    up=(r['A']['abs_up']*r['B']['abs_up'])**3
    if c in MODEL: relab+=1; continue
    cls[c]=max(cls.get(c,0),up)
tot=sum(cls.values())
out=dict(n_short_rows=sum(1 for r in rows if r['kind']=='short'),model_relabellings=relab,zero=zero,genuine_rows=sum(1 for r in rows if r['kind']=='short')-relab-zero,
         genuine_classes=len(cls),sum_absw_up_distinct=tot,per_site_x2=2*tot,top=sorted([(v,k) for k,v in cls.items()],reverse=True)[:8])
print(json.dumps(out,indent=1)); json.dump(out,open('/workspace/bgs-lineN/N14/logs/f_short.json','w'),indent=1)
