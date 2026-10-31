"""N10b d_h13.py [N] — derived from N8b/code/b_cline.py (enumeration part, unchanged) + G* slow-time recomputation.
Original doc: N8b [N]: isotropic c-lines at conductors c | h_m (m=3p), Lin convention: points beta/c, tau_i = Tr(lam^i beta)/c (twlaw).
Line generator v: 'cons' = gamma_3 mod c (gamma_3 = x_{k3+1}+y_{k3} sqrt2, N = h_{3p}; consistent line, its conjugate gives equal Zhat);
'inc:c1' = CRT(gamma_3 mod c1, conj(gamma_3) mod c/c1)  (inconsistent line).
Classes = orbits of beta -> lam*beta, -beta on {s v : gcd(s,c)=1}.  depth(orbit) = min_j |N(Y_j)|/c, Y_j = centred residue of 8 lam^j beta mod c.
mode 'full' (all orbits) or 'shallow:D' (orbits containing an element Y of the line-ideal with |N(Y)| <= D c, via lattice enumeration).
Also checks the exact identity tau_i == sigma Tr(eps^{2i-M} beta)/c (mod 1) on every evaluated class (M = period of lam mod line).
usage: b_cline.py p c line mode"""
import sys, json, math, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import *
from sympy import factorint
p=int(sys.argv[1]); c=int(sys.argv[2]); line=sys.argv[3]; mode=sys.argv[4]; m=3*p
def xy(n):
    x,y=1,0
    for _ in range(n): x,y=x+2*y,x+y
    return x,y
def mul(u,v,M=None):
    r=(u[0]*v[0]+2*u[1]*v[1], u[0]*v[1]+u[1]*v[0]); return r if M is None else (r[0]%M,r[1]%M)
hp=xy(p)[0]; k3=(m-1)//2; g3=(xy(k3+1)[0],xy(k3)[1]); H=xy(m)[0]; assert abs(g3[0]**2-2*g3[1]**2)==H and H%c==0
fc=factorint(c)
if line=='cons': v=(g3[0]%c,g3[1]%c)
else:
    c1=int(line.split(':')[1]); c2=c//c1; assert c1*c2==c and math.gcd(c1,c2)==1
    a=(g3[0]%c1,g3[1]%c1); b=(g3[0]%c2,(-g3[1])%c2)
    e1=c2*pow(c2,-1,c1); e2=c1*pow(c1,-1,c2)
    v=((a[0]*e1+b[0]*e2)%c,(a[1]*e1+b[1]*e2)%c)
assert (v[0]**2-2*v[1]**2)%c==0
LAMv=mul((3,2),v,c); ell=(LAMv[1]*pow(v[1],-1,c))%c; assert (ell*v[0]-LAMv[0])%c==0
# period M of lam on the line and sign sigma with eps^M == sigma (mod line ideal):  test eps^M v == sigma v (mod c)
M=None
for MM in (p,3*p,2*p,6*p):
    em=(1,0)
    for _ in range(MM): em=mul(em,(1,1),c)
    w=mul(em,v,c)
    for sg in (1,-1):
        if ((w[0]-sg*v[0])%c==0) and ((w[1]-sg*v[1])%c==0): M,sigma=MM,sg; break
    if M: break
h,nu0=nu_rho(m,1); tw=TW(m,nu0,L=8,K=16); Z0=Zbatch(tw,[[0.0]*m])[0]; pw=lam_pows(m,c)
def cen(x): x%=c; return x-c if x>c//2 else x
def depth_orbit(s):
    beta=((s*v[0])%c,(s*v[1])%c); best=None; L=beta
    for j in range(M if M else m):
        Y=(cen(8*L[0]),cen(8*L[1])); n=abs(Y[0]**2-2*Y[1]**2)
        if best is None or n<best: best=n
        L=mul((3,2),L,c)
    return best//c if best%c==0 else best/c
def orbit(s):
    o=set(); t=s
    while t not in o: o.add(t); o.add((-t)%c); t=(t*ell)%c
    return o
reps=[];sizes=[]
if mode=='full':
    seen=np.zeros(c,bool)
    for s in range(1,c):
        if seen[s] or math.gcd(s,c)!=1: continue
        o=orbit(s)
        for t in o: seen[t]=True
        reps.append(s); sizes.append(len(o))
else:
    D=float(mode.split(':')[1])
    # lattice of Y=(a,b) in the line ideal: a*v1 - b*v0 == 0 mod c ; basis (c,0),(v0*inv(v1) ,1)
    r=(v[0]*pow(v[1],-1,c))%c; B=[np.array([c,0],dtype=object),np.array([r,1],dtype=object)]
    # Gauss reduce in the quadratic form a^2+2b^2
    def qf(u): return int(u[0])**2+2*int(u[1])**2
    def bil(u,w): return int(u[0])*int(w[0])+2*int(u[1])*int(w[1])
    while True:
        if qf(B[0])>qf(B[1]): B=[B[1],B[0]]
        mu=round(bil(B[0],B[1])/qf(B[0]))
        if mu==0: break
        B[1]=B[1]-mu*B[0]
    R=math.sqrt(2*D*c)*1.0+1  # balanced Y with |N|<=Dc has a^2+2b^2 = (Y1^2+Y2^2)/2 <= ~ lam*D*c ; enlarge
    Rq=6*D*c
    seenS=set(); found=[]
    n0=int(math.sqrt(Rq/qf(B[0])))+2; n1=int(math.sqrt(Rq/max(1,qf(B[1])-bil(B[0],B[1])**2/qf(B[0]))))+2
    inv8=pow(8,-1,c)
    for i1 in range(-n1,n1+1):
        for i0 in range(-n0,n0+1):
            Y=i0*B[0]+i1*B[1]; a,b=int(Y[0]),int(Y[1])
            if a==0 and b==0: continue
            if qf(Y)>Rq: continue
            n=abs(a*a-2*b*b)
            if n>D*c: continue
            s=(a*pow(v[0],-1,c))%c if v[0]%c else (b*pow(v[1],-1,c))%c
            s=(s*inv8)%c
            if math.gcd(s,c)!=1: continue
            if s in seenS: continue
            o=orbit(s); seenS|=o; reps.append(s); sizes.append(len(o))
T=[taus_of(((s*v[0])%c,(s*v[1])%c),pw,c) for s in reps]
# exact identity check: tau_i == sigma*Tr(eps^{2i-M} beta)/c mod 1  (integers mod c)
epsinv=(-1,1); bad=0
for s in reps[:50]:
    beta=((s*v[0])%c,(s*v[1])%c)
    for i in range(m):
        e=2*i-M; u=(1,0)
        for _ in range(abs(e)): u=mul(u,(1,1) if e>0 else epsinv,c)
        w=mul(u,beta,c); t1=taus_of(beta,[pw[i]],c)[0]; t2=((sigma*2*w[0])%c)/c
        if abs(t1-t2)>1e-12 and abs(abs(t1-t2)-1)>1e-12: bad+=1

MU=1.9154732
def tdist(x): x=x%1.0; return min(x,1-x)
FP=(0.0,0.25,0.5,0.75)
def slow_pairs(t,th,fps):
    return sum(1 for i in range(m) if any(max(tdist(t[i]-f),tdist(t[(i+1)%m]-f))<th for f in fps))
Z=[]
for i in range(0,len(T),64): Z+=list(Zbatch(tw,T[i:i+64]))
a=np.abs(np.array(Z))/abs(Z0)
res=dict(p=p,c=c,line=line,classes=len(reps),max_abs=float(a.max()),Gamma_raw=float(MU*a.max()**(1/m)))
for th in (1/16,1/8):
    for nm,fps in (('0,1/2',(0.0,0.5)),('all4',FP)):
        S=np.array([slow_pairs(t,th,fps) for t in T]); ge=MU*a**(1/np.maximum(1,m-S)); k=int(np.argmax(ge))
        res[f'th{th:.4f}_{nm}']=dict(Gamma_eff_max=float(ge.max()),s=int(S[k]),absr=float(a[k]),s_cls=int(reps[k]),
             top_abs_class=dict(s=int(reps[int(np.argmax(a))]),slow=int(S[int(np.argmax(a))]),Geff=float(ge[int(np.argmax(a))])))
import json; print(json.dumps(res),flush=True)
open('/workspace/bgs-lineN/N10b/logs/d_h13.jsonl','a').write(json.dumps(res)+'\n')
