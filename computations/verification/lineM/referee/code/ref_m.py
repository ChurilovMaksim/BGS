# Independent referee checks for Line M (exact integer arithmetic unless stated)
import numpy as np, random, cmath
from math import gcd, log, sqrt
from sympy import factorint, primerange, isprime
# Z[sqrt2] arithmetic, independent of author's recurrence: h_m = rational part of (1+sqrt2)^m
def mul(a,b,N=None):
    x=a[0]*b[0]+2*a[1]*b[1]; y=a[0]*b[1]+a[1]*b[0]
    return (x%N,y%N) if N else (x,y)
def pw(a,k,N=None):
    r=(1,0)
    while k:
        if k&1: r=mul(r,a,N)
        a=mul(a,a,N); k>>=1
    return r
def h(m): return pw((1,1),m)[0]
H={m:h(m) for m in range(1,1300,2)}
lam=(3,2)
print("[1] Pell norm h^2+1=2y^2 (odd m<=1299):", all(H[m]**2+1==2*pw((1,1),m)[1]**2 for m in H))
# M1 strong divisibility, larger range
bad=sum(1 for m in range(1,602,2) for n in range(1,602,2) if gcd(H[m],H[n])!=H[gcd(m,n)])
print("[2] strong divisibility failures odd m,n<=601:",bad)
# LTE valuation check v_q(h_m)=v_q(h_r)+v_q(m/r) for q|h_r, q in small primes
def v(q,x):
    c=0
    while x%q==0: x//=q;c+=1
    return c
lt=0;cnt=0
for q in primerange(5,400):
    r=next((r for r in range(1,4*q,2) if H.get(r,1)%q==0 and r in H),None) if any(H[r]%q==0 for r in range(1,min(1299,4*q),2)) else None
    if r is None: continue
    for m in range(r,1299,2*r):
        cnt+=1
        if v(q,H[m])!=v(q,H[r])+v(q,m//r): lt+=1
print("[3] LTE valuation failures:",lt,"of",cnt)
# r(q) lemma: q|h_m <=> lambda^m==1 mod q, odd m
f=0
for q in primerange(3,300):
    for m in range(1,400,2):
        if (H[m]%q==0) != (pw(lam,m,q)==(1,0)): f+=1
print("[4] r(q) lemma mismatches q<300, m<400:",f)
print("[5] 3|h_m odd m<1300:",[m for m in H if H[m]%3==0], "; lambda^k mod 3:",[pw(lam,k,3) for k in range(1,5)])
print("[6] h_3n=h_n(4h_n^2+3) fails odd n<=431:",[n for n in range(1,432,2) if H[3*n]!=H[n]*(4*H[n]**2+3)])
# M1 corollary: gcd(h_3p,h_3p')=7
print("[7] gcd(h_3p,h_3p') !=7 for primes 5<=p<p'<=200:",[(p,q) for p in primerange(5,200) for q in primerange(p+1,200) if gcd(H[3*p],H[3*q])!=7])
# prime factors of h_p: q==1 mod 2p ; ord lambda mod h_p == p ; lambda^p ==1 mod 2h_p, not mod 4h_p
rows=[]
for p in primerange(3,62):
    hp=H[p]; fa=factorint(hp)
    ok=all(q%(2*p)==1 for q in fa)
    o2=pw(lam,p,2*hp)==(1,0); o4=pw(lam,p,4*hp)==(1,0)
    nh=1
    for q,e in fa.items(): nh*= (q-2)*q**(e-1)  # n_q=q-2 for q||h (TRACE-228); crude for powers
    phi=1
    for q,e in fa.items(): phi*=(q-1)*q**(e-1)
    rows.append((p,len(fa),ok,o2,o4,round(phi/hp,8),round(nh/hp,8),min(fa)))
print("[8] p, omega(h_p), all q==1 mod 2p, lam^p==1 mod 2h_p, mod 4h_p, phi(h_p)/h_p, n/h_p, min q")
for r in rows: print("   ",r)
# exact family-overlap enumeration (M4): units nu mod 2h, level d_rho(nu)=2h/gcd(b nu - a, 2h)
P=[(2,8),(-2,8),(2,16),(-2,16)]
for m in range(5,20,2):
    hh=H[m]; N=2*hh
    nu=np.arange(N,dtype=np.int64)
    unit=np.gcd(nu,N)==1
    lv=[]
    for a,b in P:
        g=np.gcd((b*nu-a)%N,N); g[g==0]=N
        d=N//g
        lv.append(np.where(unit&(d*d<=hh),d,0))   # level <= sqrt h (incl primary d=1)
    L=np.array(lv)
    multi=((L>0).sum(0)>1).sum()
    # per family: d always divides h ; primary count
    divok=all(((x[x>0])==0).sum()==0 and np.all(hh%x[x>0]==0) for x in L)
    prim=[(x==1).sum() for x in L]
    print(f"[9] m={m} h={hh}: nu in >=2 families (levels<=sqrt h incl primaries): {multi}; levels divide h: {divok}; primaries per family {prim}")
# M5 identity and quadratic minimum, random
random.seed(1); err=0
for _ in range(2000):
    n=random.randint(1,30); d=random.randint(2,50)
    Zr=complex(random.gauss(0,50),random.gauss(0,50))
    Zs=[complex(random.gauss(0,5),random.gauss(0,5)) for _ in range(n)]
    X=[z-Zr/d for z in Zs]; S=sum(X)
    dev=sum(abs(z)**2 for z in Zs)-n*abs(Zr)**2/d**2
    rhs=2*(Zr.conjugate()*S).real/d+sum(abs(x)**2 for x in X)
    err=max(err,abs(dev-rhs)/(1+abs(dev)))
    assert dev>=-n*abs(Zr)**2/d**2-1e-9
print("[10] M5 decomposition max rel err:",err,"; Dev>=-n|Z|^2/d^2 holds (=Prop K2 per-level bound)")
# M6 sign algebra: c^-_{a+4}=s_a conj c^+_a, z^-_{a+4}=conj z^+_a, y^-_{b+4}=conj y^+_b
s={0:-1,4:-1,2:1,6:1}; e6=0
for _ in range(500):
    c={a:cmath.exp(2j*cmath.pi*random.random())/2 for a in s}
    z={a:complex(random.gauss(0,1),random.gauss(0,1)) for a in s}
    y={a:complex(random.gauss(0,1),random.gauss(0,1)) for a in s}
    cm={(a+4)%8:s[a]*c[a].conjugate() for a in s}; zm={(a+4)%8:z[a].conjugate() for a in s}; ym={(a+4)%8:y[a].conjugate() for a in s}
    Zp=sum(c[a]*z[a] for a in s); Yp=sum(c[a]*y[a] for a in s)
    Zm=sum(cm[a]*zm[a] for a in s); Ym=sum(cm[a]*ym[a] for a in s)
    lhs=2*(Zp.conjugate()*Yp).real+2*(Zm.conjugate()*Ym).real
    rhs=2*sum(((c[a]*z[a]).conjugate()*c[b]*y[b]).real*(1+s[a]*s[b]) for a in s for b in s)
    e6=max(e6,abs(lhs-rhs))
print("[11] M6 sign algebra max err:",e6," -> pairs with s_a=s_b DOUBLE (incl {2,6}x{2,6}), s_a!=s_b cancel")
# constants
mu=1.9154712; L=3+2*sqrt(2); xi=2.4586893
print("[12] capacity base mu^2/lam^(2/3)=%.6f ; /1.0184224=%.6f ; L_m base mu^2/xi=%.6f ; h_p base %.5f ; sqrt h base %.5f"%(mu**2/L**(2/3),mu**2/L**(2/3)/1.0184224,mu**2/xi,L**(1/6),L**0.25))
eta_max=log(L**0.25)/log(mu**2/xi)-1
print("[13] L_m<sqrt h needs eta_m<%.4f; with eta<=2.010/log(2p+1): p > %.3g"%(eta_max,(np.exp(2.010/eta_max)-1)/2))
print("[14] (1+sqrt2)^m mod 8, m=1..16:",[pw((1,1),m,8) for m in range(1,17)])
print("[15] m vs 3m mod 8 distinct for odd m:",all((m%8)!=(3*m%8) for m in range(1,200,2)))
