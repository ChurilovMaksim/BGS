"""Auditor's independent exact check of E1 (rational arithmetic, no author code).
For odd m: nu* = odd lift of -4^{-1} mod h; check for random integer n that
   -nu* y' Nm(alpha_n)/g'  ==  (1/2) n^T H^{-1} n + kappa (sum n)^2/8   (mod 1)
with Nm computed in Z[lambda] (a+b*lam, lam^2=6lam-1) and H^{-1} by exact rational Gauss-Jordan (sympy)."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import sys, random, math; sys.path.insert(0,'.')
from fractions import Fraction as Fr
import sympy as sp
from aud import data, nustar
def Nm_alpha(n):
    a,b=0,0; pa,pb=1,0               # lam^j = pa + pb lam
    for nj in n:
        a+=nj*pa; b+=nj*pb; pa,pb=-pb,pa+6*pb
    return a*a+6*a*b+b*b
def Hinv(m):
    H=sp.zeros(m,m)
    for i in range(m):
        H[i,i]+=6; H[i,(i+1)%m]-=1; H[(i+1)%m,i]-=1
    return H.inv()
def frac(x): return x-math.floor(x)
random.seed(1)
res=[]
for m in range(5,42,2):
    d=data(m); h,gp,yp=d['h'],d['gp'],d['yp']; nu=nustar(m)
    k=(-4*nu-1)//h; assert (-4*nu-1)%h==0 and k%2==1
    kap=(k*yp)%8
    Hi=Hinv(m) if m<=25 else None
    ok=True; ntest=40 if m<=25 else 0
    for t in range(ntest):
        n=[random.randint(-5,5) for _ in range(m)]
        lhs=frac(Fr(-nu*yp*Nm_alpha(n),gp))
        q=sum(Fr(int(sp.numer(Hi[i,j])),int(sp.denom(Hi[i,j])))*n[i]*n[j] for i in range(m) for j in range(m))
        rhs=frac(q/2+Fr(kap*sum(n)**2,8))
        ok&=(lhs==rhs)
    # control: nu*+2 must fail somewhere
    n=[1]+[0]*(m-1); bad=frac(Fr(-(nu+2)*yp*Nm_alpha(n),gp))!=frac(Fr(int(sp.numer(Hi[0,0])),int(sp.denom(Hi[0,0])))/2+Fr(kap,8)) if Hi is not None else None
    # minus residue: nu-=odd lift of +4bar: expect conj form -(1/2)q - kappa(sum)^2/8
    num=nustar(m,-1); okm=True
    for t in range(ntest):
        n=[random.randint(-5,5) for _ in range(m)]
        lhs=frac(Fr(-num*yp*Nm_alpha(n),gp))
        q=sum(Fr(int(sp.numer(Hi[i,j])),int(sp.denom(Hi[i,j])))*n[i]*n[j] for i in range(m) for j in range(m))
        okm&=(lhs==frac(-q/2-Fr(kap*sum(n)**2,8)))
    print(f'm={m} h={h} nu*={nu} k={k} kappa={kap} m%8={m%8} identity_ok={ok} (ntest={ntest}) control_fails={bad} minus_residue_conj_ok={okm} gcd(y\',2h)={math.gcd(yp,gp)}',flush=True)
