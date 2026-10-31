"""Referee (Grok Bot) [N]: signed isotropic line sums at q = h_p (prime), m = 3p, by sector-4 depth class.
Every point of the two isotropic lines is y = (q + gamma)/(4q) mod O^dual with gamma in qbar-or-q ideal (gamma in 4qy + sqrt2 q O),
16D = min |N(gamma)|/q.  We enumerate gamma = +-eps^j * g_q * alpha, N(alpha) = +-k, k <= K, both primes above q, keep
q + gamma in sqrt2 O (i.e. the point exists), key = exact twist pair (4q tau_0, 4q tau_1) mod 4q, keep min k per key.
Twists tau_i = Tr(lam^i (q+gamma))/(4q) mod 1, exact integers.  Zhat via the twlaw transfer law (L, K below), relative to Z0 = Zhat(0).
X = sum over all enumerated points of Zhat/Z0; the level-q deviation is ~ (|Z0|^2/q)(2 Re X + |X|^2) (TRACE-212 I2(d), K1).
usage: p K [sign] [L Kgal]"""
import sys, json, math, time, numpy as np
from collections import defaultdict
sys.path.insert(0,'/workspace/bgs-lineL/L2/code'); sys.path.insert(0,'/workspace/bgs-lineI/code')
from law import mdata
from twlaw import TW
p=int(sys.argv[1]); KMAX=int(sys.argv[2]); sg=int(sys.argv[3]) if len(sys.argv)>3 else 1
L=int(sys.argv[4]) if len(sys.argv)>4 else 8; KG=int(sys.argv[5]) if len(sys.argv)>5 else 32
def hp(p):
    x,y=1,1
    for _ in range(p-1): x,y=x+2*y,x+y
    return x
def mul(u,v): return (u[0]*v[0]+2*u[1]*v[1], u[0]*v[1]+u[1]*v[0])
N=lambda u: u[0]*u[0]-2*u[1]*u[1]
q=hp(p); m=3*p
from sympy import isprime, sqrt_mod
assert isprime(q)
def short(r,mod):  # shortest vector of {(a,b): a == r b mod mod} for a^2+2b^2, then generator of norm +-mod
    u=(mod,0); v=(r,1); f=lambda w:w[0]**2+2*w[1]**2; dot=lambda w,z:w[0]*z[0]+2*w[1]*z[1]
    if f(u)<f(v): u,v=v,u
    while True:
        k=(2*dot(u,v)+f(v))//(2*f(v)); u=(u[0]-k*v[0],u[1]-k*v[1])
        if f(u)>=f(v): break
        u,v=v,u
    for w in (v,u):
        if abs(N(w))==mod: return w
    raise RuntimeError
r=int(sqrt_mod(2,q)); gq=[short(r,q),short(q-r,q)]          # generators of the two primes above q
# elements of small norm up to units: alpha = a + b sqrt2 with |N| = k, reduced so that 1 <= alpha/|alpha'| < lam (one per ideal)
alphas=defaultdict(list); B=int(2*math.sqrt(KMAX))+3
lam=3+2*math.sqrt(2)
for a in range(0,4*B):
    for b in range(-2*B,2*B):
        k=abs(N((a,b)))
        if k==0 or k>KMAX: continue
        v=a+b*math.sqrt(2); vc=a-b*math.sqrt(2)
        if v<=0: continue
        rat=v/abs(vc)
        if 1<=rat<lam-1e-12: alphas[k].append((a,b))
pts={}; E=(1,1); per=8*p
for k in sorted(alphas):
    for al in alphas[k]:
        for li,g in enumerate(gq):
            base=mul(g,al)
            u=base
            for j in range(per):
                for s in (1,-1):
                    gam=(s*u[0],s*u[1])
                    if (q+gam[0])%2: continue
                    A,Bc=q+gam[0],gam[1]; M4=4*q
                    t0=(2*A)%M4; A1,B1=(3*A+4*Bc)%M4,(2*A+3*Bc)%M4; t1=(2*A1)%M4
                    key=(t0,t1)
                    if key not in pts or pts[key][0]>k: pts[key]=(k,li,(A%M4,Bc%M4))
                u=mul(u,E)
d=mdata(m); h=d['h']; M=2*h; assert h%q==0
x0=(sg*pow(4,-1,M//2))%(M//2); nu0=min(x for x in (x0,x0+M//2) if x%2==1); assert (8*nu0-2*sg)%M==0
tw=TW(m,nu0,L=L,K=KG); Z0=tw.Z([0.0]*m); Zhalf=tw.Z([0.5]*m)
def taus(A,Bc):
    out=[]; M4=4*q
    for i in range(m):
        out.append(((2*A)%M4)/M4); A,Bc=(3*A+4*Bc)%M4,(2*A+3*Bc)%M4
    return out
# group points into lambda-orbits (orbit = cyclic shifts of the twist sequence); evaluate one per orbit
seen={}; classes=defaultdict(lambda:[0,0j]); t0=time.time(); evals=0; per_line=defaultdict(complex)
for key,(k,li,(A,Bc)) in sorted(pts.items(),key=lambda kv:kv[1][0]):
    if key in seen: continue
    tw_=taus(A,Bc); orb=[]
    AA,BB=A,Bc
    for i in range(p):
        M4=4*q; t0_=(2*AA)%M4; A1,B1=(3*AA+4*BB)%M4,(2*AA+3*BB)%M4; orb.append((t0_,(2*A1)%M4)); AA,BB=A1,B1
    z=tw.Z(tw_)/Z0; evals+=1
    n=0
    for kk in orb:
        if kk in pts and kk not in seen: seen[kk]=1; n+=1
    classes[k][0]+=n; classes[k][1]+=n*z; per_line[li]+=n*z
rows=[]; cum=0j
for k in sorted(classes):
    cum+=classes[k][1]; rows.append(dict(k16D=k,points=classes[k][0],sum=[classes[k][1].real,classes[k][1].imag],cum=[cum.real,cum.imag],cum_abs_arg=[abs(cum),math.atan2(cum.imag,cum.real)]))
X=cum
res=dict(p=p,m=m,q=str(q),sign=sg,L=L,Kgal=KG,KMAX=KMAX,Z0=[Z0.real,Z0.imag],Zhalf_over_Z0=[(Zhalf/Z0).real,(Zhalf/Z0).imag],
  n_points=len(seen),evals=evals,X=[X.real,X.imag],per_line=[[v.real,v.imag] for _,v in sorted(per_line.items())],
  dev_factor_2ReX_plus_X2=2*X.real+abs(X)**2,rows=rows,sec=round(time.time()-t0,1))
print(json.dumps(res,indent=1)); json.dump(res,open(f'logs/ref_depth_sum_p{p}_K{KMAX}_s{sg}.json','w'),indent=1)
