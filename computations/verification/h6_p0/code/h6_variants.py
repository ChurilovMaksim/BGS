"""P4 (1) sensitivity: 8V k=4000 p0 with log K shifted by delta (A_J, kappa_F, robust Bowen ball contracted both ways = +k log lam)."""
if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")
import os as _os
HERE=_os.path.dirname(_os.path.abspath(__file__)); LOGS=_os.path.join(_os.path.dirname(HERE),'logs')
import json
exec(open(HERE+'/h6_p0.py').read().split("if __name__")[0])
t=r2tab(); c=consts('8V'); h=hs_consts('8V',4000)
out=[]
for name,delta in [('base',0),('kappa_F x 1e3',float(arb(1000).log().upper())),('robust Bowen ball (contract v1 by lam^-(p-1+k), v2 by lam^-k; frequency-embedding-free, +k log lam)',float((4000*LAM.log()).upper())),('log K + 1e5',1e5)]:
    h2=dict(h); h2['logLp']=h['logLp']+arb(delta)/2   # K1 contains 2*log c1 -> shifts K1 by delta
    r=certify('8V',4000,c,h2,t[('8V',4000)],10**10); r['variant']=name; r['delta_logK']=delta; out.append(r); print(json.dumps(r),flush=True)
json.dump(out,open(LOGS+'/h6_variants.json','w'),indent=1)
