"""Line F: from the lifted full-alphabet certificates to unconditional lower bounds for the physical k1 kick, all odd m.
 |Z_m(nu*)| >= (1-lam^-m) * 1/2 * ( mu_lo^m - r2^(m-1) * 4 (T_V + T_E) )     (Lidskii + Weyl, |c_a| = 1/2, a even)
 F_m >= |Z_m(nu*)|^2 / phi(h_m) >= |Z|^2/(h_m - 1);  W~rest_m >= F_m - 4m.
 Usage: bounds_lift.py eta certV_a4.json certV_a0.json certV_a2.json certV_a6.json certE.json out.json"""
import sys, json
from flint import arb, ctx
ctx.prec=256
eta=sys.argv[1]; fV4,fV0,fV2,fV6,fE,out=sys.argv[2:8]
V4=json.load(open(fV4)); E=json.load(open(fE)); Vo=[json.load(open(f)) for f in (fV0,fV2,fV6)]
ok = V4['sectors']['4']['certified'] and all(v['sectors'][k]['certified'] for v,k in zip(Vo,('0','2','6'))) and all(E['sectors'][a]['certified'] for a in ('0','2','4','6'))
assert ok, 'not all certified'
r2s={V4['r2']}|{v['r2'] for v in Vo}|{E['r2']}; assert len(r2s)==1
r2=arb(r2s.pop())
pad=lambda x,up: arb(x)*(1+arb(2)**-50) if up else arb(x)*(1-arb(2)**-50)
mu_lo=pad(V4['sectors']['4']['mu_abs_lower'],False)
TV=max(pad(v['trace_norm'],True) for v in [V4]+Vo) if False else pad(max(v['trace_norm'] for v in [V4]+Vo),True)
TE=pad(E['trace_norm'],True)
lam=3+2*arb(2).sqrt()
def pell_h(m):
    x,y=1,0
    for _ in range(m): x,y=3*x+8*y,x+3*y
    D=2*(x-1); import math; h=math.isqrt(D//4); assert 4*h*h==D; return h
res=dict(eta=eta,mu_lo=float(mu_lo.lower()),r2=str(r2),T_V=float(TV.upper()),T_E=float(TE.upper()),rows=[])
m0=None
for m in range(5,201,2):
    Zlo=(1-lam**(-m))/2*(mu_lo**m - r2**(m-1)*4*(TV+TE))
    if not (Zlo>0):
        continue
    if m0 is None: m0=m
    h=pell_h(m); F=Zlo**2/(h-1)
    row=dict(m=m,Z_lower=float(Zlo.lower()),F_over_2m=float((F/(2*m)).lower()),Wrest_over_m=float(((F-4*m)/m).lower()))
    res['rows'].append(row)
res['m0']=m0
g=mu_lo**2/lam.sqrt()
res['growth_per_step_m_plus_2']=float((g**2*arb(199)/201).lower())
# Closed-form all-m bound (referee nit F.7: encoded as assertions, not only prose).
# For odd m >= m1 (m1 = first odd m >= 15 with 1 - 4(T_V+T_E) r2^(m-1)/mu_lo^m > 0):
#   F_m/2m >= C * g^m / m,  C = (1/4)(1-lam^-m1)^2 (1 - 4(T_V+T_E) r2^(m1-1)/mu_lo^m1)^2,  g = mu_lo^2/sqrt(lam),
# because |Z| >= (1/2)(1-lam^-m) mu_lo^m (1 - K r2^(m-1)/mu_lo^m) with both factors increasing in m (r2 < mu_lo),
# F_m >= |Z|^2/(h_m - 1) and 2(h_m - 1) < lam^(m/2) (h_m^2 = (lam^m + lam^-m - 2)/4 < lam^m/4).
# g^m/m is increasing once g^2 m/(m+2) > 1; the bound then tends to infinity because g > 1.
K=4*(TV+TE)
assert r2 < mu_lo
m1=next(m for m in range(15,401,2) if (1-K*r2**(m-1)/mu_lo**m)>0)
C=(1-lam**(-m1))**2*(1-K*r2**(m1-1)/mu_lo**m1)**2/4
assert g>1 and g**2*arb(m1)/(m1+2)>1
for row in res['rows']:
    m=row['m']
    if m<m1: continue
    h=pell_h(m)
    ctx.prec=2048; assert 2*(h-1) < (3+2*arb(2).sqrt())**(arb(m)/2); ctx.prec=256   # margin ~2 at size lam^(m/2)
    cf=C*g**m/m
    assert cf <= arb(row['F_over_2m'])*(1+arb(2)**-40), (m, float(cf.mid()), row['F_over_2m'])
fs=[r['F_over_2m'] for r in res['rows'] if r['m']>=m1]
assert all(x<y for x,y in zip(fs,fs[1:])), 'row bounds not increasing'
res['closed_form']=dict(m_from=m1, C_lower=float(C.lower()), g_lower=float(g.lower()), statement='F_m/2m >= C_lower * g_lower^m / m for all odd m >= m_from (asserted above)')
json.dump(res,open(out,'w'),indent=1)
print('eta',eta,'m0',m0,'mu_lo',res['mu_lo'],'growth(mu^2/sqrt lam)=',float(g.lower()))
for r in res['rows'][:12]: print(r)
print('...',res['rows'][-1])
