"""m=9: ND_9 cluster check and exact Bohr mean.
B_9 = B_sym - sum_{bad C} sum_{xi in C} |Gamma xi| K(xi,xi) + sum_{bad C} avg_nu |sum_{xi in C} k_nu(xi)|^2 ,
with k_nu(xi) = sum_r e(-nu r/g') W_r(xi), W_r(xi) = D^-1 sum_{beta: class r} e(-<beta,xi>), computed only on non-dihedral clusters."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import dlib, numpy as np, math, time
import sys; m=int(sys.argv[1]) if len(sys.argv)>1 else 9; TOL=float(sys.argv[2]) if len(sys.argv)>2 else 1e-12; print("# clustering tolerance",TOL)
t0=time.time(); O=dlib.Orbits(m); D=O.D; d1,d2=O.d1,O.d2; gp=O.gp
E=dlib.e(-O.cls/gp); Kd=np.abs(np.fft.fft2(E)/D)**2; supp=Kd>1e-9*Kd.max(); Deff=int(supp.sum())
X1=O.T[0]; X2=O.T[1]
a,b=X1.copy(),X2.copy(); ra,rb=X1.copy(),(6*X1-X2)%d2; stab=np.zeros(X1.shape,np.int64)
for j in range(m):
    stab+=((a==X1)&(b==X2)); stab+=((ra==X1)&(rb==X2)); a,b=b,(6*b-a)%d2; ra,rb=rb,(6*rb-ra)%d2
orb=2*m//stab
S=O.S; Ssup=S[supp]; order=np.argsort(Ssup); Ss=Ssup[order]
brk=np.concatenate([[True],np.diff(Ss)>TOL]); cs_=np.cumsum(brk)-1; cid=np.empty_like(cs_); cid[order]=cs_; nC=cid.max()+1
csize=np.bincount(cid); corb=np.zeros(nC,int); np.maximum.at(corb,cid,orb[supp]); bad=np.where(csize!=corb)[0]
gaps=np.diff(Ss); mingap=gaps[gaps>TOL].min()
mn=np.full(nC,np.inf); mx=np.full(nC,-np.inf); np.minimum.at(mn,cid,Ssup); np.maximum.at(mx,cid,Ssup); spread=(mx-mn).max()
Bsym=float((orb*Kd)[supp].sum())
print(f'm={m} D={D} (d1,d2)=({d1},{d2}) D_eff={Deff} 2m={2*m} B_sym={Bsym:.6f} 2m-B_sym={2*m-Bsym:.6f} #xi on short orbits={int((orb[supp]<2*m).sum())} '
      f'clusters={nC} nonsym_clusters={len(bad)} max_in_cluster_spread={spread:.1e} min_gap_between_clusters={mingap:.3e} t={time.time()-t0:.0f}s',flush=True)
supidx=np.flatnonzero(supp)
badxi=[supidx[np.where(cid==c)[0]] for c in bad]
nbad=sum(len(x) for x in badxi); print(f'# xi in non-dihedral clusters: {nbad}',flush=True)
for c,idx in zip(bad,badxi):
    print('   cluster size',len(idx),'orbit sizes',sorted(set(orb.ravel()[idx].tolist())),'S=',Ssup[np.where(cid==c)[0][0]],
          'theta*d2 orders (lcm of denominators):', sorted(set(int(d2//math.gcd(d2,math.gcd(*[int(O.T[j].ravel()[i]) for j in range(m)]))) for i in idx)))
if nbad:
    b1=np.arange(d1)[:,None]; b2=np.arange(d2)[None,:]; cls=O.cls.ravel(); u=O.units()
    corr_old=0.0; corr_new=0.0
    for idx in badxi:
        ks=[]
        for i in idx:
            i1,i2=np.unravel_index(i,(d1,d2))
            ph=np.exp(-2j*np.pi*((b1*i1)%d1/d1+(b2*i2)%d2/d2)).ravel()/D
            W=np.bincount(cls,weights=ph.real,minlength=gp)+1j*np.bincount(cls,weights=ph.imag,minlength=gp)
            ks.append(np.fft.fft(W)[u])            # k_nu(xi) for all units nu
            corr_old+=orb.ravel()[i]*Kd.ravel()[i]
        ks=np.array(ks); assert np.allclose(np.abs(ks)**2, Kd.ravel()[idx][:,None], atol=1e-12)
        corr_new+=np.mean(np.abs(ks.sum(0))**2)
    B=Bsym-corr_old+corr_new
else: B=Bsym
print(f'B_m_exact={B:.6f}  B_m_sym={Bsym:.6f}  2m={2*m}  t={time.time()-t0:.0f}s',flush=True)
