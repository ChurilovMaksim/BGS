"""Auditor's direct physical trace Tr (K M_N)^m (dense matrices, Line B / TRACE-163 conventions) at N = h_m - 4,
compared with the E1/E2 finite-N prediction (c -> c(1+4/N)) from the auditor's transfer operator."""
import sys,json,numpy as np; sys.path.insert(0,'.')
from aud import *; from tmop import *
eta=2.0; G=ghat(K1,eta)
for m in map(int,sys.argv[1].split(',')):
    h=data(m)['h']; N=h-4; assert N%2==1 and math.gcd(N,data(m)['D'])==1
    x=np.arange(N); i8=pow(8,-1,N)
    ph=(-i8*((3*x[:,None]**2-2*x[:,None]*x[None,:]+3*x[None,:]**2)%N))%N
    M=np.exp(2j*np.pi*ph/N)/np.sqrt(N); del ph
    U=np.exp(1j*eta*fvals(K1,x/N))[:,None]*M
    TM=np.trace(np.linalg.matrix_power(M,m)); TU=np.trace(np.linalg.matrix_power(U,m))
    sp=spectra(G,10,2.6,140,c=C0*(1+4/N)); zp=Zpred(m,sp)
    r=dict(m=m,N=N,absTrM=abs(TM),TU2=abs(TU)**2,pred2=abs(zp)**2,rel=abs(abs(zp)**2/abs(TU)**2-1),ratio_phase_diff=abs(TU/TM-zp))
    print(json.dumps(r),flush=True)
