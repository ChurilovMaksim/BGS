# M-F1: certified inclusion threshold for (+-2,8) using Line F F3 lower bound |Z| >= 1/2 (1-lam^-m)(mu_lo^m - 3012.4).
# Exact rational/bigint comparison via mpmath at high precision (outward safety: mu_lo rounded down).
from mpmath import mp, mpf, sqrt, log
mp.dps=60
mu_lo=mpf('1.9154712'); lam=3+2*sqrt(2)
def mul(a,b): return (a[0]*b[0]+2*a[1]*b[1], a[0]*b[1]+a[1]*b[0])
fails=[];first=None
hx=(1,1); sq=mul((1,1),(1,1))
m=1
while m<=20001:
    if m>=9:
        Zlo=mpf(1)/2*(1-lam**(-m))*(mu_lo**m-mpf('3012.4'))
        ok = Zlo>0 and Zlo**2 >= 4*m*hx[0]
        if not ok: fails.append(m)
        elif first is None: first=m
    hx=mul(hx,sq); m+=2
print("certified: |Z|^2>=4mh holds for odd m in [first, 20001]; first =",first,"; failures >= first:",[f for f in fails if f>first])
print("odd m <",first,"where certified bound does not suffice:",fails)
print("monotone beyond: ratio ~ (mu/lam^(1/4))^m/sqrt(m), base",mu_lo/lam**0.25)
print("float (Line G growth_law, referee): m=11 ratio 1.13, m=13 ratio 2.22 -> [N] at m=11,13")
