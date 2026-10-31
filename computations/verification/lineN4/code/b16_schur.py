"""N4 (B16) [CA]: twist- and block-uniform certificate for the (+-2,16) families in the Line F space.
Operator (core<-core Galerkin section, letters |n|<=Nmax):  A_{B,tau} = sum_n w(n) e(n tau) B_n (x) A_{B,n},
  w(n) = i^n J_n(1.8) e(C n^2/2),  B_n = core Galerkin block of the lift with multiplier coefficient |C| = c0/2 (sign irrelevant below),
  A_{B,n} = 2x2 monomial matrix with entries in zeta16^Z in the orthonormalised (f1,f2) basis of block B (J3 blocks16_exact:
  pattern P_n = swap^(n+PAR), PAR in {0,1}; exactly these two patterns occur, verified below from the JSON).
Entrywise |A_{B,tau}| <= M := sum_n |J_n| |B_n| (x) P_n  (independent of tau, B, sign of a).  For positive x,y with M x <= alpha x,
M^T y <= beta y (Schur test) and D = diag(sqrt(x/y)):  ||D^{-1} A_{B,tau} D||_2 <= ||D^{-1} M D||_2 <= sqrt(alpha beta).
All of M, alpha, beta are computed in arb (ball arithmetic): entries of B_n exactly as in bgs-lineF cert_lift / N3 i_verify.
usage: b16_schur.py typ K0 rho K Nmax prec out.json PAR [FAM=16|8]"""
import sys, json, time, math, numpy as np
from flint import arb, acb, acb_mat, arb_mat, ctx
typ=sys.argv[1]; K0=int(sys.argv[2]); rho_s=sys.argv[3]; K=int(sys.argv[4]); Nmax=int(sys.argv[5]); ctx.prec=int(sys.argv[6]); outf=sys.argv[7]
t0=time.time()
J16=json.load(open('/workspace/bgs-lineJ/J3/logs/blocks16_exact.json'))
pats=set()
for case,v in J16['cases'].items():
    for bb in v['blocks']:
        pats.add(tuple(tuple(bb['act'][str(r)]['perm']) for r in range(16)))
PAR=int(sys.argv[8]); FAM=sys.argv[9] if len(sys.argv)>9 else '16'   # FAM='8': scalar (+-2,8) operator, multiplier coefficient c0, no internal factor   # pattern parity: P_n = swap^(n+PAR)
assert pats=={tuple(((0,1) if (r+q)%2==0 else (1,0)) for r in range(16)) for q in (0,1)}, pats   # exactly two patterns occur (64 blocks each)
two=arb(2); lam=3+2*two.sqrt(); cc=1/(lam-1/lam)/(2 if FAM=='16' else 1); pi=arb.pi(); I=acb(0,1); rho=arb(rho_s); half=arb(1)/2; x18=arb('1.8')
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
idx={c2:i for i,c2 in enumerate(cores)}; nc=len(cores); D=nc*K; NI=2 if FAM=='16' else 1; D2=NI*D
fact=[arb(1)]
for i in range(1,K+1): fact.append(fact[-1]*i)
lamp=[arb(1)]
for i in range(1,K+1): lamp.append(lamp[-1]/lam)
Jabs={n: abs(x18.bessel_j(arb(abs(n)))) for n in range(-Nmax,Nmax+1)}
up=lambda a: math.nextafter(float(a.upper()),math.inf)
# M as float upper bounds (entries are sums of nonneg upper bounds; float summation error absorbed by factor INF below)
M=np.zeros((D2,D2)); nb=0; maxterms=0
cnt=np.zeros((D2,D2),dtype=np.int32)
for n in range(-Nmax,Nmax+1):
    P=(np.eye(2) if (n+PAR)%2==0 else np.array([[0.,1.],[1.,0.]])) if FAM=='16' else np.eye(1)
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
        blk=Mm*Cm; jn=Jabs[n]
        U=np.array([[up(abs(blk[a,b])*jn) for b in range(K)] for a in range(K)])
        r0=idx[c2]*K; c0=idx[j2]*K
        for s in range(NI):
            for t in range(NI):
                if P[s,t]:
                    M[s*D+r0:s*D+r0+K, t*D+c0:t*D+c0+K]+=U; cnt[s*D+r0:s*D+r0+K, t*D+c0:t*D+c0+K]+=1
        nb+=1
kmax=int(cnt.max()); u=2.0**-53; INF=1+2*(kmax+2)*u+1e-15
M*=INF   # rigorous: fl sum of k nonneg terms <= (1+(k-1)u)^... ; generous factor
print('blocks',nb,'dim',D2,'max terms/entry',kmax,round(time.time()-t0,1),'s',flush=True)
# float Perron vectors (power iteration), regularised to be strictly positive
def perron(A):
    v=np.ones(A.shape[0])
    for it in range(3000):
        w=A@v; lamb=np.linalg.norm(w)/np.linalg.norm(v); w/=np.linalg.norm(w)
        if np.linalg.norm(w-v)<1e-14: break
        v=w
    return v, lamb
xv,lx=perron(M); yv,ly=perron(M.T)
reg=1e-8
xv=np.abs(xv)+reg*np.abs(xv).max(); yv=np.abs(yv)+reg*np.abs(yv).max()
print('float perron',lx,ly,flush=True)
# rigorous alpha, beta in arb
Ma=arb_mat(M.tolist())
xa=arb_mat([[float(t)] for t in xv]); ya=arb_mat([[float(t)] for t in yv])
Mx=Ma*xa; MTy=Ma.transpose()*ya
alpha=max((Mx[i,0]/xa[i,0]).upper() for i in range(D2)); beta=max((MTy[i,0]/ya[i,0]).upper() for i in range(D2))
f=(arb(alpha)*arb(beta)).sqrt().upper()
d=np.sqrt(xv/yv); d/=d.max(); cond=float(1/d.min())
print('alpha',float(alpha),'beta',float(beta),'f=sqrt(ab)',float(f),'cond D',cond,round(time.time()-t0,1),'s',flush=True)
json.dump(dict(FAM=FAM,PAR=PAR,typ=typ,K0=K0,rho=rho_s,K=K,Nmax=Nmax,prec=ctx.prec,dim=D2,blocks=nb,alpha=float(alpha),beta=float(beta),
  f_core=float(f),condD=cond,float_perron=[lx,ly],secs=time.time()-t0),open(outf,'w'),indent=1)
np.save(outf.replace('.json','_d.npy'),d)
