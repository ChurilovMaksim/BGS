# Line M elementary checks [N]/[P-check]: strong divisibility, 3 not| h, family overlaps, inherited-level capacity
from math import gcd, log, sqrt
from sympy import factorint, primerange
def hseq(M):
    # (1+sqrt2)^m = h_m' + y_m sqrt2 ; NSW for odd m: h_m = x-part? use recurrence for odd-index V/2
    x,y=1,1; out={1:1}
    for m in range(2,M+1):
        x,y=x+2*y,x+y
        if m%2: out[m]=x
    return out
H=hseq(400)
assert [H[m] for m in (1,3,5,7,9)]==[1,7,41,239,1393], [H[m] for m in (1,3,5,7,9)]
# 1. strong divisibility gcd(h_m,h_n)=h_gcd(m,n) for odd m,n<=301
bad=0
for m in range(1,302,2):
    for n in range(1,302,2):
        if gcd(H[m],H[n])!=H[gcd(m,n)]: bad+=1
print("strong divisibility failures (odd m,n<=301):",bad)
# 2. 3 never divides h_m (odd m)
print("3|h_m for odd m<=399:",[m for m in H if H[m]%3==0])
# 3. h_{3p} = h_p (4 h_p^2 + 3)
print("h_3p identity fails:",[p for p in primerange(3,130) if H[3*p]!=H[p]*(4*H[p]**2+3)])
# 4. family overlaps: nu with 4nu=1 mod h/d and 4nu=-1 / 8nu=+-1 mod h/d' -> need gcd(h/d,h/d') | {1,3}; check exhaustively small m
def divisors(n):
    f=factorint(n); ds=[1]
    for q,e in f.items(): ds=[d*q**k for d in ds for k in range(e+1)]
    return sorted(ds)
ov=0
for m in range(9,40,2):
    h=H[m]; Ds=[d for d in divisors(h) if 1<=d and d*d<=h]
    for d in Ds:
        for d2 in Ds:
            g=gcd(h//d,h//d2)
            if g>3: continue
            # overlap possible only when g<=3; g==1 requires d*d2>=h
            if g==1 and not(d==1 and d2==1): ov+=1
print("nontrivial family-overlap candidates (m=9..39):",ov)
# 5. inherited-level capacity rate vs D7 rate, m=3p: kappa ~ |Z|^2/(h_p*phi(2h)), |Z|=mu^m/2
mu=1.9154712; lam=3+2*sqrt(2); xi=2.4586893
print(" p   m   log(kappa)/m  exp   D7rate log(1.0184224)=",log(1.0184224))
for p in [11,17,29,53,101,199]:
    m=3*p; hp=H[p]; h=H[m]
    lk=2*(m*log(mu)-log(2))-log(hp)-log(h)  # phi(2h)<=h
    print(p,m,round(lk/m,5),round(__import__('math').exp(lk/m),5))
print("asymptotic capacity base mu^2/(lam^(1/6) lam^(1/2)) =",mu**2/lam**(1/6)/lam**0.5)
print("L_m base mu^2/xi =",mu**2/xi, " h_p base lam^(1/6)=",lam**(1/6), " sqrt h base lam^(1/4)=",lam**0.25)
