"""Referee (Line H audit): independent re-implementation of the spectral certificate for one lifted operator.
Different from rig_spec.py: (i) more conservative dot-product constant gref = sqrt2*gamma_{2n+2} (covers zgemm kernels that
accumulate the 2n real products of a complex dot product in one accumulator); (ii) dom mode: a-posteriori residual bound for the
Householder similarity (E = H A - B H computed and bounded), not the a-priori formula; (iii) norms inflated by 1+1e-6.
Usage: ref_rig.py prefix sector mode R r1 p build.json out.json"""
import sys, json, time, numpy as np, scipy.sparse.linalg as ssl, scipy.linalg as sl
from flint import arb, acb, ctx
ctx.prec=128
pre,b,mode,Rs,r1s,p,bj,outf=sys.argv[1],int(sys.argv[2]),sys.argv[3],sys.argv[4],sys.argv[5],int(sys.argv[6]),sys.argv[7],sys.argv[8]
t0=time.time(); u=arb(2)**-53
def A_(x): return arb(float(x))
def up(x): return A_(x)*arb('1.000001')
def fro(M): return up(np.sqrt(np.vdot(M,M).real))
A=np.load(f'{pre}_b{b}_mid.npy'); rad=np.load(f'{pre}_b{b}_rad.npy'); D=A.shape[0]
assert np.isfinite(A).all() and np.isfinite(rad).all() and (rad>=0).all()
epsA=fro(rad); del rad
g=lambda L: arb(2).sqrt()*(L*u)/(1-L*u)
gref=g(2*D+2)
info=json.load(open(bj)); assert info['D']==D
out=dict(D=D,epsA=float(epsA.upper()),midfro=float(np.linalg.norm(A)),gref=float(gref.upper()))
print(out,flush=True)
kap=arb(1); extra=arb(0)
if mode=='dom':
    ev,vv=ssl.eigs(A,k=4,which='LM',tol=1e-13,maxiter=10000); i0=np.argmax(abs(ev)); mu=ev[i0]; v=vv[:,i0]
    lu=sl.lu_factor(A-mu*np.eye(D))
    for _ in range(2): v=sl.lu_solve(lu,v); v/=np.linalg.norm(v)
    del lu
    w=v.copy(); k0=int(np.argmax(abs(v)));  # Householder vector mapping v -> alpha e_{k0} (no permutation; deflate index k0)
    al=-v[k0]/abs(v[k0]); w[k0]-=al
    nw=float(np.vdot(w,w).real); tau=2.0/nw
    n_=sum((A_(t.real)**2+A_(t.imag)**2 for t in w),arb(0)); dev=abs(A_(tau)*n_-2); assert dev<arb('1e-10')
    Hn=arb.max(arb(1),abs(1-A_(tau)*n_)); Hin=1/(1-dev); kap=Hn*Hin
    # B = H A H in float
    u1=A@w; u2=w.conj()@A; be=np.vdot(w,u1)
    B=A-tau*np.outer(w,u2)-tau*np.outer(u1,w.conj())+(tau*tau*be)*np.outer(w,w.conj())
    # a-posteriori: true similarity is S = H A H^{-1}. Residual E = H A - B H (exact) => S = B + E H^{-1}.
    # compute HA = A - tau w (w^H A) and BH = B - tau (B w) w^H in float; Efl = HA - BH.
    HA=A-tau*np.outer(w,u2); Bw=B@w; BH=B-tau*np.outer(Bw,w.conj())
    Efl=HA-BH; del HA,BH
    nA=fro(A); nB=fro(B); nwF=up(np.sqrt(nw)); t=A_(tau)
    # rounding of Efl vs exact E: matvecs u2, Bw: <= gref ||A||_F ||w||, gref||B||_F||w||; times tau||w||;
    # entrywise ops (product tau*w_i*x_j: <=3 complex roundings, two subtractions): <= 8u*(|A|+tau|w||u2|+|B|+tau|Bw||w|) normwise
    err=t*nwF*(gref*nA*nwF)+t*nwF*(gref*nB*nwF)+8*u*(nA+t*nwF*fro(u2)+nB+t*fro(Bw)*nwF)
    Enorm=fro(Efl)+err
    extra=Enorm*Hin           # ||E H^{-1}||
    # move index k0 to front by exact permutation of B
    perm=np.arange(D); perm[0],perm[k0]=k0,0
    B=B[np.ix_(perm,perm)]
    b11=complex(B[0,0]); b12=B[0,1:].copy(); b21=fro(B[1:,0]); Y=np.ascontiguousarray(B[1:,1:]); del B,A,Efl
    extra=extra+b21     # in deflated coordinates; similarity H^{-1} applied => factor kap later
    out.update(b11=str(b11),b21=float(b21.upper()),Eres=float(Enorm.upper()),kappa=float(kap.upper()),extra=float(extra.upper()))
    print(out,round(time.time()-t0),flush=True)
else:
    Y=A; del A
nY=fro(Y); gY=g(2*Y.shape[0]+2)
N=[arb(1),None]; Es={}
M=Y.copy(); N[1]=arb.min(nY,(up(abs(Y).sum(0).max())*up(abs(Y).sum(1).max())).sqrt())
rows=[]; 
if mode=='dom':
    r=b12.copy(); rows.append(fro(r)); Er={}
for j in range(2,p+1):
    Es[j]=gY*fro(M)*nY; M=M@Y
    e=sum((Es[i]*N[j-i] for i in range(2,j+1)),arb(0))
    n1=up(abs(M).sum(0).max()); ni=up(abs(M).sum(1).max())
    N.append(arb.min(fro(M),(n1*ni).sqrt())+e)
    if j%4==0: print('j',j,float(N[j].upper()),float(e.upper()),round(time.time()-t0),flush=True)
G=M.conj().T@M; N[p]=arb.min(N[p],(fro(G)+gY*fro(M)**2).sqrt()+e); del G,M
if mode=='dom':
    # rows[j] >= ||b12 Y^j||, j=0..p-1 : r_j = fl(r_{j-1}Y), r_j - b12Y^j = sum_{i=1..j} Er_i Y^{j-i}
    for j in range(1,p):
        Er[j]=gY*fro(r)*nY; r=r@Y
        rows.append(fro(r)+sum((Er[i]*N[j-i] for i in range(1,j+1)),arb(0)))
pert=A_(info['delta1'])+A_(info['delta2'])+A_(info['Delta'])+epsA+kap*extra
X=A_(info['Xnorm'])
def neum(z,V):
    q=N[p]/z**p; assert q<1
    return sum((V[j]/z**(j+1) for j in range(p)),arb(0))/(1-q)
full=lambda Rc,za:(kap*Rc+1/za)*(1+X/za)+1/za
res=[]
for R_ in Rs.split(','):
    R=arb(R_)
    if mode=='rest':
        FR=pert*full(neum(R,N),R); res.append(dict(R=R_,F=float(FR.upper()),cert=bool(FR<1)))
    else:
        for r1_ in r1s.split(','):
            r1=arb(r1_); ab=abs(acb(A_(b11.real),A_(b11.imag))); z1=ab-r1; assert z1>R
            Rc1=(1+neum(z1,rows))/r1+neum(z1,N); Rc2=(1+neum(R,rows))/(ab-R)+neum(R,N)
            F1=pert*full(Rc1,z1); F2=pert*full(Rc2,R)
            res.append(dict(R=R_,r1=r1_,F1=float(F1.upper()),F2=float(F2.upper()),cert=bool(F1<1 and F2<1),mu_lo=float((ab-r1).lower()),mu_hi=float((ab+r1).upper())))
    print(res[-1],flush=True)
out.update(pert=float(pert.upper()),N=[float(x.upper()) for x in N],res=res,secs=round(time.time()-t0))
json.dump(out,open(outf,'w'),indent=1); print('DONE',round(time.time()-t0),flush=True)
