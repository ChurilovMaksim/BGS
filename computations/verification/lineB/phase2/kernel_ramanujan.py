"""Prop K check: D_eff*K(xi,xi') in {mu(q)/phi(q): q | g'} (Ramanujan-sum structure of the arithmetic kernel)."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from p2lib import *
rng=np.random.default_rng(1)
for m in range(2,8):
    O,supp=support_data(m); Deff=int(supp.sum()); idx=np.flatnonzero(supp)
    sel=idx if len(idx)<=400 else rng.choice(idx,400,replace=False)
    u,k=k_all_units(O,sel)
    K=(k.T@k.conj())/len(u)*Deff                        # D_eff*K on sel x sel
    allowed=np.array(sorted({mobius(q)/phi(q) for q in range(1,O.gp+1) if O.gp%q==0}))
    dist=np.min(np.abs(K.real.ravel()[:,None]-allowed[None,:]),axis=1)
    # also check: k_nu(xi)*conj k_nu(xi') = e(nu^{-1} t)/D_eff for a single t in (1/g')Z (test via nu -> its inverse)
    inv=np.array([pow(int(v),-1,O.gp) for v in u]); i,j=0,1
    r=k[:,i]*k[:,j].conj()*Deff
    # find t: r(nu) = e(t*inv(nu)/g')
    ts=[t for t in range(O.gp) if np.allclose(r, np.exp(2j*np.pi*t*inv/O.gp), atol=1e-9)]
    print(f'm={m} g\'={O.gp} D_eff={Deff} pairs={K.size} max|Im K|={np.abs(K.imag).max():.1e} max dist to {{mu(q)/phi(q)}}={dist.max():.1e} '
          f'values={sorted(set(np.round(K.real.ravel(),6)))[:8]} ; pair(0,1): k k*·D_eff = e(t·nu^-1/g\') with t={ts}',flush=True)
