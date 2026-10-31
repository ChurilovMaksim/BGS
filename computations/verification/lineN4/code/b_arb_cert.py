"""N4 (B) [CA]: full interval-arithmetic (arb, python-flint) certificate for the free twisted family in the Line F space,
upgrading N3 i_verify.py ([CA*], verified floating point).  Proves  sup_{tau in [lo,hi]} ||R A_tau R^{-1}||_2 <= ftarget  on this
worker's share of cells, where A_tau = sum_{|n|<=Nmax} w0(n) e(n tau) B_n (core<-core Galerkin section, exact blocks as N3 i_verify /
Line F cert_lift).  Everything below is ball arithmetic except the choice of S ~ R^{-1} and of the SVD frames U,V (any matrices work;
their effect is bounded rigorously).
  C_n = R (w0(n) B_n) S  (|n|<=N1, arb),  F = RS - I,  R A_tau R^{-1} = (R A_tau S)(I+F)^{-1}.
  R A_tau S = sum_{|n|<=N1} e(n tau) C_n + T,  ||T|| <= T0 = ||R||_F ||S||_F sum_{N1<|n|<=Nmax} ||w0(n) B_n||_F.
  Cell [t0-h, t0+h]:  ||X(t0+s)|| <= ||X(t0)|| + h ||X'(t0)|| + h^2/2 L2,  L2 = sum (2 pi n)^2 ||C_n||_F.
  ||X||_2 for an acb matrix: float SVD frames U,V; M = U^* X V (arb);  ||M|| <= max|M_ii| + ||M - diag M||_F;
  ||X|| <= ||M|| / (s_min(U) s_min(V)),  s_min(U)^2 >= 1 - ||U^*U - I||_F.
  Bound for the cell: (||X0|| + h n1 + h^2 L2/2 + T0) / (1 - ||F||_F); n1 = ||X'(t0)||_F first, spectral if needed; else bisect.
usage: b_arb_cert.py typ K0 rho K Rfile|I Nmax N1 NC0 ftarget worker nworkers prec out.jsonl"""
import sys, json, time, math, numpy as np
from flint import arb, acb, acb_mat, ctx
typ=sys.argv[1]; K0=int(sys.argv[2]); rho_s=sys.argv[3]; K=int(sys.argv[4]); Rfile=sys.argv[5]; Nmax=int(sys.argv[6]); N1=int(sys.argv[7])
NC0=int(sys.argv[8]); ftarget=float(sys.argv[9]); wk=int(sys.argv[10]); nw=int(sys.argv[11]); ctx.prec=int(sys.argv[12]); outf=sys.argv[13]
t0=time.time(); log=open(outf,'a')
def emit(**d): d['t']=round(time.time()-t0,1); log.write(json.dumps(d)+'\n'); log.flush()
two=arb(2); lam=3+2*two.sqrt(); cc=1/(lam-1/lam); pi=arb.pi(); I=acb(0,1); rho=arb(rho_s); half=arb(1)/2; x18=arb('1.8')
def e(t): return (2*pi*I*t).exp()
def certfloor(y):
    f=int(math.floor(float(y.mid())))
    if not ((y-f)>=0): raise ValueError('floor')
    if not (y-f-1<0): raise ValueError('floor')
    return f
Rc = arb(K0) if typ=='V' else arb(K0)-half
def rnd(t): return certfloor(t+half)
def target(c2,n):
    c=arb(c2)/2
    if typ=='V':
        j=rnd((c+n)/lam); return (2*j,(c+n)/lam-j)
    a=rnd((c-half+n)/lam); b=rnd((c+half+n)/lam)
    if b!=a+1: return None
    return (2*a+1,(c+n)/lam-(arb(a)+half))
iscore=lambda c2: abs(arb(c2)/2)<=Rc
cores=[c2 for c2 in range(-2*K0-2,2*K0+3) if (c2%2==(0 if typ=='V' else 1)) and iscore(c2)]
idx={c2:i for i,c2 in enumerate(cores)}; nc=len(cores); D=nc*K
fact=[arb(1)]
for i in range(1,K+1): fact.append(fact[-1]*i)
lamp=[arb(1)]
for i in range(1,K+1): lamp.append(lamp[-1]/lam)
J={n: x18.bessel_j(arb(abs(n)))*(1 if (n>=0 or n%2==0) else -1) for n in range(-Nmax,Nmax+1)}
def w0(n): return (I**(n%4))*J[n]*e(cc*n*n/2)
def blocks(n):
    out=[]; wn=w0(n)
    for c2 in cores:
        tg=target(c2,n)
        if tg is None: continue
        j2,dl=tg
        if not iscore(j2): continue
        z=2*pi*I*cc*n*rho; zp=[acb(1)]
        for i in range(1,K): zp.append(zp[-1]*z)
        Mm=acb_mat(K,K)
        for l in range(K):
            for jj in range(l+1): Mm[l,jj]=zp[l-jj]/fact[l-jj]
        Cm=acb_mat(K,K); Bq=dl/rho; bp=[arb(1)]
        for i in range(1,K): bp.append(bp[-1]*Bq)
        for k in range(K):
            for jj in range(k+1): Cm[jj,k]=fact[k]/(fact[jj]*fact[k-jj])*lamp[jj]*bp[k-jj]
        out.append((idx[c2]*K, idx[j2]*K, (Mm*Cm)*(e(cc*n*arb(c2)/2)*wn)))
    return out
def frob(Xa):
    return sum((abs(x)**2 for x in Xa.entries()),arb(0)).sqrt()
def tomat(np_arr): return acb_mat(np_arr.tolist())
def rignorm(Xa):
    Xm=np.array([complex(x.mid()) for x in Xa.entries()]).reshape(D,D)
    U,s,Vh=np.linalg.svd(Xm); Ua=tomat(U); Va=tomat(Vh.conj().T)
    UaH=Ua.conjugate().transpose()
    Mx=UaH*(Xa*Va)
    ent=Mx.entries(); dmax=arb(0); off=arb(0)
    for k,x in enumerate(ent):
        i,j=divmod(k,D)
        if i==j: dmax=max(dmax,abs(x).upper()) if True else None
        else: off+=abs(x)**2
    nM=dmax+off.sqrt()
    eU=frob(UaH*Ua-acb_mat(D,D,[acb(1) if i==j else acb(0) for i in range(D) for j in range(D)]))
    eV=frob(Va.conjugate().transpose()*Va-acb_mat(D,D,[acb(1) if i==j else acb(0) for i in range(D) for j in range(D)]))
    assert eU<0.5 and eV<0.5
    return (nM/((1-eU)*(1-eV)).sqrt()).upper()
# ---- precompute ----
if Rfile=='I':
    Ra=None
else:
    R=np.load(Rfile); assert R.shape==(D,D); S=np.linalg.inv(R); Ra=tomat(R.astype(complex)); Sa=tomat(S.astype(complex))
Iden=acb_mat(D,D,[acb(1) if i==j else acb(0) for i in range(D) for j in range(D)])
if Ra is None: Fb=arb(0); nRF=arb(D).sqrt(); nSF=nRF   # R=S=I exactly (Frobenius of I used only in the tail; spectral norm 1 used below)
else:
    Fb=frob(Ra*Sa-Iden); nRF=frob(Ra); nSF=frob(Sa)
assert Fb<0.5
C={}; T0=arb(0); L2=arb(0)
for n in range(-Nmax,Nmax+1):
    bl=blocks(n)
    if not bl: continue
    if abs(n)>N1:
        fn=sum((abs(x)**2 for (_,_,b) in bl for x in b.entries()),arb(0)).sqrt()
        T0+= (fn if Ra is None else nRF*fn*nSF); continue
    An=acb_mat(D,D)
    for (r0,c0,b) in bl:
        for a in range(K):
            for bb in range(K): An[r0+a,c0+bb]=b[a,bb]
    Cn=An if Ra is None else Ra*(An*Sa)
    C[n]=Cn; L2+=(2*pi*n)**2*frob(Cn)
emit(kind='pre',typ=typ,D=D,letters=len(C),Fb=float(Fb.upper()),T0=float(T0.upper()),L2=float(L2.upper()),nRF=float(nRF.upper()),nSF=float(nSF.upper()))
print('precompute done',round(time.time()-t0,1),'s  Fb',float(Fb.upper()),'T0',float(T0.upper()),'L2',float(L2.upper()),flush=True)
ns=sorted(C)
def X_at(t0r):
    X0=acb_mat(D,D); X1=acb_mat(D,D)
    for n in ns:
        ph=e(arb(n)*t0r); X0+=C[n]*ph; X1+=C[n]*(2*pi*I*n*ph)
    return X0,X1
den=1-Fb
stack=[(arb(2*i+1)/(2*NC0), arb(1)/(2*NC0), f'{i}') for i in range(NC0) if i%nw==wk]
stack.reverse(); worst=0.0
while stack:
    tc,h,lab=stack.pop()
    X0,X1=X_at(tc)
    n0=rignorm(X0); q=h*h/2*L2+T0
    n1=frob(X1); bd=((n0+h*n1+q)/den).upper(); how='F'
    if bd>ftarget:
        n1=rignorm(X1); bd=((n0+h*n1+q)/den).upper(); how='S'
    if bd<=ftarget:
        worst=max(worst,float(bd)); emit(kind='cell',lab=lab,tc=float(tc.mid()),h=float(h.mid()),n0=float(n0),n1=float(n1.upper()) if hasattr(n1,'upper') else float(n1),how=how,bound=float(bd))
    else:
        h2=h/2; stack.append((tc+h2,h2,lab+'R')); stack.append((tc-h2,h2,lab+'L'))
        emit(kind='split',lab=lab,tc=float(tc.mid()),h=float(h.mid()),n0=float(n0),bound=float(bd))
emit(kind='done',worker=wk,worst=worst)
print('worker',wk,'done worst',worst,round(time.time()-t0,1),flush=True)
