# V5 copy of N19b/code/a_crossover_v3.py (identical logic; output path -> V5/logs). usage: crossover_v5.py delta_eff
# N19b (R1 fix of N18b a_crossover_v2.py); B2 [P-arith, float + monotonicity]: correct gas form G(p) = (2 b^p - 1)^2 - 1, b = (1+R) e^{-delta},
# R = Re Lambda_lo' = 6.234e-4 (lower bound), delta = delta_int = 5.14476e-7 (upper bound).  vs Robin bound on I_p
# with exact K_p = h_{3p}/h_p = 4 h_p^2 + 3 (big ints), and an envelope g(p) >= Robin(K_p) for the tail p > scan.
import math, json
from sympy import primerange
import sys
R=6.234e-4; dl=float(sys.argv[1]) if len(sys.argv)>1 else 5.14476e-7; gam=0.5772156649015329; lne=math.log(1+math.sqrt(2))
lnb=math.log1p(R)-dl                      # ln b ; (1+R)e^{-delta}
a_low=math.floor((math.exp(lnb)-1)*1e9)/1e9   # lower bound for a := b-1, rounded DOWN
def G(p): x=math.exp(p*lnb); return (2*x-1)**2-1
def robin(L): return math.exp(gam)*math.log(L)+0.6483/math.log(L)-1   # L = ln K; Robin Thm 2: 0.6483/ln ln K (N19b fix R1)
def h(p):
    a,b=1,7
    for _ in range((p-1)//2-1): a,b=b,6*b-a
    return b
def lnK(p):
    K=4*h(p)**2+3; return math.log(K)   # exact big int; math.log handles big ints
def env(p): return robin((2*p+1)*lne)   # ln K_p <= (2p+1) ln eps  (K_p <= (eps^p+1)^2+3 <= eps^{2p+1}, p>=2); robin increasing in L > e^{0.6033} ~ 1.83
assert all(lnK(p) <= (2*p+1)*lne for p in [5,7,11,13,101,1009,1399])
out=dict(a_low=a_low, lnb=lnb)
# (1) all integers p (real-variable form, envelope) and exact primes in [1289, 5000]
first_int=next(p for p in range(1000,6000) if G(p)>env(p))
first_prime_exact=next(p for p in primerange(1000,6000) if G(p)>robin(lnK(p)))
first_prime_env=next(p for p in primerange(1000,6000) if G(p)>env(p))
viol=[p for p in primerange(first_prime_exact,5001) if not G(p)>robin(lnK(p))]
out.update(first_int_envelope=first_int, first_prime_exact=first_prime_exact, first_prime_envelope=first_prime_env, violations_exact_primes_to_5000=viol,
           at1289=[G(1289),robin(lnK(1289))], at1386=[G(1386),env(1386)], at1399=[G(1399),robin(lnK(1399))])
# (2) monotonicity for p >= p*: G'(p) = 4x(2x-1) lnb with x=b^p increasing; env'(p) = e^gam*2/(2p+1) - (0.6483/L^2)*2 lne <= e^gam*2/(2p+1)
ps=first_int
Gd=4*math.exp(ps*lnb)*(2*math.exp(ps*lnb)-1)*lnb; Ed=math.exp(gam)*2/(2*ps+1)
out.update(mono_at=ps, Gprime_lower=Gd, envprime_upper=Ed, mono_ok=Gd>Ed)
print(json.dumps(out,indent=1)); json.dump(out,open(f'/workspace/bgs-lineN/V5/logs/crossover_v5_d{dl:.6e}.json','w'),indent=1)
