"""N7 [N, sampling]: shell sums S_j = sum_{classes, N(alpha) in [2^j,2^{j+1})} |w(alpha)| for base 1/4 at q = h_p,
count of classes estimated from the asymptotic ideal count, mean |w| from n random classes (balanced generators).
usage: i_shells.py p jmin jmax n"""
import sys, json, math, random
from fractions import Fraction as Fr
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import *
p,jmin,jmax,n=map(int,sys.argv[1:5]); m=3*p; k=(p-1)//2; random.seed(7)
def xy(N):
    x,y=1,0
    for _ in range(N): x,y=x+2*y,x+y
    return x,y
def mul(u,v): return (u[0]*v[0]+2*u[1]*v[1], u[0]*v[1]+u[1]*v[0])
q=xy(p)[0]; g=(xy(k+1)[0],xy(k)[1]); S2=math.sqrt(2); EPS=1+S2
def rand_class(j):
    # uniform point in the fundamental domain {1/eps <= |a1/a2| < eps, 2^j <= |a1 a2| < 2^{j+1}} (log-coords uniform = Haar), round to lattice;
    while True:
        Nt=2**j*2**random.random(); r=EPS**(2*random.random()-1); s1=random.choice((1,-1)); s2=random.choice((1,-1))
        a1=s1*math.sqrt(Nt*r); a2=s2*math.sqrt(Nt/r); a=round((a1+a2)/2); b=round((a1-a2)/(2*S2))
        Nn=a*a-2*b*b
        if Nn%2 and 2**j<=abs(Nn)<2**(j+1): return (a,b),abs(Nn)
def twist(al):
    L=(1,0); w=mul(g,al); w=(q+w[0],w[1]); out=[]
    for i in range(m):
        v=mul(L,w); out.append(float(Fr(2*v[0],4*q)%1)); L=mul(L,(3,2))
    return out
h,nu=nu_rho(m,1); tw=TW(m,nu,L=8,K=16); Z0=Zbatch(tw,[[0.0]*m])[0]
# class count: #{ideals of odd norm in [X,2X)} ~ c X with c = (2 ln eps/sqrt8)*(1/2) * (fraction odd) -- calibrated empirically below from exact counts
res=[]
for j in range(jmin,jmax+1):
    al=[rand_class(j)[0] for _ in range(n)]
    Z=[]
    for i in range(0,n,32): Z+=list(Zbatch(tw,[twist(a) for a in al[i:i+32]]))
    a=[abs(z/Z0) for z in Z]; mean=sum(a)/n; mx=max(a); sd=(sum((x-mean)**2 for x in a)/(n-1))**.5
    rec=dict(j=j,mean=mean,sd=sd,max=mx,sumRe=sum((z/Z0).real for z in Z)/n); print(json.dumps(rec),flush=True); res.append(rec)
json.dump(dict(p=p,res=res),open(f'/workspace/bgs-lineN/N7/logs/i_shells_p{p}.json','w'),indent=1)
