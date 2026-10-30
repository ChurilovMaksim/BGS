"""Auditor's independent library (no author code imported)."""
import numpy as np, subprocess, os, math, itertools
from fractions import Fraction
from scipy.special import jv
HERE=os.path.dirname(os.path.abspath(__file__))
LAM=3+2*math.sqrt(2)
def pell(d):                     # S^d = [[x,4y],[2y,x]]
    x,y=1,0
    for _ in range(d): x,y=3*x+8*y,x+3*y
    return x,y
def data(m):
    xm,ym=pell(m); g=math.gcd(ym,xm-1); yp,gp=ym//g,(xm-1)//g
    D=2*(xm-1); h=math.isqrt(D//4); assert 4*h*h==D and gp==2*h
    return dict(m=m,xm=xm,ym=ym,yp=yp,gp=gp,h=h,D=D)
def nustar(m,sign=1):
    d=data(m); h=d['h']; nu=(-sign*pow(4,-1,h))%h
    if nu%2==0: nu+=h
    return nu
# kicks: f(q) real trig poly given by dict k->c_k
K1={1:0.45,-1:0.45}
def fullkick():
    r=lambda k:{0:1.0,1:.5,-1:.5,7:-.5,-7:-.5,6:-.25,-6:-.25,8:-.25,-8:-.25}.get(k,0.0)
    C={}
    for k in range(-9,10):
        v=(0.5 if k in(7,-7) else 0)+r(k)/10+(r(k-1)-r(k+1))/(200j)-(0.1 if k==0 else 0)
        if abs(v)>0: C[k]=complex(v)
    return C
def fvals(C,q):
    q=np.asarray(q,float); out=np.zeros(q.shape,complex)
    for k,c in C.items(): out+=c*np.exp(2j*np.pi*k*q)
    return out.real
def ghat(C,eta,L=2048):
    th=np.arange(L)/L; c=np.fft.fft(np.exp(1j*eta*fvals(C,th)))/L
    n=np.fft.fftfreq(L,1/L).astype(int); return dict(zip(n.tolist(),c.tolist()))
def classes(C,eta,m,threads=8):
    d=data(m); h=d['h']; tab=np.exp(1j*eta*fvals(C,0.5+np.arange(h)/h)).astype(np.complex128)
    tf=f'/tmp/aud_tab_{os.getpid()}.bin'; of=f'/tmp/aud_out_{os.getpid()}.bin'; tab.tofile(tf)
    subprocess.run([os.path.join(HERE,'classes'),str(m),str(h),tf,of],check=True,env=dict(os.environ,OMP_NUM_THREADS=str(threads)))
    T=np.fromfile(of,np.complex128); os.remove(tf); os.remove(of); return T
def Zabs2_all(T,m):
    """|Z(nu)|^2 for every unit nu mod g'=2h, from class sums: |Z|^2 = h^-2 |sum_r e(v r/h) T(r)|^2, v = -16bar nubar y'bar mod h"""
    d=data(m); h=d['h']; gp=d['gp']; yp=d['yp']
    S=np.fft.ifft(T)*h            # S[v] = sum_r T[r] e(v r/h)
    out={}
    for nu in range(1,gp,2):
        if math.gcd(nu,gp)!=1: continue
        v=(-pow(16,-1,h)*pow(nu,-1,h)*pow(yp,-1,h))%h
        out[nu]=abs(S[v])**2/h**2
    return out
def nsum_Z(C,eta,m,nu,L):
    """Brute force Line-B n-sum Z_m(nu) = sum_{|n_j|<=L} Phihat(n) e(-nu y' Nm(alpha_n)/g') (TRACE-163 Thm 1), exact integer phases"""
    d=data(m); gp,yp=d['gp'],d['yp']; G=ghat(C,eta)
    vals=np.arange(-L,L+1); g=np.array([G.get(int(v),0) for v in vals])
    X=np.array([[pell(abs(i-j))[0] for j in range(m)] for i in range(m)],dtype=object)
    tot=0j
    # iterate over first m-1 coords in chunks via numpy int64 (safe: |Nm| <= m^2 L^2 x_m)
    Xi=np.array([[pell(abs(i-j))[0] for j in range(m)] for i in range(m)],dtype=np.int64)
    grid=np.array(list(itertools.product(range(2*L+1),repeat=m-1)),dtype=np.int64)
    for last in range(2*L+1):
        nv=np.concatenate([vals[grid],np.full((len(grid),1),vals[last])],axis=1)
        Nm=np.einsum('ki,ij,kj->k',nv,Xi,nv)
        ph=((-nu*yp*Nm)%gp)/gp
        tot+=np.sum(np.prod(g[np.concatenate([grid,np.full((len(grid),1),last)],axis=1)],axis=1)*np.exp(2j*np.pi*ph))
    return tot
def mobius(n):
    r=1;p=2
    while p*p<=n:
        if n%p==0:
            n//=p
            if n%p==0: return 0
            r=-r
        p+=1
    return -r if n>1 else r
def totient(n):
    r=n;p=2;k=n
    while p*p<=k:
        if k%p==0:
            while k%p==0:k//=p
            r-=r//p
        p+=1
    if k>1:r-=r//k
    return r
