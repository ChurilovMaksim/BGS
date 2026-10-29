# Driver for engine.cpp: exact large-p expansions (mode 0) and exact per-prime values (mode P).
import subprocess, sys, math, os
from fractions import Fraction as F
HERE = os.path.dirname(os.path.abspath(__file__))

def wseries(N):
    """w(n) with sum_n w(n) t^n/n! = log sum_n t^n/(n!)^2 (independent recomputation)."""
    a = [F(1, math.factorial(n)**2) for n in range(N+1)]
    l = [F(0)]*(N+1)
    for n in range(1,N+1):
        l[n] = (n*a[n] - sum(k*l[k]*a[n-k] for k in range(1,n)))/n
    return [l[n]*math.factorial(n) for n in range(N+1)]

def setpartitions(m, dmax):
    out=[]
    def rec(j, x, k):
        if j==m:
            if m-k<=dmax: out.append(tuple(x))
            return
        if m - (k + (m-j)) > dmax: return
        for v in range(k+1):
            x.append(v); rec(j+1, x, max(k, v+1)); x.pop()
    rec(0, [], 0); return out

def canon(x):
    m=len(x); best=None
    for refl in (False,True):
        for s in range(m):
            y=[x[(s + (-j if refl else j))%m] for j in range(m)]
            mp={}; z=tuple(mp.setdefault(v,len(mp)) for v in y)
            if best is None or z<best: best=z
    return best

def orbits(m,dmax):
    orb={}
    for x in setpartitions(m,dmax):
        c=canon(x); orb[c]=orb.get(c,0)+1
    return orb

def run_engine(m, mode, maxk2, nth=8, dmax=None, raw=False):
    if dmax is None: dmax = min(maxk2//2, m-1)
    orb = orbits(m, dmax)
    w = wseries(m)
    inp = "\n".join(",".join(map(str,c)) for c in orb)+"\n"
    out = subprocess.run([HERE+'/engine',str(m),str(mode),str(maxk2),str(nth)],input=inp,capture_output=True,text=True,check=True).stdout
    terms={}; bydr={}
    cur=None
    for line in out.splitlines():
        t=line.split()
        if t[0]=='RHO':
            x=tuple(map(int,t[1].split(','))); n=max(x)+1
            mult=[x.count(v) for v in range(n)]
            W=F(1); s=1
            for c in mult: W*=w[c]; s*=math.factorial(c)
            multb=int(t[4].split('=')[1]); d=m-n
            cur = orb[x]*W*s*F(m,multb)
        else:
            k2,r,D,c = int(t[1]),int(t[2]),int(t[3]),int(t[4])
            key=(k2,r,D); terms[key]=terms.get(key,0)+cur*c
            kk=(d,r,D); bydr[kk]=bydr.get(kk,0)+cur*c
    return (terms,bydr) if raw else terms

def legendre(a,p):
    a%=p
    if a==0: return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

def evaluate(terms, p, symbolic=True, maxk2=None):
    """(rational part, coefficient of sqrt(p)); for p = 3 mod 4 asserts the imaginary part vanishes."""
    re=F(0); sq=F(0); im=F(0)
    for (k2,r,D),c in terms.items():
        if maxk2 is not None and k2>maxk2: continue
        chi = legendre(D,p) if symbolic else D
        if chi==0: raise ValueError("p divides D")
        val = c*chi; e = F(1, p**(k2//2))
        if p%4==1:
            if k2%2==0: re+=val*e
            else: sq+=val*e/p
        else:
            if r%2==0: re += val*e*(1 if r%4==0 else -1)
            else: im += val*e*(1 if r%4==1 else -1)/p
    if p%4==3: assert im==0, ("imag part nonzero", p, im)
    return re, sq

def expansion(terms):
    """{(k2, cls): {|D|: coeff}}: coefficient of p^{-k2/2} for p = cls mod 4, as sum_D coeff*(|D|/p)."""
    out={}
    for (k2,r,D),c in terms.items():
        if c==0: continue
        for cls in (1,3):
            if cls==1: coef=c
            else:
                if r%2==1: continue
                coef=c*(1 if r%4==0 else -1)
                if D<0: coef=-coef
            key=(k2,cls); out.setdefault(key,{}); out[key][abs(D)]=out[key].get(abs(D),0)+coef
    return {k:{d:v for d,v in dd.items() if v!=0} for k,dd in sorted(out.items())}

def fmt(dd):
    if not dd: return "0"
    parts=[]
    for D in sorted(dd):
        v=dd[D]; parts.append(f"{v}" if D==1 else f"{v}*({D}/p)")
    return " + ".join(parts)
