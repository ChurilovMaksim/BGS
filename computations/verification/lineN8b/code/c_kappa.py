"""N8b [CA arithmetic of implications; inputs labelled]: thresholds of the block-split Bowen method (Prop B1 family).
kappa_s(Lam, R_s) = 3(ln Lam - ln T')/(s ln Lam - ln R_s), valid when kappa_s <= 3/s (s HS blocks of length n=kappa p fit in m=3p);
for iota >= lam^{3p/s} the bound is R_s^{m/s}: needs R_s^{1/s} < T'.
T' = mu* lam^{-1/6}. mu* in [1.9154712, 1.9155] (lower: TRACE-199 certified; upper: input, N-lines numerics).
r2 <= 1.0529012 [CA, N2 Prop E]; Lam_8V <= 1.9656353 [CA, N4]."""
from flint import arb, ctx
ctx.prec=200
lam=arb(3)+2*arb(2).sqrt(); L=lam.log()
mu_lo=arb('1.9154712'); mu_hi=arb('1.9155'); mu=mu_lo.union(mu_hi)
Tp=mu*lam**(arb(-1)/6)
r2=arb('1.0529012'); Lam=arb('1.9656353')
def kap(Lm,R,s,mu_=mu): T=mu_*lam**(arb(-1)/6); return 3*(Lm.log()-T.log())/(s*Lm.log()-R.log())
out=[]
def pr(name,x): s=f"{name}: {x.str(8,radius=False) if hasattr(x,'str') else x}  ball={x}"; print(s); out.append(s)
pr("kappa_2(Lam_8V, r2)  [N7b Prop B1]", kap(Lam,r2,2))
pr("kappa_2(Lam=mu*, r2) [floor of the 2-block method with ANY op-norm rate >= mu*]", (L/2)/(2*mu.log()-r2.log()))
pr("kappa_2(Lam=mu*, r2=1) [H: true r2 >= ~1 (typical HS growth ~1)]", (L/2)/(2*mu.log()))
pr("kappa_2(Lam=mu*, r2=mu*^2/lam) [absolute floor = B3 barrier]", (L/2)/(L))
pr("fixed-point lower bound R_s >= mu*^s/lam, s=2", mu**2/lam)
for s in (3,4,5):
    Rmin=mu**s/lam
    pr(f"s={s}: R_s lower bound mu*^s/lam", Rmin)
    pr(f"s={s}: kappa_s(Lam_8V, R_s=mu*^s/lam)", kap(Lam,Rmin,s))
    pr(f"s={s}: kappa_s(Lam=mu*, R_s=mu*^s/lam)", kap(mu,Rmin,s))
    for kt in ('0.55','0.6','0.65','0.7375915'):
        # R_s needed for kappa_s(Lam_8V)<=kt :  ln R_s <= s ln Lam - 3(ln Lam - ln T')/kt
        Rneed=(s*Lam.log()-3*(Lam.log()-Tp.log())/arb(kt)).exp()
        pr(f"s={s}: R_s needed (Lam_8V) for kappa<={kt}  [and per-step R_s^(1/s)]", Rneed)
    pr(f"s={s}: Jensen lower bound r2^(s/2) (if r2 were =1.0529)", r2**(arb(s)/2))
pr("T'", Tp)
open('logs/c_kappa.out','w').write('\n'.join(out)+'\n')
