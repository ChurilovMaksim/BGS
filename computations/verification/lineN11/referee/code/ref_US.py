"""Referee N9b: independent recompute of |r| for small-beta unit points (|a|,|b|<=3), twists tau_i = 2*a_i/d where
lambda^i beta = a_i + b_i sqrt2 mod d, d = h_p; r = Z(beta)/Z(0) via N6 twb (L=8,K=16), m=3p."""
import os; os.environ.setdefault('OMP_NUM_THREADS','4')
import sys, json
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import Zbatch, nu_rho, TW
p=int(sys.argv[1]); m=3*p
def xy(n):
    x,y=1,0
    for _ in range(n): x,y=x+2*y,x+y
    return x,y
d=xy(p)[0]
def seq(b):
    a,c=b; s=[]
    for i in range(m):
        s.append((2*a % d)/d); a,c=(3*a+4*c)%d,(2*a+3*c)%d
    return s
B=[(a,b) for a in range(-3,4) for b in range(-3,4) if (a,b)!=(0,0) and (a*a-2*b*b)%d]
h,nu=nu_rho(m,1); tw=TW(m,nu,L=8,K=16); Z0=Zbatch(tw,[[0.0]*m])[0]
Z=[]
for i in range(0,len(B),24): Z+=list(Zbatch(tw,[seq(b) for b in B[i:i+24]]))
r=sorted(((abs(z/Z0),b) for z,b in zip(Z,B)),reverse=True)
out=dict(p=p,n=len(B),top=[(x,b) for x,b in r[:6]])
print(json.dumps(out)); json.dump(out,open(f'logs/ref_US_p{p}.json','w'))
