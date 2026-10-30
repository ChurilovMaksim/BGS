"""s0(eta)=sum|g^(n)|, g=e^{i eta f}; Theorem U window constants c(eta)=1/(log lam + 2 log s0); improved alternatives."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys, numpy as np, math
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__))); from core import *
NG=1<<15; lam=3+2*math.sqrt(2); L=math.log(lam)
f=ftab(NG)
print(f'log(lambda)={L:.5f}  1/(2 log lambda)={1/(2*L):.4f}  Ehrenfest 1/log(lambda)={1/L:.4f}')
for eta in [0.5,1,5,25,100,400]:
    c=np.fft.fft(np.exp(1j*eta*f))/NG; s0=np.sum(np.abs(c)); s2=np.sum(np.abs(c)*np.fft.fftfreq(NG,1/NG)**2); kap=np.sum(np.abs(c)**4)
    c1=1/(L+2*math.log(s0)); c_first=1/(2*math.log(s0)) if s0>1 else float('inf')
    cimp=min(c_first, max(c1,1/(2*L)))
    print(f'eta={eta:6}: s0={s0:.3f} s2={s2:.1f} kappa={kap:.2e}  c(eta)={c1:.3f}  c*log(lam)={c1*L:.3f}  improved window (using min(s0^2m,D_eff)) c={cimp:.3f}')
