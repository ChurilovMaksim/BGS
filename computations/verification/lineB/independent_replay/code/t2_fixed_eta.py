"""Fixed-eta second moment F_m(eta)=avg_nu |Z(nu)|^2, its parity decomposition, and the nu-distribution, odd m.
Own implementation from the definitions: SNF coordinates of G and V, CRT split V = V_2 + V_odd (orthogonality asserted),
k_nu = (2-part factor) x (odd-part Gauss sum via FFT).  For m<=9 also a full-G FFT cross-check of F (no split)."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys, numpy as np, math, time
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__))); from core import *
def ks_exp(x):
    x=np.sort(x); n=len(x); c=1-np.exp(-x)
    return max(np.max(np.arange(1,n+1)/n-c), np.max(c-np.arange(n)/n))
def run(m, etas, fullcheck=False):
    t0=time.time(); M=Model(m); D=M.D; h=math.isqrt(D)//2; assert 4*h*h==D
    e=M.e; assert sorted(e)==[h,4*h]; i4=e.index(4*h); ih=1-i4
    L=4*h
    # odd part coords: s[i4]=4*t1, s[ih]=t2 ; 2-part: s[i4]=h*u, s[ih]=0
    t1,t2=np.meshgrid(np.arange(h,dtype=np.int64),np.arange(h,dtype=np.int64),indexing='ij')
    def seq_num(j,s4,sh):   # numerator over L of xi_j for SNF coords (s4 mod 4h, sh mod h)
        a=M.Vxi[j][i4]%L; b=M.Vxi[j][ih]%L
        return (a*s4 + b*4*sh)%L      # xi_j = a*s4/(4h) + b*sh/h
    # find 2-part support element: xi2 = 1/2*1 ?
    half=[u for u in range(4) if all(seq_num(j,h*u,0)==L//2 for j in range(m))]
    assert len(half)==1; u0=half[0]
    # quadratic form: Q(b)=2 b^T A b / D;  beta coords b4 (mod 4h), bh (mod h)
    A=M.A
    def Qnum(b4,bh):
        B={i4:b4, ih:bh}
        return sum((B[a]*B[b]%D)*(2*A[a][b]%D) for a in (0,1) for b in (0,1))%D
    # orthogonality checks of the CRT split on a sample
    rng=np.random.default_rng(0)
    for _ in range(200):
        c1,c2,u=int(rng.integers(h)),int(rng.integers(h)),int(rng.integers(4))
        assert (Qnum(4*c1+h*u,c2)-Qnum(4*c1,c2)-Qnum(h*u,0))%D==0
    # 2-part kernel factor k2(nu, xi2) = 1/4 sum_{u'} e(-nu Q(h u') - u' * u * h*h/(4h))  (beta.xi = b4*s4/(4h))
    def k2(nu,u):
        return sum(np.exp(-2j*np.pi*(nu*Qnum(h*w,0)%D/D + (h*w)*(h*u)/(4*h))) for w in range(4))/4
    for nu in M.units[:20]:
        vals=[abs(k2(nu,u)) for u in range(4)]
        assert abs(vals[u0]-1)<1e-12 and all(vals[u]<1e-12 for u in range(4) if u!=u0)
    # odd-part levels: Q(beta_o) for beta=(4c1, c2): values in (1/h)Z
    Qo=np.zeros((h,h),dtype=np.int64)
    c1,c2=t1,t2
    Qo=((4*c1)*(4*c1)%D*(2*A[i4][i4]%D) + 2*((4*c1)*c2%D)*(2*A[i4][ih]%D) + (c2*c2%D)*(2*A[ih][ih]%D))%D
    assert np.all(Qo%(4*h)==0); lev=(Qo//(4*h))%h     # Q = lev/h
    del Qo, c1, c2
    # sequences on the support xi = 1/2*1 + odd(t1,t2)
    S=np.zeros((h,h)); Sn=np.zeros((h,h)); ft=ftab(L)
    first=[]; nums=[]
    for j in range(m):
        nj=(seq_num(j,h*u0,0)+seq_num(j,4*t1,t2))%L
        S+=ft[nj]; Sn+=ft[(-nj)%L]
        nums.append(nj.astype(np.int16 if L<32767 else np.int32))
    nums=np.array(nums)
    # x_j = h*(xi_j - 1/2): check recursion & map to (x0,x1)
    rows=np.arange(0,h,max(1,h//50))
    X=((h*(2*nums[:,rows,:].astype(np.int64)-L))//(2*L))%h
    assert np.all((X[2:]-6*X[1:-1]+X[:-2])%h==0); del X
    # orbit data: stabilizer size and parity relation (-xi in Gamma xi)
    code=lambda a,b: a.astype(np.int64)*L+b.astype(np.int64)
    c0=code(nums[0],nums[1]); cneg=code((-nums[0])%L,(-nums[1])%L)
    stab=np.zeros((h,h),dtype=np.int16); par=np.zeros((h,h),dtype=bool)
    for k in range(m):
        rot=code(nums[k%m],nums[(k+1)%m]); ref=code(nums[k%m],nums[(k-1)%m])
        stab+= (rot==c0); stab+=(ref==c0)
        par|=(rot==cneg)|(ref==cneg)
    del nums
    del c0,cneg,t1,t2
    orb=(2*m//stab).astype(np.int16); nbad=int(np.sum((stab>1)|par)); del stab
    deficit=int(np.sum(2*m-orb.astype(np.int64)))
    Bsym=2*m-deficit/h**2
    print(f'm={m} h={h} D={D} units(mod 2h)={len(M.units)} deficit={deficit} Bsym={Bsym:.6f} #(nontriv stab or -xi in Gamma xi)={nbad} (<= 2m h = {2*m*h})',flush=True)
    good=~par
    units_h=[v for v in range(1,h) if math.gcd(v,h)==1]
    for eta in etas:
        chi=0j; Wpar=0j
        for r0 in range(0,h,512):
            sl=slice(r0,r0+512); d=np.exp(1j*eta*(S[sl]-Sn[sl]))
            chi+=d.sum(); Wpar+=np.sum((orb[sl]*good[sl])*d)
        chi/=h**2; Wpar/=h**2
        import scipy.fft as sfft
        Fh=sfft.fft2(np.exp(1j*eta*S),overwrite_x=True,workers=8)   # sum_t Phi e(-(a t1 + c2 t2)/h): need freq a = 4c1 mod h
        Fh=Fh[(4*np.arange(h))%h,:]
        Lv=np.bincount(lev.ravel(),weights=Fh.real.ravel(),minlength=h)+1j*np.bincount(lev.ravel(),weights=Fh.imag.ravel(),minlength=h)
        del Fh
        # inner(nu) = h^-2 sum_lev e(-nu lev/h) Lv ;  Z(nu) = k2(nu,u0) * inner
        nus=np.array(M.units)
        inner=np.concatenate([np.exp(-2j*np.pi*(np.outer(nus[i:i+1000]%h,np.arange(h))%h)/h)@Lv for i in range(0,len(nus),1000)])/h**2
        Z=np.array([k2(int(nu),u0) for nu in nus])*inner
        a2=np.abs(Z)**2; F=a2.mean()
        M4=np.mean(a2**2)/F**2; M6=np.mean(a2**3)/F**3; EZ2=abs(np.mean(Z**2))/F; KS=ks_exp(a2/F)
        Wrest=F-Bsym-Wpar; E=Wpar-2*m*chi
        line=(f'  eta={eta:7.2f} F={F:.6f} F/2m={F/2/m:.4f} chi={chi.real:+.6f}{chi.imag:+.1e}i Wpar/2m={Wpar.real/2/m:+.4f} '
              f'|E|={abs(E):.2e}(bound {4*m*m/h:.2e}) Wrest/2m={Wrest.real/2/m:+.4f} M4={M4:.3f} M6={M6:.3f} |EZ2|/F={EZ2:.3f} KS={KS:.4f} (5%crit {1.358/math.sqrt(len(nus)):.4f})')
        if fullcheck:
            seq,Q,LL=M.grids()
            ftL=ftab(LL); Sfull=np.zeros(Q.shape)
            for j in range(m): Sfull+=ftL[seq[j]]
            Ph=np.fft.fftn(np.exp(1j*eta*Sfull)); lvl=(Q*M.gp//D)%M.gp
            Lf=np.bincount(lvl.ravel(),weights=Ph.real.ravel(),minlength=M.gp)+1j*np.bincount(lvl.ravel(),weights=Ph.imag.ravel(),minlength=M.gp)
            Zf=np.exp(-2j*np.pi*np.outer(nus,np.arange(M.gp))/M.gp)@Lf/D
            line+=f' | fullG F={np.mean(np.abs(Zf)**2):.6f} max|Z-Zfull|={np.max(np.abs(Zf-Z)):.1e}'
        print(line,flush=True)
    print(f'  time {time.time()-t0:.0f}s',flush=True)
if __name__=='__main__':
    ms=[int(x) for x in sys.argv[1].split(',')]; etas=[float(x) for x in sys.argv[2].split(',')]
    full=len(sys.argv)>3
    for m in ms: run(m,etas,full)
