"""Theorem 2 check (fast): exact quantum |Tr U_N^m|^2, m=1..5, via matrix products (no eigensolver), fixed diagonal kick,
over admissible N in a window; compare with F_m(eta)=avg_nu|Z_m(nu)|^2 and the same-sample avg of |Z_m(N^{-1} mod g')|^2.
Uses |Tr M^m|=1 (Theorem 1(b)), which is also checked."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import dlib, numpy as np, math, sys
eta=float(sys.argv[1]); lo=int(sys.argv[2]); hi=int(sys.argv[3]); step=int(sys.argv[4])
ms=[1,2,3,4,5]; Os={m:dlib.Orbits(m) for m in ms}; Z={m:Os[m].Z_all(eta) for m in ms}; Fm={m:Os[m].F(eta)[0] for m in ms}
def traces(A):
    A2=A@A; A4=A2@A2
    return {1:np.trace(A),2:np.trace(A2),3:np.sum(A2*A.T),4:np.sum(A2*A2.T),5:np.sum(A4*A.T)}
acc={m:[] for m in ms}; accZ={m:[] for m in ms}; worstM=0
for N in range(lo,hi,step):
    if N%2==0: continue
    M=dlib.MN(N); x=np.arange(N); K=np.exp(1j*eta*dlib.f_diag(x/N))
    tU=traces(K[:,None]*M); tM=traces(M)
    for m in ms:
        if math.gcd(N,dlib.Dm(m))!=1: continue
        worstM=max(worstM,abs(abs(tM[m])-1))
        gp,yp=dlib.gprime(m); acc[m].append(abs(tU[m])**2); accZ[m].append(abs(Z[m][pow(N,-1,gp)])**2)
print(f'# eta={eta} odd N in [{lo},{hi}) step {step}; max over N,m of ||TrM^m|-1| = {worstM:.1e}')
for m in ms:
    a=np.array(acc[m]); b=np.array(accZ[m])
    print(f'm={m} #N={len(a)} avg|TrU^m|^2={a.mean():.4f} (se {a.std()/math.sqrt(len(a)):.4f})  same-sample avg|Z(nu_N)|^2={b.mean():.4f}  F_m(eta)={Fm[m]:.4f}  '
          f'RMS(|TrU|^2-|Z(nu_N)|^2)={np.sqrt(np.mean((a-b)**2)):.4f}',flush=True)
