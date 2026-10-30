"""Independent torsion-class split at m=11 (h=23*353): A_r = sum_{x: q(x)=r} e^{i eta S(x)}, q = x0^2-6x0x1+x1^2,
F = h^-2 sum_{r,r'} A_r conj(A_r') c_h(r-r')/phi(h) (Ramanujan sum, multiplicative).  Own code (not phase-4)."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys, numpy as np, math, time
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__))); from core import ck_complex
m=11; p1,p2=23,353; h=p1*p2; phi=(p1-1)*(p2-1)
ck=ck_complex()
def f(th): return sum((c*np.exp(2j*np.pi*k*th)).real for k,c in ck.items())
ft=f(0.5+np.arange(h)/h); ftn=f(0.5-np.arange(h)/h)
etas=[2.0,5.0,10.0]
A=np.zeros((len(etas),h),complex); P=np.zeros(len(etas),complex); cnt=np.zeros(h)
t0=time.time(); x1all=np.arange(h,dtype=np.int64)
for s0 in range(0,h,200):
    a=np.repeat(np.arange(s0,min(h,s0+200),dtype=np.int64)[:,None],h,1); b=np.broadcast_to(x1all,a.shape).copy()
    r=((a*a-6*a*b+b*b)%h).ravel(); cnt+=np.bincount(r,minlength=h)
    S=np.zeros(a.shape); Sn=np.zeros(a.shape)
    for j in range(m): S+=ft[a]; Sn+=ftn[a]; a,b=b,(6*b-a)%h
    for i,e in enumerate(etas):
        z=np.exp(1j*e*S).ravel(); A[i]+=np.bincount(r,z.real,h)+1j*np.bincount(r,z.imag,h)
        P[i]+=np.exp(1j*e*(S-Sn)).sum()
print('built',round(time.time()-t0),'s',flush=True)
def F(X):
    tot=0.0
    for d,sg in [(1,1),(p1,-1),(p2,-1),(h,1)]:
        e=h//d   # e = product of primes in S: d is complementary; coefficient prod_{p in S} p, sign (-1)^{2-|S|}
    # explicit: c_h(d)/phi = prod_p (p*[p|d]-1)/(p-1)
    out=0.0
    for S_ in [(),(p1,),(p2,),(p1,p2)]:
        e=int(np.prod(S_)) if S_ else 1; coef=(np.prod(S_) if S_ else 1)*(-1)**(2-len(S_))
        cls=np.bincount(np.arange(h)%e,X.real,e)+1j*np.bincount(np.arange(h)%e,X.imag,e)
        out+=coef*np.sum(np.abs(cls)**2)
    return out/phi/h**2
for i,e in enumerate(etas):
    chi=(P[i]/h**2).real; Ft=F(A[i])
    print(f'eta={e}: F/2m={Ft/(2*m):.4f} chi={chi:.6f}',flush=True)
    for p in (p1,p2):
        R=(np.arange(h)%p==0); sp=cnt[R].sum()/h**2
        Fg=F(np.where(R,0,A[i])); Fto=Ft-Fg
        print(f'   p={p}: s_p={sp:.5f} (2p-1)/p^2={(2*p-1)/p**2:.5f}  e_gen={Fg/(2*m*(1-sp))-(1+chi):+.4f}  e_tor={Fto/(2*m*sp)-(1+chi):+.4f}  F_tor/2m={Fto/(2*m):.4f}')
    mag=np.abs(A[i]); top=np.argsort(-mag)[:12]
    print('   top |A_r|:',[(int(r),round(float(mag[r])),int(r%p1),int(r%p2)) for r in top],' rms',round(float(np.sqrt(np.mean(mag**2)))),
          ' median',round(float(np.median(mag))))
    # level-1 diagonal share: h^-2 sum |A_r|^2 * (coefficient of the full-h term = h/phi)
    print(f'   h^-2 sum|A_r|^2 * h/phi = {np.sum(mag**2)/h**2*h/phi:.2f}  of F = {Ft:.2f};  share of sum|A_r|^2 in r%23==0: {np.sum(mag[np.arange(h)%p1==0]**2)/np.sum(mag**2):.4f}',flush=True)
