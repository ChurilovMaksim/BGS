"""lineN16 referee: N18b crossover with the CORRECT Robin form.  Robin 1984 Thm 2: sigma(n)/n < e^gamma lnln n + 0.6483/lnln n (n>=3).
With L = ln K_p:  I_p <= rho(L) := e^gamma ln L + 0.6483/ln L - 1.   (N18b a_crossover_v2.py uses 0.6483/L -- wrong variable.)
Gas: G(p) = (2 b^p - 1)^2 - 1, ln b = ln(1+R) - delta, R = 6.234e-4.  Exact K_p via big ints (mpmath 50 digits for ln)."""
import math, json, mpmath as mp
mp.mp.dps=50
gam=mp.euler; R=mp.mpf('6.234e-4'); lne=mp.log(1+mp.sqrt(2))
def h(p):
    a,b=1,7
    for _ in range((p-1)//2-1): a,b=b,6*b-a
    return b
def rho(L): return mp.e**gam*mp.log(L)+mp.mpf('0.6483')/mp.log(L)-1
def rho_wrong(L): return mp.e**gam*mp.log(L)+mp.mpf('0.6483')/L-1
def isprime(n):
    if n<2: return False
    i=2
    while i*i<=n:
        if n%i==0: return False
        i+=1
    return True
out={}
for dl in ('5.14476e-7','2.470e-6'):
    lnb=mp.log1p(R)-mp.mpf(dl)
    G=lambda p:(2*mp.e**(p*lnb)-1)**2-1
    lnK=lambda p: mp.log(4*h(p)**2+3)
    env=lambda p: rho((2*p+1)*lne)
    fi_env=next(p for p in range(1200,3000) if G(p)>env(p))
    fi_exact=next(p for p in range(1201,3000,2) if G(p)>rho(lnK(p)))     # odd p
    fp_exact=next(p for p in range(1201,3000,2) if isprime(p) and G(p)>rho(lnK(p)))
    fp_env=next(p for p in range(1201,3000,2) if isprime(p) and G(p)>env(p))
    viol=[p for p in range(fp_exact,5001,2) if isprime(p) and not G(p)>rho(lnK(p))]
    x=mp.e**(fi_env*lnb); Gd=4*x*(2*x-1)*lnb; Ed=2*mp.e**gam/(2*fi_env+1)
    out[dl]=dict(first_int_env=fi_env,first_odd_exact=fi_exact,first_prime_exact=fp_exact,first_prime_env=fp_env,viol_primes_to_5000=viol,
      margin_env_at_first=float(G(fi_env)-env(fi_env)),margin_exact_1399=float(G(1399)-rho(lnK(1399))),margin_env_1399=float(G(1399)-env(1399)),
      G1289=float(G(1289)),robin_exact_1289=float(rho(lnK(1289))),robin_wrongform_1289=float(rho_wrong(lnK(1289))),
      Gprime_at=float(Gd),envprime_upper=float(Ed))
    print(dl,out[dl],flush=True)
json.dump(out,open('/workspace/audit/lineN16/logs/ref_crossover.json','w'),indent=1)
