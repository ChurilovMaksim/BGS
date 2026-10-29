"""Theorem 1(c) rate check at large N via the (proved, quantum-verified) exact Pell-norm sum, m=1,2,3:
|Z_N - Z_m(N^{-1} mod g')| * N should stay bounded (O(1/N)) and below pi m s2 s0^{m-1}."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import numpy as np, math, dlib, importlib.util
spec=importlib.util.spec_from_file_location('ve','verify_exact.py')
src=open('verify_exact.py').read(); src=src[:src.index("print('== (1)")]   # import helper only
ns={}; exec(src.replace('','')+open('verify_exact.py').read().split("print('== (2) exact finite-N formula vs quantum ==')")[1].split('for eta in')[0],ns)
exact_sum=ns['exact_sum']
for eta in [0.5,1.0]:
    n,gh=dlib.ghat(eta); a=np.abs(gh); s0=a.sum(); s2=(a*n.astype(float)**2).sum()
    for m in [1,2,3]:
        Zl=dlib.Orbits(m).Z_all(eta); gp,_=dlib.gprime(m)
        for N in [1001,10001,100001,1000001,10000001]:
            if math.gcd(N,dlib.Dm(m))!=1: N+=2
            if math.gcd(N,dlib.Dm(m))!=1: N+=2
            zs=exact_sum(N,m,eta,1e-14 if m<3 else 1e-11); zl=Zl[pow(N,-1,gp)]
            print(f'eta={eta} m={m} N={N} nu={pow(N,-1,gp)} |Z_N-Z(nu)|={abs(zs-zl):.3e} N*|diff|={N*abs(zs-zl):.2f} bound*N={math.pi*m*s2*s0**(m-1):.1f}',flush=True)
