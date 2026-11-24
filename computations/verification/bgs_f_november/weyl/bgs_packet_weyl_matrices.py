"""Check exact finite formulae via two independently assembled representations."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import numpy as np, scipy.linalg as la,json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'research'))
from coefficients import raw_symbol
def one(N,xi):
    x=np.arange(N);q=x/N
    def phase(t):return np.exp(2j*np.pi*(t%N)/N)
    def r(q):return (1-np.cos(14*np.pi*q))*(1+np.cos(2*np.pi*q))
    A=np.diag(np.cos(14*np.pi*q)-.1+r(q)*(.1+.01*np.sin(2*np.pi*q))).astype(complex)
    off=(-3-4j)*r(((x+pow(2,-1,N))%N)/N)/1000
    A[x,(x+1)%N]+=off;A[(x+1)%N,x]+=off.conj()
    X,Y=np.meshgrid(x,x,indexing='ij')
    M=phase(-pow(8,-1,N)*(3*X**2-2*X*Y+3*Y**2))/np.sqrt(N)
    U=la.expm(1j*xi*A)@M
    ix=lambda a,b:(a%N)*N+b%N
    W0=np.zeros((N*N,N*N),complex);S=W0.copy();gs=W0.copy()
    for a in range(N):
        for b in range(N):
            j=ix(a,b);S[ix(3*a+4*b,2*a+3*b),j]=1
            for (k,l),(re,im) in raw_symbol().items():
                w=k*b-l*a
                gs[ix(a+k,b+l),j]+=-2*xi*complex(re,im)/4000*np.sin(2*np.pi*((pow(2,-1,N)*w)%N)/N)
            T=np.zeros((N,N),complex);T[x,(x+a)%N]=phase(b*(x+pow(2,-1,N)*a))
            T=U@T@U.conj().T
            for d in range(N):
                W0[d*N:(d+1)*N,j]=np.fft.fft(T[x,(x+d)%N])/N*phase(-x*pow(2,-1,N)*d)
    W=la.expm(gs)@S
    gin=float(np.max(abs(W-W0)));assert gin<2e-13
    # Choose a larger test box on these small sizes to exercise the Schur complement.
    low=[j for j in range(1,N*N) if (j%3!=0 and j%5!=0)];high=[j for j in range(1,N*N) if j not in low]
    K=W[np.ix_(low,low)];B=W[np.ix_(low,high)];C=W[np.ix_(high,low)];D=W[np.ix_(high,high)]
    z=.62+.18j;R=la.inv(np.eye(len(low))-z*K);Sx=D+z*C@R@B
    delta=np.linalg.det(np.eye(N*N-1)-z*W[1:,1:])-np.linalg.det(np.eye(len(low))-z*K)*np.linalg.det(np.eye(len(high))-z*Sx)
    defect=np.eye(len(high))-Sx.conj().T@Sx-(1-abs(z)**2)*(R@B).conj().T@(R@B)
    assert abs(delta)<2e-11 and la.norm(defect,2)<2e-13
    # Compare generating-log coefficient to enumeration of all circular patterns or a direct DP.
    m=7;T=2; lifted=[np.linalg.matrix_power(K,t) for t in range(T)]
    acts=[(1,D)]+[(t+2,C@lifted[t]@B) for t in range(T)]
    def series(left,count,op):
        if left==0:return m/count*np.trace(op)
        return sum((series(left-d,count+1,op@V) for d,V in acts if d<=left),0j)
    from itertools import product
    mask_sum=0j
    for seq in product((0,1),repeat=m):
        if 1 not in seq or '0'*(T+1) in ''.join(map(str,seq*2)):continue
        inds=[(high if a else low) for a in seq]
        mat=np.eye(len(inds[0]),dtype=complex)
        for j in range(m):mat=mat@W[np.ix_(inds[j],inds[(j+1)%m])]
        mask_sum+=np.trace(mat)
    diff=abs(mask_sum-series(m,0,np.eye(len(high))))
    assert diff<2e-11
    return dict(N=N,xi=xi,adjoint_error=gin,det_error=float(abs(delta)),defect_error=float(la.norm(defect,2)),word_count_error=float(diff))
print(json.dumps([one(5,.38),one(7,.21),one(9,.59)],indent=2))
