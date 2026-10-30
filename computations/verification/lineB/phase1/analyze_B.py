"""Exact Bohr mean B_m = sum_{S-clusters C} avg_{nu unit mod g'} |sum_{xi in C} k_nu(xi)|^2, B_sym, coincidence structure.
usage: analyze_B.py mmax kick(actual|real)"""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import dlib, numpy as np, math, sys, time
mmax=int(sys.argv[1]); kick=sys.argv[2]
ck=dict(dlib.CK)
if kick=='real': ck={k:complex(c.real,0) for k,c in ck.items()}
print('# kick',kick)
for m in range(1,mmax+1):
    t0=time.time(); O=dlib.Orbits(m,ck); D=O.D; d1,d2=O.d1,O.d2
    E=dlib.e(-O.cls/O.gp); Kd=np.abs(np.fft.fft2(E)/D)**2; supp=Kd>1e-9*Kd.max(); Deff=int(supp.sum())
    X1=O.T[0]; X2=O.T[1] if m>1 else O.T[0]
    if m==1: orb=np.ones_like(X1)
    else:
        a,b=X1.copy(),X2.copy(); ra,rb=X1.copy(),(6*X1-X2)%d2; stab=np.zeros(X1.shape,np.int64)
        for j in range(m):
            stab+=((a==X1)&(b==X2)); stab+=((ra==X1)&(rb==X2)); a,b=b,(6*b-a)%d2; ra,rb=rb,(6*rb-ra)%d2
        orb=2*m//stab
    S=O.S; Ssup=S[supp]
    # clusters by S (tol)
    order=np.argsort(Ssup); Ss=Ssup[order]; brk=np.concatenate([[True],np.diff(Ss)>1e-9]); cid_sorted=np.cumsum(brk)-1
    cid=np.empty_like(cid_sorted); cid[order]=cid_sorted; nC=cid.max()+1
    csize=np.bincount(cid); corb=np.zeros(nC,int); np.maximum.at(corb,cid,orb[supp])
    bad=np.where(csize!=corb)[0]
    gaps=np.diff(Ss); mingap=gaps[gaps>1e-9].min() if (gaps>1e-9).any() else np.nan
    maxin=0.0
    # within-cluster spread
    spread=np.zeros(nC); mn=np.full(nC,np.inf); mx=np.full(nC,-np.inf); np.minimum.at(mn,cid,Ssup); np.maximum.at(mx,cid,Ssup); spread=(mx-mn).max()
    Bsym=float((orb*Kd)[supp].sum())
    # exact Bohr mean over clusters, all units nu
    u=O.units(); acc=0.0
    for nu in u:
        k=(np.fft.fft2(dlib.e(-nu*O.cls/O.gp))/D)[supp]
        cs=np.bincount(cid,weights=k.real,minlength=nC)+1j*np.bincount(cid,weights=k.imag,minlength=nC)
        acc+=np.sum(np.abs(cs)**2)
    B=acc/len(u)
    # small-orbit deficit
    nsmall=int((orb[supp]<2*m).sum())
    print(f'm={m} D={D} D_eff={Deff} 2m={2*m} B_exact={B:.6f} B_sym={Bsym:.6f} 2m-B_sym={2*m-Bsym:.6f} #xi on short orbits={nsmall} '
          f'clusters={nC} nonsym_clusters={len(bad)} max_in_cluster_spread={spread:.1e} min_gap_between_clusters={mingap:.3e} sqrtD={math.sqrt(D):.1f} t={time.time()-t0:.1f}s',flush=True)
    if 0<len(bad)<=6:
        for c in bad:
            mem=np.where(cid==c)[0]; idx=np.flatnonzero(supp)[mem]
            print('   nonsym cluster size',len(mem),'orbit sizes',orb.ravel()[idx][:8],'S=',Ssup[mem][:3])
            # theta sequences of first two members of different orbits
            for i in idx[:1]:
                i1,i2=np.unravel_index(i,(d1,d2)); print('     theta*d2 seq',[int(O.T[j][i1,i2]) for j in range(m)],'d2=',d2)
            others=[i for i in idx if orb.ravel()[i]>0]
            seqs=set()
            for i in idx:
                i1,i2=np.unravel_index(i,(d1,d2)); s=tuple(int(O.T[j][i1,i2]) for j in range(m))
                can=min(min(s[r:]+s[:r] for r in range(m)), min((s[::-1])[r:]+(s[::-1])[:r] for r in range(m)))
                seqs.add(can)
            for s in list(seqs)[:4]: print('     orbit class',s)
