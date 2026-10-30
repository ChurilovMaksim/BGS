import json
from flint import arb, ctx
ctx.prec=200
V=json.load(open('../logs/own_V_eta2.json')); E=json.load(open('../logs/own_E_eta2.json'))
assert all(V['sectors'][a]['certified'] for a in ('4','0','2')) and all(E['sectors'][a]['certified'] for a in ('4','0','2'))
up=lambda x: arb(x)*(1+arb(2)**-50); lo=lambda x: arb(x)*(1-arb(2)**-50)
mu=lo(V['sectors']['4']['lo']); TV=up(V['trace_norm']); TE=up(E['trace_norm']); lam=3+2*arb(2).sqrt()
def h(m):
    a,b=1,0
    for _ in range(m): a,b=a+2*b,a+b
    return a
out=[]
for m in range(13,61,2):
    Z=(1-lam**-m)/2*(mu**m-4*(TV+TE))   # r2=1; sector 6 via reflection lemma (= sector 2)
    if not Z>0: continue
    F=Z**2/(h(m)-1); out.append((m,float((F/(2*m)).lower()),float(((F-4*m)/m).lower())))
print('mu_lo',float(mu.lower()),'TV',float(TV.upper()),'TE',float(TE.upper()),'rate',float((mu**2/lam.sqrt()).lower()))
for r in out[:6]: print(r)
