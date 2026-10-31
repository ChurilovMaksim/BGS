"""N7 pattern lemma check [exact integer arithmetic + mpmath 200 digits]:
gamma = x_{k+1} + y_k sqrt2 (p=2k+1) has norm h_p; twist tau_i := Tr(lam^i (q+gamma))/(4q) mod 1 (computed exactly with integers) equals
1/2 + d1_i and 1/2 + d2_i (mod 1) with the closed forms of REPORT_N7 sec 3; also compare with the N5/N6 family twist sequence (b_family gen/ok/taus_of)
up to cyclic shift / sign / conjugation, and with Zhat ratio.  usage: b_pattern.py p1,p2,..."""
import sys, json, mpmath as mp
from fractions import Fraction as Fr
mp.mp.dps=400
sys.path.insert(0,'/workspace/bgs-lineN/N6/code')
def xy(n):
    x,y=1,0
    for _ in range(n): x,y=x+2*y,x+y
    return x,y
def mul(u,v): return (u[0]*v[0]+2*u[1]*v[1], u[0]*v[1]+u[1]*v[0])
E=1+mp.sqrt(2)
out=[]
for p in [int(t) for t in sys.argv[1].split(',')]:
    k=(p-1)//2; q=xy(p)[0]; g=(xy(k+1)[0],xy(k)[1])
    assert g[0]**2-2*g[1]**2==q, (p,g)
    D=E**(2*k+1)-E**(-(2*k+1)); assert abs(D-2*q)<mp.mpf(10)**-150
    s=2*mp.sqrt(2); maxerr1=0; maxerr2=0; seq=[]
    lam=(3,2); L=(1,0); w=(q+g[0],g[1])
    for i in range(p):
        v=mul(L,w); num=2*v[0]                                   # Tr((a+b sqrt2)) = 2a
        tau=Fr(num,4*q)%1; seq.append(tau)
        d1=(E**(2*i+k+1)+E**(k-2*i)+(-1)**k*(E**(-2*i-k-1)-E**(2*i-k)))/(D*s)
        n=2*i-k; yn=xy(abs(n))[1]*(1 if n>=0 else (-1)**(n+1))     # y_n for negative n: eps^{-n}=(-1)^n eps'^n
        d2=d1-yn
        t=mp.mpf(tau.numerator)/tau.denominator
        e1=abs(((t-mp.mpf(1)/2-d1)+mp.mpf(1)/2)%1-mp.mpf(1)/2); e2=abs(((t-mp.mpf(1)/2-d2)+mp.mpf(1)/2)%1-mp.mpf(1)/2)
        maxerr1=max(maxerr1,e1); maxerr2=max(maxerr2,e2)
        L=mul(L,lam)
    # pattern: deviations from 1/2 and junction values
    dev=[float(((mp.mpf(t.numerator)/t.denominator-mp.mpf(1)/2+mp.mpf(1)/2)%1)-mp.mpf(1)/2) for t in seq]
    rec=dict(p=p,k=k,q=str(q) if q>10**15 else q,gamma=[str(g[0]),str(g[1])],max_mod1_err_d1=float(maxerr1),max_mod1_err_d2=float(maxerr2),
             slow_count=sum(abs(x)<0.05 for x in dev),dev_head=[round(x,6) for x in dev[:3]],
             junction=[round(dev[i],7) for i in range(k//2-2,k//2+3)], junction2=[round(dev[i%p],7) for i in range((3*k+1)//2-2,(3*k+1)//2+3)])
    print(json.dumps(rec),flush=True); out.append(rec)
json.dump(out,open('/workspace/bgs-lineN/N7/logs/b_pattern.json','w'),indent=1)
