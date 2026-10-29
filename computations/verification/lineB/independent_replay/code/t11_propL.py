"""Prop L check: X(x)=sum_j u(1/2+x_j/h) over q-sequences x mod h (x_{j+1}=6x_j-x_{j-1}); E X^2 = m sigma^2 exactly?
chi_m(eta)=E cos(eta X) >= 1 - m sigma^2 eta^2/2 ?  Independent of phase-4 code."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys, numpy as np, math
from fractions import Fraction as Fr
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__))); from core import CK
AK={k:-4*float(CK[k][1]) for k in CK if CK[k][1]!=0}
sig2=sum(a*a for a in AK.values())/2
def hh(m):
    T=[2,6]
    for i in range(m): T.append(6*T[-1]-T[-2])
    D=T[m]-2; h=math.isqrt(D//4); assert 4*h*h==D; return h
print('sigma^2 =',sig2)
for m in [3,5,7,9,11]:
    h=hh(m); x0=np.arange(h)
    EX=0.0; EX2=0.0; etas=[0.5,2,5,10,25,50]; cs=np.zeros(len(etas))
    for a0 in range(h):
        xm=np.full(h,a0,np.int64); xc=x0.copy(); X=np.zeros(h)
        for j in range(m):
            th=0.5+xm/h
            X+=sum(a*np.sin(2*np.pi*k*th) for k,a in AK.items())
            xm,xc=xc,(6*xc-xm)%h
        assert np.all(xm==a0) and np.all(xc==x0)   # period m
        EX+=X.sum(); EX2+=(X*X).sum()
        for i,e in enumerate(etas): cs[i]+=np.cos(e*X).sum()
    N=h*h; EX/=N; EX2/=N; cs/=N
    print(f'm={m} h={h}: E X={EX:+.3e}  E X^2={EX2:.10e}  m*sigma^2={m*sig2:.10e}  ratio={EX2/(m*sig2):.12f}')
    print('    chi:',' '.join(f'eta={e}:{c:.6f}(LB {1-0.5*m*sig2*e*e:+.4f}, ok={c>=1-0.5*m*sig2*e*e-1e-12})' for e,c in zip(etas,cs)),flush=True)
