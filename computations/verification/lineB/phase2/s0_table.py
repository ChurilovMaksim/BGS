"""s0(eta)=sum|ghat|, s2=sum n^2|ghat|, kappa=sum|ghat|^4 for the actual diagonal symbol; uniform-in-m window constant
c(eta) = 1/(log lambda + 2 log s0)  (Theorem U: N-average -> F_m(eta) uniformly for m <= (1-eps) c(eta) log X)."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from p2lib import *
lam=3+2*np.sqrt(2)
for eta in [0.25,0.5,1,2,5,10,25,50,100,200]:
    n,g=ghat(eta,L=1<<14); a=np.abs(g); s0=a.sum(); s2=(a*n.astype(float)**2).sum(); kap=(a**4).sum()
    c=1/(np.log(lam)+2*np.log(s0))
    print(f'eta={eta:6g} s0={s0:10.4f} s2={s2:12.4e} kappa=sum|ghat|^4={kap:.4e}  c(eta)=1/(log lam+2 log s0)={c:.4f}  (vs 1/log lam={1/np.log(lam):.4f})')
