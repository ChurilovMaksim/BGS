"""N8b [N] p-uniformity of c-line class ratios.  A class at (p, c | h_p, consistent line) with representative beta (Lin convention,
point beta/c) is rewritten as x = z + e*gamma_p/(8 q) (q = h_p, gamma_p = x_{k+1}+y_k sqrt2, N7 Lemma P'), e = +-Y*conj(gamma_p)/c in O,
Y = centred residue of 8*beta mod c (Y in frak c), z = (8 beta - Y)/(8c) in (1/8)O.  Check exactly that Tr(z)+Tr(lam^i e gamma_p)/(8q)
reproduces tau_i(beta), then evaluate the SAME (z,e) at other p' (x' = z + e gamma_{p'}/(8 q_{p'})) and compare Zhat/Z.
usage: d_puni.py p c s [p' ...]   (env RANK=3: c | K_p, use gamma_{3p}, q = h_{3p})"""
import sys, os, json, math, numpy as np
RK=int(os.environ.get('RANK','1'))
from fractions import Fraction as Fr
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import *
p=int(sys.argv[1]); c=int(sys.argv[2]); s=int(sys.argv[3]); P2=[int(a) for a in sys.argv[4:]]
def xy(n):
    x,y=1,0
    for _ in range(n): x,y=x+2*y,x+y
    return x,y
def mul(u,v): return (u[0]*v[0]+2*u[1]*v[1], u[0]*v[1]+u[1]*v[0])
def gam(P,conj=False):
    P=RK*P; k=(P-1)//2; g=(xy(k+1)[0],xy(k)[1]); g=(g[0],-g[1]) if conj else g; return g, xy(P)[0], g[0]**2-2*g[1]**2
m=3*p; k3=(m-1)//2; g3=(xy(k3+1)[0],xy(k3)[1])
beta=((s*g3[0])%c,(s*g3[1])%c)
cen=lambda x:(x%c)-c if (x%c)>c//2 else x%c
Y=(cen(8*beta[0]),cen(8*beta[1]))
# z must be a genuine lam-fixed point: 8z in sqrt2*O (fixed points (sqrt2/8)O / O^vee, 4 of them) -> 8beta - Y in c*sqrt2*O
if ((8*beta[0]-Y[0])//c)%2:
    cands=[(Y[0]+c,Y[1]),(Y[0]-c,Y[1])]; Y=min(cands,key=lambda u:abs(u[0]**2-2*u[1]**2))
g,q,Ng=gam(p); assert abs(Ng)==q and q%c==0
CONJ=False; gb=(g[0],-g[1]); t=mul(Y,gb)
if not (t[0]%c==0 and t[1]%c==0):
    CONJ=True; t=mul(Y,g)       # line consistent with conj(gamma_p): use x = z + e*conj(gamma_p)/(8q)
assert t[0]%c==0 and t[1]%c==0
e=(t[0]//c,t[1]//c)
if Ng<0: e=(-e[0],-e[1])          # gamma/(q) = conj(gamma)^{-1} * sign
zn=(8*beta[0]-Y[0],8*beta[1]-Y[1]); assert zn[0]%c==0 and zn[1]%c==0; z8=(zn[0]//c,zn[1]//c)   # 8z
def twists(P,mm):
    gP,qP,_=gam(P,CONJ); w=mul(e,gP); L=(1,0); out=[]
    for i in range(mm):
        v=mul(L,w); out.append(float((Fr(2*z8[0],8)+Fr(2*v[0],8*qP))%1)); L=mul(L,(3,2))
    return out
tau=taus_of(beta,lam_pows(m,c),c); t0=twists(p,m)
err=max(min(abs(a-b),1-abs(a-b)) for a,b in zip(tau,t0))
res=dict(rank=RK,conj=CONJ,p=p,c=c,s=s,e=list(e),Ne=e[0]**2-2*e[1]**2,q_over_c=q//c,z8=list(z8),twist_identity_err=err,vals={})
for P in [p]+P2:
    mm=3*P; h,nu=nu_rho(mm,1); tw=TW(mm,nu,L=8,K=16); Z0=Zbatch(tw,[[0.0]*mm])[0]
    T=twists(P,mm) if P!=p else tau
    r=Zbatch(tw,[T])[0]/Z0; res['vals'][P]=[r.real,r.imag]
print(json.dumps(res),flush=True)
open('/workspace/bgs-lineN/N8b/logs/d_puni.jsonl','a').write(json.dumps(res)+'\n')
