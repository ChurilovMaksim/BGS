"""Line I, item 2: rigorous COUNTING certificate for a lifted twisted cyclic operator L (certG_build output):
   'L has exactly k eigenvalues (with multiplicity) in |z| > R'.   With the exact Z/3 symmetry S L S^-1 = omega L (S = phase omega^i on
   cycle component i) and k = 3 this means sigma(L) ∩ {|z|>R} = {mu, omega mu, omega^2 mu}, i.e. spectral radius r(L) = |mu| > R.
Generalises Line H rig_spec.py v4 (sha f346e22c..., same a-priori float bounds gc = sqrt2*gamma_{2n+2}, JSON padding, provenance):
 * k-dimensional Householder deflation H = H_{k-1}...H_0 of an (orthonormalised) float basis of the dominant invariant subspace;
   exact similarity S = H A H^-1 = Bt + E H^-1 with E = H A - Bt H bounded a posteriori; kappa <= prod ||H_j|| ||H_j^-1||.
 * T0 = [[Lam (k x k), b12],[0, Y]];  b21 and E H^-1 moved into the perturbation (pertT = pert + kappa(epsH + ||b21||)).
 * ||R_T0(z)|| <= ||R_Lam(z)|| (1 + ||b12 R_Y(z)||) + ||R_Y(z)||;  R_Y, b12 R_Y by Neumann series with explicit powers (as rig_spec);
   sup_{|z|=R} ||R_Lam(z)|| by an arb grid + resolvent Lipschitz bound;  eigenvalues of Lam isolated in arb (acb_poly roots) and
   checked to lie in |z| > R; Neumann validity gives sigma(Y) in |z| < R.
 * comparison op T0' as in Line H; homotopy: pertT * fullR < 1 on |z| = R  =>  #eig(L) in |z|>R  =  #eig(T0) in |z|>R = k.
v2 (rig_dom3b): ||R_Lam b12 R_Y|| evaluated POINTWISE on a fine grid (vector Neumann sum M(z)=sum_j (b12 Y^j) z^-j-1 kept as
   float rows with rigorous error), whole-T0 resolvent bound g(z0) and covering by the resolvent identity
   ||R(z)|| <= g/(1-|z-z0| g).  Grid points are the float numbers z_f themselves; all radii use Rm = R(1-1e-13).
v3 (DF4, referee delta review): gmax is the max of the exact upper ends g.upper() (an arb comparison g>gmax is
   False on overlapping balls and could skip a ball with a larger upper end).
Usage: rig_dom3b.py prefix sector k Rlist p out.json"""
import sys, json, time, math, hashlib, os, numpy as np, scipy.linalg as sl, scipy.sparse.linalg as ssl
from flint import arb, acb, acb_poly, ctx
ctx.prec=128
pre=sys.argv[1]; b=int(sys.argv[2]); k=int(sys.argv[3]); Rlist=sys.argv[4]; p=int(sys.argv[5]); outf=sys.argv[6]
t0=time.time(); info=json.load(open(pre+'.json'))
def sha(f):
    h=hashlib.sha256()
    with open(f,'rb') as fh:
        for chunk in iter(lambda: fh.read(1<<24), b''): h.update(chunk)
    return h.hexdigest()
PAD=1+arb(2)**-40
def Fp(x): return arb(float(x))*PAD
def fu(x): return math.nextafter(float(x.upper()),math.inf)
def fl(x): return math.nextafter(float(x.lower()),-math.inf)
prov=dict(code=os.path.abspath(__file__),code_sha256=sha(__file__),argv=sys.argv,build_json_sha256=sha(pre+'.json'),
    mid_sha256=sha(pre+f'_b{b}_mid.npy'),rad_sha256=sha(pre+f'_b{b}_rad.npy'),started=time.strftime('%Y-%m-%d %H:%M:%S %z'))
U=2.0**-53; INF=1+1e-7
def F(x): return arb(float(x))
def up(x): return F(x)*arb(INF)
def fro(M): return up(np.sqrt(np.vdot(M,M).real))
A=np.load(pre+f'_b{b}_mid.npy'); Arad=np.load(pre+f'_b{b}_rad.npy'); D=A.shape[0]
assert np.isfinite(A).all() and np.isfinite(Arad).all()
epsA=up(np.sqrt((Arad**2).sum())); del Arad
gc=arb(2).sqrt()*arb(2*D+2)*arb(U)/(1-arb(2*D+2)*arb(U))
res=dict(version='rig_dom3b v3 (DF4 gmax fix)',provenance=prov,prefix=pre,sector=b,k=k,Rlist=Rlist,p=p,D=D,epsA=fu(epsA))
print('D',D,'epsA',fu(epsA),flush=True)
normA=fro(A)
# ---- float dominant invariant subspace
ev,vv=ssl.eigs(A,k=max(2*k,8),which='LM',tol=1e-12,maxiter=20000)
o=np.argsort(-abs(ev)); ev=ev[o]; vv=vv[:,o]
print('eigs',[complex(round(z.real,8),round(z.imag,8)) for z in ev],flush=True)
res['eigs_float']=[str(z) for z in ev]
Qb,_=np.linalg.qr(vv[:,:k])
# ---- Householder reflectors (float w, tau real): H_j = I - tau_j w_j w_j^H  maps span(Qb) to span(e_0..e_{k-1})
ws=[]; taus=[]; X=Qb.copy()
for j in range(k):
    x=X[j:,j].copy(); al=-np.exp(1j*np.angle(x[0]))*np.linalg.norm(x)
    w=np.zeros(D,complex); w[j:]=x; w[j]-=al
    nw=float(np.vdot(w,w).real); tau=2.0/nw
    X=X-tau*np.outer(w,w.conj()@X)
    ws.append(w); taus.append(tau)
kap=arb(1); Hn_l=[]; Hin_l=[]
for w,tau in zip(ws,taus):
    n_=sum((F(t.real)**2+F(t.imag)**2 for t in w[np.nonzero(w)[0]]),arb(0)); ta=F(tau)
    dev=abs(ta*n_-2); assert dev<1
    Hn=arb.max(arb(1),abs(1-ta*n_)); Hin=arb.max(arb(1),1/(1-dev))
    Hn_l.append(Hn); Hin_l.append(Hin); kap*=Hn*Hin
HinvN=arb(1)
for v in Hin_l: HinvN*=v
HN=arb(1)
for v in Hn_l: HN*=v
def left(Xm,err,j):
    """fl(H_j Xm) with error propagation (Frobenius): returns (Xnew, errnew)"""
    w=ws[j]; tau=taus[j]; g=w.conj()@Xm; Y_=Xm-tau*np.outer(w,g)
    nX=fro(Xm); nw=up(np.linalg.norm(w)); ng=fro(g); ta=F(tau)
    loc=ta*nw*(gc*nw*nX)+4*arb(U)*(ta*nw*ng+nX+fro(Y_))
    return Y_, Hn_l[j]*err+loc
def right(Xm,err,j,inv=False):
    """fl(Xm H_j) (or with H_j^-1 approx, inv=True: no error tracking needed)"""
    w=ws[j]; tau=taus[j]
    if inv:
        nw=float(np.vdot(w,w).real); tau=tau/(tau*nw-1)
    g=Xm@w; Y_=Xm-tau*np.outer(g,w.conj())
    if inv: return Y_, None
    nX=fro(Xm); nw=up(np.linalg.norm(w)); ng=fro(g); ta=F(tau)
    loc=ta*nw*(gc*nw*nX)+4*arb(U)*(ta*nw*ng+nX+fro(Y_))
    return Y_, Hn_l[j]*err+loc
HA=A; eHA=arb(0)
for j in range(k): HA,eHA=left(HA,eHA,j)          # H = H_{k-1}...H_0 applied on the left
del A
Bt=HA.copy()
for j in range(k): Bt,_=right(Bt,None,j,inv=True)  # Bt ~ H A H^-1 (any float matrix is fine; exactness via residual)
BH=Bt.copy(); eBH=arb(0)
for j in reversed(range(k)): BH,eBH=right(BH,eBH,j)  # Bt H = Bt H_{k-1}...H_0 : apply H_{k-1} first on the right
Efl=HA-BH; del HA,BH
epsE=fro(Efl)*(1+2*arb(U))+eHA+eBH; del Efl
epsH=epsE*HinvN
Lam=Bt[:k,:k].copy(); b12=Bt[:k,k:].copy(); b21n=fro(Bt[k:,:k]); Y=np.ascontiguousarray(Bt[k:,k:]); del Bt
res.update(kappa=fu(kap),epsH=fu(epsH),b21=fu(b21n),b12=fu(fro(b12)),Lam=[[str(Lam[i,j]) for j in range(k)] for i in range(k)])
print('kappa',fu(kap),'epsH',fu(epsH),'|b21|',fu(b21n),'|b12|',fu(fro(b12)),round(time.time()-t0),'s',flush=True)
# ---- Lam in arb: eigenvalues (rigorous root isolation of char poly), resolvent grid
LamA=[[acb(F(Lam[i,j].real),F(Lam[i,j].imag)) for j in range(k)] for i in range(k)]
from flint import acb_mat
LM=acb_mat(LamA)
cp=LM.charpoly(); roots=cp.roots()
res['Lam_eig_abs']=[abs(r).str(15,radius=True) for r in roots]
print('Lam eig |.|',res['Lam_eig_abs'],flush=True)
# ---- powers of Y with error tracking (as rig_spec v4)
normY=fro(Y)
N=[arb(1)]; Es=[None,None]; rows=[]; Er=[None]
r=b12.copy(); rows.append(fro(r)); WL=[r.copy()]; EB=[arb(0)]
M=Y.copy(); N.append(normY)
for j in range(2,p+1):
    Er.append(gc*fro(r)*normY); r=r@Y
    ebr=sum((Er[i]*N[j-1-i] for i in range(1,j)),arb(0)); rows.append(fro(r)+ebr); EB.append(ebr)
    if len(WL)<p: WL.append(r.copy())
    Es.append(gc*fro(M)*normY); M=M@Y; fM=fro(M)
    e=sum((Es[i]*N[j-i] for i in range(2,j+1)),arb(0))
    n1=up(abs(M).sum(0).max()); ninf=up(abs(M).sum(1).max())
    N.append(arb.min(fM,(n1*ninf).sqrt()*arb(1+1e-12))+e)
    if j%4==0 or j==p: print('j',j,'||Y^j|| <=',float(N[-1].upper()),round(time.time()-t0),'s',flush=True)
Er.append(gc*fro(r)*normY); rn=r@Y
ebr=sum((Er[i]*N[p-i] for i in range(1,p+1)),arb(0)); rows.append(fro(rn)+ebr)
G=M.conj().T@M; s2=(fro(G)+gc*fro(M)**2).sqrt()+e; del G
N[p]=arb.min(N[p],s2)
res['N']=[fu(x) for x in N]; res['rows']=[fu(x) for x in rows]
def neum(zeta):
    t=N[p]/zeta**p
    if not t<1: return None,None
    SY=sum((N[j]/zeta**(j+1) for j in range(p)),arb(0))/(1-t)
    Sb=sum((rows[j]/zeta**(j+1) for j in range(p)),arb(0))/(1-t)
    return SY,Sb
Xn=Fp(info['Xnorm']); pert=Fp(info['delta1'])+Fp(info['delta2'])+Fp(info['Delta'])+epsA
pertT=pert+kap*(epsH+b21n)
def fullR(Rc,za): return (kap*Rc+1/za)*(1+Xn/za)+1/za
def RLam_sup(R,Ngrid):
    pi=arb.pi(); h=R*pi/Ngrid; best=arb(0)
    I=acb_mat([[acb(1) if i==j else acb(0) for j in range(k)] for i in range(k)])
    for q in range(Ngrid):
        th=2*pi*q/Ngrid; z=acb(R*th.cos(),R*th.sin())
        Rz=(I*z-LM).inv()
        Mq=sum((abs(Rz[i,j])**2 for i in range(k) for j in range(k)),arb(0)).sqrt()
        den=1-h*Mq
        if not den>0: return None
        v=Mq/den
        best=arb.max(best,v)
    return best

Wst=np.stack(WL)            # p x k x Dy : float rows w_j ~ b12 Y^j (j<p), true = w_j + err, ||err||<=EB[j]
assert Wst.shape[0]==p
wn=[fro(Wst[j]) for j in range(p)]
gcp=arb(2).sqrt()*arb(2*p+2)*arb(U)/(1-arb(2*p+2)*arb(U))
Dy=Wst.shape[2]; gcD=arb(2).sqrt()*arb(2*Dy+2)*arb(U)/(1-arb(2*Dy+2)*arb(U))
Wmat=Wst.reshape(p,-1)
def gridsup(R,Ng):
    Rm=R*(1-arb(10)**-13)
    SY,_=neum(Rm)
    if SY is None: return None,'neumann'
    tail=rows[p]/Rm**p*SY
    err0=sum(((EB[j]+8*(j+2)*arb(U)*wn[j]+gcp*wn[j])/Rm**(j+1) for j in range(p)),arb(0))+tail
    Rf=float(R.mid()); th=2*np.pi*np.arange(Ng)/Ng; zs=Rf*np.exp(1j*th)
    # covering radius: every |z|=R within hcov of some grid z_f
    hcov=R*arb.pi()/Ng*(1+arb(10)**-6)+arb(10)**-12
    I=acb_mat([[acb(1) if i==j else acb(0) for j in range(k)] for i in range(k)])
    gmax=arb(0); worst=None
    for c0 in range(0,Ng,256):
        zc=zs[c0:c0+256]; C=np.empty((len(zc),p),complex); iz=1/zc; cur=iz.copy()
        for j in range(p): C[:,j]=cur; cur=cur*iz
        Mf=(C@Wmat).reshape(len(zc),k,Dy)
        Gf=np.einsum('qid,qjd->qij',Mf,Mf.conj()); mfn=np.sqrt(np.einsum('qid,qid->q',Mf,Mf.conj()).real)
        for q in range(len(zc)):
            z=acb(F(zc[q].real),F(zc[q].imag))
            Rz=(I*z-LM).inv()
            RLn=sum((abs(Rz[i,j])**2 for i in range(k) for j in range(k)),arb(0)).sqrt()
            Gq=acb_mat([[acb(F(Gf[q,i,j].real),F(Gf[q,i,j].imag)) for j in range(k)] for i in range(k)])
            P=Rz*Gq*Rz.transpose().conjugate()
            PF=sum((abs(P[i,j])**2 for i in range(k) for j in range(k)),arb(0)).sqrt()
            errG=gcD*up(mfn[q])**2*(1+arb(10)**-10)+4*arb(U)*up(mfn[q])**2
            KM=(PF+RLn**2*errG).sqrt()+RLn*err0
            g=RLn+KM+SY
            gu=arb(g.upper())   # v3 (DF4): compare exact upper ends, so no ball with a larger upper end is skipped
            if gu>gmax: gmax=gu; worst=float(th[c0+q])
    den=1-hcov*gmax
    if not den>0: return None,'grid too coarse (h g=%.3g)'%float((hcov*gmax).upper())
    return gmax/den,dict(Ng=Ng,gmax=fu(gmax),worst_theta=worst,hg=fu(hcov*gmax),SY=fu(SY),err0=fu(err0))
scan=[]; best=None
for Rs in Rlist.split(','):
    R=arb(Rs); out=dict(R=Rs,certified=False)
    outside=all(abs(rt)>R for rt in roots)
    if not outside: out['why']='Lam eig inside'; scan.append(out); print(json.dumps(out),flush=True); continue
    Rc=None
    for Ng in (4096,16384,65536):
        Rc,inf=gridsup(R,Ng)
        print(' grid',Rs,Ng,inf if Rc is None else inf,round(time.time()-t0),'s',flush=True)
        if Rc is not None or inf=='neumann': break
    if Rc is None: out['why']=inf; scan.append(out); print(json.dumps(out),flush=True); continue
    FR=pertT*fullR(Rc,R)
    out.update(grid=inf,Rcore=fu(Rc),pertT=fu(pertT),F=fu(FR),F_str=FR.str(10,radius=True),certified=bool(FR<1),count=k,radius_lower=fl(R))
    print(json.dumps(out),flush=True); scan.append(out)
    if out['certified'] and (best is None or float(Rs)>float(best['R'])): best=out
res['scan']=scan; res['best']=best; res['secs']=round(time.time()-t0)
json.dump(res,open(outf,'w'),indent=1); print('BEST',json.dumps(best),flush=True)
