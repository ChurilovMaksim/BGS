if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")
from sympy import factorint, isprime, primerange
def u(n):
    a,b=1,7
    for _ in range(n): a,b=b,6*b-a
    return a
def h(p): return u((p-1)//2)
from math import gcd, isqrt
bad=[]
for p in primerange(5,2000):
    hp=h(p); K=4*hp*hp+3
    if K%7 or hp%7==0 or gcd(hp,K)!=1 or hp%3==0: bad.append(p)
    assert u((3*p-1)//2)==hp*K
print("bad up to 2000:",bad)
for p in [5,7,11,13,17,19,23,29,31]:
    hp=h(p);K=4*hp*hp+3; f=factorint(K)
    print(p,hp,isprime(hp),f,all(q%3==1 for q in f), all((q-1)%(6*p)==0 for q in f if q!=7))
for p,d in [(19,3437426497),(19,24061985479),(29,2735635252619983),(29,390805036088569)]:
    hp=h(p);K=4*hp*hp+3;hm=hp*K
    print(p,d,factorint(d),"K%d=",K%d,"hp|d?",d%hp==0,"d^2<=hm",d*d<=hm, "d<=sqrt",d<=isqrt(hm), "hm/d^2=%.4g"%(hm/d/d), "d|hp*?", gcd(d,hp))
# included divisors lists
for p in [19,29]:
    hp=h(p);K=4*hp*hp+3;hm=hp*K
    from sympy import divisors
    print(p,[x for x in divisors(K) if 1<x and x*x<=hm])
