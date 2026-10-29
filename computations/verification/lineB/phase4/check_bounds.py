"""Independent check (FFT, no arb) that the certified envelopes b(n) dominate |w_eta(n)| on sampled eta in each interval."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys, json, glob; sys.path.insert(0,'.'); sys.path.insert(0,__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','phase2'))
import numpy as np
from p2lib import f_diag
from certify import bounds
L=8192; th=np.arange(L)/L; uu=f_diag(th)-f_diag(-th)
recs=[json.loads(l) for f in sorted(glob.glob('logs/grid_s*.jsonl')) for l in open(f)]
recs=[d for d in recs if d['ok']]
worst=0
for d in recs[::4]:
    n,b,b0,eps,tl=bounds(d['e0'],d['e1'])
    ratio=0
    for eta in np.linspace(d['e0'],d['e1'],12):
        c=np.fft.fft(np.exp(1j*eta*uu))/L; w=np.abs(c[n%L])
        sel=w>1e-12; ratio=max(ratio,float(np.max(w[sel]/b[sel]))); assert np.all(w<=b+1e-14)
    worst=max(worst,ratio)
    print(f"[{d['e0']:.4f},{d['e1']:.4f}] max_n,eta |w|/b = {ratio:.6f}",flush=True)
print('WORST',worst)
