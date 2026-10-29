"""Certificate envelopes, version 2 (fixes referee gaps G1, G2; REPORT4 §1.3).
G1: the J-truncation tail of the Bessel product is bounded directly in the TILTED l1 norm
    ||f||_tau = sum_n |f(n)| e^{tau|n|}  (submultiplicative under convolution since e^{tau|a+b|} <= e^{tau|a|}e^{tau|b|}):
    per factor k (argument x_k = eta*beta_k), sum_{|j|>J} |J_j(x)| e^{tau k|j|} <= 2 sum_{j>J} y^j/j! <= 2 y^{J+1}/(J+1)! e^{y},
    y = |x| e^{tau k}/2   (|J_j(x)| <= (|x|/2)^j/j!).  Product error:  err_{i} = err_{i-1}(L_k+t_k) + L_{<k} t_k  in ||.||_tau.
    Over the eta-interval the error propagates through e^{itu}: total <= tl_tau/(1-x), x = eps*||D||_tau (all Taylor orders).
G2: arrays are padded by 9*4 zeros on both sides before the 4 Taylor convolutions, and the mass that would still leave the
    array is computed exactly (full convolution minus kept part) and added, tilted at the worst |n|, to the remainder."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys, math; sys.path.insert(0,'.')
import numpy as np, flint
from wcoef import BETA
from certify import D, SAFE, remainder_mass
flint.ctx.prec=128
def what_arb_tilted(eta, tau, J=60):
    eta=flint.arb(eta); poly=flint.arb_poly([1]); off=0
    err=flint.arb(0); L=flint.arb(1)
    for k,b in sorted(BETA.items()):
        x=eta*flint.arb(b.numerator)/b.denominator
        coeffs=[flint.arb(0)]*(2*J*k+1)
        for j in range(-J,J+1): coeffs[(j+J)*k]=x.bessel_j(j) if j>=0 else ((-1)**(-j))*x.bessel_j(-j)
        y=abs(x).upper()*flint.arb(tau*k).exp()/2
        t=2*y**(J+1)/flint.arb(math.factorial(J+1))*y.exp()
        Lk=sum(abs(c)*flint.arb(tau*k*abs(j)).exp() for j,c in zip(range(-J,J+1),coeffs[::k]))
        err=err*(Lk+t)+L*t; L=L*Lk
        poly=poly*flint.arb_poly(coeffs); off-=J*k
    cs=[poly[i] for i in range(poly.degree()+1)]
    return off, cs, float(err.upper())*SAFE
def bounds_v2(e0,e1,tau,J=60):
    off,cs,tlt=what_arb_tilted(e0,tau,J)
    PAD=36
    b0=np.array([float(abs(x).upper()) for x in cs])*SAFE+1e-300
    b0=np.concatenate([np.zeros(PAD),b0,np.zeros(PAD)]); n=np.arange(len(b0))+off-PAD
    eps=e1-e0; b=b0.copy(); term=b0.copy(); spill=0.0
    for i in range(1,5):
        full=np.convolve(term,D)*eps*SAFE
        kept=full[9:-9]; spill+=float(full[:9].sum()+full[-9:].sum())*SAFE
        term=kept; b=b+term
    nmax=float(np.abs(n).max())+9
    Dt=sum(abs(float(bb))*math.exp(tau*k) for k,bb in BETA.items())*SAFE
    x=eps*Dt; assert x<0.5
    rem=remainder_mass(b0,n,eps,tau) + tlt/(1-x) + spill*math.exp(tau*nmax)
    return n,b*SAFE,b0,eps,rem,dict(trunc_tilted=tlt,spill=spill,x=x)
if __name__=='__main__':
    tau=(0.1+0.05)*0.35356
    for e0,e1 in [(1,1.1),(50,50.5),(81.2445,81.5741)]:
        n,b,b0,eps,rem,info=bounds_v2(e0,e1,tau)
        print(e0,e1,'rem',rem,info,flush=True)
