import sys, cmath, math, numpy as np
sys.path.insert(0,'/workspace/bgs-lineI/code')
from law import mdata
from sympy import factorint, n_order
def h(n):
    a,b=1,1
    for _ in range(n-1): a,b=a+2*b,a+b
    return a
for p in (5,7,11,13,17,19,23):
    hp=h(p); K=4*hp*hp+3
    assert h(3*p)==hp*K
    f=factorint(K) if K<10**30 else None
    # rank of lambda mod prime r: smallest d with lambda^d = 1 mod r (lambda=3+2sqrt2)
    def rank(r):
        for d in sorted(set(x for x in range(1,3*p+1) if (3*p)%x==0)):
            a,b=1,0
            for _ in range(d): a,b=(3*a+4*b)%r,(2*a+3*b)%r
            if a==1 and b==0: return d
    print(p, 'gcd',math.gcd(hp,K), 'K factors', {r:(e,rank(r)) for r,e in f.items()} if f else 'big', flush=True)
# S2 Gauss L1 norm at even M' with actual coefficient
for m,q in ((9,199),(9,7),(21,239),(15,41)):
    d=mdata(m); H=d['h']; yp=d['yp']; M=2*H
    nu0=next(x for x in range(1,M,2) if (8*x-2)%M==0)
    Mp=M//q; b=pow(q,-1,Mp); c=nu0*yp
    k=(c*b)%Mp
    A=np.arange(Mp)
    X,Y=np.meshgrid(A,A,indexing='ij')
    psi=np.exp(-2j*np.pi*((k*(X*X-2*Y*Y))%Mp)/Mp)
    F=np.fft.fft2(psi)/Mp**2
    print('m',m,'q',q,"M'",Mp,'gcd(k,M\')',math.gcd(k,Mp),'sum|Fhat|',np.abs(F).sum(),'max|Fhat|*M\'',np.abs(F).max()*Mp,'support',(np.abs(F)>1e-9).sum(),'of',Mp*Mp)
