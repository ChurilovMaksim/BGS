# Inclusion threshold for rho=(+-2,8): |Z_rho|^2/d^2 >= 4m for all d<=sqrt(h_m), using the TRACE-199 lower bound
# |Z_rho| >= (1/2)(1-lam^-m)(1.9154712^m - 3012.3) (as registered).  Exact integers via mpmath at 50 digits. [P-arith given TRACE-199]
from mpmath import mp, mpf, sqrt
mp.dps=50
lam=3+2*sqrt(2)
def h(m):  # NSW S_n, n=(m-1)/2 (h_9=1393): S_0=1,S_1=7, S_{n+1}=6S_n-S_{n-1}
    a,b=1,7
    for _ in range((m-1)//2-1): a,b=b,6*b-a
    return b
first=None
for m in range(5,201,2):
    Zlb=(1-lam**(-m))*(mpf('1.9154712')**m-mpf('3012.3'))/2
    ok = Zlb>0 and Zlb**2 >= 4*m*h(m)   # worst case d^2 <= h
    if ok and first is None: first=m
    if not ok: first=None
    if m<=21: print(m,h(m),float(Zlb),bool(ok))
print("m0 (all larger odd m<=199 also ok):",first)
