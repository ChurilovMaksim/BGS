"""N7b [CA]: constants of Proposition B1 (block-split Bowen bound) in arb.
Inputs (all upper bounds unless noted): Lambda_8V <= 1.9656353 (N4 [CA]), r2_8V(4000) <= 1.0529012 (N2 Prop E [CA]),
mu* >= 1.9154712 (Line F [CA], lower), lam = 3+2sqrt2.  Target T' = mu*_lo lam^(-1/6) (lower bound of the family rate).
kappa = 3 (ln Lam - ln T')/(2 ln Lam - ln r2): pattern (c, a) handled iff iota = c^2/N(a) >= lam^{(kappa+eta) p}.
kappa is increasing in Lam and r2 (d/dLam ∝ 2lnT'-ln r2 > 0 checked), so upper inputs give a valid (larger) kappa."""
from flint import arb, ctx
ctx.prec=200
lam=3+2*arb(2).sqrt(); L=lam.log()
Lam=arb('1.9656353'); r2=arb('1.0529012'); mu=arb('1.9154712')
T=mu*lam**(-arb(1)/6)
lT=T.log(); lL=Lam.log(); lr=r2.log()
assert (2*lT-lr)>0
kappa=3*(lL-lT)/(2*lL-lr)
print('T_prime lower =',T.lower())
print('kappa_8V (iota exponent, units of p) <=',kappa.upper())
print('unit patterns: c >= lam^{kappa/2 p}, kappa/2 <=',(kappa/2).upper())
print('as fraction of log_lam h_p ~ p/2: c >= h_p^{kappa}, kappa <=',kappa.upper())
# naive alternative: Theorem C periodic form (op on one winding, HS^2 on p steps, Bowen at n=p): loss (h_p/c)^2 per m
naive=3*(lT-((Lam*r2).log()/3))/(2)   # (h_p/c)^{2/(3p)} < T'/(Lam r2)^{1/3}  ->  log_lam(h_p/c) < 1.5 p ln(T'/(Lam r2)^{1/3})/ln lam
print('Theorem-C-with-index-loss threshold: log_lam(h_p/c) <',( (arb(3)/2)*(lT-(Lam*r2).log()/3)/L ).lower(),'* p')
print('B1 threshold for units at c|h_p: log_lam(h_p/c) <',(arb(1)/2-kappa/2).lower(),'* p (using h_p<=lam^{p/2})')
# E families: sup bound
for nm,LE,Tt in (('8E',arb('0.4915932'),T),):
    print(nm,'sup-bound rate',LE,'< target',T.lower(),bool(LE<T))
# barrier of any Bowen/Lebesgue majorant: needs iota > lam^{m/6}*(mu*/T')^{...}: iota^{1/m} > mu*/T' = lam^{1/6}
print('Bowen-Lebesgue barrier: iota >= lam^{p/2} (=4 h_p^2/h_p ... fully isotropic at c<=h_p has iota=c<=h_p<lam^{p/2}/2)')
# J-moment heuristic thresholds (slow-point lower bounds r_J >= mu*^J/lam): n > 3p (lnLam-lnT')/(J lnLam - ln r_J)
for J in (2,4,6,10):
    rJ = r2 if J==2 else mu**J/lam
    print('J',J,'threshold n/p >',(3*(lL-lT)/(J*lL-rJ.log())).mid() if J>2 else kappa.mid(), '(J>2: optimistic, r_J at its slow-point lower bound)')
