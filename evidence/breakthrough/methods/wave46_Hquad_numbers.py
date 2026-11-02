"""Wave 46, task 8: closed-form predictions for H-quad/H-diff coefficients.

alpha^m = A + B*sqrt(2).  nu = (alpha^m - 1)/27 = (a, b) with
a = (A-1)/27, b = B/27.  Derived (see note):
  nu_0 = Tr(nu) = 2a,  nu_1 = Tr(sqrt2*nu) = 4b
  mu_0 = Tr(abar*nu) = 6a - 8b,  mu_1 = Tr(sqrt2*abar*nu) = 12b - 8a
  tau_0 = Tr(alpha^(m-1)) = 2*A_{m-1}, tau_1 = 4*B_{m-1}
  u = (D_m // 729) mod 729
Predictions mod 27 (uinv2 = u^-2 mod 27):
  a_pred = (-4*mu_0 + 2*nu_0*tau_0)*uinv2
  b_pred = 2*nu_1*tau_1*uinv2
  c_pred = (-4*mu_1 + 2*nu_0*tau_1 + 2*nu_1*tau_0)*uinv2   (expect 0)
  d_pred(xbar) = -6*mu_0*xbar*uinv2
  e_pred(ybar) = 3*nu_1*tau_1*ybar*uinv2
  eps_pred = (u^-1 * tau_1 * nu_1) mod 3  -> +1 if 1, -1 if 2
Check against wave-45 fits: m=180 (a,b,c,d)=(19,16,0,21);
m=252 k=20 (a,b,c,d,e,f)=(17,20,0,6,6,23); eps: 180 -> +1, 252 -> -1.
"""
from math import gcd

def AB(m):
    A, B = 1, 0
    for _ in range(m):
        A, B = 3*A + 4*B, 2*A + 3*B
    return A, B

def v3(n):
    c = 0
    while n % 3 == 0:
        n //= 3; c += 1
    return c

def report(m):
    A, B = AB(m)
    Am1, Bm1 = AB(m-1)
    D = 2*(A-1)
    assert (A-1) % 27 == 0 and B % 27 == 0, (m, (A-1) % 27, B % 27)
    a, b = (A-1)//27, B//27
    nu_0, nu_1 = 2*a, 4*b
    mu_0, mu_1 = 6*a - 8*b, 12*b - 8*a
    tau_0, tau_1 = 2*Am1, 4*Bm1
    u = (D//729) % 729
    assert gcd(u, 3) == 1
    uinv2 = pow(u % 27, -2, 27)
    uinv = pow(u % 3, -1, 3)
    a_pred = ((-4*mu_0 + 2*nu_0*tau_0)*uinv2) % 27
    b_pred = ((2*nu_1*tau_1)*uinv2) % 27
    c_pred = ((-4*mu_1 + 2*nu_0*tau_1 + 2*nu_1*tau_0)*uinv2) % 27
    d_pred = ((-6*mu_0*14)*uinv2) % 27
    e_pred = ((3*nu_1*tau_1*20)*uinv2) % 27
    eps = (uinv*(tau_1 % 3)*(nu_1 % 3)) % 3
    print(f"m={m}: v3(D)={v3(D)} v3(B)={v3(B)} nu_0%27={nu_0%27} "
          f"mu_0%3={mu_0%3} nu_1%3={nu_1%3} tau_0%27={tau_0%27} tau_1%27={tau_1%27}")
    print(f"   a={a_pred} b={b_pred} c={c_pred} d(14)={d_pred} e(20)={e_pred} "
          f"eps={'+1' if eps==1 else '-1'}  a%3={a_pred%3} b%3={b_pred%3}")

for m in [36, 72, 144, 180, 252, 45, 90]:
    report(m)
print("fits to match: m=180 (19,16,0,21) eps +1; m=252 (17,20,0,6,6,23) eps -1")
