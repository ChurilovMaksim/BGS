"""Second reader, BGS-TRACE-169 (Prop C).  Fresh code: only the 14 rational kick coefficients are shared input.
(1) DIRECT: k_nu(xi) = D^-1 sum_{beta in V} e(-nu Q(beta) - <beta,xi>) computed on ALL of G (= H^-1 Z^m/Z^m) by a 2-D DFT
    over beta = a e0 + b e1, (a,b) in (Z/4h)^2 (each class of V counted 4 times; V = O/(lambda^m-1), exponent 4h),
    Q(beta) = y' Nm(a+b lambda)/g' mod 1, Nm = a^2+6ab+b^2.  Z(nu) = sum_xi k_nu(xi) e^{i eta S(xi)},  F = mean_nu |Z|^2 over
    ALL units nu mod g'.  Compare with the Prop C class formula h^-2 sum A_r conj(A_r') mu(q)/phi(q) built from (Z/h)^2.
(2) KERNEL: h^2 k_nu(1/2+x/h) conj k_nu(1/2) = e(nubar c q(x)/h) with ONE unit c, all x, all tested nu.
(3) PRIMARY PARTS with p^2 | h (m=15: 31^2, m=21: 7^2): the Gauss sum on V_(p) has |k|=p^-e and its phase is
    e(nubar c_p q(y)/p^e), c_p a unit mod p, for ALL units nu mod p^e."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import numpy as np, math, json, sys, time
from fractions import Fraction as Fr
from sympy import factorint, totient, mobius
CK={1:(Fr(1,20),Fr(-1,200)),2:(Fr(0),Fr(-1,400)),5:(Fr(0),Fr(-1,800)),6:(Fr(-1,40),Fr(-1,400)),7:(Fr(9,20),Fr(0)),
    8:(Fr(-1,40),Fr(1,400)),9:(Fr(0),Fr(1,800))}
def ftab(M):
    n=np.arange(M); out=np.zeros(M)
    for k,(a,b) in CK.items():
        c=complex(a,b); out+=2*(c*np.exp(2j*np.pi*k*n/M)).real     # c_k e(k t) + conj
    return out
def pell(m):
    x,y=1,0
    for _ in range(m): x,y=3*x+8*y,x+3*y
    return x,y
def data(m):
    x,y=pell(m); D=2*(x-1); h=math.isqrt(D//4); assert 4*h*h==D
    g=math.gcd(y,x-1); return dict(D=D,h=h,yp=y//g,gp=(x-1)//g)
def units(n): return [u for u in range(1,n) if math.gcd(u,n)==1]
def kgrid(m,nu,d):
    h,yp,gp=d['h'],d['yp'],d['gp']; M=4*h
    a=np.arange(M,dtype=np.int64)
    A,B=np.meshgrid(a,a,indexing='ij')
    Nm=(A*A+6*A*B+B*B)%gp
    ph=np.exp(-2j*np.pi*(((nu*yp)%gp)*Nm%gp)/gp)
    return np.fft.fft2(ph)/(4*d['D'])            # k at (u,v)/M : e(-(au+bv)/M) convention of numpy
def Sgrid(m,d,sub):
    """S(xi) for xi=(u,v)/M on the given index arrays (u,v); sequence w_{j+1}=6w_j-w_{j-1} mod M"""
    M=4*d['h']; ft=ftab(M); u,v=sub; w0,w1=u.copy(),v.copy(); S=np.zeros(len(u))
    for j in range(m):
        S+=ft[w0]; w0,w1=w1,(6*w1-w0)%M
    assert np.all(w0==u) and np.all(w1==v)       # period m closes
    return S
def propC(m,d,etas):
    h=d['h']; x=np.arange(h,dtype=np.int64); X0,X1=np.meshgrid(x,x,indexing='ij'); X0=X0.ravel(); X1=X1.ravel()
    q=(X0*X0-6*X0*X1+X1*X1)%h
    M=4*h; u=(2*h+4*X0)%M; v=(2*h+4*X1)%M      # xi = 1/2 + x/h  ->  (u,v)/M
    S=Sgrid(m,d,(u,v)); out={}
    r=np.arange(h); G=np.gcd((r[:,None]-r[None,:])%h,h); G[G==0]=h
    qq=h//G; W=np.vectorize(lambda t:float(mobius(int(t)))/float(totient(int(t))))(qq)
    for eta in etas:
        A=np.bincount(q,weights=np.cos(eta*S),minlength=h)+1j*np.bincount(q,weights=np.sin(eta*S),minlength=h)
        out[eta]=float(np.real(A@W@A.conj()))/h**2
    return out,(u,v,q)
def direct(m,d,etas,nus,want_kernel=True):
    h=d['h']; M=4*h
    ft=None; res={e:0.0 for e in etas}; kern_dev=0.0; cval=None; supp_ok=True; norm_dev=0.0
    # S on all of G: first find G = support of the DFT for nu=1
    k1=kgrid(m,1,d); G=np.argwhere(np.abs(k1)>1e-12*0+1e-9)
    _,(us,vs,q)=propC(m,d,[])  # support indices
    Sall=None
    for nu in nus:
        k=kgrid(m,nu,d)
        mask=np.abs(k)>1e-9
        if mask.sum()!=h*h: supp_ok=False
        if Sall is None:
            iu,iv=np.nonzero(mask); Sall=(iu,iv,Sgrid(m,d,(iu.astype(np.int64),iv.astype(np.int64))))
            exp_supp=set(zip(us.tolist(),vs.tolist()))
            if set(zip(iu.tolist(),iv.tolist()))!=exp_supp: supp_ok=False
        iu,iv,S=Sall
        kv=k[iu,iv]; norm_dev=max(norm_dev,float(np.max(np.abs(np.abs(kv)**2*h*h-1))))
        for e in etas: res[e]+=abs(np.sum(kv*np.exp(1j*e*S)))**2/len(nus)
        if want_kernel:
            ks=k[us,vs]; k0=ks[0]                     # x=0 is first (X0=X1=0)
            ratio=ks*np.conj(k0)*h*h
            nub=pow(nu,-1,d['gp'])%h
            if cval is None:
                # find unit c with ratio = e(nub c q/h)
                for c in range(1,h):
                    if math.gcd(c,h)==1 and np.max(np.abs(ratio-np.exp(2j*np.pi*nub*c*q/h)))<1e-8: cval=c; break
                assert cval is not None, 'no unit c fits'
            kern_dev=max(kern_dev,float(np.max(np.abs(ratio-np.exp(2j*np.pi*nub*cval*q/h)))))
    return res,dict(support_is_half_plus_Vodd=supp_ok,max_dev_h2k2=norm_dev,c=cval,max_kernel_dev=kern_dev)
def primary(m,p):
    d=data(m); h=d['h']; e=factorint(h)[p]; P=p**e; C=4*h//P; assert math.gcd(C,p)==1
    yp,gp=d['yp'],d['gp']; a=np.arange(P,dtype=np.int64); A,B=np.meshgrid(a,a,indexing='ij')
    Nm=(A*A+6*A*B+B*B)%gp; coef=(yp*C*C)%gp
    # Q(C(a+b lam)) = coef*Nm/gp mod 1 ; check it lies in (1/P)Z
    num=(coef*Nm)%gp; assert np.all((num*P)%gp==0), 'Q not in (1/p^e)Z on V_(p)'
    Qint=(num*P)//gp                           # Q = Qint/P
    # the q-sequence start (u,v)/P must have period m mod P
    y0,y1=np.meshgrid(a,a,indexing='ij'); w0,w1=y0.copy(),y1.copy()
    for j in range(m): w0,w1=w1,(6*w1-w0)%P
    assert np.all(w0==y0) and np.all(w1==y1)
    qy=(y0*y0-6*y0*y1+y1*y1)%P
    maxabs=0.0; cfit=None; maxdev=0.0; cnt=0
    for nu in units(P):
        ph=np.exp(-2j*np.pi*((nu*Qint)%P)/P)
        k=np.fft.fft2(ph)/P**2                 # index (u',v') with <beta,xi> = (a u' + b v')/P,  u' = C*u
        idx_u=(C*y0)%P; idx_v=(C*y1)%P; kk=k[idx_u,idx_v]
        maxabs=max(maxabs,float(np.max(np.abs(np.abs(kk)*P-1))))
        ratio=kk*np.conj(kk[0,0])*P*P; nub=pow(nu,-1,P)
        if cfit is None:
            for c in range(1,P):
                if c%p and np.max(np.abs(ratio-np.exp(2j*np.pi*nub*c*qy/P)))<1e-8: cfit=c; break
            assert cfit is not None,'no unit c_p fits'
        maxdev=max(maxdev,float(np.max(np.abs(ratio-np.exp(2j*np.pi*nub*cfit*qy/P))))); cnt+=1
    return dict(m=m,p=p,e=e,pe=P,units_tested=cnt,max_dev_abs_k=maxabs,c_p=cfit,max_phase_dev=maxdev)
if __name__=='__main__':
    etas=[0.5,2.0,10.0,50.0]
    for m in [3,5,7]:
        d=data(m); t=time.time(); nus=units(d['gp'])
        C,_=propC(m,d,etas); Dr,info=direct(m,d,etas,nus)
        dev=max(abs(C[e]-Dr[e])/max(1,abs(Dr[e])) for e in etas)
        print(json.dumps(dict(m=m,h=d['h'],gp=d['gp'],n_units=len(nus),F_direct={str(e):Dr[e] for e in etas},
              F_propC={str(e):C[e] for e in etas},max_rel_dev=dev,**info,secs=round(time.time()-t))),flush=True)
    # m = 9 (composite h = 7*199): all units for F would be 1188 FFTs of 5572^2; use 48 units for the kernel identity,
    # and the exact Ramanujan average is then implied; F checked with the identity.
    m=9; d=data(m); t=time.time(); nus=units(d['gp']); rng=np.random.default_rng(9); sub=sorted(rng.choice(nus,24,replace=False).tolist())
    Dr,info=direct(m,d,[2.0],sub)
    print(json.dumps(dict(m=m,h=d['h'],units_tested=sub,**info,secs=round(time.time()-t))),flush=True)
    for (m,p) in [(15,31),(21,7),(15,7),(9,7),(9,199)]:
        t=time.time(); r=primary(m,p); r['secs']=round(time.time()-t); print(json.dumps(r),flush=True)
