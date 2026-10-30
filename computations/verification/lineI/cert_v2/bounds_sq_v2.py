"""Line I bounds_sq v2 (Session 4; fixes referee B1 + R1; old cert/bounds_sq.py kept for provenance).
Same chain as v1 (reads cert/data/*.json build info and cert/logs/*_rest.json, read-only), changes:
 * all printed/stored constants are OUTWARD rounded (upper bounds: round up at 4 significant digits; lower: down);
 * table over ALL m ≡ 3 (mod 6) (valid for rho=(±2,8) and every operator case by the exact intertwiners of sym/, Session 4);
 * rigorous tail (R1): for m >= M1 the bound is <= K q^m (e^gamma ln m + 2.50637/lnln h_M1) * 3 with q = R^2/(1+sqrt2), decreasing in m.
"""
import json, sys, math, hashlib, os
from flint import arb, ctx
ctx.prec=128
PAD=1+arb(2)**-40
def U(x): return arb(float(x))*PAD
def up4(x):   # outward (upward) rounding to 4 significant digits of a positive arb
    v=float(x.upper()); e=math.floor(math.log10(v)); s=10**(e-3); r=math.ceil(v/s*(1+1e-15))*s
    assert arb(repr(r))>=x; return float('%.4g'%r) if arb('%.4g'%r)>=x else r
CD='/workspace/bgs-lineI/cert'
cls=['1:3','2:1','0:1','1:2','1:5','0:3','1:0','0:2']
lam=3+2*arb(2).sqrt(); sl=1+arb(2).sqrt()
def lat(typ,c):
    t=c.replace(':','_'); b=json.load(open(f'{CD}/data/{typ}_{t}.json')); r=json.load(open(f'{CD}/logs/{typ}_{t}_rest.json'))
    best=None
    for s in r['scan']:
        if not s.get('certified'): continue
        R=arb(s['R']); SY=U(s['SY_R']); X=U(b['Xnorm']); G=(SY+1/R)*(1+X/R)+1/R
        pert=U(b['delta1'])+U(b['delta2'])+U(b['Delta'])+U(r['epsA'])
        F=pert*G; assert F<1
        C=4*U(b['trace_norm'])*G/(1-F)
        if best is None or float(R.mid())<float(best[0].mid()): best=(R,C,F)
    return best
rows=[(c,lat('V',c),lat('E',c)) for c in cls]
assert all(v is not None and e is not None for _,v,e in rows)
RV=max((r[1][0] for r in rows),key=lambda x:float(x.mid())); CV=rows[0][1][1]
for r in rows: CV=arb.max(CV,r[1][1])
RE=max((r[2][0] for r in rows),key=lambda x:float(x.mid())); CE=rows[0][2][1]
for r in rows: CE=arb.max(CE,r[2][1])
q=RV**2/sl
eg=arb('0.5772156649015328606065120900824024310422').exp(); c2=arb('2.50637')
K=arb(13)/7*48
def hm(m):
    x,y=1,0
    for _ in range(m): x,y=3*x+8*y,x+3*y
    h2=(x-1)//2; h=math.isqrt(h2); assert h*h==h2; return h
def bound(m):
    H=arb(hm(m)); ll=H.log().log(); return K*(CV*RV**m+CE*RE**m)**2*(eg*ll+c2/ll)/H
table={}
for m in range(9,1426,6): table[m]=bound(m)
ok=[m for m in table if table[m]<arb('0.01')]
M0=min(m for m in ok if all(table[n]<arb('0.01') for n in table if n>=m))
# tail m >= M1=1425 (m ≡ 3 mod 6): (CV R^m+CE)^2 <= (CV+CE)^2 R^{2m}; h >= (1+sqrt2)^m/3 (h = ((1+√2)^m+(1-√2)^m)/2);
# lnln h <= ln m (h <= e^m); 1/lnln h <= 1/lnln h_{M1}.  g(m) = q^m (e^g ln m + c) decreasing when ln q + 1/(m ln m) < 0.
M1=1425; llM1=arb(hm(M1)).log().log(); assert arb(hm(M1))>=3
cst=K*(CV+CE)**2*3
gM1=cst*q**M1*(eg*arb(M1).log()+c2/llM1)
assert q.log()+1/(arb(M1)*arb(M1).log())<0
tail_ok=bool(gM1<arb('0.01'))
out=dict(version='bounds_sq v2',code_sha256=hashlib.sha256(open(__file__,'rb').read()).hexdigest(),
  input_sha256={f:hashlib.sha256(open(f'{CD}/{f}','rb').read()).hexdigest() for f in
     [f'logs/{t}_{c.replace(":","_")}_rest.json' for t in 'VE' for c in cls]+[f'data/{t}_{c.replace(":","_")}.json' for t in 'VE' for c in cls]},
  RV=RV.str(10),RE=RE.str(10),CV_exact=CV.str(12,radius=True),CE_exact=CE.str(12,radius=True),CV_up=up4(CV),CE_up=up4(CE),
  q_exact=q.str(12,radius=True),q_up=up4(q),first_m_all_below_0p01=M0,value_at_M0_up=up4(table[M0]),
  tail_M1=M1,tail_bound_at_M1_up=up4(gM1),tail_ok=tail_ok,
  table_up={m:up4(v) for m,v in table.items()})
json.dump(out,open('/workspace/bgs-lineI/cert_v2/logs/bounds_sq_v2.json','w'),indent=1)
for k_ in ['CV_exact','CV_up','CE_exact','CE_up','q_exact','q_up','first_m_all_below_0p01','value_at_M0_up','tail_bound_at_M1_up','tail_ok']: print(k_,out[k_])
print('m=315,321,327:',out['table_up'][315],out['table_up'][321],out['table_up'][327])
