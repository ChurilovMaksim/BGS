# N4: copy of bgs-lineF/code/cert_lift.py with multiplier coefficient cc -> c0/2 = |C| for the (+-2,16) families (|C| = 4*2*c0/16).
# Only the abs-majorant error terms (delta1, delta2, Delta, Xnorm) are used; run with empty sector list.
"""Line F: rigorous (arb ball arithmetic) spectral certificate for the FULL-ALPHABET lifted transfer operators
  vertex (typ V):  (L Phi)_c(s) = sum_{n in Z} w_a(n) e(cc n s) Phi_{c'}((s+n)/lam),  c in Z, c' = round((c+n)/lam), disc D(c,rho)
  edge   (typ E):  same, c in Z+1/2 (pair (c-1/2,c+1/2)), transition only if round((c+1/2+n)/lam) = round((c-1/2+n)/lam)+1,
                   c' = round((c-1/2+n)/lam)+1/2, disc D(c,rho)
 on the weighted Hilbert direct sum  ||Phi||^2 = sum_c om(c)^2 ||Phi_c||^2_{H^2(D(c,rho))},  om(c) = exp(-beta (|c|-Rc)_+).
 w_a(n) = i^n J_n(0.9 eta) e(cc n^2/2 + a n/8),  cc = 1/(lam-1/lam).  ALL n in Z are accounted for (explicit |n|<=Nmax, Bessel tail bound beyond).
 Decomposition L = A (core<-core, Galerkin) + X (far<-core) + Delta (everything else: big letters into core rows, far<-far, rows |c|>Rmax).
 Comparison operator T0' = [[H T0 H (+) 0, 0],[X, 0]] (block lower triangular, spec = spec(T0) u {0}).
 Usage: cert_lift.py typ eta K0 rho K beta prec p r1 r2 Nmax Rmax sectors out.json"""
import sys, json, time, math
import numpy as np
from flint import arb, acb, acb_mat, ctx
typ=sys.argv[1]; eta=sys.argv[2]; K0=int(sys.argv[3]); rho_s=sys.argv[4]; K=int(sys.argv[5]); beta_s=sys.argv[6]
ctx.prec=int(sys.argv[7]); p=int(sys.argv[8]); r1=arb(sys.argv[9]); r2=arb(sys.argv[10]); Nmax=int(sys.argv[11]); Rmax=int(sys.argv[12])
sectors=[int(t) for t in sys.argv[13].split(',') if t]; outf=sys.argv[14]
t0=time.time()
two=arb(2); lam=3+2*two.sqrt(); cc=1/(lam-1/lam)/2; pi=arb.pi(); I=acb(0,1)
rho=arb(rho_s); beta=arb(beta_s); x=arb(9)/10*arb(eta)
half=arb(1)/2
Rc = arb(K0) if typ=='V' else arb(K0)-half
def e(t): return (2*pi*I*t).exp()
J={n: x.bessel_j(arb(abs(n)))*(1 if (n>=0 or n%2==0) else -1) for n in range(-Nmax,Nmax+1)}
W={n: abs(J[n]) for n in J}
def wa(a,n): return (I**(n%4))*J[n]*e(cc*n*n/2+arb(a*n)/8)
def certfloor(y):
    f=math.floor(float(y.mid())); assert (y-f)>0 and (y-f)<1, 'floor not certified'; return f
def rnd(t): return certfloor(t+half)
def target(c2,n):
    """c2 = 2*center (int). returns (c2', delta) or None."""
    if typ=='V':
        j=rnd(arb(c2//2+n)/lam); return 2*j, arb(c2//2+n)/lam-j
    lo=(c2-1)//2; j=rnd(arb(lo+n)/lam); j2=rnd(arb(lo+1+n)/lam)
    if j2!=j+1: return None
    return 2*j+1, arb(c2,)/2/lam+arb(n)/lam-(arb(2*j+1)/2)
def om(c2): 
    d=abs(arb(c2)/2)-Rc
    return (-beta*d).exp() if d>0 else arb(1)
iscore=lambda c2: abs(arb(c2)/2)<=Rc
Mn=lambda n,R: (2*pi*cc*abs(n)*R).exp()
thstar = (half/rho+1/lam) if typ=='V' else (half/lam/rho+1/lam)
# Bessel tail: sum_{|n|>Nmax} |J_n| e^{alpha|n|} <= 2 t^{N+1}/(N+1)! /(1-t/(N+2)), t=x e^alpha/2
def btail(alpha):
    t=x*alpha.exp()/2; N=Nmax; f=arb(1)
    for i in range(1,N+2): f*=i
    q=t/(N+2); assert q<1
    return 2*t**(N+1)/f/(1-q)
cores=[c2 for c2 in range(-2*K0-2,2*K0+3) if (c2%2==(0 if typ=='V' else 1)) and iscore(c2)]
idx={c2:i for i,c2 in enumerate(cores)}; nc=len(cores); D=nc*K
print('typ',typ,'cores',[c/2 for c in cores],'dim',D,flush=True)
# ---------- core blocks (exact Galerkin sections), delta1, delta2, Delta1 rows, trace norm of core rows
fact=[arb(1)]
for i in range(1,K+1): fact.append(fact[-1]*i)
lamp=[arb(1)]
for i in range(1,K+1): lamp.append(lamp[-1]/lam)
Rp=2*rho; q=rho/Rp
blocks={}   # (c2,n) -> (j2, matrix)
col_tail={c2:arb(0) for c2 in cores}   # delta1 per input component (Minkowski sum)
d2acc={}    # (c2,j2) -> list over l of sums
Del_rows={} # row c2 -> Delta row sum (operator-norm b_n)
X_rows={}
Tn=arb(0)   # trace-norm bound total
for c2 in cores:
    Del_rows[c2]=arb(0)
    for n in range(-Nmax,Nmax+1):
        tg=target(c2,n)
        if tg is None: continue
        j2,dl=tg; th=abs(dl)/rho+1/lam; assert th<1
        bn=W[n]*Mn(n,rho)/(1-th*th).sqrt(); tn=W[n]*Mn(n,rho)/(1-th)
        ratio=om(c2)/om(j2)
        Tn+=ratio*tn
        if not iscore(j2):
            Del_rows[c2]+=ratio*bn; continue
        # Galerkin block: output basis ((s-c)/rho)^i, input ((u-c')/rho)^l ; tau = sig/lam + dl/rho
        z=2*pi*I*cc*n*rho; zp=[acb(1)]
        for i in range(1,K): zp.append(zp[-1]*z)
        M=acb_mat(K,K)
        for l in range(K):
            for jj in range(l+1): M[l,jj]=zp[l-jj]/fact[l-jj]
        Cm=acb_mat(K,K); B=dl/rho; bp=[arb(1)]
        for i in range(1,K): bp.append(bp[-1]*B)
        for k in range(K):
            for jj in range(k+1): Cm[jj,k]=fact[k]/(fact[jj]*fact[k-jj])*lamp[jj]*bp[k-jj]
        ph=e(cc*n*arb(c2)/2)
        blocks[(c2,n)]=(j2,(M*Cm)*ph)
        col_tail[j2]+=W[n]*Mn(n,rho)*th**K/(1-th*th).sqrt()
        key=(c2,j2)
        if key not in d2acc: d2acc[key]=[arb(0)]*K
        g=(abs(dl)+Rp/lam)/rho; Mr=W[n]*Mn(n,Rp)
        d2acc[key]=[d2acc[key][l]+Mr*g**l for l in range(K)]
    # n-tail for core rows: |c'|<=(|c|+|n|)/lam+1/2 ; ratio<=exp(beta((|c|+|n|)/lam+1/2-Rc)_+) <= exp(beta(|c|/lam+1/2)) e^{beta|n|/lam}
    al=2*pi*cc*rho+beta/lam
    tailfac=(beta*(abs(arb(c2)/2)/lam+half)).exp()
    Del_rows[c2]+=tailfac*btail(al)/(1-thstar*thstar).sqrt()
    Tn+=tailfac*btail(al)/(1-thstar)
delta1=sum((col_tail[c]**2 for c in cores),arb(0)).sqrt()
delta2=(sum((sum((v**2 for v in L_),arb(0)) for L_ in d2acc.values()),arb(0))*q**(2*K)/(1-q*q)).sqrt()
delta=delta1+delta2
print('delta1',delta1.mid(),'delta2',delta2.mid(),'blocks',len(blocks),round(time.time()-t0,1),'s',flush=True)
# ---------- far rows Rc<|c|<=Rmax : X (into core) and Delta
lat=[c2 for c2 in range(-2*Rmax,2*Rmax+1) if (c2%2==(0 if typ=='V' else 1)) and not iscore(c2)]
for c2 in lat:
    X_rows[c2]=arb(0); Del_rows[c2]=arb(0)
    for n in range(-Nmax,Nmax+1):
        tg=target(c2,n)
        if tg is None: continue
        j2,dl=tg; th=abs(dl)/rho+1/lam
        bn=W[n]*Mn(n,rho)/(1-th*th).sqrt(); tn=W[n]*Mn(n,rho)/(1-th)
        ratio=om(c2)/om(j2); Tn+=ratio*tn
        if iscore(j2): X_rows[c2]+=ratio*bn
        else: Del_rows[c2]+=ratio*bn
    # n-tail: ratio <= om(c) * exp(beta((|c|+|n|)/lam+1/2-Rc)_+) <= om(c) exp(beta(|c|/lam+1/2)) e^{beta|n|/lam}
    al=2*pi*cc*rho+beta/lam
    tailfac=om(c2)*(beta*(abs(arb(c2)/2)/lam+half)).exp()
    Del_rows[c2]+=tailfac*btail(al)/(1-thstar*thstar).sqrt(); Tn+=tailfac*btail(al)/(1-thstar)
# rows |c|>Rmax, analytic: ratio <= e^{-beta(|c|-Rc)} + e^{-beta|c|(1-1/lam)+beta/2} e^{beta|n|/lam}  (Rc>=0)
B0=sum((W[n]*Mn(n,rho) for n in J),arb(0))+btail(2*pi*cc*rho)
B1=sum((W[n]*Mn(n,rho)*(beta*abs(n)/lam).exp() for n in J),arb(0))+btail(2*pi*cc*rho+beta/lam)
g1=beta; g2=beta*(1-1/lam)
cmin=arb(Rmax)+half     # every lattice point beyond Rmax has |c|>=Rmax+1/2
def geo(g,pw): # sum over lattice |c|>=cmin (both signs, spacing 1) of e^{-pw g |c|}
    return 2*(-pw*g*cmin).exp()/(1-(-pw*g).exp())
far2 = 2*( (g1*Rc).exp()**2*geo(g1,2)*B0**2 + (beta).exp()*geo(g2,2)*B1**2 )/(1-thstar*thstar)
farT = ((g1*Rc).exp()*geo(g1,1)*B0 + (beta/2).exp()*geo(g2,1)*B1)/(1-thstar)
Delta=(sum((v**2 for v in Del_rows.values()),arb(0))+far2).sqrt()
Xn=(sum((v**2 for v in X_rows.values()),arb(0))).sqrt()
Tn=Tn+farT
print('Delta rows',{k/2:float(v.mid()) for k,v in Del_rows.items() if float(v.mid())>1e-12})
print('Delta',Delta.mid(),'||X||',Xn.mid(),'trace-norm',Tn.mid(),'far2',far2.mid(),round(time.time()-t0,1),'s',flush=True)
res=dict(typ=typ,eta=eta,K0=K0,rho=rho_s,K=K,beta=beta_s,prec=ctx.prec,p=p,r1=str(r1),r2=str(r2),Nmax=Nmax,Rmax=Rmax,
         delta1=float(delta1.upper()),delta2=float(delta2.upper()),Delta=float(Delta.upper()),Xnorm=float(Xn.upper()),trace_norm=float(Tn.upper()),sectors={})
def fro(Mx):
    s=arb(0)
    for i in range(Mx.nrows()):
        for j in range(Mx.ncols()): s+=abs(Mx[i,j])**2
    return s.sqrt()
def powers(Y):
    nr=[arb(1)]; P=Y
    for j in range(1,p+1):
        nr.append(fro(P))
        if j<p: P=P*Y
    return nr
def neumann(nr,r):
    Yp=nr[p]
    if not (Yp< r**p): return None
    S=sum((nr[j]/r**(j+1) for j in range(p)),arb(0))
    return S/(1-Yp/r**p)
def full_R(Rcore,zabs):   # resolvent of T0' from core resolvent bound (includes zero block on (I-P) core and far part)
    Rc_=Rcore if Rcore>1/zabs else 1/zabs
    Rc_=max(Rcore,1/zabs) if False else (Rcore+1/zabs)   # safe: max<=sum
    return Rc_*(1+Xn/zabs)+1/zabs
Pert=delta+Delta
for a in sectors:
    A=acb_mat(D,D); agg={}
    for (c2,n),(j2,Mx) in blocks.items():   # aggregate per (c,c') pair with C-level matrix ops (no entry skipped)
        key=(c2,j2); term=Mx*wa(a,n)
        agg[key]=term if key not in agg else agg[key]+term
    for (c2,j2),S in agg.items():
        i0=idx[c2]*K; j0=idx[j2]*K
        for i in range(K):
            for j in range(K): A[i0+i,j0+j]=S[i,j]
    d=dict(certified=False)
    if typ=='V' and a==4:
        An=np.array([[complex(A[i,j].mid()) for j in range(D)] for i in range(D)])
        ev,V=np.linalg.eig(An); i0=np.argmax(abs(ev)); v=V[:,i0]; v=v/np.linalg.norm(v)
        mu0=acb(complex(ev[i0]).real,complex(ev[i0]).imag)
        Am=acb_mat([[A[i,j].mid() for j in range(D)] for i in range(D)])
        va=acb_mat([[acb(complex(t).real,complex(t).imag)] for t in v])
        Sh=Am-acb_mat([[mu0 if i==j else 0 for j in range(D)] for i in range(D)])
        for it in range(3):
            va=Sh.solve(va); va=acb_mat([[va[i,0].mid()] for i in range(D)])
            nv=sum((abs(va[i,0])**2 for i in range(D)),arb(0)).sqrt().mid()
            va=acb_mat([[(va[i,0]/nv).mid()] for i in range(D)])
        vv=[va[i,0] for i in range(D)]
        al_=-(vv[0]/abs(vv[0])).mid()
        wv_a=[(vv[i]-(al_ if i==0 else 0)).mid() for i in range(D)]
        nn=sum((abs(t)**2 for t in wv_a),arb(0))
        H=acb_mat(D,D)
        for i in range(D):
            for j in range(D): H[i,j]=(1 if i==j else 0)-2*wv_a[i]*wv_a[j].conjugate()/nn
        B=H*A*H
        b11=B[0,0]
        b12=(sum((abs(B[0,j])**2 for j in range(1,D)),arb(0))).sqrt()
        b21=(sum((abs(B[i,0])**2 for i in range(1,D)),arb(0))).sqrt()
        Y=acb_mat(D-1,D-1)
        for i in range(1,D):
            for j in range(1,D): Y[i-1,j-1]=B[i,j]
        nr=powers(Y); RY2=neumann(nr,r2)
        absb=abs(b11); rlow=absb-r1
        F=b21+Pert
        d.update(b11=str(b11),b12=float(b12.upper()),b21=float(b21.upper()),Yp_root=float((nr[p]**(arb(1)/p)).upper()))
        if RY2 is not None and rlow>r2:
            RY1=neumann(nr,rlow)
            # core resolvent of T0=[[b11,b12],[0,Y]] on |z-b11|=r1 (|z|>=rlow) and |z|=r2 (|z-b11|>=|b11|-r2)
            R1=full_R(1/r1+b12*RY1/r1+RY1, rlow)
            R2=full_R(1/(absb-r2)+b12*RY2/(absb-r2)+RY2, r2)
            d.update(mu_abs_lower=float((absb-r1).lower()),mu_abs_upper=float((absb+r1).upper()),RY_r2=float(RY2.upper()),
                     F_R1=float((F*R1).upper()),F_R2=float((F*R2).upper()),certified=bool(F*R1<1 and F*R2<1))
    else:
        nr=powers(A); RA=neumann(nr,r2)
        d.update(Ap_root=float((nr[p]**(arb(1)/p)).upper()))
        if RA is not None:
            R2=full_R(RA,r2); d.update(RA_r2=float(RA.upper()),F_R2=float((Pert*R2).upper()),certified=bool(Pert*R2<1))
    res['sectors'][a]=d
    print('sector',a,d,round(time.time()-t0,1),'s',flush=True)
    json.dump(res,open(outf,'w'),indent=1)
res['secs']=time.time()-t0; json.dump(res,open(outf,'w'),indent=1); print('done',res['secs'],flush=True)
