# independent crossover check (referee lineN21): mpmath 60 digits, exact K_p = 4 h_p^2 + 3, h_p = sinh(p ln eps) via recurrence
import mpmath as mp, json
from sympy import primerange, isprime
mp.mp.dps=60
R=mp.mpf('6.234e-4'); gam=mp.euler; lne=mp.log(1+mp.sqrt(2))
def run(dl):
    lnb=mp.log1p(R)-mp.mpf(dl)
    G=lambda p:(2*mp.exp(p*lnb)-1)**2-1
    rob=lambda L: mp.e**gam*mp.log(L)+mp.mpf('0.6483')/mp.log(L)-1
    env=lambda p: rob((2*p+1)*lne)
    hs={}; a,b=1,7  # h_1=1,h_3=7, h_{p+2}=6h_p-h_{p-2}
    p=3; hs[1]=1; hs[3]=7
    while p<5100: a,b=b,6*b-a; p+=2; hs[p]=b
    lnK=lambda p: mp.log(4*mp.mpf(hs[p])**2+3)
    # check h_p = sinh(p ln eps) for a few p
    for q in (5,7,101): assert abs(mp.log(hs[q])-mp.log(mp.sinh(q*lne)))<1e-40
    fi=next(p for p in range(1000,6000) if G(p)>env(p))
    fo=next(p for p in range(1001,6000,2) if G(p)>rob(lnK(p)))
    fp=next(p for p in primerange(1000,6000) if G(p)>rob(lnK(p)))
    viol=[p for p in primerange(fp,5001) if not G(p)>rob(lnK(p))]
    x=mp.exp(fi*lnb); Gd=4*x*(2*x-1)*lnb; Ed=2*mp.e**gam/(2*fi+1)
    return dict(dl=dl,first_int_env=fi,margin_env=float(G(fi)-env(fi)),prev_int_margin=float(G(fi-1)-env(fi-1)),first_odd_exact=fo,first_prime=fp,
                viol=viol,G1399=float(G(1399)),rob1399=float(rob(lnK(1399))),Gprime=float(Gd),envprime=float(Ed))
out=[run(d) for d in ('5.0313e-6','6.29e-6','6.3e-6','7.0944e-6','7.0944e-6')]
print(json.dumps(out,indent=1)); json.dump(out,open('../logs/ref_crossover21b.json','w'),indent=1)
