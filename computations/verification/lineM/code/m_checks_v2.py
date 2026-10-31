# Line M v2 checks (supersedes m_checks.py, which is kept pinned). Fixes M-F4 (KeyError p=199), M-F3 (membership enumeration).
# Exact integers; h_m by fast powering in Z[sqrt2] (independent of the v1 recurrence, cross-checked against it).
from math import gcd, log, sqrt
from sympy import factorint, primerange
def mul(a,b,N=None):
    x=a[0]*b[0]+2*a[1]*b[1]; y=a[0]*b[1]+a[1]*b[0]
    return (x%N,y%N) if N else (x,y)
def pw(a,k,N=None):
    r=(1,0)
    while k:
        if k&1: r=mul(r,a,N)
        a=mul(a,a,N); k>>=1
    return r
H={m:pw((1,1),m)[0] for m in range(1,1300,2)}
x,y=1,1;R={1:1}
for m in range(2,700):
    x,y=x+2*y,x+y
    if m%2:R[m]=x
print("[0] recurrence (v1) == fast power, odd m<700:",all(R[m]==H[m] for m in R))
print("[1] strong divisibility failures odd m,n<=301:",sum(1 for m in range(1,302,2) for n in range(1,302,2) if gcd(H[m],H[n])!=H[gcd(m,n)]))
print("[2] odd m<1300 with 3|h_m:",[m for m in H if H[m]%3==0])
print("[3] h_3p identity failures p<433:",[p for p in primerange(3,433) if H[3*p]!=H[p]*(4*H[p]**2+3)])
# [4] M-F3: direct membership enumeration. Family rho=(a,b): exact level d_rho(nu)=2h/gcd(b nu - a, 2h).
P=[(2,8),(-2,8),(2,16),(-2,16)]
for m in range(5,18,2):
    h=H[m]; M=2*h; multi=0; prim={r:0 for r in P}
    for nu in range(1,M,2):
        if gcd(nu,M)!=1: continue
        fams=[]
        for (a,b) in P:
            d=M//gcd((b*nu-a)%M,M)
            if d*d<=h: fams.append((a,b))
            if d==1: prim[(a,b)]+=1
        if len(fams)>=2: multi+=1
    print(f"[4] m={m} h={h}: units in >=2 families (levels<=sqrt h, primaries incl.): {multi}; primaries per family: {list(prim.values())}")
# [5] capacity base: CONSTANT ARITHMETIC (not numerics): log(mu^2/(lam^(1/6)lam^(1/2))) with |Z|=mu^m/2 assumed.
mu=1.9154712; lam=3+2*sqrt(2); xi=2.4586893
print("[5] capacity base mu*^2/lam^(2/3) =",mu**2/lam**(2/3)," ratio to 1.0184224:",mu**2/lam**(2/3)/1.0184224)
for p in [11,17,29,53,101,199]:
    m=3*p; lk=2*(m*log(mu)-log(2))-log(H[p])-log(H[m])
    print(f"    p={p} m={m} (log kappa)/m = {lk/m:.5f}  base {2.718281828459045**(lk/m):.5f}  (closed form; tends to the constant above)")
print("[5] L_m base mu^2/xi =",mu**2/xi," h_p base lam^(1/6) =",lam**(1/6)," sqrt h base lam^(1/4) =",lam**0.25)
# [6] M-F5(b): n_{h_p}/h_p = prod (q-2)/q over q|h_p (h_p squarefree checked), and lower bound 1-2*omega/(2p+1)
for p in primerange(5,62):
    f=factorint(H[p]); sqf=all(e==1 for e in f.values())
    n=1
    for q in f: n*=q-2
    om=len(f); lb=1-2*om/(2*p+1)
    print(f"[6] p={p}: squarefree={sqf} omega={om} min q={min(f)} (q=1 mod 2p: {all(q%(2*p)==1 for q in f)}) n/h_p={n/H[p]:.4f} >= 1-2w/(2p+1)={lb:.4f}: {n/H[p]>=lb}")
