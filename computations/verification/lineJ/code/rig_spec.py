"""Line H, H2: rigorous spectral certificate for one lifted 49-state operator from cert49_build output.
v4 (2026-10-30, referee fixes 2/3): Float BLAS linear algebra with RIGOROUS a-priori rounding bounds |fl(AB)-AB| <= gc |A||B| entrywise,
gc = sqrt(2)*gamma_{2n+2}, gamma_k = ku/(1-ku): valid for complex dot products of length n in IEEE binary64 round-to-nearest for ANY
summation order / FMA, including kernels that accumulate all 2n real products in one accumulator (OpenBLAS SkylakeX m2/m1 edge paths);
assumption: BLAS zgemm uses only classical dot products (true for OpenBLAS; no Strassen). Frobenius norms inflated by (1+1e-7)).
All scalar bound arithmetic in arb.
mode 'dom': Householder deflation of the leading eigenvector, T0=[[b11,b12],[0,Y]]; contours |z-b11|=r1 and |z|=R.
mode 'rest': T0 = A_mid; contour |z|=R.
Neumann: ||R_Y(z)|| <= sum_{j<p} N_j z^-(j+1) / (1 - N_p R^-p)  for |z|>=zeta,  N_j >= ||Y^j||_2 (explicit powers).
Usage: rig_spec.py prefix sector mode R r1 p out.json"""
import sys, json, time, math, hashlib, os, numpy as np, scipy.linalg as sl, scipy.sparse.linalg as ssl
from flint import arb, acb, ctx
ctx.prec=128
pre=sys.argv[1]; b=int(sys.argv[2]); mode=sys.argv[3];  p=int(sys.argv[6]); outf=sys.argv[7]
t0=time.time(); info=json.load(open(pre+'.json'))
def sha(f):
    h=hashlib.sha256()
    with open(f,'rb') as fh:
        for chunk in iter(lambda: fh.read(1<<24), b''): h.update(chunk)
    return h.hexdigest()
PAD=1+arb(2)**-40
def Fp(x): return arb(float(x))*PAD          # JSON floats are display values (float(arb.upper()) may be 1 ulp low): pad upward
def fu(x): return math.nextafter(float(x.upper()),math.inf)    # stored upper bounds: rounded up
def fl(x): return math.nextafter(float(x.lower()),-math.inf)   # stored lower bounds: rounded down
provenance=dict(code=os.path.abspath(__file__),code_sha256=sha(__file__),argv=sys.argv,build_json_sha256=sha(pre+'.json'),
    mid_sha256=sha(pre+f'_b{b}_mid.npy'),rad_sha256=sha(pre+f'_b{b}_rad.npy'),started=time.strftime('%Y-%m-%d %H:%M:%S %z'))
U=2.0**-53; INF=1+1e-7
def F(x): return arb(float(x))   # exact conversion of a double
def up(x): return F(x)*arb(INF)  # inflate a float-computed nonneg quantity
def fro(M): return up(np.sqrt(np.vdot(M,M).real)) if M.ndim>1 else up(np.linalg.norm(M))
A=np.load(pre+f'_b{b}_mid.npy'); Arad=np.load(pre+f'_b{b}_rad.npy'); D=A.shape[0]
assert np.isfinite(A).all() and np.isfinite(Arad).all()
epsA=up(np.sqrt((Arad**2).sum())); del Arad
gc=arb(2).sqrt()*arb(2*D+2)*arb(U)/(1-arb(2*D+2)*arb(U))   # sqrt2*gamma_{2D+2} (D >= every dot-product length used)
res=dict(version='rig_spec v4',provenance=provenance,note='floats: *_upper rounded up, *_lower rounded down; other floats display only; decisions made in arb',prefix=pre,sector=b,mode=mode,Rlist=sys.argv[4],r1list=sys.argv[5],p=p,D=D,epsA=fu(epsA))
print('D',D,'epsA',fu(epsA),flush=True)
normA=fro(A); kap=arb(1); epsH=arb(0); b21n=arb(0)
if mode=='dom':
    # leading eigenvector: ARPACK + inverse-iteration polish (float; only used to choose the similarity)
    ev,vv=ssl.eigs(A,k=6,which='LM',tol=1e-12,maxiter=5000); i0=np.argmax(abs(ev)); mu=ev[i0]; v=vv[:,i0]; print('eigs',sorted(ev,key=lambda z:-abs(z)),flush=True)
    lu=sl.lu_factor(A-mu*np.eye(D))
    for _ in range(3):
        v=sl.lu_solve(lu,v); v/=np.linalg.norm(v)
    del lu
    k0=int(np.argmax(abs(v)))   # pivot (permute k0 <-> 0 via exact permutation similarity)
    perm=np.arange(D); perm[0],perm[k0]=k0,0
    A=A[np.ix_(perm,perm)]; v=v[perm]
    al=-v[0]/abs(v[0]); w=v.copy(); w[0]-=al
    nw=float(np.vdot(w,w).real); tau=2.0/nw
    # H_f = I - tau w w^H (exact, Hermitian); H_f^{-1} = I - tau' w w^H, tau' = tau/(tau*n-1), n = ||w||^2 exact
    n_=sum((F(t.real)**2+F(t.imag)**2 for t in w),arb(0)); taua=F(tau)
    dev=abs(taua*n_-2)        # H_f^2 = I + tau(tau n - 2) w w^H
    Hn=1+taua*n_              # ||H_f|| <= 1 + tau n ; tighter: H_f has eigenvalues 1 and 1 - tau n
    Hn=arb.max(arb(1),abs(1-taua*n_)); Hin=1/(1-dev)  # ||H_f^{-1}|| <= 1/(1-|tau n -2|) (eigenvalue 1-tau n ~ -1)
    kap=Hn*Hin
    u1=A@w; u2=w.conj()@A; beta=np.vdot(w,u1)
    B=A-tau*np.outer(w,u2)-tau*np.outer(u1,w.conj())+(tau*tau*beta)*np.outer(w,w.conj())
    # v4: a-posteriori residual for the similarity (adopted from the referee's ref_rig.py, /workspace/audit/lineH/code/ref_rig.py):
    # exact S = H A H^{-1}; residual E = H A - B H (exact) => S = B + E H^{-1}, ||S - B|| <= ||E|| ||H^{-1}||.
    HA=A-tau*np.outer(w,u2); Bw=B@w; BH=B-tau*np.outer(Bw,w.conj()); Efl=HA-BH; del HA,BH
    nA=normA; nB=fro(B); nwF=up(math.sqrt(nw)); u2F=fro(u2); BwF=fro(Bw)
    # float error of Efl: matvecs u2=w^H A, Bw: <= gc||A||_F||w||, gc||B||_F||w||, each times tau||w||; entrywise products/subtractions
    # (<= 3 complex roundings per product, 2 subtractions): <= 8u (||A||+tau||w|| ||u2|| + ||B|| + tau ||Bw|| ||w||)
    errE=taua*nwF*(gc*nA*nwF)+taua*nwF*(gc*nB*nwF)+8*arb(U)*(nA+taua*nwF*u2F+nB+taua*BwF*nwF)
    epsH=(fro(Efl)+errE)*Hin; del Efl,A
    b11=complex(B[0,0]); b12=B[0,1:].copy(); b21n=fro(B[1:,0]); Y=np.ascontiguousarray(B[1:,1:]); del B
    b11a=acb(F(b11.real),F(b11.imag))
    res.update(mu_float=str(mu),b11=str(b11),b12=fu(fro(b12)),b21=fu(b21n),epsH=fu(epsH),kappa=fu(kap))
    print('mu',mu,'b11',b11,'|b12|',res['b12'],'|b21|',res['b21'],'epsH',res['epsH'],round(time.time()-t0),'s',flush=True)
else:
    Y=A; del A
normY=fro(Y)
# explicit powers with norm-wise error tracking
# computed M_j = fl(M_{j-1} Y) = M_{j-1}Y + E_j, ||E_j||_2 <= ||E_j||_F <= gc ||M_{j-1}||_F ||Y||_F (entrywise Higham).
# Hence M_j - Y^j = sum_{i=2..j} E_i Y^{j-i}  =>  e_j <= sum_i ||E_i|| N_{j-i}  (N_k rigorous upper bounds, k<j).
# Same for row vectors r_j = fl(r_{j-1} Y).
N=[arb(1)]; Es=[None,None]; rows=[]; Er=[None]
if mode=='dom':
    r=b12.copy(); rows.append(fro(r))
M=Y.copy(); N.append(normY)
for j in range(2,p+1):
    if mode=='dom':
        Er.append(gc*fro(r)*normY); r=r@Y
        ebr=sum((Er[i]*N[j-1-i] for i in range(1,j)),arb(0))   # r_{j-1}: errors E_1..E_{j-1} (r_i ~ b12 Y^i)
        rows.append(fro(r)+ebr)
    Es.append(gc*fro(M)*normY)
    M=M@Y; fM=fro(M)
    e=sum((Es[i]*N[j-i] for i in range(2,j+1)),arb(0))
    n1=up(abs(M).sum(0).max()); ninf=up(abs(M).sum(1).max())
    N.append(arb.min(fM,(n1*ninf).sqrt()*arb(1+1e-12))+e)
    if j%4==0 or j==p: print('j',j,'||Y^j|| <=',float(N[-1].upper()),'err',fu(e),round(time.time()-t0),'s',flush=True)
if mode=='dom':
    Er.append(gc*fro(r)*normY); rn=r@Y
    ebr=sum((Er[i]*N[p-i] for i in range(1,p+1)),arb(0)); rows.append(fro(rn)+ebr)   # rows[j] >= ||b12 Y^j||, j=0..p
# sharp 2-norm for Y^p: ||M||_2^2 <= ||M^H M||_F + gc||M||_F^2
G=M.conj().T@M; s2=(fro(G)+gc*fro(M)**2).sqrt()+e; del G
N[p]=arb.min(N[p],s2)
res['N']=[fu(x) for x in N]
if mode=='dom': res['rows']=[fu(x) for x in rows]
def neum(zeta):
    t=N[p]/zeta**p
    if not t<1: return None,None
    SY=sum((N[j]/zeta**(j+1) for j in range(p)),arb(0))/(1-t)
    Sb=sum((rows[j]/zeta**(j+1) for j in range(p)),arb(0))/(1-t) if mode=='dom' else None
    return SY,Sb
Xn=Fp(info['Xnorm']); pert=Fp(info['delta1'])+Fp(info['delta2'])+Fp(info['Delta'])+epsA
def fullR(Rc,za): return (kap*Rc+1/za)*(1+Xn/za)+1/za
# np.save powers' bounds so contour radii can be re-optimised offline (all quantities rigorous upper bounds)
res['N_str']=[x.str(20,radius=True) for x in N]
if mode=='dom': res['rows_str']=[x.str(20,radius=True) for x in rows]; res['b11_re']=b11.real; res['b11_im']=b11.imag
res.update(kappa_str=kap.str(20,radius=True),epsH_str=epsH.str(20,radius=True),b21_str=b21n.str(20,radius=True),pert0=fu(pert))
best=None; scan=[]
for Rs in sys.argv[4].split(','):
  R=arb(Rs)
  for r1s in sys.argv[5].split(','):
    r1=arb(r1s); out=dict(R=Rs,r1=r1s,certified=False)
    if mode=='dom':
        ab=abs(b11a); zeta1=ab-r1
        pertT=pert+kap*(epsH+b21n)
        SY2,Sb2=neum(R); SY1,Sb1=neum(zeta1) if zeta1>R else (None,None)
        if SY2 is not None and SY1 is not None:
            Rc1=1/r1+Sb1/r1+SY1
            Rc2=1/(ab-R)+Sb2/(ab-R)+SY2
            FR1=pertT*fullR(Rc1,zeta1); FR2=pertT*fullR(Rc2,R)
            out.update(SY_R=fu(SY2),Sb_R=fu(Sb2),Rcore_R=fu(Rc2),Rcore_r1=fu(Rc1),pert=fu(pertT),
                   F_R1=fu(FR1),F_R2=fu(FR2),mu_abs_lower=fl(ab-r1),mu_abs_upper=fu(ab+r1),
                   certified=bool(FR1<1 and FR2<1),F_R1_str=FR1.str(10,radius=True),F_R2_str=FR2.str(10,radius=True),b11_abs_str=ab.str(25,radius=True))
            score=max(out['F_R1'],out['F_R2'])
        else: score=1e300
    else:
        r1=None; SY2,_=neum(R); score=1e300
        if SY2 is not None:
            FR2=pert*fullR(SY2,R); out.update(SY_R=fu(SY2),pert=fu(pert),F_R2=fu(FR2),certified=bool(FR2<1),F_R2_str=FR2.str(10,radius=True)); score=out['F_R2']
    print(json.dumps(out),flush=True); scan.append(out)
    if best is None or score<best[0]: best=(score,out)
  if mode!='dom': pass
res['scan']=scan; res.update(best[1]); res['secs']=round(time.time()-t0)
json.dump(res,open(outf,'w'),indent=1); print('BEST',json.dumps(best[1]),flush=True)
