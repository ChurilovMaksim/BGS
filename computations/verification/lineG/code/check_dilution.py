"""Exact check of the dilution identity (Theorem G3) by brute force, random weights, m=9 (h=1393=7*199, d=7), m=5 (h=41,d=41).
Z(nu0 + (2h/d) j) = G_d(t)/d^2 * sum_{beta in O/d} e(tbar Nm(beta)/d) * Z_{nu0}^{(beta)},  t = j y' mod d (unit),
Z^{(beta)} = sum_n w(n) e(sum_i n_i Tr(beta lam^i)/d),  w(n)=Phihat(n) e(-nu0 P(n)/2h),  G_d(t)=sum_{alpha in O/d} e(-t Nm(alpha)/d)."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import numpy as np, itertools, math, random
from law import mdata, pell
def run(m,L,d,seed=0):
    rng=np.random.default_rng(seed); D=mdata(m); h=D['h']; yp=D['yp']; assert h%d==0
    vals=np.arange(-L,L+1); gh=rng.normal(size=2*L+1)+1j*rng.normal(size=2*L+1)
    grid=np.array(list(itertools.product(range(2*L+1),repeat=m)),dtype=np.int64); n=vals[grid]
    X=np.array([[pell(abs(i-j))[0] for j in range(m)] for i in range(m)],dtype=object)
    Y=np.array([[pell(abs(i-j))[1] for j in range(m)] for i in range(m)],dtype=object)
    # P(n) = sum psi(|i-j|) n_i n_j exactly, psi = y' x - 2h y ; compute mod 2h*d for safety via python ints on int64 chunks
    psi=np.array([[ (yp*pell(abs(i-j))[0]-2*h*pell(abs(i-j))[1]) % (2*h*d) for j in range(m)] for i in range(m)],dtype=np.int64)
    Pm=np.zeros(len(n),dtype=np.int64)
    for i in range(m):
        for j in range(m):
            Pm=(Pm+ (psi[i,j]*((n[:,i]*n[:,j])%(2*h*d)))%(2*h*d))%(2*h*d)
    W=np.prod(gh[grid],axis=1)
    units=[nu for nu in range(1,2*h,2) if math.gcd(nu,2*h)==1]
    nu0=random.Random(seed).choice(units)
    w=W*np.exp(-2j*np.pi*((nu0*Pm)%(2*h))/(2*h))
    # O/d elements beta = x + y sqrt2 ; lam = 3+2sqrt2 ; Tr(beta lam^i) mod d ; Nm(beta)=x^2-2y^2
    lam_pows=[]; a,b=1,0
    for i in range(m): lam_pows.append((a,b)); a,b=(3*a+4*b)%d,(2*a+3*b)%d   # (a+b sqrt2)(3+2sqrt2)=3a+4b + (2a+3b)sqrt2
    def Tr(x,y,a,b): return (2*(x*a+2*y*b))%d   # Tr((x+y s)(a+b s)) = 2(xa+2yb)
    Zb={}
    for x in range(d):
        for y in range(d):
            tau=np.array([Tr(x,y,*lam_pows[i]) for i in range(m)],dtype=np.int64)
            Zb[(x,y)]=np.sum(w*np.exp(2j*np.pi*((n@tau)%d)/d))
    maxerr=0
    for j in range(1,d):
        nu=nu0+(2*h//d)*j
        if math.gcd(nu,2*h)!=1: continue
        t=(j*yp)%d
        if math.gcd(t,d)!=1: continue
        Zl=np.sum(W*np.exp(-2j*np.pi*((nu*Pm)%(2*h))/(2*h)))
        G=sum(np.exp(-2j*np.pi*((t*(x*x-2*y*y))%d)/d) for x in range(d) for y in range(d))
        tb=pow(t,-1,d)
        R=G/d**2*sum(np.exp(2j*np.pi*((tb*(x*x-2*y*y))%d)/d)*Zb[(x,y)] for x in range(d) for y in range(d))
        err=abs(R-Zl)/max(1,abs(Zl)); maxerr=max(maxerr,err)
        print(f'm={m} d={d} nu0={nu0} j={j} |Z|={abs(Zl):.6g} identity rel.err={err:.1e} |G|={abs(G):.4f} main-term ratio |G Z0|/(d^2|Z|)={abs(G*Zb[(0,0)])/d**2/abs(Zl):.3f}')
    return maxerr
e1=run(5,2,41); e2=run(9,1,7); e3=run(9,1,7,seed=3)
print('MAXERR',max(e1,e2,e3))
