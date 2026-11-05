# Independent referee check for BGS-TRACE-348..351 (written from scratch, not derived from h5_arith.py). Run: python indep_check.py
import math, mpmath
from sympy import isprime, primerange, factorint
from math import gcd
def h(n):  # eps^n = a + b sqrt2, eps = 1 + sqrt2; returns a = h_n
    a,b=1,0
    for _ in range(n): a,b=a+2*b,a+b
    return a
P=1000
ps=[p for p in primerange(3,P+1)]
H={p:h(p) for p in ps}
# 348 via full factorisation p<=61, plus mod checks
for p in ps:
    if p>61: break
    for q,e in factorint(H[p]).items():
        assert q%(2*p)==1 and q%8 in (1,7) and e==1,(p,q)
# 348 via small primes q<2e5 for all p<=1000
for q in primerange(3,200000):
    for p in ps:
        if 2*p+1>q: break
        if H[p]%q==0: assert q%(2*p)==1 and q%8 in (1,7)
# 349
import itertools
for p,r in itertools.combinations(ps,2): assert gcd(H[p],H[r])==1
# 350 + converse + minFac on the family
fam=[]
for p in ps:
    q=2*p+1
    div = H[p]%q==0
    if isprime(q): assert div==(p%4==3),p
    if p%4==3 and isprime(q):
        assert div
        assert all(H[p]%r for r in primerange(2,q)), p
        if p>=5: fam.append(p); assert H[p]>q
print("family p in [5,1000]:",len(fam),fam)
# 351
mpmath.mp.dps=60
for n in range(1,202,2):
    pr=mpmath.fprod([6-2*mpmath.cos(2*mpmath.pi*k/n) for k in range(1,(n-1)//2+1)])
    assert abs(pr-h(n))/h(n)<mpmath.mpf(10)**-50
print("all OK")
