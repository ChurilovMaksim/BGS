"""Referee arb spot-check of the N3 Lambda certificate: for selected tau, rigorous ball-arithmetic upper bound of
||R A_tau R^{-1}||_2 (A_tau = core Galerkin section, letters |n|<=Nmax, sector 0), plus arb Lipschitz constant.
Blocks are rebuilt here in arb (same formulas as Line F cert_lift); ||.||_2 via G=Y*Y, float eigvecs Q, Gershgorin on Q*GQ.
usage: typ K0 rho K Rfile Nmax tau1,tau2,..  [lip]"""
import sys, math, json, time, numpy as np
from flint import arb, acb, acb_mat, arb_mat, ctx
ctx.prec=96
typ=sys.argv[1]; K0=int(sys.argv[2]); rho=arb(sys.argv[3]); K=int(sys.argv[4]); R=np.load(sys.argv[5]); Nmax=int(sys.argv[6])
taus=[float(t) for t in sys.argv[7].split(',')]; dolip=len(sys.argv)>8
t0=time.time(); two=arb(2); lam=3+2*two.sqrt(); cc=1/(lam-1/lam); pi=arb.pi(); I=acb(0,1); half=arb(1)/2; x=arb('1.8')
e=lambda t:(2*pi*I*t).exp()
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
J={n:x.bessel_j(arb(abs(n)))*(1 if (n>=0 or n%2==0) else -1) for n in range(-Nmax,Nmax+1)}
blocks={}  # (c2,j2) -> list of (n, acb_mat)
for n in range(-Nmax,Nmax+1):
    wn=(I**(n%4))*J[n]*e(cc*n*n/2)
    for c2 in cores:
        tg=target(c2,n)
        if tg is None or not iscore(tg[0]): continue
        j2,dl=tg
        z=2*pi*I*cc*n*rho
        M=acb_mat(K,K); Cm=acb_mat(K,K); B=dl/rho
        for l in range(K):
            for jj in range(l+1): M[l,jj]=z**(l-jj)/fact[l-jj]
        for k in range(K):
            for jj in range(k+1): Cm[jj,k]=fact[k]/(fact[jj]*fact[k-jj])*lam**(-jj)*B**(k-jj)
        blocks.setdefault((c2,j2),[]).append((n,(M*Cm)*(e(cc*n*arb(c2)/2)*wn)))
print('blocks',sum(len(v) for v in blocks.values()),round(time.time()-t0,1),flush=True)
def place(parts):
    A=acb_mat(D,D)
    for (c2,j2),Mb in parts.items():
        r0=ix[c2]*K; c0=ix[j2]*K
        for a in range(K):
            for b in range(K): A[r0+a,c0+b]=Mb[a,b]
    return A
def A_tau(tau):
    parts={}
    for key,lst in blocks.items():
        S=None
        for n,Mb in lst:
            T=Mb*e(arb(tau)*n)
            S=T if S is None else S+T
        parts[key]=S
    return place(parts)
Rf=R; Sf=np.linalg.inv(Rf)
Ra=acb_mat([[acb(complex(v).real,complex(v).imag) for v in row] for row in Rf])
Sa=acb_mat([[acb(complex(v).real,complex(v).imag) for v in row] for row in Sf])
F=Ra*Sa
for i in range(D): F[i,i]-=1
fF=arb(0)
for i in range(D):
    for j in range(D): fF+=abs(F[i,j])**2
fF=fF.sqrt(); inv_fac=1/(1-fF)
print('||RS-I||_F <=',float(fF.upper()),round(time.time()-t0,1),flush=True)
def norm2_upper(Y):
    G=Y.conjugate().transpose()*Y
    Gm=np.array([[complex(float(G[i,j].real.mid()),float(G[i,j].imag.mid())) for j in range(D)] for i in range(D)])
    w,Q=np.linalg.eigh(Gm)
    Qa=acb_mat([[acb(v.real,v.imag) for v in row] for row in Q])
    M=Qa.conjugate().transpose()*G*Qa; QQ=Qa.conjugate().transpose()*Qa
    g=0.0
    for i in range(D):
        s=M[i,i].real
        for j in range(D):
            if j!=i: s+=abs(M[i,j])
        g=max(g,float(s.upper())*(1+1e-15))
    q=arb(0)
    for i in range(D):
        for j in range(D):
            v=QQ[i,j]-(1 if i==j else 0); q+=abs(v)**2
    q=q.sqrt()
    return (arb(g)/(1-q)).sqrt(), math.sqrt(max(w))
res=[]
for tau in taus:
    A=A_tau(tau); Y=Ra*A*Sa
    ub,fl=norm2_upper(Y); ub=ub*inv_fac
    r=dict(tau=tau,norm_upper=float(ub.upper()),float_sigma=fl,sec=round(time.time()-t0,1)); res.append(r); print(json.dumps(r),flush=True)
if dolip:
    Lip=arb(0)
    for key,lst in blocks.items():
        pass
    # per letter n: C_n = R B_n S, B_n placed sparse
    byn={}
    for key,lst in blocks.items():
        for n,Mb in lst: byn.setdefault(n,{})[key]=Mb
    for n,parts in byn.items():
        Cn=Ra*place(parts)*Sa; f=arb(0)
        for i in range(D):
            for j in range(D): f+=abs(Cn[i,j])**2
        Lip+=2*pi*abs(n)*f.sqrt()
    print(json.dumps(dict(Lip_upper=float(Lip.upper()),sec=round(time.time()-t0,1))),flush=True)
