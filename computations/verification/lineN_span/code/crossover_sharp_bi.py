#!/usr/bin/env python3
"""Sharp-span Prop. K fixed point, v5 crossover, J0 = 13/14 rows and Lemma BI numerics (mpmath dps 40).

Independent referee implementation (audit of PR #83, 4 Nov 2026), moved to repository paths.
[P-arith] layer as in V5: idealised additive terms (tails = Y = X_cross = eps = 0, n/h_p := 1),
delta_true = 5.0313e-6, Re Lambda_lo' = 6.234e-4, g0 = 4. Every row is CONDITIONAL on H1-bad
(BGS-TRACE-336) through C; the BI rows are in addition conditional on hypothesis (M) and the
unproved per-site / factor-2 normalisation of A_M (see BGS-TRACE-340).
Inputs: lineN15/logs/a_cert3.jsonl (j <= 12), N20 a_cert_ext*.jsonl (j = 13, 14), spans from
logs/span_census_J16.jsonl (run span_census.py 16 first).
Output: computations/verification/lineN_span/logs/crossover_sharp_bi.json
"""
import pathlib
ROOT = pathlib.Path(__file__).resolve().parents[4]
LOG = ROOT / 'computations/verification/lineN_span/logs'
import json, mpmath as mp
mp.mp.dps=40
R=mp.mpf('6.234e-4'); DT=mp.mpf('5.0313e-6'); g0=4; J0=12
lam=3+2*mp.sqrt(2); eps=1+mp.sqrt(2); theta=mp.log(2)/mp.log(eps)
beta=2*mp.log(1/mp.mpf('0.28'))/mp.log(lam); q=mp.power(2,mp.mpf(1.5)*(1-beta))
span={(r['a'],r['b']):r['span'] for r in map(json.loads,open(LOG / 'span_census_J16.jsonl'))}
MODEL={(1,0),(0,1),(2,0),(0,2)}
rows=[]
for r in map(json.loads,open(ROOT / 'computations/verification/lineN15/logs/a_cert3.jsonl')):
    ab=(r['a'],r['b'])
    if r['j']>J0 or ab in MODEL or r['zr']>=g0: continue
    rows.append((mp.mpf(r['absw_up']),span[ab]))
from collections import defaultdict
WS=defaultdict(lambda: mp.mpf(0))
for w,sp in rows: WS[sp+g0]+=w
def fin(a):
    s0=s1=mp.mpf(0)
    for l,w in WS.items():
        e=mp.exp(a*l); s0+=2*w*e; s1+=2*w*l*e
    return s0*(1+mp.mpf('1e-9')), s1*(1+mp.mpf('1e-9'))
def tail(C,a,slope,add):
    r=q*mp.exp(slope*a); J=J0+1
    g=r**J/(1-r); gj=r**J*(J-(J-1)*r)/(1-r)**2
    pref=2*mp.mpf(C)**mp.mpf(1.5)*mp.exp(a*(g0+add))
    return pref*g, pref*(slope*gj+(add+g0)*g)
def F(a,C,slope,add):
    s0,s1=fin(a); t0,t1=tail(C,a,slope,add); return s0+t0, s0+t0+(s1+t1)/(1+g0)
def minimal_a(C,slope,add):
    a=mp.mpf('1e-7')
    while F(a,C,slope,add)[1]>a: a*=mp.mpf('1.01')
    lo,hi=a/mp.mpf('1.01'),a
    for _ in range(70):
        m=(lo+hi)/2
        if F(m,C,slope,add)[1]<=m: hi=m
        else: lo=m
    return hi
def published_iter(C,slope,add):
    a=mp.mpf('1e-6')
    for _ in range(120): a=F(a,C,slope,add)[1]*mp.mpf('1.02')
    return a
# crossover
gam=mp.euler
def hseq(P):
    h={}; a,b=1,7; p=3; h[3]=7
    k=1
    while 2*k+3<=P:
        a,b=b,6*b-a; k+=1; h[2*k+1]=b
    return h
H=hseq(5003)
def primes(n):
    s=bytearray([1])*(n+1); s[0]=s[1]=0
    for i in range(2,int(n**.5)+1):
        if s[i]: s[i*i::i]=bytearray(len(s[i*i::i]))
    return [i for i in range(n+1) if s[i]]
PR=[p for p in primes(5000) if p>=1000]
LNK={p:mp.log(4*mp.mpf(H[p])**2+3) for p in PR}
def xover(d):
    lnb=mp.log1p(R)-d
    def G(p): x=mp.exp(p*lnb); return (2*x-1)**2-1
    def rob(L): return mp.exp(gam)*mp.log(L)+mp.mpf('0.6483')/mp.log(L)-1
    ok=[p for p in PR if G(p)>rob(LNK[p])]
    first=ok[0]; viol=[p for p in PR if p>first and p not in ok]
    lnE=mp.log(eps)
    first_int=next(p for p in range(1000,6000) if G(p)>rob((2*p+1)*lnE))
    return first,viol,first_int
out={}
out['theta']=str(theta); out['beta']=mp.nstr(beta,20); out['q']=mp.nstr(q,20); out['n_fin_rows']=len(rows)
for name,C,slope,add,mode in [('slope2_min',0.082,2,0,'min'),('slope2_N20iter',0.082,2,0,'iter'),('theta_min',0.082,theta,3,'min'),
        ('theta_iter',0.082,theta,3,'iter'),('4/5_min',0.082,mp.mpf(4)/5,3,'min'),('theta_min_C8.8e-4',8.8e-4,theta,3,'min'),
        ('slope2_iter_C8.8e-4',8.8e-4,2,0,'iter'),('theta_min_C4.4e-4',4.4e-4,theta,3,'min')]:
    a=minimal_a(C,slope,add) if mode=='min' else published_iter(C,slope,add)
    S0,lhs=F(a,C,slope,add); d=S0+DT
    f,v,fi=xover(d)
    out[name]=dict(a=mp.nstr(a,8),S0=mp.nstr(S0,8),KPlhs=mp.nstr(lhs,8),KP_ok=bool(lhs<=a),budget_left=mp.nstr(R-S0-DT,6),delta_eff=mp.nstr(d,8),first_prime=f,first_int=fi,viol=v[:5])
    print(name,out[name],flush=True)
    if name=='theta_min':
        out['sens']={}
        for fac in ['0.99','1','1.01','1.03','1.1']:
            out['sens'][fac]=xover(S0*mp.mpf(fac)+DT)[0]
        print(out['sens'])
for d in ['3.4962e-4','7.4115e-6','1.1691e-4']:
    out['published_'+d]=xover(mp.mpf(d)); print(d,out['published_'+d])


# ---- J0 = 13/14 rows and Lemma BI ----
import json, glob, mpmath as mp, sys
from collections import defaultdict
mine={(r['a'],r['b']):r for r in map(json.loads,open(LOG / 'span_census_J16.jsonl'))}
allrows=[]
for r in map(json.loads,open(ROOT / 'computations/verification/lineN15/logs/a_cert3.jsonl')):
    allrows.append((r['j'],(r['a'],r['b']),r['zr'],mp.mpf(r['absw_up'])))
spm=0
for f in sorted(glob.glob(str(ROOT / 'evidence/executions/20261101/lineNgas/N20/logs/a_cert_ext*.jsonl'))):
    for l in open(f):
        r=json.loads(l)
        if r.get('coded'): assert mine[(r['a'],r['b'])]['zr']>=6; continue
        if r['span']!=mine[(r['a'],r['b'])]['span'] or r['zr']!=mine[(r['a'],r['b'])]['zr']: spm+=1
        allrows.append((r['j'],(r['a'],r['b']),r['zr'],mp.mpf(r['absw_up'])))
print('ext span/zr mismatches vs auditor census',spm,'rows',len(allrows))
def mkWS(J0):
    WS=defaultdict(lambda: mp.mpf(0))
    for j,ab,zr,w in allrows:
        if j>J0 or ab in MODEL or zr>=g0: continue
        WS[mine[ab]['span']+g0]+=w
    return WS
def finW(WS,a,extra=0):  # sum 2 w e^{a l + extra(l)}
    s0=s1=mp.mpf(0)
    for l,w in WS.items():
        e=mp.exp(a*l+extra(l)) if callable(extra) else mp.exp(a*l); s0+=2*w*e; s1+=2*w*l*e
    return s0*(1+mp.mpf('1e-9')), s1*(1+mp.mpf('1e-9'))
def tailJ(C,a,slope,add,J0,kap=0):
    # sum_{j>J0} sum|w| e^{(a+kap) l + 7 kap}, l<= slope*j+add+g0
    b=a+kap; r=q*mp.exp(slope*b); J=J0+1
    g=r**J/(1-r); gj=r**J*(J-(J-1)*r)/(1-r)**2
    pref=2*mp.mpf(C)**mp.mpf(1.5)*mp.exp(b*(g0+add)+7*kap)
    return pref*g, pref*(slope*gj+(add+g0)*g)
def bare(C,J0,slope,add,iter102=False):
    WS=mkWS(J0)
    def Fv(a):
        s0,s1=finW(WS,a); t0,t1=tailJ(C,a,slope,add,J0); return s0+t0, s0+t0+(s1+t1)/5
    if iter102:
        a=mp.mpf('1e-6')
        for _ in range(150): a=Fv(a)[1]*mp.mpf('1.02')
    else:
        a=mp.mpf('1e-7')
        while Fv(a)[1]>a: a*=mp.mpf('1.01')
        lo,hi=a/mp.mpf('1.01'),a
        for _ in range(60):
            m=(lo+hi)/2
            if Fv(m)[1]<=m: hi=m
            else: lo=m
        a=hi
    S0,lhs=Fv(a); return a,S0,lhs
AM=mp.mpf('1.03e-3')
def bi(C,J0,slope,add,AM=AM,LM=7,iter102=False):
    WS=mkWS(J0)
    def S_of(a,kap):
        s0,s1=finW(WS,a,lambda l: kap*(l+7)); t0,t1=tailJ(C,a,slope,add,J0,kap); return s0+t0,s1+t1
    def cprime(a,S,S1):
        # smallest c' with (LM+5... ) ratio (5+LM)/5 * AM e^{LM c' + LM(a+S)+S1} <= c'
        fac=mp.mpf(5+LM)/5; c=mp.mpf(0)
        for _ in range(200): c=fac*AM*mp.exp(LM*c+LM*(a+S)+S1)
        assert fac*AM*mp.exp(LM*c+LM*(a+S)+S1)<=c*(1+mp.mpf('1e-25'))
        return c
    def solve_kappa(a):
        kap=AM
        for _ in range(100):
            S,S1=S_of(a,kap); c=cprime(a,S,S1); kn=mp.exp(LM*c)*AM*mp.exp(LM*c+LM*(a+S)+S1)
            if abs(kn-kap)<mp.mpf('1e-30'): break
            kap=kn
        S,S1=S_of(a,kap*(1+mp.mpf('1e-12')))
        return kap,S,S1
    def ok(a):
        kap,S,S1=solve_kappa(a); return S+(S1+(5+LM)*kap)/5<=a, kap,S,S1
    if iter102:  # N20-style bookkeeping: a <- 1.02 * (S + (S1 + (5+LM) kappa)/5), as in the P2 solver
        a=mp.mpf('1e-4')
        for _ in range(60):
            kap,S,S1=solve_kappa(a); a=(S+(S1+(5+LM)*kap)/5)*mp.mpf('1.02')
        good,kap,S,S1=ok(a); assert good; return a,kap,S,S1
    a=mp.mpf('1e-4')
    while not ok(a)[0]: a*=mp.mpf('1.01')
    lo,hi=a/mp.mpf('1.01'),a
    for _ in range(40):
        m=(lo+hi)/2
        if ok(m)[0]: hi=m
        else: lo=m
    _,kap,S,S1=ok(hi); return hi,kap,S,S1
res={}
for name,args in [('J12_C082_theta',(0.082,12,theta,3)),('J13_C082_theta',(0.082,13,theta,3)),('J14_C082_theta',(0.082,14,theta,3)),
                  ('J14_C082_slope2',(0.082,14,2,0)),('J14_C15_theta',(0.15,14,theta,3)),('J12_C04_theta',(0.04,12,theta,3))]:
    a,S0,lhs=bare(*args); f=xover(S0+DT)[0]
    a2,S02,_=bare(*args,iter102=True); f2=xover(S02+DT)[0]
    res['bare_'+name]=dict(a_min=mp.nstr(a,6),S0=mp.nstr(S0,7),prime=f,a_iter=mp.nstr(a2,6),S0_iter=mp.nstr(S02,7),prime_iter=f2)
    print('bare',name,res['bare_'+name],flush=True)
for name,args,kw in [('J12_C082',(0.082,12,theta,3),{}),('J12_C04',(0.04,12,theta,3),{}),('J12_C88e-4',(8.8e-4,12,theta,3),{}),
                     ('J13_C082',(0.082,13,theta,3),{}),('J14_C082',(0.082,14,theta,3),{}),('J12_C082_AM2x',(0.082,12,theta,3),{'AM':2*AM}),
                     ('J12_C082_LM8',(0.082,12,theta,3),{'LM':8}),('J12_C082_iter102',(0.082,12,theta,3),{'iter102':True}),
                     ('J12_C88e-4_iter102',(8.8e-4,12,theta,3),{'iter102':True})]:
    a,kap,S,S1=bi(*args,**kw); f=xover(S+DT)[0]
    res['BI_'+name]=dict(a=mp.nstr(a,5),kappa=mp.nstr(kap,5),S0=mp.nstr(S,7),delta_eff=mp.nstr(S+DT,7),prime=f)
    print('BI',name,res['BI_'+name],flush=True)
out['J0_and_BI']=res
json.dump(out,open(LOG / 'crossover_sharp_bi.json','w'),indent=1,default=str)
