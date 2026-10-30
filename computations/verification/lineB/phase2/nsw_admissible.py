"""Theorem N (odd m, h_m prime): hypotheses and explicit bound.
h_m = Q_m/2 (NSW numbers). V_odd = Z[sqrt2]/h, lambda=3+2sqrt2 acts by multiplication and has exact order m.
Admissibility: (a) lambda^d != k'/k mod h for all d and all k != k' in K (supp of the kick symbol);
               (b) lambda^a + lambda^b != 6 (= lambda + lambda^-1) unless {a,b} = {1,-1} mod m.
Bound: |B_m - B_m^sym| <= 8 m^2 N_m / h_m, N_m = C(14m,2) + m + m*(m(m+1)/2 - 1)."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sympy
from math import comb
K=[-9,-8,-7,-6,-5,-2,-1,1,2,5,6,7,8,9]
def hQ(m):
    Q=[2,2]
    for _ in range(m): Q.append(2*Q[-1]+Q[-2])
    return Q[m]//2
def mul(x,y,h): return ((x[0]*y[0]+2*x[1]*y[1])%h,(x[0]*y[1]+x[1]*y[0])%h)
rows=[]
for m in list(range(3,62,2))+[163,257,421,937,947,1493]:
    h=hQ(m); prime=sympy.isprime(h)
    if not prime:
        if m<=61: rows.append((m,h,False,None,None,None))
        continue
    lam=(3,2); p=(1,0); pw=[]
    for d in range(m): pw.append(p); p=mul(p,lam,h)
    order_ok=(p==(1,0)) and all(q!=(1,0) for q in pw[1:])
    S=set(pw)
    ratios={(kp*pow(k,-1,h))%h for k in K for kp in K if kp!=k} if h>28*m else set()
    a_ok=not any((r,0) in S for r in ratios)
    six=(6%h,0); idx={q:i for i,q in enumerate(pw)}
    b_bad=[]
    for a,q in enumerate(pw):
        t=((six[0]-q[0])%h,(-q[1])%h)
        if t in idx:
            b=idx[t]
            if {a%m,b%m}!={1%m,(m-1)%m}: b_bad.append((a,b))
    Nm=comb(14*m,2)+m+m*(m*(m+1)//2-1)
    import math as _m; bound=_m.log10(8*m*m*Nm)-_m.log10(h)
    rows.append((m,h,True,order_ok and a_ok and not b_bad and h>28*m,bound,(order_ok,a_ok,len(b_bad),h>28*m)))
for m,h,pr,adm,bd,det in rows:
    hs=str(h) if len(str(h))<25 else f'{str(h)[:6]}...({len(str(h))} digits)'
    print(f'm={m:4d} h_m={hs:>28s} prime={pr} ' + ('' if not pr else f'admissible={adm} (order m, (a), #(b)-violations, h>28m)={det} log10(8m^2N_m/h)={bd:.2f} N_m={comb(14*m,2)+m+m*(m*(m+1)//2-1)} primality={'deterministic' if h<2**64 else 'BPSW probable prime'}'))
