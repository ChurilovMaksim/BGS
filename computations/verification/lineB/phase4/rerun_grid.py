"""Re-certify the 93 phase-4 intervals with the G1/G2-fixed envelopes (certify_v2.bounds_v2).
Same parameters as grid.py (beta=0.1, kappa=0.05, Kmid=min(20,8+round(e1/4)), x2=min(50,25+round(e1/2)), theta=1e-9, iters=20).
Usage: rerun_grid.py worker nworkers   -> logs/grid_v2_w<worker>.jsonl (resumable)."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys, json, glob, os, time; sys.path.insert(0,'.')
import certify3 as c3
from certify_v2 import bounds_v2
def params(e): return dict(beta=0.1,kappa=0.05,Kmid=min(20,8+round(e/4)),x2=min(50,25+round(e/2)))
w,nw=int(sys.argv[1]),int(sys.argv[2])
old=sorted([json.loads(l) for f in glob.glob('logs/grid_s*.jsonl') for l in open(f)],key=lambda d:d['e0'])
old=[d for d in old if d['ok']]
assert len(old)==93
out=f'logs/grid_v2_w{w}.jsonl'
done=set()
if os.path.exists(out): done={json.loads(l)['e0'] for l in open(out)}
# interleave heavy (large eta) intervals across workers
mine=[d for i,d in enumerate(old) if i%nw==w]
for d in mine:
    if d['e0'] in done: continue
    e0,e1=d['e0'],d['e1']; p=params(e1); t=time.time()
    tau=(p['beta']+p['kappa'])*c3.CC_SAFE
    n,b,b0,eps,rem,info=bounds_v2(e0,e1,tau)
    res=[c3.cert_one(e0,e1,0,n,b,rem,p['beta'],p['kappa'],p['Kmid'],p['x2'],theta=1e-9,iters=20)]
    for a in (1,2,3):
        res.append(c3.cert_one(e0,e1,a,n,b,rem,p['beta'],p['kappa'],p['Kmid'],p['x2'],theta=1e-9,iters=20,rfloor=min(0.95,res[0]['rho_t'])))
    ok=all(r['valid'] for r in res) and max(r['rho'] for r in res)<1
    rec=dict(e0=e0,e1=e1,ok=ok,rho=[r['rho'] for r in res],C=[r['C'] for r in res],rho_old=max(d['rho']),
             rem=rem,trunc_tilted=info['trunc_tilted'],spill=info['spill'],secs=round(time.time()-t))
    open(out,'a').write(json.dumps(rec)+'\n'); print(json.dumps(rec),flush=True)
print('DONE worker',w,flush=True)
