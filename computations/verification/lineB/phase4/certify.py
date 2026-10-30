"""Rigorous certificate:  for eta in [e0,e1],  |chi_m(eta)| <= sum_a C_a rho_a^(m-1)  (odd m).
Ingredients (REPORT4 §1): arb enclosures of what_eta0(n) (Bessel product); Gronwall bound over the eta-interval;
cycle inequality  gamma0*sum N(s_j) <= c*sum|n_j-a|  => |chi_m| <= sum_a Tr(A_a^m), A_a tilted (beta);
Collatz-Wielandt with test vector v = max(v_perron, e^{-kappa N}) on box S_K and v <= C e^{-kappa N} outside.
All float sums are of nonnegative terms; we multiply by SAFE=1+1e-9 (>> accumulated rounding (#terms)*2^-52)."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys, math, time, json; sys.path.insert(0,'.')
import numpy as np, flint
from wcoef import BETA, what_arb
from transfer import *
flint.ctx.prec=128
SAFE=1+1e-9
D=np.zeros(19); 
for k,b in BETA.items(): D[9+k]=D[9-k]=abs(float(b))/2*SAFE     # |d_k|, u=sum d_k e(k th)
Dnorm=D.sum()
def bounds(e0,e1,J=60):
    off,cs,tl=what_arb(e0,J)
    b0=np.array([float(abs(x).upper()) for x in cs])*SAFE+1e-300; n=np.arange(len(cs))+off
    eps=e1-e0; b=b0.copy(); term=b0.copy()
    for i in range(1,5):
        term=np.convolve(term,D)[9:-9]*eps*SAFE; b=b+term
    return n,b*SAFE,b0,eps,float(tl)
def remainder_mass(b0,n,eps,tau):
    Dt=sum(abs(float(bb))*math.exp(tau*k) for k,bb in BETA.items())*SAFE   # tilted l1 of D
    x=eps*Dt; nb=float(np.sum(b0*np.exp(tau*np.abs(n))))
    return x**5/(1-x)*nb
def lattice_tail(K,x):
    s=0.0; j=int(math.floor(K))
    while True:
        t=(2*(j+1)+1)*(2*LAM*(j+1)+1)*math.exp(-x*j); s+=t
        if t<1e-20*s and j>K+50: break
        j+=1
    return s*1.01
def certify(e0,e1,beta,kappa,K,a,n,b,rem,jt):
    tau=(beta+kappa)*CC_SAFE
    keep=b*np.exp(tau*(np.abs(n)+3))>1e-40
    drop=float(np.sum((b*np.exp(tau*(np.abs(n)+3)))[~keep]))
    nn,bb=n[keep],b[keep]
    A,om,(P,Q,Nv)=build(K,a,nn,bb,beta)
    r0,vp=perron(A)
    v=np.maximum(vp/vp.max(),np.exp(-kappa*Nv))
    Cc=float(np.max(v*np.exp(kappa*(Nv+1e-9))))*SAFE          # global v <= Cc e^{-kappa N}
    # (Av)(s): inside part + outside neighbours bounded by Cc e^{-kappa N(s')} computed per n
    Av=A@v
    R=int(math.ceil(LAM*K))+2
    damp=np.exp(-beta*G0_SAFE*Nv)
    extra=np.zeros(len(P))
    for nv,w in zip(nn,bb*np.exp(beta*CC_SAFE*np.abs(nn-a))):
        p2=Q; q2=6*Q-P+a-nv; N2=Ncoord(p2.astype(float),q2.astype(float))-1e-9
        outside=N2>K
        extra[outside]+=damp[outside]*w*Cc*np.exp(-kappa*N2[outside])
    # dropped n's and Gronwall remainder and J-tail: mass * max v (v<=Cc) , tilted by e^{beta c(|n|+3)}
    extra+=damp*(drop+rem+jt)*max(Cc,1.0)
    ratio=(Av+extra)*SAFE/v
    rin=float(ratio.max())
    Wp=float(np.sum(b*np.exp(tau*(np.abs(n)+3))))+drop+rem+jt
    rout=math.exp(-(beta-kappa)*G0_SAFE*K)*Wp*SAFE
    rho=max(rin,rout)
    const=float(np.sum(ratio))+Wp*lattice_tail(K,(beta-kappa)*G0_SAFE)
    return dict(e0=e0,e1=e1,a=a,beta=beta,kappa=kappa,K=K,states=len(P),rho_float=r0,rho_in=rin,rho_out=rout,rho=rho,C=const)
def params(e):
    if e<=12: return 0.1,0.05
    if e<=40: return 0.1,0.05
    return 0.08,0.04
if __name__=='__main__':
    e_lo,e_hi,ratio=float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3])
    out=open(sys.argv[4],'a')
    e0=e_lo
    while e0<e_hi-1e-12:
        e1=min(e_hi,e0*ratio); t0=time.time()
        n,b,b0,eps,tl=bounds(e0,e1)
        beta,kappa=params(e1); tau=(beta+kappa)*CC_SAFE
        rem=remainder_mass(b0,n,eps,tau); jt=tl*1e30  # crude: J-tail l1 (<=1e-80) times generous tilt factor
        Wp=float(np.sum(b*np.exp(tau*(np.abs(n)+3))))
        res=[]
        for a in range(4):
            # choose K so that rho_out <= 0.98*rho_float estimate
            A0,_,_=build(6,a,n[b>1e-30],b[b>1e-30],beta); r6,_=perron(A0)
            K=int(math.ceil(math.log(Wp/(0.9*min(r6,0.999)) if Wp>0.9*min(r6,.999) else 1)/((beta-kappa)*G0_SAFE)))+3
            K=max(K,8)
            if r6>1e-3 and math.exp(-(beta-kappa)*G0_SAFE*K)*Wp>r6: K+=10
            res.append(certify(e0,e1,beta,kappa,K,a,n,b,rem,jt))
        rec=dict(e0=e0,e1=e1,res=res,time=time.time()-t0)
        out.write(json.dumps(rec)+'\n'); out.flush()
        print(f'[{e0:.4f},{e1:.4f}] '+' | '.join(f"a={r['a']} K={r['K']} rho<={r['rho']:.6f} (float {r['rho_float']:.6f}, out {r['rho_out']:.3f}) C<={r['C']:.2e}" for r in res)+f'  {time.time()-t0:.0f}s',flush=True)
        e0=e1
