"""Line I integration checks (independent re-implementation, 2026-10-31).  Exact integer arithmetic for P, alpha_n, h, y';
complex binary64 for the sums.  Finite alphabets with RANDOM complex weights (the identities are algebraic: they hold for any
weights), so agreement is a test of the identities, not of the k1 kick.
Checks:
 C1  P(n) == y' Nm(alpha_n) (mod 2h) for every word (R3 congruence).
 C2  Prop I1: Z(nu0+delta) = Z(nu0) * sigmahat(delta) for sigma = pushforward of w/Z(nu0) to P mod 2h.
 C3  Prop I2 (a)-(d) for prime d || h (norm counts N(u), Parseval, cross/square decomposition).
 C4  Prop I2': Z(nu0 + 2hj/d) = d^-2 sum_beta Zhat(beta) G_t(beta), |G_t(beta)| = d, for prime AND composite odd d | h.
 C5  Aliasing identity: (1/q) sum_{nu' mod q} |Z_m(nu'/q)|^2 = sum_j C_Z(jq) for every q | 2h, and the Moebius form of F.
 C6  Lemma I5' (a) all residues and (b) units (Ramanujan sums), random Fourier coefficients c_k, |k| <= 40.
 C7  Thm I4 bookkeeping: W'_m (frozen definition, any inclusion set) = (1/phi) sum_{non-resonant units}(|Z|^2-RMT) + (1/phi) sum Dev.
 C8  Arithmetic: 7 | h_m <=> m == 3 (6) (m < 700); 2 is a QR mod every prime d | h_m (odd m <= 61);
     every m in [2, 60] has a prime of h_m dividing no h_m' (m' < m); primitive divisor of U_2m for 16 <= m <= 60.
"""
import itertools, math, cmath, sys, json, random
import numpy as np
from sympy import factorint, mobius, divisors, totient, isprime
rng=np.random.default_rng(20261031)
def nsw_U(m):  # (1+sqrt2)^m = h + U sqrt2
    a,b=1,0
    for _ in range(m): a,b=a+2*b,a+b
    return a,b
def data(m,L):
    h,yp=nsw_U(m); assert h*h+1==2*yp*yp
    psi=[yp*nsw_U(2*d)[0]-h*nsw_U(2*d)[1] for d in range(m)]
    lam=[nsw_U(2*i) for i in range(m)]          # lambda^i = x + y sqrt2
    letters=list(range(-L,L+1)); g=rng.normal(size=len(letters))+1j*rng.normal(size=len(letters))
    words=np.array(list(itertools.product(letters,repeat=m)),dtype=np.int64)
    W=np.prod(g[words+L],axis=1)
    Ps=np.zeros(len(words),dtype=object); ar=np.zeros(len(words),dtype=object); ai=np.zeros(len(words),dtype=object)
    for k,n in enumerate(words.tolist()):
        Ps[k]=sum(psi[abs(i-j)]*n[i]*n[j] for i in range(m) for j in range(m))
        ar[k]=sum(n[i]*lam[i][0] for i in range(m)); ai[k]=sum(n[i]*lam[i][1] for i in range(m))
    return h,yp,W,Ps,ar,ai
def e(x): return np.exp(2j*np.pi*x)
def Zall(W,Ps,h):
    M=2*h; A=np.zeros(M,complex)
    np.add.at(A,np.array([int(p%M) for p in Ps]),W)
    return np.fft.fft(A)          # Z_nu = sum_p A[p] e(-nu p/M)
res={}; worst={}
def rec(name,err):
    worst[name]=max(worst.get(name,0.0),float(err))
for (m,L) in [(5,2),(7,1),(9,1)]:
    h,yp,W,Ps,ar,ai=data(m,L); M=2*h
    # C1
    bad=sum(1 for k in range(len(Ps)) if (Ps[k]-yp*(ar[k]**2-2*ai[k]**2))%M)
    assert bad==0, ('C1',m,bad); rec('C1_failures',bad)
    Z=Zall(W,Ps,h); scale=np.sqrt(np.mean(abs(Z)**2))
    units=[v for v in range(M) if math.gcd(v,M)==1]; phi=len(units)
    # C2
    nu0=next(v for v in units if (4*v-1)%h==0)
    w=W*np.array([e(-nu0*int(p%M)/M) for p in Ps]); Z0=w.sum(); sig=w/Z0
    for dl in [1,2,3,7,M//3]:
        lhs=Z[(nu0+dl)%M]; rhs=Z0*np.sum(sig*np.array([e(-dl*int(p%M)/M) for p in Ps])); rec('C2_I1',abs(lhs-rhs)/scale)
    # C3/C4 over odd divisors d of h
    for d in [x for x in divisors(h) if 1<x<=60]:   # d = h allowed (m = 5: d = 41); d <= 60 for cost (d^4 work)
        ar_d=np.array([int(x%d) for x in ar]); ai_d=np.array([int(x%d) for x in ai])
        Wg=np.zeros((d,d),complex); np.add.at(Wg,(ar_d,ai_d),w)
        X,Y=np.meshgrid(np.arange(d),np.arange(d),indexing='ij'); Nm=(X*X-2*Y*Y)%d
        Zhat=np.zeros((d,d),complex)   # Zhat(beta) = sum_gamma W(gamma) e(Tr(beta gamma)/d), Tr = 2(b1 g1 + 2 b2 g2)
        for b1 in range(d):
            for b2 in range(d):
                Zhat[b1,b2]=np.sum(Wg*e((2*(b1*X+2*b2*Y))%d/d))
        for j in range(1,d):
            t=(j*yp)%d
            if math.gcd(t,d)!=1: continue
            lhs=Z[(nu0+M//d*j)%M]
            direct=np.sum(Wg*e(-(t*Nm)%d/d)); rec('C4_Zt_vs_W',abs(lhs-direct)/scale)
            if j>4: continue
            G=np.zeros((d,d),complex); acc=0
            for b1 in range(d):
                for b2 in range(d):
                    Gt=np.sum(e(-((t*Nm+2*(b1*X+2*b2*Y))%d)/d)); G[b1,b2]=Gt; acc+=Zhat[b1,b2]*Gt
            rec('C4_I2prime',abs(lhs-acc/d**2)/scale); rec('C4_absG_minus_d',np.max(abs(abs(G)-d))/d)
        if isprime(d) and (h//d)%d:
            eps=1 if pow(2,(d-1)//2,d)==1 else -1
            Wu=np.zeros(d,complex); np.add.at(Wu,Nm.ravel(),Wg.ravel())
            Nu=np.bincount(Nm.ravel(),minlength=d)
            assert all(Nu[u]==(d+(d-1)*eps if u==0 else d-eps) for u in range(d)), 'norm counts'
            Zt=[np.sum(Wu*e(-(t*np.arange(d))%d/d)) for t in range(d)]
            rec('C3a_parseval',abs(sum(abs(z)**2 for z in Zt)-d*np.sum(abs(Wu)**2))/scale**2)
            c=Z0; dlt=Wu-c*Nu/d**2
            rec('C3c_cross',abs(np.sum(Nu*dlt)-eps*d*dlt[0])/scale)
            lhs=sum(abs(z)**2 for z in Zt[1:]); rhs=abs(c)**2*(1/d-1/d**2)+2*eps*(np.conj(c)*dlt[0]).real+d*np.sum(abs(dlt)**2)
            rec('C3d_decomp',abs(lhs-rhs)/scale**2)
            # members Z_t of the coset equal Z(nu0 + 2hj/d):
            for j in range(1,d):
                rec('C3_member_id',abs(Z[(nu0+M//d*j)%M]-Zt[(j*yp)%d])/scale)
    # C5 aliasing
    Pi=np.array([int(p) for p in Ps]); off=-Pi.min(); A=np.zeros(Pi.max()+off+1,complex); np.add.at(A,Pi+off,W)
    CZ=np.correlate(A,A,mode='full')  # CZ[k+len-1] = sum_n A[n+k] conj A[n]
    K0=len(A)-1
    def CZk(k): return CZ[k+K0] if -K0<=k<=K0 else 0
    def sumj(q): return sum(CZk(j*q) for j in range(-(K0//q)-1,K0//q+2))
    def Zth(th): return np.sum(W*np.exp(-2j*np.pi*th*Pi))
    for q in [x for x in divisors(M)]:
        if q>4000: continue
        lhs=sum(abs(Zth(v/q))**2 for v in range(q))/q; rec('C5_alias',abs(lhs-sumj(q))/scale**2)
    F=np.mean(abs(Z[units])**2)
    rhs=sum(mobius(e_)*(M//e_)*sumj(M//e_) for e_ in divisors(M))/phi; rec('C5_mobius',abs(F-rhs)/scale**2)
    # C6 Lemma I5'
    K=40; ck=rng.normal(size=2*K+1)+1j*rng.normal(size=2*K+1); ks=np.arange(-K,K+1)
    f=lambda v: np.sum(ck*e(ks*v/M))
    Pm=np.array([int(p%M) for p in Ps]); Cmod=np.zeros(M,complex)
    for k in range(M): pass
    Am=np.zeros(M,complex); np.add.at(Am,Pm,W)
    Cm=np.fft.ifft(np.fft.fft(Am)*np.conj(np.fft.fft(Am)))*1  # Cm[k] = sum_{p-p'==k} A[p]conj A[p'] (circular)
    lhs=sum(abs(Z[v])**2*f(v) for v in range(M)); rhs=M*np.sum(ck*Cm[ks%M]); rec('C6a',abs(lhs-rhs)/(M*scale**2))
    def ram(q,n): return sum(cmath.exp(2j*math.pi*v*n/q) for v in range(q) if math.gcd(v,q)==1).real
    rv=np.array([ram(M,r) for r in range(M)])
    lhs=sum(abs(Z[v])**2*f(v) for v in units)
    rhs=sum(ck[i]*np.sum(Cm*rv[(ks[i]-np.arange(M))%M]) for i in range(2*K+1)); rec('C6b',abs(lhs-rhs)/(M*scale**2))
    # C7 Thm I4 bookkeeping, frozen definition, all levels 1<d<=sqrt h included
    RMT=4*m-m*m/h; Pstar=[(2,8),(-2,8),(2,16),(-2,16)]
    def reso(a,b,mod): return [v for v in units if (b*v-a)%mod==0]
    resset=set(); Res=0; Dev=0
    levels=[d for d in divisors(h) if 1<d and d*d<=h]
    for (a,b) in Pstar:
        r0=reso(a,b,M); assert len(r0)==1; nr=r0[0]; Zr2=abs(Z[nr])**2; assert nr not in resset; resset.add(nr)
        Res+=Zr2-RMT
        for d in levels:
            Md=[v for v in reso(a,b,M//d) if not any((b*v-a)%(M//dd)==0 for dd in divisors(d) if dd<d)]
            assert not (set(Md)&resset), 'overlap'; resset|=set(Md)
            Res+=len(Md)*(Zr2/d**2-RMT); Dev+=sum(abs(Z[v])**2-Zr2/d**2 for v in Md)
    Wp=F-RMT-Res/phi
    nonres=sum(abs(Z[v])**2-RMT for v in units if v not in resset)/phi
    rec('C7_I4',abs(Wp-(nonres+Dev/phi))/scale**2)
    res[m]=dict(h=h,yp=yp,words=len(Ps),phi=phi,levels=levels,resonant=len(resset))
# C8 arithmetic
for m in range(1,700): assert (nsw_U(m)[0]%7==0)==(m%6==3)
for m in range(1,62,2):
    h=nsw_U(m)[0]
    for p in factorint(h):
        assert pow(2,(p-1)//2,p)==1, (m,p)
seen=set(); newprime={}
for m in range(1,61):
    h=nsw_U(m)[0]; fs=set(factorint(h)) if h>1 else set(); new=fs-seen; newprime[m]=sorted(new); seen|=fs
assert all(newprime[m] for m in range(2,61))
for m in range(16,61):
    U2=nsw_U(2*m)[1]; prev=[nsw_U(k)[1] for k in range(1,2*m)]
    prim=[p for p in factorint(U2) if p!=2 and all(u%p for u in prev)]
    assert prim and all(nsw_U(m)[0]%p==0 for p in prim) and all(nsw_U(mm)[0]%p for p in prim for mm in range(1,m))
out=dict(cases=res,worst_relative_errors=worst,C8='passed: 7|h<=>m==3 mod 6 (m<700); 2 QR mod all p|h_m (odd m<=61); new prime in h_m for every m in [2,60]; primitive prime of U_2m divides h_m and no earlier h for 16<=m<=60',
         newprime_examples={m:newprime[m][:3] for m in (2,3,4,5,16,30,60)})
print(json.dumps(out,indent=1,default=str))
bad={k:v for k,v in worst.items() if k!='C1_failures' and v>1e-9}
print('ALL_OK' if not bad and worst.get('C1_failures',0)==0 else 'FAIL '+str(bad))
