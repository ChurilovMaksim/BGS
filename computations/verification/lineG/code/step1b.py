import sys, math, json, numpy as np
from law import mdata, ratrec
from collections import defaultdict
def Z2all(T,m):
    d=mdata(m); h=d['h']; gp=2*h; yp=d['yp']
    S=np.fft.ifft(T)*h; res=[]
    for nu in range(1,gp,2):
        if math.gcd(nu,gp)!=1: continue
        v=(-pow(16,-1,h)*pow(nu,-1,h)*pow(yp,-1,h))%h
        res.append((nu,abs(S[v])**2/h**2))
    return res
def factor(n):
    f={};p=2
    while p*p<=n:
        while n%p==0: f[p]=f.get(p,0)+1; n//=p
        p+=1
    if n>1: f[n]=f.get(n,0)+1
    return f
def load(kick,m):
    import os
    p=f'../logs/Torb_{kick}_m{m}.bin'
    if os.path.exists(p) and m>=15: return np.fromfile(p,np.complex128)
    return np.load(f'computations/verification/lineE/referee/logs/T_{kick}_eta2.0_m{m}.npy')
if __name__=='__main__':
    kick=sys.argv[1]; ms=[int(x) for x in sys.argv[2].split(',')]
    allout={}
    for m in ms:
        T=load(kick,m); d=mdata(m); h=d['h']; R=Z2all(T,m); phi=len(R); F=sum(z for _,z in R)/phi
        fam=defaultdict(list); rows=[]
        for nu,z in R:
            (a,b),(a2,b2)=ratrec(nu,2*h)
            g=math.gcd(a,b); ap,bp=a//g,b//g
            L=math.hypot(a,b)
            rows.append(dict(nu=nu,z=z,a=a,b=b,g=g,ap=ap,bp=bp,len=L))
            fam[(ap,bp,g)].append(z)
        print(f'== {kick} m={m} h={h}={factor(h)} phi={phi} F/2m={F/(2*m):.4f}')
        famlist=sorted(fam.items(),key=lambda kv:-sum(kv[1]))
        for (ap,bp,g),zs in famlist[:30]:
            print(f'  nu≡{ap}/{bp} mod 2h/{g}: size={len(zs):5d} share F/2m={sum(zs)/phi/(2*m):9.4f} max|Z|^2={max(zs):11.4g} mean|Z|^2/4m={np.mean(zs)/(4*m):9.3f}')
        # rest after removing primitive classes with |ap|,bp<=B and g<=G
        for B in [8,16,32]:
            for G in [1,50,10**9]:
                sel=[r['z'] for r in rows if not (abs(r['ap'])<=B and r['bp']<=B and r['g']<=G)]
                print(f'  remove |a\'|,b\'<={B}, d<={G}: removed={phi-len(sel)} rest mean/(4m)={np.mean(sel)/(4*m):.4f}  rest F/2m={np.mean(sel)/(2*m):.4f}')
        # distribution of |Z|^2/(4m) for generic (len > sqrt(h)/2)
        gen=np.array([r['z'] for r in rows if r['len']>0.5*math.sqrt(2*h)])
        x=gen/np.mean(gen)
        print(f'  generic (len>0.5 sqrt(2h)): n={len(gen)} mean/(4m)={np.mean(gen)/(4*m):.4f}  E[x^2]={np.mean(x**2):.3f} (exp: COE-Gaussian complex 2, real 3)  max x={x.max():.2f}')
        allout[m]=dict(h=h,phi=phi,F=F,rows=sorted(rows,key=lambda r:-r['z'])[:300])
    json.dump(allout,open(f'../logs/step1b_{kick}_{ms[0]}_{ms[-1]}.json','w'))
