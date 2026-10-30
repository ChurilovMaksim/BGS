"""Rigorous final bounds from a certificate JSON (cert.py) for the k1 kick at that eta.
 |Z_L(m)| >= (1-lam^-m) * 1/2 * ( mu_lo^m - 4 T1 r2^(m-1) )                     (E4: truncated alphabet, all odd m)
 |Z(nu*)| >= |Z_L(m)| - (s0^m - (s0-t_L)^m)                                      (E5: physical k1 kick)
 F_m >= |Z(nu*)|^2 / phi(h_m) >= |Z|^2/(h_m - 1);   W~_m >= F_m - 4m   (B^sym<=2m [TRACE-165], |chi|<=1)
 Also verifies exactly (sympy, cyclotomic) |c_a| = 1/2 (a even), 0 (a odd) for kappa in {1,3,5,7}."""
import json, sys
from flint import arb, ctx
import sympy as sp
ctx.prec=256
cf=sys.argv[1]; d=json.load(open(cf)); eta=d['eta']; L=d['L']
assert all(s.get('certified') for s in d['sectors'].values()), 'certificate incomplete'
z=sp.exp(2*sp.pi*sp.I/8)
for kap in (1,3,5,7):
    for a in range(8):
        ca=sp.nsimplify(sp.expand(sum(z**((kap*b*b-a*b)%8) for b in range(8))/8))
        mod2=sp.simplify(sp.expand(ca*sp.conjugate(ca)))
        assert mod2==(sp.Rational(1,4) if a%2==0 else 0), (kap,a,mod2)
s4=d['sectors']['4']
mu_lo=arb(s4['mu_star_abs_lower'])*(1-arb(2)**-50)
T1=arb(d['trace_norm'])*(1+arb(2)**-50); r2=arb(d['r2'])
lam=3+2*arb(2).sqrt(); x=arb(9)/10*arb(str(eta))
Jn=lambda n: abs(x.bessel_j(arb(n)))
N0=60
tail=sum(((x/2)**n/arb.fac_ui(n) for n in range(N0+1,N0+60)),arb(0))*2*(1+arb(2)**-20)   # |J_n(x)|<=(x/2)^n/n!, generous
s0=Jn(0)+2*sum((Jn(n) for n in range(1,N0+1)),arb(0))+tail
tL=2*sum((Jn(n) for n in range(L+1,N0+1)),arb(0))+tail
def hm(m):
    a,b=1,7
    for _ in range((m-3)//2): a,b=b,6*b-a
    return b
rows=[]
for m in range(5,402,2):
    ZL=(1-lam**(-m))*(mu_lo**m-4*T1*r2**(m-1))/2
    Zp=ZL-(s0**m-(s0-tL)**m)
    h=hm(m)
    r=dict(m=m,ZL_lower=float(ZL.lower()),Zphys_lower=float(Zp.lower()))
    if Zp>0:
        F=Zp**2/(h-1); r.update(F_over_2m_lower=float((F/(2*m)).lower()),Wt_over_m_lower=float(((F-4*m)/m).lower()))
    rows.append(r)
good=[r['m'] for r in rows if r['Zphys_lower']>0]; goodL=[r['m'] for r in rows if r['ZL_lower']>0]
out=dict(cert=cf,eta=eta,L=L,s0=float(s0.upper()),tL=float(tL.upper()),mu_lo=float(mu_lo.lower()),T1=float(T1.upper()),
         truncated_valid_from=min(goodL) if goodL else None, phys_valid=[min(good),max(good)] if good else None,rows=rows)
json.dump(out,open(cf.replace('.json','_bounds.json'),'w'),indent=1)
print('eta',eta,'L',L,'s0',out['s0'],'t_L',out['tL'],'mu_lo',out['mu_lo'],'T1',out['T1'])
print('truncated-alphabet bound |Z_L|>0 for all odd m >=',out['truncated_valid_from'],' (and all larger m: the bound is increasing)')
print('physical-kick bound valid for odd m in',out['phys_valid'])
for r in rows:
    if r['m'] in (11,13,15,17,19,21,25,31,41,51,61,71) and 'F_over_2m_lower' in r: print('  m',r['m'],'F/2m >=',f"{r['F_over_2m_lower']:.4g}",'  W~/m >=',f"{r['Wt_over_m_lower']:.4g}")
