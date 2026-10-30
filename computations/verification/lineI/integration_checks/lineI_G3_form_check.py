"""Line I owner-audit check (PR #60, item 6): the Line G G3 form of the dilation identity (BGS-TRACE-204), derived from Prop I2'
(BGS-TRACE-212) by completing the square, checked against brute force for prime and composite odd d | h_m.
For t a unit mod d, tbar = t^-1 mod d, beta = b1 + b2 sqrt2, Nm = x^2 - 2y^2, Tr(beta gamma) = 2(b1 x + 2 b2 y):
 (S) completing the square:   G_t(beta) = e(tbar Nm(beta)/d) G_d(t),  G_t(beta) = sum_gamma e(-(t Nm gamma + Tr beta gamma)/d),
                               G_d(t) = G_t(0) = sum_gamma e(-t Nm gamma/d)  (checked for EVERY beta mod d);
 (G3) Z_m(nu0 + 2hj/d) = (G_d(t)/d^2) sum_{beta mod d} e(tbar Nm(beta)/d) Zhat(beta),
      Zhat(beta) = sum_n w(n) e(Tr(beta alpha_n)/d),  w(n) = Phihat(n) e(-nu0 P(n)/2h),  t = j y' mod d,
 LHS by brute force over all words directly from P(n) = sum psi(|i-j|) n_i n_j (psi(k) = y' x_k - 2h y_k), random site-dependent
 complex weights, random unit nu0; |G_d(t)| = d. Conventions are those of computations/verification/lineG/code/check_dilution.py.
NEGATIVE CONTROL (expected FAIL): the same G3 sum with the sign of the phase flipped, e(-tbar Nm(beta)/d), is evaluated for every
(m, d, j); its error must be large (> 1e-3) in every case, otherwise the check is not discriminating and the run reports FAIL."""
import itertools, math, json, numpy as np
rng=np.random.default_rng(20261031)
def nsw_U(m):
    a,b=1,0
    for _ in range(m): a,b=a+2*b,a+b
    return a,b
def e(x): return np.exp(2j*np.pi*x)
CASES=[(5,(0,1,2),[41]),(7,(-1,0,1),[239]),(9,(-1,0,1),[7,199,1393]),(11,(0,1),[23,353]),(13,(0,1),[79,599]),
       (15,(0,1),[7,31,41,217,287,961,1271]),(21,(0,1),[7,49,1673])]
NJ=8   # number of unit j tested per d (all of them when fewer)
out={}; worst=dict(S=0.0,G3=0.0,absG=0.0); negctl_min=float('inf')
for m,alph,ds in CASES:
    h,yp=nsw_U(m); M=2*h; assert h*h+1==2*yp*yp
    psi=np.array([(yp*nsw_U(2*k)[0]-h*nsw_U(2*k)[1])%M for k in range(m)],dtype=np.int64)
    lam=[nsw_U(2*i) for i in range(m)]
    A=np.array(alph,dtype=np.int64)
    words=A[np.array(list(itertools.product(range(len(A)),repeat=m)),dtype=np.int64)]
    g=rng.normal(size=(m,len(A)))+1j*rng.normal(size=(m,len(A)))
    W=np.ones(len(words),complex)
    for i in range(m): W*=g[i,np.searchsorted(A,words[:,i])]
    P=np.zeros(len(words),dtype=np.int64)
    for i in range(m):
        for j in range(m):
            P=(P+psi[abs(i-j)]*((words[:,i]*words[:,j])%M))%M
    units=[v for v in range(1,M,2) if math.gcd(v,M)==1]
    nu0=int(units[rng.integers(len(units))])
    w=W*e(-(nu0*P%M)/M); scale=np.sqrt(np.sum(abs(W)**2))
    rec={}
    for d in ds:
        assert h%d==0 and d%2==1
        ar=np.zeros(len(words),dtype=np.int64); ai=np.zeros(len(words),dtype=np.int64)
        for i in range(m): ar=(ar+words[:,i]*(lam[i][0]%d))%d; ai=(ai+words[:,i]*(lam[i][1]%d))%d
        Wg=np.zeros((d,d),complex); np.add.at(Wg,(ar,ai),w)
        F=np.fft.ifft2(Wg)*d*d                      # F[k1,k2] = sum W(x,y) e((k1 x + k2 y)/d)
        B1,B2=np.meshgrid(np.arange(d),np.arange(d),indexing='ij')
        Zhat=F[(2*B1)%d,(4*B2)%d]                   # e(Tr(beta gamma)/d) = e((2 b1 x + 4 b2 y)/d)
        NmB=(B1*B1-2*B2*B2)%d
        js=[j for j in range(1,d) if math.gcd((j*yp)%d,d)==1 and math.gcd((nu0+M//d*j)%M,M)==1]
        if len(js)>NJ: js=sorted(rng.choice(js,NJ,replace=False).tolist())
        xs=np.arange(d); eS=eG3=eA=0.0; eN=0.0
        for j in js:
            t=(j*yp)%d; tb=pow(t,-1,d)
            g1=np.array([np.sum(e(-((t*xs*xs+2*b*xs)%d)/d)) for b in range(d)])
            g2=np.array([np.sum(e(-((-2*t*xs*xs+4*b*xs)%d)/d)) for b in range(d)])
            Gb=np.outer(g1,g2); Gd=Gb[0,0]
            eS=max(eS,np.max(abs(Gb-e((tb*NmB%d)/d)*Gd))/d); eA=max(eA,abs(abs(Gd)-d)/d)
            Zt=np.sum(W*e(-(((nu0+M//d*j)%M)*P%M)/M))
            R=Gd/d**2*np.sum(e((tb*NmB%d)/d)*Zhat)
            eG3=max(eG3,abs(Zt-R)/scale)
            Rneg=Gd/d**2*np.sum(e((-tb*NmB%d)/d)*Zhat)   # negative control: flipped sign
            eN=max(eN,abs(Zt-Rneg)/scale)
        rec[d]=dict(js=js,completing_square=eS,G3_form=eG3,absGd_minus_d=eA,negctl_flipped_sign_G3_err=eN,negctl_result='FAIL (expected)' if eN>1e-3 else 'PASS (unexpected)')
        negctl_min=min(negctl_min,eN)
        worst['S']=max(worst['S'],eS); worst['G3']=max(worst['G3'],eG3); worst['absG']=max(worst['absG'],eA)
    out[m]=dict(h=h,nu0=nu0,alphabet=list(alph),words=len(words),checks=rec)
print(json.dumps(dict(cases=out,worst=worst,negctl_min_err_over_cases=negctl_min),indent=1,default=str))
print('NEGATIVE CONTROL (flipped sign e(-tbar Nm beta/d)): FAIL as expected, min error over all (m,d) = %.3g' % negctl_min if negctl_min>1e-3 else 'NEGATIVE CONTROL UNEXPECTEDLY PASSED (min error %.3g)' % negctl_min)
ok=all(v<1e-9 for v in worst.values()) and negctl_min>1e-3
print('ALL_OK' if ok else 'FAIL')
