# Independent recomputation (mpmath, no flint, no PR code) of the Prop. K fixed point and the v5 crossover.
import json, mpmath as mp
mp.mp.dps=40
R=mp.mpf('6.234e-4'); DT=mp.mpf('5.0313e-6'); g0=4; J0=12
lam=3+2*mp.sqrt(2); eps=1+mp.sqrt(2); theta=mp.log(2)/mp.log(eps)
beta=2*mp.log(1/mp.mpf('0.28'))/mp.log(lam); q=mp.power(2,mp.mpf(1.5)*(1-beta))
span={(r['a'],r['b']):r['span'] for r in map(json.loads,open('/workspace/audit/pr83/AUDIT_code/census_J12.jsonl'))}
MODEL={(1,0),(0,1),(2,0),(0,2)}
rows=[]
for r in map(json.loads,open('/workspace/audit/pr83/computations/verification/lineN15/logs/a_cert3.jsonl')):
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
json.dump(out,open('/workspace/audit/pr83/AUDIT_code/kp_xover.json','w'),indent=1,default=str)
