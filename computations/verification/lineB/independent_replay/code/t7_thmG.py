"""Theorem G prediction M4/B^2 = 2 - sum_o w_o^2 / B^2, w_o=|o|^2/D_eff, from own orbit enumeration on the support (x-coordinates)."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import numpy as np, math, sys
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__))); from core import hm
for m in [3,5,7]:
    h=math.isqrt(hm(m))//2
    x0,x1=np.meshgrid(np.arange(h),np.arange(h),indexing='ij'); x0=x0.ravel(); x1=x1.ravel()
    seq=[x0,x1]
    for j in range(2,m): seq.append((6*seq[-1]-seq[-2])%h)
    seq=np.array(seq).T
    assert np.all((6*seq[:,-1]-seq[:,-2])%h==seq[:,0]%h)
    canon=np.full(len(x0),np.iinfo(np.int64).max)
    for g in range(2*m):
        img=np.roll(seq,g%m,axis=1) if g<m else np.roll(seq[:,::-1],g%m,axis=1)
        c=img[:,0].astype(np.int64)*h+img[:,1]; canon=np.minimum(canon,c)
    _,sizes=np.unique(canon,return_counts=True)
    w=sizes.astype(float)**2/h**2; B=w.sum()
    print(f'm={m}: #orbits={len(sizes)} B^sym={B:.6f} M4/B^2 predicted = {2-np.sum(w**2)/B**2:.6f}')
