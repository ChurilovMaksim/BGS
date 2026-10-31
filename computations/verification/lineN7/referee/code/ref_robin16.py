"""Referee: recompute the Theorem-16 cost ratio  2 C16^2 1.6355^{2m} (e^g lnln h_m + 0.6483/lnln h_m) / (0.01 * 2.06e-3 p |Z8|^2 / h_p)
with |Z8| >= 0.5(1-lam^-m)(mu^m - 3012.3), h_m = x_m(eps^m), and the m>=51 claim  2 C16^2 1.6355^{2m} <= 2|Z8|^2 (i.e. 4|Z8|^2 total)."""
import mpmath as mp, json
mp.mp.dps=60
eps=1+mp.sqrt(2); L=eps**2; MU=mp.mpf('1.9154712'); C=mp.mpf('2.273e5'); r=mp.mpf('1.6355'); g=mp.euler
def x(n): return mp.nint((eps**n+(-1/eps)**n)/2)
def Z8lo(m): return mp.mpf('0.5')*(1-L**(-m))*(MU**m-mp.mpf('3012.3'))
out={}
# m threshold for sum_rho |Z_rho|^2 <= 4|Z8|^2 : need 2*(C r^m)^2 <= 2*Z8lo^2  (two (+-2,8) with |Z8| each, two (+-2,16))
m=1
while not (C*r**m <= Z8lo(m) and all(C*r**mm<=Z8lo(mm) for mm in range(m,m+200))): m+=1
out['m1']=m
def ratio(p):
    m=3*p; hm=x(m); hp=x(p); ll=mp.log(mp.log(hm))
    cost=2*C**2*r**(2*m)*(mp.e**g*ll+mp.mpf('0.6483')/ll)
    return cost/(mp.mpf('0.01')*mp.mpf('2.06e-3')*p*Z8lo(m)**2/hp)
rows={p:float(ratio(p)) for p in (300,330,335,337,338,339,340,400,537,1000,1165)}
out['ratio']=rows
first=None
for p in range(200,2000):
    if all(ratio(pp)<=1 for pp in (p,)) and first is None: first=p
out['first_p_ratio_le_1']=first
out['monotone_after_first']=all(ratio(p+1)<ratio(p) for p in range(first,first+400))
print(json.dumps(out,indent=1)); json.dump(out,open('logs/ref_robin16.json','w'),indent=1)
