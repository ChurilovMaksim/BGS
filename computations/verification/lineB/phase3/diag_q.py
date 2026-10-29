"""Decompose F by the Ramanujan level q | h (contribution of class pairs with h/gcd(r-r',h)=q), and top classes."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from fast_classes import *
from fast_classes import _kernel_fast
m=int(sys.argv[1]); etas=[float(x) for x in sys.argv[2].split(',')]
h,A,P=class_sums(m,etas); d=np.arange(h); q=h//np.gcd(d,h); ker=_kernel_fast(h,q)
for i,eta in enumerate(etas):
    Fa=np.fft.fft(A[i]); corr=np.real(np.fft.ifft(np.abs(Fa)**2))
    parts={int(a):float(np.sum((ker*corr)[q==a]))/h**2 for a in np.unique(q)}
    top=np.argsort(-np.abs(A[i]))[:5]
    cls=np.bincount((lambda x0,x1:(x0*x0-6*x0*x1+x1*x1)%h)(*np.meshgrid(np.arange(h),np.arange(h),indexing='ij')).ravel(),minlength=h) if h<9000 else None
    print(f'm={m} eta={eta} F={sum(parts.values()):.3f} by q: '+' '.join(f'q={k}:{v:+.3f}' for k,v in parts.items()))
    print('   top |A_r|: '+' '.join(f'r={r} gcd={np.gcd(r,h)} |A|={abs(A[i][r]):.1f} size={cls[r] if cls is not None else -1}' for r in top))
