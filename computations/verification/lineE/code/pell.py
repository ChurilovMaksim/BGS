"""Exact Pell data (Line B conventions, TRACE-163): S^d=[[x_d,4y_d],[2y_d,x_d]], lambda^d=x_d+2sqrt2 y_d."""
from fractions import Fraction as Fr
from math import gcd
def xy(d):
    x,y=1,0
    for _ in range(d): x,y=3*x+8*y,x+3*y
    return x,y
def data(m):
    xm,ym=xy(m); D=2*(xm-1); g=gcd(ym,xm-1); yp=ym//g; gp=(xm-1)//g
    return dict(m=m,D=D,yp=yp,gp=gp,h=gp//2 if gp%2==0 else None)
def hm(m):  # NSW numbers h_m for odd m: 1,7,41,239,...  (m=1,3,5,...)
    a,b=1,7
    if m==1: return 1
    for _ in range((m-3)//2): a,b=b,6*b-a
    return b
def frac_c(num,den):  # centred fractional part in (-1/2,1/2]
    r=num%den
    if 2*r>den: r-=den
    return Fr(r,den)
def couplings(m,nu):
    """phase(n)= sum_j k0 n_j^2 + sum_{i<j} kap(j-i) n_i n_j (mod 1) for Z_m(nu)=sum Phihat(n) e(-nu y' Nm(alpha_n)/g')"""
    d=data(m); yp,gp=d['yp'],d['gp']
    k0=frac_c(-nu*yp,gp)
    kap=[None]+[frac_c(-2*nu*yp*xy(k)[0],gp) for k in range(1,m)]
    return k0,kap
