"""Auditor's independent recomputation of the E4/E5 arithmetic (arb), from the certified constants in the author's cert JSON
(mu_lo, T1, r2), plus true-value comparison (auditor's transfer operator numerics) and exact phi(h_m)."""
import sys,json,math; sys.path.insert(0,'.')
from flint import arb, ctx
import sympy as sp, numpy as np
from aud import data, ghat, K1
from tmop import spectra, Zpred
ctx.prec=300
cf=sys.argv[1]; d=json.load(open(cf)); eta=d['eta']; L=d['L']
s4=d['sectors']['4']; assert all(v['certified'] for v in d['sectors'].values())
mu_lo=arb(s4['mu_star_abs_lower']); T1=arb(d['trace_norm']); r2=arb(d['r2'])
# float->arb: the stored floats are round-to-nearest of arb endpoints; pad by 2 ulp
mu_lo=mu_lo*(1-arb(2)**-51); T1=T1*(1+arb(2)**-51)
lam=3+2*arb(2).sqrt(); x=arb(9)/10*arb(str(eta))
# s0 = sum_n |J_n(x)| : terms n<=80 with arb Bessel, tail n>80 bounded by 2*sum (x/2)^n/n! <= 2*(x/2)^81/81! * 2
J=lambda n: abs(x.bessel_j(arb(n)))
tail=2*2*(x/2)**81/arb.fac_ui(81)
s0=J(0)+2*sum((J(n) for n in range(1,81)),arb(0))+tail
tL=2*sum((J(n) for n in range(L+1,81)),arb(0))+tail
G=ghat(K1,float(eta)); SPL=spectra(G,L,2.0,120); SPF=spectra(G,10,2.6,140)
print(f'eta={eta} L={L} s0={s0} tL={tL} mu_lo={mu_lo.lower()} T1={T1.upper()} r2={r2}')
auth={r['m']:r for r in json.load(open(cf.replace('.json','_bounds.json')))['rows']}
for m in range(13,43,2):
    h=data(m)['h']; ph=int(sp.totient(h)) if m<=41 else None
    ZL=(1-lam**(-m))*(mu_lo**m-4*T1*r2**(m-1))/2
    Zp=ZL-(s0**m-(s0-tL)**m)
    trueZL=abs(Zpred(m,SPL)); trueZ=abs(Zpred(m,SPF))
    line=f'm={m:2d} ZL>={float(ZL.lower()):.6g} (true~{trueZL:.6g}) Zphys>={float(Zp.lower()):.6g} (true~{trueZ:.6g})'
    a=auth.get(m,{})
    if Zp>0:
        Fb=Zp**2/(h-1); Fb2=Zp**2/ph
        line+=f' F/2m>={float((Fb/(2*m)).lower()):.5g} [author {a.get("F_over_2m_lower",float("nan")):.5g}] (with exact phi: {float((Fb2/(2*m)).lower()):.5g}; true-ish |Z*|^2/phi/2m={trueZ**2/ph/(2*m):.5g})'
    else: line+=f' [author Zphys_lower {a.get("Zphys_lower",float("nan")):.4g}]'
    print(line,flush=True)
