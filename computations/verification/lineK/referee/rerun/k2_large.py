"""K2: large levels are negligible by positivity.  For d >= L:  Dev_d(rho) >= -n_d |Z_rho|^2/d^2 >= -|Z_rho|^2/d  (n_d <= d).
Sum over included d | h_m, L <= d <= sqrt(h):  Rankin:  sum_{d|h, d>=L} 1/d <= L^{s-1} prod_{q^k||h} (1-q^{-s})^{-1},  0<s<1.
On m = 3p: primes of h are 7 (once, 49 not| h) and q >= 2p+1 (rank p or 3p), at most w = floor(log h/log(2p+1)) of them.
=> sum <= L^{s-1} (1-7^{-s})^{-1} (1-(2p+1)^{-s})^{-w}.   We find the least L = l^m with
   S_Z * mu^{2m} * bound <= eps * (K_min/2) * xi_lo^m,  S_Z := sum_rho C_rho^2 (|Z_rho| <= C_rho mu^m), eps = 0.01,
and compare l with sqrt(h)^{1/m}.  All in arb (upper bounds rounded up)."""
import json, math
from flint import arb, ctx
ctx.prec=120
mu=arb('1.9154753'); xi=arb('2.4586893'); Kmin=arb('0.009985'); eps=arb('0.01')
lam=arb(3)+2*arb(2).sqrt(); eps1=1+arb(2).sqrt()
def logh_up(m): return (m*eps1.log()).upper()  # h_m <= eps1^m (h=(e^m+e^-m)/2 < e^m for m>=1 odd)
def run(m,SZ):
    p=m//3; logh=arb(logh_up(m)); w=int(math.floor(float((logh/arb(2*p+1).log()).upper())))
    target=(eps*Kmin/2*xi**m/(SZ*mu**(2*m))).log()   # need log(bound) <= target
    best=None
    for k in range(1,400):
        s=arb(k)/400
        E=-(1-arb(7)**(-s)).log() - w*(1-arb(2*p+1)**(-s)).log()
        # log bound = (s-1) log L + E <= target  <=>  log L >= (E-target)/(1-s)
        logL=(E-target)/(1-s)
        if best is None or float(logL.upper())<best[0]: best=(float(logL.upper()),float(s))
    l=math.exp(best[0]/m); lsqrt=math.exp(float(logh.lower())/(2*m))*2**(-0.5/m)
    return dict(m=m,p=p,w=w,s=best[1],l=l,sqrt_h_rate=lsqrt,eta=math.log(l)/math.log(float(mu*mu/xi))-1,nontrivial=l<lsqrt)
out=[]
for SZ in ['1e8','1e14']:
    for p in [167,331,1009,10007,100003,1000003,10**7+19]:
        r=run(3*p,arb(SZ)); r['S_Z']=SZ; out.append(r); print(r,flush=True)
print('mu^2/xi =',float((mu*mu/xi).upper()))
json.dump(out,open('logs/k2_large.json','w'),indent=1)
# crossover: least tested p (geometric grid) with l < sqrt(h) rate
cross=None
p=10**7
while p<10**12:
    r=run(3*p,arb('1e14'))
    if r['nontrivial']: cross=r; break
    p=int(p*1.5)
print('first nontrivial (grid, S_Z=1e14):',cross)
json.dump(dict(table=out,crossover=cross),open('logs/k2_large.json','w'),indent=1)
