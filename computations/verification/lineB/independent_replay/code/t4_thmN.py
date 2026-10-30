"""Theorem N: NSW-prime indices, hypotheses (a),(b), h>28m, bound 8 m^2 N_m / h; plus the proof that (a),(b) are automatic."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import gmpy2, math, sys
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from a1_ecpp_verify import hm
K=[-9,-8,-7,-6,-5,-2,-1,1,2,5,6,7,8,9]
def mul(x,y,h): return ((x[0]*y[0]+2*x[1]*y[1])%h,(x[0]*y[1]+x[1]*y[0])%h)   # a+b sqrt2
idx=[m for m in range(1,1501,2) if gmpy2.is_bpsw_prp(hm(m))]
print('odd m<=1500 with h_m BPSW-prime:',idx)
for m in [7,19,29,47,59,163,257,421,937,947,1493]:
    h=hm(m); P=[(1,0)]
    for _ in range(m): P.append(mul(P[-1],(3,2),h))
    order_ok = P[m]==(1,0) and all(p!=(1,0) for p in P[1:m])
    rats={ (k2*pow(k1,-1,h))%h for k1 in K for k2 in K if k1!=k2 }
    condA = all(not (p[1]==0 and p[0] in rats) for p in P[:m])
    pset={}
    for a,p in enumerate(P[:m]): pset[p]=a
    condB=True
    for a in range(m):
        for b in range(m):
            s=((P[a][0]+P[b][0])%h,(P[a][1]+P[b][1])%h)
            if s==(6%h,0) and {a,b}!={1,m-1}: condB=False
    Nm=math.comb(14*m,2)+m+m*(m*(m+1)//2-1)
    bound=8*m*m*Nm/h
    print(f'm={m:5d} digits(h)={len(str(h)):4d} h>28m={h>28*m} ord(lambda)=m:{order_ok} (a):{condA} (b):{condB} log10(8m^2N_m/h)={math.log10(8*m*m*Nm)-math.log10(h):.2f}',flush=True)
