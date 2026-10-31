"""N12b shared: N12 sector-4 operator in adapted coordinates v~ = T v:  M(t) = T A(t) T^{-1} / s,  ||M(t)||_2 = N_H(t).
Twist-pair map F(y0,y1) = (y1, 6 y1 - y0) mod 1; step i uses t = y0 (first coordinate). Closed box: max(|y0|,|y1|)_T <= TH around (0,0)."""
import sys, json, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N12/code'); import a_ops as A
NPZ='/workspace/bgs-lineN/N12/logs/adapted_norm_t0.0_k0.45.npz'
z=np.load(NPZ); T=z['T']; s=complex(z['s']); Ti=np.linalg.inv(T); MU=abs(s)
TM=np.array([T@Mk@Ti for Mk in A.MS])/s; NS=A.NS; C0=A.COEF0
def M(t): return np.tensordot(C0*np.exp(2j*np.pi*NS*t),TM,1)
def dM(t): return np.tensordot(C0*(2j*np.pi*NS)*np.exp(2j*np.pi*NS*t),TM,1)
def td(x): x=np.mod(x,1.0); return np.minimum(x,1-x)
def inbox(y,TH): return max(td(y[0]),td(y[1]))<=TH
def F(y): return np.array([y[1],(6*y[1]-y[0])%1])
TP=1.4279
