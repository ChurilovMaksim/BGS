"""Independent numerical check at N=343, using a dilation eigenbasis."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')


from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
from scipy.linalg import eigvals

from resolvent.bgs_packet_check import PRIMITIVE_BOUND, NONPRIMITIVE_BOUND
from spectrum.bgs_packet_check import rho_at, split, COEFFICIENTS

N=343
m=3*N//7
rho=rho_at(3)
gamma=(3+2*rho)%N
vectors=[]; labels=[]
seen=set()
for x in range(N):
    if x in seen:
        continue
    cyc=[]
    y=x
    while y not in seen:
        seen.add(y); cyc.append(y); y=y*gamma%N
    for j in range(len(cyc)):
        col=np.zeros(N,complex)
        col[cyc]=np.exp(-2j*np.pi*j*np.arange(len(cyc))/len(cyc))/np.sqrt(len(cyc))
        vectors.append(col);labels.append(j*(m//len(cyc)))
V=np.array(vectors).T
labels=np.array(labels)
assert np.max(abs(V.conj().T@V-np.eye(N)))<1e-11
differences=np.subtract.outer(labels,labels)%m
x=np.arange(N)
X=np.zeros((N,N),complex)
for raw,(r,i) in COEFFICIENTS.items():
    a,b=split(raw,rho,N)
    phase=(b*(x+pow(2,-1,N)*a))%N
    X+=(r+1j*i)/4000*np.exp(2j*np.pi*phase[:,None]/N)*V[(x+a)%N,:]
A=V.conj().T@X
W_h=np.bincount(differences.ravel(),weights=np.abs(A).ravel()**2)
bound=N/m*(float(PRIMITIVE_BOUND)+float(NONPRIMITIVE_BOUND)*(np.arange(m)%7==0))
assert np.max(W_h-bound)<1e-10
time=1e-3  # Auxiliary parameter visible at machine precision.
radius=0.35
lambdas=np.exp(2j*np.pi*labels/m)
a,Q=np.linalg.eigh(A)
expA=(Q*np.exp(1j*time*a))@Q.conj().T
delta=(expA-np.eye(N))*lambdas
spectrum=eigvals(expA*lambdas)
true=0
for center in range(m):
    d=(labels-center)%m
    d=np.minimum(d,m-d)
    w=np.where(d==0,1/radius,1/(2*m*np.sin(np.pi*d/m)-radius))
    B=m*(np.sqrt(w[:,None]*w[None,:]))*delta
    if np.linalg.norm(B)<1:
        lam=np.exp(2j*np.pi*center/m)
        assert np.sum(np.abs(spectrum-lam)<radius/m)==np.sum(labels==center)
        true+=1
assert true>0
print(f"Independent direct matrix check: all {m} spectral-difference bounds, {true} good contour counts.")
