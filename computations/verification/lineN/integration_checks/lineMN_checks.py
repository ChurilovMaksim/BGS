"""Integration constant checks for Lines M and N (BGS-TRACE-269..285). Exact integer / Fraction arithmetic where possible,
mpmath (50 digits) for logarithms. Prints one line per check and ALL_OK at the end."""
from fractions import Fraction as F
import json, pathlib, sys
import mpmath as mp
mp.mp.dps = 50
ROOT = pathlib.Path(__file__).resolve().parents[4]
ok = True
def chk(name, cond, val=''):
    global ok
    ok &= bool(cond); print(('OK  ' if cond else 'FAIL'), name, val)
lam = 3 + 2 * mp.sqrt(2); mu_lo = mp.mpf('1.9154712')
# h_m = rational part of (1+sqrt2)^m for odd m (eps^{2m} - 1 = 2 h_m eps^m)
def eps_pow(m):
    a, b = 1, 0
    for _ in range(m):
        a, b = a + 2 * b, a + b
    return a, b
h = {m: eps_pow(m)[0] for m in range(1, 200, 2)}
chk('h_3, h_5, h_7, h_9 = 7, 41, 239, 1393', (h[3], h[5], h[7], h[9]) == (7, 41, 239, 1393))
# M7a: lambda^p = 1 + 2 h_p eps^p in Z[sqrt2], odd p
def mul(x, y): return (x[0]*y[0] + 2*x[1]*y[1], x[0]*y[1] + x[1]*y[0])
good = True
for p in range(1, 120, 2):
    e = eps_pow(p); l = eps_pow(2 * p); r = mul((2 * h[p], 0), e); good &= (l[0] == 1 + r[0] and l[1] == r[1])
chk('M7a lambda^p = 1 + 2 h_p eps^p, odd p < 120', good)
# M1 strong divisibility, odd m, n < 120
from math import gcd
chk('M1 gcd(h_m, h_n) = h_gcd(m,n), odd m, n < 120', all(gcd(h[m], h[n]) == h[gcd(m, n)] for m in range(1, 120, 2) for n in range(1, 120, 2)))
chk('M1/L3 h_3m = h_m (4 h_m^2 + 3), odd m < 60', all(h[3 * m] == h[m] * (4 * h[m] ** 2 + 3) for m in range(1, 60, 2)))
# M3 constants
fl = mu_lo ** 2 / lam ** (mp.mpf(2) / 3)
chk('M3 floor base mu_lo^2/lambda^(2/3) >= 1.13287 (report 1.13288 = rounded)', fl >= mp.mpf('1.13287'), mp.nstr(fl, 8))
chk('M3 margin over D7 1.0184224: >= 1.11238 (report 1.11239 = rounded)', fl / mp.mpf('1.0184224') >= mp.mpf('1.11238'), mp.nstr(fl / mp.mpf('1.0184224'), 8))
chk('M4b growth base mu_lo/lambda^(1/4) = 1.2328', abs(mu_lo / lam ** mp.mpf('0.25') - mp.mpf('1.2328')) < 1e-4, mp.nstr(mu_lo / lam ** mp.mpf('0.25'), 8))
chk('M5 base mu*^2/xi_lo = 1.4923', abs(mu_lo ** 2 / mp.mpf('2.4586893') - mp.mpf('1.4923')) < 1e-4)
# Line N constants from the Line L final constants (delta_F, eps_F)
log_eps = mp.mpf('-12.507')
cN = 9 * log_eps - mp.log10(mp.mpf('17.31'))
chk('W+ log10 c_N = 9 log10 eps_F - log10 17.31 ~ -113.80 (eps_F = 10^-12.507)', abs(cN + mp.mpf('113.80')) < 0.01, mp.nstr(cN, 7))
cross = 3 * (mp.mpf('-25.62') - cN)
chk('W+ beats Weil iff p >= 10^(3 (log c_W - log c_N)) ~ 10^264.5', abs(cross - mp.mpf('264.5')) < 0.1, mp.nstr(cross, 6))
chk('N1.2 4 3^(4/3) < 17.31', 4 * mp.mpf(3) ** (mp.mpf(4) / 3) < mp.mpf('17.31'), mp.nstr(4 * mp.mpf(3) ** (mp.mpf(4) / 3), 8))
chk('N1.2 (2,3) constant 34.62 = 2 * 17.31', F('34.62') == 2 * F('17.31'))
chk('N1.3 Cochrane-Pinner lambda = 2/3^(1/4) in (1.51967, 1.519672) (report 1.51967 = rounded down)', mp.mpf('1.51967') < 2 / mp.mpf(3) ** mp.mpf('0.25') < mp.mpf('1.519672'), mp.nstr(2 / mp.mpf(3) ** mp.mpf('0.25'), 8))
d8V = mp.mpf('0.008107520478707103')
T = (1 - d8V / 2) * mp.mpf('1.28359')
th = (T / mu_lo) ** 30
chk('N3 theta_8V = ((1 - delta/2) 1.28359/mu_lo)^30 in [5.38e-6, 5.4e-6]', mp.mpf('5.38e-6') <= th < mp.mpf('5.4e-6'), mp.nstr(th, 6))
chk('N3 Lean theta8V numerator 1.278387 >= (1 - delta/2) 1.28359', mp.mpf('1.278387') >= T, mp.nstr(T, 10))
chk('N3 thresholds 3 theta/2 ~ 8.1e-6 (rank 3p), theta/2 ~ 2.7e-6 (rank p)', abs(3 * th / 2 - mp.mpf('8.085e-6')) < 1e-8 and abs(th / 2 - mp.mpf('2.695e-6')) < 1e-8)
# N4 index: |det(S^p - 1)| = 4 h_p^2 and 32/8 = 4
def matpow(M, n):
    R = [[1, 0], [0, 1]]
    for _ in range(n):
        R = [[R[0][0]*M[0][0] + R[0][1]*M[1][0], R[0][0]*M[0][1] + R[0][1]*M[1][1]], [R[1][0]*M[0][0] + R[1][1]*M[1][0], R[1][0]*M[0][1] + R[1][1]*M[1][1]]]
    return R
S = [[3, 4], [2, 3]]
dets = all(abs((matpow(S, p)[0][0] - 1) * (matpow(S, p)[1][1] - 1) - matpow(S, p)[0][1] * matpow(S, p)[1][0]) == 4 * h[p] ** 2 for p in range(1, 60, 2))
chk('N4 |det(S^p - 1)| = 4 h_p^2, odd p < 60', dets)
chk('N4 index N(4 sqrt2)/[O^dual : O] = 32/8 = 4', F(32, 8) == 4)
print('ALL_OK' if ok else 'SOME_FAIL'); sys.exit(0 if ok else 1)
