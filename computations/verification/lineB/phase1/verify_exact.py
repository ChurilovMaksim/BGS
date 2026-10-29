"""(1) Exact rational identity  2 n^T H^{-1} n = (2 y_m/D_m) Nm(alpha_n) + beta(n),  beta(n) = -2 sum_{i<j} n_i n_j y_{j-i}
    (alpha_n = sum n_j lambda^j, Nm(a+b lam)=a^2+6ab+b^2), checked with Fractions for random n, m=1..12.
(2) Exact finite-N trace formula (Theorem 1, exact form), gcd(N,D_m)=1:
    Tr U_N^m / Tr M_N^m = sum_{n in Z^m} Phihat(n) e(Q(n)/N) e(-nu y' Nm(alpha_n)/g'),  nu = N^{-1} mod g'
    checked against brute-force quantum traces (eigenvalues) for m=1,2,3 at many N and eta."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import dlib, numpy as np, math, random, sympy
from fractions import Fraction as Fr
random.seed(1)
print('== (1) rational identity ==')
for m in range(1,13):
    H=sympy.Matrix(m,m,lambda i,j: (6 if i==j else 0) - (1 if (j-i)%m==1 else 0) - (1 if (i-j)%m==1 else 0)) if m>2 else (sympy.Matrix([[4]]) if m==1 else sympy.Matrix([[6,-2],[-2,6]]))
    Hi=H.inv(); D=dlib.Dm(m); xs,ys=dlib.pell(m); assert H.det()==D
    ok=0
    for trial in range(200):
        n=sympy.Matrix([random.randint(-12,12) for _ in range(m)])
        lhs=2*(n.T*Hi*n)[0]
        # alpha_n in basis (1,lam): lam^j = (-y_{j-1}, y_j) with y_{-1}=-1
        a=sum(n[j]*(-(ys[j-1] if j>=1 else -1)) for j in range(m)); b=sum(n[j]*ys[j] for j in range(m))
        Nm=a*a+6*a*b+b*b
        beta=-2*sum(n[i]*n[j]*ys[j-i] for i in range(m) for j in range(i+1,m))
        rhs=sympy.Rational(2*ys[m],D)*Nm+beta
        ok+= (sympy.simplify(lhs-rhs)==0)
    print(f'm={m} D_m={D} det H={H.det()} identity holds in {ok}/200 random trials')
print('== (2) exact finite-N formula vs quantum ==')
def exact_sum(N,m,eta,thr=1e-14):
    n,gh=dlib.ghat(eta); s=np.abs(gh)>thr; n=n[s]; gh=gh[s]
    xs,ys=dlib.pell(m); D=dlib.Dm(m); gp,yp=dlib.gprime(m); nu=pow(N,-1,gp)
    lamj=[(-(ys[j-1] if j>=1 else -1), ys[j]) for j in range(m)]
    grids=np.meshgrid(*([n]*m),indexing='ij'); W=np.ones(grids[0].shape,complex)
    for j in range(m): W=W*gh[np.searchsorted(n,grids[j])] if False else W
    idx=np.meshgrid(*([np.arange(len(n))]*m),indexing='ij'); W=np.ones(idx[0].shape,complex)
    for j in range(m): W=W*gh[idx[j]]
    nn=[n[idx[j]].astype(np.int64) for j in range(m)]
    a=sum(nn[j]*lamj[j][0] for j in range(m)); b=sum(nn[j]*lamj[j][1] for j in range(m))
    Nm=(a*a+6*a*b+b*b)
    beta=np.zeros(a.shape,np.int64)
    for i in range(m):
        for j in range(i+1,m): beta+= -2*nn[i]*nn[j]*ys[j-i]
    Q=(2*ys[m]/D)*Nm.astype(float)+beta.astype(float)
    ph=np.exp(2j*np.pi*Q/N)*np.exp(-2j*np.pi*((nu*yp*(Nm%gp))%gp)/gp)
    return np.sum(W*ph)
for eta in [0.3,1.0,2.5]:
    for N in [15,21,25,33,35,45,61,77,101,143,155,201]:
        res=dlib.trace_ratio_quantum(N,[1,2,3],eta)
        for m in [1,2,3]:
            if math.gcd(N,dlib.Dm(m))!=1: continue
            if m==3 and eta>2: thr=1e-10
            else: thr=1e-14 if m<3 else 1e-11
            zq=res[m][0]/res[m][1]; zs=exact_sum(N,m,eta,thr)
            print(f'eta={eta} N={N} m={m} |TrM^m|={abs(res[m][1]):.12f} quantum={zq:.10f} exact_sum={zs:.10f} |diff|={abs(zq-zs):.2e}',flush=True)
