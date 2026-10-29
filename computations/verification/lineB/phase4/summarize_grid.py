"""Merge certified intervals, check contiguous coverage, print table (REPORT4 §1.4)."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import json, glob, math
recs=[]
for f in sorted(glob.glob('logs/grid_s*.jsonl')):
    for L in open(f):
        d=json.loads(L)
        if d['ok']: recs.append(d)
recs.sort(key=lambda d:d['e0'])
cov=[]; 
for d in recs:
    if cov and abs(d['e0']-cov[-1][1])<1e-12: cov[-1][1]=d['e1']
    else: cov.append([d['e0'],d['e1']])
print('certified coverage:',[(round(a,6),round(b,6)) for a,b in cov])
print('#intervals',len(recs))
sig2=3.75e-4
print(f"{'eta0':>8} {'eta1':>8} {'rho_I':>9} {'C_I':>8} {'-logrho/(s2 e1^2/2)':>19} {'m+(.01)':>8} {'m_gauss(.01)':>12} {'m_lo(.99)':>9} {'states':>7}")
for d in recs:
    r=max(d['rho']); C=sum(d['C']); lr=-math.log(r)
    mc=1+math.ceil(math.log(C/0.01)/lr)
    mlb=math.floor(0.02/(sig2*d['e1']**2)); g=sig2*d['e1']**2/2; mg=math.log(100)/(sig2*d['e0']**2/2)
    print(f"{d['e0']:8.4f} {d['e1']:8.4f} {r:9.6f} {C:8.2g} {lr/g:19.3f} {mc:8d} {mg:12.0f} {mlb:9d} {d['states']:7d}")
