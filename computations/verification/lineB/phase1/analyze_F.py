"""Exact limit objects for the FIXED diagonal kick:
 F_m(eta)=avg_{nu unit mod g'}|Z_m(nu)|^2  (= lim of N-averaged |Tr U_N^m|^2, Theorem 2),
 B_sym = sum_xi |Orb(xi)| K(xi,xi)  (Bohr mean if no accidental orbit-sum coincidences, Theorem 4),
 coincidence check, Bohr mean by direct eta-averaging, moments of Z (distribution over nu)."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import dlib, numpy as np, math, sys, time
mmax=int(sys.argv[1]) if len(sys.argv)>1 else 8
kick=sys.argv[2] if len(sys.argv)>2 else 'actual'
ck=dict(dlib.CK)
if kick=='real':   # parity-symmetrised control: c_k -> Re c_k (f even)
    ck={k:complex(c.real,0) for k,c in ck.items()}
print('# kick =',kick, ' coefficients', {k:(round(c.real,6),round(c.imag,6)) for k,c in ck.items() if k>0})
LT=np.array([[0,1],[-1,6]]); SigT=np.array([[1,0],[6,-1]])
for m in range(1,mmax+1):
    t0=time.time()
    O=dlib.Orbits(m,ck); D=O.D; d1,d2=O.d1,O.d2
    E=dlib.e(-1*O.cls/O.gp); k1=np.fft.fft2(E)/D; Kd=np.abs(k1)**2   # K(xi,xi), nu-independent (checked)
    supp=Kd>1e-12*Kd.max(); Deff=supp.sum()
    # dual coordinates of xi: X=(X1,X2) mod d2 numerators; recover from T[0],T[1]: theta_0=X1, theta_1=X2 (L^T e: (a,b)->(b,-a+6b))
    X1=O.T[0].astype(np.int64); X2=O.T[1].astype(np.int64) if m>1 else ((-O.T[0]+6*O.T[0])%d2)
    # orbit size via stabilizer count in dihedral group <L^T, Sig^T>; act on (theta_0,theta_1)-coordinates:
    # xi determined by (theta_0,theta_1) for m>=2 (theta_{j+1}=6theta_j-theta_{j-1}); shift: (t0,t1)->(t1,6t1-t0); reversal: (t0,t1)->(t0,t_{-1})=(t0,6t0-t1)
    if m==1:
        orb=np.ones_like(X1)  # single point orbits; reversal trivial
    else:
        a,b=X1.copy(),X2.copy(); stab=np.zeros(X1.shape,np.int64)
        ra,rb=X1.copy(),(6*X1-X2)%d2
        for j in range(m):
            stab+=((a==X1)&(b==X2)); stab+=((ra==X1)&(rb==X2))
            a,b=b,(6*b-a)%d2; ra,rb=rb,(6*rb-ra)%d2
        orb=2*m//stab
    Bsym=float((orb*Kd)[supp].sum())
    # coincidence check: distinct dihedral orbits (in support) with equal S
    S=O.S[supp]; ob=orb[supp]
    Ss=np.sort(S); gaps=np.diff(Ss)
    # cluster S values with tol; each cluster must have size == orbit size
    tol=1e-9
    brk=np.concatenate([[True],gaps>tol]); cid=np.cumsum(brk)-1
    csize=np.bincount(cid); 
    # orbit size of members of each cluster
    order=np.argsort(S); obs=ob[order]
    cl_orb=np.zeros(len(csize)); np.maximum.at(cl_orb,cid,obs)
    bad=(csize!=cl_orb).sum()
    nontriv=gaps[gaps>tol]; mingap=nontriv.min() if len(nontriv) else np.nan
    # F at several eta, distribution moments over nu
    out=[]
    for eta in [0.25,0.5,1,2,4,8]:
        F,Z=O.F(eta); u=O.units(); z=Z[u]; M4=np.mean(np.abs(z)**4)/F**2
        out.append(f'eta={eta}: F={F:.4f} F/2m={F/(2*m):.3f} M4/M2^2={M4:.2f}')
    # direct Bohr mean check: average F over eta uniform in [0,T], many samples (deterministic grid)
    T=2000.0; etas=np.linspace(T/2,T,400)
    Fb=np.mean([O.F(x)[0] for x in etas]) if m<=6 else np.nan
    print(f'm={m} D={D} SNF=({d1},{d2}) g\'={O.gp} D_eff={Deff} D_eff*Kd={Kd[supp].max()*Deff:.6f} Bsym={Bsym:.6f} 2m={2*m} '
          f'clusters={len(csize)} bad_clusters={bad} min_nonzero_gap={mingap:.3e} Bohr(eta in[{T/2},{T}],400pts)={Fb:.4f} t={time.time()-t0:.1f}s',flush=True)
    for s in out: print('    ',s,flush=True)
