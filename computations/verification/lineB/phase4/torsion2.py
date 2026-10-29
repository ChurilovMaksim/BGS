"""Exact torsion-class split of Prop C (REPORT4 §2.3).  For a prime p | h:
R_p = {r in Z/h : p | r} = norm classes of the x with x mod p on an isotropic line (x mod p in l_+ u l_-).
F = F_gen + F_tor, F_gen = h^-2 sum_{r,r' notin R_p} A_r conj(A_r') K(r-r'),  F_tor = all pairs with r or r' in R_p.
Baseline (diagonal-only, |g|=1): the torsion classes carry the share s_p = #{x: p|q(x)}/h^2 = (2p-1)/p^2 of the diagonal.
Reports F_gen/(2m(1-s_p)) - (1+chi)  (generic remainder, normalised) and F_tor/(2m s_p) - (1+chi) (torsion excess)."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys; sys.path.insert(0,__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','phase3')); sys.path.insert(0,__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','phase2'))
from fast_classes import hm, _kernel_fast
from p2lib import f_diag
import numpy as np, time
m=int(sys.argv[1]); ps=[int(x) for x in sys.argv[2].split(',')]; etas=[float(x) for x in sys.argv[3].split(',')]
h=hm(m); ftab=f_diag(0.5+np.arange(h)/h); ftabn=f_diag(0.5-np.arange(h)/h)
A=np.zeros((len(etas),h),complex); Pp=np.zeros((len(etas),h),complex); cnt=np.zeros(h)
x1=np.arange(h,dtype=np.int64); chunk=max(1,int(2e6//h)); t0=time.time()
for s in range(0,h,chunk):
    x0=np.arange(s,min(h,s+chunk),dtype=np.int64)[:,None]
    a=np.broadcast_to(x0,(len(x0),h)).copy(); b=np.broadcast_to(x1,(len(x0),h)).copy()
    r=((a*a-6*a*b+b*b)%h).ravel(); cnt+=np.bincount(r,minlength=h)
    S=np.zeros(a.shape); Sn=np.zeros(a.shape)
    for j in range(m): S+=ftab[a]; Sn+=ftabn[a]; a,b=b,(6*b-a)%h
    for i,eta in enumerate(etas):
        ph=np.exp(1j*eta*S).ravel(); A[i]+=np.bincount(r,ph.real,h)+1j*np.bincount(r,ph.imag,h)
        pp=np.exp(1j*eta*(S-Sn)).ravel(); Pp[i]+=np.bincount(r,pp.real,h)+1j*np.bincount(r,pp.imag,h)
ker=_kernel_fast(h,h//np.gcd(np.arange(h),h)).astype(complex)
fk=np.fft.fft(ker)
def Fx(X,Y):  # h^-2 sum_{r,r'} X_r conj(Y_r') K(r-r')
    return float(np.real(np.sum(X*np.conj(np.fft.ifft(np.conj(fk)*np.fft.fft(Y))))))/h**2
num_by=None
import importlib
src=open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','phase2/deficit_odd.py')).read().split("print('== direct")[0]; ns={}; exec(src,ns)
nu,de=ns['formula'](m); Bsym=2*m-nu/de
print(f'm={m} h={h} B_sym={Bsym:.6f} time {time.time()-t0:.0f}s',flush=True)
for p in ps:
    assert h%p==0
    R=(np.arange(h)%p==0); sp=cnt[R].sum()/h**2
    print(f' p={p}: share s_p={sp:.5f} ((2p-1)/p^2={(2*p-1)/p**2:.5f}); torsion classes are {cnt[R][1:2]} pts each',flush=True)
    for i,eta in enumerate(etas):
        chi=(Pp[i].sum()/h**2).real
        Ag=np.where(R,0,A[i]); At=np.where(R,A[i],0)
        F=Fx(A[i],A[i]); Fg=Fx(Ag,Ag); Ft=F-Fg
        Wt=F-Bsym-2*m*chi
        print(f'   eta={eta:5g} F/2m={F/(2*m):.4f} chi={chi:+.4f} Wtilde/2m={Wt/(2*m):+.4f} | F_gen/(2m(1-s))-(1+chi)={Fg/(2*m*(1-sp))-(1+chi):+.4f} '
              f'| F_tor/(2m s)-(1+chi)={Ft/(2*m*sp)-(1+chi):+.4f}  F_tor/2m={Ft/(2*m):+.4f}',flush=True)
