"""N11b [CA]: certificate of the UNIT-bump activity w_U(beta) = r_U^3 (limit p->oo) for a unit point x = beta/h_p at background 0,
using the N9 n9_cert.py machinery VERBATIM (Line F / n_cert inputs) with a single excursion core zeta_U = 2 beta/eps.
usage: u_cert.py tag a b [KK]   (beta = a + b sqrt2)
Original header follows.
N8 [CA]: generalisation of N6 n_cert.py (verbatim certificate logic) to the excursion cores of ANY isotropic class (z, e) whose two
windows sit at the same base twist t0 in {0, 1/2} (true for z=1/4, e=2alpha and z=0, e=2sqrt2 alpha).  By Lemma P'(iv) (REPORT_N7 sec 2)
the cores are d_j = emb1(lam^j zeta) (mod 1) for j<=0 and -emb2(lam^j zeta) (mod 1) for j>=1, zeta_A = e eps^{-(k mod 2)}/(4 sqrt2),
zeta_B = -(-1)^k e eps^{2 floor((3k+1)/2)-3k-1}/(4 sqrt2) (k = (p-1)/2; we use k even, the odd case swaps A and B).
Amat(d) = sector-4 weights twisted by d: for t0 = 0 the window operator is L_{4,d} itself (ratio sign +1); for t0 = 1/2 it is
L_{0,1/2+d} = Amat(d) with c_0/c_4 = -1 (sign -1).  w = sign*(r_A r_B)^3 for rho = (-2,8) (coef +C0); (2,8) is the conjugate.
usage: n8_cert.py tag t0 e_a e_b [KK]     (e = e_a + e_b sqrt2, integers)"""
import sys, json, time, math
import numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N6/code')
import cert_core as C
from flint import arb, acb, ctx
ctx.prec=128
t0=time.time()
lam=C.lam; pi=C.pi; I=C.I; D=C.D; K=C.K
Pert=C.delta+C.Delta; Xn=C.Xn
u=2.0**-53
def gam(n): return 1.05*(n+4)*2*u*math.sqrt(2)      # complex inner products of length n, conservative
def up(x): return float(x.upper()) if isinstance(x,arb) else float(x)
# ---------- derivative bound N1:  ||L_{t+d}-L_t|| <= 2 pi |d| N1  (weights |n||w(n)|, all rows, letter block bounds of cert_lift)
def btail1(alpha):
    t=C.x*alpha.exp()/2; N=C.Nmax; f=arb(1)
    for i in range(1,N+1): f*=i
    q=t/(N+1); assert q<1
    return 2*t*t**N/f/(1-q)
rows={}
lat=[c2 for c2 in range(-2*C.Rmax,2*C.Rmax+1) if c2%2==0]
al=2*pi*C.cc*C.rho+C.beta/lam
for c2 in lat:
    s_=arb(0)
    for n in range(-C.Nmax,C.Nmax+1):
        if n==0: continue
        tg=C.target(c2,n)
        if tg is None: continue
        j2,dl=tg; th=abs(dl)/C.rho+1/lam; assert th<1
        s_+=abs(n)*C.W[n]*C.Mn(n,C.rho)/(1-th*th).sqrt()*C.om(c2)/C.om(j2)
    tailfac=(C.om(c2) if not C.iscore(c2) else arb(1))*(C.beta*(abs(arb(c2)/2)/lam+C.half)).exp()
    s_+=tailfac*btail1(al)/(1-C.thstar*C.thstar).sqrt()
    rows[c2]=s_
B0=sum((abs(n)*C.W[n]*C.Mn(n,C.rho) for n in C.J),arb(0))+btail1(2*pi*C.cc*C.rho)
B1=sum((abs(n)*C.W[n]*C.Mn(n,C.rho)*(C.beta*abs(n)/lam).exp() for n in C.J),arb(0))+btail1(2*pi*C.cc*C.rho+C.beta/lam)
g1=C.beta; g2=C.beta*(1-1/lam); cmin=arb(C.Rmax)+C.half
geo=lambda g,pw: 2*(-pw*g*cmin).exp()/(1-(-pw*g).exp())
far2=2*((g1*C.Rc).exp()**2*geo(g1,2)*B0**2+(C.beta).exp()*geo(g2,2)*B1**2)/(1-C.thstar*C.thstar)
N1=(sum((v**2 for v in rows.values()),arb(0))+far2).sqrt()
print('N1',N1.upper(),'Pert',Pert.upper(),'Xn',Xn.upper(),round(time.time()-t0,1),flush=True)
# ---------- twisted core matrices
agg_keys=sorted(set((c2,j2) for (c2,n),(j2,M) in C.blocks.items()))
def Amat(d):   # sector 4 plus twist d: weight w_4(n) e(n d)
    agg={}
    for (c2,n),(j2,Mx) in C.blocks.items():
        term=Mx*(C.wa(4,n)*C.e(arb(n)*d)); key=(c2,j2)
        agg[key]=term if key not in agg else agg[key]+term
    A=np.zeros((D,D),complex); rad=0.0
    for (c2,j2),S in agg.items():
        i0=C.idx[c2]*K; j0=C.idx[j2]*K
        for i in range(K):
            for j in range(K):
                z=S[i,j]; A[i0+i,j0+j]=complex(float(z.real.mid()),float(z.imag.mid()))
                rad=max(rad,float(z.real.rad())+float(z.imag.rad()))
    # midpoint->double rounding: |z - fl(z)| <= u|z| ; collect as Frobenius bound
    dA=math.sqrt(D*D)*rad+u*np.linalg.norm(A)*1.01
    return A,dA
TAG=sys.argv[1]; BA=int(sys.argv[2]); BB=int(sys.argv[3]); KK=int(sys.argv[4]) if len(sys.argv)>4 else 18
T0='0'; SIGN=1
r2=arb(2).sqrt(); epsq=1+r2
def red(x):
    n=(x+arb(1)/2).floor(); return x-n
def core(zu,zv):
    e1=zu+zv*r2; e2=zu-zv*r2
    L1=max(0,math.ceil(float((abs(e1)+1).log()/lam.log()))); L2=max(0,math.ceil(float((abs(e2)+1).log()/lam.log())))
    ds=[]
    for j in range(-(KK+L1),KK+L2+1):
        x=e1*lam**j if j<=0 else -e2*lam**(-j)
        ds.append(red(x))
    tail=abs(e1)*lam**(-(KK+L1+1))/(1-1/lam)+abs(e2)*lam**(-(KK+L2+1))/(1-1/lam)
    return ds,tail
# UNIT point beta = BA + BB sqrt2 at level h_p, background 0: core zeta_U = 2 beta / eps  (limit p->oo; exact value carries 1/(1-lam^-p))
# 2 beta/eps = 2 beta (sqrt2 - 1) = 2[(BA+BB s)(-1+s)] = 2[(-BA+2BB) + (BA-BB) s]
zu=2*(-arb(BA)+2*arb(BB)); zv=2*(arb(BA)-arb(BB))
dU_,tailU=core(zu,zv)
print('unit core',[round(float(x.mid()),5) for x in dU_ if abs(float(x.mid()))>1e-3],'tail',float(tailU.upper()),flush=True)
A0,dA0=Amat(arb(0))
print('A0 built',round(time.time()-t0,1),flush=True)
ev,R=np.linalg.eig(A0); i=np.argmax(abs(ev)); s=ev[i]; Phi=R[:,i]/np.linalg.norm(R[:,i])
evl,Lv=np.linalg.eig(A0.T); psi=Lv[:,np.argmin(abs(evl-s))]; psi=psi/np.linalg.norm(psi)
b11=acb(arb('1.3572399242659728227708727178601298'),arb('-1.3516424762972735896036200390941797'))
sA=acb(s.real,s.imag)
mu_minus_s=up(abs(b11-sA))+2e-6        # |mu - b11| <= r1 = 2e-6 (Line F certified), plus |b11 - s|
print('s',s,'|b11-s|',up(abs(b11-sA)),flush=True)
# ---------- rigorous resolvent bound of A0 on Gamma: |z - s| = rc
rc=0.6; NG=512; RA=0.0
absA0=np.abs(A0)
for k in range(NG):
    z=s+rc*np.exp(2j*np.pi*k/NG); M=z*np.eye(D)-A0
    Y=np.linalg.inv(M); Rr=np.eye(D)-M@Y
    rb=np.linalg.norm(Rr)*1.01+gam(D)*np.linalg.norm(np.abs(M)@np.abs(Y))*1.01+dA0*np.linalg.norm(Y)*1.01
    assert rb<0.5
    nY=np.linalg.norm(Y)*1.01/(1-rb)
    RA=max(RA,nY)
hstep=2*math.pi*rc/NG/2
assert hstep*RA<0.5
RA=RA/(1-hstep*RA)
RT=RA*(1+up(Xn)/(abs(s)-rc))+1/(abs(s)-rc)        # resolvent of T0'=[[A0,0],[X,0]] on Gamma
FRT=up(Pert)*RT; assert FRT<0.5
dPi=rc*RT*RT*up(Pert)/(1-FRT)                   # ||Pi - Pi_{T0'}||
print('RA(Gamma)',RA,'RT',RT,'||Pi-Pi_T||',dPi,round(time.time()-t0,1),flush=True)
# ---------- eigenvector residuals and the exact core projector Pi_A (rank one; Line F: exactly one eigenvalue of A0 in |z|>1)
def mv_err(Mm,v,dM):   # bound on ||Mm v - fl(Mm v)|| + ||dM|| ||v||
    return gam(D)*np.linalg.norm(np.abs(Mm)@np.abs(v))*1.01+dM*np.linalg.norm(v)
rR=A0@Phi-s*Phi; erR=np.linalg.norm(rR)*1.01+mv_err(A0,Phi,dA0)+u*abs(s)*2
rL=A0.T@psi-s*psi; erL=np.linalg.norm(rL)*1.01+mv_err(A0.T,psi,dA0)+u*abs(s)*2
er=RA*erR; el=RA*erL                           # ||(1-Pi_A)Phi~||, ||psi~^T(1-Pi_A)||  (reduced resolvent at the centre s)
den0=psi@Phi; den=abs(den0)-er               # |psi~^T Pi_A Phi~| >= |psi~.Phi~| - ||e_r||
normPiA=(1+er)*(1+el)/den
normPiT=normPiA*math.sqrt(1+(up(Xn)/(abs(s)-mu_minus_s))**2)
normPi=normPiT+dPi
R2=0.0  # Line F: F_R2 = F * R2 with F = b21 + Pert
lf=json.load(open('/workspace/bgs-lineF/logs/certV_eta2_a4_tight.json'))['sectors']['4']
Fcert=lf['b21']+up(Pert); R2=lf['F_R2']/Fcert*1.0000001
Cpow=normPi+R2/(1-lf['F_R2'])
print('||Pi_A||<=',normPiA,'||Pi||<=',normPi,'Cpow<=',Cpow,'er,el',er,el,flush=True)
def excursion(ds,tail):
    As=[]; dAs=[]
    for d in ds:
        A,dA=Amat(d); As.append(A/s); dAs.append(dA/abs(s)+u*np.linalg.norm(A/s)*2)
    n=len(As)
    # G_A: max over contiguous sub-products of Frobenius bound (incl. rounding propagation); empty product -> 1
    # rigorous: for every contiguous interval I, ||Q_I|| <= ||P^_I||_F + G * sum_k delta_k(I)  (delta_k = local rounding/midpoint error,
    # later factors bounded by G itself)  =>  G <= max ||P^_I||_F / (1 - max_I sum_k delta_k(I)).
    Gh=1.0; Dm=0.0
    for i0 in range(n):
        P=np.eye(D,dtype=complex); acc=0.0
        for j in range(i0,n):
            nP=np.linalg.norm(P)*1.01
            acc+=dAs[j]*nP+gam(D)*np.linalg.norm(np.abs(As[j])@np.abs(P))*1.01
            P=As[j]@P; Gh=max(Gh,np.linalg.norm(P)*1.01); Dm=max(Dm,acc)
    assert Dm<0.5
    GA=Gh/(1-Dm)
    GT=GA*(1+up(Xn)/abs(s))
    # core matrix element with the approximate Perron vectors, rigorous propagation
    v=Phi.copy(); acc=0.0
    for M,dM in zip(As,dAs):
        acc+=dM*np.linalg.norm(v)*1.01+gam(D)*np.linalg.norm(np.abs(M)@np.abs(v))*1.01; v=M@v
    ev_=GA*acc
    num=psi@v; num_err=ev_*1.01+gam(D)*np.linalg.norm(np.abs(psi))*np.linalg.norm(np.abs(v))
    # Tr(Pi_A M) = v^T M u / (psi.Phi - psi.e_r):  |.. - psi^T M Phi/psi.Phi| <= ...
    Mnorm=GA
    tr_approx=num/den0
    err_proj=(el*Mnorm*1+Mnorm*er+el*Mnorm*er+num_err)/den+abs(num)/abs(den0)*er/den
    Fs=up(Pert)/abs(s)
    prodL=GT*(1+GT*Fs)**n
    err_pert=2*dPi*prodL+normPiT*GT*((1+GT*Fs)**n-1)
    eps=math.exp(Cpow*2*math.pi*up(N1)*up(tail)/(abs(s)-mu_minus_s))-1
    scale=(1+mu_minus_s/(abs(s)-mu_minus_s))**n-1     # |(s/mu)^n - 1|
    err_tail=normPi*prodL*(1+scale)*((1+eps)**2-1)
    tot=abs(tr_approx)*scale+(err_proj+err_pert)*(1+scale)+err_tail
    return dict(n=n,GA=GA,GT=GT,value=[tr_approx.real,tr_approx.imag],err_proj=err_proj,err_pert=err_pert,eps_tail=eps,err_tail=err_tail,scale=scale,radius=tot)
rU=excursion(dU_,tailU); print('U',rU,round(time.time()-t0,1),flush=True)
ctx.prec=64
def ball(r): return acb(arb(float(r['value'][0]),float(r['radius'])),arb(float(r['value'][1]),float(r['radius'])))
U_=ball(rU); w=SIGN*(U_**3)
res=dict(beta=[BA,BB],KK=KK,N1=up(N1),Pert=up(Pert),Cpow=Cpow,rU=rU,abs_rU=str(abs(U_)),w=str(w),Re_w=str(w.real),Im_w=str(w.imag),
         Re_w_lower=float(w.real.lower()),Re_w_upper=float(w.real.upper()),Im_w_lower=float(w.imag.lower()),Im_w_upper=float(w.imag.upper()),
         absw_upper=float(abs(w).upper()),absw_lower=float(abs(w).lower()),secs=round(time.time()-t0,1))
print('ENDPOINTS',json.dumps({k:res[k] for k in ['Re_w_lower','Re_w_upper','Im_w_lower','Im_w_upper','absw_lower','absw_upper']}),flush=True)
json.dump(res,open(f'/workspace/bgs-lineN/N11b/logs/u_cert_{TAG}.json','w'),indent=1)
