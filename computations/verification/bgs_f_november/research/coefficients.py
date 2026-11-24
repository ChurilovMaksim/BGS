"""Build a rational Taylor polynomial for the kick and four finite carry matrices."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from collections import defaultdict
from fractions import Fraction as F
from math import ceil, factorial
from pathlib import Path
import json

Q=1<<61
K=209
DEG=16
OUT=Path(__file__).resolve().parent/"data"
OUT.mkdir(exist_ok=True)
def pell(n):
    h,v=1,0
    for _ in range(n):
        h,v=h+2*v,h+v
    return h
def add(tab,key,re,im):
    x,y=tab.get(key,(0,0))
    tab[key]=(x+re,y+im)
def multiply(P,G):
    T={}
    for (a,b),(x,y) in P.items():
        for (c,d),(s,t) in G.items():
            add(T,(a+c,b+d),x*s-y*t,x*t+y*s)
    return T
def raw_symbol():
    # 4r(q) in frequency coordinates. Entries here and below are integers.
    r={0:4,1:2,-1:2,7:-2,-7:-2,6:-1,-6:-1,8:-1,-8:-1}
    A={}
    for b in [-7,7]: add(A,(0,b),2000,0)
    add(A,(0,0),-400,0)
    for b,z in r.items():
        add(A,(0,b),100*z,0)
        for sign in [1,-1]:
            add(A,(0,b+sign),0,-5*sign*z)
            add(A,(sign,b),-3*z,-4*sign*z)
    return {d:v for d,v in A.items() if v!=(0,0)}
def nearest(x,den):
    return (2*x+den)//(2*den)
def make_kick():
    N=pell(K)
    xi=F(N,10**80)
    x=F(500136142312,10**12)
    A=raw_symbol()
    norm=F(sum(abs(i)+abs(j) for i,j in A.values()),4000)
    assert norm<F(6,5) and abs(x-xi)<F(1,10**12)
    # Use W(a,b)=(-1)^(ab)T(a,b), freeze its small continuous cocycle.
    G={}
    for (a,b),(re,im) in A.items():
        s=1-2*(a*b%2)
        G[a,b]=(-s*im,s*re) # i times physical Fourier symbol
    den0=x.denominator*4000
    den=den0**DEG*factorial(DEG)
    numer={}; power={(0,0):(1,0)}
    for t in range(DEG+1):
        scale=den//(den0**t*factorial(t))*x.numerator**t
        for d,(i,j) in power.items(): add(numer,d,i*scale,j*scale)
        if t<DEG: power=multiply(power,G)
    D={}; loss=0
    for (a,b),(i,j) in numer.items():
        # Exact l1 threshold, in Gaussian rational arithmetic
        if (abs(i)+abs(j))*10**11<=den:
            loss+=abs(i)+abs(j)
            continue
        s=1-2*(a*b%2)
        v,w=nearest(s*i*Q,den),nearest(s*j*Q,den)
        D[a,b]=v,w
    tail=2*(x*norm)**(DEG+1)/factorial(DEG+1)
    eps=tail+abs(x-xi)*norm+F(loss,den)+F(len(D),Q)+F(1,10**70)
    assert eps<F(8,10**10)
    phase=F(18*4*120*3,N)
    assert phase<F(1,10**70) and sum(abs(v)+abs(w) for v,w in D.values())<2*Q
    items={"polynomial_tail":tail,"parameter":abs(x-xi)*norm,"discarded_digits":F(loss,den),
           "quantization":F(len(D),Q),"weyl_phase_upper":phase,"combined_upper":eps}
    (OUT/"error_budget.json").write_text(json.dumps({n:{"exact":str(z),"approx":float(z)}
                                                      for n,z in items.items()},indent=2)+"\n")
    (OUT/"digits.json").write_text(json.dumps([[a,b,v,w] for (a,b),(v,w) in sorted(D.items())])+"\n")
    return D,eps
def make():
    N=pell(K);D,eps=make_kick()
    rad=max(abs(a)+F(1415,1000)*abs(b) for a,b in D)
    u=rad/F(482,100); v=rad/F(828,1000)
    R=ceil(u+v)+1
    U=ceil(2000*u)+R; V=ceil(2000*v)+R
    summary=dict(k=K,N=str(N),Q=str(Q),digits=len(D),epsilon_upper="8e-10",epsilon_approx=float(eps),box=R,shapes=[])
    for i in range(2):
        for j in range(2):
            states=[(X,Y) for X in range(-R,R+1) for Y in range(-R,R+1)
                    if X%2==i and Y%2==j and abs(1000*X+1414*Y)<=U and abs(1000*X-1414*Y)<=V]
            lookup={s:n for n,s in enumerate(states)}
            with (OUT/f"H{i}{j}.txt").open("w") as f:
                f.write(f"{len(states)}\n")
                for t,(X,Y) in enumerate(states):
                    A,B=3*X+4*Y,2*X+3*Y
                    for (a,b),(x,y) in D.items():
                        row=lookup.get((A+2*a,B+2*b))
                        if row is not None:
                            z=(-N*(a*B-b*A))%4
                            re,im=((x,y),(-y,x),(-x,-y),(y,-x))[z]
                            f.write(f"{row} {t} {re} {im}\n")
            summary["shapes"].append(len(states))
    assert max(summary["shapes"])<3000 and R<300
    (OUT/"bounds.json").write_text(json.dumps(summary,indent=2)+"\n")
    print(summary)
if __name__=="__main__":make()
