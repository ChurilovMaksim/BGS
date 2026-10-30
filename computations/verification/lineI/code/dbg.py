import time,numpy as np
t=time.time()
from law import kick_ghat
from twist import build
gh=kick_ghat('k1',2.0,10); print('import',time.time()-t,flush=True)
parts,nu,S=build(9,2,8,gh,2.6,30); print('build',time.time()-t,flush=True)
A=np.random.rand(480,480)+0j; np.linalg.eigvals(A); print('eig',time.time()-t,flush=True)
