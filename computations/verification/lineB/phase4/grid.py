"""Adaptive certified grid for the parity transfer majorant.  Usage: grid.py lo hi tag
Each line of logs/grid_<tag>.jsonl is one certified interval [e0,e1] with per-a (rho_a, C_a, valid flags).
An interval counts as CERTIFIED iff all 4 a are valid and max rho_a < 1."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys, json, time, math, os; sys.path.insert(0,'.')
import numpy as np, certify3 as c3
from certify import bounds, remainder_mass
lo,hi,tag=float(sys.argv[1]),float(sys.argv[2]),sys.argv[3]
out=f'logs/grid_{tag}.jsonl'
def params(e):
    return dict(beta=0.1,kappa=0.05,Kmid=min(20,8+round(e/4)),x2=min(50,25+round(e/2)))
def try_iv(e0,e1):
    p=params(e1); beta,kappa=p['beta'],p['kappa']
    n,b,b0,eps,tl=bounds(e0,e1); tau=(beta+kappa)*c3.CC_SAFE
    rem=remainder_mass(b0,n,eps,tau)+tl*1e40
    r0=c3.cert_one(e0,e1,0,n,b,rem,beta,kappa,p['Kmid'],p['x2'],theta=1e-9,iters=20)
    if not(r0['valid'] and r0['rho']<1): return [r0]
    res=[r0]
    for a in (1,2,3):
        r=c3.cert_one(e0,e1,a,n,b,rem,beta,kappa,p['Kmid'],p['x2'],theta=1e-9,iters=20,rfloor=min(0.95,r0['rho_t']))
        res.append(r)
    return res
e=lo; w=float(sys.argv[4]) if len(sys.argv)>4 else 0.1
if os.path.exists(out):
    for L in open(out):
        d=json.loads(L)
        if d['ok']: e=max(e,d['e1']); w=d['w']*1.4
while e<hi-1e-12:
    e1=min(hi,e+w); t=time.time(); res=try_iv(e,e1)
    ok=all(r['valid'] for r in res) and len(res)==4 and max(r['rho'] for r in res)<1
    rec=dict(e0=e,e1=e1,w=w,ok=ok,rho=[r['rho'] for r in res],C=[r['C'] for r in res],rho_float=res[0]['rho_float'],
             valid=[r['valid'] for r in res],states=res[0]['states'],Kmid=res[0]['Kmid'],K2=res[0]['K2'],secs=round(time.time()-t))
    open(out,'a').write(json.dumps(rec)+'\n')
    print(json.dumps(rec),flush=True)
    if ok: e=e1; w*=1.4
    else:
        w/=2
        if w<1e-3: print('STOP: width too small at',e,flush=True); break
print('DONE',tag,e,flush=True)
