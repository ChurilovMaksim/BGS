"""Independent exact Gaussian-rational occupation sums; numerical norm checks."""
from fractions import Fraction as F
from itertools import product
from math import factorial, sqrt
import json
import numpy as np

Z=(F(0),F(0)); ONE=(F(1),F(0))
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[0],-a[1])
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def conj(a): return (a[0],-a[1])
def sc(a,q): return (a[0]*q,a[1]*q)
def fl(a): return complex(float(a[0]),float(a[1]))
def norm2(a): return a[0]**2+a[1]**2
def mm(A,B):
    n=len(A); return [[sum((A[i][k]*B[k][j] for k in range(n)),F(0)) for j in range(n)] for i in range(n)]
def cc(U): return np.array([[fl(a) for a in row] for row in U])
def house(n):
    vs=[(F(1),F(0)),(F(1),F(1)),(F(2),F(-1)),(F(1),F(2))][:n]
    d=sum(map(norm2,vs),F(0)); ph=[ONE,(F(0),F(1)),(F(3,5),F(4,5)),(F(-1),F(0))]
    return [[mul(ph[i],add(ONE if i==j else Z,sc(mul(vs[i],conj(vs[j])),-F(2)/d))) for j in range(n)] for i in range(n)]
def occupations(U,m):
    n=len(U); out={}
    for x in product(range(n),repeat=m):
        v=ONE
        for k in range(m): v=mul(v,U[x[k]][x[(k+1)%m]])
        occ=tuple(x.count(a) for a in range(n))
        out.setdefault(occ,[Z for a in range(n)])
        out[occ][x[0]]=add(out[occ][x[0]],v)
    return out
def covariance(dic,n):
    S=[[Z for j in range(n)] for i in range(n)]
    for d in dic.values():
        for i in range(n):
            for j in range(n): S[i][j]=add(S[i][j],mul(d[i],conj(d[j])))
    return S
def trace_poly(dic):
    return {k:sumg(v) for k,v in dic.items()}
def sumg(xs):
    v=Z
    for x in xs: v=add(v,x)
    return v
def pmixed(P,Q,R):
    out=Z
    for a,x in P.items():
        for b,y in Q.items():
            c=tuple(i+j for i,j in zip(a,b))
            if c in R: out=add(out,mul(mul(x,y),conj(R[c])))
    return out

results=[]
for n in (3,4):
    U=house(n); un=cc(U); assert np.linalg.norm(un@un.conj().T-np.eye(n))<1e-14
    P=[[norm2(U[i][j]) for j in range(n)] for i in range(n)]
    C=float(n*max(max(row) for row in P)); pn=np.array(P,dtype=float); J=np.ones((n,n))/n
    rho=float(np.linalg.norm(pn-J,2)); Q=un*un.T.conj(); r=float(np.linalg.norm(Q,2))
    powers=[[[F(int(i==j)) for j in range(n)] for i in range(n)]]
    dic={}; traces={}
    for m in range(1,7):
        powers.append(mm(powers[-1],P)); dic[m]=occupations(U,m); traces[m]=trace_poly(dic[m])
        S=covariance(dic[m],n); sn=cc(S)
        assert all(S[i][j]==conj(S[j][i]) for i in range(n) for j in range(n))
        L=[[sum((powers[u][i][j]*powers[m-u][j][i] for u in range(m)),F(0)) for j in range(n)] for i in range(n)]
        ln=np.array(L,dtype=float); err=float(np.linalg.norm(sn-ln,2))
        if m==1:
            assert S==[[(P[i][i],F(0)) if i==j else Z for j in range(n)] for i in range(n)]
            bound=0.
        else:
            e=factorial(m)*(C**(m-1)*r+C**(m-.5)/sqrt(n)+m*(m-1)*C**m/n)
            bound=e/n; assert err<=bound+1e-12
            # Test centered Green-Kubo and transformed coherence bounds separately.
            pi=np.eye(n)-J; R=np.linalg.inv(np.eye(n)-pn+J); H=R+R.T-np.eye(n)
            k=m*(C-1)*rho**(m-2)+2*rho**m/(1-rho)
            assert np.linalg.norm(n*pi@sn@pi-pi@H@pi,2)<=e+k+1e-10
            assert np.linalg.norm(n*(np.eye(n)-pn)@sn@(np.eye(n)-pn.T)-(np.eye(n)-pn@pn.T),2)<=(1+rho)**2*(e+k)+1e-10
            if m==2:
                expected=Z
                for a in range(n):
                    for b in range(n): expected=add(expected,sc(mul(mul(U[a][a],U[b][b]),conj(mul(U[a][b],U[b][a]))),F(2)))
                expected=add(expected,(-sum((norm2(U[a][a])**2 for a in range(n)),F(0)),F(0)))
                assert pmixed(traces[1],traces[1],traces[2])==expected
                # Exact two-cycle repeated-occupation correction.
                assert all(S[i][j]==((L[i][j]-P[i][i]**2 if i==j else L[i][j]),F(0)) for i in range(n) for j in range(n))
            else:
                for u in range(1,m): assert abs(fl(pmixed(traces[u],traces[m-u],traces[m])))<=e+1e-10
        results.append(dict(N=n,m=m,exact_paths=n**m,occupation_classes=len(dic[m]),norm_error=err,theorem_bound=bound))
def div(a,b): return sc(mul(a,conj(b)),F(1)/norm2(b))
def gp(a,k):
    if k<0: return gp(conj(a),-k)
    v=ONE
    for _ in range(k): v=mul(v,a)
    return v

# A separate exact Ward check, from the raw Hessian/cotangent formula.
n=3; basis=house(n); w=[[norm2(basis[a][j]) for a in range(n)] for j in range(n)]
G=[[sum((w[j][a]*w[k][a] for a in range(n)),F(0)) for k in range(n)] for j in range(n)]
E=[[G[j][k]-F(1+int(j==k),n+1) for k in range(n)] for j in range(n)]
lam=[ONE,(F(0),F(1)),(F(3,5),F(4,5))]; I=(F(0),F(1)); ward=[]
def pp(k): return sumg(gp(a,k) for a in lam)
def we(r,s): return sumg(sc(mul(gp(lam[j],r),gp(lam[k],s)),E[j][k]) for j in range(n) for k in range(n))
for m in range(1,7):
    p=pp(m); pc=pp(-m); raw=Z
    for j in range(n):
        for k in range(n):
            hess=sc(add(mul(gp(lam[j],m),gp(lam[k],-m)),mul(gp(lam[k],m),gp(lam[j],-m))),F(m*m))
            if j==k: hess=add(hess,sc(add(mul(gp(lam[j],m),pc),mul(gp(lam[j],-m),p)),-F(m*m)))
            raw=add(raw,sc(hess,E[j][k]/2))
            if j!=k:
                grad=sc(mul(I,add(mul(add(gp(lam[j],m),neg(gp(lam[k],m))),pc),neg(mul(add(gp(lam[j],-m),neg(gp(lam[k],-m))),p)))),F(m))
                cot=mul(I,div(add(lam[j],lam[k]),add(lam[j],neg(lam[k]))))
                raw=add(raw,sc(mul(cot,grad),E[j][k]/4))
    reduced=sc(we(m,-m),F(m*m))
    for u in range(1,m):
        reduced=add(reduced,sc(add(mul(pc,we(u,m-u)),mul(p,we(-u,-m+u))),-F(m,2)))
    assert raw==reduced,(m,raw,reduced)
    ward.append(dict(m=m,exact_equal=True))
print(json.dumps({'arithmetic':'Exact Gaussian rational coefficients; floating operator norms only','checks':results,'raw_Ward_hessian_cotangent_checks':ward,'status':'pass'},indent=2))
