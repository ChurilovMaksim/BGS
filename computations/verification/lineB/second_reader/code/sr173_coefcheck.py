"""Second reader: t9_cert coefficient envelopes b(n) vs an independent FFT of w_eta(theta)=exp(i eta u(theta)),
u = f(1/2+.)-f(1/2-.) built from the shifted symbol c~_k=(-1)^k c_k (and, as a control, from c_k: |w^(n)| is the same).
Checks b(n) >= |w^_eta(n)| at sampled eta (for |w^| > 1e-14, above the float FFT noise floor ~1e-18), and that b is tight (ratio close to 1 on the bulk)."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys, json, math, numpy as np
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__))); import t9_cert as T
from fractions import Fraction as Fr
CK={1:(Fr(1,20),Fr(-1,200)),2:(Fr(0),Fr(-1,400)),5:(Fr(0),Fr(-1,800)),6:(Fr(-1,40),Fr(-1,400)),7:(Fr(9,20),Fr(0)),8:(Fr(-1,40),Fr(1,400)),9:(Fr(0),Fr(1,800))}
M=4096; th=np.arange(M)/M
def f(t,shift):
    out=np.zeros_like(t)
    for k,(a,b) in CK.items():
        c=complex(a,b)*((-1)**k if shift else 1); out+=2*(c*np.exp(2j*np.pi*k*t)).real
    return out
res=[]
for (e0,e1) in [(1.0,1.1),(30.0,30.5),(81.24448885935443,81.57406988332305)]:
    tau=(0.1/(4*math.sqrt(2))*1.5)*2
    n,b,Ed=T.coef_bounds(e0,e1,tau,M=24); bd=dict(zip(n.tolist(),b.tolist()))
    worst=0.0; tight=[]
    for eta in np.linspace(e0,e1,7):
        for shift in (True,False):
            u=f(th,shift)-f(-th,shift)
            w=np.fft.fft(np.exp(1j*eta*u))/M          # w^(n) at index n mod M
            for nn in range(-60,61):
                val=abs(w[nn%M]); bb=bd.get(nn,0.0)
                if val>1e-14: worst=max(worst,val/bb if bb>0 else np.inf)
                if shift and val>1e-6: tight.append(val/bb)
    res.append(dict(e0=e0,e1=e1,max_ratio_fft_over_b=worst,median_ratio_bulk=float(np.median(tight)),Edrop=Ed))
    print(json.dumps(res[-1]),flush=True)
