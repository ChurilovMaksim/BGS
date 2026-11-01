"""referee lineN20: Prop F arithmetic + sanity: on U_n corners, |r_A|,|r_B| >= 0.502 (float)."""
import sys, math, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N14/code'); import fastops as F
from flint import arb
d=arb('1.69e-3'); lam=3+2*arb(2).sqrt(); eps=1+arb(2).sqrt()
s=eps/(eps-1); expo=arb('1e10')*arb('1.01e-12')+4260*s*d*d; pref=expo.exp()
dev=pref*(arb('167.214')*s*d+arb('1e10')*arb('6.85e-16')); rlo=1-arb('1.8e-16')-dev
area=2*arb(2).sqrt()*d*d; c=area*rlo**4
print('sum|tau|/delta',s.str(8),'exponent',expo.str(6),'dev',dev.str(6),'|r|lo',rlo.str(6),'const',c.str(6),'ratio const',(c/arb('3.45')**2).str(6),
      'growth',(1/(lam*arb('0.28')**2)).str(8))
for n in range(18,26): print(n,float((c/arb('3.45')**2*(1/(lam*arb('0.28')**2))**n).mid()))
ef=1+2**.5; epf=1-2**.5
for n in (2,4,8):
    for sa in (1,-1):
        for sb in (1,-1):
            a=sa*0.5*1.69e-3*ef**(-2*n); b=sb*0.5*1.69e-3
            tau=[a*ef**k+b*epf**k for k in range(2*n+1)]
            vA=F.Phi.astype(complex); vB=vA.copy()
            for t in range(1,n+1): vA=F.step(vA,tau[2*t]); vB=F.step(vB,-tau[2*t-1])
            print(n,sa,sb,'|rA|',abs(F.psi@vA),'|rB|',abs(F.psi@vB), 'max|tau|',max(map(abs,tau)))
