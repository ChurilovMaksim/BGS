"""Independent audit of BGS-TRACE-126 (PR #46). Own construction (from bgs-recon/code/model.py conventions)."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import numpy as np, sys
from fractions import Fraction as F
sys.path.insert(0,__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','common'))
from model import MN, weylT, fCoeff, rCoeff

def eN(N,t): return np.exp(2j*np.pi*(np.asarray(t)%N)/N)

# exact rational coefficients
def rC(k): return {0:F(1),1:F(1,2),-1:F(1,2),7:F(-1,2),-7:F(-1,2),6:F(-1,4),-6:F(-1,4),8:F(-1,4),-8:F(-1,4)}.get(k,F(0))
def cEx(k,l):
    if l==0:
        re=(F(1,2) if abs(k)==7 else 0)+rC(k)/10-(F(1,10) if k==0 else 0)
        im=-(rC(k-1)-rC(k+1))/200   # 1/(200 i) = -i/200
        return (F(re),F(im))
    if l==1: return (rC(k)*F(-3,1000), rC(k)*F(-4,1000))
    if l==-1: return (rC(k)*F(-3,1000), rC(k)*F(4,1000))
    return (F(0),F(0))
MODES=[]   # v=(a,b)=(l,k) T-label, complex coeff, exact
for k in range(-9,10):
    for l in (-1,0,1):
        re,im=cEx(k,l)
        if re or im:
            MODES.append(((l,k),complex(re,im),(re,im)))
            assert abs(complex(re,im)-fCoeff(k,l))<1e-15
assert len(MODES)==32
CO={v:c for v,c,_ in MODES}
PAIRS=[]; seen=set()
for v,c,_ in MODES:
    if v in seen: continue
    w=(-v[0],-v[1]); assert w in CO and abs(CO[w]-np.conj(c))<1e-15
    PAIRS.append((v,w)); seen|={v,w}
assert len(PAIRS)==16
S=np.array([[3,4],[2,3]])

def Tmats(N): return {v:weylT(N,v[0]%N,v[1]%N) for v in CO}
def A_phi(N,Ts,phi):
    A=np.zeros((N,N),complex)
    for r,(v,w) in enumerate(PAIRS):
        A+=CO[v]*np.exp(1j*phi[r])*Ts[v]+CO[w]*np.exp(-1j*phi[r])*Ts[w]
    return A
def matpow_mod(Mt,m,N):
    R=np.eye(2,dtype=object); B=np.array(Mt,dtype=object)
    for _ in range(m): R=R.dot(B)%N
    return R
def ker_size(N,m):
    R=(matpow_mod(S,m,N)-np.eye(2,dtype=object))%N
    cnt=0
    for a in range(N):
        for b in range(N):
            if (R[0,0]*a+R[0,1]*b)%N==0 and (R[1,0]*a+R[1,1]*b)%N==0: cnt+=1
    return cnt
def order(N):
    m=1
    while not (matpow_mod(S,m,N)%N==np.eye(2,dtype=object)).all(): m+=1
    return m
