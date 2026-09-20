"""High-precision check of a cancelling third-derivative identity.

Double precision can lose the answer after subtracting two large terms.
Generate the unitary via a Cayley transform at working precision instead
of promoting an approximately unitary double-precision input.
"""
import json
import random
import mpmath as mp


def check(n,dps):
    mp.mp.dps=dps
    rng=random.Random(183+n)
    H=mp.zeros(n)
    for j in range(n):
        H[j,j]=mp.mpf(rng.randrange(-6,7))/n
        for k in range(j):
            H[j,k]=mp.mpc(rng.randrange(-6,7),rng.randrange(-6,7))/n
            H[k,j]=H[j,k].conjugate()
    V=(mp.eye(n)+1j*H)*(mp.eye(n)-1j*H)**-1
    lam=[(1+1j*mp.mpf((j+1)**2)/n)/(1-1j*mp.mpf((j+1)**2)/n)
         for j in range(n)]
    U=V*mp.diag(lam)*V.H
    A=mp.matrix(n*n,n*n)
    for j in range(n*n):
        for k in range(n*n):
            A[j,k]=U[j//n,k//n]*U[j%n,k%n].conjugate()
    ip=[j*(n+1) for j in range(n)]
    iq=[j for j in range(n*n) if j not in ip]
    sub=lambda rows,cols:mp.matrix([[A[j,k] for k in cols] for j in rows])
    a,b,c,d=sub(ip,ip),sub(ip,iq),sub(iq,ip),sub(iq,iq)
    R=(mp.eye(len(iq))-d)**-1
    X=R*R*R*c
    F2=2*b*X
    F3=6*b*d*R*X
    B=mp.matrix([[abs(V[j,k])**2 for k in range(n)] for j in range(n)])
    D=B*B.T
    H1=mp.zeros(n)
    Hs=mp.zeros(n)
    mass=mp.mpf('0.7')/n
    for j in range(n):
        for k in range(n):
            if j==k:continue
            v=mp.matrix([V[x,j]*V[x,k].conjugate() for x in range(n)])
            gap2=abs(1-lam[j]*lam[k].conjugate())**2
            H1+=v*v.H/gap2
            Hs+=v*v.H/(mass**2+gap2)
    recovered=D*(F2*D*F2/4-F3/6)*D
    err=mp.norm(recovered-H1)/mp.norm(H1)
    hermitian_err=mp.norm((F2+F2.H)/2-(D**-2-D**-1))/mp.norm(D**-2-D**-1)
    r=mp.exp(-2*mp.asinh(mass/2))
    return_f=r*a+r*r*b*(mp.eye(len(iq))-r*d)**-1*c
    compressed=(mp.eye(n)-return_f)**-1
    regularized=(compressed+compressed.H-mp.eye(n))/(1/r-r)-D/mass**2
    regularized_err=mp.norm(regularized-Hs)/mp.norm(Hs)
    assert err<mp.mpf(10)**(-dps//2)
    assert hermitian_err<mp.mpf(10)**(-dps//2)
    assert regularized_err<mp.mpf(10)**(-dps//2)
    return dict(n=n,dps=dps,inverse_gap_relative=mp.nstr(err,8),
                hermitian_second_relative=mp.nstr(hermitian_err,8),
                regularized_resolvent_relative=mp.nstr(regularized_err,8))


if __name__=='__main__':
    print(json.dumps([check(n,80) for n in (2,3,5,8)],indent=2))
