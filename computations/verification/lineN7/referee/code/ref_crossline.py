"""Referee [N]: at composite h_p = q1*q2, fully isotropic beta (N(beta)=0 mod d, nonzero mod both q_i) lie on 4 'lines'
(sign of sqrt2 mod q1) x (sign mod q2).  Only 2 of them are the lines (gamma), (gamma-bar) of Lemma P'(i); the other 2 ('cross lines',
ideal q1 * q2-bar) are NOT covered by identity (I).  Sample |Zhat/Z| per sign pattern and form ratio = count*E|Zhat/Z| / (4p Re w_fam)
(full isotropic weight n_d on both sides).  usage: p N seed"""
import os; os.environ.setdefault('OMP_NUM_THREADS','2'); os.environ.setdefault('OPENBLAS_NUM_THREADS','2')
import sys, json, random, numpy as np
from sympy import factorint, sqrt_mod
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import Zbatch, nu_rho, TW
p,N,seed=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]); m=3*p; random.seed(seed)
def xy(n):
    x,y=1,0
    for _ in range(n): x,y=x+2*y,x+y
    return x,y
d=xy(p)[0]; q1,q2=sorted(factorint(d)); w1,w2=int(sqrt_mod(2,q1)),int(sqrt_mod(2,q2))
def crt(b1,b2):
    u1=q2*pow(q2,-1,q1); u2=q1*pow(q1,-1,q2)
    return ((b1[0]*u1+b2[0]*u2)%d,(b1[1]*u1+b2[1]*u2)%d)
def tw_seq(b):
    L=(1,0); out=[]
    for i in range(m):
        v=((L[0]*b[0]+2*L[1]*b[1])%d,(L[0]*b[1]+L[1]*b[0])%d); out.append((2*v[0]%d)/d); L=((3*L[0]+4*L[1])%d,(2*L[0]+3*L[1])%d)
    return out
h,nu=nu_rho(m,1); tw=TW(m,nu,L=8,K=16); Z0=Zbatch(tw,[[0.0]*m])[0]
# Binet gamma = x_{k+1} + y_k sqrt2 ; its sign pattern mod q1,q2
k=(p-1)//2; gx=xy(k+1)[0]; gy=xy(k)[1]
pat_g=tuple(1 if (gx-w*gy)%q==0 else (-1 if (gx+w*gy)%q==0 else 0) for q,w in ((q1,w1),(q2,w2)))
out=dict(p=p,d=d,q1=q1,q2=q2,N=N,gamma_pattern=pat_g,patterns={})
for s1 in (1,-1):
    for s2 in (1,-1):
        pts=[]
        for _ in range(N):
            y1=random.randrange(1,q1); y2=random.randrange(1,q2)
            pts.append(tw_seq(crt(((s1*w1*y1)%q1,y1),((s2*w2*y2)%q2,y2))))
        Z=[]
        for i in range(0,N,64): Z+=list(Zbatch(tw,pts[i:i+64]))
        a=np.abs(np.array(Z))/abs(Z0); cnt=(q1-1)*(q2-1)
        rel=(s1,s2) in (pat_g,(-pat_g[0],-pat_g[1]))
        out['patterns'][f'{s1},{s2}']=dict(gamma_line=bool(rel),mean=float(a.mean()),max=float(a.max()),
            ratio=float(cnt*a.mean()/(4*p*3.43578e-4)),ratio_se=float(cnt*a.std()/np.sqrt(N)/(4*p*3.43578e-4)))
        print(s1,s2,json.dumps(out['patterns'][f'{s1},{s2}']),flush=True)
json.dump(out,open(f'logs/ref_crossline_p{p}.json','w'),indent=1)
