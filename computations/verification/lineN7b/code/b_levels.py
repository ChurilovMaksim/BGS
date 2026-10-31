"""N7b (F) [N]: gap-(b) conductors at m = 3p.  For every conductor c | h_m with c not in {1,7,h_p,7h_p}, c <= sqrt(h_m) (frozen inclusion
range), c squarefree (7^2 at p=7 handled by brute force), compute per CRT 'pattern' (set g of primes where beta is isotropic):
  #points, mean/max |Zhat/Z_rho|, and the one-sided budget ratio
     rel = (h_p^2/c^2) * w_g * sum_{pattern}|Zhat/Z| / ReR_fam,   w_g = prod_{q in g}(q-1) * prod_{q notin g} 2   (|J3 weight| <= w_g/c^2),
     ReR_fam = (h_p-2)*Re X_{h_p} (family+near-0 iso sum at h_p, N6), so rel < 1 means the pattern is below the h_p family term.
Exact enumeration (orbit-reduced under lam, -1, conj; N6 t_sym) when the pattern has <= FULL points, else NS random samples (estimate).
Also signed Ramanujan sum R = sum c_c(N beta) Zhat/Z over exactly enumerated conductors.  usage: b_levels.py p [FULL] [NS]"""
import sys, json, math, random, numpy as np
from sympy import factorint, divisors, sqrt_mod, mobius
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import *
p=int(sys.argv[1]); FULL=int(sys.argv[2]) if len(sys.argv)>2 else 60000; NS=int(sys.argv[3]) if len(sys.argv)>3 else 200
random.seed(p); m=3*p
def hpf(p):
    x,y=1,1
    for _ in range(p-1): x,y=x+2*y,x+y
    return x
hp=hpf(p); h,nu0=nu_rho(m,1); assert h==hp*(4*hp*hp+3)
tw=TW(m,nu0,L=8,K=16); Z0=Zbatch(tw,[[0.0]*m])[0]
XH={5:0.003533,7:0.010724,11:0.016493,13:0.019429,19:0.028554}
ReX=XH.get(p,4*p*3.4358e-4*1.08); ReRfam=(hp-2)*ReX
fac=factorint(h)
def ram(n,u):
    g=math.gcd(n,u%n) if u%n else n
    return sum(int(mobius(n//d))*d for d in divisors(g))
def Zs(betas,c):
    pw=lam_pows(m,c); T=[taus_of(b,pw,c) for b in betas]; out=np.zeros(len(T),complex)
    for i in range(0,len(T),64): out[i:i+64]=Zbatch(tw,T[i:i+64])
    return out/Z0
def lam_mul(b,c): x,y=b; return ((3*x+4*y)%c,(2*x+3*y)%c)
def norm(b,c): x,y=b; return (x*x-2*y*y)%c
def is_exact(b,c):
    return all(not(b[0]%q==0 and b[1]%q==0) for q in factorint(c))
def crt(res,mods):
    M=1
    for q in mods: M*=q
    x=0
    for r,q in zip(res,mods): Mi=M//q; x+=r*Mi*pow(Mi,-1,q)
    return x%M
levels=[c for c in divisors(h) if c>1 and c not in (7,hp,7*hp) and c*c<=h]
print('p',p,'m',m,'h_p',hp,'fac h_m',fac,'|Z|',abs(Z0),'ReRfam',ReRfam,'conductors',levels,flush=True)
res=[]
for c in levels:
    fc=factorint(c); primes=sorted(fc)
    if any(e>1 for e in fc.values()) or c*c<=FULL:
        # brute force all exact-conductor beta, orbit reduce, Ramanujan weights
        seen=np.zeros(c*c,bool); reps=[];sizes=[];wts=[];pats=[]
        for x in range(c):
            for y in range(c):
                if seen[x*c+y] or not is_exact((x,y),c): continue
                orb=set(); b=(x,y)
                for _ in range(3*m+3):
                    for bb in (b,((-b[0])%c,(-b[1])%c),(b[0],(-b[1])%c),((-b[0])%c,b[1])): orb.add(bb)
                    b=lam_mul(b,c)
                for bb in orb: seen[bb[0]*c+bb[1]]=True
                reps.append((x,y)); sizes.append(len(orb)); u=norm((x,y),c); wts.append(ram(c,u))
                pats.append(tuple(q for q in primes if u%q==0))
        z=Zs(reps,c); sizes=np.array(sizes); wts=np.array(wts)
        Rsigned=complex(np.sum(sizes*wts*z))
        bypat={}
        for zz,s,w,pt in zip(z,sizes,wts,pats):
            d=bypat.setdefault(pt,dict(n=0,sabs=0.0,mx=0.0,wabs=0.0)); d['n']+=int(s); d['sabs']+=float(s*abs(zz)); d['mx']=max(d['mx'],abs(zz)); d['wabs']+=float(s*abs(w)*abs(zz))
        for pt,d in bypat.items():
            rel=(hp**2/c**2)*d['wabs']/ReRfam
            res.append(dict(c=c,fac=str(fc),pattern=list(pt),exact=True,npts=d['n'],nev=None,mean=d['sabs']/d['n'],max=d['mx'],
                 rate_max=(d['mx']*abs(Z0))**(1/m),rel=rel))
            print(json.dumps(res[-1]),flush=True)
        res.append(dict(c=c,signed_Ramanujan_R=[Rsigned.real,Rsigned.imag],Lin_over_famLin=(hp**2/c**2)*Rsigned.real/ReRfam)); print(json.dumps(res[-1]),flush=True)
        continue
    # squarefree, sampled per pattern
    w2={q:int(sqrt_mod(2,q)) for q in primes}
    for k in range(len(primes)+1):
      import itertools
      for g in itertools.combinations(primes,k):
        npts=1; wg=1
        for q in primes:
            if q in g: npts*=2*(q-1); wg*=(q-1)
            else: npts*=(q-1)**2; wg*=2   # unit residues mod q: q^2-1-2(q-1) = (q-1)^2
        sample=[]
        nsamp=min(NS,npts)
        for _ in range(nsamp):
            rx=[];ry=[]
            for q in primes:
                if q in g:
                    yv=random.randrange(1,q); xv=(random.choice((1,-1))*w2[q]*yv)%q
                else:
                    while True:
                        xv=random.randrange(q); yv=random.randrange(q)
                        if (xv*xv-2*yv*yv)%q: break
                rx.append(xv); ry.append(yv)
            sample.append((crt(rx,primes),crt(ry,primes)))
        z=np.abs(Zs(sample,c)); mean=float(z.mean())
        rel=(hp**2/c**2)*wg*npts*mean/ReRfam
        res.append(dict(c=c,fac=str(fc),pattern=list(g),exact=False,npts=npts,nev=nsamp,mean=mean,max=float(z.max()),
                        rate_max=(float(z.max())*abs(Z0))**(1/m),rel=rel))
        print(json.dumps(res[-1]),flush=True)
json.dump(dict(p=p,m=m,hp=hp,ReRfam=ReRfam,absZ=abs(Z0),res=res),open(f'/workspace/bgs-lineN/N7b/logs/b_levels_p{p}.json','w'),indent=1)
