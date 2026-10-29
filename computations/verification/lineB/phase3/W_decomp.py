"""Fixed-eta decomposition (odd m):  F_m(eta) = B_sym + W_par + W_rest,
B_sym = 2m - deficit (Theorem D closed form), W_par ~= 2m*chi_m(eta), chi_m = h^-2 sum_x exp(i eta (S(x)-S(-x)))
(the replacement |Gamma xi| -> 2m and the exclusion of -xi in Gamma xi change W_par by <= 4m*(#nongeneric)/h^2 = O(m^2/h)).
chi_m also predicted by the transfer operator: chi_m = sum_a (-1)^a Tr M_a^m."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from fast_classes import *
from fast_classes import _kernel_fast
sys.path.insert(0,__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','phase3'))
from parity_transfer import chi_transfer
import importlib.util
spec=importlib.util.spec_from_file_location('dodd',__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','phase2/deficit_odd.py'))
src=open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','phase2/deficit_odd.py')).read().split("print('== direct")[0]
ns={}; exec(src,ns)
ms=[int(x) for x in sys.argv[1].split(',')]; etas=[float(x) for x in sys.argv[2].split(',')]
for m in ms:
    t0=time.time(); h,A,P=class_sums(m,etas); ker=_kernel_fast(h,h//np.gcd(np.arange(h),h))
    num,den=ns['formula'](m); Bsym=2*m-num/den
    print(f'm={m} h={h} B_sym={Bsym:.6f} (2m={2*m}) error bound on W_par approx ~4m*m*h/h^2={4*m*m/h:.3f}',flush=True)
    for i,eta in enumerate(etas):
        F=F_from_A(h,A[i],ker); chi=(P[i].sum()/h**2).real
        K=8 if eta<=50 else 14
        chiT=chi_transfer(eta,m,K,(1,-1,1,-1)).real
        Wpar=2*m*chi; Wr=F-Bsym-Wpar
        print(f'  eta={eta:6g} F/2m={F/(2*m):.4f} chi={chi:+.5f} (transfer {chiT:+.5f}) W_par/2m={chi:+.4f} W_rest/2m={Wr/(2*m):+.4f}',flush=True)
    print(f'  time {time.time()-t0:.0f}s',flush=True)
