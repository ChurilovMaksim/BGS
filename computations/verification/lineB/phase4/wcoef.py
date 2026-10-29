"""Exact data of the parity symbol and rigorous enclosures of its Fourier coefficients.
c_k*800 (k=-9..9) from phase2 Lean list; u(th) = f(th)-f(-th) = sum_{k>0} beta_k sin(2 pi k th) (real),
beta_k*800 = 16,8,4,8,-8,-4 for k=1,2,5,6,8,9.  e^{i eta u} = prod_k sum_j J_j(eta beta_k) e(j k th)
=> what(n) = sum_{sum_k k j_k = n} prod_k J_{j_k}(eta beta_k)  (real).  Rigorous via arb (python-flint)."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import flint, math
from fractions import Fraction as Fr
C800={-9:(0,-1),-8:(-20,-2),-7:(360,0),-6:(-20,2),-5:(0,1),-2:(0,2),-1:(40,4),1:(40,-4),2:(0,-2),5:(0,-1),6:(-20,-2),7:(360,0),8:(-20,2),9:(0,1)}
# u = sum_k (c_k - c_{-k}) e(k th); c_k-c_{-k} = 2i Im c_k ; u = sum_{k>0} 2i Im(c_k) (e(k th)-e(-k th)) = sum_{k>0} -4 Im(c_k) sin(2 pi k th)
BETA={k: Fr(-4*C800[k][1],800) for k in range(1,10) if k in C800 and C800[k][1]!=0}
U2=sum(b*b for b in BETA.values())/2          # ||u||_2^2
assert U2==Fr(240,640000)
def what_arb(eta, J=60):
    """returns (offset, list of arb) for what(n), n=offset..; truncation |j|<=J, rigorous tail added as radius."""
    eta=flint.arb(eta)
    poly=flint.arb_poly([1]); off=0; tail_l1=flint.arb(0); l1=flint.arb(1)
    for k,b in sorted(BETA.items()):
        x=eta*flint.arb(b.numerator)/b.denominator
        coeffs=[flint.arb(0)]*(2*J*k+1)
        for j in range(-J,J+1): coeffs[(j+J)*k]=x.bessel_j(j) if j>=0 else ((-1)**(-j))*x.bessel_j(-j)
        # tail |j|>J: sum 2*(|x|/2)^j/j! <= 2*(|x|/2)^(J+1)/(J+1)! * e^{|x|/2}
        ax=abs(x).upper()
        t=2*(ax/2)**(J+1)/flint.arb(math.factorial(J+1))*(ax/2).exp()
        poly=poly*flint.arb_poly(coeffs); off-=J*k
        # l1 of truncated factor <= sum|J_j| ; error mass propagation: (L1+t)*... accumulate crude bound
        Lk=sum(abs(c) for c in coeffs)
        tail_l1=tail_l1*(Lk+t)+l1*t; l1=l1*Lk
    cs=[poly[i] for i in range(poly.degree()+1)]
    return off, cs, tail_l1.upper()
if __name__=='__main__':
    import numpy as np, sys
    sys.path.insert(0,__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','phase3')); sys.path.insert(0,__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','phase2'))
    from p2lib import f_diag
    for eta in [1.0,10.0,100.0]:
        L=4096; th=np.arange(L)/L; g=np.exp(1j*eta*(f_diag(th)-f_diag(-th))); c=np.fft.fft(g)/L
        off,cs,tl=what_arb(eta)
        err=max(abs(float(cs[i].mid())-c[(i+off)%L].real) for i in range(len(cs)) if abs(i+off)<L//2)
        print(f'eta={eta}: max |arb - FFT| = {err:.2e}, max imag FFT {np.abs(c.imag).max():.1e}, tail_l1 <= {float(tl):.1e}, max radius {max(float(x.rad()) for x in cs):.1e}')
