"""Computer-assisted certificate (python-flint / arb ball arithmetic) for the IFS transfer operators
   (L_a phi)(s) = sum_{|n|<=L} w_a(n) e(c n s) phi((s+n)/lam),  w_a(n) = i^n J_n(0.9 eta) e(c n^2/2 + a n/8),  c = 1/(lam - 1/lam)
 on the Hardy space H^2(D_rho), orthonormal basis e_k = (s/rho)^k.  Sectors a in {0,2,4,6} (odd a have c_a = 0).
 Rigorous: delta >= ||L - P_K L P_K|| (HS tail bounds), trace-norm bound ||L||_1,
 sector 4: Householder deflation of the top Galerkin eigenvector, Neumann/resolvent bounds on two circles (no sampling):
   exactly one eigenvalue in D(b11, r1), all others in |z| <= r2;  other sectors: spectrum in |z| <= r2.
 Usage: cert.py eta L rho K prec p r1 r2 outjson"""
import sys, json, time, numpy as np
from flint import arb, acb, acb_mat, ctx
eta=sys.argv[1]; L=int(sys.argv[2]); rho_f=sys.argv[3]; K=int(sys.argv[4]); ctx.prec=int(sys.argv[5])
p=int(sys.argv[6]); r1=arb(sys.argv[7]); r2=arb(sys.argv[8]); outf=sys.argv[9]
t0=time.time()
rho=arb(rho_f); two=arb(2); sq2=two.sqrt(); lam=3+2*sq2; c=1/(lam-1/lam); pi=arb.pi()
x=arb(9)/10*arb(eta)
J={n: x.bessel_j(arb(abs(n)))*(1 if (n>=0 or n%2==0) else -1) for n in range(-L,L+1)}   # J_{-n}=(-1)^n J_n
I=acb(0,1)
def e(t): return (2*pi*I*t).exp()
def w(a,n): return (I**(n%4))*J[n]*e(c*n*n/2+arb(a*n)/8)
theta={n:(rho+abs(n))/(lam*rho) for n in range(-L,L+1)}
assert all(theta[n]<1 for n in theta), 'rho too small'
Pn={n: abs(J[n])*(2*pi*c*abs(n)*rho).exp() for n in range(-L,L+1)}
delta1=sum((Pn[n]*theta[n]**K/(1-theta[n]**2).sqrt() for n in Pn),arb(0))
Rp=2*rho; q=rho/Rp
Mk=lambda k: sum((abs(J[n])*(2*pi*c*abs(n)*Rp).exp()*((Rp+abs(n))/(lam*rho))**k for n in Pn),arb(0))
delta2=(sum((Mk(k)**2 for k in range(K)),arb(0))*q**(2*K)/(1-q*q)).sqrt()
delta=delta1+delta2
trnorm=sum((Pn[n]/(1-theta[n]) for n in Pn),arb(0))
print('delta1',delta1.mid(),'delta2',delta2.mid(),'trace-norm bound',trnorm.mid(),flush=True)
fact=[arb(1)]
for i in range(1,K+1): fact.append(fact[-1]*i)
lamp=[arb(1)]
for i in range(1,K+1): lamp.append(lamp[-1]/lam)
MC={}
for n in range(-L,L+1):
    z=2*pi*I*c*n*rho
    zp=[acb(1)]
    for i in range(1,K): zp.append(zp[-1]*z)
    M=acb_mat(K,K)
    for l in range(K):
        for j in range(l+1): M[l,j]=zp[l-j]/fact[l-j]
    Cm=acb_mat(K,K); r=arb(n)/rho
    rp=[arb(1)]
    for i in range(1,K): rp.append(rp[-1]*r)
    for k in range(K):
        for j in range(k+1): Cm[j,k]=fact[k]/(fact[j]*fact[k-j])*lamp[k]*rp[k-j]
    MC[n]=M*Cm
print('built MC',round(time.time()-t0,1),'s',flush=True)
def fro(Mx):
    s=arb(0)
    for i in range(Mx.nrows()):
        for j in range(Mx.ncols()): s+=abs(Mx[i,j])**2
    return s.sqrt()
_cache={}
def powers_bound(Y,r):
    key=id(Y)
    if key not in _cache:
        nr=[arb(1)]; P=Y
        for j in range(1,p+1):
            nr.append(fro(P))
            if j<p: P=P*Y
        _cache[key]=nr
    nr=_cache[key]; Yp=nr[p]
    if not (Yp< r**p): return None, Yp
    S=sum((nr[j]/r**(j+1) for j in range(p)),arb(0))
    return S/(1-Yp/r**p), Yp
res=dict(eta=eta,L=L,rho=rho_f,K=K,prec=ctx.prec,p=p,r1=str(r1),r2=str(r2),delta=float(delta.upper()),trace_norm=float(trnorm.upper()),sectors={})
for a in (4,0,2,6):
    A=acb_mat(K,K)
    for n in range(-L,L+1): A+=MC[n]*w(a,n)
    if a==4:
        An=np.array([[complex(A[i,j].mid()) for j in range(K)] for i in range(K)])
        ev,V=np.linalg.eig(An); i0=np.argmax(abs(ev)); v=V[:,i0]; v=v/np.linalg.norm(v)
        mu0=acb(complex(ev[i0]).real,complex(ev[i0]).imag)
        Am=acb_mat([[A[i,j].mid() for j in range(K)] for i in range(K)])
        va=acb_mat([[acb(complex(t).real,complex(t).imag)] for t in v])
        Sh=Am-acb_mat([[mu0 if i==j else 0 for j in range(K)] for i in range(K)])
        for it in range(3):
            va=Sh.solve(va); va=acb_mat([[va[i,0].mid()] for i in range(K)])
            nv=sum((abs(va[i,0])**2 for i in range(K)),arb(0)).sqrt().mid()
            va=acb_mat([[(va[i,0]/nv).mid()] for i in range(K)])
        vv=[va[i,0] for i in range(K)]
        al=-(vv[0]/abs(vv[0])).mid()
        wv_a=[vv[i]-(al if i==0 else 0) for i in range(K)]
        wv_a=[t.mid() for t in wv_a]
        nn=sum((abs(t)**2 for t in wv_a),arb(0))
        H=acb_mat(K,K)
        for i in range(K):
            for j in range(K): H[i,j]=(1 if i==j else 0)-2*wv_a[i]*wv_a[j].conjugate()/nn
        B=H*A*H
        b11=B[0,0]
        b12=(sum((abs(B[0,j])**2 for j in range(1,K)),arb(0))).sqrt()
        b21=(sum((abs(B[i,0])**2 for i in range(1,K)),arb(0))).sqrt()
        Y=acb_mat(K-1,K-1)
        for i in range(1,K):
            for j in range(1,K): Y[i-1,j-1]=B[i,j]
        F=b21+delta
        RY2,Yp=powers_bound(Y,r2)
        absb=abs(b11); rlow=absb-r1
        ok=False; d=dict(b11=str(b11),b12=float(b12.upper()),b21=float(b21.upper()),Yp_root=float((Yp**(arb(1)/p)).upper()))
        if RY2 is not None and rlow>r2:
            RY1,_=powers_bound(Y,rlow)
            R1=1/r1+b12*RY1/r1+RY1+1/rlow
            R2=1/(absb-r2)+b12*RY2/(absb-r2)+RY2+1/r2
            ok=bool(F*R1<1 and F*R2<1)
            d.update(mu_star_abs_lower=float((absb-r1).lower()),mu_star_abs_upper=float((absb+r1).upper()),RY_r2=float(RY2.upper()),
                     F_R1=float((F*R1).upper()),F_R2=float((F*R2).upper()))
        d['certified']=ok; res['sectors'][4]=d
    else:
        RA,Ap=powers_bound(A,r2)
        d=dict(Ap_root=float((Ap**(arb(1)/p)).upper()),certified=False)
        if RA is not None:
            Rt=RA+1/r2; d.update(RA_r2=float(RA.upper()),dR=float((delta*Rt).upper()),certified=bool(delta*Rt<1))
        res['sectors'][a]=d
    print('sector',a,res['sectors'][a],round(time.time()-t0,1),'s',flush=True)
    json.dump(res,open(outf,'w'),indent=1)
res['secs']=time.time()-t0; json.dump(res,open(outf,'w'),indent=1); print('done',res['secs'],flush=True)
