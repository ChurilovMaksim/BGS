"""Classification with a FIXED primary list Pr (strong primaries) for dilution d|h (1<d<=h^Dexp),
plus all d=1 primaries of height<=H1 (single residues). Then inspect leftover outliers."""
import sys, math, json, numpy as np
from law import mdata, ratrec
from step1b import Z2all, factor, load
from step1c import divisors
PR=[(-2,8),(2,8),(-2,16),(2,16),(-2,4),(2,4),(-6,16),(6,16)]
def label(nu,h,ds,H1):
    for d in ds:
        M=2*h//d
        for a,b in PR:
            if (b*nu-a)%M==0: return (d,a,b)
    (a,b),_=ratrec(nu,2*h)
    if max(abs(a),b)<=H1: return (1,a,b)
    return None
def explain(nu,h,ds_all,Hx=40):
    best=None
    for d in ds_all:
        M=2*h//d
        if M<=8*Hx*Hx: continue
        (a,b),_=ratrec(nu%M,M)
        hh=max(abs(a),b)
        if hh<=Hx and (best is None or hh*d<best[0]): best=(hh*d,d,a,b)
    return best
if __name__=='__main__':
    kick=sys.argv[1]; ms=[int(x) for x in sys.argv[2].split(',')]; Dexp=float(sys.argv[3]); H1=int(sys.argv[4])
    summ=[]
    for m in ms:
        T=load(kick,m); h=mdata(m)['h']; R=Z2all(T,m); phi=len(R); Z=dict(R)
        dall=divisors(h); ds=[d for d in dall if d<=h**Dexp]
        F=sum(Z.values())/phi
        lab={nu:label(nu,h,ds,H1) for nu in Z}
        res=[n for n in Z if lab[n]]; non=[n for n in Z if not lab[n]]
        zn=np.array([Z[n] for n in non]); base=zn.mean(); x=zn/base
        print(f'== {kick} m={m} h={h} {factor(h)} ds={ds} phi={phi} F/2m={F/(2*m):.4f}')
        print(f'  resonant {len(res)} ({len(res)/phi:.3%}) share={sum(Z[n] for n in res)/phi/(2*m):.4f} | nonres F/2m={base/(2*m):.4f} W\'/m={2*(base/(2*m)-2):+.3f} | E[x^2]={np.mean(x**2):.3f} max x={x.max():.1f} #x>20={int((x>20).sum())}')
        by={}
        for n in res: by.setdefault(lab[n],[]).append(Z[n])
        for key,zl in sorted(by.items(),key=lambda kv:-sum(kv[1]))[:12]:
            print(f'   {key} n={len(zl)} mean|Z|^2={np.mean(zl):.4g} share={sum(zl)/phi/(2*m):.4f}')
        top=sorted(non,key=lambda n:-Z[n])[:12]
        print('  leftover outliers:')
        for n in top: print(f'    x={Z[n]/base:7.1f} nu={n} shortest={ratrec(n,2*h)[0]} explain(d,a,b)={explain(n,h,dall)}')
        summ.append(dict(m=m,F2m=F/(2*m),non2m=base/(2*m),nres=len(res),phi=phi,Ex2=float(np.mean(x**2)),maxx=float(x.max())))
    json.dump(summ,open(f'../logs/step1e_{kick}.json','w'))
