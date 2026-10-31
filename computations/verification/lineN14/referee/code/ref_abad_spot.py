"""Referee spot-check of N14 a_cert.jsonl: |w| = |r_A r_B|^3 for random classes alpha=(a,b) (seed e=2 alpha), own float chain
(N13-audit window code), compared to absw_up / absw_float; plus check enumerated classes are distinct mod +-eps^Z and norms < 2^13."""
import json, random, sys, math
exec(open('/workspace/audit/lineN13/code/ref_replay_spot.py').read().split("rows=[json.loads")[0])
R=[json.loads(l) for l in open('/workspace/bgs-lineN/N14/logs/a_cert.jsonl')]
random.seed(14); pick=random.sample(R,8)+[R[0],R[3]]
res=[]
for r in pick:
    wA,wB=window(2*r['a'],2*r['b']); w=abs(wA*wB)**3
    res.append(dict(a=r['a'],b=r['b'],w_ref=w,absw_up=r['absw_up'],absw_float=r['absw_float'],ok=w<=r['absw_up']*(1+1e-12),rel=abs(w-r['absw_float'])/r['absw_float']))
    print(res[-1],flush=True)
# distinctness / norm range
r2=math.sqrt(2); lam=3+2*r2
def mul(u,v): return (u[0]*v[0]+2*u[1]*v[1], u[0]*v[1]+u[1]*v[0])
def canon(a,b):
    for _ in range(400):
        x1=a+b*r2; x2=a-b*r2
        if x1<0: a,b=-a,-b; continue
        q=x1/abs(x2)
        if q>=lam*(1-1e-12): a,b=mul((a,b),(-1,1)); continue
        if q<1: a,b=mul((a,b),(1,1)); continue
        return (a,b)
cs=[canon(r['a'],r['b']) for r in R]; norms=[abs(r['a']**2-2*r['b']**2) for r in R]
out=dict(spot=res,all_ok=all(x['ok'] for x in res),n=len(R),n_distinct=len(set(cs)),max_norm=max(norms),norm_lt_2_13=all(n<2**13 for n in norms))
print({k:v for k,v in out.items() if k!='spot'}); json.dump(out,open('logs/ref_abad_spot.json','w'),indent=1)
