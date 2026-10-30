"""Line G: general rational-reconstruction law for Z_m(nu) (independent of Line E code except MC formula re-derived below).
Z_m(nu) = sum_n Phihat(n) e(-nu P(n)/(2h)),  P(n) = sum_ij psi(|i-j|) n_i n_j,  psi(d) = y' x_d - 2h y_d,  q = P/(4h).
For any (a,b), b>0, with b nu = a + 2h k:   -nu P/(2h) = -(2a/b) q(n) - k P(n)/b   (exact).
Real part: q = 2c[sum n_j s_j + 1/2 sum n_j^2] (periodic IFS orbit s).  Arithmetic part: P mod b by the automaton
  (u,w)_0=(0,0), step n: contribution psi0 n^2 + 2 n u ;  (u,w) -> (6u - w + n psi1, u + n psi0)  (mod b).
Transfer law (finite alphabet |n|<=L):  Z = (1-lam^-m) Tr_H[(I x <1|) Lop^m (I x |delta_0>)],
  Lop = sum_n ghat(n) e(C n^2/2) MC_n (x) A_n,  C = -4 a c / b,  MC_n: phi(s) -> e(C n s) phi((s+n)/lam) on H^2(D_rho)."""
import math, numpy as np
from scipy.special import gammaln, jv
LAM=3+2*math.sqrt(2); C0=1/(LAM-1/LAM)
def pell(d):
    x,y=1,0
    for _ in range(d): x,y=3*x+8*y,x+3*y
    return x,y
def mdata(m):
    xm,ym=pell(m); D=2*(xm-1); h=math.isqrt(D//4); assert 4*h*h==D and ym%h==0
    yp=ym//h; assert h*h+1==2*yp*yp
    return dict(m=m,h=h,yp=yp,gp=2*h)
def gauss_reduce(u,v):
    n2=lambda w:w[0]*w[0]+w[1]*w[1]
    if n2(u)>n2(v): u,v=v,u
    while True:
        d=u[0]*v[0]+u[1]*v[1]; nu=n2(u); q=(2*d+nu)//(2*nu)
        v=(v[0]-q*u[0],v[1]-q*u[1])
        if n2(v)>=n2(u): return u,v
        u,v=v,u
def ratrec(nu,M):
    """short (a,b) with a == b nu (mod M); returns both reduced basis vectors normalised b>0 (or b=0,a>0)"""
    u,v=gauss_reduce((M,0),(nu%M,1)); out=[]
    for a,b in (u,v):
        if b<0 or (b==0 and a<0): a,b=-a,-b
        out.append((a,b))
    return out
def kick_ghat(name,eta,L):
    if name=='k1':
        return {n:(1j**n)*jv(n,0.9*eta) for n in range(-L,L+1)}
    raise ValueError
def ghat_fft(f,eta,L,M=4096):
    th=np.arange(M)/M; c=np.fft.fft(np.exp(1j*eta*f(th)))/M
    return {n:complex(c[n%M]) for n in range(-L,L+1)}
def MC(x,coef,rho,K):
    """Galerkin matrix of phi -> e(coef*x*s) phi((s+x)/lam) in the ON basis (s/rho)^k of H^2(D_rho)."""
    l=np.arange(K); d=l[:,None]-l[None,:]
    if x==0: return np.diag(LAM**(-l.astype(float))).astype(complex)
    z=2j*np.pi*coef*x*rho
    dd=np.where(d>=0,d,0)
    if coef==0: Mm=np.eye(K,dtype=complex)
    else: Mm=np.where(d>=0,np.exp(dd*np.log(z+0j)-gammaln(dd+1)),0)
    kk=l[None,:]; jj=l[:,None]; e=kk-jj; ee=np.where(e>=0,e,0)
    logb=gammaln(kk+1)-gammaln(jj+1)-gammaln(ee+1)
    Cm=np.where(e>=0,np.exp(logb-kk*np.log(LAM)+ee*np.log(abs(x)/rho))*np.sign(x)**ee,0)
    return Mm@Cm
def Z_law(m,nu,gh,K=40,rho=None,ab=None,return_parts=False):
    d=mdata(m); h=d['h']; yp=d['yp']; M=2*h
    if ab is None: a,b=ratrec(nu,M)[0]
    else: a,b=ab
    assert b>0 and (b*nu-a)%M==0
    k=(b*nu-a)//M
    L=max(abs(n) for n in gh)
    if rho is None: rho=1.25*L/(LAM-1)+0.5
    assert rho>L/(LAM-1)
    coef=-4*a*C0/b
    psi0=yp%b; psi1=(3*yp-2*h)%b
    S=b*b  # states s = u*b + w
    us=np.arange(S)//b; ws=np.arange(S)%b
    # state vector: X[k_out,k_in,state]
    X=np.zeros((K,K,S),complex); X[:,:,0]=np.eye(K)
    mats={n:gn*np.exp(2j*np.pi*coef*n*n/2)*MC(n,coef,rho,K) for n,gn in gh.items() if abs(gn)>0}
    for step in range(m):
        Y=np.zeros_like(X)
        for n,Mn in mats.items():
            ph=np.exp(-2j*np.pi*((k*((psi0*n*n+2*n*us)%b))%b)/b)   # e(-k*contrib/b)
            tgt=(((6*us-ws+n*psi1)%b)*b+((us+n*psi0)%b))
            contrib=np.einsum('ij,jks->iks',Mn,X)*ph[None,None,:]
            np.add.at(Y,(slice(None),slice(None),tgt),contrib) if False else None
            # scatter along state axis
            Yt=np.zeros_like(X)
            np.add.at(Yt.transpose(2,0,1),tgt,contrib.transpose(2,0,1))
            Y+=Yt
        X=Y
    Z=(1-LAM**(-m))*np.trace(X.sum(axis=2))
    return (Z,(a,b,k)) if return_parts else Z
def Z_brute(m,nu,gh):
    import itertools
    d=mdata(m); h=d['h']; yp=d['yp']
    X=[pell(t)[0] for t in range(m)]
    tot=0j; keys=list(gh)
    for n in itertools.product(keys,repeat=m):
        Nm=sum(X[abs(i-j)]*n[i]*n[j] for i in range(m) for j in range(m))
        w=1
        for t in n: w*=gh[t]
        tot+=w*np.exp(2j*np.pi*((-nu*yp*Nm)%(2*h))/(2*h))
    return tot
