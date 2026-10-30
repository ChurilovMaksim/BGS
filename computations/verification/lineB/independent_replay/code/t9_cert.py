"""Independent rigorous re-certification of |chi_m(eta)| <= sum_a C_a rho_a^(m-1) on an eta-interval.
Own normalisation: u=q-p/lam, t=q-p*lam, N=|u|+|t|; T(p,q)=(q,6q-p): u->lam u, t->t/lam; kick (0,-d): |du|,|dt|<=|d| => c=2.
gamma0 = 1-1/lam (L=|u|-|t| Lyapunov).  Tilted majorant A_a[s->s'] = e^{-b g0 N(s)} b(n) e^{b c |n-a|}, s'=Ts+(0,a-n).
Coefficients: arb (python-flint) with eta as a BALL (sub-intervals), Bessel product; rigorous tilted tail.
Verification arithmetic: float64 with explicit outward rounding (np.nextafter after every +,*,/), exponentials only
via arb-computed tables on a 1/64 grid (monotone), N(s) enclosed by float +-1e-9.  No reuse of phase-4 code."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys, math, time, json
import numpy as np, flint, scipy.sparse as sp, scipy.sparse.linalg as spl
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__))); from core import CK
from fractions import Fraction as Fr
flint.ctx.prec=120
arb=flint.arb
AK={k:Fr(-4)*Fr(CK[k][1]) for k in CK if k>0 and CK[k][1]!=0}   # u = sum_k AK[k] sin(2 pi k th)
LAMa=arb(3)+2*arb(2).sqrt(); G0a=1-1/LAMa
LAM=3+2*math.sqrt(2)
G0_LO=float((G0a).lower())*(1-1e-15)      # rigorous lower for gamma0
CC=2.0                                    # exact
INF=np.inf
up=lambda x: np.nextafter(x,INF)
dn=lambda x: np.nextafter(x,-INF)
def aup(x): return float(np.nextafter(float(x.upper()),INF)) if not isinstance(x,float) else x
def coef_bounds(e0,e1,tau,M=24,J=40,cut=1e-30):
    """b[n] >= sup_{eta in [e0,e1]} |trunc coefficient n| for band |n|<=nc; Edrop >= sup tilted (weight e^{tau(|n|+3)}) mass of
    everything else (out-of-band truncated coefficients + full truncation error)."""
    deg=J*sum(AK.keys()); bmax=np.zeros(2*deg+1); Emax=0.0
    edges=[Fr(e0)+(Fr(e1)-Fr(e0))*i/M for i in range(M+1)]
    for i in range(M):
        lo,hi=edges[i],edges[i+1]
        eta=arb(float((lo+hi)/2),float((hi-lo)/2)*(1+1e-12)+1e-30)
        poly=flint.arb_poly([1]); A_tr=arb(1); A_er=arb(1)
        for k in sorted(AK):
            x=eta*arb(AK[k].numerator)/AK[k].denominator
            cs=[arb(0)]*(2*J*k+1)
            for j in range(0,J+1):
                bj=x.bessel_j(j); cs[(J+j)*k]=bj; cs[(J-j)*k]=bj*(-1)**j
            poly=poly*flint.arb_poly(cs)
            X=abs(x).upper(); y=X*arb(tau*k).exp()/2
            tail=2*y**(J+1)/arb(math.factorial(J+1))*y.exp()
            ntr=sum((abs(cs[(J+j)*k]).upper()*arb(tau*k*j).exp()*(1 if j==0 else 2)) for j in range(J+1))
            A_tr=A_tr*ntr; A_er=A_er*(ntr+tail)
        err=(A_er-A_tr).upper()          # tilted l1 of (true - truncated)
        c=[poly[j] for j in range(poly.degree()+1)]; assert len(c)==2*deg+1
        b=np.array([aup(abs(z).upper()) for z in c])
        bmax=np.maximum(bmax,b)
        Emax=max(Emax,float(err.upper())*1.0000001)
    n=np.arange(-deg,deg+1)
    wt=bmax*np.exp(tau*(np.abs(n)+3))*1.000001
    keep=wt>cut
    Edrop=float(np.sum(wt[~keep]))*1.000001+Emax*math.exp(3*tau)*1.000001
    return n[keep],bmax[keep],Edrop
class ExpTab:
    """rigorous upper/lower for e^{s x} for x>=0 on grid step 1/64 (monotone in x)."""
    def __init__(s,rate,xmax):
        s.rate=rate; s.h=64; L=int(math.ceil(xmax*64))+2
        s.v_up=np.array([aup((arb(rate)*arb(i)/64).exp()) for i in range(L)])
        s.v_dn=np.array([float(np.nextafter(float((arb(rate)*arb(i)/64).exp().lower()),-INF)) for i in range(L)])
    def up_of(s,x):   # >= e^{rate*x}; rate may be negative: then use floor if rate<0
        if s.rate>=0: return s.v_up[np.ceil(np.maximum(x,0)*64).astype(np.int64)]
        return s.v_up[np.floor(np.maximum(x,0)*64).astype(np.int64)]
def Nenc(p,q):
    p=p.astype(float); q=q.astype(float); u=q-p/LAM; t=q-p*LAM; N=np.abs(u)+np.abs(t)
    return np.maximum(N-1e-9,0), N+1e-9
def certify(e0,e1,a,beta,kappa,R1,x2,coef,theta=1e-9,iters=40,verbose=False):
    n,b,Edrop=coef
    R=LAM*(R1+CC*x2)*(1+1e-12)+1.0
    Pm=int(math.ceil(R/(4*math.sqrt(2))))+2; Qm=int(math.ceil(R*(1+1/(4*math.sqrt(2)*LAM))))+2
    P,Q=np.meshgrid(np.arange(-Pm,Pm+1),np.arange(-Qm,Qm+1),indexing='ij'); P=P.ravel(); Q=Q.ravel()
    Nlo,Nhi=Nenc(P,Q); sel=Nhi<=R            # box B: N(s)<=R certainly; complement: N>R-2e-9  (we use Nlo of outside >= R-2e-9)
    P,Q,Nlo,Nhi=P[sel],Q[sel],Nlo[sel],Nhi[sel]; S=len(P)
    idx=-np.ones((2*Pm+1,2*Qm+1),np.int64); idx[P+Pm,Q+Qm]=np.arange(S)
    Nmax_needed=LAM*R+CC*(np.max(np.abs(n))+3)+10
    Tdamp=ExpTab(-beta*G0_LO,R+1); Tk=ExpTab(-kappa,Nmax_needed); Tkp=ExpTab(kappa,R+1)
    damp=Tdamp.up_of(Nlo)                    # >= e^{-beta g0 N(s)}
    wn=np.array([aup(arb(float(bb))*(arb(beta*CC)*abs(int(nn)-a)).exp()) for nn,bb in zip(n,b)])  # >= b e^{beta c|n-a|}
    # float sparse matrix (values rounded up) + out-of-box unit masses e^{-kappa N(s')}
    rows=[];cols=[];vals=[]; bout=np.zeros(S)
    for nn,w in zip(n,wn):
        p2=Q; q2=6*Q-P+a-nn
        ok=(np.abs(p2)<=Pm)&(np.abs(q2)<=Qm); j=np.full(S,-1); j[ok]=idx[p2[ok]+Pm,q2[ok]+Qm]; inb=j>=0
        rows.append(np.flatnonzero(inb).astype(np.int32)); cols.append(j[inb].astype(np.int32)); vals.append(up(damp[inb]*w))
        if (~inb).any():
            nlo,_=Nenc(p2[~inb],q2[~inb])
            bout[~inb]=up(bout[~inb]+up(up(damp[~inb]*w)*Tk.up_of(nlo)))
    rr=np.concatenate(rows); del rows; cc=np.concatenate(cols); del cols; vv=np.concatenate(vals); del vals
    A=sp.csr_matrix((vv,(rr,cc)),shape=(S,S)); del rr,cc,vv
    # ---- heuristic construction of v (any positive v is fine) ----
    core=np.flatnonzero(Nhi<=R1)
    Ac=A[core][:,core].toarray(); ev,evec=np.linalg.eig(Ac); i=np.argmax(ev.real); vc=np.abs(evec[:,i].real)
    v0=np.full(S,1e-9); v0[core]+=vc/vc.max()
    ev,evv=spl.eigs(A,k=1,which='LM',v0=v0,tol=1e-13,maxiter=10000)
    r0=float(abs(ev[0])); vp=np.abs(evv[:,0].real); vp/=vp.max()
    rt=r0*(1+max(2e-6,0.03*(1-r0))) if a==0 else max(0.9,r0*(1+max(2e-6,0.03*(1-r0))))
    phi=theta*np.exp(-kappa*Nhi)
    outer=Nlo>R1
    Cv=1.5*float(np.max((np.maximum(phi,vp)*np.exp(kappa*Nhi))[outer]))
    Vg=1.5
    for rnd in range(40):
        v=np.maximum(phi,vp)
        for it in range(iters): v=np.maximum(phi,(A@v+Cv*bout+damp*Edrop*Vg)/rt)
        Cact=float(np.max((v*np.exp(kappa*Nhi))[outer])); Vm=max(float(v.max()),Cv*math.exp(-kappa*R))
        if Cact<=Cv*0.999 and Vm<=Vg*0.999: break
        Cv=max(Cv,1.5*Cact); Vg=max(Vg,1.5*Vm)
    # ---- rigorous verification (outward rounding) ----
    Vmax=max(float(v.max()),aup(arb(Cv)*(-arb(kappa)*arb(R-2e-9)).exp()))   # sup over Z^2 of v (outside: Cv e^{-kappa N}, N>R-2e-9)
    okV = Vmax<=Vg
    chkC=up(v*Tkp.up_of(Nhi)); okC=bool(np.all(chkC[outer]<=Cv))   # v(s) <= Cv e^{-kappa N(s)} for N(s)>R1 in box
    # Av upper: sum over n of up(A_sn * v_s') with upward accumulation: emulate per-row via CSR loop in numpy
    # fl(A@v) for nonnegative entries: any summation order, each product and sum rounded to nearest (FMA only helps):
    # true <= fl * (1+(k+1)u)/(1-(k+1)u), k = row nnz, u = 2^-53.  A entries are already upper bounds.
    cnt=np.diff(A.indptr).astype(float); g=(cnt+1)*2.0**-53
    rs=up(up(A@v)*up((1+g)/(1-g)*(1+4*2.0**-53)))
    tot=up(rs+up(Cv*bout)); tot=up(tot+up(up(damp*Edrop)*Vmax)); tot=up(tot*(1+8*2.0**-53))
    ratio=up(tot/v); rin=float(ratio.max())
    # ---- outside the box (N(s)>R): analytic, evaluated in arb ----
    tau=(beta+kappa)*CC
    small=np.abs(n-a)<x2
    Wp=sum(arb(float(bb))*(arb(tau)*abs(int(nn)-a)).exp() for nn,bb in zip(n[small],b[small]))
    Tx=sum(arb(float(bb))*(arb(beta*CC)*abs(int(nn)-a)).exp() for nn,bb in zip(n[~small],b[~small]))+arb(Edrop)
    g0=G0a; Rl=arb(R-2e-9)
    term1=(-(arb(beta)-kappa)*g0*Rl).exp()*Wp
    term2=(-(arb(beta)*g0-kappa)*Rl).exp()*Tx*arb(Vmax)/arb(Cv)
    rout=float((term1+term2).upper())
    xo=min(float(((arb(beta)-kappa)*g0).lower()),float((arb(beta)*g0-kappa).lower()))
    # lattice tail sum_{N(s)>R} e^{-xo N(s)}; #{N<=r} <= (2r/(4 sqrt2)+1)(2r(1+1/(4 sqrt2 lam))+1)
    s4=4*arb(2).sqrt(); cntf=lambda r: (2*r/s4+1)*(2*r*(1+1/(s4*LAMa))+1)
    tail=arb(0); j=int(math.floor(R-1e-6))
    while True:
        t=cntf(arb(j+1))*(-arb(xo)*j).exp(); tail+=t
        if j>R+50 and float(t.upper())<1e-30*float(tail.lower()): break
        j+=1
    # remaining: terms decrease at least geometrically with ratio q=((j+2)/(j+1))^2 e^{-xo} < 1
    qq=((arb(j+2)/(j+1))**2)*(-arb(xo)).exp(); tail+=t*qq/(1-qq)
    const=float((arb(float(np.sum(ratio)))*(1+1e-12)+(Wp*(1)+Tx*arb(Vmax)/arb(Cv))*tail).upper())
    rho=max(rin,rout)
    return dict(e0=e0,e1=e1,a=a,states=S,R=R,rho_float=r0,rho_t=rt,rho_in=rin,rho_out=rout,rho=rho,C=const,
                valid=bool(okV and okC and rho<1),Vmax=Vmax,Cv=Cv,Edrop=Edrop,nband=len(n))
def run(e0,e1,beta,kappa,R1,x2,M=24):
    tau=(beta+kappa)*CC
    t=time.time(); coef=coef_bounds(e0,e1,tau,M=M)
    out=[]
    for a in range(4):
        r=certify(e0,e1,a,beta,kappa,R1,x2,coef); r['secs']=round(time.time()-t); out.append(r)
        print(json.dumps({k:(float(f'{x:.8g}') if isinstance(x,float) else x) for k,x in r.items()}),flush=True)
    return out
if __name__=='__main__':
    e0,e1=float(sys.argv[1]),float(sys.argv[2])
    beta=float(sys.argv[3]) if len(sys.argv)>3 else 0.1/(4*math.sqrt(2))
    kappa=float(sys.argv[4]) if len(sys.argv)>4 else beta/2
    R1=float(sys.argv[5]) if len(sys.argv)>5 else 8*4*math.sqrt(2)
    x2=float(sys.argv[6]) if len(sys.argv)>6 else 25
    res=run(e0,e1,beta,kappa,R1,x2)
    rho=max(r['rho'] for r in res); C=sum(r['C'] for r in res)
    print(f'RESULT [{e0},{e1}] valid={all(r["valid"] for r in res)} rho<={rho:.7f} C<={C:.3e}  => |chi_m| <= C rho^(m-1)',flush=True)
