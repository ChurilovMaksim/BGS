if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")
from math import gcd, isqrt
from mpmath import mp, mpf, log
mp.dps=40
def u(n):
    a,b=1,7
    for _ in range(n): a,b=b,6*b-a
    return a
h=lambda p:u((p-1)//2)
def order(d):
    x,y,k=1,0,0
    while True:
        x,y=(3*x+4*y)%d,(2*x+3*y)%d; k+=1
        if (x,y)==(1,0): return k
L={5:[31,217],7:[49,4663],19:[457,3199,14593,102151,6669001,7521721,46683007,52652047,3437426497,24061985479],
   29:[13921,97447,5806729,40647103,28073057689,80835474409,196511403823,565848320863,390805036088569,2735635252619983]}
n=0
for p,ds in L.items():
    hp=h(p);K=4*hp*hp+3;hm=hp*K
    for d in ds:
        if d==4663: continue
        n+=1
        o=order(d) if d<10**12 else None
        print(p,d,K%d==0,d*d<=hm,d%3,o, (o==3*p) if o else '')
print('count',n)
# big d orders: check lambda^{3p}=1 mod d and lambda^{3p/q}!=1 for q in {3,p}
def mpow(d,e):
    R=(1,0);B=(3,2)
    while e:
        if e&1: R=((R[0]*B[0]+2*R[1]*B[1])%d,(R[0]*B[1]+R[1]*B[0])%d)
        B=((B[0]*B[0]+2*B[1]*B[1])%d,(2*B[0]*B[1])%d); e>>=1
    return R
for p,d in [(29,390805036088569),(29,2735635252619983),(19,3437426497),(19,24061985479)]:
    print(p,d,mpow(d,3*p),mpow(d,p),mpow(d,3))
print(2*169*33*6728 < 3*140*32*6725, 2*3072**2 > 2209**2, 4*49+3, (4*49+3)%7, 41*6727, isqrt(275807), 525**2,526**2)
T=mpf('1.42785')
for r,P in [('1.458772466390154',57),('1.5119805975188876',57),('1.4686852948918232',87)]:
    print(r, (mpf(r)/T)**P, mpf(r)-T)
for b,d in [(208,3437426497),(227,24061985479),(89,2735635252619983)]: print(gcd(b,d))
