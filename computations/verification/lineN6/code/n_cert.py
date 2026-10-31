"""N6 (1) [CA]: rigorous enclosures of the excursion factors r_A, r_B, hence c* = |r_A r_B|^3 and w* = -(r_A r_B)^3 (the family/Z_rho limit),
for the Line F lifted sector-4 vertex operator (eta = 2, k1 kick; coef = +C0, i.e. rho = (-2,8); (2,8) is the complex conjugate).
Representation, Galerkin blocks, delta1/delta2/Delta/||X|| are those of Line F certV_eta2_a4_tight (cert_core.py = verbatim set-up).
Twisted operators L_t (t = 1/2 + d) differ only by letter phases e(n d): all truncation bounds depend on |w(n)| only, so the same
Pert = delta1+delta2+Delta bounds ||L_t - T_t|| for every t (T_t = [[A_t,0],[X_t,0]] comparison operator, ||X_t|| <= ||X||).
Float linear algebra with a-priori rounding bounds (gamma_n |A||B|), arb for all scalar bookkeeping.  See REPORT_N6 §1 for the proof."""
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
a=(2-arb(2).sqrt())/4; b=arb(2).sqrt()/4; KK=18
dA_=[-a*lam**k for k in range(-KK,1)]+[a*lam**(-(k-1)) for k in range(1,KK+2)]     # k=-KK..KK+1 (30 steps)
dB_=[-b*lam**(-abs(k)) for k in range(-KK,KK+1)]                                 # 29 steps
tailA=2*a*lam**(-(KK+1))/(1-1/lam); tailB=2*b*lam**(-(KK+1))/(1-1/lam)   # sum of |d| over both outer tails (each side <= half... use total per side bound)
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
rA=excursion(dA_,tailA); print('A',rA,round(time.time()-t0,1),flush=True)
rB=excursion(dB_,tailB); print('B',rB,round(time.time()-t0,1),flush=True)
ctx.prec=64
def ball(r): return acb(arb(float(r['value'][0]),float(r['radius'])),arb(float(r['value'][1]),float(r['radius'])))
A_=ball(rA); B_=ball(rB); P=A_*B_; w=-(P**3)
res=dict(N1=up(N1),Pert=up(Pert),Xn=up(Xn),s=[s.real,s.imag],mu_minus_s=mu_minus_s,RA_Gamma=RA,RT_Gamma=RT,dPi=dPi,normPiA=normPiA,normPi=normPi,Cpow=Cpow,
         rA=rA,rB=rB,abs_rA=str(abs(A_)),abs_rB=str(abs(B_)),cstar=str(abs(P)**3),w=str(w),Re_w=str(w.real),Im_w=str(w.imag),arg_w=str(w.arg()),
         Re_w_positive=bool(w.real>0),cstar_lower=float((abs(P)**3).lower()),cstar_upper=float((abs(P)**3).upper()),secs=round(time.time()-t0,1))
print(json.dumps({k:res[k] for k in ['abs_rA','abs_rB','cstar','w','arg_w','Re_w_positive','secs']},indent=1))
json.dump(res,open('/workspace/bgs-lineN/N6/logs/n_cert.json','w'),indent=1)
