"""K2 v2 (fixes K2-F1/F4): explicit S_Z (code/k2_SZ.py: S_Z <= 0.5000001 for m >= 495), continuous-s optimisation, correct rounding:
log L_m upper bound (arb), sqrt(h) lower bound via h_m >= (eps^m - 1)/2. Non-vacuous iff L_m < sqrt(h_m). Crossover by bisection over p
(m = 3p, p real for the bisection; reported [N] since the crossover location is a float statement)."""
import json, math
from flint import arb, ctx
ctx.prec=150
mu=arb('1.9154753'); xi=arb('2.4586893'); Kmin=arb('0.009985'); eps=arb('0.01'); SZ=arb('0.5000001')
e1=1+arb(2).sqrt()
def logL(p):
    m=3*p; logh=m*e1.log(); w=int(math.floor(float((logh/arb(2*p+1).log()).upper())))
    target=(eps*Kmin/2/SZ).log()+m*(xi.log()-2*mu.log())
    def f(s):
        s=arb(s); E=-(1-arb(7)**(-s)).log()-w*(1-arb(2*p+1)**(-s)).log()
        return (E-target)/(1-s)
    # golden-section on s in (0,1) using float mids, then evaluate rigorously at the chosen s (any s gives a valid bound)
    a,b=1e-4,0.9
    for _ in range(80):
        c=b-(b-a)/1.618; d=a+(b-a)/1.618
        if float(f(c).mid())<float(f(d).mid()): b=d
        else: a=c
    s=(a+b)/2; return f(s).upper(), s, w
def loghalf_lo(p):
    m=3*p; return ((((e1**m)-1)/2).log()/2).lower()
rows=[]
for p in [167,331,1009,10007,100003,1000003,10**7+19,10**8+7]:
    lL,s,w=logL(p); m=3*p
    eta=float(lL)/(m*math.log(float((mu*mu/xi).mid())))-1
    rows.append(dict(m=m,s=s,w=w,l=math.exp(float(lL)/m),sqrt_h_rate=math.exp(float(loghalf_lo(p))/m),eta=eta,eta_log2p1=eta*math.log(2*p+1),
                     nonvacuous=bool(arb(lL)<arb(loghalf_lo(p)))))
    print(rows[-1],flush=True)
lo,hi=10**8,10**9   # p range
assert not (arb(logL(lo)[0])<arb(loghalf_lo(lo))) and (arb(logL(hi)[0])<arb(loghalf_lo(hi)))
while hi-lo>10**5:
    mid=(lo+hi)//2
    if arb(logL(mid)[0])<arb(loghalf_lo(mid)): hi=mid
    else: lo=mid
print('crossover m in [%.4e, %.4e]'%(3*lo,3*hi))
json.dump(dict(S_Z=str(SZ),rows=rows,crossover_m=[3*lo,3*hi]),open('logs/k2_large_v2.json','w'),indent=1)
