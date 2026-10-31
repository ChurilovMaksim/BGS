"""Referee: independent Schur-test certificate for N4 (8E, 16V, 16E core bounds).
Scalar majorant M_s = sum_n |J_n(1.8)| |B_n| (blocks rebuilt here in arb; multiplier coefficient c0/kdiv).
For the (+-2,16) tensor M = M_e (x) I + M_o (x) swap, the test vector x_s (x) (1,1) gives M x = (M_s x_s) (x) (1,1), so
alpha, beta of the scalar M_s bound the tensor (any PAR).  Own Perron vectors (scipy eigs), own regularisation, arb check.
usage: typ K0 rho K Nmax kdiv"""
import sys, math, json, time, numpy as np
from flint import arb, acb, acb_mat, arb_mat, ctx
from scipy.sparse.linalg import eigs
ctx.prec=100
typ=sys.argv[1]; K0=int(sys.argv[2]); rho=arb(sys.argv[3]); K=int(sys.argv[4]); Nmax=int(sys.argv[5]); kdiv=int(sys.argv[6])
t0=time.time(); lam=3+2*arb(2).sqrt(); kap=1/(lam-1/lam)/kdiv; pi=arb.pi(); I=acb(0,1); half=arb(1)/2; x=arb('1.8')
Rc=arb(K0) if typ=='V' else arb(K0)-half
def rnd(t):
    f=math.floor(float((t+half).mid())); assert (t+half-f)>0 and (t+half-f-1)<0; return f
def target(c2,n):
    c=arb(c2)/2
    if typ=='V':
        j=rnd((c+n)/lam); return 2*j,(c+n)/lam-j
    a=rnd((c-half+n)/lam); b=rnd((c+half+n)/lam)
    if b!=a+1: return None
    return 2*a+1,(c+n)/lam-(arb(a)+half)
iscore=lambda c2: abs(arb(c2)/2)<=Rc
cores=[c2 for c2 in range(-2*K0-2,2*K0+3) if c2%2==(0 if typ=='V' else 1) and iscore(c2)]
ix={c:i for i,c in enumerate(cores)}; D=len(cores)*K
fact=[arb(1)]
for i in range(1,K+1): fact.append(fact[-1]*i)
Ma=[[arb(0)]*D for _ in range(D)]
for n in range(-Nmax,Nmax+1):
    jn=abs(x.bessel_j(arb(abs(n))))
    for c2 in cores:
        tg=target(c2,n)
        if tg is None or not iscore(tg[0]): continue
        j2,dl=tg; z=2*pi*I*kap*n*rho; B=dl/rho
        M=acb_mat(K,K); Cm=acb_mat(K,K)
        for l in range(K):
            for jj in range(l+1): M[l,jj]=z**(l-jj)/fact[l-jj]
        for k in range(K):
            for jj in range(k+1): Cm[jj,k]=fact[k]/(fact[jj]*fact[k-jj])*lam**(-jj)*B**(k-jj)
        blk=M*Cm; r0=ix[c2]*K; c0=ix[j2]*K
        for a in range(K):
            for b in range(K): Ma[r0+a][c0+b]+=abs(blk[a,b])*jn
Mf=np.array([[float(v.mid()) for v in row] for row in Ma])
MA=arb_mat(Ma)
def perron(A):
    w,v=eigs(A,k=1,which='LM'); v=np.abs(np.real(v[:,0])); return v/v.max(), abs(w[0])
xv,lx=perron(Mf); yv,ly=perron(Mf.T)
xv=xv+1e-9; yv=yv+1e-9
xa=arb_mat([[float(t)] for t in xv]); ya=arb_mat([[float(t)] for t in yv])
Mx=MA*xa; My=MA.transpose()*ya
al=max(float((Mx[i,0]/xa[i,0]).upper()) for i in range(D)); be=max(float((My[i,0]/ya[i,0]).upper()) for i in range(D))
f=(arb(al)*arb(be)).sqrt()
print(json.dumps(dict(typ=typ,K0=K0,rho=str(rho),K=K,Nmax=Nmax,kdiv=kdiv,dim=D,perron=[lx,ly],alpha=al,beta=be,f_upper=float(f.upper())*(1+1e-15),sec=round(time.time()-t0,1))),flush=True)
