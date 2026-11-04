exec(open('indep.py').read().split('# independent cover')[0].replace("print(","(lambda *a,**k:None)("))
from mpmath import log, mpf
for fam,d in []:# [('8V',10+log(mpf(4)/3)),('8E',mpf('8.75')+log(mpf(4)/3))]:
    K1,lk,wmax,ok0=out[fam]; K=K1+d
    ok=lambda p: wmax(p)*log(2)+K+2*log(p)-2*log(1-lam**(-p)) < p*lk
    lo,hi=3,3
    while not ok(hi): hi*=2
    lo=hi//2
    while hi-lo>1:
        m=(lo+hi)//2
        if ok(m): hi=m
        else: lo=m
    print(fam,'shift',float(d),'pointwise least p0',hi, 'check next 2000 all ok:', all(ok(p) for p in range(hi,hi+2000)))
K1,lk,wmax,_=out['8V']; K=K1+10+log(mpf(4)/3)
ok=lambda p: wmax(p)*log(2)+K+2*log(p)-2*log(1-lam**(-p)) < p*lk
fails=[p for p in range(28424000,28432000) if not ok(p)]
print('last fail',fails[-1] if fails else None, 'count',len(fails))
# base also: check no fails above 28420500 in a window (non-monotonicity)
K=K1; print('base fails in [28420500,28428500):',sum(1 for p in range(28420500,28428500) if not ok(p)))
