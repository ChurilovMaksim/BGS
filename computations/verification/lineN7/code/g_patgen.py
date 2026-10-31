"""N7 Lemma P' check [exact integers + mpmath 600 digits]: for iso points x = z + e*gamma/(8q) (z in {1/4 (twist 1/2), 0}), every i in [0,m):
Tr(lam^i x) - Tr(z) == Tr(W1_i) == Tr(W2_i) + Tr(c_i) (mod 1), W1_i = lam^i e gamma/(8q),
W2_i = e[eps^{2i-3k-1} - (-1)^k eps^{2i-k}]/(8 sqrt2 q), c_i = e eps^{2i-k}/(4 sqrt2) (in (1/4sqrt2)O; Tr(c_i) in (1/2)Z, constant in i).
Also reports the core seeds zeta_A = e eps^{-(k mod 2)}/(4 sqrt2) check: deviation at i = floor(k/2)+j vs Tr(lam^j zeta_A) for |j|<=3."""
import sys, json, mpmath as mp
from fractions import Fraction as Fr
mp.mp.dps=600
s2=mp.sqrt(2); E=1+s2; Ec=1-s2
def xy(n):
    x,y=1,0
    for _ in range(n): x,y=x+2*y,x+y
    return x,y
def mul(u,v): return (u[0]*v[0]+2*u[1]*v[1], u[0]*v[1]+u[1]*v[0])
def emb(u): return (u[0]+u[1]*s2, u[0]-u[1]*s2)
def frac(x): return x-mp.floor(x)
def d1(a,b): t=frac(a-b); return min(t,1-t)
out=[]
for p in (19,29,47,59):
    k=(p-1)//2; m=3*p; q=xy(p)[0]; g=(xy(k+1)[0],xy(k)[1])
    for base,es in (('1/4',[(2,0),(-2,-4),(-6,0),(-2,6),(-10,-2)]),('0',[(0,2),(-4,-2),(0,6)])):
        for e in es:
            eg=mul(e,g); E1,E2=emb(e); mx=0; mx2=0; trc=set()
            L=(1,0)
            for i in range(m):
                v=mul(L,eg); tex=Fr(2*v[0],8*q)            # Tr(lam^i e gamma/(8q)) exact
                W2=[E1*(E**(2*i-3*k-1)-(-1)**k*E**(2*i-k))/(8*s2*q), E2*(Ec**(2*i-3*k-1)-(-1)**k*Ec**(2*i-k))/(-8*s2*q)]
                c=[E1*E**(2*i-k)/(4*s2), E2*Ec**(2*i-k)/(-4*s2)]
                trc.add(str(mp.nint(2*(c[0]+c[1]))%2))
                t=mp.mpf(tex.numerator)/tex.denominator
                mx=max(mx,d1(t,W2[0]+W2[1]+c[0]+c[1]))
                L=mul(L,(3,2))
            # core A check
            zA=[E1*E**(-(k%2))/(4*s2), E2*Ec**(-(k%2))/(-4*s2)]
            for j in range(-3,4):
                i=k//2+j; L=(1,0)
                for _ in range(i%m): L=mul(L,(3,2))
                v=mul(L,eg); t=mp.mpf(Fr(2*v[0],8*q).numerator)/Fr(2*v[0],8*q).denominator if False else mp.mpf(2*v[0])/(8*q)
                mx2=max(mx2,d1(t,zA[0]*E**(2*j)))   # core: d == emb1(lam^j zeta) (mod 1), zeta = e eps^{-(k mod 2)}/(4 sqrt2)
            rec=dict(p=p,base=base,e=e,N=e[0]**2-2*e[1]**2,max_err_W2=float(mx),Trc_classes=sorted(trc),max_err_coreA=float(mx2))
            print(json.dumps(rec)); out.append(rec)
json.dump(out,open('/workspace/bgs-lineN/N7/logs/g_patgen.json','w'),indent=1)
