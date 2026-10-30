"""INDEPENDENT physical trace for the FULL fixed diagonal kick (14 nonzero modes, Line B coefficients via dlib CK)
 at N = h_m - 196 (i.e. N = -4*49 mod h_m: the Galois image nu = 49^{-1} nu* of the resonant residue for the dominant mode 7).
 Usage: indep_trace_full.py m eta batch [Noffset]"""
import numpy as np, sys, time, json
import os
_here=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(_here,'..','..','lineB','common'))
from model import fCoeff                      # Line B kick coefficients (vendored path, referee fix F7)
CK={k: fCoeff(k,0) for k in range(-9,10) if abs(fCoeff(k,0))>0}   # identical to lineB/phase1/dlib.py CK
def fvals(q):
    out=np.zeros_like(q,dtype=complex)
    for k,c in CK.items(): out+=c*np.exp(2j*np.pi*k*q)
    return out.real
def hm(m):
    a,b=1,7
    for _ in range((m-3)//2): a,b=b,6*b-a
    return b
m=int(sys.argv[1]); eta=float(sys.argv[2]); B=int(sys.argv[3]); off=int(sys.argv[4]) if len(sys.argv)>4 else 196
h=hm(m); N=h-off
if N%2==0: N+=h
x=np.arange(N); i8=pow(8,-1,N); i4=pow(4,-1,N)
chirp=np.exp(-2j*np.pi*((3*i8*(x*x % N)) % N)/N); perm=(i4*x) % N
kick=np.exp(1j*eta*fvals(x/N))
def applyU(V):
    W=chirp[:,None]*V; F=np.fft.ifft(W,axis=0)*N
    return kick[:,None]*(F[perm,:]*chirp[:,None]/np.sqrt(N))
t0=time.time(); tr=0j
for s in range(0,N,B):
    b=min(B,N-s); V=np.zeros((N,b),complex); V[np.arange(s,s+b),np.arange(b)]=1
    for _ in range(m): V=applyU(V)
    tr+=np.sum(V[np.arange(s,s+b),np.arange(b)])
r=dict(kick='full',m=m,eta=eta,N=N,h=h,offset=off,abs2=abs(tr)**2,secs=time.time()-t0)
print(json.dumps(r),flush=True); open(os.path.join(_here,'indep_trace.jsonl'),'a').write(json.dumps(r)+'\n')
