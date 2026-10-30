"""Principled classification: primaries rho=(a,b) [b nu ≡ a mod 2h], b<=Bmax, |a|<=Amax; dilution level d | h, d<=D.
nu in F(d,rho) iff b nu ≡ a (mod 2h/d).  Level of nu = smallest such d (over all rho)."""
import sys, math, json, numpy as np
from law import mdata, ratrec
from step1b import Z2all, factor, load
from step1c import divisors
def primaries(Bmax,Amax):
    out=[]
    for b in range(1,Bmax+1):
        for a in range(-Amax,Amax+1):
            if math.gcd(a,b)==1 or (b%2==0 and a%2==0 and math.gcd(a//2,b//2)==1 and (b//2)%2==0):
                out.append((a,b))
    return out
def run(kick,m,Bmax=16,Amax=16,Dexp=0.5,verbose=True):
    T=load(kick,m); h=mdata(m)['h']; R=Z2all(T,m); phi=len(R)
    ds=[d for d in divisors(h) if d<=h**Dexp]
    P=primaries(Bmax,Amax)
    F=sum(z for _,z in R)/phi
    lab={}
    for nu,z in R:
        best=None
        for d in ds:
            M=2*h//d
            for a,b in P:
                if (b*nu-a)%M==0:
                    best=(d,a,b); break
            if best: break
        lab[nu]=best
    return h,R,phi,F,lab,ds
if __name__=='__main__':
    kick=sys.argv[1]; ms=[int(x) for x in sys.argv[2].split(',')]
    Bmax=int(sys.argv[3]); Amax=int(sys.argv[4]); Dexp=float(sys.argv[5])
    summary=[]
    for m in ms:
        h,R,phi,F,lab,ds=run(kick,m,Bmax,Amax,Dexp)
        Z=dict(R)
        res=[nu for nu in Z if lab[nu]]; non=[nu for nu in Z if not lab[nu]]
        zn=np.array([Z[n] for n in non]); x=zn/zn.mean()
        print(f'== {kick} m={m} h={h} {factor(h)} D-divisors={ds} phi={phi} F/2m={F/(2*m):.4f} (Bmax={Bmax},Amax={Amax})')
        print(f'  resonant: {len(res)} ({len(res)/phi:.3%}) share F/2m={sum(Z[n] for n in res)/phi/(2*m):.4f} | nonres F/2m={zn.mean()/(2*m):.4f}  -> W\'/m={2*(zn.mean()/(2*m)-2):+.3f}')
        print(f'  nonres moments: E[x^2]={np.mean(x**2):.3f} E[x^3]={np.mean(x**3):.2f} max x={x.max():.2f} #x>10={int(np.sum(x>10))}')
        by={}
        for n in res: by.setdefault(lab[n],[]).append(Z[n])
        for key,zl in sorted(by.items(),key=lambda kv:-sum(kv[1]))[:16]:
            d,a,b=key; print(f'   d={d:5d} rho=({a},{b}) [N≡{b}/{a} mod h/d]  n={len(zl):4d}  mean|Z|^2={np.mean(zl):11.4g}  share={sum(zl)/phi/(2*m):.4f}')
        top=sorted(non,key=lambda n:-Z[n])[:10]
        print('  top nonres (x, nu, shortest vec, N mod h):',[(round(Z[n]/zn.mean(),1),n,ratrec(n,2*h)[0]) for n in top])
        summary.append(dict(m=m,h=h,F2m=F/(2*m),nonres2m=zn.mean()/(2*m),nres=len(res),phi=phi,Ex2=float(np.mean(x**2)),maxx=float(x.max())))
    json.dump(summary,open(f'../logs/step1d_{kick}_B{Bmax}_A{Amax}_D{Dexp}.json','w'))
