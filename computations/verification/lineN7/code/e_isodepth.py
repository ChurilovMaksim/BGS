"""N7 gap (a) [N]: isotropic points at q = h_p (prime) parametrised as x = 1/4 + gamma*alpha/(4q) (mod O^vee), alpha in O with N(alpha) odd,
gamma = x_{k+1} + y_k sqrt2 (norm q).  For every ideal (alpha) of odd norm k <= K (balanced generator) compute Zhat/Z_rho for the points
alpha, eps*alpha, -alpha (exact integer twists mod 1), both rho = (+-2,8).  Purpose: p-independence (compare p) and decay in k.
usage: e_isodepth.py p K"""
import sys, json, math
from fractions import Fraction as Fr
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import *
p=int(sys.argv[1]); K=int(sys.argv[2]); m=3*p; k=(p-1)//2
def xy(n):
    x,y=1,0
    for _ in range(n): x,y=x+2*y,x+y
    return x,y
def mul(u,v): return (u[0]*v[0]+2*u[1]*v[1], u[0]*v[1]+u[1]*v[0])
q=xy(p)[0]; g=(xy(k+1)[0],xy(k)[1]); assert g[0]**2-2*g[1]**2==q
S2=math.sqrt(2)
# balanced generators of ideals of odd norm <= K: a+b sqrt2 with |N| odd <= K, reduce |emb1/emb2| into [1/eps, eps) via eps multiplication, dedupe
seen={}; B=int(3*math.sqrt(K))+3
for a in range(-B,B+1):
    for b in range(-B,B+1):
        n=a*a-2*b*b
        if n%2==0 or abs(n)>K: continue
        u=(a,b)
        for _ in range(60):
            e1=u[0]+u[1]*S2; e2=u[0]-u[1]*S2; r=abs(e1/e2)
            if r>=1+S2: u=mul(u,(-1,1))         # multiply by eps^{-1} = -1+sqrt2
            elif r<1/(1+S2): u=mul(u,(1,1))
            else: break
        if u[0]+u[1]*S2<0: u=(-u[0],-u[1])
        key=(abs(n),u); seen[u]=abs(n)
reps=sorted(seen.items(),key=lambda t:(t[1],t))
# dedupe associates (u and eps*u can both be 'balanced' at the boundary): canonical = lexicographically smallest over {+-eps^j u, |j|<=1}
canon={}
for u,n in reps:
    cands=[u,mul(u,(1,1)),mul(u,(-1,1))]; cands+= [(-c[0],-c[1]) for c in cands]
    cands=[c for c in cands if 1/(1+S2)-1e-12<=abs((c[0]+c[1]*S2)/(c[0]-c[1]*S2))<1+S2+1e-12]
    canon.setdefault(min(cands),n)
alist=sorted(canon.items(),key=lambda t:(t[1],t))
def twist(al):
    L=(1,0); w=mul(g,al); w=(q+w[0],w[1]); out=[]
    for i in range(m):
        v=mul(L,w); out.append(float(Fr(2*v[0],4*q)%1)); L=mul(L,(3,2))
    return out
pts=[]; lab=[]
for al,n in alist:
    for tag,a2 in (('a',al),('ea',mul(al,(1,1))),('-a',(-al[0],-al[1]))):
        pts.append(twist(a2)); lab.append((n,al,tag))
res=[]
for sg in (1,-1):
    h,nu=nu_rho(m,sg); tw=TW(m,nu,L=8,K=16); Z0=Zbatch(tw,[[0.0]*m])[0]; Z=[]
    for i in range(0,len(pts),32): Z+=list(Zbatch(tw,pts[i:i+32]))
    for (n,al,tag),z in zip(lab,Z): res.append(dict(sg=sg,N=n,alpha=list(al),tag=tag,r=[(z/Z0).real,(z/Z0).imag]))
json.dump(dict(p=p,K=K,q=str(q),res=res),open(f'/workspace/bgs-lineN/N7/logs/e_isodepth_p{p}_K{K}.json','w'),indent=1)
for r in res:
    if r['sg']==1: print(r['N'],r['alpha'],r['tag'],'%.4e %+.4e'%tuple(r['r']))
