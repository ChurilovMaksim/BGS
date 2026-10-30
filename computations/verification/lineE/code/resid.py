"""Line E: resonant residue nu* = odd lift of -4^{-1} mod h (mod g'=2h). Exact structure:
 phase(n) = -nu* y' Nm(alpha_n)/g' == (1/2) n^T H^{-1} n + kap8 (sum n)^2 / 8  (mod 1),  kap8 = k y' mod 8, k=(-4nu*-1)/h."""
import sys; import os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from pell import data, xy, hm
from fractions import Fraction as Fr
def nustar(m, sign=+1):
    d=data(m); h=d['h']; gp=d['gp']
    nu=(-sign*pow(4,-1,h))%h
    if nu%2==0: nu+=h
    k=(-4*nu-1)//h if sign==1 else None
    assert (-4*nu-1)%h==0 or sign!=1
    return nu,k
def G(m,dd):  # Green's function of H=6I-C-C^T : X/D with X=phi(d)=y_m x_d-(x_m-1)y_d (d>=1), y_m (d=0)
    xm,ym=xy(m); D=2*(xm-1); x,y=xy(dd)
    phi= ym if dd==0 else ym*x-(xm-1)*y
    return Fr(phi,D)
def check(m):
    d=data(m); h,gp,yp=d['h'],d['gp'],d['yp']; nu,k=nustar(m)
    kap8=(k*yp)%8
    ok=True
    # diagonal: -nu y'/g' == G(0)/2 + kap8/8 ; pair: -2 nu y' x_d/g' == G(d) + kap8/4  (mod 1)
    def m1(f): return f-(f.numerator//f.denominator)
    if m1(Fr(-nu*yp,gp)-G(m,0)/2-Fr(kap8,8))!=0: ok=False
    for dd in range(1,m):
        if m1(Fr(-2*nu*yp*xy(dd)[0],gp)-G(m,dd)-Fr(kap8,4))!=0: ok=False
    return dict(m=m,h=h,nu=nu,k=k,kap8=kap8,exact_ok=ok,G0=float(G(m,0)),G1=float(G(m,1)))
if __name__=='__main__':
    for m in range(5,42,2): print(check(m))
