"""Structure checks for odd m <= 9 from the raw definitions: support, |k|^2, k(-xi)=k(xi), Prop K/C kernel values,
B^sym / Theorem D deficits, Lemma F reflection fixed points."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys, numpy as np, math, time
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__))); from core import *
from sympy import factorint, mobius, totient
def run(m,nu_sample=12,seed=1):
    t0=time.time(); M=Model(m); seq,Q,L=M.grids(); D=M.D; e=M.e
    h=math.isqrt(D)//2; assert 4*h*h==D
    print(f'm={m} D={D} e={e} h={h} gprime={M.gp} (2h={2*h}) #units={len(M.units)}')
    # Q in (1/g')Z ?
    assert np.all((Q*M.gp)%D==0); 
    rng=np.random.default_rng(seed); nus=rng.choice(M.units,size=min(nu_sample,len(M.units)),replace=False)
    pts=seq.reshape(m,-1).T   # each row: xi_j*L
    # predicted support: h*xi_j = 1/2 mod 1  <=> numerator*h mod L == L/2
    pred=np.all((pts*h)%L==L//2,axis=1)
    ks=[]
    for nu in nus:
        k=np.fft.fftn(np.exp(-2j*np.pi*(nu*Q%D)/D))/D     # fft: sum_b a_b e(-b.s/e)
        k=k.reshape(-1); ks.append(k)
        a2=np.abs(k)**2*h*h
        supp=a2>0.5
        assert np.all(np.abs(a2[supp]-1)<1e-8) and np.all(a2[~supp]<1e-8)
        assert np.array_equal(supp,pred), 'support != 1/2+V_odd'
    print('  support = 1/2*1 + V_odd for all sampled nu; |k|^2 = 1/h^2 = 1/D_eff on it  [OK]')
    # index map xi -> -xi, and Gamma action, on full G via hashing of sequences
    negk=lambda k: np.roll(np.flip(k.reshape(tuple(e)),axis=tuple(range(len(e)))),1,axis=tuple(range(len(e)))).reshape(-1)  # s -> -s mod e
    sg=np.stack(np.meshgrid(*[np.arange(ei) for ei in e],indexing='ij')).reshape(len(e),-1)
    for k in ks: assert np.allclose(k,negk(k),atol=1e-12)
    # sanity: negk really maps xi -> -xi (check on sequences)
    ii=np.arange(0,len(pts),max(1,len(pts)//1000)); nn=negk(np.arange(len(pts)))[ii]
    assert np.all((pts[ii]+pts[nn])%L==0)
    print('  k_nu(-xi) = k_nu(xi)  [OK]')
    sidx=np.nonzero(pred)[0]
    # orbits
    orb_size={}; deficit=0; seen=set()
    refl_fix=[0]*m
    sub0=pts[sidx]
    for g in range(2*m):
        img=np.roll(sub0,g%m,axis=1) if g<m else np.roll(sub0[:,::-1],g%m,axis=1)
        deficit+=0
        if g==0: stab=np.zeros(len(sidx),dtype=np.int64)
        stab+=np.all(img==sub0,axis=1)
    deficit=int(np.sum(2*m-2*m//stab))
    # Lemma F: reflection fixing vertex 0: xi_j = xi_{-j}
    sub=pts[sidx]; rev=sub[:,(-np.arange(m))%m]
    refl0=int(np.sum(np.all(sub==rev,axis=1)))
    # Theorem D closed form
    H=lambda d: math.isqrt(hm(d))//2
    def a(d): return sum(mobius(d//c)*H(c)**2 for c in range(1,d+1) if d%c==0)
    def b(d): return sum(mobius(d//c)*H(c) for c in range(1,d+1) if d%c==0)
    TD=sum(2*(m-d)*a(d)+d*d*b(d) for d in range(1,m+1) if m%d==0)
    print(f'  direct deficit sum(2m-|Gamma xi|) over S = {deficit}; Theorem D closed form = {TD}; ratio deficit/h^2 / (m^2/h) = {deficit/h/m/m:.5f}')
    print(f'  reflection fixing a vertex: {refl0} fixed points on S (Lemma F predicts h_m = {h})')
    Bsym=2*m-deficit/h**2
    # Prop K / C: K(xi,xi') = avg_nu k k'^*  vs  mu(q)/phi(q)/h^2 with q = h/gcd(r-r',h), r = x0^2-6x0x1+x1^2
    P=min(400,len(sidx)); pick=rng.choice(len(sidx),size=P,replace=False)
    allk=[]
    for nu in M.units:
        k=np.fft.fftn(np.exp(-2j*np.pi*(nu*Q%D)/D)).reshape(-1)[sidx[pick]]/D; allk.append(k)
    allk=np.array(allk)
    # x coordinates: x_j = h*xi_j - 1/2 mod h  (xi_j = num/L)
    X=((h*(2*sub-L))//(2*L))%h ; assert np.all((h*(2*sub-L))%(2*L)==0)
    # check recursion x_{j+1} = 6x_j - x_{j-1}
    assert np.all((X[:,2:]-6*X[:,1:-1]+X[:,:-2])%h==0)
    r=(X[:,0]**2-6*X[:,0]*X[:,1]+X[:,1]**2)%h
    Kmat=(allk.T@allk.conj())/len(M.units)*h*h
    maxerr=0; vals=set()
    for ii in range(P):
        for jj in range(P):
            q=h//math.gcd(int(r[pick[ii]]-r[pick[jj]]),h)
            pred=float(mobius(q))/float(totient(q))
            maxerr=max(maxerr,abs(Kmat[ii,jj]-pred)); vals.add(round(pred,12))
    print(f'  Prop K/C: h^2 K(xi,xi\') = mu(q)/phi(q), q=h/gcd(r-r\',h): max err over {P}^2 pairs, all {len(M.units)} units = {maxerr:.2e}; distinct values {sorted(vals)[:6]}')
    print(f'  B^sym = {Bsym:.8f}   2m = {2*m}   time {time.time()-t0:.1f}s',flush=True)
for m in [int(x) for x in sys.argv[1].split(',')]: run(m)
