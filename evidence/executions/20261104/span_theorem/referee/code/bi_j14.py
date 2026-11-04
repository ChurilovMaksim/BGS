# Auditor: J0=14 rows and Lemma BI numerics, own implementation (mpmath). Uses kp_xover.py definitions.
import json, glob, mpmath as mp, sys
src=open('/workspace/audit/pr83/AUDIT_code/kp_xover.py').read().split("out={}")[0]
exec(src)
from collections import defaultdict
mine={(r['a'],r['b']):r for r in map(json.loads,open('/workspace/audit/pr83/AUDIT_code/census_J16.jsonl'))}
allrows=[]
for r in map(json.loads,open('/workspace/audit/pr83/computations/verification/lineN15/logs/a_cert3.jsonl')):
    allrows.append((r['j'],(r['a'],r['b']),r['zr'],mp.mpf(r['absw_up'])))
spm=0
for f in glob.glob('/workspace/audit/pr83/evidence/executions/20261101/lineNgas/N20/logs/a_cert_ext*.jsonl'):
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
def bi(C,J0,slope,add,AM=AM,LM=7):
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
                     ('J12_C082_LM8',(0.082,12,theta,3),{'LM':8})]:
    a,kap,S,S1=bi(*args,**kw); f=xover(S+DT)[0]
    res['BI_'+name]=dict(a=mp.nstr(a,5),kappa=mp.nstr(kap,5),S0=mp.nstr(S,7),delta_eff=mp.nstr(S+DT,7),prime=f)
    print('BI',name,res['BI_'+name],flush=True)
json.dump(res,open('/workspace/audit/pr83/AUDIT_code/bi_j14.json','w'),indent=1)
