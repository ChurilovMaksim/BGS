# referee lineN21: independent re-implementation of Lemma Q + Lemma D^T (REPORT_N21 sec.4) in arb.
# Window chain arrays (phi_k, beta_k, GL, scale, eta, sig) come from the author's Lemma C chain (CA-fp; reproduced bit-identically elsewhere);
# all constants of Lemma Q are recomputed here from the raw certified inputs (N8 json, N13 b_arb, conv_c float residual constants).
# Differences vs author: Psi^max uses max_k cov(beta_k) (author: cov(max b)); option FIX toggles this.
import sys, json, math
sys.path.insert(0,'/workspace/bgs-lineN/N21/code')
import conv_c as CC, mpmath as mp
from flint import arb, ctx
ctx.prec=100
KK=int(sys.argv[1]); GS=[int(x) for x in sys.argv[2].split(',')]; FIX=int(sys.argv[3]) if len(sys.argv)>3 else 1
def up(x): return float(x.upper())
def U(x): return arb(x)*(1+arb(2)**-45)
N8=json.load(open('/workspace/bgs-lineN/N8/logs/n8_cert_fam.json')); B13=json.load(open('/workspace/bgs-lineN/N13/logs/b_arb.json'))
s=CC.s; abs_s=arb(s.real)**2+arb(s.imag)**2; abs_s=abs_s.sqrt()      # exact from the float s
mus=U(N8['mu_minus_s']); mu_lo=abs_s-mus
cond=U(B13['V1']['c_hi'])/(arb(B13['V1']['c_lo'])*(1-arb(2)**-45)); eta=arb(B13['V2']['eta']); kap0=arb(B13['V3b']['kap'])
Pert=U(N8['Pert']); Xn=U(N8['Xn']); N1=U(N8['N1']); normPi=U(N8['normPi']); dPi=U(N8['dPi'])
ER=U(CC.ER); EL=U(CC.EL); n2=U(CC.nPhi2); p2=U(CC.npsi2)
den1=arb(CC.den1)*(1-arb(2)**-45)
xs=Xn/abs_s
nPsiT=p2+EL; nPhiT=(1+xs**2).sqrt()*(n2+ER); tau=dPi*nPsiT*nPhiT
c_dev=U(abs(CC.psiPhi-1)+CC.eps_p)+p2*ER
nPiA=(n2+ER)*(p2+EL)/den1; nQA=1+nPiA
dQ=(ER*(p2+EL)+n2*EL+n2*p2*c_dev)/den1
kap=kap0*(1+eta)+(1+eta)*cond*dQ
assert up(abs_s*kap)<1
RAz=nPiA/(abs_s-1)+nQA+cond*abs_s*kap/(1-abs_s*kap)
ST=(RAz**2+(Xn*RAz+1)**2).sqrt(); assert up(Pert*ST)<1
Rem=ST**2*Pert/(1-Pert*ST)
sr=abs_s/mu_lo
def m(k):
    if k==0: return 1+normPi
    mT=cond*kap+xs*nQA if k==1 else cond*(kap**k+xs*kap**(k-1))
    return sr**k*mT+Rem/mu_lo**k
mm=[m(k) for k in range(0,400)]
K0=normPi+max(mm[1:],key=up)
rho=arb('0.5225'); assert up(1/mu_lo)<0.5225 and up(sr*kap)<0.5225
LAM=3+2*arb(2).sqrt(); assert up(1/(LAM*rho))<1
Mrho=max([mm[0],mm[1]/rho,mm[2]/rho**2],key=up)
ell=2*arb.pi()*N1/mu_lo
nPsiMu=nPsiT*(1+dPi)/(den1-tau); nPhiMu=nPhiT*(1+dPi); Fs=Pert/abs_s
const=dict(kap=up(kap),dQ=up(dQ),RAz=up(RAz),ST=up(ST),Rem=up(Rem),K0=up(K0),m1=up(mm[1]),m2=up(mm[2]),m3=up(mm[3]),Mrho=up(Mrho),ell=up(ell),tau=up(tau),nPsiMu=up(nPsiMu),nPhiMu=up(nPhiMu))
print(json.dumps(const),flush=True)
def e12(z): return abs(z[0]+z[1]*CC.Dg.S2), abs(z[0]-z[1]*CC.Dg.S2)
def single(z):
    ds=CC.Dg.core(z,KK); e1,e2=e12(z)
    L1=max(0,int(mp.ceil(mp.log(e1+1)/mp.log(CC.Dg.LAM)))); L2=max(0,int(mp.ceil(mp.log(e2+1)/mp.log(CC.Dg.LAM))))
    jlo=-(KK+L1); kp={}
    r,E,_=CC.chain(ds,CC.tails(z,KK),keep=kp); n=kp['n']
    GL=U(kp['GL']); sc=U(kp['scale']); et=U(kp['eta']); sig=U(kp['sig']); phi=[U(x) for x in kp['phi']]; beta=[U(x) for x in kp['beta']]
    cs=[arb(0)]
    for k in range(1,n+2): cs.append(cs[-1]+phi[k])
    cov=lambda b:(1+sc)*((b+nPsiT*dPi*GL)/(den1-tau)+nPsiMu*et*GL)
    vec=lambda k:(1+sc)*(phi[k+1]+Fs*GL*cs[k]+GL*dPi*nPhiT+GL*nPhiMu*et)
    Kx=K0*(K0*sig).exp()
    covs=[cov(b) for b in beta]
    bA=max([U(x)+EL*U(kp['GA']) for x in kp['B']],key=up); cov_author=cov(bA)
    inner=max(covs,key=up) if FIX else cov_author
    Psimax=max([Kx*covs[0],inner,nPsiMu*(1+K0*sig*(K0*sig).exp())],key=up)
    Phimax=Kx*max([vec(k) for k in range(n+1)],key=up)
    Gam=K0*Kx*GL*(1+sc)
    WR={};WL={}
    for D0 in range(1,KK):
        if e1*float(LAM.mid())**(-D0-1)<0.45 and -D0-jlo>=0: WR[D0]=covs[-D0-jlo]
        if e2*float(LAM.mid())**(-D0)<0.45 and D0-jlo<=n: WL[D0]=vec(D0-jlo)
    return dict(r=U(abs(r)+E),e1=U(e1),e2=U(e2),jlo=jlo,jhi=jlo+n-1,Psimax=Psimax,Phimax=Phimax,Gam=Gam,WR=WR,WL=WL,
                diag=dict(cov_bmax_author=up(cov_author),max_cov_beta=up(max(covs,key=up)),Kx_cov0=up(Kx*covs[0])))
def Y(S,D):
    best=None
    for D0,W in S['WR'].items():
        if D0>=D: continue
        sg=ell*S['e1']*LAM**(-D0-1)/(1-1/LAM); Kx=K0*(K0*sg).exp()
        v=W*(mm[D-D0]+Kx*ell*S['e1']*sum((LAM**t*mm[t+D] for t in range(-D,-D0)),arb(0)))
        best=v if best is None or up(v)<up(best) else best
    return best
def X(S,D):
    best=None
    for D0,W in S['WL'].items():
        if D0>=D: continue
        sg=ell*S['e2']*LAM**(-D0)/(1-1/LAM); Kx=K0*(K0*sg).exp()
        v=W*(mm[D-D0]+Kx*ell*S['e2']*sum((LAM**(-t)*mm[D-1-t] for t in range(D0,D)),arb(0)))
        best=v if best is None or up(v)<up(best) else best
    return best
TY=CC.TYPES
iseeds={ti:CC.Dg.seeds(*TY[ti]) for ti in TY}
jseeds={}
for tj in TY:
    for h in (0,1):
        for sg in (1,-1):
            e=TY[tj] if not h else CC.mulq(TY[tj],CC.EPS); jseeds[(tj,h,sg)]=CC.Dg.seeds(sg*e[0],sg*e[1])
SI={(k,w):single(z) for k,zz in iseeds.items() for w,z in enumerate(zz)}
SJ={(k,w):single(z) for k,zz in jseeds.items() for w,z in enumerate(zz)}
def Delta(A,B,G):
    Di=G//2; Dj=G-Di
    assert Di>=-A['jlo']+1 and Dj>=B['jhi']+1
    sdR=ell*B['e2']*LAM**(-Dj)/(1-1/LAM)      # sum_{t'>=Dj} |d^j_t'| * ell
    sdL=ell*A['e1']*LAM**(-Di-1)/(1-1/LAM)    # sum_{t<=-Di-1} |d^i_t| * ell
    assert up(A['Gam']*sdR)<1 and up(B['Gam']*sdL)<1
    main=Y(A,Di)*X(B,Dj)
    al=A['Psimax']*K0*sdL*(K0*sdL).exp()*nPhiMu            # |alpha_i|
    be=nPsiMu*K0*sdR*(K0*sdR).exp()*B['Phimax']             # |beta_j|
    ai=A['r']+al; bj=B['r']+be                              # |a_i|, |b_j|
    dL=B['Gam']*(B['Gam']*sdL).exp()*sdL*B['Phimax']       # ||(L-L^j)Phi_mu||
    V0=A['Phimax']*(bj+nPsiMu*dL)+A['Gam']*(X(B,Dj)+(1+normPi)*dL)
    cR=A['Psimax']*sdR*V0/(1-A['Gam']*sdR)
    cL=(ai*B['Psimax']/(1-B['Gam']*sdL)+Y(A,Di)*B['Gam']*(B['Gam']*sdL).exp())*sdL*B['Phimax']
    return main+cR+cL+al*bj+ai*be+al*be, A['r']*B['r']
res={}
for G in GS:
    T=arb(0)
    for i in TY:
        for j in jseeds:
            dA,yA=Delta(SI[(i,0)],SJ[(j,0)],G); dB,yB=Delta(SI[(i,1)],SJ[(j,1)],G)
            dxy=dA*yB+yA*dB+dA*dB; y=yA*yB; x=y+dxy
            T+=dxy*(x**2+x*y+y**2)
    res[G]=up(T); print('G',G,'T %.6g'%res[G],flush=True)
diag={str(k):v['diag'] for k,v in list(SI.items())+list(SJ.items())}
json.dump(dict(KK=KK,FIX=FIX,const=const,T=res,diag=diag),open(f'../logs/ref_DT_KK{KK}_fix{FIX}.json','w'),indent=1)
