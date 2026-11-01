"""N21 (C): Lemma Q + Lemma D^T (true-operator difference form), analytic interaction tail for G >= G1.  REPORT_N21 sec. 4.
Inputs: Lemma C chain arrays for the 5 i-seeds and 20 j-seeds per window ([CA-fp]); N8/N13 certified constants ([CA]).
All G-sums and the geometric remainder are evaluated in arb (python-flint).  usage: tail_DT.py G1 Gmax"""
import os, sys, json, math
os.environ.setdefault('OMP_NUM_THREADS','1'); os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
sys.path.insert(0,'/workspace/bgs-lineN/N21/code')
import conv_c as CC, mpmath as mp
from flint import arb, ctx
ctx.prec=80
G1=int(sys.argv[1]) if len(sys.argv)>1 else 40; GMAX=int(sys.argv[2]) if len(sys.argv)>2 else 200
KK=int(sys.argv[3]) if len(sys.argv)>3 else 18   # single-window padding for the anchors (window = [-(KK+L1), KK+L2])
U=lambda x: arb(x)*(1+arb(2)**-40)          # float input -> slightly widened upper (all inputs are upper bounds >= 0)
def up(a): return float(a.upper())
LAM=arb(3)+2*arb(2).sqrt()
# ---------- certified constants
s=CC.s; abs_s=arb(abs(s))*(1+arb(2)**-50); mus=U(CC.mus); mu_lo=abs_s*(1-arb(2)**-50)-mus
cond=U(CC.CONDH); eta=arb('1e-6'); Pert=U(CC.Pert); Xn=U(CC.Xn); N1=U(CC.N1); Cpow=U(CC.Cpow); normPi=U(CC.N8['normPi'])
xs=Xn/mu_lo*0+U(CC.xs)                       # xs = Xn/|s| (conv_c), upper
ER=U(CC.ER); EL=U(CC.EL); den1=arb(CC.den1)*(1-arb(2)**-40); n2=U(CC.nPhi2); p2=U(CC.npsi2)
psiPhi=CC.psiPhi; one_m=U(abs(psiPhi-1)+CC.eps_p)
# Pi_A, Q_A, delta_Q = ||Pi_A - Phi psi||_2
nPiA=(n2+ER)*(p2+EL)/den1; nQA=1+nPiA
c_lo=den1; c_dev=one_m+p2*ER
dQ=((ER*(p2+EL)+n2*EL)+n2*p2*c_dev)/c_lo
kap=arb('0.45')*(1+eta)+(1+eta)*cond*dQ                 # ||(A0/s)Q_A||_H
sr=abs_s/mu_lo                                           # |s/mu|
assert up(abs_s*kap)<1
# resolvent of T on |z|=1, Lemma Q remainder
RA=nPiA/(abs_s-1)+nQA+cond*(abs_s*kap)/(1-abs_s*kap)
ST=(RA**2+(Xn*RA+1)**2).sqrt()
assert up(ST*Pert)<1
Rem=ST**2*Pert/(1-ST*Pert)
nQ=1+normPi
def mT(k):
    if k==0: return None
    if k==1: return cond*kap+xs*nQA
    return cond*(kap**k+xs*kap**(k-1))
KMAX=2*GMAX+50
m=[nQ]+[sr**k*mT(k)+Rem/mu_lo**k for k in range(1,KMAX)]
K0=min(up(Cpow),up(normPi+max(m[1:4],key=up)))+0.0; K0=U(max(K0,1.0))
assert up(K0)<=up(normPi+m[1])*1.0000001 or up(K0)<=up(Cpow)
rho=arb('0.5225'); assert up(1/mu_lo)<0.5225 and up(kap*sr)<0.5225
Mrho=max([m[0],m[1]/rho,m[2]/rho**2],key=up)
for k in range(2,KMAX-1): assert up(m[k+1]/rho**(k+1))<=up(m[k]/rho**k)*(1+1e-12) or up(m[k+1]/rho**(k+1))<=up(Mrho)
ell=2*arb(math.pi)*N1/mu_lo
nPsiT=U(CC.nPsiT); nPhiT=U(CC.nPhiT); tau=U(CC.tau); dPi=U(CC.dPi); Fs=U(CC.Fs)
nPsiMu=nPsiT*(1+dPi)/(den1-tau); nPhiMu=nPhiT*(1+dPi)
CONST=dict(dQ=up(dQ),kap=up(kap),RA=up(RA),ST=up(ST),Rem=up(Rem),K0=up(K0),m1=up(m[1]),m2=up(m[2]),Mrho=up(Mrho),ell=up(ell),nQ=up(nQ),
           nPiA=up(nPiA),nPsiMu=up(nPsiMu),nPhiMu=up(nPhiMu),m_list={k:up(m[k]) for k in (0,1,2,5,10,20,30,40,60,80)})
print(json.dumps(CONST),flush=True)
# ---------- single seeds
def e12(z): return float(z[0]+z[1]*CC.Dg.S2), float(z[0]-z[1]*CC.Dg.S2)
def single(z):
    ds=CC.Dg.core(z,KK); e1,e2=e12(z)
    L1=max(0,int(mp.ceil(mp.log(abs(mp.mpf(e1))+1)/mp.log(CC.Dg.LAM)))); L2=max(0,int(mp.ceil(mp.log(abs(mp.mpf(e2))+1)/mp.log(CC.Dg.LAM))))
    jlo=-(KK+L1); jhi=KK+L2; kp={}
    r,E,inf=CC.chain(ds,CC.tails(z,KK),keep=kp); n=kp['n']; assert n==jhi-jlo+1
    GL=U(kp['GL']); sc=U(kp['scale']); et=U(kp['eta']); sig=U(kp['sig']); phi=[U(x) for x in kp['phi']]; beta=[U(x) for x in kp['beta']]
    cphi=[arb(0)]
    for k in range(1,n+2): cphi.append(cphi[-1]+phi[k])
    def cov(bk): return (1+sc)*((bk+nPsiT*dPi*GL)/(den1-tau)+nPsiMu*et*GL)          # >= ||psi_mu R_tail P_{>k}|| / |mu|-scaled
    def vec(k): return (1+sc)*(phi[k+1]+Fs*GL*cphi[k]+GL*dPi*nPhiT+GL*nPhiMu*et)    # >= ||P_{<=k} L_tail Phi_mu||
    Kx=K0*(K0*sig).exp()
    Gam=K0*Kx*GL*(1+sc)
    bmax=max(beta,key=up)
    # v2 (referee F1): window-interior covector bound is max_k cov(beta_k), not cov(max_k b_k)
    Psimax=max([Kx*cov(beta[0]),max([cov(bk) for bk in beta],key=up),nPsiMu*(1+K0*sig*(K0*sig).exp())],key=up)
    Phimax=Kx*max([vec(k) for k in range(0,n+1)],key=up)
    WR={}; WL={}
    for D0 in range(1,KK):
        if abs(e1)*float(LAM.mid())**(-D0-1)<0.45 and -D0-jlo>=0: WR[D0]=cov(beta[-D0-jlo])
        if abs(e2)*float(LAM.mid())**(-D0)<0.45 and D0-jlo<=n: WL[D0]=vec(D0-jlo)
    return dict(r=abs(r)+E,e1=abs(e1),e2=abs(e2),jlo=jlo,jhi=jhi,Gam=Gam,Psimax=Psimax,Phimax=Phimax,WR=WR,WL=WL,n=n)
def Yfun(S,D):            # >= ||psi_mu R^i_{>=-D} Q||  (i-role, cut at -D)
    best=None; e1=U(S['e1'])
    for D0,W in S['WR'].items():
        if D0>=D: continue
        sg=ell*e1*LAM**(-D0-1)/(1-1/LAM); Kx=K0*(K0*sg).exp()
        tot=m[D-D0]+Kx*ell*e1*sum((LAM**t*m[t+D] for t in range(-D,-D0)),arb(0))
        v=W*tot
        if best is None or up(v)<up(best): best=v
    return best
def Xfun(S,D):            # >= ||Q L^j_{<D} Phi_mu||  (j-role, cut at D in j coordinates)
    best=None; e2=U(S['e2'])
    for D0,W in S['WL'].items():
        if D0>=D: continue
        sg=ell*e2*LAM**(-D0)/(1-1/LAM); Kx=K0*(K0*sg).exp()
        tot=m[D-D0]+Kx*ell*e2*sum((LAM**(-t)*m[D-1-t] for t in range(D0,D)),arb(0))
        v=W*tot
        if best is None or up(v)<up(best): best=v
    return best
TY=CC.TYPES; EPS=CC.EPS
iseeds={ti:list(CC.Dg.seeds(*TY[ti])) for ti in TY}
jseeds={}
for tj in TY:
    for h in (0,1):
        for sg in (1,-1):
            e=TY[tj] if not h else CC.mulq(TY[tj],EPS); e=(sg*e[0],sg*e[1]); jseeds[(tj,h,sg)]=list(CC.Dg.seeds(*e))
SI={(k,w):single(z) for k,zz in iseeds.items() for w,z in enumerate(zz)}
SJ={(k,w):single(z) for k,zz in jseeds.items() for w,z in enumerate(zz)}
print('singles done', {str(k):(round(v['r'],4),v['jlo'],v['jhi'],up(v['Gam']),up(v['Psimax']),up(v['Phimax'])) for k,v in list(SI.items())[:4]},flush=True)
def pairdev(i,j,G):
    Di=G//2; Dj=G-Di; Dl=[]; yy=[]
    for w in (0,1):
        A=SI[(i,w)]; B=SJ[(j,w)]
        assert Di>=-A['jlo']+1 and Dj>=B['jhi']+1, (G,i,j)
        Y=Yfun(A,Di); X=Xfun(B,Dj)
        sdR=ell*U(B['e2'])*LAM**(-Dj)/(1-1/LAM); sdL=ell*U(A['e1'])*LAM**(-Di-1)/(1-1/LAM)
        assert B['e2']*float(LAM.mid())**(-Dj)<0.45 and A['e1']*float(LAM.mid())**(-Di-1)<0.45
        Gi=A['Gam']; Gj=B['Gam']; assert up(Gi*sdR)<0.5
        dLPhi=Gj*(Gj*sdL).exp()*sdL*B['Phimax']
        ri=U(A['r']); rj=U(B['r'])
        betj=nPsiMu*K0*sdR*(K0*sdR).exp()*B['Phimax']
        alpi=A['Psimax']*K0*sdL*(K0*sdL).exp()*nPhiMu
        bj=rj+betj
        psiv=bj+nPsiMu*dLPhi; Qv=X+nQ*dLPhi
        Vmax=A['Phimax']*psiv+Gi*Qv
        crossR=A['Psimax']/(1-Gi*sdR)*sdR*Vmax
        assert up(Gj*sdL)<0.5
        # crossL = psi_mu R^i (L - L^j) Phi_mu, covector side: psi_mu R^i = a_i psi_mu + psi_mu R^i Q  (||.|| <= |a_i|, Y)
        crossL=((ri+alpi)*B['Psimax']/(1-Gj*sdL)+Y*Gj*(Gj*sdL).exp())*sdL*B['Phimax']
        Dl.append(Y*X+crossR+crossL+alpi*bj+(ri+alpi)*betj+alpi*betj); yy.append(ri*rj)
    dAB=Dl[0]*yy[1]+yy[0]*Dl[1]+Dl[0]*Dl[1]; Y0=yy[0]*yy[1]; xb=Y0+dAB
    return dAB*(xb**2+xb*Y0+Y0**2), Dl
res={}; tot=arb(0)
for G in range(G1,GMAX+1):
    TG=arb(0)
    for i in TY:
        for j in jseeds: TG+=pairdev(i,j,G)[0]
    res[G]=up(TG); tot+=TG
    if G<=G1+5 or G%10==0: print(G,'%.4g'%res[G],'cum %.4g'%up(tot),flush=True)
# ---------- rigorous remainder G > GMAX (REPORT_N21 sec. 4.6)
# m(k) <= Mrho rho^k for all k (ratio monotone: s/mu*kap < rho, 1/(mu rho) < 1, checked above)  =>  Y(D) <= CY rho^D, X(D) <= CX rho^D;
# every cross/norm term carries a factor sd <= ell|e|lambda^{-G/2}/(1-1/lambda) with monotone prefactors, so it is <= its value at the
# GMAX envelope times lambda^{-(G-GMAX)/2}.
lr=1/LAM.sqrt()
def CYf(S):
    best=None; e1=U(S['e1'])
    for D0,W in S['WR'].items():
        sg=ell*e1*LAM**(-D0-1)/(1-1/LAM); Kx=K0*(K0*sg).exp()
        v=W*Mrho*(rho**(-D0)+Kx*ell*e1*(LAM*rho)**(-D0-1)/(1-1/(LAM*rho)))          # Y(D) <= v rho^D
        if best is None or up(v)<up(best): best=v
    return best
def CXf(S):
    best=None; e2=U(S['e2'])
    for D0,W in S['WL'].items():
        sg=ell*e2*LAM**(-D0)/(1-1/LAM); Kx=K0*(K0*sg).exp()
        v=W*Mrho*(rho**(-D0)+Kx*ell*e2*(LAM*rho)**(-D0)/(1-1/(LAM*rho))/rho)        # X(D) <= v rho^D
        if best is None or up(v)<up(best): best=v
    return best
assert up(LAM*rho)>1
REM=arb(0); G0=GMAX
for i in TY:
    for j in jseeds:
        a=[];b=[];yy=[]
        for w in (0,1):
            A=SI[(i,w)]; B=SJ[(j,w)]
            CY=CYf(A); CX=CXf(B)
            Y=CY*rho**(G0//2); X=CX*rho**(G0-G0//2)
            sdR=ell*U(B['e2'])*lr**G0/(1-1/LAM); sdL=ell*U(A['e1'])*lr**G0/(1-1/LAM)
            Gi=A['Gam']; Gj=B['Gam']; assert up(Gi*sdR)<0.5 and up(Gj*sdL)<0.5
            dLPhi=Gj*(Gj*sdL).exp()*sdL*B['Phimax']
            ri=U(A['r']); rj=U(B['r'])
            betj=nPsiMu*K0*sdR*(K0*sdR).exp()*B['Phimax']; alpi=A['Psimax']*K0*sdL*(K0*sdL).exp()*nPhiMu; bj=rj+betj
            psiv=bj+nPsiMu*dLPhi; Qv=X+nQ*dLPhi; Vmax=A['Phimax']*psiv+Gi*Qv
            crossR=A['Psimax']/(1-Gi*sdR)*sdR*Vmax
            crossL=((ri+alpi)*B['Psimax']/(1-Gj*sdL)+Y*Gj*(Gj*sdL).exp())*sdL*B['Phimax']
            cr=crossR+crossL+alpi*bj+(ri+alpi)*betj+alpi*betj      # value at the GMAX envelope; scales <= lr^(G-GMAX)
            a.append(CY*CX); b.append(cr*lr**(-G0)); yy.append(ri*rj)
        # Delta_W(G) <= a_W rho^G + b_W lr^G  for G >= GMAX
        S=[a[w]*rho**(G0+1)/(1-rho)+b[w]*lr**(G0+1)/(1-lr) for w in (0,1)]
        Dmx=[a[w]*rho**(G0+1)+b[w]*lr**(G0+1) for w in (0,1)]
        Y0=yy[0]*yy[1]; dmax=Dmx[0]*yy[1]+yy[0]*Dmx[1]+Dmx[0]*Dmx[1]
        REM+=3*(Y0+dmax)**2*(yy[1]*S[0]+yy[0]*S[1]+Dmx[0]*S[1])
print('remainder G>GMAX <= %.4g'%up(REM),flush=True)
total=tot+REM
ratios=[res[G+1]/res[G] for G in range(max(G1,GMAX-20),GMAX)] or [0.0]
out=dict(G1=G1,GMAX=GMAX,KK=KK,const=CONST,T_by_G=res,sum_G1_GMAX=up(tot),remainder=up(REM),total_G_ge_G1=up(total),
         ratios_tail=[min(ratios),max(ratios)])
print(json.dumps({k:v for k,v in out.items() if k not in ('T_by_G','const')}),flush=True)
json.dump(out,open(f'/workspace/bgs-lineN/N21/logs/tail_DT_{G1}_{GMAX}'+('' if KK==18 else f'_KK{KK}')+os.environ.get('OUTSUF','')+'.json','w'),indent=1)
