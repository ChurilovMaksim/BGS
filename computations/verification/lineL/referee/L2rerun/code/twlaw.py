"""Line L2 [N]: twisted transfer law  Zhat(beta) = sum_n w(n) e(sum_i n_i tau_i),  tau_i = Tr(beta lam^i)/q,
w(n) = Phihat(n) e(-nu0 P(n)/2h) (TRACE-206), via Line G/I law.py transfer (MC Galerkin + P mod b automaton),
with an extra per-step letter phase e(n tau_step).  Validated against brute force (m=5)."""
import sys, math, numpy as np
sys.path.insert(0,'/workspace/bgs-lineI/code')
from law import mdata, pell, ratrec, kick_ghat, MC, LAM, C0
class TW:
    def __init__(s,m,nu,L=10,K=40,rho=None):
        d=mdata(m); s.m=m; s.h=d['h']; yp=d['yp']; M=2*s.h
        a,b=ratrec(nu,M)[0]; assert b>0 and (b*nu-a)%M==0
        s.k=(b*nu-a)//M; s.a,s.b=a,b
        gh=kick_ghat('k1',2.0,L); s.gh=gh
        if rho is None: rho=1.25*L/(LAM-1)+0.5
        coef=-4*a*C0/b; s.K=K
        s.psi0=yp%b; s.psi1=(3*yp-2*s.h)%b
        S=b*b; s.S=S; us=np.arange(S)//b; ws=np.arange(S)%b
        s.ns=[n for n,g in gh.items() if abs(g)>0]
        s.Mn={n:gh[n]*np.exp(2j*np.pi*coef*n*n/2)*MC(n,coef,rho,K) for n in s.ns}
        s.ph={n:np.exp(-2j*np.pi*((s.k*((s.psi0*n*n+2*n*us)%b))%b)/b) for n in s.ns}
        s.tgt={n:(((6*us-ws+n*s.psi1)%b)*b+((us+n*s.psi0)%b)) for n in s.ns}
        assert all(len(set(t.tolist()))==S for t in s.tgt.values())
    def Z(s,taus):
        K,S=s.K,s.S
        X=np.zeros((S,K,K),complex); X[0]=np.eye(K)
        for step in range(s.m):
            Y=np.zeros_like(X); t=taus[step]
            for n in s.ns:
                c=np.exp(2j*np.pi*n*t)
                contrib=np.matmul(s.Mn[n],X)*(s.ph[n]*c)[:,None,None]
                Y[s.tgt[n]]+=contrib   # tgt is a permutation of states (affine map with det 1 mod b)
            X=Y
        return (1-LAM**(-s.m))*np.trace(X.sum(axis=0))
def lam_pows(m,q):
    out=[]; x,y=1,0
    for i in range(m): out.append((x%q,y%q)); x,y=3*x+4*y,2*x+3*y
    return out   # lam^i = x + y sqrt2
def taus_of(beta,pw,q):
    bx,by=beta
    return [((2*(bx*x+2*by*y))%q)/q for (x,y) in pw]
if __name__=='__main__':
    import itertools
    from scipy.special import jv
    m=5; d=mdata(m); h=d['h']; yp=d['yp']; M=2*h
    nu0=next(x for x in range(1,M,2) if (8*x-2)%M==0)
    tw=TW(m,nu0,L=4,K=40)
    q=h; pw=lam_pows(m,q)
    xs=[pell(k) for k in range(m)]; psi=[yp*xs[k][0]-2*h*xs[k][1] for k in range(m)]
    for beta in [(0,0),(1,0),(3,7),(5,2)]:
        tau=taus_of(beta,pw,q); tot=0j
        for n in itertools.product(range(-4,5),repeat=m):
            P=sum(psi[abs(i-j)]*n[i]*n[j] for i in range(m) for j in range(m))
            w=np.prod([tw.gh[t] for t in n])*np.exp(-2j*np.pi*((nu0*P)%M)/M)
            tot+=w*np.exp(2j*np.pi*sum(n[i]*tau[i] for i in range(m)))
        z1=tw.Z(tau); z2=tw.Z(tau[::-1])
        print(beta, 'brute',np.round(tot,8),'tw',np.round(z1,8),'tw_rev',np.round(z2,8))
