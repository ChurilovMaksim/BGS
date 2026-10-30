import sys, math, json, numpy as np
from law import mdata, ratrec
from step1b import Z2all, factor, load
def divisors(n):
    f=factor(n); ds=[1]
    for p,e in f.items(): ds=[d*p**k for d in ds for k in range(e+1)]
    return sorted(ds)
def classify(nu,h,ds,B):
    """smallest d|h (d<h) such that nu mod 2h/d has a primitive reconstruction a'/b' with |a'|,b'<=B; returns (d,a',b')"""
    for d in ds:
        M=2*h//d
        if M<=2*B*B: break
        for (a,b) in ratrec(nu%M,M):
            g=math.gcd(a,b)
            if b>0 and abs(a)//g<=B and b//g<=B and (b//g*nu-a//g)%(M)==0 if False else (b>0 and abs(a)<=2*B and b<=2*B):
                return d,a,b
    return None
if __name__=='__main__':
    kick=sys.argv[1]; ms=[int(x) for x in sys.argv[2].split(',')]; B=int(sys.argv[3]) if len(sys.argv)>3 else 8
    for m in ms:
        T=load(kick,m); h=mdata(m)['h']; R=Z2all(T,m); phi=len(R); ds=divisors(h)
        F=sum(z for _,z in R)/phi
        rows=[]
        for nu,z in R:
            c=classify(nu,h,ds,B); rows.append((z,nu,c))
        res=[r for r in rows if r[2] is not None]; non=[r for r in rows if r[2] is None]
        zs=np.array([r[0] for r in non])
        print(f'== {kick} m={m} h={h} {factor(h)} divisors={ds[:8]} phi={phi} F/2m={F/(2*m):.4f}  B={B}')
        print(f'  resonant count={len(res)} ({len(res)/phi:.4%}), share F/2m={sum(r[0] for r in res)/phi/(2*m):.4f}; nonres mean/(4m)={zs.mean()/(4*m):.4f}  (rest F/2m={zs.mean()/(2*m):.4f})')
        x=zs/zs.mean(); print(f'  nonres E[x^2]={np.mean(x**2):.3f} E[x^3]={np.mean(x**3):.2f} max x={x.max():.2f}  P(x>5)={np.mean(x>5):.2e} (Exp law: {math.exp(-5):.2e})')
        by={}
        for z,nu,c in res: by.setdefault((c[0],c[1],c[2]),[]).append(z)
        top=sorted(by.items(),key=lambda kv:-sum(kv[1]))[:14]
        for (d,a,b),zl in top: print(f'   d={d:6d} nu≡{a}/{b} mod 2h/d  n={len(zl):4d} mean|Z|^2={np.mean(zl):11.4g} share={sum(zl)/phi/(2*m):.4f}')
        non.sort(key=lambda r:-r[0])
        print('  top nonresonant:',[(round(z/(4*m),1),nu,ratrec(nu,2*h)[0]) for z,nu,c in non[:8]])
