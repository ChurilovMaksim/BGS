"""Line H, H2: all-m consequence for the REAL Line B kick f_B (eta=2), 49-state lift, s=-1, odd m with 3 does not divide m (nu* per TRACE-194/195).
 Z_m = (1-lam^-m) sum_{b in 0,2,4,6} c_b (Tr V_b^m - Tr E_b^m), |c_b| = 1/2   (Line F, F1 lifted identity; 49-state version).
 V_0: exactly one eigenvalue mu outside |z|=R0 (rig_spec dom, Riesz homotopy), |mu| >= mu_lo.  Every other operator L in {V_2,V_4,V_6,E_0..E_6}:
 spectrum in |z| < R_L (rig_spec rest).  Lidskii + Weyl: sum_{k != *} |mu_k|^m <= R^(m-1) ||L||_1.
 => |Z_m| >= (1-lam^-m)/2 * ( mu_lo^m - R0^(m-1) T_V - sum_{b=2,4,6} R_Vb^(m-1) T_V - sum_b R_Eb^(m-1) T_E ).
 F_m >= |Z_m|^2/phi(h_m) >= |Z_m|^2/(h_m - 1);  W~rest_m >= F_m - 4m (TRACE-165, TRACE-170) -- cited from Line F F3.
 Rounding: all floats read from JSON are padded by a relative 2^-40 in the safe direction; arb at 256 bits.
 Usage: bounds49.py dom.json buildV.json restV2 restV4 restV6 buildE.json restE0 restE2 restE4 restE6 out.json"""
import sys, json, math, hashlib
from flint import arb, ctx
ctx.prec=256
a=sys.argv[1:]
d0=json.load(open(a[0])); bV=json.load(open(a[1])); rV=[json.load(open(f)) for f in a[2:5]]; bE=json.load(open(a[5])); rE=[json.load(open(f)) for f in a[6:10]]; out=a[10]
for r,(pre,sec) in zip(rV+rE,[('V',2),('V',4),('V',6),('E',0),('E',2),('E',4),('E',6)]):
    assert r['mode']=='rest' and r['sector']==sec and ('prodE' if pre=='E' else 'prodV') in r['prefix'], (r['prefix'],r['sector'])
assert d0['mode']=='dom' and d0['sector']==0
for b_ in (bV,bE): assert b_['s']==-1 and b_['eta']=='2'
up=lambda x: arb(x)*(1+arb(2)**-40); lo=lambda x: arb(x)*(1-arb(2)**-40)
fu=lambda x: math.nextafter(float(x.upper()),math.inf); fl=lambda x: math.nextafter(float(x.lower()),-math.inf)
def floor2(x):   # 2 significant digits, rounded DOWN (safe for lower bounds), as a string
    v=fl(x); e=math.floor(math.log10(v)); q=math.floor(v/10**(e-1))
    while q*10**(e-1)>v: q-=1
    return f'{q/10:.1f}e{e}' if e>=4 else str(q*10**(e-1))
def certs(r): return [o for o in r['scan'] if o.get('certified')]
assert certs(d0) and all(certs(r) for r in rV+rE), 'not all certified'
Rr=[min(arb(o['R']) for o in certs(r)) for r in rV+rE]     # R strings are exact decimals -> arb exact enough (contour radius used in certificate)
TV=up(bV['trace_norm']); TE=up(bE['trace_norm'])
lam=3+2*arb(2).sqrt()
def pell_h(m):
    x,y=1,0
    for _ in range(m): x,y=3*x+8*y,x+3*y
    D=2*(x-1); h=math.isqrt(D//4); assert 4*h*h==D; return h
def Zlow(m,mu_lo,R0):
    S=mu_lo**m - R0**(m-1)*TV - sum((Rr[i]**(m-1)*TV for i in range(3)),arb(0)) - sum((Rr[i]**(m-1)*TE for i in range(3,7)),arb(0))
    return (1-lam**(-m))/2*S
def first_m(o):
    mu_lo=lo(o['mu_abs_lower']); R0=arb(o['R'])
    for m in range(5,4001,2):
        if m%3 and Zlow(m,mu_lo,R0)>0: return m
    return 10**9
ob=min(certs(d0),key=lambda o:(first_m(o),-o['mu_abs_lower']))
mu_lo=lo(ob['mu_abs_lower']); R0=arb(ob['R'])
res=dict(version='bounds49 v3 (referee fixes 3/4)',inputs={f:hashlib.sha256(open(f,'rb').read()).hexdigest() for f in a[:10]},code_sha256=hashlib.sha256(open(__file__,'rb').read()).hexdigest(),dom_choice=ob,mu_lo=fl(mu_lo),R0=ob['R'],R_rest=[fu(x) for x in Rr],T_V=fu(TV),T_E=fu(TE),rows=[])
m0=None; prev=None
for m in range(5,601,2):
    if m%3==0: continue
    Zlo=Zlow(m,mu_lo,R0)
    if not (Zlo>0):
        assert m0 is None, 'non-monotone'; continue
    if m0 is None: m0=m
    h=pell_h(m); F=Zlo**2/(h-1)
    Fo=F/(2*m); Wo=(F-4*m)/m
    if prev is not None: assert Fo>prev[0] and Wo>prev[1], 'rows not increasing'
    prev=(Fo,Wo)
    row=dict(m=m,Z_lower=fl(Zlo),F_over_2m=fl(Fo),Wrest_over_m=fl(Wo),F_over_2m_safe2=floor2(Fo),Wrest_over_m_safe2=floor2(Wo))
    res['rows'].append(row)
res['m0']=m0
# all m >= M (closed form): 2(h_m-1) < lam^(m/2) (h_m^2 ~ lam^m/32), Zlo >= (1-lam^-m)/2 mu_lo^m (1-eps_M) with eps_m decreasing in m (each ratio R/mu_lo<1)
M=599
eps=(R0**(M-1)*TV+sum((Rr[i]**(M-1)*TV for i in range(3)),arb(0))+sum((Rr[i]**(M-1)*TE for i in range(3,7)),arb(0)))/mu_lo**M
assert all(x<mu_lo for x in Rr) and R0<mu_lo and eps<1
g=mu_lo**2/lam.sqrt()
C=(1-lam**(-M))**2*(1-eps)**2/4   # F_m/2m >= Zlo^2/(2m(h_m-1)), h_m-1 < lam^(m/2)/2, Zlo >= (1-lam^-M)/2 mu^m (1-eps_M)
assert g>1 and arb(M)*g.log()>1
assert C>arb('0.2499')
res['tail']=dict(M=M,eps_M=fu(eps),growth_mu2_over_sqrtlam=fl(g),C_lower_str=C.str(20,radius=True),C_ge='0.2499',
   statement='for odd m>=M with 3 not| m: F_m/2m >= C g^m/m (g=mu_lo^2/sqrt(lam)>1), increasing in m -> infinity; m<M covered by rows')
json.dump(res,open(out,'w'),indent=1)
print('m0',m0,'minWrest/m',res['rows'][0]['Wrest_over_m_safe2'],'mu_lo',res['mu_lo'],'R0',res['R0'],'Rrest',res['R_rest'],'TV',res['T_V'],'TE',res['T_E'],'growth',float(g.lower()))
for r in res['rows'][:12]: print(r)
print('...',res['rows'][-1])
