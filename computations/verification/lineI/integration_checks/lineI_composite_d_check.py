"""Line I integration check C4b: Prop I2' for COMPOSITE odd d | h (d = 287 = 7*41 at m = 15; d = 49 = 7^2 at m = 21), alphabet {0,1}
with random complex weights; plus |G_t(beta)| = d for every t unit, beta mod d, via the exact factorisation
G_t(beta) = g1(b1) g2(b2),  g1 = sum_x e(-(t x^2 + 2 b1 x)/d),  g2 = sum_y e(-(-2t y^2 + 4 b2 y)/d)  (Nm = x^2-2y^2, Tr = 2(b1x+2b2y))."""
import itertools, math, json, numpy as np
rng=np.random.default_rng(31102026)
def nsw_U(m):
    a,b=1,0
    for _ in range(m): a,b=a+2*b,a+b
    return a,b
def e(x): return np.exp(2j*np.pi*x)
out={}
for m,ds in [(15,[7,41,287]),(21,[7,49])]:
    h,yp=nsw_U(m); M=2*h; assert h*h+1==2*yp*yp
    psi=np.array([(yp*nsw_U(2*d)[0]-h*nsw_U(2*d)[1])%M for d in range(m)],dtype=np.int64)
    lam=[nsw_U(2*i) for i in range(m)]
    words=np.array(list(itertools.product([0,1],repeat=m)),dtype=np.int64)
    g=rng.normal(size=(m,2))+1j*rng.normal(size=(m,2))   # site-dependent random weights (identity is algebraic)
    W=np.ones(len(words),complex)
    for i in range(m): W*=g[i,words[:,i]]
    P=np.zeros(len(words),dtype=np.int64)
    for i in range(m):
        for j in range(m):
            P=(P+psi[abs(i-j)]*(words[:,i]*words[:,j]))%M
    nu0=next(v for v in range(1,M,2) if (4*v-1)%h==0)
    w=W*e(-(nu0*P%M)/M); Z0=w.sum(); scale=np.sqrt(np.sum(abs(W)**2))
    rec={}
    for d in ds:
        assert h%d==0
        ar=np.zeros(len(words),dtype=np.int64); ai=np.zeros(len(words),dtype=np.int64)
        for i in range(m): ar=(ar+words[:,i]*(lam[i][0]%d))%d; ai=(ai+words[:,i]*(lam[i][1]%d))%d
        # R3 congruence mod d
        assert np.all((P-yp*(ar*ar-2*ai*ai))%d==0)
        Wg=np.zeros((d,d),complex); np.add.at(Wg,(ar,ai),w)
        X,Y=np.meshgrid(np.arange(d),np.arange(d),indexing='ij'); Nm=(X*X-2*Y*Y)%d
        # Zhat(beta) for all beta by 2-D DFT: Zhat(b1,b2) = sum_g W(g) e((2 b1 x + 4 b2 y)/d)
        F=np.fft.ifft2(Wg)*d*d    # F[k1,k2] = sum W e(+(k1 x + k2 y)/d)
        i2=pow(2,-1,d); i4=pow(4,-1,d)
        B1,B2=np.meshgrid(np.arange(d),np.arange(d),indexing='ij')
        Zhat=F[(2*B1)%d,(4*B2)%d]
        errZ=0; errI=0; errG=0
        for j in range(1,d):
            t=(j*yp)%d
            if math.gcd(t,d)!=1: continue
            Zt=np.sum(w*e(-(((nu0+M//d*j)-nu0)*P%M)/M)) if False else np.sum(W*e(-(((nu0+M//d*j)%M)*P%M)/M))
            direct=np.sum(Wg*e(-(t*Nm%d)/d)); errZ=max(errZ,abs(Zt-direct)/scale)
            xs=np.arange(d)
            g1=np.array([np.sum(e(-((t*xs*xs+2*b*xs)%d)/d)) for b in range(d)])
            g2=np.array([np.sum(e(-((-2*t*xs*xs+4*b*xs)%d)/d)) for b in range(d)])
            G=np.outer(g1,g2); errG=max(errG,np.max(abs(abs(G)-d))/d)
            errI=max(errI,abs(Zt-np.sum(Zhat*G)/d**2)/scale)
        rec[d]=dict(Zt_vs_W=errZ,I2prime=errI,absG_minus_d=errG)
    out[m]=dict(h=h,words=len(words),checks=rec)
print(json.dumps(out,indent=1,default=str))
ok=all(v<1e-9 for c in out.values() for r in c['checks'].values() for v in r.values())
print('ALL_OK' if ok else 'FAIL')
