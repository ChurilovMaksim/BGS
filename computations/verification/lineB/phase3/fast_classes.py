"""Fast exact fixed-eta second moment for odd m via norm classes on V^_odd = (Z/h)^2 (coordinates (x0,x1) of the
q-sequence x_j, x_{j+1}=6x_j-x_{j-1} mod h; support xi = 1/2*1 + x/h).  Invariant form q(x0,x1)=x0^2-6x0x1+x1^2 mod h.
F_m(eta) = h^-2 sum_{r,r'} A_r conj(A_r') mu(q)/phi(q),  q = h/gcd(r-r',h),  A_r = sum_{q(x)=r} exp(i eta S(1/2+x/h)).
Also P_r = sum_{q(x)=r} exp(i eta (S(x)-S(-x)))  -> parity part.  Validated against the Orbits/FFT computation for m=5,7,9."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys; sys.path.insert(0,__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','phase2'))
from p2lib import *
import math, time
def hm(m):
    x,y=1,0
    for _ in range(m): x,y=3*x+8*y,x+3*y
    return math.isqrt((x-1)//2)
def kernel(h):
    d=np.arange(h); g=np.gcd(d,h); q=h//g
    return np.array([mobius(int(a))/phi(int(a)) if True else 0 for a in q]) if h<2000 else _kernel_fast(h,q)
def _kernel_fast(h,q):
    vals={}
    for a in np.unique(q): vals[a]=mobius(int(a))/phi_fast(int(a))
    return np.vectorize(vals.get)(q).astype(float)
def phi_fast(n):
    r=n; p=2; k=n
    while p*p<=k:
        if k%p==0:
            while k%p==0: k//=p
            r-=r//p
        p+=1
    if k>1: r-=r//k
    return r
def class_sums(m, etas, chunk=None):
    h=hm(m); ftab=f_diag(0.5+np.arange(h)/h); ftabn=f_diag(0.5-np.arange(h)/h)
    A=np.zeros((len(etas),h),complex); P=np.zeros((len(etas),h),complex)
    x1=np.arange(h,dtype=np.int64)
    chunk=chunk or max(1,int(2e6//h))
    for s in range(0,h,chunk):
        x0=np.arange(s,min(h,s+chunk),dtype=np.int64)[:,None]
        a=np.broadcast_to(x0,(len(x0),h)).copy(); b=np.broadcast_to(x1,(len(x0),h)).copy()
        r=(a*a-6*a*b+b*b)%h
        S=np.zeros(a.shape); Sn=np.zeros(a.shape)
        for j in range(m):
            S+=ftab[a]; Sn+=ftabn[a]; a,b=b,(6*b-a)%h
        rr=r.ravel()
        for i,eta in enumerate(etas):
            ph=np.exp(1j*eta*S).ravel(); A[i]+=np.bincount(rr,ph.real,h)+1j*np.bincount(rr,ph.imag,h)
            pp=np.exp(1j*eta*(S-Sn)).ravel(); P[i]+=np.bincount(rr,pp.real,h)+1j*np.bincount(rr,pp.imag,h)
    return h,A,P
def F_from_A(h,A,ker):
    # sum_{r,r'} A_r conj A_r' ker(r-r') = sum_d ker(d) Corr(d), Corr(d)=sum_r A_{r+d} conj A_r
    Fa=np.fft.fft(A); corr=np.fft.ifft(np.abs(Fa)**2)
    return float(np.real(np.sum(ker*corr)))/h**2
if __name__=='__main__':
    ms=[int(x) for x in sys.argv[1].split(',')]; etas=[float(x) for x in sys.argv[2].split(',')]
    for m in ms:
        t0=time.time(); h,A,P=class_sums(m,etas); ker=_kernel_fast(h,h//np.gcd(np.arange(h),h))
        for i,eta in enumerate(etas):
            F=F_from_A(h,A[i],ker); chi=P[i].sum()/h**2
            print(f'm={m} h={h} eta={eta:g} F={F:.6f} F/2m={F/(2*m):.4f} chi_par={chi.real:+.5f}',flush=True)
        print(f'  time {time.time()-t0:.0f}s',flush=True)
