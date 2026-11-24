"""Check arithmetic strata, first harmonic and Weyl trace phases independently."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd
from pathlib import Path
import json
import sys

import numpy as np

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'research'))
from coefficients import raw_symbol

def mul(x,y,n):
    a,b=x;c,d=y
    return (a*c+2*b*d)%n,(a*d+b*c)%n

def power(m,n):
    a=(1,0)
    g=(3,2)
    while m:
        if m&1:
            a=mul(a,g,n)
        g=mul(g,g,n)
        m//=2
    return a

def order7(x,cap):
    if not x:
        return cap
    ans=0
    while x%7==0 and ans<cap:
        x//=7
        ans+=1
    return ans

def sqrt_two(k):
    r=3;n=7
    for _ in range(1,k):
        r=next(r+i*n for i in range(7) if ((r+i*n)**2-2)%(7*n)==0)
        n*=7
    return r

def cayley_checks():
    results=[]
    for k in (3,4,5,6):
        N=7**k
        o=3*N//7
        rho=sqrt_two(k)
        p=Counter()
        seen=[set(),set()]
        for m in range(1,o+1):
            a,b=power(m,N)
            val=min(order7(a-1,k),order7(b,k))
            want=min(k,1+order7(m,k)) if m%3==0 else 0
            assert val==want
            p[val]+=1
            if m%3:
                z=(a+rho*b)%N
                cayley=(-b*pow(4*(a-1),-1,N))%N
                assert cayley==(-(z+1)*pow(4*rho*(z-1),-1,N))%N
                seen[m%3-1].add(cayley)
        assert seen==[set(range(5,N,7)),set(range(2,N,7))]
        results.append(dict(k=k,period=o,classes=dict(sorted(p.items()))))
    return results

def label_phases(n,k):
    # Direct matrix evaluation after constructing the original Gaussian kernel.
    x,y=np.indices((n,n))
    mtx=np.exp(2j*np.pi*((-pow(8,-1,n)*(3*x*x-2*x*y+3*y*y))%n)/n)/np.sqrt(n)
    rho=sqrt_two(k)
    inv2=pow(2,-1,n); inv4=pow(4,-1,n)
    support=list(raw_symbol())
    errors=[]
    for m in (1,2,3,4,5,9,21,3*n//7):
        M=np.linalg.matrix_power(mtx,m)
        den=np.trace(M)
        a,b=power(m,n)
        val=min(k,1+order7(m,k)) if m%3==0 else 0
        mod=7**val
        worst=abs(abs(den)-mod)
        for d in [(0,0),(1,2),(0,7),(7,7),(0,49),(49,49)]:
            ratio=(np.exp(2j*np.pi*((d[1]*(np.arange(n)+inv2*d[0]))%n)/n)
                   *M[(np.arange(n)+d[0])%n,np.arange(n)]).sum()/den
            if d[0]%mod or d[1]%mod:
                ref=0j
            elif val==k:
                ref=1+0j
            else:
                q=n//mod
                c=power(m,n*mod*mod)
                u=(c[0]-1)//mod
                b0=c[1]//mod
                determinant=(u*u-2*b0*b0)%q
                x0,y0=d[0]//mod,d[1]//mod
                pair=pow(determinant,-1,q)*b0*(x0*x0-2*y0*y0)
                phase=pow(2,-1,q)*pair%q
                ref=np.exp(2j*np.pi*phase/q)
            worst=max(worst,abs(ratio-ref))
        if m%3:
            c=(-inv4*b*pow(a-1,-1,n))%n
            z=(a+rho*b)%n
            A=(c-inv4*pow(rho,-1,n))%n
            B=(c+inv4*pow(rho,-1,n))%n
            assert gcd(A*B,n)==1
            for r in (2,3,4,6):
                ds=[support[(i**2+3*m+i*r)%len(support)] for i in range(r)]
                js=[i*i+m*i+1 for i in range(r)]
                path=np.eye(n,dtype=complex)
                for i,d in zip(js,ds):
                    x,y=power(i,n)
                    aa,bb=(x*d[0]+2*y*d[1])%n,(y*d[0]+x*d[1])%n
                    pos=np.arange(n)
                    phase=np.exp(2j*np.pi*((bb*(pos+inv2*aa))%n)/n)
                    # Right multiplication by the Weyl operator.
                    path=(path*phase[None,:])[:,(pos-aa)%n]
                direct=np.trace(path@M)/den
                E=c*sum(x*x-2*y*y for x,y in ds)
                plus=[(x+rho*y)%n for x,y in ds]
                minus=[(x-rho*y)%n for x,y in ds]
                zs=[(x+rho*y)%n for x,y in [power(i,n) for i in js]]
                for i in range(r):
                    for j in range(i+1,r):
                        z1=zs[i]*pow(zs[j],-1,n)%n
                        E+=A*plus[i]*minus[j]*z1+B*minus[i]*plus[j]*pow(z1,-1,n)
                estimated=np.exp(2j*np.pi*(E%n)/n)
                worst=max(worst,abs(direct-estimated))
        assert worst<1e-9
        errors.append(dict(m=m,trace_error=float(worst)))
    return dict(N=n,errors=errors)

def main():
    norm=Counter()
    for (a,b),(x,y) in raw_symbol().items():
        norm[a*a-2*b*b]+=x
    norm={u:v for u,v in norm.items() if v}
    assert norm=={-128:-200,-127:12,-98:3600,-97:24,-72:-200,-71:12,-2:400,-1:-24,1:-24}
    var=Fraction(sum((norm.get(-i,0)-norm.get(i,0))**2 for i in range(1,129)),2*2000**2)
    assert var == Fraction(412527,250000)
    algebra=dict(coefficients=dict(sorted(norm.items())),slope_variance=str(var),cayley=cayley_checks())
    numerical=[label_phases(n,k) for n,k in ((49,2),(343,3))]
    data=dict(algebra=algebra,numerical=numerical)
    if '--verify' in sys.argv:
        given=json.loads((Path(__file__).resolve().parent/'data/checks.json').read_text())
        assert given['algebra']==json.loads(json.dumps(algebra))
        print('Arithmetic classes, exact coefficients and direct matrix trace phases verified.')
    else:
        print(json.dumps(data,indent=2))

if __name__=='__main__':
    main()
