"""Referee's INDEPENDENT arb certificate for Line F's lifted operators (written from scratch from the referee's own derivation).
usage: own_cert.py V|E eta K0 rho K beta N Rmax tau p r1 r2 sectors out.json
L = A (core<-core, |n|<=N) + X (far(|c|<=Rmax)<-core, |n|<=N) + Delta (rest).  Comparison T0' = [[PAP (+)0,0],[X,0]].
Weights om_c = exp(-beta(|c|-R)_+), R = max core |c|. Galerkin basis ((s-c)/rho)^i (orthonormal in H^2(D(c,rho)))."""
import sys, json, time
import numpy as np
from flint import arb, acb, acb_mat, ctx
ctx.prec=128
typ=sys.argv[1]; eta=arb(sys.argv[2]); K0=int(sys.argv[3]); rho=arb(sys.argv[4]); K=int(sys.argv[5]); beta=arb(sys.argv[6])
N=int(sys.argv[7]); Rmax=int(sys.argv[8]); tau=arb(sys.argv[9]); p=int(sys.argv[10]); r1=arb(sys.argv[11]); r2=arb(sys.argv[12])
sectors=[int(s) for s in sys.argv[13].split(',')]; out=sys.argv[14]
T0=time.time()
lam=3+2*arb(2).sqrt(); C=1/(lam-1/lam); PI=arb.pi(); x=arb(9)/10*eta; one=arb(1); half=one/2
def ex(t): return acb(0,2*PI*t).exp() if isinstance(t,arb) else (acb(0,1)*2*PI*t).exp()
Jabs={}; Jval={}
for n in range(0,N+1):
    j=x.bessel_j(arb(n)); Jval[n]=j; Jval[-n]=j*(-1)**n; Jabs[n]=abs(j); Jabs[-n]=abs(j)
def w(a,n):  # i^n J_n(x) e(C n^2/2 + a n/8)
    return acb(0,1)**(n%4)*Jval[n]*ex(C*n*n/2+arb(a)*n/8)
def cround(t):  # certified round-to-nearest of arb t
    f=int(np.floor(float((t+half).mid())))
    assert (t+half-f)>0 and (t+half-f)<1, 'uncertified rounding'
    return f
# states as doubled integers s2 (centre = s2/2)
par=0 if typ=='V' else 1
R2=2*K0 if typ=='V' else 2*K0-1      # max core |2c|
def tgt(s2,n):
    c=arb(s2)/2
    if typ=='V':
        j=cround((c+n)/lam); return 2*j, (c+n)/lam-j
    e=(s2-1)//2; j=cround(arb(e+n)/lam)
    if cround(arb(e+1+n)/lam)!=j+1: return None
    return 2*j+1, (c+n)/lam-(arb(2*j+1)/2)
def om(s2):
    d=abs(s2)-R2
    return (-beta*arb(d)/2).exp() if d>0 else one
core=[s for s in range(-R2,R2+1) if s%2==par%2]
ix={s:i for i,s in enumerate(core)}; nc=len(core); D=nc*K
thmax=(half/rho if typ=='V' else half/lam/rho)+1/lam
assert thmax<1
mult=lambda n,r: (2*PI*C*abs(n)*r).exp()
def tail(alpha):   # sum_{|n|>N} |J_n(x)| e^{alpha|n|} <= 2 sum_{n>N} t^n/n!, t=x e^alpha/2
    t=x*alpha.exp()/2; term=t**(N+1)
    for i in range(1,N+2): term=term/i
    q=t/(N+2); assert q<1
    return 2*term/(1-q)
print('typ',typ,'core states',[s/2 for s in core],'dim',D,flush=True)
# exact Galerkin block (without weight): entry(i,l) = [sig^i] e^{z sig} (sig/lam + d)^l * e(C n c)
from math import comb
def gblock(n,s2,d):
    z=acb(0,2*PI*C*n*rho)
    Mm=acb_mat(K,K); Cm=acb_mat(K,K)
    zp=[acb(1)]; fac=[arb(1)]
    for i in range(1,K): zp.append(zp[-1]*z); fac.append(fac[-1]*i)
    for i in range(K):
        for j in range(i+1): Mm[i,j]=zp[i-j]/fac[i-j]
    dd=d/rho; dp=[arb(1)]
    for i in range(1,K): dp.append(dp[-1]*dd)
    li=[arb(1)]
    for i in range(1,K): li.append(li[-1]/lam)
    for l in range(K):
        for i in range(l+1): Cm[i,l]=comb(l,i)*li[i]*dp[l-i]
    return (Mm*Cm)*ex(C*n*arb(s2)/2)
blocks=[]   # (row s2, col s2', n, matrix)
colt={s:arb(0) for s in core}; hs2=arb(0); rows={}; Xrows={}; Tr=arb(0)
for s2 in core:
    rows[s2]=arb(0); pairacc={}
    for n in range(-N,N+1):
        tg=tgt(s2,n)
        if tg is None: continue
        t2,d=tg; th=abs(d)/rho+1/lam; assert th<1
        bnd=Jabs[n]*mult(n,rho)/(1-th*th).sqrt(); trn=Jabs[n]*mult(n,rho)/(1-th)
        rat=om(s2)/om(t2); Tr+=rat*trn
        if abs(t2)>R2: rows[s2]+=rat*bnd; continue
        blocks.append((s2,t2,n,gblock(n,s2,d)))
        colt[t2]+=bnd*th**K
        g=tau/lam+abs(d)/rho; sup=Jabs[n]*mult(n,tau*rho)
        acc=pairacc.setdefault(t2,[arb(0)]*K)
        for l in range(K): acc[l]+=sup*g**l
    for t2,acc in pairacc.items():
        for l in range(K): hs2+=acc[l]**2
    al=2*PI*C*rho+beta/lam; fac=(beta*(abs(arb(s2))/2/lam+half)).exp()
    rows[s2]+=fac*tail(al)/(1-thmax*thmax).sqrt(); Tr+=fac*tail(al)/(1-thmax)
delta1=sum((v**2 for v in colt.values()),arb(0)).sqrt()
delta2=(hs2*tau**(-2*K)/(1-tau**-2)).sqrt()
print('delta1',delta1,'delta2',delta2,round(time.time()-T0),'s',flush=True)
far=[s for s in range(-2*Rmax,2*Rmax+1) if s%2==par%2 and abs(s)>R2]
for s2 in far:
    rows[s2]=arb(0); Xrows[s2]=arb(0)
    for n in range(-N,N+1):
        tg=tgt(s2,n)
        if tg is None: continue
        t2,d=tg; th=abs(d)/rho+1/lam
        bnd=Jabs[n]*mult(n,rho)/(1-th*th).sqrt(); trn=Jabs[n]*mult(n,rho)/(1-th)
        rat=om(s2)/om(t2); Tr+=rat*trn
        if abs(t2)<=R2: Xrows[s2]+=rat*bnd
        else: rows[s2]+=rat*bnd
    al=2*PI*C*rho+beta/lam; fac=om(s2)*(beta*(abs(arb(s2))/2/lam+half)).exp()
    rows[s2]+=fac*tail(al)/(1-thmax*thmax).sqrt(); Tr+=fac*tail(al)/(1-thmax)
# analytic rows |c| > Rmax: ratio <= e^{-beta(|c|-R)} + e^{-beta(1-1/lam)|c|} e^{beta(|n|/lam+1/2)}
Rr=arb(R2)/2
B0=sum((Jabs[n]*mult(n,rho) for n in range(-N,N+1)),arb(0))+tail(2*PI*C*rho)
B1=sum((Jabs[n]*mult(n,rho)*(beta*abs(n)/lam).exp() for n in range(-N,N+1)),arb(0))+tail(2*PI*C*rho+beta/lam)
first=arb(Rmax+1) if typ=='V' else arb(Rmax)+half
def gs(g): return 2*(-g*first).exp()/(1-(-g).exp())   # sum over lattice |c|>=first, both signs
g1=beta; g2=beta*(1-1/lam)
far_op2=2*((2*beta*Rr).exp()*gs(2*g1)*B0**2+(beta).exp()*gs(2*g2)*B1**2)/(1-thmax*thmax)
far_tr=((beta*Rr).exp()*gs(g1)*B0+(beta/2).exp()*gs(g2)*B1)/(1-thmax)
Delta=(sum((v**2 for v in rows.values()),arb(0))+far_op2).sqrt(); Xn=sum((v**2 for v in Xrows.values()),arb(0)).sqrt()
Tr+=far_tr; delta=delta1+delta2; E0=delta+Delta
print('Delta',Delta,'Xnorm',Xn,'trace',Tr,round(time.time()-T0),'s',flush=True)
res=dict(args=sys.argv[1:],delta=float(delta.upper()),Delta=float(Delta.upper()),X=float(Xn.upper()),trace_norm=float(Tr.upper()),sectors={})
def frob(M):
    s=arb(0)
    for i in range(M.nrows()):
        for j in range(M.ncols()): s+=abs(M[i,j])**2
    return s.sqrt()
def neu(nr,r):
    if not nr[p]<r**p: return None
    return sum((nr[j]/r**(j+1) for j in range(p)),arb(0))/(1-nr[p]/r**p)
def RT(Rc,za):   # resolvent of T0' from resolvent of core part
    Rcc=Rc+1/za
    return Rcc*(1+Xn/za)+1/za
for a in sectors:
    A=acb_mat(D,D)
    acc={}
    for (s2,t2,n,M) in blocks:
        k=(s2,t2); term=M*w(a,n)
        acc[k]=term if k not in acc else acc[k]+term
    for (s2,t2),M in acc.items():
        i0=ix[s2]*K; j0=ix[t2]*K
        for i in range(K):
            for j in range(K): A[i0+i,j0+j]=M[i,j]
    d={}
    if typ=='V' and a==4:
        Am=np.array([[complex(A[i,j].mid()) for j in range(D)] for i in range(D)])
        ev,vec=np.linalg.eig(Am); k=int(np.argmax(abs(ev))); v=vec[:,k]/np.linalg.norm(vec[:,k])
        v=v*np.exp(-1j*np.angle(v[0]))   # v0 real >0
        u=v.copy(); u[0]-=-1.0           # Householder vector u = v + e1 (maps v -> -e1)
        ua=[acb(complex(t).real,complex(t).imag) for t in u]
        nn=sum((abs(t)**2 for t in ua),arb(0))
        H=acb_mat(D,D)
        for i in range(D):
            for j in range(D): H[i,j]=(1 if i==j else 0)-2*ua[i]*ua[j].conjugate()/nn
        B=H*A*H
        b11=B[0,0]; b12=sum((abs(B[0,j])**2 for j in range(1,D)),arb(0)).sqrt(); b21=sum((abs(B[i,0])**2 for i in range(1,D)),arb(0)).sqrt()
        Y=acb_mat(D-1,D-1)
        for i in range(1,D):
            for j in range(1,D): Y[i-1,j-1]=B[i,j]
        nr=[arb(1)]; P=Y
        for j in range(1,p+1):
            nr.append(frob(P))
            if j<p: P=P*Y
        rl=abs(b11)-r1
        RY1=neu(nr,rl); RY2=neu(nr,r2)
        d.update(b11=str(b11),b12=float(b12.upper()),b21=float(b21.upper()),Yroot=float((nr[p]**(one/p)).upper()))
        if RY1 is not None and RY2 is not None and rl>r2:
            R1=RT((1+b12*RY1)/r1+RY1, rl); R2=RT((1+b12*RY2)/(abs(b11)-r2)+RY2, r2)
            Fp=E0+b21
            d.update(lo=float(rl.lower()),hi=float((abs(b11)+r1).upper()),FR1=float((Fp*R1).upper()),FR2=float((Fp*R2).upper()),certified=bool(Fp*R1<1 and Fp*R2<1))
        else: d['certified']=False
    else:
        nr=[arb(1)]; P=A
        for j in range(1,p+1):
            nr.append(frob(P))
            if j<p: P=P*A
        RA=neu(nr,r2); d['Aroot']=float((nr[p]**(one/p)).upper())
        if RA is not None:
            R2=RT(RA,r2); d.update(FR2=float((E0*R2).upper()),certified=bool(E0*R2<1))
        else: d['certified']=False
    res['sectors'][a]=d; print('sector',a,d,round(time.time()-T0),'s',flush=True)
    json.dump(res,open(out,'w'),indent=1)
res['secs']=time.time()-T0; json.dump(res,open(out,'w'),indent=1); print('done',flush=True)
