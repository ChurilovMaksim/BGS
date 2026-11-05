"""research1105b [N]: exact level-D decomposition of the frozen TRACE-206 member sum via the proved member formula
(TRACE-212 / I2'):  |Z_m(nu_rho + 2hj/D)|^2 = |sum_{beta mod D} e(tbar*Nm(beta)/D) Zhat(beta)|^2 / D^2,  t = j*y' mod D.
Zhat(beta) = twisted sum with tau_i = Tr(beta lam^i)/D (L2/N6 transfer law, L=8, K=16).
Betas are generated class by class via CRT and reduced modulo the group <lam, -1, Galois conj> (Zhat invariant).
usage: level.py m sg D CLASSSPEC OUT [nsample]
  CLASSSPEC: comma list of 'type' strings, one char per prime factor q of D (D squarefree):  i = iso mod q (Nm==0, incl 0), u = unit mod q (Nm!=0),
             z = beta==0 mod q, n = iso nonzero mod q.  e.g. D=23*353: 'ii' = full iso, 'ui' = unit mod 23 & iso mod 353.
  if nsample>0 the class is sampled uniformly (nsample betas, no orbit reduction) instead of enumerated."""
import sys, os, math, time, json, numpy as np
from multiprocessing import Pool
sys.path.insert(0,'/workspace/bgs-lineN/N6/code')
from twb import TW, Zbatch, nu_rho, mdata, LAM
from sympy import factorint
def lam_xy(i):
    x,y=1,0
    for _ in range(i): x,y=3*x+4*y,2*x+3*y
    return x,y
def local_set(q,typ):
    a=np.arange(q,dtype=np.int64); X,Y=np.meshgrid(a,a,indexing='ij'); X=X.ravel(); Y=Y.ravel()
    N=(X*X-2*Y*Y)%q
    if typ=='i': s=(N==0)
    elif typ=='u': s=(N!=0)
    elif typ=='z': s=(X==0)&(Y==0)
    elif typ=='n': s=(N==0)&~((X==0)&(Y==0))
    elif typ=='a': s=np.ones_like(N,bool)
    return X[s],Y[s]
def crt_class(D,primes,spec):
    X=np.zeros(1,np.int64); Y=np.zeros(1,np.int64); Mod=1
    for q,typ in zip(primes,spec):
        x,y=local_set(q,typ)
        # combine: beta == X mod Mod, == x mod q
        inv=pow(Mod,-1,q)
        X2=(X[:,None]+Mod*(((x[None,:]-X[:,None])*inv)%q)); Y2=(Y[:,None]+Mod*(((y[None,:]-Y[:,None])*inv)%q))
        X=X2.ravel(); Y=Y2.ravel(); Mod*=q
    return X%D,Y%D
def canon(X,Y,D,per):
    """canonical rep (min code) under lam^k (k<per), +-1, conj (x,y)->(x,-y)"""
    best=X*D+Y; cx,cy=X.copy(),Y.copy()
    for k in range(per):
        for sx,sy in ((1,1),(-1,-1),(1,-1),(-1,1)):
            best=np.minimum(best,((sx*cx)%D)*D+((sy*cy)%D))
        cx,cy=(3*cx+4*cy)%D,(2*cx+3*cy)%D
    return best
G={}
def winit(m,nu0,D):
    G['tw']=TW(m,nu0,L=8,K=16); G['m']=m; G['D']=D
    pw=[lam_xy(i) for i in range(m)]; G['px']=np.array([x%D for x,y in pw],np.int64); G['py']=np.array([y%D for x,y in pw],np.int64)
def wrun(chunk):
    bx,by=chunk; D=G['D']
    T=((2*((bx[:,None]*G['px'][None,:]+2*by[:,None]*G['py'][None,:])%D))%D)/D
    return Zbatch(G['tw'],T)
def evaluate(m,nu0,D,bx,by,nproc=7,ch=32):
    chunks=[(bx[i:i+ch],by[i:i+ch]) for i in range(0,len(bx),ch)]
    with Pool(nproc,initializer=winit,initargs=(m,nu0,D)) as P:
        res=P.map(wrun,chunks,chunksize=1)
    return np.concatenate(res) if res else np.zeros(0,complex)
def order_lam(D):
    x,y=3%D,2%D; k=1
    while not (x%D==1 and y%D==0): x,y=(3*x+4*y)%D,(2*x+3*y)%D; k+=1
    return k
if __name__=='__main__':
    m=int(sys.argv[1]); sg=int(sys.argv[2]); D=int(sys.argv[3]); specs=sys.argv[4].split(','); out=sys.argv[5]
    nsamp=int(sys.argv[6]) if len(sys.argv)>6 else 0
    h,nu0=nu_rho(m,sg); assert h%D==0
    fac=factorint(D); assert all(v==1 for v in fac.values()), 'squarefree D only'
    primes=sorted(fac); per=order_lam(D)
    tw=TW(m,nu0,L=8,K=16); Z0=Zbatch(tw,np.zeros((1,m)))[0]
    res=dict(m=m,sg=sg,D=D,primes=primes,per=per,Z0=[Z0.real,Z0.imag],classes={})
    for spec in specs:
        t0=time.time()
        if nsamp>0:
            rng=np.random.default_rng(1000003*m+7*D+sum(map(ord,spec))+(sg>0))
            loc=[local_set(q,t) for q,t in zip(primes,spec)]; tot=int(np.prod([len(l[0]) for l in loc]))
            X=np.zeros(nsamp,np.int64); Y=np.zeros(nsamp,np.int64); Mod=1
            for q,(lx,ly) in zip(primes,loc):
                k=rng.integers(0,len(lx),nsamp); inv=pow(Mod,-1,q)
                X=X+Mod*(((lx[k]-X)*inv)%q); Y=Y+Mod*(((ly[k]-Y)*inv)%q); Mod*=q
            bx,by=X%D,Y%D; w=np.full(nsamp,tot/nsamp); X=np.zeros(tot) if tot<10**7 else range(tot)
        else:
            X,Y=crt_class(D,primes,spec)
            c=canon(X,Y,D,per); reps,cnt=np.unique(c,return_counts=True); bx,by=reps//D,reps%D; w=cnt.astype(float)
        Zh=evaluate(m,nu0,D,bx,by)
        Nm=(bx*bx-2*by*by)%D
        np.savez(f'{out}_{spec}.npz',bx=bx,by=by,w=w,Zh=Zh,Nm=Nm,Z0=Z0,total=len(X),sampled=nsamp>0)
        res['classes'][spec]=dict(total=int(len(X)),nrep=int(len(bx)),sampled=nsamp>0,sec=round(time.time()-t0,1))
        print(spec,res['classes'][spec],flush=True)
    json.dump(res,open(f'{out}_meta.json','w'),indent=1)
