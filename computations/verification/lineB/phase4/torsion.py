"""Exact small-prime torsion correction (REPORT4 §2.3).  p | h split prime (sqrt2 in F_p), lambda mod p in F_p^*.
l_+, l_- = isotropic eigenlines of T mod p;  P_pm = averaging over translations by the p-torsion points of l_pm
(t = 0 mod h/p),  P_0 = P_+P_- = averaging over all p-torsion.  g = e^{i eta S(1/2+x/h)},  g0 = (1-P_+)(1-P_-)g.
F(.) = Prop-C Hermitian form.  T_p := F(g) - F(g0)  (exact torsion correction).  Class sums of P g are computed exactly
from refined class sums A[r, type(x mod p)] (derivation in REPORT4)."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys; sys.path.insert(0,__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','phase3')); sys.path.insert(0,__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','phase2'))
from fast_classes import hm, F_from_A, _kernel_fast
from p2lib import f_diag
import numpy as np, time
m=int(sys.argv[1]); p=int(sys.argv[2]); etas=[float(x) for x in sys.argv[3].split(',')]
h=hm(m); assert h%p==0; hp=h//p
mus=[u for u in range(p) if (u*u-6*u+1)%p==0]; assert len(mus)==2, 'p must split'
ftab=f_diag(0.5+np.arange(h)/h); ftabn=f_diag(0.5-np.arange(h)/h)
A=np.zeros((len(etas),4,h),complex); Pp=np.zeros((len(etas),h),complex)
x1=np.arange(h,dtype=np.int64); chunk=max(1,int(2e6//h)); t0=time.time()
for s in range(0,h,chunk):
    x0=np.arange(s,min(h,s+chunk),dtype=np.int64)[:,None]
    a=np.broadcast_to(x0,(len(x0),h)).copy(); b=np.broadcast_to(x1,(len(x0),h)).copy()
    r=((a*a-6*a*b+b*b)%h).ravel()
    am,bm=a%p,b%p
    typ=np.full(a.shape,3); typ[(bm-mus[0]*am)%p==0]=1; typ[(bm-mus[1]*am)%p==0]=2; typ[(am==0)&(bm==0)]=0
    idx=(typ.ravel()*h+r)
    S=np.zeros(a.shape); Sn=np.zeros(a.shape)
    for j in range(m): S+=ftab[a]; Sn+=ftabn[a]; a,b=b,(6*b-a)%h
    for i,eta in enumerate(etas):
        ph=np.exp(1j*eta*S).ravel()
        A[i]+=(np.bincount(idx,ph.real,4*h)+1j*np.bincount(idx,ph.imag,4*h)).reshape(4,h)
        pp=np.exp(1j*eta*(S-Sn)).ravel(); Pp[i]+=np.bincount(r,pp.real,h)+1j*np.bincount(r,pp.imag,h)
ker=_kernel_fast(h,h//np.gcd(np.arange(h),h))
rr=np.arange(h); Np=np.where(rr%p==0,2*p-1,p-1)
def fold(v):   # sum over r' = r mod h/p, returned on Z/h
    return np.tile(v.reshape(p,hp).sum(0),p)
print(f'm={m} h={h}={p}*{hp} mu={mus} time {time.time()-t0:.0f}s',flush=True)
for i,eta in enumerate(etas):
    A0,Ap,Am,Ag=A[i]; Ag_all=A0+Ap+Am+Ag
    APp=A0+Ap+fold(Am+Ag)/p
    APm=A0+Am+fold(Ap+Ag)/p
    AP0=Np*fold(Ag_all)/p**2
    Ao=Ag_all-APp-APm+AP0
    F=F_from_A(h,Ag_all,ker); Fo=F_from_A(h,Ao,ker); chi=(Pp[i].sum()/h**2).real
    print(f'  eta={eta:5g} F/2m={F/(2*m):.4f}  F(g0)/2m={Fo/(2*m):.4f}  T_p/2m={(F-Fo)/(2*m):+.4f}  chi={chi:+.4f}  '
          f'(F-2m-2m chi)/2m={(F-2*m-2*m*chi)/(2*m):+.4f}  (F(g0)-2m-2m chi)/2m={(Fo-2*m-2*m*chi)/(2*m):+.4f}',flush=True)
