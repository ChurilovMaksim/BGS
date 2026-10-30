"""Independent numerical check of Prop L: E X^2 = m sigma^2 (sigma^2=3.75e-4) and chi_m(eta) >= 1 - m eta^2 sigma^2/2, m>=5.
X(x) = S(1/2+x/h) - S(1/2-x/h) over the odd support (phase-2 p2lib, independent of the transfer code)."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys; sys.path.insert(0,__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','phase2'))
from p2lib import *
import numpy as np
sig2=3.75e-4
for m in [3,5,7,9]:
    O,supp=support_data(m); i1=(-np.arange(O.d1))%O.d1; i2=(-np.arange(O.d2))%O.d2
    X=(O.S-O.S[i1][:,i2])[supp]
    print(f'm={m} D_eff={supp.sum()} E X={X.mean():+.2e} E X^2={np.mean(X**2):.10f} m*sig2={m*sig2:.10f}',flush=True)
    for eta in [1,3,10,20,30,50]:
        chi=np.mean(np.exp(1j*eta*X)); lb=1-m*eta**2*sig2/2
        print(f'   eta={eta:3d} chi={chi.real:+.6f} (imag {chi.imag:+.0e})  LB={lb:+.6f}  ok={chi.real>=lb-1e-12}',flush=True)
