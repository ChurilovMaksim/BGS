"""Which constant q-sequences (fixed points of S: theta in {0,1/4,1/2,3/4}) lie in the support S_m; is 0 in S_m?"""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from p2lib import *
for m in range(1,10):
    O,supp=support_data(m); d2=O.d2
    T=O.T.reshape(m,-1); s=supp.ravel()
    const=np.all(T==T[0],axis=0)
    th=sorted(set((T[0][const & s]*4//d2).tolist()))   # theta*4
    zero=bool(s[np.flatnonzero(np.all(T==0,axis=0))[0]])
    print(f'm={m} D={O.D} fixed points of S in support: theta in {[f"{t}/4" for t in th]}  0 in support: {zero}',flush=True)
