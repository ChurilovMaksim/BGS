"""N3 (I) [CA*]: verified-floating-point certificate for the free twisted family in the Line F space.
Given R (float, from g2_ext_norm.py), prove   sup_{tau in R/Z} ||R A_tau R^{-1}||_2 <= f_cert,  where
  A_tau = sum_{|n|<=Nmax} w_0(n) e(n tau) B_n  is the core<-core Galerkin section (letters |n|<=Nmax, sector 0, eta=2).
Exact blocks B_n are built in arb (same formulas as bgs-lineF/code/cert_lift.py) and rounded to double with recorded radii.
Rounding of every float matrix product is bounded a priori: |fl(XY) - XY| <= g_n |X||Y|, g_n = 2(n+4)u/(1-2(n+4)u) (complex,
Higham Thm 3.5 type, generous), u = 2^-53; all bound computations are inflated by (1+1e-9).
Steps: S ~ R^{-1}; F = RS - I bounded;  C_n = R (w_n B_n) S with error matrices;  for tau on a grid of NG points:
  Y = sum e(n tau) C_n,  ||Y||_2 <= sqrt(lam_max(Y^*Y)) bounded via eigh + residual + Ostrowski;  then
  sup over the grid cell via Lipschitz 2 pi h/2 sum |n| ||C_n||_F;  divide by (1-||F||).
Then the full operator: L = T + E with T = [[PAP,0],[X,0]] and ||E|| <= eps = delta1+delta2+Delta (Line F certificate numbers for the
same (typ,K0,rho,K,beta), uniform in tau since all bounds use |w(n)|):  |||L_tau||| <= f_cert + pi_pen  for the norm
 |||(u,t,y)||| = max(||Ru||, ||t||, b||y||), b = f/(||X|| (||R^{-1}||+1)).
usage: i_verify.py typ K0 rho K Rfile NG Nmax certjson out.json"""
import sys, json, time, math, numpy as np
from flint import arb, acb, acb_mat, ctx
ctx.prec=128
typ=sys.argv[1]; K0=int(sys.argv[2]); rho_s=sys.argv[3]; K=int(sys.argv[4]); Rfile=sys.argv[5]; NG=int(sys.argv[6]); Nmax=int(sys.argv[7])
certjson=sys.argv[8]; outf=sys.argv[9]
t0=time.time(); u=2.0**-53; SAFE=1+1e-9
two=arb(2); lam=3+2*two.sqrt(); cc=1/(lam-1/lam); pi=arb.pi(); I=acb(0,1); rho=arb(rho_s); half=arb(1)/2; x=arb('1.8')
def e(t): return (2*pi*I*t).exp()
def certfloor(y):
    f=int(math.floor(float(y.mid()))); 
    assert (y-f).lower()>=0 or True
    if not ((y-f)>0 or (y-f)==0): raise ValueError
    if not (y-f-1<0): raise ValueError
    return f
# ---- target map exactly as cert_lift (V: centres c in Z; E: c in Z+1/2) ----
Rc = arb(K0) if typ=='V' else arb(K0)-half
def rnd(t): return certfloor(t+half)
def target(c2,n):
    c=arb(c2)/2
    if typ=='V':
        j=rnd((c+n)/lam); dl=(c+n)/lam-j; return (2*j,dl)
    a=rnd((c-half+n)/lam); b=rnd((c+half+n)/lam)
    if b!=a+1: return None
    j=arb(a)+half; dl=(c+n)/lam-j; return (2*a+1,dl)
iscore=lambda c2: abs(arb(c2)/2)<=Rc
cores=[c2 for c2 in range(-2*K0-2,2*K0+3) if (c2%2==(0 if typ=='V' else 1)) and iscore(c2)]
idx={c2:i for i,c2 in enumerate(cores)}; nc=len(cores); D=nc*K
fact=[arb(1)]
for i in range(1,K+1): fact.append(fact[-1]*i)
lamp=[arb(1)]
for i in range(1,K+1): lamp.append(lamp[-1]/lam)
J={n: x.bessel_j(arb(abs(n)))*(1 if (n>=0 or n%2==0) else -1) for n in range(-Nmax,Nmax+1)}
def w0(n): return (I**(n%4))*J[n]*e(cc*n*n/2)
Bf={}; Brad={}
for n in range(-Nmax,Nmax+1):
    M_=np.zeros((D,D),complex); Rad=np.zeros((D,D))
    wn=w0(n); any_=False
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
        Cm=acb_mat(K,K); B=dl/rho; bp=[arb(1)]
        for i in range(1,K): bp.append(bp[-1]*B)
        for k in range(K):
            for jj in range(k+1): Cm[jj,k]=fact[k]/(fact[jj]*fact[k-jj])*lamp[jj]*bp[k-jj]
        blk=(Mm*Cm)*(e(cc*n*arb(c2)/2)*wn)
        r0=idx[c2]*K; c0=idx[j2]*K
        for a in range(K):
            for b in range(K):
                v=blk[a,b]; M_[r0+a,c0+b]=complex(float(v.real.mid()),float(v.imag.mid()))
                Rad[r0+a,c0+b]=float(v.real.rad())+float(v.imag.rad())+abs(M_[r0+a,c0+b])*u*2
        any_=True
    if any_: Bf[n]=M_; Brad[n]=Rad
print('blocks built',len(Bf),round(time.time()-t0,1),'s',flush=True)
R=np.load(Rfile); assert R.shape==(D,D), (R.shape,D)
def g(n): k=2*(n+4)*u; return k/(1-k)
gD=g(D)*SAFE
absR=np.abs(R)
S=np.linalg.inv(R); absS=np.abs(S)
Fm=R@S-np.eye(D); Fbound=np.linalg.norm(np.abs(Fm)+gD*(absR@absS),'fro')*SAFE+ D*u
assert Fbound<0.5, Fbound
normR=np.linalg.norm(R,2)*(1+1e-6); normS_upper=np.linalg.norm(S,'fro')*(1+1e-6)  # ||S||_2<=||S||_F
normRinv=normS_upper/(1-Fbound)   # R^{-1} = S (RS)^{-1}
C={}; Cerr=0.0; Lip=0.0
for n in Bf:
    T1=R@Bf[n]; e1=gD*(absR@np.abs(Bf[n]))+absR@Brad[n]
    Cn=T1@S; e2=gD*(np.abs(T1)@absS)+e1@absS
    C[n]=Cn; Cerr+=np.linalg.norm(e2,'fro')*SAFE
    Lip+=2*math.pi*abs(n)*np.linalg.norm(Cn,'fro')*SAFE
Cerr+=len(C)*D*u*max(np.linalg.norm(c,'fro') for c in C.values())  # summation rounding of Y (generous)
print('Fbound',Fbound,'Cerr',Cerr,'Lip',Lip,round(time.time()-t0,1),'s',flush=True)
ns=np.array(sorted(C)); Cst=np.stack([C[n] for n in ns])
best=0.0; arg=None
for gi in range(NG):
    tau=(gi+0.5)/NG
    Y=np.tensordot(np.exp(2j*np.pi*ns*tau),Cst,axes=1)
    G=Y.conj().T@Y; Gerr=np.linalg.norm(gD*(np.abs(Y).T@np.abs(Y)),'fro')*SAFE
    lamv,Q=np.linalg.eigh(G)
    Res=G-(Q*lamv)@Q.conj().T; resb=np.linalg.norm(np.abs(Res)+gD*(np.abs(Q)*np.abs(lamv))@np.abs(Q).T+gD*np.abs(G),'fro')*SAFE
    QQ=Q.conj().T@Q-np.eye(D); qqb=np.linalg.norm(np.abs(QQ)+gD*(np.abs(Q).T@np.abs(Q)),'fro')*SAFE
    lmax=max(lamv.max(),0)*(1+qqb)+resb+Gerr
    sig=math.sqrt(lmax)*SAFE
    if sig>best: best=sig; arg=tau
fgrid=best+Cerr
fcell=fgrid+Lip*(0.5/NG)
fcert=fcell/(1-Fbound)
cj=json.load(open(certjson)); eps=cj['delta1']+cj['delta2']+cj['Delta']; Xn=cj['Xnorm']
b=fcert/(Xn*(normRinv+1))
pen=eps*max(normR,1.0,b)*(normRinv+1+1/b)
res=dict(typ=typ,K0=K0,rho=rho_s,K=K,NG=NG,Nmax=Nmax,Rfile=Rfile,Fbound=Fbound,Cerr=Cerr,Lip=Lip,max_grid=best,argmax=arg,
         f_cell=fcell,f_cert=fcert,eps=eps,Xnorm=Xn,normR=normR,normRinv=normRinv,b=b,penalty=pen,Lambda_free_upper=fcert+pen,
         kappa=max(normR,1.0,b)*(normRinv+1+1/b),sec=round(time.time()-t0,1))
print(json.dumps(res),flush=True); json.dump(res,open(outf,'w'),indent=1)
