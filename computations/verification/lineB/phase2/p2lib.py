if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys; sys.path.insert(0,__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','phase1'))
from dlib import *
import numpy as np, math
def support_data(m, ck=CK):
    O=Orbits(m,ck); D=O.D; E=e(-O.cls/O.gp); k1=np.fft.fft2(E)/D; Kd=np.abs(k1)**2
    supp=Kd>1e-9*Kd.max(); return O,supp
def k_all_units(O, idx):
    """k_nu(xi) for all units nu (rows) and flat support indices idx (cols)."""
    u=O.units(); out=np.empty((len(u),len(idx)),complex)
    for a,nu in enumerate(u):
        out[a]=(np.fft.fft2(e(-nu*O.cls/O.gp))/O.D).ravel()[idx]
    return u,out
def mobius(n):
    r=1; p=2
    while p*p<=n:
        if n%p==0:
            n//=p
            if n%p==0: return 0
            r=-r
        p+=1
    return -r if n>1 else r
def phi(n): return sum(1 for a in range(1,n+1) if math.gcd(a,n)==1)
