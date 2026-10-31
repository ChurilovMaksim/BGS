"""Referee arithmetic checks for N13b/N14b/N14: NSW primality of h_p (proven via FLINT fmpz.is_prime), factorizations,
theta_max, C' ranges, mu*^3/lam, ideal count |N|<2^13 in Z[sqrt2]."""
import json, math
from flint import fmpz
import sympy
mu=1.9154712; lam=3+2*math.sqrt(2); eps=1+math.sqrt(2)
def hp(p):
    x,y=1,1
    for _ in range(p-1): x,y=x+2*y,x+y
    return x
out={}
primes=[p for p in range(3,301) if sympy.isprime(p)]
out['nsw_prime_p_le_300']=[p for p in primes if fmpz(hp(p)).is_prime()]
out['listed']=[5,7,19,29,47,59,163,257]
out['listed_all_prime_proven']=all(fmpz(hp(p)).is_prime() for p in out['listed'])
out['listed_composites_check']={p:bool(fmpz(hp(p)).is_prime()) for p in [11,13,17,23,31,37,41,43,53]}
out['h5,h7']=[hp(5),hp(7)]
out['h31']=hp(31); out['h31_eq']=hp(31)==424577*865087; out['h31_factors_prime']=[fmpz(424577).is_prime(),fmpz(865087).is_prime()]
cB=math.log(1.9656353**3/(1.9656353*1.0529012))/math.log(lam); need=-math.log(eps*(1.2744/mu)**3)
out['cB']=cB; out['need']=need; out['theta_B']=need/(cB*math.log(lam)); out['dmax_base_B']=lam**out['theta_B']; out['dmax_base_A']=1/(eps*(1.2744/mu)**3)
out['cstar']=need/(0.5*math.log(lam)); out['sqrt_h_base']=math.sqrt(eps)
th={}
for p in [q for q in primes if 5<=q<=89]:
    h=hp(p)
    if fmpz(h).is_prime(): continue
    f=sympy.factorint(h); qmin=min(f); th[p]=dict(f={str(k):v for k,v in f.items()},theta=math.log(h//qmin)/(p*math.log(lam)))
out['theta_max']=th
out['mu3_over_lam']=mu**3/lam; out['mu3_over_lam_with_1.9154732']=1.9154732**3/lam
# ideals of norm < 2^13 in Z[sqrt2]: a(n) = sum_{d|n} chi(d), chi = Kronecker (8/.) ... count = sum_{n<N} a(n)
N=2**13
def chi(d): return 0 if d%2==0 else (1 if d%8 in (1,7) else -1)
out['ideal_count_norm_lt_2^13']=sum(sum(chi(d) for d in sympy.divisors(n)) for n in range(1,N))
# mixed weight max at p=11, d=353: 695/7371
out['695/7371']=695/7371; out['2^w*2d/h p11 d353 (w=omega(h/d)=1)']=2*2*353/8119
json.dump(out,open('logs/ref_arith.json','w'),indent=1); print(json.dumps(out,indent=1))
