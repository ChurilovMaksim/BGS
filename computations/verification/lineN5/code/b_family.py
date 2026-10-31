"""N5 (B) [N]: the dominant isotropic family (sector-4 depth 16D=1) at q = h_p for many p.
h_p = x_p (eps^p = x_p + y_p sqrt2).  gamma = generator of a prime above q (|N gamma| = q), chosen among +-eps^j gamma0 with q+gamma in 4O + q sqrt2 O,
y = (q+gamma)/(4q),  tau_i = Tr(lam^i y) mod 1 (exact rationals).  Model Z = Tr prod V - Tr prod E over m = 3p steps (as a_model.py; at (21,239)
it equals 2.0 x |Zhat| of the top TRACE-206 point).  Reports |Z|^{1/m}, the family rate (4p (q-2)/q^2 |Z|/2)^{1/m}, and the slow-window length."""
import sys, json, math, numpy as np
from sympy import isprime, sqrt_mod
sys.path.insert(0,'/workspace/bgs-lineF/code'); sys.path.insert(0,'/workspace/bgs-lineN/N5/code')
from a_model import zmodel
def hp(p):
    x,y=1,1
    for _ in range(p-1): x,y=x+2*y,x+y
    return x
def gen(q):
    """Gauss-reduce the lattice {(a,b): a = r b mod q} for the form a^2+2b^2; the shortest vector has |a^2-2b^2| = q (Minkowski: a^2+2b^2 <= 1.64 q)."""
    r=int(sqrt_mod(2,q)); u=(q,0); v=(r,1)
    f=lambda w: w[0]*w[0]+2*w[1]*w[1]; dot=lambda w,z: w[0]*z[0]+2*w[1]*z[1]
    if f(u)<f(v): u,v=v,u
    while True:
        k=round(dot(u,v)/f(v)) if f(v) else 0
        k=(2*dot(u,v)+f(v))//(2*f(v))
        u=(u[0]-k*v[0],u[1]-k*v[1])
        if f(u)>=f(v): break
        u,v=v,u
    for w in (v,u):
        if abs(w[0]**2-2*w[1]**2)==q: return w
    raise RuntimeError('no generator')
def mul(u,v): return (u[0]*v[0]+2*u[1]*v[1], u[0]*v[1]+u[1]*v[0])
def ok(q,g):
    # q+gamma in 4O + q sqrt2 O : (q+a) + b sqrt2 ;  4O + q sqrt2 O = {(c,d): c = 4 c1, d = 4 d1 + q c2 sqrt... } compute: elements 4(u+v s2) + q s2 (w+z s2) = (4u+2qz) + (4v+qw) s2
    c,d=q+g[0],g[1]
    # need c = 4u + 2q z, d = 4v + q w  -> d any mod gcd(4,q)=1: always solvable; c mod gcd(4,2q)=2: c even
    return c%2==0
P=[int(t) for t in sys.argv[1].split(',')]; res=[]
for p in P:
    q=hp(p)
    if not isprime(q): print('p',p,'h_p not prime'); continue
    g0=gen(q); eps=(1,1); cands=[]
    g=g0
    for j in range(2*p):
        for s in (1,-1):
            gg=(s*g[0],s*g[1])
            if ok(q,gg): cands.append(gg)
        g=mul(g,eps)
    # twist values for each candidate; keep distinct orbits (by sorted twist multiset)
    seen={}; m=3*p
    for gg in cands:
        A,B=q+gg[0],gg[1]   # 4q*y = q+gamma
        tw=[]
        for i in range(m):
            tw.append(((2*A)%(4*q))/(4*q)); A,B=3*A+4*B,2*A+3*B
            A%=(4*q); B%=(4*q)
        key=tuple(sorted(set(round(t,12) for t in tw)))
        if key not in seen: seen[key]=tw
    for key,tw in seen.items():
        z=zmodel(tw); slow=sum(1 for t in tw[:p] if min(abs(t-0.5),1-abs(t-0.5))<0.05)
        rec=dict(p=p,q=q,absZ=float(abs(z)),root=float(abs(z))**(1/m) if z!=0 else 0,
                 family_rate=float(4*p*(q-2)/q**2*abs(z)/2)**(1/m),slow_steps_per_period=slow,logq=math.log(q)/math.log(3+2*math.sqrt(2)))
        res.append(rec); print(json.dumps(rec),flush=True)
json.dump(res,open('logs/b_family.json','w'),indent=1)
